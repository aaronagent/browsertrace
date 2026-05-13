"""Run comparison helpers shared by the CLI and local JSON API."""

from __future__ import annotations

import sqlite3


def run_summary(run: sqlite3.Row) -> dict[str, str]:
    return {
        "id": run["id"],
        "name": run["name"] or "",
        "status": run["status"],
    }


def step_for_compare(step: sqlite3.Row | None) -> dict[str, object] | None:
    if step is None:
        return None
    return {
        "step_index": step["step_index"],
        "action": step["action"] or "",
        "url": step["url"] or "",
        "status": step["status"] or "ok",
        "error": step["error"],
    }


def compare_runs(
    left_run: sqlite3.Row,
    left_steps: list[sqlite3.Row],
    right_run: sqlite3.Row,
    right_steps: list[sqlite3.Row],
) -> dict[str, object]:
    payload: dict[str, object] = {
        "left": run_summary(left_run),
        "right": run_summary(right_run),
        "step_counts": {"left": len(left_steps), "right": len(right_steps)},
        "first_divergence": None,
    }

    fields = ["action", "url", "status", "error"]
    for i in range(max(len(left_steps), len(right_steps))):
        left_step = step_for_compare(left_steps[i] if i < len(left_steps) else None)
        right_step = step_for_compare(right_steps[i] if i < len(right_steps) else None)

        if left_step is None or right_step is None:
            payload["first_divergence"] = {
                "step_index": i,
                "fields": {
                    "presence": {
                        "left": left_step is not None,
                        "right": right_step is not None,
                    }
                },
                "left_step": left_step,
                "right_step": right_step,
            }
            break

        changed = {
            field: {"left": left_step[field], "right": right_step[field]}
            for field in fields
            if left_step[field] != right_step[field]
        }
        if changed:
            payload["first_divergence"] = {
                "step_index": left_step["step_index"],
                "fields": changed,
                "left_step": left_step,
                "right_step": right_step,
            }
            break

    return payload
