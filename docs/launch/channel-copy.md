# BrowserTrace Channel Copy

All copy points to https://github.com/aaronlab/browsertrace and the live demo at https://aaronlab.github.io/browsertrace/. Lead with Browser Use failure debugging. Ask for feedback or real use, not upvotes or stars.

Recommended media attachment for X, LinkedIn, Product Hunt, Jike, and Xiaohongshu:

- Video: `docs/demo.mp4`
- Poster: `docs/demo-poster.png`
- Backup GIF: `docs/demo.gif`

Primary Browser Use guide:

https://aaronlab.github.io/browsertrace/browser-use-debugging.html

Value-first tutorial link for Reddit, Discord, and community posts:

https://aaronlab.github.io/browsertrace/debug-browser-agent-failure.html

Failure patterns link for posts that need a concrete technical hook:

https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

Public-safe demo export for privacy-sensitive replies:

https://github.com/aaronlab/browsertrace/releases/download/v0.1.19/browsertrace-demo-public.html

Optional external-listing credibility note:

BrowserTrace is listed in `Jenqyang/Awesome-AI-Agents` under `Applications`
-> `Tools`. Use this only as supporting context when useful; do not ask for
stars, votes, reposts, backlinks, or reciprocal promotion.

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

Capture: live HTML, accessibility snapshot, candidate boxes, and the clicked element.
```

Follow-up with link:

```text
Guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html

Durable fix: put an accessible name on the real button, e.g. aria-label="Create Test".

BrowserTrace keeps the failed-step timeline local so screenshot, URL, action, and model output stay inspectable.
```

## Fresh Browser Use Remote CDP Angle

Use this for Browser Use, Browserless, remote-CDP, and pooled-browser users.
It is a technical debugging note, not a launch ask.

Short post:

```text
Fresh Browser Use debugging note:

Remote CDP failures are not always screenshot failures.

A stale remote browser session can keep the websocket open while one CDP request never returns. If recovery holds a global event-bus lock, one bad session can block unrelated sessions.
```

Follow-up with link:

```text
The evidence I would capture for this class of bug:

- event id + browser/session/target id
- CDP method/request id/duration
- websocket ping/pong near the stuck request
- event-bus lock wait/acquire/release timing
- whether recovery waited while holding the lock
```

```text
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
Trace before the page opens:

- profile selection + session_mode
- lock/stale-process signal
- CDP attach/probe timing
- approval source + recovery action
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
Browser Use failed on a local `.html` upload: it navigated to the filename and the upload preview never appeared.

I built BrowserTrace to replay what the agent saw, clicked, and returned before the first red step.

No signup, no cloud, MIT.
```

```text
It records failed Browser Use runs as local timelines:

- screenshot
- URL
- action
- model input/output
- error

Live demo: https://aaronlab.github.io/browsertrace/
Repo: https://github.com/aaronlab/browsertrace
```

```text
v0.1.19 adds `browsertrace compare`: give it a failed Browser Use run and a known-good run, and it reports the first divergent action, URL, status, or error.

That is the fastest path from "the agent failed" to "this is where it drifted."
```

## X Follow-Up

Non-Premium-safe follow-up. Post each `text` block as one X post.

```text
The shortest way to try BrowserTrace:

uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace

Open localhost:3000 and click `demo: Browser Use local HTML upload navigation failure`.
```

```text
Persistent install from PyPI:

pip install "browsertrace[ui]"
browsertrace doctor
browsertrace demo
browsertrace
```

```text
Then compare a failed Browser Use run with a good run:

browsertrace compare <failed_run_id> <success_run_id>

I want feedback from Browser Use builders: what state should a trace capture when a run fails?
```

## LinkedIn

```text
I built BrowserTrace, an open-source local replay debugger for Browser Use failures.

The problem: when a Browser Use run fails, normal logs usually miss the actual browser state. You know a tool call happened, but not what the model saw, which URL it was on, which screenshot led to the decision, or where the first wrong assumption entered the run.

BrowserTrace records each step as a local timeline:

- Screenshot
- URL
- Action
- Model input/output
- Step status and error
- Exportable HTML trace, with a redacted sharing mode
- Failed-vs-known-good comparison with `browsertrace compare`

Browser Use is the primary path. Stagehand, Skyvern, Playwright + LLM scripts, and custom computer-use agents are secondary integrations.

If you have one failed Browser Use run and one successful run for the same task, `browsertrace compare <failed_run_id> <success_run_id>` reports the first divergent action, URL, status, or error before you open the local UI.

The live demo now replays the local HTML upload navigation failure: a Browser Use-shaped run tries to upload file:///tmp/browsertrace-report.html, navigates to the local file path instead, and the upload preview never appeared.

Live demo: https://aaronlab.github.io/browsertrace/
Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
Repo: https://github.com/aaronlab/browsertrace

I am looking for feedback from people debugging real Browser Use runs. What should it record that your current logs miss?
```

## Hacker News

Submission URL:

```text
https://github.com/aaronlab/browsertrace
```

Title:

```text
Show HN: BrowserTrace - replay Browser Use failures locally
```

First comment draft, to edit in the owner's own voice before posting:

```text
Hi HN,

