"""Tests for the CLI (browsertrace list / show / export)."""

from __future__ import annotations

import json
import py_compile
import sqlite3
from pathlib import Path
from io import StringIO
from contextlib import redirect_stderr, redirect_stdout

import pytest

from browsertrace import Tracer


@pytest.fixture
def cli(tmp_path, monkeypatch):
    """Reload the CLI module bound to an isolated BROWSERTRACE_HOME."""
    monkeypatch.setenv("BROWSERTRACE_HOME", str(tmp_path))
    import importlib
    import browsertrace.cli as cli_mod
    importlib.reload(cli_mod)
    return cli_mod, tmp_path


def _seed(tmp_path, name, fail=False):
    tracer = Tracer(home=tmp_path)
    if fail:
        try:
            with tracer.run(name) as run:
                run.step(action="step 0", url="https://example.com")
                run.step(action="step 1", url="https://example.com/x")
                raise RuntimeError("intentional")
        except RuntimeError:
            pass
    else:
        with tracer.run(name) as run:
            run.step(action="step 0")
    return run.id


def _seed_compare_runs(tmp_path):
    tracer = Tracer(home=tmp_path)

    with tracer.run("browser-use success") as run:
        run.step(
            action="navigate",
            url="https://example.com/start",
            model_output={"thought": "open start"},
        )
        run.step(
            action="click(selector=#checkout)",
            url="https://example.com/done",
            model_output={"result": "checkout complete"},
        )
        success_id = run.id

    try:
        with tracer.run("browser-use failure") as run:
            run.step(
                action="navigate",
                url="https://example.com/start",
                model_output={"thought": "open start"},
            )
            run.step(
                action="click(selector=#cancel)",
                url="https://example.com/cart",
                status="error",
                error="wrong target",
                model_output={"result": "cancelled"},
            )
            failed_id = run.id
            raise RuntimeError("wrong target")
    except RuntimeError:
        pass

    return failed_id, success_id


def test_cli_module_compiles_on_python311():
    """Guard against Python 3.11 f-string syntax regressions.

    The package supports Python 3.11, so CLI source must parse on 3.11 before
    any import-time tests can run.
    """
    root = Path(__file__).resolve().parents[1]
    py_compile.compile(str(root / "browsertrace" / "cli.py"), doraise=True)


def test_cli_list_prints_recent_runs(cli):
    cli_mod, tmp_path = cli
    _seed(tmp_path, "first")
    _seed(tmp_path, "second")
    buf = StringIO()
    with redirect_stdout(buf):
        rc = cli_mod.main(["list"])
    out = buf.getvalue()
    assert rc == 0
    assert "first" in out
    assert "second" in out
    assert not out.lstrip().startswith("[")


def test_cli_list_json_prints_recent_runs_as_json(cli):
    cli_mod, tmp_path = cli
    first_id = _seed(tmp_path, "first")
    second_id = _seed(tmp_path, "second", fail=True)
    buf = StringIO()
    with redirect_stdout(buf):
        rc = cli_mod.main(["list", "--json"])

    runs = json.loads(buf.getvalue())
    by_id = {run["id"]: run for run in runs}

    assert rc == 0
    assert {first_id, second_id} <= set(by_id)
    assert by_id[first_id]["name"] == "first"
    assert by_id[first_id]["status"] == "completed"
    assert by_id[second_id]["name"] == "second"
    assert by_id[second_id]["status"] == "failed"
    assert isinstance(by_id[first_id]["created_at"], float)


def test_cli_list_status_filter_prints_matching_human_runs(cli):
    cli_mod, tmp_path = cli
    _seed(tmp_path, "completed-run")
    _seed(tmp_path, "failed-run", fail=True)
    buf = StringIO()
    with redirect_stdout(buf):
        rc = cli_mod.main(["list", "--status", "failed"])

    out = buf.getvalue()

    assert rc == 0
    assert "failed-run" in out
    assert "completed-run" not in out


def test_cli_list_status_filter_applies_to_json_output(cli):
    cli_mod, tmp_path = cli
    completed_id = _seed(tmp_path, "completed-run")
    _seed(tmp_path, "failed-run", fail=True)
    buf = StringIO()
    with redirect_stdout(buf):
        rc = cli_mod.main(["list", "--status", "completed", "--json"])

    runs = json.loads(buf.getvalue())

    assert rc == 0
    assert [run["id"] for run in runs] == [completed_id]
    assert runs[0]["name"] == "completed-run"
    assert runs[0]["status"] == "completed"


