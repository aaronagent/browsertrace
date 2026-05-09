# BrowserTrace Response Templates

Use these as notes, not as pasted auto-replies. Keep launch replies personal and specific to the comment.

## How is this different from Langfuse or LangSmith?

Langfuse and LangSmith are strong for LLM call tracing. BrowserTrace is narrower: it is built around the browser-agent failure loop. The timeline puts screenshots, URL, action, model input/output, status, and error in one local view so you can see what the agent actually saw when it failed.

## How is this different from Browserbase recordings?

Browserbase is a hosted browser runtime with recordings. BrowserTrace is runtime-agnostic and local-first. You can use it with a local Playwright page, Browser Use, Stagehand, or custom computer-use code without moving the run into a hosted browser environment.

## Does data leave my machine?

No by default. The local tracer stores SQLite data and screenshots under `~/.browsertrace/` unless you override `BROWSERTRACE_HOME`. The optional AI summary endpoint only calls an OpenAI-compatible API if you configure an API key and request a summary.

## Does it work with Browser Use?

Yes. There is a Browser Use integration in `browsertrace.integrations.browser_use`, plus a generic decorator/context-manager API if you want to record steps manually.

## Does it work with Stagehand?

Yes. The Stagehand wrapper records `act` and `extract` calls and keeps the same run timeline. The README has a minimal example.

## Can I share traces with a teammate?

Today, use `browsertrace export <run_id> -o run.html` to create a self-contained HTML file. Hosted share links are on the roadmap, but the local OSS path comes first.

## Why no PyPI install yet?

The current install path uses GitHub while the package is still early. PyPI publishing is tracked as a launch follow-up. Once credentials are available, the README install path should become `pip install browsertrace[ui]`.

## I found a bug.

Thanks for trying it. Please open an issue with the run shape, framework, Python version, and the smallest snippet that reproduces it. If the trace can be exported safely, attaching the HTML export would help a lot.

## This is too early.

That is fair. The project is intentionally v0.1 and scoped to the smallest useful loop: record the browser-agent failure and inspect the step timeline locally. The next useful improvements are likely framework adapters, sharing, and regression comparison.

## Does it support Skyvern?

Not first-class yet. Skyvern support is a good next adapter because the debugging problem is similar: browser state plus model decision context. There is a tracked issue for a Skyvern adapter.

## Is this for production observability?

Not yet. Treat the current version as a local development and debugging tool. Production/team workflows need retention, access control, hosted sharing, and CI ingestion, which are tracked separately.
