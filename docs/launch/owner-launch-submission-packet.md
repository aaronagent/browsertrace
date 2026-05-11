# BrowserTrace Owner Launch Submission Packet

Use this packet only when the owner can stay available to reply for several
hours. Show HN and Product Hunt work best when the maker can answer technical
questions quickly and keep the discussion useful.

Do not ask for votes, reciprocal promotion, reposts, or artificial engagement.
Ask for workflow feedback from people building browser agents.

Primary links:

- Repo: https://github.com/aaronlab/browsertrace
- Live demo: https://aaronlab.github.io/browsertrace/
- Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
- Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html

## Show HN

Submission URL:

```text
https://github.com/aaronlab/browsertrace
```

Title:

```text
Show HN: BrowserTrace - record and replay AI browser-agent runs to find bugs
```

First comment:

```text
Hi HN,

I've been building browser-using AI agents and kept hitting the same debugging loop: a multi-minute run fails, the logs show tool calls, but I cannot see what the agent actually saw at the browser step where things went wrong.

Another failure class happens even earlier: persistent browser recovery can fail before any screenshot exists. For that, profile lock files are not enough; I want session_mode, redacted profile id, CDP attach/probe timing, recovery action, and final connection state in the trace.

BrowserTrace is a small Python library plus local web UI that records each browser-agent step: screenshot, URL, action, model input, model output, status, and error. You open localhost:3000, click the run, and jump to the failed step.

It is intentionally local-first: no signup, no cloud, SQLite plus filesystem, MIT licensed, and works with Browser Use, Stagehand, Skyvern, Playwright + LLM scripts, and custom computer-use agents.

The repo has a no-API deterministic demo and a live exported HTML trace if you want to inspect the output before installing anything:
https://aaronlab.github.io/browsertrace/

Concrete failure patterns:
https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

Examples covered there include Browser Use new-tab desync, Stagehand semantic verification boundary, and Skyvern VNC/CDP debug integration.

No-install PyPI uvx path:
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace

I'd like feedback from people who are building or testing browser agents. What browser state do you wish your current traces captured?
```

Detailed checklist: `docs/launch/day-2-show-hn-packet.md`

## Product Hunt

Name:

```text
BrowserTrace
```

Tagline:

```text
Replay failed AI browser-agent runs
```

Description:

```text
BrowserTrace records each AI browser-agent step locally: screenshot, URL, action, model input/output, status, and error. Open a timeline, jump to the failed step, and export a shareable HTML trace.
```

Topics:

```text
AI Agents, Developer Tools, Open Source, Debugging
```

Maker comment:

```text
I built BrowserTrace after losing too much time debugging browser-agent failures from logs alone.

The agent would fail at step 47, but by then the browser was gone. I could see which code ran, but not what the model saw, clicked, or returned.

Some failures happen before the first page screenshot too: persistent browser recovery, profile lock state, CDP attach/probe timing, and whether the agent reused, attached, reset, or fell back to an isolated session.

BrowserTrace keeps the missing context locally: screenshots, URLs, actions, model input/output, failed-step errors, and exportable HTML traces, including `--public` for public sharing.

It is MIT licensed and designed for Browser Use, Stagehand, Skyvern, Playwright + LLM scripts, and custom computer-use agents.

Live demo:
https://aaronlab.github.io/browsertrace/

Failure patterns:
https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

Examples covered there include Browser Use new-tab desync, Stagehand semantic verification boundary, and Skyvern VNC/CDP debug integration.

GitHub:
https://github.com/aaronlab/browsertrace

Try locally:
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace

I would especially like feedback from people running browser agents in tests or production. What would make this useful in your workflow?
```

Detailed checklist: `docs/launch/day-4-product-hunt-packet.md`
