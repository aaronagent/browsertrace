# BrowserTrace Response Templates

Use these as notes, not as pasted auto-replies. Keep launch replies personal and specific to the comment.

## How is this different from Langfuse or LangSmith?

Langfuse and LangSmith are strong for LLM call tracing. BrowserTrace is narrower: it is built around the browser-agent failure loop. The timeline puts screenshots, URL, action, model input/output, status, and error in one local view so you can see what the agent actually saw when it failed.

Detailed comparison: https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html

## How is this different from Browserbase recordings?

Browserbase is a hosted browser runtime with recordings. BrowserTrace is runtime-agnostic and local-first. You can use it with a local Playwright page, Browser Use, Stagehand, or custom computer-use code without moving the run into a hosted browser environment.

Detailed comparison: https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html

## How is this different from Browserbase browser-trace skill?

The browser-trace skill is a good fit when you want raw CDP telemetry: DevTools
events, screenshots, DOM dumps, and per-page buckets around a running browser
automation. BrowserTrace sits one layer higher: it gives a local Python UI and
HTML export for the agent-facing failure story, including the action label,
URL, screenshot, model input/output, status, and error.

Detailed comparison: https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html

## Does data leave my machine?

No by default. The local tracer stores SQLite data and screenshots under `~/.browsertrace/` unless you override `BROWSERTRACE_HOME`. The optional AI summary endpoint only calls an OpenAI-compatible API if you configure an API key and request a summary.

## Does it work with Browser Use?

Yes. There is a Browser Use integration in `browsertrace.integrations.browser_use`, plus a generic decorator/context-manager API if you want to record steps manually.

## Does it work with Stagehand?

Yes. The Stagehand wrapper records `act` and `extract` calls and keeps the same run timeline. The README has a minimal example.

## Stagehand custom tools are skipped during replay

For a useful technical reply, separate the replay contract and the diagnostic trace contract.

For replay, the cache needs enough data to call the current tool implementation
again: tool name, serialized arguments, step id, original status/error, and
whether the tool is replay-safe. Credential-fill or other side-effectful tools
should usually require explicit opt-in.

For debugging, the trace can preserve a richer boundary even when replay is
disabled: tool name, redacted argument summary, result summary, status/error,
step index, timestamp, URL or page id before/after, and optional screenshot or
observation ids. That makes a skipped custom tool visible instead of letting
later browser steps continue against missing page state.

Avoid storing raw credentials or sensitive tool args by default. Prefer a
redacted shape plus a runtime hook that can rehydrate secrets when replay is
explicitly enabled.

## Skyvern VNC and CDP debug integration

For a useful technical reply, suggest treating VNC and CDP data as linked artifacts for the same step instead of two unrelated debug streams.

For each automation step or failure boundary, the useful shape is: step id,
task id, workflow id, URL and frame/page id,
VNC screenshot or recording artifact id with timestamp and dimensions,
CDP DOM snapshot or selected element summary, scoped
console/network/performance slices, action or tool name, status/error, retry
or recovery decision, and redaction state for screenshots, URLs, headers,
cookies, and form values.

Also call out debug-session lifecycle events. For reverse-proxy, WebSocket,
VNC, or CDP connection failures, the connect/probe result, capture start,
capture stop, timeout, cleanup, and resource leak detection can be more useful
than screenshots alone.

## Persistent browser recovery fails before screenshots

For a useful technical reply, move the trace boundary earlier than the first
browser step. Persistent browser sessions can fail during profile selection,
launch, attach, or recovery before a screenshot or URL exists.

The useful evidence shape is: `session_mode`, redacted profile id or user data
directory token, browser/session/target id when available, profile lock or stale
process signal, CDP attach/probe timing and timeout, detected process ids,
approval source, recovery action, and final connection state.

For public sharing, keep local profile paths, usernames, process details,
cookies, and profile contents redacted by default.

Guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## Stack-Specific Reply Links

Use the closest guide when a reply needs workflow-specific context:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## Does this map to OWASP AOS?

This is not an AOS compliance claim yet. The current research direction maps
BrowserTrace concepts to tool request/result records, step correlation,
URI-style screenshot/video artifacts, URL metadata, model I/O summaries, and
explicit redaction state.

The active browser/GUI artifact mapping tracker is:
https://github.com/aaronlab/browsertrace/issues/237

## Can I share traces with a teammate?

Today, use `browsertrace export <run_id> -o run.html` to create a self-contained HTML file. Hosted share links are on the roadmap, but the local OSS path comes first.

## How do I install it?

BrowserTrace is published on PyPI. The quickest no-install trial is:

```bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace
```

For a persistent install:

```bash
pip install "browsertrace[ui]"
```

## I found a bug.

Thanks for trying it. Please open an issue with the run shape, framework, Python version, and the smallest snippet that reproduces it. If the trace can be exported safely, attaching the HTML export would help a lot.

## Can I contribute a small fix?

Yes. Use the current good first issue queue:
https://github.com/aaronlab/browsertrace/labels/good%20first%20issue

Use the First PR Recipe:
https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.

For security-sensitive reports or private trace data, follow:
https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md before sharing details publicly.

## Can you share JSON diagnostics?

For local first-run issues, CI failures, or AI/coding-agent troubleshooting,
ask for workflow/debugging details plus this JSON CLI output when it is safe to
share:

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

## This is too early.

That is fair. The project is intentionally v0.1 and scoped to the smallest useful loop: record the browser-agent failure and inspect the step timeline locally. The next useful improvements are likely framework adapters, sharing, and regression comparison.

## Does it support Skyvern?

Yes, there is now a basic Skyvern wrapper in `browsertrace.integrations.skyvern`
that records high-level `run_task` and `run_workflow` calls. A deeper adapter
that captures workflow state, selected elements, and richer run artifacts is
still a good next step.

## Is this for production observability?

Not yet. Treat the current version as a local development and debugging tool. Production/team workflows need retention, access control, hosted sharing, and CI ingestion, which are tracked separately.
