"""Tests for the demo GIF recording helper script."""

from __future__ import annotations

import json


def test_resolve_demo_run_id_prefers_env(monkeypatch):
    from scripts import record_demo

    monkeypatch.setenv("BROWSERTRACE_DEMO_RUN_ID", "explicit-run")

    assert record_demo.resolve_demo_run_id("http://127.0.0.1:3000") == "explicit-run"


def test_resolve_demo_run_id_reads_latest_failed_run(monkeypatch):
    from scripts import record_demo

    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def read(self):
            return json.dumps({"runs": [{"id": "failed-run"}]}).encode()

    monkeypatch.delenv("BROWSERTRACE_DEMO_RUN_ID", raising=False)
    monkeypatch.setattr(record_demo.urllib.request, "urlopen", lambda _url: FakeResponse())

    assert record_demo.resolve_demo_run_id("http://127.0.0.1:3000") == "failed-run"