I've been building with Browser Use and kept hitting the same debugging loop: a multi-minute run fails, the logs show tool calls, but I cannot see what the agent actually saw at the browser step where things went wrong.

Concrete Browser Use failure shapes include new-tab desync, local HTML upload navigation being misread as a URL, remote CDP hangs, and icon-only buttons where the screenshot looks obvious but the accessible target is missing.

BrowserTrace is a small Python library plus local web UI that records each Browser Use step: screenshot, URL, action, model input, model output, status, and error. You open localhost:3000, click the run, and jump to the failed step. If you have a known-good run for the same task, `browsertrace compare <failed_run_id> <success_run_id>` reports the first divergent action, URL, status, or error before you open the UI.

It is intentionally local-first:
- no signup
- no cloud
- SQLite plus filesystem
- MIT licensed
- Browser Use is the primary path
- Stagehand, Playwright + LLM scripts, Skyvern, and custom computer-use agents are secondary integrations

The repo has a no-API deterministic demo and a live exported HTML trace if you want to inspect the output before installing anything:
https://aaronlab.github.io/browsertrace/

Browser Use guide:
https://aaronlab.github.io/browsertrace/browser-use-debugging.html

No-install PyPI uvx path:
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace

I'd like feedback from people who are building or testing Browser Use workflows. What browser state do you wish your current traces captured?
```

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

BrowserTrace keeps the missing context locally:
- screenshots
- URLs
- actions
- model input/output
- failed-step errors
- failed-vs-known-good comparison with `browsertrace compare`
- exportable HTML traces, including `--public` for public sharing

Browser Use is the primary path. Stagehand, Skyvern, Playwright + LLM scripts, and custom computer-use agents are secondary integrations.

Live demo:
https://aaronlab.github.io/browsertrace/

Browser Use guide:
https://aaronlab.github.io/browsertrace/browser-use-debugging.html

GitHub:
https://github.com/aaronlab/browsertrace

Try locally:
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace

I would especially like feedback from people running Browser Use in tests or production. What would make this useful in your workflow?
```

Launch share post:

```text
BrowserTrace is live on Product Hunt today.

Local replay debugger for Browser Use failures: screenshots, URLs, actions, model I/O, failed-step timelines.

Feedback welcome from Browser Use builders. Secondary: Stagehand, Skyvern, Playwright + LLM.

[Product Hunt link]
```

## Reddit

Title:

```text
How are you debugging Browser Use failures when logs do not show screenshots?
```

Body:

```text
I have been running into a specific debugging problem with Browser Use:

The agent fails deep into a run. Logs show tool calls and exceptions, but the browser state is gone. I cannot see what the model saw, which screenshot led to the action, or where the first wrong assumption happened.

I built a small OSS tool for this called BrowserTrace. It records a local timeline for each step:

- screenshot
- URL
- action
- model input/output
- status and error

It is local-first, MIT licensed, and Browser Use is the primary path. Stagehand, Skyvern, Playwright + LLM scripts, and custom computer-use agents are secondary integrations.

Repo: https://github.com/aaronlab/browsertrace
Live demo: https://aaronlab.github.io/browsertrace/
Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html

I am mainly looking for workflow feedback: if you are building Browser Use workflows, what context do you need at failure time that your current logs do not capture?
```

## WeChat Group

```text
我做了一个开源小工具 BrowserTrace，先给 Browser Use 失败调试用。

痛点是：Browser Use agent 跑到一半挂了，日志只告诉你代码调用了什么，但看不到当时浏览器页面、截图、URL、模型输入输出，所以很难知道它到底在哪一步想错了。

BrowserTrace 会本地记录每一步：
- 截图
- URL
- action
- model input/output
- 错误步骤
- failed run 和 good run 的第一处分歧

本地跑，不上云，MIT 开源。

新版还加了 `browsertrace compare <failed_run_id> <success_run_id>`：同一个 Browser Use 任务有失败和成功两条记录时，可以先在命令行看到第一处 action、URL、status 或 error 分歧。

Live demo: https://aaronlab.github.io/browsertrace/
Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
GitHub: https://github.com/aaronlab/browsertrace

如果你在用 Browser Use，想听听你觉得还应该记录什么。Stagehand / Skyvern / Playwright + LLM / computer-use 是 secondary integration。
```

## Jike

```text
最近做了一个开源工具 BrowserTrace：Browser Use 失败的本地回放调试器。

以前 Browser Use 挂了，只能看一堆 log，很难知道它当时看到了什么、为什么点错、哪一步开始偏了。

BrowserTrace 会把每一步录成 timeline：截图、URL、动作、模型输入输出、错误信息。打开本地 UI 就能直接跳到失败步骤；如果同一个任务有 failed run 和 good run，也可以用 `browsertrace compare` 先找第一处 action、URL、status 或 error 分歧。

先适合 Browser Use，也保留 Stagehand / Skyvern / Playwright + LLM / computer-use secondary integrations。

Live demo: https://aaronlab.github.io/browsertrace/
Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
GitHub: https://github.com/aaronlab/browsertrace

想找正在用 Browser Use 或做 browser agent 的朋友试一下，主要求真实反馈。
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
