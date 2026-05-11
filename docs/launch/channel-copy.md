# BrowserTrace Channel Copy

All copy points to https://github.com/aaronlab/browsertrace and the live demo at https://aaronlab.github.io/browsertrace/. Ask for feedback or real use, not upvotes or stars.

Recommended media attachment for X, LinkedIn, Product Hunt, Jike, and Xiaohongshu:

- Video: `docs/demo.mp4`
- Poster: `docs/demo-poster.png`
- Backup GIF: `docs/demo.gif`

Value-first tutorial link for Reddit, Discord, and community posts:

https://aaronlab.github.io/browsertrace/debug-browser-agent-failure.html

Failure patterns link for posts that need a concrete technical hook:

https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

Public-safe demo export for privacy-sensitive replies:

https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html

## Contribution Reply

If someone asks how to make a small docs fix, point to the current good first
issue queue:
https://github.com/aaronlab/browsertrace/labels/good%20first%20issue

Then share the First PR Recipe:
https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.

If they say they want to work on an issue, acknowledge the claim and leave a
short claim window before implementing it yourself. If GitHub cannot assign
them, add the `claimed` label so the handoff is visible.

## Troubleshooting Reply

For local first-run issues, CI failures, or AI/coding-agent troubleshooting replies, ask for debugging/workflow details plus JSON CLI diagnostics when safe to share:

For security-sensitive reports or changes, or anything that includes private trace data, point people to the private path in the Security Policy before they share details publicly:
https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

## Stack-Specific Reply Links

Use the closest guide when a technical reply needs workflow-specific context:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## AOS Mapping Research

Use this when someone asks whether BrowserTrace maps to OWASP AOS.
BrowserTrace is not an AOS compliance claim yet. Current research maps the
closest BrowserTrace concepts to tool request/result records, step correlation,
URI-style screenshot/video artifacts, URL metadata, model I/O summaries, and
explicit redaction state.

Tracker: https://github.com/aaronlab/browsertrace/issues/237

## Artifact Boundary Reply

Use this when someone is debugging screenshot blobs, base64 payloads, oversized
tool results, or model-context pollution in browser-agent runs.

```text
The pattern that has worked best for BrowserTrace is to keep browser artifacts
and model messages separate:

1. Store screenshots, URLs, and trace data as local artifacts for humans.
2. Pass image pixels to the model only when that next model call needs a typed
   image content block.
3. Otherwise pass small metadata: artifact id, dimensions, digest, status, and
   error.

That avoids stuffing large screenshots or data URIs into every future model
turn, while still keeping the failed browser state available for debugging.
For public sharing, `browsertrace export --public` omits prompt/model I/O,
screenshots, and URLs.
```

## Fresh Browser Use Debugging Angle

Use this after the icon-only Browser Use failure write-up is live. It is a
technical story, not a launch ask.

Short post:

```text
Fresh Browser Use debugging note:

If the screenshot shows a plus icon but the agent clicks a nearby toolbar button, treat it as a visible-target vs accessible-target mismatch.

I wrote up the repro evidence to capture: live HTML, accessibility snapshot, candidate boxes, and the clicked element.
```

Follow-up with link:

```text
Guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html

The useful fix is usually on the app side: put an accessible name on the real button, e.g. aria-label="Create Test".

For agent debugging, BrowserTrace keeps the failed-step timeline local so this evidence is easier to inspect.
```

## Fresh Browser Use Remote CDP Angle

Use this for Browser Use, Browserless, remote-CDP, and pooled-browser users.
It is a technical debugging note, not a launch ask.

Short post:

```text
Fresh Browser Use debugging note:

Remote CDP failures are not always "the screenshot failed".

A stale remote browser session can leave the websocket looking open while one CDP request never returns. If the event bus holds a global lock during that recovery path, one bad session can block unrelated browser sessions.
```

Follow-up with link:

```text
The evidence I would capture for this class of bug:

- event id and browser/session/target id
- CDP method, request id, start/end/duration
- websocket ping/pong near the stuck request
- event-bus lock wait/acquire/release timing
- whether recovery waits happen while the lock is held

BrowserTrace is trying to make these browser-agent failure boundaries inspectable instead of hiding them in logs.

Guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
```

