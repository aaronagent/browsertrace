"""Packaged deterministic demo trace for first-run onboarding."""

from __future__ import annotations

import base64
from pathlib import Path
from typing import Union

from .tracer import Tracer


DEMO_NAME = "demo: Browser Use local HTML upload navigation failure"

PNG_1X1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/p9sAAAAASUVORK5CYII="
)


def create_demo_run(home: Union[str, Path, None] = None) -> str:
    """Create a deterministic failed run and return its run id."""
    tracer = Tracer(home=home)
    run_id = ""

    try:
        with tracer.run(DEMO_NAME) as run:
            run_id = run.id
            run.step(
                action="open Browser Use upload page",
                url="https://app.example.test/upload",
                screenshot=PNG_1X1,
                model_input={
                    "task": "Upload the local HTML report with Browser Use.",
                    "browser_state": {
                        "url": "about:blank",
                        "title": "New tab",
                    },
                },
                model_output={
                    "thought": "Open the app upload page before attaching the local file.",
                    "action": "go_to_url",
                    "url": "https://app.example.test/upload",
                },
            )
            run.step(
                action="select local HTML fixture",
                url="https://app.example.test/upload",
                screenshot=PNG_1X1,
                model_input={
                    "browser_state": {
                        "url": "https://app.example.test/upload",
                        "title": "Upload report",
                    },
                    "file_input": "input[type=file]",
                    "candidate_file": "file:///tmp/browsertrace-report.html",
                },
                model_output={
                    "thought": "The upload control needs the local HTML file.",
                    "action": "upload_file",
                    "path": "file:///tmp/browsertrace-report.html",
                    "expected": "preview renders uploaded HTML",
                },
            )
            run.step(
                action="Browser Use navigates to local file path",
                url="file:///tmp/browsertrace-report.html",
                screenshot=PNG_1X1,
                model_input={
                    "previous_url": "https://app.example.test/upload",
                    "selected_action": "upload_file",
                    "path": "file:///tmp/browsertrace-report.html",
                },
                model_output={
                    "action": "navigate",
                    "url": "file:///tmp/browsertrace-report.html",
                    "risk": "The local file path was treated as a navigation target instead of an upload payload.",
                },
            )
            failed_step = run.step(
                action="assert uploaded file preview",
                url="file:///tmp/browsertrace-report.html",
                screenshot=PNG_1X1,
                model_input={
                    "expected_url": "https://app.example.test/upload",
                    "actual_url": "file:///tmp/browsertrace-report.html",
                    "expected_preview": "browsertrace-report.html",
                },
                model_output={
                    "status": "failed",
                    "missing": "uploaded file preview",
                    "actual_url": "file:///tmp/browsertrace-report.html",
                },
            )
            try:
                raise RuntimeError(
                    "Browser Use navigated away from the upload page; "
                    "upload preview never appeared"
                )
            except RuntimeError as exc:
                run.update_step(
                    failed_step,
                    status="error",
                    error=f"{type(exc).__name__}: {exc}",
                )
                raise
    except RuntimeError:
        return run_id

    return run_id
