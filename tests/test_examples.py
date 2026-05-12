"""Tests for launch demo scripts."""

from __future__ import annotations

import json
import runpy
import sqlite3


def test_no_api_failure_demo_creates_failed_trace(tmp_path, monkeypatch):
    monkeypatch.setenv("BROWSERTRACE_HOME", str(tmp_path))

    runpy.run_path("examples/no_api_failure_demo.py", run_name="__main__")

    with sqlite3.connect(tmp_path / "db.sqlite") as c:
        run = c.execute(
            "SELECT id, name, status, error FROM runs ORDER BY started_at DESC LIMIT 1"
        ).fetchone()
        steps = c.execute(
            "SELECT step_index, action, status, error, model_output "
            "FROM steps WHERE run_id=? ORDER BY step_index",
            (run[0],),
        ).fetchall()

    assert run[1] == "demo: checkout agent fails on disabled button"
    assert run[2] == "failed"
    assert "RuntimeError" in run[3]
    assert len(steps) == 4
    assert steps[3][1] == "click disabled checkout button"
    assert steps[3][2] == "error"
    assert "button was disabled" in steps[3][3]
    assert "button.checkout.primary" in steps[3][4]


def test_skyvern_wrapper_example_creates_completed_trace(tmp_path, monkeypatch):
    monkeypatch.setenv("BROWSERTRACE_HOME", str(tmp_path))

    runpy.run_path("examples/skyvern_wrapper_example.py", run_name="__main__")

    with sqlite3.connect(tmp_path / "db.sqlite") as c:
        run = c.execute(
            "SELECT id, name, status, error FROM runs ORDER BY started_at DESC LIMIT 1"
        ).fetchone()
        step = c.execute(
            "SELECT action, status, model_input, model_output, metadata "
            "FROM steps WHERE run_id=? ORDER BY step_index",
            (run[0],),
        ).fetchone()

    assert run[1] == "demo: skyvern invoice extraction"
    assert run[2] == "completed"
    assert run[3] is None
    assert step[0] == "run_task: extract the invoice total"
    assert step[1] == "ok"
    assert json.loads(step[2])["kwargs"]["url"] == "https://example.com/invoice"
    assert json.loads(step[3])["task_run_id"] == "tsk_demo_001"
    assert json.loads(step[4])["skyvern_run_id"] == "tsk_demo_001"


def test_stagehand_wrapper_example_creates_completed_trace(tmp_path, monkeypatch):
    monkeypatch.setenv("BROWSERTRACE_HOME", str(tmp_path))

    runpy.run_path("examples/stagehand_wrapper_example.py", run_name="__main__")

    with sqlite3.connect(tmp_path / "db.sqlite") as c:
        run = c.execute(
            "SELECT id, name, status, error FROM runs ORDER BY started_at DESC LIMIT 1"
        ).fetchone()
        steps = c.execute(
            "SELECT action, url, status, model_input, screenshot_path "
            "FROM steps WHERE run_id=? ORDER BY step_index",
            (run[0],),
        ).fetchall()

    assert run[1] == "demo: stagehand checkout flow"
    assert run[2] == "completed"
    assert run[3] is None
    assert [step[0] for step in steps] == [
        "act: click the checkout button",
        "extract: extract the order total",
    ]
    assert steps[0][1] == "https://shop.example.test/cart"
    assert steps[0][2] == "ok"
    assert json.loads(steps[0][3])["method"] == "act"
    assert steps[0][4].endswith(".png")


def test_browser_use_callback_demo_creates_completed_trace(tmp_path, monkeypatch):
    monkeypatch.setenv("BROWSERTRACE_HOME", str(tmp_path))

    runpy.run_path("examples/browser_use_callback_demo.py", run_name="__main__")

    with sqlite3.connect(tmp_path / "db.sqlite") as c:
        run = c.execute(
            "SELECT id, name, status, error FROM runs ORDER BY started_at DESC LIMIT 1"
        ).fetchone()
        steps = c.execute(
            "SELECT action, url, status, model_output "
            "FROM steps WHERE run_id=? ORDER BY step_index",
            (run[0],),
        ).fetchall()

    assert run[1] == "demo: browser-use callback flow"
    assert run[2] == "completed"
    assert run[3] is None
    assert [step[0] for step in steps] == [
        "search_google(query=BrowserTrace)",
        "click(selector=#result-1)",
    ]
    assert steps[0][1] == "https://example.com/search"
    assert steps[1][2] == "ok"
    assert json.loads(steps[1][3])["thought"] == "open the first useful result"