## Fresh Computer-Use Persistent Browser Recovery Angle

Use this for custom computer-use agents, persistent browser profiles, and local
browser session recovery failures. It is a technical debugging note, not a
launch ask.

Short post:

```text
Fresh computer-use debugging note:

Persistent browser failures often happen before any screenshot exists.

Do not trust profile lock files or process names alone. Capture session_mode, redacted profile id, CDP attach/probe timing, recovery action, and final connection state.
```

Follow-up with link:

```text
The useful trace boundary starts before the page opens:

- profile selection and session_mode
- profile lock or stale process signal
- CDP attach/probe timing and timeout
- approval source and recovery action
- final connection state

Guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html
```

## Fresh Chinese Computer-Use Recovery Angle

Use this for WeChat, Jike, or Chinese AI-builder groups when the audience is
building custom computer-use agents or persistent browser sessions.

```text
最近遇到一个 browser agent 调试点：有些失败发生在第一张截图之前。

比如 persistent browser session 复用失败，profile lock 或进程名看起来像线索，但不一定可信。真正需要记录的是：

- session_mode
- redacted profile id
- CDP attach/probe timing
- recovery action
- final connection state

我在 BrowserTrace 里把这个 failure shape 写成了 computer-use 调试指南，想听听做 browser agent / computer-use agent 的人：你们遇到过哪些 session recovery 问题？

Guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html
Repo: https://github.com/aaronlab/browsertrace
```

## X

Non-Premium-safe thread. Post each `text` block as one X post.

```text
3 AM browser-agent debugging problem:

The run failed. Logs say what code ran, but not what the agent saw, clicked, or decided.

So I built BrowserTrace: a local trace viewer for AI browser-agent failures.

No signup, no cloud, MIT.
```

```text
It records each failed Browser Use / Stagehand / Playwright + LLM run as a local timeline:

- screenshot
- URL
- action
- model input/output
- error

Live demo: https://aaronlab.github.io/browsertrace/
Repo: https://github.com/aaronlab/browsertrace
```

## X Follow-Up

Non-Premium-safe follow-up. Post each `text` block as one X post.

```text
The shortest way to try BrowserTrace:

uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace

Open localhost:3000 and click the failed checkout demo.
```

```text
Persistent install from PyPI:

pip install "browsertrace[ui]"
browsertrace doctor
browsertrace demo
browsertrace

I want feedback from people building browser agents: what state should a trace capture when a run fails?
```

## LinkedIn

```text
I built BrowserTrace, an open-source local debugger for AI browser agents.

The problem: when a browser agent fails, normal logs usually miss the actual browser state. You know a tool call happened, but not what the model saw, which URL it was on, which screenshot led to the decision, or where the first wrong assumption entered the run.

BrowserTrace records each step as a local timeline:

- Screenshot
- URL
- Action
- Model input/output
- Step status and error
- Exportable HTML trace, with a redacted sharing mode

It is MIT licensed, local-first, and designed for Browser Use, Stagehand, Playwright + LLM scripts, and custom computer-use agents.

Live demo: https://aaronlab.github.io/browsertrace/
Repo: https://github.com/aaronlab/browsertrace

I am looking for feedback from people debugging real browser-agent runs. What should it record that your current logs miss?
```

## Hacker News

Submission URL:

```text
https://github.com/aaronlab/browsertrace
```

Title:

```text
Show HN: BrowserTrace - record and replay AI browser-agent runs to find bugs
```

First comment draft, to edit in the owner's own voice before posting:

```text
Hi HN,

I've been building browser-using AI agents and kept hitting the same debugging loop: a multi-minute run fails, the logs show tool calls, but I cannot see what the agent actually saw at the browser step where things went wrong.

Another failure class happens even earlier: persistent browser recovery can fail before any screenshot exists. For that, profile lock files are not enough; I want session_mode, redacted profile id, CDP attach/probe timing, recovery action, and final connection state in the trace.

BrowserTrace is a small Python library plus local web UI that records each browser-agent step: screenshot, URL, action, model input, model output, status, and error. You open localhost:3000, click the run, and jump to the failed step.

It is intentionally local-first:
- no signup
- no cloud
- SQLite plus filesystem
- MIT licensed
- works with Browser Use, Stagehand, Playwright + LLM scripts, and custom computer-use agents

The repo has a no-API deterministic demo and a live exported HTML trace if you want to inspect the output before installing anything:
https://aaronlab.github.io/browsertrace/

No-install PyPI uvx path:
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace

I'd like feedback from people who are building or testing browser agents. What browser state do you wish your current traces captured?
```

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

