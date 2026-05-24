"""Run comparison helpers shared by the CLI and local JSON API."""

from __future__ import annotations

import json
import sqlite3
from typing import Any


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


def _parse_json_field(value: Any) -> Any:
    if value in (None, ""):
        return None
    if isinstance(value, (dict, list)):
        return value
    if isinstance(value, (bytes, bytearray)):
        value = value.decode("utf-8", errors="ignore")
    if isinstance(value, str):
        try:
            return json.loads(value)
        except (TypeError, ValueError):
            return None
    return None


def _deep_get(data: dict[str, Any], paths: list[tuple[str, ...]]) -> str:
    for path in paths:
        cursor: Any = data
        ok = True
        for key in path:
            if isinstance(cursor, dict) and key in cursor:
                cursor = cursor[key]
            else:
                ok = False
                break
        if ok and cursor not in (None, ""):
            return str(cursor)
    return ""


def compare_metadata(steps: list[sqlite3.Row]) -> dict[str, str]:
    """Extract run-comparison metadata from step metadata/model_input payloads.

    This is best-effort and intentionally narrow: only keys that help determine
    whether two runs are reasonably comparable are surfaced.
    """
    fields: dict[str, str] = {
        "browser_use_version": "",
        "browsertrace_version": "",
        "model_provider": "",
        "model": "",
        "prompt_template_version": "",
    }

    metadata_paths: dict[str, list[tuple[str, ...]]] = {
        "browser_use_version": [
            ("browser_use_version",),
            ("browseruse_version",),
        ],
        "browsertrace_version": [
            ("browsertrace_version",),
        ],
        "model_provider": [
            ("model_provider",),
            ("provider",),
            ("llm_provider",),
            ("model", "provider"),
        ],
        "model": [
            ("model",),
            ("model_name",),
            ("llm_model",),
            ("model", "name"),
        ],
        "prompt_template_version": [
            ("prompt_template_version",),
            ("prompt_version",),
            ("template_version",),
            ("prompt", "template_version"),
        ],
    }

    for step in steps:
        metadata = _parse_json_field(step["metadata"])
        model_input = _parse_json_field(step["model_input"])
        metadata_dict = metadata if isinstance(metadata, dict) else {}
        nested_metadata = metadata_dict.get("metadata") if isinstance(metadata_dict.get("metadata"), dict) else {}
        candidates = [
            metadata_dict,
            nested_metadata,
            model_input if isinstance(model_input, dict) else {},
        ]

        for field, paths in metadata_paths.items():
            if fields[field]:
                continue
            for source in candidates:
                value = _deep_get(source, paths)
                if value:
                    fields[field] = value
                    break

        if all(fields.values()):
            break

    return fields


def compare_runs(
    left_run: sqlite3.Row,
    left_steps: list[sqlite3.Row],
    right_run: sqlite3.Row,
    right_steps: list[sqlite3.Row],
) -> dict[str, object]:
    left_metadata = compare_metadata(left_steps)
    right_metadata = compare_metadata(right_steps)

    payload: dict[str, object] = {
        "left": run_summary(left_run),
        "right": run_summary(right_run),
        "step_counts": {"left": len(left_steps), "right": len(right_steps)},
        "compare_metadata": {
            "left": left_metadata,
            "right": right_metadata,
            "differences": {
                key: {"left": left_metadata[key], "right": right_metadata[key]}
                for key in left_metadata.keys()
                if left_metadata[key] != right_metadata[key]
            },
        },
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