def test_browser_use_run_hooks_demo_creates_completed_trace(tmp_path, monkeypatch):
    monkeypatch.setenv("BROWSERTRACE_HOME", str(tmp_path))

    runpy.run_path("examples/browser_use_run_hooks_demo.py", run_name="__main__")

    with sqlite3.connect(tmp_path / "db.sqlite") as c:
        run = c.execute(
            "SELECT id, name, status, error FROM runs ORDER BY started_at DESC LIMIT 1"
        ).fetchone()
        steps = c.execute(
            "SELECT action, url, status, model_input, model_output, metadata "
            "FROM steps WHERE run_id=? ORDER BY step_index",
            (run[0],),
        ).fetchall()

    assert run[1] == "demo: browser-use run hooks flow"
    assert run[2] == "completed"
    assert run[3] is None
    assert [step[0] for step in steps] == [
        "search_google(query=BrowserTrace)",
        "click(selector=#result-1)",
    ]
    assert steps[0][1] == "https://example.com/search"
    assert steps[1][1] == "https://example.com/results"

    model_input = json.loads(steps[0][3])
    model_output = json.loads(steps[1][4])
    metadata = json.loads(steps[1][5])

    assert model_input["task"] == "Find BrowserTrace with Browser Use hooks"
    assert model_input["browser_state"]["title"] == "Search"
    assert model_output["thought"] == "open the first useful result"
    assert model_output["extracted_content"] == "BrowserTrace repository"
    assert metadata["hook"] == "browser_use_run_hooks"


def test_computer_use_loop_example_creates_failed_trace(tmp_path, monkeypatch):
    monkeypatch.setenv("BROWSERTRACE_HOME", str(tmp_path))

    runpy.run_path("examples/computer_use_loop_example.py", run_name="__main__")

    with sqlite3.connect(tmp_path / "db.sqlite") as c:
        run = c.execute(
            "SELECT id, name, status, error FROM runs ORDER BY started_at DESC LIMIT 1"
        ).fetchone()
        steps = c.execute(
            "SELECT action, url, status, error, model_input, model_output, metadata "
            "FROM steps WHERE run_id=? ORDER BY step_index",
            (run[0],),
        ).fetchall()

    assert run[1] == "demo: custom computer-use checkout"
    assert run[2] == "failed"
    assert "RuntimeError" in run[3]
    assert [step[0] for step in steps] == [
        "open checkout page",
        "observe checkout form",
        "click model-selected submit button",
    ]
    assert steps[0][1] == "https://shop.example.test/checkout"
    assert steps[2][2] == "error"
    assert "disabled submit button" in steps[2][3]
    assert json.loads(steps[1][4])["task"] == "complete checkout"
    assert json.loads(steps[2][5])["selector"] == "button.checkout.primary"
    assert json.loads(steps[2][6])["agent_loop"] == "observe-decide-act"


def test_playwright_llm_loop_example_creates_failed_trace(tmp_path, monkeypatch):
    monkeypatch.setenv("BROWSERTRACE_HOME", str(tmp_path))

    runpy.run_path("examples/playwright_llm_loop_example.py", run_name="__main__")

    with sqlite3.connect(tmp_path / "db.sqlite") as c:
        run = c.execute(
            "SELECT id, name, status, error FROM runs ORDER BY started_at DESC LIMIT 1"
        ).fetchone()
        steps = c.execute(
            "SELECT action, url, status, error, model_input, model_output, metadata "
            "FROM steps WHERE run_id=? ORDER BY step_index",
            (run[0],),
        ).fetchall()

    assert run[1] == "demo: playwright llm checkout selector failure"
    assert run[2] == "failed"
    assert "RuntimeError" in run[3]
    assert [step[0] for step in steps] == [
        "observe checkout page",
        "choose checkout selector",
        "click model-selected button",
    ]
    assert steps[0][1] == "https://shop.example.test/checkout"
    assert steps[2][2] == "error"
    assert "button.checkout.primary was disabled" in steps[2][3]

    choose_input = json.loads(steps[1][4])
    choose_output = json.loads(steps[1][5])
    click_metadata = json.loads(steps[2][6])

    assert choose_input["messages"][1]["content"] == "Pick the checkout submit selector."
    assert choose_input["page"]["url"] == "https://shop.example.test/checkout"
    assert "checkout primary" in choose_input["page"]["dom_snippet"]
    assert "Checkout" in choose_input["page"]["accessibility_tree"]
    assert choose_input["retry_count"] == 0
    assert choose_output["selector"] == "button.checkout.primary"
    assert choose_output["action"] == "click"
    assert click_metadata["agent_stack"] == "playwright+llm"
    assert click_metadata["selector"] == "button.checkout.primary"
    assert click_metadata["retry"] == 0
