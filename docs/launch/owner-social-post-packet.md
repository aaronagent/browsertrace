# BrowserTrace Owner Social Post Packet

Use this packet when the owner has one short session to publish from personal
accounts. Attach `docs/demo.mp4` where the platform supports video, or
`docs/demo-poster.png` where a static image works better.

Do not ask for stars, reposts, reciprocal sharing, or artificial engagement.
Ask for workflow feedback from people building browser agents.

Primary links:

- Repo: https://github.com/aaronlab/browsertrace
- Live demo: https://aaronlab.github.io/browsertrace/
- Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

## X

Post as a short thread.

```text
3 AM browser-agent debugging problem:

The run failed. Logs say what code ran, but not what the agent saw, clicked, or decided.

So I built BrowserTrace: a local trace viewer for AI browser-agent failures.

No signup, no cloud, MIT.
```

```text
It records each failed Browser Use / Stagehand / Skyvern / Playwright + LLM run as a local timeline:

- screenshot
- URL
- action
- model input/output
- error

Live demo: https://aaronlab.github.io/browsertrace/
Repo: https://github.com/aaronlab/browsertrace
```

```text
Concrete failure patterns:
https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

Examples: Browser Use new-tab desync, Stagehand semantic verification boundary, Skyvern VNC/CDP debug integration.

I am looking for feedback from people building browser agents: what state should a trace capture when a run fails?
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

It is MIT licensed, local-first, and designed for Browser Use, Stagehand, Skyvern, Playwright + LLM scripts, and custom computer-use agents.

Live demo: https://aaronlab.github.io/browsertrace/
Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
Repo: https://github.com/aaronlab/browsertrace

The failure-patterns page includes Browser Use new-tab desync, Stagehand semantic verification boundary, and Skyvern VNC/CDP debug integration.

I am looking for feedback from people debugging real browser-agent runs. What should it record that your current logs miss?
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
Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
GitHub: https://github.com/aaronlab/browsertrace

里面有几个具体案例：Browser Use new-tab desync、Stagehand semantic verification boundary、Skyvern VNC/CDP debug integration。

如果你在用 Browser Use / Stagehand / Skyvern / Playwright + LLM / computer use，想听听你觉得还应该记录什么。
```

## Jike

```text
最近做了一个开源工具 BrowserTrace：AI browser agent 的本地飞行记录仪。

以前 browser agent 挂了，只能看一堆 log，很难知道它当时看到了什么、为什么点错、哪一步开始偏了。

BrowserTrace 会把每一步录成 timeline：截图、URL、动作、模型输入输出、错误信息。打开本地 UI 就能直接跳到失败步骤。

适合 Browser Use / Stagehand / Skyvern / Playwright + LLM / computer-use agent。

Live demo: https://aaronlab.github.io/browsertrace/
Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
GitHub: https://github.com/aaronlab/browsertrace

具体 failure patterns 包括 Browser Use new-tab desync、Stagehand semantic verification boundary、Skyvern VNC/CDP debug integration。

想找正在做 browser agent 的朋友试一下，主要求真实反馈。
```
