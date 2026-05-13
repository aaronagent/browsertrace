"""Local web UI for viewing traces. Run via: `browsertrace` or `python -m browsertrace.server`."""

from __future__ import annotations

import json
import os
import sqlite3
import time
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from .compare import compare_runs
from .tracer import DEFAULT_HOME

app = FastAPI(title="BrowserTrace", docs_url=None, redoc_url=None)
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


# Cache AI summaries per run id so re-asking is free.
_SUMMARY_CACHE: dict[str, str] = {}


def _home() -> Path:
    """Resolve storage home each call so env override / CLI flag work after import."""
    override = os.environ.get("BROWSERTRACE_HOME")
    return Path(override).expanduser() if override else DEFAULT_HOME


_INITIALIZED_HOMES: set[str] = set()


def _ensure_initialized(home: Path) -> None:
    """Make sure the storage dir + SQLite schema exist before any read.

    Without this, a fresh user running `browsertrace` with no prior trace
    would 500 on the runs table not existing.
    """
    key = str(home)
    if key in _INITIALIZED_HOMES:
        return
    from .tracer import Tracer
    Tracer(home=home)  # idempotent: creates dir, schema, runs migrations
    _INITIALIZED_HOMES.add(key)


def _db() -> sqlite3.Connection:
    home = _home()
    _ensure_initialized(home)
    conn = sqlite3.connect(home / "db.sqlite", timeout=5.0)
    conn.row_factory = sqlite3.Row
    return conn


def _runs(q: str | None = None, status: str | None = None) -> list[dict[str, Any]]:
    sql = "SELECT id, name, status, started_at, ended_at, error FROM runs WHERE 1=1"
    args: list[Any] = []
    if status:
        sql += " AND status = ?"
        args.append(status)
    if q:
        sql += " AND (name LIKE ? OR error LIKE ? OR id LIKE ?)"
        like = f"%{q}%"
        args.extend([like, like, like])
    sql += " ORDER BY started_at DESC LIMIT 200"
    with _db() as c:
        rows = c.execute(sql, args).fetchall()
    runs = []
    for r in rows:
        d = dict(r)
        d["duration"] = (
            f"{d['ended_at'] - d['started_at']:.1f}s"
            if d["ended_at"]
            else "running..."
        )
        d["started_human"] = _format_started(d["started_at"])
        runs.append(d)
    return runs


def _format_started(epoch: float) -> str:
    import datetime as _dt
    delta = time.time() - epoch
    if delta < 60:
        return f"{int(delta)}s ago"
    if delta < 3600:
        return f"{int(delta // 60)}m ago"
    if delta < 86400:
        return f"{int(delta // 3600)}h ago"
    return _dt.datetime.fromtimestamp(epoch).strftime("%Y-%m-%d %H:%M")


def _run_detail(run_id: str) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
    with _db() as c:
        run_row = c.execute("SELECT * FROM runs WHERE id=?", (run_id,)).fetchone()
        step_rows = c.execute(
            "SELECT * FROM steps WHERE run_id=? ORDER BY step_index", (run_id,)
        ).fetchall()
    if not run_row:
        return None, []
    run = dict(run_row)
    run["duration"] = (
        f"{run['ended_at'] - run['started_at']:.1f}s" if run["ended_at"] else "running..."
    )
    run["started_human"] = _format_started(run["started_at"])
    steps = []
    base_ts = run["started_at"]
    first_error_index = None
    for s in step_rows:
        d = dict(s)
        for k in ("model_input", "model_output", "metadata"):
            if d.get(k):
                try:
                    d[k] = json.loads(d[k])
                except (TypeError, ValueError):
                    pass
        offset = (d.get("timestamp") or base_ts) - base_ts
        d["offset"] = f"+{offset:.2f}s" if offset >= 0 else f"{offset:.2f}s"
        # Treat anything that isn't "ok" as a failure (accepts "error", "failed",
        # "warn", custom values).
        d["is_error"] = (d.get("status") or "ok") != "ok"
        if first_error_index is None and d["is_error"]:
            first_error_index = d["step_index"]
        # Build a short metadata preview so the user sees signal without expanding.
        d["meta_preview"] = _meta_preview(d.get("metadata"))
        steps.append(d)
    run["first_error_index"] = first_error_index
    return run, steps