def test_cli_show_prints_steps_and_url(cli):
    cli_mod, tmp_path = cli
    rid = _seed(tmp_path, "showme", fail=True)
    buf = StringIO()
    with redirect_stdout(buf):
        rc = cli_mod.main(["show", rid[:8]])  # short prefix should also work
    out = buf.getvalue()
    assert rc == 0
    assert "showme" in out
    assert "step 0" in out
    assert "https://example.com" in out
    assert not out.lstrip().startswith("{")


def test_cli_show_json_prints_run_and_steps_as_json(cli):
    cli_mod, tmp_path = cli
    rid = _seed(tmp_path, "show-json", fail=True)
    buf = StringIO()
    with redirect_stdout(buf):
        rc = cli_mod.main(["show", rid[:8], "--json"])

    payload = json.loads(buf.getvalue())

    assert rc == 0
    assert payload["run"]["id"] == rid
    assert payload["run"]["name"] == "show-json"
    assert payload["run"]["status"] == "failed"
    assert payload["run"]["error"] == "RuntimeError: intentional"
    assert [step["action"] for step in payload["steps"]] == ["step 0", "step 1"]
    assert payload["steps"][0]["step_index"] == 0
    assert payload["steps"][0]["url"] == "https://example.com"
    assert payload["steps"][0]["status"] == "ok"


def test_cli_compare_json_reports_first_divergent_step(cli):
    cli_mod, tmp_path = cli
    failed_id, success_id = _seed_compare_runs(tmp_path)

    buf = StringIO()
    with redirect_stdout(buf):
        rc = cli_mod.main(["compare", failed_id[:8], success_id[:8], "--json"])

    payload = json.loads(buf.getvalue())

    assert rc == 0
    assert payload["left"]["id"] == failed_id
    assert payload["left"]["status"] == "failed"
    assert payload["right"]["id"] == success_id
    assert payload["right"]["status"] == "completed"
    assert payload["first_divergence"]["step_index"] == 1
    assert payload["first_divergence"]["left_step"]["action"] == "click(selector=#cancel)"
    assert payload["first_divergence"]["right_step"]["action"] == "click(selector=#checkout)"
    assert payload["first_divergence"]["fields"]["action"] == {
        "left": "click(selector=#cancel)",
        "right": "click(selector=#checkout)",
    }
    assert payload["first_divergence"]["fields"]["url"] == {
        "left": "https://example.com/cart",
        "right": "https://example.com/done",
    }
    assert payload["first_divergence"]["fields"]["error"] == {
        "left": "wrong target",
        "right": None,
    }


def test_cli_compare_human_output_mentions_first_divergence(cli):
    cli_mod, tmp_path = cli
    failed_id, success_id = _seed_compare_runs(tmp_path)

    buf = StringIO()
    with redirect_stdout(buf):
        rc = cli_mod.main(["compare", failed_id[:8], success_id[:8]])

    out = buf.getvalue()

    assert rc == 0
    assert "First divergence at step 1" in out
    assert "action:" in out
    assert "click(selector=#cancel)" in out
    assert "click(selector=#checkout)" in out
    assert not out.lstrip().startswith("{")


def test_cli_compare_json_reports_no_divergence_for_same_run(cli):
    cli_mod, tmp_path = cli
    run_id = _seed(tmp_path, "same-run")

    buf = StringIO()
    with redirect_stdout(buf):
        rc = cli_mod.main(["compare", run_id, run_id, "--json"])

    payload = json.loads(buf.getvalue())

    assert rc == 0
    assert payload["first_divergence"] is None
    assert payload["step_counts"] == {"left": 1, "right": 1}


def test_cli_show_unknown_run_id_returns_2(cli):
    cli_mod, _ = cli
    # Need a real DB file or _open() will exit 1, so seed an empty one.
    Tracer(home=cli[1])
    rc = cli_mod.main(["show", "nonexistent-id"])
    assert rc == 2


def test_cli_export_ambiguous_run_id_prefix_returns_2(cli, tmp_path):
    cli_mod, home = cli
    Tracer(home=home)
    with sqlite3.connect(home / "db.sqlite") as conn:
        conn.execute(
            "INSERT INTO runs (id, name, status, started_at) VALUES (?, ?, ?, ?)",
            ("abcdef01-0000-0000-0000-000000000000", "first", "completed", 1.0),
        )
        conn.execute(
            "INSERT INTO runs (id, name, status, started_at) VALUES (?, ?, ?, ?)",
            ("abcdef02-0000-0000-0000-000000000000", "second", "completed", 2.0),
        )

    err = StringIO()
    out_file = tmp_path / "public.html"
    with redirect_stderr(err):
        rc = cli_mod.main(["export", "abcdef", "--public", "-o", str(out_file)])

    assert rc == 2
    assert "More than one run matching 'abcdef'" in err.getvalue()
    assert not out_file.exists()


