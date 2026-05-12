# BrowserTrace Owner Social Post Packet

Use this packet when the owner has one short session to publish from personal
accounts. Attach `docs/demo.mp4` where the platform supports video, or
`docs/demo-poster.png` where a static image works better.

Do not ask for stars, reposts, reciprocal sharing, or artificial engagement.
Ask for Browser Use debugging feedback first. Mention Stagehand, Skyvern,
Playwright + LLM, and computer-use only as secondary integrations.

Primary links:

- Repo: https://github.com/aaronlab/browsertrace
- Live demo: https://aaronlab.github.io/browsertrace/
- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

Optional credibility note:

- BrowserTrace is now listed in `Jenqyang/Awesome-AI-Agents` under
  `Applications` -> `Tools`. Use this only as social proof when useful; do not
  ask for stars, votes, reposts, or reciprocal promotion.

## Media Alt Text

Use this when the platform supports alt text for `docs/demo.mp4` or
`docs/demo-poster.png`:

```text
BrowserTrace timeline for a failed Browser Use run, showing a screenshot, URL,
action, model output, status, and the failed step highlighted in red.
```

## X

Post as a short thread.

```text
3 AM Browser Use debugging problem:

The run failed. Logs say what code ran, but not what the agent saw, clicked, returned, or why the first red step happened.

So I built BrowserTrace: a local replay debugger for Browser Use failures.

No signup, no cloud, MIT.
```

```text
It records each failed Browser Use run as a local timeline:

- screenshot
- URL
- action
- model input/output
- error

Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
Live demo: https://aaronlab.github.io/browsertrace/
```

```text
Concrete Browser Use failure patterns:
https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

Examples: Browser Use new-tab desync, Browser Use local HTML upload navigation, remote CDP hangs, icon-only target mismatch.

If you build with Browser Use: what state should a trace capture when a run fails?

Repo: https://github.com/aaronlab/browsertrace
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

Browser Use is the primary path. Stagehand, Skyvern, Playwright + LLM scripts, and custom computer-use agents are supported as secondary integrations.

Live demo: https://aaronlab.github.io/browsertrace/
Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
Repo: https://github.com/aaronlab/browsertrace

The failure-patterns page includes Browser Use new-tab desync, Browser Use local HTML upload navigation, remote CDP hangs, and icon-only target mismatch. Secondary examples cover Stagehand semantic verification and Skyvern VNC/CDP debug.

I am looking for feedback from people debugging real Browser Use runs. What should it record that your current logs miss?
```

## WeChat Group

```text
我做了一个开源小工具 BrowserTrace，先给 Browser Use 失败调试用。

痛点是：Browser Use agent 跑到一半挂了，日志只告诉你代码调用了什么，但看不到当时浏览器页面、截图、URL、模型输入输出，也很难知道第一步红在哪里。

BrowserTrace 会本地记录每一步：
- 截图
- URL
- action
- model input/output
- 错误步骤

本地跑，不上云，MIT 开源。

Live demo: https://aaronlab.github.io/browsertrace/
Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
GitHub: https://github.com/aaronlab/browsertrace

里面有几个具体 Browser Use 案例：new-tab desync、local HTML upload navigation、remote CDP hang、icon-only target mismatch。

如果你在用 Browser Use，想听听你觉得还应该记录什么。Stagehand / Skyvern / Playwright + LLM / computer-use 也有 secondary integration。
```

## Jike

```text
最近做了一个开源工具 BrowserTrace：Browser Use 失败的本地回放调试器。

以前 Browser Use 挂了，只能看一堆 log，很难知道它当时看到了什么、为什么点错、哪一步开始偏了。

BrowserTrace 会把每一步录成 timeline：截图、URL、动作、模型输入输出、错误信息。打开本地 UI 就能直接跳到失败步骤。

先适合 Browser Use，也保留 Stagehand / Skyvern / Playwright + LLM / computer-use 这些 secondary integrations。

Live demo: https://aaronlab.github.io/browsertrace/
Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
GitHub: https://github.com/aaronlab/browsertrace

具体 Browser Use failure patterns 包括 new-tab desync、local HTML upload navigation、remote CDP hang、icon-only target mismatch。

想找正在用 Browser Use 或做 browser agent 的朋友试一下，主要求真实反馈。
```