def _meta_preview(meta: Any, max_keys: int = 3, max_len: int = 60) -> str:
    """Render metadata as 'k=v, k=v' for quick scanning."""
    if not isinstance(meta, dict) or not meta:
        return ""
    parts = []
    for k, v in list(meta.items())[:max_keys]:
        if isinstance(v, (dict, list)):
            v = type(v).__name__
        s = f"{k}={v}"
        parts.append(s if len(s) <= max_len else s[: max_len - 1] + "…")
    if len(meta) > max_keys:
        parts.append(f"+{len(meta) - max_keys} more")
    return " · ".join(parts)


@app.get("/", response_class=HTMLResponse)
def index(request: Request, q: str | None = None, status: str | None = None) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "index.html",
        {"runs": _runs(q=q, status=status), "q": q or "", "status_filter": status or ""},
    )


@app.get("/run/{run_id}", response_class=HTMLResponse)
def run_view(request: Request, run_id: str) -> HTMLResponse:
    run, steps = _run_detail(run_id)
    if not run:
        raise HTTPException(404, "Run not found")
    return templates.TemplateResponse(request, "run.html", {"run": run, "steps": steps})


@app.get("/api/run/{run_id}")
def api_run(run_id: str) -> JSONResponse:
    """JSON export of a full run. Suitable for feeding back to an LLM for self-debug."""
    run, steps = _run_detail(run_id)
    if not run:
        raise HTTPException(404, "Run not found")
    # Strip heavy / non-LLM-useful fields and add screenshot URLs.
    payload_steps = [
        {
            "step_index": s["step_index"],
            "offset": s["offset"],
            "action": s.get("action") or "",
            "url": s.get("url") or "",
            "status": s.get("status") or "ok",
            "is_error": s.get("is_error", False),
            "error": s.get("error"),
            "model_input": s.get("model_input"),
            "model_output": s.get("model_output"),
            "metadata": s.get("metadata"),
            "screenshot_url": (
                f"/screenshot/{run_id}/{s['step_index']}" if s.get("screenshot_path") else None
            ),
        }
        for s in steps
    ]
    return JSONResponse(
        {
            "run": {
                "id": run["id"],
                "name": run.get("name"),
                "status": run.get("status"),
                "duration": run.get("duration"),
                "started_at": run.get("started_at"),
                "ended_at": run.get("ended_at"),
                "error": run.get("error"),
                "first_error_index": run.get("first_error_index"),
            },
            "steps": payload_steps,
        }
    )