def test_cli_export_writes_html_with_inlined_screenshots(cli, tmp_path):
    cli_mod, home = cli
    tracer = Tracer(home=home)
    png = b"\x89PNG\r\n\x1a\n" + b"\x00" * 16
    with tracer.run("export-me") as run:
        run.step(action="snap", screenshot=png)

    out_file = tmp_path / "out.html"
    rc = cli_mod.main(["export", run.id, "-o", str(out_file)])
    assert rc == 0
    body = out_file.read_text()
    assert body.startswith("<!doctype html><html lang='en'><head><meta charset='utf-8'>")
    assert "<meta name='viewport' content='width=device-width, initial-scale=1'>" in body
    assert "@media(max-width:720px){body{padding:14px}.step{grid-template-columns:1fr}}" in body
    assert "export-me" in body
    assert "data:image/png;base64" in body  # screenshot inlined


def test_cli_export_writes_model_input_and_output(cli, tmp_path):
    cli_mod, home = cli
    tracer = Tracer(home=home)
    with tracer.run("model-io") as run:
        run.step(
            action="choose button",
            model_input={"prompt": "Which checkout button should I click?"},
            model_output={"selector": "button.checkout.primary"},
        )

    out_file = tmp_path / "model-io.html"
    rc = cli_mod.main(["export", run.id, "-o", str(out_file)])

    assert rc == 0
    body = out_file.read_text()
    assert "Model input" in body
    assert "Which checkout button should I click?" in body
    assert "Model output" in body
    assert "button.checkout.primary" in body


def test_cli_export_redact_hides_model_io(cli, tmp_path):
    cli_mod, home = cli
    tracer = Tracer(home=home)
    with tracer.run("sensitive-export") as run:
        run.step(
            action="ask model",
            model_input={"prompt": "private checkout token sk-browsertrace-test"},
            model_output={"selector": "#pay-now", "reason": "private model answer"},
        )

    out_file = tmp_path / "redacted.html"
    rc = cli_mod.main(["export", run.id, "--redact", "-o", str(out_file)])

    assert rc == 0
    body = out_file.read_text()
    assert "private checkout token" not in body
    assert "private model answer" not in body
    assert "Model I/O redacted" in body


def test_cli_export_redact_screenshots_omits_inlined_images(cli, tmp_path):
    cli_mod, home = cli
    tracer = Tracer(home=home)
    png = b"\x89PNG\r\n\x1a\n" + b"\x00" * 16
    with tracer.run("screenshot-redaction") as run:
        run.step(action="visible private page", screenshot=png)

    out_file = tmp_path / "redacted-screenshots.html"
    rc = cli_mod.main(["export", run.id, "--redact-screenshots", "-o", str(out_file)])

    assert rc == 0
    body = out_file.read_text()
    assert "data:image/png;base64" not in body
    assert "Screenshot redacted" in body


def test_cli_export_redact_urls_omits_step_urls(cli, tmp_path):
    cli_mod, home = cli
    tracer = Tracer(home=home)
    with tracer.run("url-redaction") as run:
        run.step(
            action="open private page",
            url="https://internal.example.test/account?token=secret-token",
        )

    out_file = tmp_path / "redacted-urls.html"
    rc = cli_mod.main(["export", run.id, "--redact-urls", "-o", str(out_file)])

    assert rc == 0
    body = out_file.read_text()
    assert "internal.example.test" not in body
    assert "secret-token" not in body
    assert "URL redacted" in body


def test_cli_export_public_redacts_model_io_screenshots_and_urls(cli, tmp_path):
    cli_mod, home = cli
    tracer = Tracer(home=home)
    png = b"\x89PNG\r\n\x1a\n" + b"\x00" * 16
    with tracer.run("public-export") as run:
        run.step(
            action="open private checkout",
            url="https://internal.example.test/account?token=secret-token",
            screenshot=png,
            model_input={"prompt": "private prompt"},
            model_output={"answer": "private answer"},
        )

    out_file = tmp_path / "public.html"
    rc = cli_mod.main(["export", run.id, "--public", "-o", str(out_file)])

    assert rc == 0
    body = out_file.read_text()
    assert "private prompt" not in body
    assert "private answer" not in body
    assert "internal.example.test" not in body
    assert "secret-token" not in body
    assert "data:image/png;base64" not in body
    assert "Model I/O redacted" in body
    assert "Screenshot redacted" in body
    assert "URL redacted" in body


