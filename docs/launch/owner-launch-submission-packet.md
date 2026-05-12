# BrowserTrace Owner Launch Submission Packet

Use this packet only when the owner can stay available to reply for several
hours. Show HN and Product Hunt work best when the maker can answer technical
questions quickly and keep the discussion useful.

Do not ask for votes, reciprocal promotion, reposts, or artificial engagement.
Ask for Browser Use debugging feedback first. Mention Stagehand, Skyvern,
Playwright + LLM, and computer-use as secondary integrations only when useful.

Primary links:

- Repo: https://github.com/aaronlab/browsertrace
- Live demo: https://aaronlab.github.io/browsertrace/
- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
- Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html

Optional credibility note:

- BrowserTrace is listed in `Jenqyang/Awesome-AI-Agents` under `Applications`
  -> `Tools`. Use this only if someone asks whether the project appears in
  external AI-agent tooling lists; do not ask for votes, stars, reposts, or
  reciprocal promotion.

## Show HN

Submission URL:

```text
https://github.com/aaronlab/browsertrace
```

Title:

```text
Show HN: BrowserTrace - replay Browser Use failures locally
```

First comment:

```text
Hi HN,

I've been building with Browser Use and kept hitting the same debugging loop: a multi-minute run fails, the logs show tool calls, but I cannot see what the agent actually saw at the browser step where things went wrong.

Concrete Browser Use failure shapes include new-tab desync, local HTML upload navigation being misread as a URL, remote CDP hangs, and icon-only buttons where the screenshot looks obvious but the accessible target is missing.

BrowserTrace is a small Python library plus local web UI that records each Browser Use step: screenshot, URL, action, model input, model output, status, and error. You open localhost:3000, click the run, and jump to the failed step.

It is intentionally local-first: no signup, no cloud, SQLite plus filesystem, MIT licensed. Browser Use is the primary path; Stagehand, Skyvern, Playwright + LLM scripts, and custom computer-use agents are secondary integrations.

The repo has a no-API deterministic demo and a live exported HTML trace if you want to inspect the output before installing anything:
https://aaronlab.github.io/browsertrace/

Concrete failure patterns:
https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

Browser Use guide:
https://aaronlab.github.io/browsertrace/browser-use-debugging.html

Examples covered there include Browser Use new-tab desync, Browser Use local HTML upload navigation, remote CDP hangs, and icon-only target mismatch.

No-install PyPI uvx path:
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace

I'd like feedback from people who are building or testing Browser Use workflows. What browser state do you wish your current traces captured?
```

Detailed checklist: `docs/launch/day-2-show-hn-packet.md`

## Product Hunt

Name:

```text
BrowserTrace
```

Tagline:

```text
Replay failed Browser Use runs
```

Description:

```text
BrowserTrace records each Browser Use step locally: screenshot, URL, action, model input/output, status, and error. Open a timeline, jump to the failed step, and export a shareable HTML trace.
```

Topics:

```text
AI Agents, Developer Tools, Open Source, Debugging
```

Maker comment:

```text
I built BrowserTrace after losing too much time debugging Browser Use failures from logs alone.

The agent would fail at step 47, but by then the browser was gone. I could see which code ran, but not what the model saw, clicked, or returned.

Concrete Browser Use failure shapes include new-tab desync, local HTML upload navigation mistakes, remote CDP hangs, and icon-only buttons where the screenshot looks obvious but the accessible target is missing.

BrowserTrace keeps the missing context locally: screenshots, URLs, actions, model input/output, failed-step errors, and exportable HTML traces, including `--public` for public sharing.

Browser Use is the primary path. Stagehand, Skyvern, Playwright + LLM scripts, and custom computer-use agents are secondary integrations.

Live demo:
https://aaronlab.github.io/browsertrace/

Failure patterns:
https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

Browser Use guide:
https://aaronlab.github.io/browsertrace/browser-use-debugging.html

Examples covered there include Browser Use new-tab desync, Browser Use local HTML upload navigation, remote CDP hangs, and icon-only target mismatch.

GitHub:
https://github.com/aaronlab/browsertrace

Try locally:
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace

I would especially like feedback from people running Browser Use in tests or production. What would make this useful in your workflow?
```

Detailed checklist: `docs/launch/day-4-product-hunt-packet.md`
