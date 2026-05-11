# BrowserTrace Owner Email Send Packet

Use this packet only from the owner's email account. It is intentionally shorter
than the full directory submission sheet so the two highest-priority email
submissions can be sent in one short session.

After sending, save the sent timestamp or any reply so Codex can log metrics and
update the launch tracking issues.

Do not ask for stars, backlinks, reciprocal placement, or artificial engagement.
The ask is editorial consideration for a relevant developer tool.

Latest verification, 2026-05-11 UTC:

- console.dev still presents itself as a weekly devtools newsletter reviewing
  a small number of interesting developer tools, and the latest public issue
  does not mention BrowserTrace. Send the editorial suggestion below; do not use
  the paid advertising route unless you intentionally want a sponsored campaign.
- AgDex still shows a Developer Tools & Observability section, does not list
  BrowserTrace, and publishes `agdex.ai@gmail.com` as its contact email.

## 1. console.dev

```text
To: hello@console.dev
Subject: Devtools suggestion: BrowserTrace

Hi console.dev team,

I wanted to suggest BrowserTrace for your developer tools queue.

BrowserTrace is an MIT-licensed local debugger for AI browser-agent runs. It
records each browser-agent step as a timeline with screenshot, URL, action,
model input/output, status, and error, then exports a standalone HTML trace with
optional redaction.

It is useful for developers building Browser Use, Stagehand, Skyvern,
Playwright + LLM, or custom computer-use agents, especially when a failed run
needs screenshot, URL, model decision, and failed-step evidence in one place.

The current failure-patterns page covers concrete cases such as Browser Use
new-tab desync, Stagehand semantic verification boundary, and Skyvern VNC/CDP
debug integration.

Failure patterns page:
https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

Repo: https://github.com/aaronlab/browsertrace
Live demo: https://aaronlab.github.io/browsertrace/
Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html
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
BrowserTrace is an MIT-licensed local debugger for AI browser-agent runs. It
records each browser-agent step as a timeline with screenshot, URL, action,
model input/output, status, and error, then exports a standalone HTML trace with
optional redaction.

Example use case:
Debugging a Browser Use, Stagehand, Skyvern, Playwright + LLM, or custom
computer-use run where logs do not show the screenshot, URL, action, model
decision, and failed-step evidence together.

Concrete cases covered include Browser Use new-tab desync, Stagehand semantic
verification boundary, and Skyvern VNC/CDP debug integration.

Failure patterns page:
https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

Repository: https://github.com/aaronlab/browsertrace
Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html
Comparison: https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html
```
