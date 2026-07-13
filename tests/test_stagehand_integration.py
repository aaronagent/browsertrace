"""Tests for browsertrace.integrations.stagehand.wrap_stagehand."""

from __future__ import annotations

import asyncio
import json
import sqlite3

from browsertrace import Tracer
from browsertrace.integrations.stagehand import wrap_stagehand


class FakeStagehandPage:
    url = "https://example.com"

    async def screenshot(self):
        return b"\x89PNG\r\n\x1a\n" + b"\x00" * 16

    async def act(self, instruction: str):
        return {
            "ok": True,
            "instruction": instruction,
            "action": "click",
            "selector": "button.login",
            "attempts": 2,
            "verification": {"status": "passed"},
        }

    async def extract(self, instruction: str):
        return {
            "status": "completed",
            "instruction": instruction,
            "data": {"text": "Welcome back", "selector": "h1"},
            "tool_calls": [{"name": "extract_text", "status": "ok"}],
        }

    async def observe(self, instruction: str):
        return [
            {
                "selector": "button.checkout.primary",
                "description": "Checkout button",
                "method": "click",
                "instruction": instruction,
            }
        ]


class NonSerializableResult:
    def __init__(self):
        self.selector = "button.nonserial"
        self.payload = object()


class FakeNoScreenshotPage:
    url = "https://example.com/no-shot"

    async def screenshot(self):
        raise RuntimeError("screenshots disabled")

    async def act(self, instruction: str):
        return NonSerializableResult()


class FakeFailurePage(FakeStagehandPage):
    async def act(self, instruction: str):
        raise RuntimeError(f"could not {instruction}")


def test_stagehand_documented_bt_run_close_marks_completed(tmp_path):
    tracer = Tracer(home=tmp_path)
    page = wrap_stagehand(FakeStagehandPage(), tracer, name="stagehand close")

    page.bt_run.close()

    with sqlite3.connect(tmp_path / "db.sqlite") as c:
        status = c.execute(
            "SELECT status FROM runs WHERE id=?",
            (page.bt_run.id,),
        ).fetchone()[0]

    assert status == "completed"


def test_stagehand_records_method_result_as_model_output(tmp_path):
    tracer = Tracer(home=tmp_path)
    page = wrap_stagehand(FakeStagehandPage(), tracer, name="stagehand result")

    result = asyncio.run(page.act("click the login button"))

    with sqlite3.connect(tmp_path / "db.sqlite") as c:
        row = c.execute(
            "SELECT model_input, model_output FROM steps WHERE run_id=?",
            (page.bt_run.id,),
        ).fetchone()

    model_input = json.loads(row[0])
    model_output = json.loads(row[1])
    assert result["instruction"] == "click the login button"
    assert model_input["method"] == "act"
    assert model_output["result"] == result

    page.bt_run.close()


def test_stagehand_records_compact_evidence_from_observe_result(tmp_path):
    tracer = Tracer(home=tmp_path)
    page = wrap_stagehand(FakeStagehandPage(), tracer, name="stagehand evidence")

    asyncio.run(page.observe("find the checkout button"))

    with sqlite3.connect(tmp_path / "db.sqlite") as c:
        row = c.execute(
            "SELECT model_output FROM steps WHERE run_id=?",
            (page.bt_run.id,),
        ).fetchone()

    model_output = json.loads(row[0])
    evidence = model_output["stagehand_evidence"]
    assert evidence["selectors"] == ["button.checkout.primary"]
    assert evidence["descriptions"] == ["Checkout button"]
    assert evidence["methods"] == ["click"]
    assert evidence["observe_candidates"] == [
        {
            "selector": "button.checkout.primary",
            "description": "Checkout button",
            "method": "click",
        }
    ]

    page.bt_run.close()


def test_stagehand_records_act_extract_evidence_and_metadata(tmp_path):
    tracer = Tracer(home=tmp_path)
    page = wrap_stagehand(FakeStagehandPage(), tracer, name="stagehand rich evidence")

    asyncio.run(page.act("click the login button"))
    asyncio.run(page.extract("read the heading"))

    with sqlite3.connect(tmp_path / "db.sqlite") as c:
        rows = c.execute(
            "SELECT model_output, metadata FROM steps WHERE run_id=? ORDER BY step_index",
            (page.bt_run.id,),
        ).fetchall()

    act_output = json.loads(rows[0][0])
    act_metadata = json.loads(rows[0][1])
    extract_output = json.loads(rows[1][0])
    extract_metadata = json.loads(rows[1][1])

    assert act_metadata == {
        "stagehand_method": "act",
        "instruction": "click the login button",
    }
    assert act_output["stagehand_evidence"]["selectors"] == ["button.login"]
    assert act_output["stagehand_evidence"]["actions"] == ["click"]
    assert act_output["stagehand_evidence"]["statuses"] == ["True", "passed"]
    assert act_output["stagehand_evidence"]["attempts"] == ["2"]
    assert act_output["stagehand_evidence"]["verification"] == ["{'status': 'passed'}"]

    assert extract_metadata["stagehand_method"] == "extract"
    assert extract_output["stagehand_evidence"]["extracted_text"] == ["Welcome back"]
    assert extract_output["stagehand_evidence"]["verification"] == [
        "{'name': 'extract_text', 'status': 'ok'}"
    ]

    page.bt_run.close()


def test_stagehand_marks_failed_step_error(tmp_path):
    tracer = Tracer(home=tmp_path)
    page = wrap_stagehand(FakeFailurePage(), tracer, name="stagehand failure")

    try:
        asyncio.run(page.act("click missing button"))
    except RuntimeError:
        pass
    else:
        raise AssertionError("expected RuntimeError")

    with sqlite3.connect(tmp_path / "db.sqlite") as c:
        status, error = c.execute(
            "SELECT status, error FROM steps WHERE run_id=?",
            (page.bt_run.id,),
        ).fetchone()

    assert status == "error"
    assert "RuntimeError: could not click missing button" in error

    page.bt_run.close()


def test_stagehand_handles_non_serializable_result_and_missing_screenshot(tmp_path):
    tracer = Tracer(home=tmp_path)
    page = wrap_stagehand(FakeNoScreenshotPage(), tracer, name="stagehand no screenshot")

    asyncio.run(page.act("click nonserial"))

    with sqlite3.connect(tmp_path / "db.sqlite") as c:
        model_output, screenshot_path = c.execute(
            "SELECT model_output, screenshot_path FROM steps WHERE run_id=?",
            (page.bt_run.id,),
        ).fetchone()

    output = json.loads(model_output)
    assert output["result"]["selector"] == "button.nonserial"
    assert isinstance(output["result"]["payload"], str)
    assert output["stagehand_evidence"]["selectors"] == ["button.nonserial"]
    assert screenshot_path is None

    page.bt_run.close()