@app.get("/api/runs")
def api_runs(limit: int = 200, status: str | None = None) -> JSONResponse:
    """JSON list of runs. Use ?status=failed or ?status=completed to filter."""
    limit = max(1, min(limit, 1000))
    with _db() as c:
        if status:
            rows = c.execute(
                "SELECT id, name, status, started_at, ended_at, error FROM runs "
                "WHERE status = ? ORDER BY started_at DESC LIMIT ?",
                (status, limit),
            ).fetchall()
        else:
            rows = c.execute(
                "SELECT id, name, status, started_at, ended_at, error FROM runs "
                "ORDER BY started_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
    runs = []
    for r in rows:
        d = dict(r)
        d["duration"] = (
            f"{d['ended_at'] - d['started_at']:.1f}s" if d["ended_at"] else None
        )
        runs.append(d)
    return JSONResponse({"runs": runs, "count": len(runs)})


@app.get("/api/run/{run_id}/summary")
def api_run_summary(run_id: str, force: bool = False) -> JSONResponse:
    """AI-generated root-cause summary for a run.

    Reads the run trace and asks an OpenAI-compatible LLM to diagnose what
    went wrong. Cached per-run; pass ?force=1 to recompute.

    Auth: set OPENAI_API_KEY (or BROWSERTRACE_LLM_API_KEY for a custom
    endpoint). Override the model with BROWSERTRACE_LLM_MODEL (default
    'gpt-4o-mini'). Override base URL with BROWSERTRACE_LLM_BASE_URL.
    """
    run, steps = _run_detail(run_id)
    if not run:
        raise HTTPException(404, "Run not found")

    if not force and run_id in _SUMMARY_CACHE:
        return JSONResponse({"run_id": run_id, "summary": _SUMMARY_CACHE[run_id], "cached": True})

    try:
        summary = _llm_diagnose(run, steps)
    except _LLMUnavailable as e:
        raise HTTPException(503, str(e))

    _SUMMARY_CACHE[run_id] = summary
    return JSONResponse({"run_id": run_id, "summary": summary, "cached": False})


@app.get("/api/compare/{left_run_id}/{right_run_id}")
def api_compare(left_run_id: str, right_run_id: str) -> JSONResponse:
    """Compare two runs and return the first divergent action, URL, status, or error."""
    with _db() as c:
        left_run = c.execute("SELECT * FROM runs WHERE id=?", (left_run_id,)).fetchone()
        right_run = c.execute("SELECT * FROM runs WHERE id=?", (right_run_id,)).fetchone()
        if left_run is None or right_run is None:
            raise HTTPException(404, "Run not found")
        left_steps = c.execute(
            "SELECT * FROM steps WHERE run_id=? ORDER BY step_index", (left_run["id"],)
        ).fetchall()
        right_steps = c.execute(
            "SELECT * FROM steps WHERE run_id=? ORDER BY step_index", (right_run["id"],)
        ).fetchall()

    return JSONResponse(compare_runs(left_run, left_steps, right_run, right_steps))


class _LLMUnavailable(RuntimeError):
    pass


def _llm_diagnose(run: dict[str, Any], steps: list[dict[str, Any]]) -> str:
    """Send a compact trace to an OpenAI-compatible chat endpoint, return the
    summary text. Raises _LLMUnavailable if no API key is configured or the
    `openai` package is missing.
    """
    api_key = (
        os.environ.get("OPENAI_API_KEY")
        or os.environ.get("BROWSERTRACE_LLM_API_KEY")
    )
    if not api_key:
        raise _LLMUnavailable(
            "Set OPENAI_API_KEY (or BROWSERTRACE_LLM_API_KEY) to enable AI summaries."
        )
    try:
        from openai import OpenAI  # type: ignore
    except ImportError:
        raise _LLMUnavailable(
            "AI summaries need the openai package. Install with `pip install \"browsertrace[ai]\"`."
        )

    base_url = os.environ.get("BROWSERTRACE_LLM_BASE_URL")
    model = os.environ.get("BROWSERTRACE_LLM_MODEL", "gpt-4o-mini")
    client = OpenAI(api_key=api_key, base_url=base_url) if base_url else OpenAI(api_key=api_key)

    # Build a compact representation: skip screenshots, trim long fields.
    compact_steps = []
    for s in steps:
        compact_steps.append(
            {
                "i": s["step_index"],
                "t": s.get("offset"),
                "status": s.get("status") or "ok",
                "action": (s.get("action") or "")[:300],
                "url": (s.get("url") or "")[:300],
                "model_input": _trim(s.get("model_input"), 800),
                "model_output": _trim(s.get("model_output"), 800),
                "error": s.get("error"),
            }
        )

    prompt = (
        "You are a senior debugger of AI browser agents (Browser Use, Stagehand, "
        "computer use). The user's agent run failed. Given the structured trace, "
        "diagnose the root cause in 5 bullets max.\n\n"
        "Format:\n"
        "**TL;DR**: <one sentence>\n"
        "**Failed at**: step N, <action>\n"
        "**Root cause**: <what specifically broke and why>\n"
        "**Evidence**: <which fields in the trace prove it>\n"
        "**Suggested fix**: <concrete change to selector / wait / model prompt>\n"
        "Be specific. Cite step indexes. Do not pad.\n\n"
        f"RUN: name={run.get('name')!r}, status={run.get('status')!r}, "
        f"duration={run.get('duration')!r}, error={run.get('error')!r}\n"
        f"first_error_index={run.get('first_error_index')}\n\n"
        f"STEPS:\n{json.dumps(compact_steps, indent=2, default=str)[:12000]}"
    )

    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600,
        temperature=0.2,
    )
    return resp.choices[0].message.content or "(no summary)"


def _trim(v: Any, n: int) -> Any:
    if v is None:
        return None
    s = json.dumps(v, default=str) if not isinstance(v, str) else v
    return s if len(s) <= n else s[: n - 1] + "…"


@app.get("/screenshot/{run_id}/{step_index}")
def screenshot(run_id: str, step_index: int) -> FileResponse:
    # Path-traversal guard: run_id must be a UUID-shaped string and step_index is int.
    if not run_id.replace("-", "").isalnum() or len(run_id) > 64:
        raise HTTPException(400, "Bad run id")
    base = (_home() / "screenshots").resolve()
    target = (base / run_id / f"{step_index:04d}.png").resolve()
    try:
        target.relative_to(base)
    except ValueError:
        raise HTTPException(400, "Bad path")
    if not target.exists():
        raise HTTPException(404, "Screenshot not found")
    return FileResponse(target)


def main() -> None:
    import uvicorn

    port = int(os.environ.get("BROWSERTRACE_PORT", "3000"))
    print(f"BrowserTrace UI: http://127.0.0.1:{port}")
    print(f"Storage:        {_home()}")
    uvicorn.run(app, host="127.0.0.1", port=port, log_level="warning")


if __name__ == "__main__":
    main()
