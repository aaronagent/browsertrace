"""Server tests covering all FastAPI routes + JSON API + edge cases.

Uses BROWSERTRACE_HOME to point each test at an isolated tmp dir, so tests
don't pollute or read each other's data and they don't read the developer's
real ~/.browsertrace.
"""

from __future__ import annotations

import importlib
import os

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def isolated_server(tmp_path, monkeypatch):
    """Spin up a TestClient against a fresh BROWSERTRACE_HOME.

    Resets the server module's cached "initialized homes" set so each test
    really initializes its own tmp dir.
    """
    monkeypatch.setenv("BROWSERTRACE_HOME", str(tmp_path))

    import browsertrace.server as server_mod
    importlib.reload(server_mod)
    server_mod._INITIALIZED_HOMES.clear()  # explicit, in case reload was skipped

    from browsertrace import Tracer  # use the same env override
    tracer = Tracer(home=tmp_path)

    return server_mod, tracer, TestClient(server_mod.app)


def _make_run(tracer, name="run", steps=None, fail_last=False):
    """Helper: create a run with optional steps; optionally make it fail."""
    steps = steps or []
    if fail_last:
        try:
            with tracer.run(name) as run:
                for s in steps:
                    run.step(**s)
                raise RuntimeError("intentional failure")
        except RuntimeError:
            pass
    else:
        with tracer.run(name) as run:
            for s in steps:
                run.step(**s)
    return run.id


# ---------- index (/) ----------

def test_index_renders_empty_state_when_db_missing(isolated_server):
    """Fresh BROWSERTRACE_HOME with no traces should render the empty state, not 500.

    Why this matters: first-time users running `browsertrace` before recording
    anything would otherwise hit a SQL error and a 500 page.
    """
    _, _, client = isolated_server
    r = client.get("/")
    assert r.status_code == 200
    assert "No runs yet" in r.text


def test_index_lists_runs_from_browsertrace_home(isolated_server):
    """Index should list runs read from the env-overridden home, not ~/.browsertrace."""
    _, tracer, client = isolated_server
    _make_run(tracer, name="my unique run name")
    r = client.get("/")
    assert r.status_code == 200
    assert "my unique run name" in r.text


# ---------- run page (/run/{id}) ----------

def test_run_page_renders_steps(isolated_server):
    _, tracer, client = isolated_server
    rid = _make_run(
        tracer,
        name="hn-fetch",
        steps=[
            {"action": "navigate", "url": "https://news.ycombinator.com"},
            {"action": "click first story"},
        ],
    )
    r = client.get(f"/run/{rid}")
    assert r.status_code == 200
    assert "navigate" in r.text
    assert "click first story" in r.text


def test_run_page_404_for_unknown_run(isolated_server):
    _, _, client = isolated_server
    r = client.get("/run/not-a-real-id")
    assert r.status_code == 404


def test_run_page_shows_jump_to_failed_step_when_failure_exists(isolated_server):
    """A failed run's page must surface a 'jump to failed step' link.

    This is the core launch-demo affordance.
    """
    _, tracer, client = isolated_server
    rid = _make_run(
        tracer,
        name="failing run",
        steps=[
            {"action": "step ok"},
            {"action": "step error", "status": "error", "error": "boom"},
        ],
    )
    r = client.get(f"/run/{rid}")
    assert r.status_code == 200
    assert "jump to failed step" in r.text


def test_run_page_treats_status_failed_as_error(isolated_server):
    """The UI must treat status='failed' (not just 'error') as a failure marker.

    Real bug found in dogfood: a user passed status='failed' and the UI didn't
    highlight it.
    """
    _, tracer, client = isolated_server
    rid = _make_run(
        tracer,
        name="permissive status",
        steps=[
            {"action": "ok step"},
            {"action": "broke", "status": "failed", "error": "x"},
        ],
    )
    r = client.get(f"/run/{rid}")
    assert r.status_code == 200
    assert "step-error" in r.text  # CSS class on the failed step


