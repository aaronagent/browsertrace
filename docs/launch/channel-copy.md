# BrowserTrace Channel Copy

All copy points to https://github.com/aaronlab/browsertrace and asks for feedback or real use, not upvotes or stars.

## X

```text
3 AM browser-agent debugging problem:

The run failed.
Logs say what code ran.
They do not show what the agent saw, clicked, or decided.

So I built BrowserTrace.

Drop it into a Browser Use / Stagehand / Playwright + LLM run and it records a local timeline:
- screenshot
- URL
- action
- model input/output
- failed step

No signup, no cloud, MIT.

https://github.com/aaronlab/browsertrace
```

## X Follow-Up

```text
The shortest way to try BrowserTrace:

git clone https://github.com/aaronlab/browsertrace
cd browsertrace
pip install -e ".[ui]"
python examples/no_api_failure_demo.py
browsertrace

Open localhost:3000 and click the failed checkout demo.

I want feedback from people building browser agents.
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
- Exportable HTML trace

It is MIT licensed, local-first, and designed for Browser Use, Stagehand, Playwright + LLM scripts, and custom computer-use agents.

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

BrowserTrace is a small Python library plus local web UI that records each browser-agent step: screenshot, URL, action, model input, model output, status, and error. You open localhost:3000, click the run, and jump to the failed step.

It is intentionally local-first:
- no signup
- no cloud
- SQLite plus filesystem
- MIT licensed
- works with Browser Use, Stagehand, Playwright + LLM scripts, and custom computer-use agents

The repo has a no-API deterministic demo and an exported HTML trace if you want to inspect the output before installing anything.

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

BrowserTrace keeps the missing context locally:
- screenshots
- URLs
- actions
- model input/output
- failed-step errors
- exportable HTML traces

It is MIT licensed and designed for Browser Use, Stagehand, Playwright + LLM scripts, and custom computer-use agents.

I would especially like feedback from people running browser agents in tests or production. What would make this useful in your workflow?
```

Launch share post:

```text
BrowserTrace is live on Product Hunt today.

It is a local flight recorder for AI browser agents: screenshots, URLs, actions, model I/O, and failed-step timelines.

If you build with Browser Use, Stagehand, Playwright + LLM scripts, or computer-use agents, I would value your feedback in the comments.

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

GitHub: https://github.com/aaronlab/browsertrace

如果你在用 Browser Use / Stagehand / Playwright + LLM / computer use，想听听你觉得还应该记录什么。
```

## Jike

```text
最近做了一个开源工具 BrowserTrace：AI browser agent 的本地飞行记录仪。

以前 browser agent 挂了，只能看一堆 log，很难知道它当时看到了什么、为什么点错、哪一步开始偏了。

BrowserTrace 会把每一步录成 timeline：截图、URL、动作、模型输入输出、错误信息。打开本地 UI 就能直接跳到失败步骤。

适合 Browser Use / Stagehand / Playwright + LLM / computer-use agent。

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