def test_cli_demo_creates_failed_demo_run(cli):
    cli_mod, home = cli
    buf = StringIO()

    with redirect_stdout(buf):
        rc = cli_mod.main(["demo"])

    assert rc == 0
    out = buf.getvalue()
    assert "demo: Browser Use local HTML upload navigation failure" in out
    assert "browsertrace" in out

    with sqlite3.connect(home / "db.sqlite") as conn:
        run = conn.execute(
            "SELECT id, status, error FROM runs WHERE name=?",
            ("demo: Browser Use local HTML upload navigation failure",),
        ).fetchone()
        assert run is not None
        assert run[1] == "failed"
        assert "Browser Use navigated away from the upload page" in run[2]
        steps = conn.execute(
            "SELECT COUNT(*) FROM steps WHERE run_id=?",
            (run[0],),
        ).fetchone()[0]
    assert steps == 4


def test_cli_doctor_reports_missing_database_without_failing(cli):
    cli_mod, home = cli
    buf = StringIO()

    with redirect_stdout(buf):
        rc = cli_mod.main(["doctor"])

    out = buf.getvalue()
    assert rc == 0
    assert "BrowserTrace doctor" in out
    assert not out.lstrip().startswith("{")
    assert f"Home: {home}" in out
    assert "Database: missing" in out
    assert "Next: browsertrace demo" in out


def test_cli_doctor_json_reports_missing_database(cli):
    cli_mod, home = cli
    buf = StringIO()

    with redirect_stdout(buf):
        rc = cli_mod.main(["doctor", "--json"])

    payload = json.loads(buf.getvalue())

    assert rc == 0
    assert payload["home"] == str(home)
    assert payload["database"]["exists"] is False
    assert payload["database"]["readable"] is False
    assert payload["database"]["runs"] == 0
    assert payload["database"]["steps"] == 0
    assert payload["ui_dependencies"]["available"] is True
    assert payload["ui_dependencies"]["missing"] == []
    assert payload["next"] == "browsertrace demo"


def test_cli_doctor_json_reports_existing_database_counts(cli):
    cli_mod, home = cli
    _seed(home, "doctor-json")
    buf = StringIO()

    with redirect_stdout(buf):
        rc = cli_mod.main(["doctor", "--json"])

    payload = json.loads(buf.getvalue())

    assert rc == 0
    assert payload["database"]["exists"] is True
    assert payload["database"]["readable"] is True
    assert payload["database"]["path"] == str(home / "db.sqlite")
    assert payload["database"]["runs"] == 1
    assert payload["database"]["steps"] == 1
    assert payload["next"] == "browsertrace"


def test_cli_doctor_json_reports_unreadable_database(cli):
    cli_mod, home = cli
    (home / "db.sqlite").write_text("not sqlite", encoding="utf-8")
    buf = StringIO()

    with redirect_stdout(buf):
        rc = cli_mod.main(["doctor", "--json"])

    payload = json.loads(buf.getvalue())

    assert rc == 0
    assert payload["database"]["exists"] is True
    assert payload["database"]["readable"] is False
    assert payload["database"]["runs"] == 0
    assert payload["database"]["steps"] == 0
    assert payload["database"]["error"]
    assert payload["next"] == "remove or move the database, then run browsertrace demo"


def test_cli_doctor_missing_ui_deps_points_to_pypi_ui_install(cli, monkeypatch):
    cli_mod, _ = cli
    import importlib.util

    original_find_spec = importlib.util.find_spec

    def fake_find_spec(name):
        if name in {"fastapi", "uvicorn", "jinja2"}:
            return None
        return original_find_spec(name)

    monkeypatch.setattr(importlib.util, "find_spec", fake_find_spec)

    buf = StringIO()
    with redirect_stdout(buf):
        rc = cli_mod.main(["doctor"])

    out = buf.getvalue()
    assert rc == 0
    assert "UI dependencies: missing fastapi, uvicorn, jinja2" in out
    assert 'Install: pip install "browsertrace[ui]"' in out
    assert "git+https://github.com/aaronlab/browsertrace" not in out


def test_cli_no_args_routes_to_serve(cli, monkeypatch):
    """`browsertrace` with no args should call serve."""
    cli_mod, _ = cli

    called = {"v": False}
    def fake_serve():
        called["v"] = True
    monkeypatch.setattr("browsertrace.server.main", fake_serve)
    cli_mod.main([])
    assert called["v"]
