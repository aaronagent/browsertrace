# BrowserTrace Owner Email Send Packet

Use this packet only from the owner's email account. It is intentionally shorter
than the full directory submission sheet so the two highest-priority email
submissions can be sent in one short session.

After sending, save the sent timestamp or any reply so Codex can log metrics and
update the launch tracking issues.

Do not ask for stars, backlinks, reciprocal placement, or artificial engagement.
The ask is editorial consideration for a relevant developer tool.

Latest verification, 2026-05-13 UTC:

- console.dev still presents itself as a weekly devtools newsletter reviewing
  a small number of interesting developer tools, and its public selection
  criteria says to submit tool suggestions to `hello@console.dev`. The latest
  public issue does not mention BrowserTrace. Send the editorial suggestion
  below; do not use the paid advertising route unless you intentionally want a
  sponsored campaign.
- AgDex still shows a Developer Tools & Observability section, says it indexes
  500+ AI tools, does not list BrowserTrace, and publishes `agdex.ai@gmail.com`
  as its contact email.
- BrowserTrace is now listed in `Jenqyang/Awesome-AI-Agents` under
  `Applications` -> `Tools`; mention this only if a reviewer wants a quick
  external discovery signal.

## 1. console.dev

```text
To: hello@console.dev
Subject: Devtools suggestion: BrowserTrace

Hi console.dev team,

I wanted to suggest BrowserTrace for your developer tools queue.

BrowserTrace is an MIT-licensed local debugger for Browser Use failures. It
records each Browser Use step as a timeline with screenshot, URL, action, model
input/output, status, and error, then exports a standalone HTML trace with
optional redaction. When a failed Browser Use run has a known-good baseline,
`browsertrace compare <failed_run_id> <success_run_id>` reports the first
divergent action, URL, status, or error before the developer opens the UI.

It is useful for developers building Browser Use workflows, especially when a
failed run needs screenshot, URL, model decision, and failed-step evidence in
one place. Stagehand, Skyvern, Playwright + LLM, and custom computer-use
workflows are supported as secondary integrations.

The current failure-patterns page covers concrete Browser Use cases such as
Browser Use new-tab desync, Browser Use local HTML upload navigation, remote
CDP hangs, and icon-only target mismatch.

The live demo now replays the local HTML upload navigation failure: a Browser
Use-shaped run tries to upload file:///tmp/browsertrace-report.html, navigates
to the local file path instead, and the upload preview never appeared.

Browser Use guide:
https://aaronlab.github.io/browsertrace/browser-use-debugging.html

Failure patterns page:
https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

Repo: https://github.com/aaronlab/browsertrace
Live demo: https://aaronlab.github.io/browsertrace/
Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.19/browsertrace-demo-public.html
Comparison: https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html

This is not a sponsored review request. I would value any editorial feedback if
it is not a fit.
```

## 2. AgDex

```text
To: agdex.ai@gmail.com
Subject: Tool submission: BrowserTrace

Tool name: BrowserTrace
Website URL: https://aaronlab.github.io/browsertrace/
Category: Developer tools / observability

Short description:
BrowserTrace is an MIT-licensed local debugger for Browser Use failures. It
records each Browser Use step as a timeline with screenshot, URL, action, model
input/output, status, and error, then exports a standalone HTML trace with
optional redaction. When a failed Browser Use run has a known-good baseline,
`browsertrace compare <failed_run_id> <success_run_id>` reports the first
divergent action, URL, status, or error before the developer opens the UI.

Example use case:
Debugging a Browser Use run where logs do not show the screenshot, URL, action,
model decision, and failed-step evidence together. Stagehand, Skyvern,
Playwright + LLM, and custom computer-use workflows remain supported as
secondary integrations.

Concrete cases covered include Browser Use new-tab desync, Browser Use local
HTML upload navigation, remote CDP hangs, and icon-only target mismatch.

Live demo use case:
The live demo now replays the local HTML upload navigation failure: a Browser
Use-shaped run tries to upload file:///tmp/browsertrace-report.html, navigates
to the local file path instead, and the upload preview never appeared.

Browser Use guide:
https://aaronlab.github.io/browsertrace/browser-use-debugging.html

Failure patterns page:
https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

Repository: https://github.com/aaronlab/browsertrace
Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.19/browsertrace-demo-public.html
Comparison: https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html
```