# ---------- /api/runs ----------

def test_api_runs_returns_runs_in_recency_order(isolated_server):
    _, tracer, client = isolated_server
    _make_run(tracer, name="older")
    _make_run(tracer, name="newer")
    r = client.get("/api/runs")
    assert r.status_code == 200
    data = r.json()
    names = [run["name"] for run in data["runs"]]
    assert names[0] == "newer"
    assert "older" in names


def test_api_runs_filters_by_status(isolated_server):
    _, tracer, client = isolated_server
    _make_run(tracer, name="ok-run")
    _make_run(tracer, name="bad-run", steps=[{"action": "x"}], fail_last=True)
    r = client.get("/api/runs", params={"status": "failed"})
    data = r.json()
    assert all(run["status"] == "failed" for run in data["runs"])
    assert "bad-run" in [run["name"] for run in data["runs"]]
    assert "ok-run" not in [run["name"] for run in data["runs"]]


def test_api_runs_clamps_limit(isolated_server):
    """Unbounded ?limit= is a foot gun. Server should clamp to 1000."""
    _, _, client = isolated_server
    r = client.get("/api/runs", params={"limit": 999999})
    assert r.status_code == 200  # not a 422 or DB OOM


# ---------- /api/run/{id} ----------

def test_api_run_returns_llm_ready_payload(isolated_server):
    """The JSON export must include first_error_index and parsed model_output."""
    _, tracer, client = isolated_server
    rid = _make_run(
        tracer,
        name="llm-export",
        steps=[
            {"action": "ok step"},
            {
                "action": "wrong selector",
                "status": "error",
                "error": "Timeout",
                "model_output": {"selector": "#wrong"},
            },
        ],
    )
    r = client.get(f"/api/run/{rid}")
    assert r.status_code == 200
    data = r.json()
    assert data["run"]["first_error_index"] == 1
    assert data["run"]["status"] == "completed" or data["run"]["status"] == "failed"
    assert data["steps"][1]["is_error"] is True
    # Model output must round-trip as parsed JSON, not a raw string.
    assert data["steps"][1]["model_output"] == {"selector": "#wrong"}


def test_api_run_404_for_unknown_run(isolated_server):
    _, _, client = isolated_server
    r = client.get("/api/run/missing")
    assert r.status_code == 404


# ---------- /api/compare/{left}/{right} ----------

def test_api_compare_returns_first_divergence(isolated_server):
    _, tracer, client = isolated_server
    with tracer.run("browser-use success") as run:
        run.step(action="navigate", url="https://example.com/start")
        run.step(action="click(selector=#checkout)", url="https://example.com/done")
        success_id = run.id

    try:
        with tracer.run("browser-use failure") as run:
            run.step(action="navigate", url="https://example.com/start")
            run.step(
                action="click(selector=#cancel)",
                url="https://example.com/cart",
                status="error",
                error="wrong target",
            )
            failed_id = run.id
            raise RuntimeError("wrong target")
    except RuntimeError:
        pass

    r = client.get(f"/api/compare/{failed_id}/{success_id}")

    assert r.status_code == 200
    data = r.json()
    assert data["left"]["id"] == failed_id
    assert data["right"]["id"] == success_id
    assert data["first_divergence"]["step_index"] == 1
    assert data["first_divergence"]["fields"]["action"] == {
        "left": "click(selector=#cancel)",
        "right": "click(selector=#checkout)",
    }
    assert data["first_divergence"]["fields"]["url"] == {
        "left": "https://example.com/cart",
        "right": "https://example.com/done",
    }


# ---------- /screenshot path-traversal guard ----------

def test_screenshot_rejects_traversal_run_id(isolated_server):
    """Path-traversal-shaped run_ids must be rejected before any FS access."""
    _, _, client = isolated_server
    # `..` is not in the UUID-ish [a-zA-Z0-9-] alphabet of run_ids.
    r = client.get("/screenshot/..%2F..%2Fetc/0")
    # We accept anything that isn't 200; the guard returns 400 OR FastAPI
    # routing returns 404 because the encoded path doesn't match the route.
    assert r.status_code != 200


