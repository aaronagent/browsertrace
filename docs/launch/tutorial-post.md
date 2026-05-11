# How to Debug an AI Browser Agent Failure with Screenshots and Model I/O

Your browser agent failed. The logs show tool calls, retries, and maybe a stack trace. They usually do not show the missing context: what the agent saw on the page, what it clicked, which URL it reached, and what the model returned immediately before the failure.

That gap is painful because browser-agent bugs are often visual or stateful:

- The button existed but was disabled.
- The selector matched the wrong element.
- The model interpreted stale page content.
- The page navigated but the next step assumed it had not.
- A modal appeared and changed the whole task.

BrowserTrace is a small open-source tool for recording that missing context locally.

## Run the no-API demo from PyPI

```bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace
```

Persistent install from PyPI:

```bash
pip install "browsertrace[ui]"
browsertrace doctor
browsertrace demo
browsertrace
```

Open `http://127.0.0.1:3000`, then click `demo: checkout agent fails on disabled button`.

The timeline shows the steps the agent took, including screenshots, actions, model input/output, and the failed step.

If you only want to inspect a share-safe export before installing anything, use
the public-safe demo HTML:

```text
https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html
```

For a compact list of browser-agent failure patterns and trace evidence to
collect, use:

```text
https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
```

## What to inspect first

Start at the first red step. Ask:

1. What did the screenshot show at that moment?
2. Did the URL match the model's assumption?
3. Did the action target the element you expected?
4. Did the model output mention a selector, label, or page state that was not true?
5. Was the failure caused by the current step, or did an earlier step set up the wrong state?

That sequence usually finds the bug faster than reading logs from the top.

## When failure happens before screenshots

Some computer-use failures happen before the first page screenshot or URL
exists. Persistent browser sessions can fail during profile selection, launch,
CDP attach/probe, or recovery.

In that case, do not rely only on a profile lock file or process name. The trace
needs an earlier boundary: `session_mode`, redacted profile id, browser/session
id when available, CDP attach/probe timing, timeout or error, approval source,
recovery action, and final connection state.

That is why the computer-use guide treats browser session recovery as traceable
evidence, not just setup code before the agent starts.

## Record your own run

The simplest API is the decorator:

```python
from browsertrace import trace

@trace
def my_agent(run, query: str):
    run.step(action=f"search: {query}", screenshot=...)
    run.step(action="click first result", screenshot=...)

my_agent("browser agent debugging")
```

For Playwright, use `run.snapshot(page, action=...)` to capture the current URL and screenshot without extra boilerplate.

## Export a trace

```bash
browsertrace list
browsertrace export <run_id> -o run.html
browsertrace export <run_id> --public -o public.html
```

The export is a self-contained HTML file. You can attach it to an issue, send it to a teammate, or inspect it without running the local server. Use `--public` before posting a real trace publicly to omit prompt/model I/O, screenshots, and URLs. Use the individual redaction flags only when you want to keep some fields visible.

## Why local-first?

Early browser-agent debugging often happens before you know what data is safe to upload. BrowserTrace stores runs under `~/.browsertrace/` by default, using SQLite and local screenshot files. You can override that with `BROWSERTRACE_HOME`.

Cloud sharing may make sense later for teams, but the first useful loop is local: record the failure, inspect the timeline, fix the agent.

## Reply To Contribution Questions

If someone asks how to make a small docs fix, point to the current good first
issue:
https://github.com/aaronlab/browsertrace/labels/good%20first%20issue

Then share the First PR Recipe:
https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.

## Reply To Troubleshooting Questions

For local first-run issues, CI failures, or AI/coding-agent troubleshooting replies, ask for debugging/workflow details plus JSON CLI diagnostics when safe to share:

For security-sensitive reports or changes, or anything that includes private trace data, point people to the private path in the Security Policy before they share details publicly:
https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

## Stack-Specific Reply Links

Use the closest guide when a tutorial reply turns into a workflow-specific
debugging question:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## AOS Mapping Research

Use this only if a tutorial reader asks whether BrowserTrace maps to OWASP
AOS. BrowserTrace is not an AOS compliance claim yet. Current research maps
the closest BrowserTrace concepts to tool request/result records, step correlation,
URI-style screenshot/video artifacts, URL metadata, model I/O summaries, and
explicit redaction state.

Tracker: https://github.com/aaronlab/browsertrace/issues/237

## Try it

Repo: https://github.com/aaronlab/browsertrace

Live demo: https://aaronlab.github.io/browsertrace/

Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html

If you are building with Browser Use, Stagehand, Playwright + LLM scripts, Skyvern, or custom computer-use agents, the most useful feedback is: what state do you wish your traces captured at failure time?