BrowserTrace keeps the missing context locally:
- screenshots
- URLs
- actions
- model input/output
- failed-step errors
- exportable HTML traces, including `--public` for public sharing

It is MIT licensed and designed for Browser Use, Stagehand, Playwright + LLM scripts, and custom computer-use agents.

Live demo:
https://aaronlab.github.io/browsertrace/

GitHub:
https://github.com/aaronlab/browsertrace

Try locally:
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace

I would especially like feedback from people running browser agents in tests or production. What would make this useful in your workflow?
```

Launch share post:

```text
BrowserTrace is live on Product Hunt today.

Local flight recorder for AI browser-agent failures: screenshots, URLs, actions, model I/O, failed-step timelines.

Builder feedback welcome from Browser Use, Stagehand, Skyvern, and Playwright + LLM workflows.

[Product Hunt link]
```

## Reddit

Title:

```text
How are you debugging browser-agent failures when logs do not show screenshots?
```

Body:

```text
I have been running into a specific debugging problem with browser agents:

The agent fails deep into a run. Logs show tool calls and exceptions, but the browser state is gone. I cannot see what the model saw, which screenshot led to the action, or where the first wrong assumption happened.

I built a small OSS tool for this called BrowserTrace. It records a local timeline for each step:

- screenshot
- URL
- action
- model input/output
- status and error

It is local-first, MIT licensed, and works with Browser Use, Stagehand, Playwright + LLM scripts, and custom computer-use agents.

Repo: https://github.com/aaronlab/browsertrace
Live demo: https://aaronlab.github.io/browsertrace/
Walkthrough: https://aaronlab.github.io/browsertrace/debug-browser-agent-failure.html

I am mainly looking for workflow feedback: if you are building browser agents, what context do you need at failure time that your current logs do not capture?
```

## WeChat Group

```text
我做了一个开源小工具 BrowserTrace，给做 browser agent 的人 debug 用。

痛点是：agent 跑到一半挂了，日志只告诉你代码调用了什么，但看不到当时浏览器页面、截图、URL、模型输入输出，所以很难知道它到底在哪一步想错了。

BrowserTrace 会本地记录每一步：
- 截图
- URL
- action
- model input/output
- 错误步骤

本地跑，不上云，MIT 开源。

Live demo: https://aaronlab.github.io/browsertrace/
GitHub: https://github.com/aaronlab/browsertrace

如果你在用 Browser Use / Stagehand / Playwright + LLM / computer use，想听听你觉得还应该记录什么。
```

## Jike

```text
最近做了一个开源工具 BrowserTrace：AI browser agent 的本地飞行记录仪。

以前 browser agent 挂了，只能看一堆 log，很难知道它当时看到了什么、为什么点错、哪一步开始偏了。

BrowserTrace 会把每一步录成 timeline：截图、URL、动作、模型输入输出、错误信息。打开本地 UI 就能直接跳到失败步骤。

适合 Browser Use / Stagehand / Playwright + LLM / computer-use agent。

Live demo: https://aaronlab.github.io/browsertrace/
GitHub: https://github.com/aaronlab/browsertrace

想找正在做 browser agent 的朋友试一下，主要求真实反馈。
```

## Xiaohongshu

Title:

```text
我给 AI 浏览器 agent 做了个本地飞行记录仪
```

Body:

```text
做 browser agent 最痛的一点：

它挂了。
log 很多。
但你不知道它当时看到了什么。

所以我做了 BrowserTrace，一个开源的本地调试工具。

它会记录 agent 每一步：
- 页面截图
- 当前 URL
- 执行动作
- 模型输入和输出
- 哪一步失败了

打开本地网页就能看完整 timeline，适合 Browser Use、Stagehand、Playwright + LLM、自研 computer-use agent。

GitHub: aaronlab/browsertrace

完全开源，本地运行，不需要注册。
```