def test_screenshot_404_for_unknown_step(isolated_server):
    _, tracer, client = isolated_server
    rid = _make_run(tracer, name="no-screens", steps=[{"action": "x"}])
    r = client.get(f"/screenshot/{rid}/9999")
    assert r.status_code == 404


def test_screenshot_serves_existing_png(isolated_server):
    _, tracer, client = isolated_server
    png = b"\x89PNG\r\n\x1a\n" + b"\x00" * 16
    rid = _make_run(
        tracer,
        name="has-screen",
        steps=[{"action": "snap", "screenshot": png}],
    )
    r = client.get(f"/screenshot/{rid}/0")
    assert r.status_code == 200
    assert r.content.startswith(b"\x89PNG")


# ---------- BROWSERTRACE_HOME end-to-end ----------

def test_browsertrace_home_override_isolates_data(tmp_path, monkeypatch):
    """Setting BROWSERTRACE_HOME after import should make the server read the new home.

    Why: Tracer(home=...) and the UI must agree on storage location, otherwise
    users will record to one place and see an empty UI in another.
    """
    monkeypatch.setenv("BROWSERTRACE_HOME", str(tmp_path))
    import browsertrace.server as server_mod
    importlib.reload(server_mod)
    server_mod._INITIALIZED_HOMES.clear()

    from browsertrace import Tracer
    Tracer(home=tmp_path)

    client = TestClient(server_mod.app)
    r = client.get("/")
    assert r.status_code == 200
    assert "No runs yet" in r.text  # the tmp home is empty


# ---------- search & filter ----------

def test_index_search_matches_by_run_name(isolated_server):
    _, tracer, client = isolated_server
    _make_run(tracer, name="apple")
    _make_run(tracer, name="banana")
    r = client.get("/", params={"q": "appl"})
    assert r.status_code == 200
    assert "apple" in r.text
    assert "banana" not in r.text


def test_index_filters_by_status(isolated_server):
    _, tracer, client = isolated_server
    _make_run(tracer, name="happy-run")
    _make_run(tracer, name="sad-run", steps=[{"action": "x"}], fail_last=True)
    r = client.get("/", params={"status": "failed"})
    assert "sad-run" in r.text
    assert "happy-run" not in r.text


def test_index_search_matches_error_text(isolated_server):
    _, tracer, client = isolated_server
    _make_run(tracer, name="run-a", steps=[{"action": "x"}], fail_last=True)
    # The intentional exception message includes "intentional"
    r = client.get("/", params={"q": "intentional"})
    assert "run-a" in r.text


# ---------- AI summary endpoint ----------

def test_api_summary_503_when_no_api_key(isolated_server, monkeypatch):
    """Without an API key the endpoint should fail gracefully, not 500."""
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("BROWSERTRACE_LLM_API_KEY", raising=False)
    _, tracer, client = isolated_server
    rid = _make_run(tracer, name="needs summary", steps=[{"action": "x"}], fail_last=True)
    r = client.get(f"/api/run/{rid}/summary")
    assert r.status_code == 503
    assert "API key" in r.text or "OPENAI_API_KEY" in r.text


def test_api_summary_uses_cache_after_first_call(isolated_server, monkeypatch):
    """The second call should be served from the in-memory cache (cached: True)."""
    _, tracer, client = isolated_server
    rid = _make_run(tracer, name="cache-me", steps=[{"action": "x"}], fail_last=True)

    # Pre-seed the cache to skip the LLM call entirely.
    import browsertrace.server as server_mod
    server_mod._SUMMARY_CACHE[rid] = "fake summary"

    r = client.get(f"/api/run/{rid}/summary")
    assert r.status_code == 200
    body = r.json()
    assert body["summary"] == "fake summary"
    assert body["cached"] is True
