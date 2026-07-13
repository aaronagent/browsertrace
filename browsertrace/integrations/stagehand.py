"""Stagehand (https://github.com/browserbase/stagehand) integration.

Stagehand exposes a Playwright-style page plus high-level act/extract methods.
The simplest, most stable way to capture traces is to wrap the page object's
key calls — we record one BrowserTrace step per Stagehand action.

Usage:
    from stagehand import Stagehand
    from browsertrace import Tracer
    from browsertrace.integrations.stagehand import wrap_stagehand

    tracer = Tracer()
    stagehand = await Stagehand(...).init()
    page = wrap_stagehand(stagehand.page, tracer, name="my run")

    await page.goto("https://example.com")
    await page.act("click the login button")  # auto-recorded
    await page.extract("get the headline")    # auto-recorded

    page.bt_run.close()  # marks the BrowserTrace run completed

The wrapper preserves all original methods; it only intercepts `goto`, `act`,
`extract`, and `observe` for tracing. If Stagehand changes its API, you can
fall back to manual `run.snapshot(page, action=...)` calls.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Optional

from ..tracer import Run, Tracer


class _TracedPage:
    """Wraps a Stagehand page and records a step per traced method."""

    _TRACED_METHODS = ("goto", "act", "extract", "observe", "click")

    def __init__(self, page: Any, tracer: Tracer, run_name: str):
        self._page = page
        self._tracer = tracer
        self.bt_run: Run = Run(tracer, run_id=__import__("uuid").uuid4().hex, name=run_name)
        self.bt_run._start()

    def __getattr__(self, name: str) -> Any:
        # Intercept the methods we trace; pass everything else straight through.
        attr = getattr(self._page, name)
        if name not in self._TRACED_METHODS or not callable(attr):
            return attr
        return self._wrap(name, attr)

    def _wrap(self, name: str, fn: Any) -> Any:
        async def traced(*args: Any, **kwargs: Any) -> Any:
            instr = args[0] if args else kwargs.get("url") or kwargs.get("instruction") or ""
            shot: Optional[bytes] = None
            try:
                shot = await self._page.screenshot()
            except Exception:
                pass
            step_id = self.bt_run.step(
                action=f"{name}: {instr}"[:300],
                url=getattr(self._page, "url", "") or "",
                screenshot=shot,
                model_input={"method": name, "args": list(args), "kwargs": kwargs},
                stagehand_method=name,
                instruction=str(instr),
            )
            try:
                result = await fn(*args, **kwargs)
            except Exception as e:
                self.bt_run.update_step(
                    step_id, status="error", error=f"{type(e).__name__}: {e}"
                )
                raise
            output = _serialize_result(result)
            model_output = {"result": output}
            evidence = _extract_stagehand_evidence(output, method=name)
            if evidence:
                model_output["stagehand_evidence"] = evidence
            self.bt_run.update_step(step_id, model_output=model_output)
            return result
        return traced

    async def screenshot(self, *args: Any, **kwargs: Any) -> Any:
        return await self._page.screenshot(*args, **kwargs)


def wrap_stagehand(page: Any, tracer: Tracer, name: str = "stagehand run") -> _TracedPage:
    """Wrap a Stagehand page so every act/extract/goto records a BrowserTrace step.

    Returns the wrapped page. Use `wrapped.bt_run` to access the underlying Run
    (e.g. to call `.close()` or read `.id`).
    """
    return _TracedPage(page, tracer, name)


def _serialize_result(result: Any) -> Any:
    return _to_plain(result, set())


def _to_plain(value: Any, seen: set[int]) -> Any:
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, bytes):
        return repr(value)
    value_id = id(value)
    if value_id in seen:
        return "<recursive>"
    seen.add(value_id)

    if hasattr(value, "model_dump"):
        try:
            return _to_plain(value.model_dump(exclude_none=True), seen)
        except Exception:
            pass
    if hasattr(value, "dict"):
        try:
            return _to_plain(value.dict(), seen)
        except Exception:
            pass
    if isinstance(value, Mapping):
        return {str(key): _to_plain(child, seen) for key, child in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_to_plain(child, seen) for child in value]
    if hasattr(value, "__dict__"):
        return _to_plain(vars(value), seen)
    return str(value)


def _extract_stagehand_evidence(output: Any, *, method: str = "") -> dict[str, Any]:
    evidence: dict[str, Any] = {}
    selectors = _find_values(output, "selector", "selectors", "css_selector", "cssSelector")
    descriptions = _find_values(output, "description")
    methods = _find_values(output, "method")
    elements = _find_values(output, "element", "elements", "target", "targets")
    extracted_text = _find_values(
        output, "text", "content", "extracted_text", "extractedText", "extracted_content"
    )
    actions = _find_values(output, "action", "actions")
    statuses = _find_values(output, "status", "success", "ok")
    attempts = _find_values(output, "attempt", "attempts", "retry_count", "retries")
    verifications = _find_values(
        output, "verification", "verified", "validation", "tool_call", "tool_calls", "toolCalls"
    )

    if selectors:
        evidence["selectors"] = selectors
    if descriptions:
        evidence["descriptions"] = descriptions
    if methods:
        evidence["methods"] = methods
    if elements:
        evidence["elements"] = elements
    if extracted_text:
        evidence["extracted_text"] = extracted_text
    if actions:
        evidence["actions"] = actions
    if statuses:
        evidence["statuses"] = statuses
    if attempts:
        evidence["attempts"] = attempts
    if verifications:
        evidence["verification"] = verifications
    if method == "observe":
        candidates = _observe_candidates(output)
        if candidates:
            evidence["observe_candidates"] = candidates

    return evidence


def _observe_candidates(output: Any) -> list[dict[str, Any]]:
    candidates = output if isinstance(output, list) else output.get("candidates", []) if isinstance(output, dict) else []
    summary: list[dict[str, Any]] = []
    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue
        item = {
            key: candidate[key]
            for key in ("selector", "description", "method", "action")
            if candidate.get(key) is not None
        }
        if item:
            summary.append(item)
    return summary


def _find_values(value: Any, *keys: str) -> list[str]:
    found: list[str] = []
    seen: set[str] = set()

    def visit(item: Any) -> None:
        if isinstance(item, dict):
            for key, child in item.items():
                if key in keys:
                    add(child)
                visit(child)
        elif isinstance(item, (list, tuple)):
            for child in item:
                visit(child)

    def add(item: Any) -> None:
        values = item if isinstance(item, (list, tuple)) else [item]
        for value in values:
            if value is None:
                continue
            serialized = str(value)
            if serialized and serialized not in seen:
                seen.add(serialized)
                found.append(serialized)

    visit(value)
    return found
