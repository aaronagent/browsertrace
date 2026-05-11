# BrowserTrace 中文长文草稿

Use this for Chinese technical platforms such as Juejin, WeChat official
account, Zhihu, V2EX, or a personal blog. Edit into the owner's voice before
publishing.

Do not ask for stars, upvotes, reposts, or artificial engagement. Ask for
workflow feedback from people who actually build browser agents.

## Title Options

```text
Browser agent 跑挂了，为什么日志还是不够用？
```

```text
我做了一个 AI browser agent 的本地飞行记录仪
```

```text
调试 AI browser agent：除了 log，还需要看到它当时看见了什么
```

## Article

最近我在调试 browser agent 的时候，一直遇到一个很具体的问题：

agent 跑了几十步，最后失败了。

日志里能看到 tool call、异常、模型输出，但最关键的信息经常已经丢了：

- 当时浏览器页面长什么样？
- agent 点之前看到了哪张截图？
- 当前 URL 是什么？
- 模型输入和模型输出分别是什么？
- 它是哪一步开始理解错页面状态的？

普通日志会告诉你“代码做了什么”，但 browser agent 的失败很多时候不是代码分支错了，而是 agent 在某一个浏览器状态下理解错了页面、点错了元素、或者基于一张过期截图继续推理。

所以我做了一个开源小工具：BrowserTrace。

GitHub:

```text
https://github.com/aaronlab/browsertrace
```

Live demo:

```text
https://aaronlab.github.io/browsertrace/
```

Failure patterns:

```text
https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
```

## BrowserTrace 是什么

BrowserTrace 可以理解成 AI browser agent 的本地飞行记录仪。

它会把一次 agent run 记录成 timeline，每一步包含：

- screenshot
- URL
- action
- model input
- model output
- step status
- error

失败之后，你打开本地 UI，就可以直接跳到出错步骤，看 agent 当时到底看到了什么、模型返回了什么、浏览器在哪个页面、错误发生在哪一步。

它是 MIT 开源、本地优先的工具，不需要注册账号，不需要上传 trace 到云端。

## 为什么不是只看 Playwright Trace Viewer？

Playwright Trace Viewer 很适合调试浏览器自动化本身。

但如果你的脚本里有 LLM 决策，例如：

- Browser Use
- Stagehand
- Playwright + LLM
- Skyvern-style workflow
- 自己写的 computer-use agent

那么 bug 往往不只在浏览器动作层，而是在“模型为什么做出这个动作”的那一层。

BrowserTrace 关注的是这个交界面：浏览器状态 + agent action + model input/output。

它不是替代 Playwright Trace Viewer，而是补上 LLM 决策上下文。

## 有些失败发生在第一张截图之前

还有一类 computer-use agent 问题更早：浏览器还没打开页面，第一张 screenshot
和 URL 都没有，persistent browser session recovery 已经失败了。

这时只看 profile lock 文件或进程名不够。更有用的 trace 边界应该记录：

- `session_mode`
- redacted profile id
- browser/session id
- CDP attach/probe timing
- timeout 或 error
- approval source
- recovery action
- final connection state

这类信息能解释 agent 到底是复用已有浏览器、attach 到 remote debugging
endpoint、fallback 到 isolated session，还是被要求人工确认后 reset。否则你只
能看到“浏览器启动失败”，但不知道失败发生在 profile、CDP attach、锁判断，还
是 recovery policy。

## 60 秒试一下

BrowserTrace 有一个不需要 API key、不需要真实浏览器的 deterministic demo：

```bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace
```

也可以从 PyPI 做持久安装：

```bash
pip install "browsertrace[ui]"
browsertrace doctor
browsertrace demo
browsertrace
```

打开：

```text
http://127.0.0.1:3000
```

点击：

```text
demo: checkout agent fails on disabled button
```

你会看到一个失败的 checkout agent trace。它不是为了展示复杂 UI，而是为了复现一个最小调试循环：agent 以为按钮可点，但页面状态实际上不允许继续。

如果你不想本地安装，也可以直接看导出的静态 trace：

```text
https://aaronlab.github.io/browsertrace/
```

如果你更关心公开分享时的隐私边界，可以先看这个 public-safe demo
HTML。它去掉了 prompt / model input/output、截图和 URL：

```text
https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html
```

## 在代码里怎么用

最简单的方式是 decorator：

```python
from browsertrace import trace

@trace
def my_agent(run, query: str):
    run.step(action=f"search: {query}", screenshot=...)
    run.step(action="click first result", screenshot=...)

my_agent("browser agent debugging")
```

如果你有 Playwright `page`，可以直接 snapshot：

```python
async with tracer.run("my-task") as run:
    await page.goto("https://example.com")
    await run.snapshot(page, action="opened example.com")
    await page.click("#login")
    await run.snapshot(page, action="clicked login")
```

也可以把 trace 导出成单个 HTML 文件：

```bash
browsertrace export <run_id> -o run.html
browsertrace export <run_id> --public -o public.html
```

这个 HTML 可以发给同事、贴到 issue、或者作为失败样例留档。如果要公开发真实 trace，用 `--public` 一次性去掉 prompt / model output、截图和 URL；只有在想保留某些字段时，才用单独的 redaction flag。

## 我现在最想要的反馈

这个项目还很早期，v0.1 的目标不是做一个大而全 observability 平台，而是先把一个很小但痛的 debug loop 做顺：

browser agent 失败以后，我能不能马上看到它当时看到的页面状态和模型决策？

如果你在做 Browser Use、Stagehand、Playwright + LLM、Skyvern 或 computer-use agent，我想知道：

- 你的 agent 失败时，当前日志最缺哪类信息？
- screenshot、DOM、selector、model input/output、workflow state，哪个最关键？
- 你希望 adapter 优先支持哪个框架？
- 本地 HTML export 是否够用，还是必须要 hosted share link？

反馈可以发在 launch discussion：

```text
https://github.com/aaronlab/browsertrace/discussions/6
```

或者直接开 integration request：

```text
https://github.com/aaronlab/browsertrace/issues/new?template=integration_request.yml
```

## 回复小贡献问题

如果有人问怎么做一个小的文档贡献，先给当前 good first issue：

```text
https://github.com/aaronlab/browsertrace/labels/good%20first%20issue
```

然后给 First PR Recipe：

```text
https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.
```

## 回复本地首跑 / CI / agent 调试问题

遇到 local first-run issues, CI failures, or AI/coding-agent troubleshooting replies 时，先问对方补充 debugging/workflow details；如果可以安全分享，再让对方贴这组 JSON CLI diagnostics：

如果涉及 security-sensitive reports or changes，或者包含 private trace data，先让对方走 Security Policy 里的私有路径，不要公开贴细节：
https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

## Stack 调试指南链接

如果中文教程的回复变成某个具体工作流的调试问题，优先给最接近的指南：

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## AOS mapping research 回复

如果有人问 BrowserTrace 和 OWASP AOS 的对应关系，保持研究口径：

- BrowserTrace is not an AOS compliance claim yet.
- Current AOS mapping research maps BrowserTrace concepts to tool request/result
  records, step correlation, URI-style screenshot/video artifacts, URL metadata,
  model I/O summaries, and explicit redaction state.
- Tracker: https://github.com/aaronlab/browsertrace/issues/237

不要把这段写成认证、审计通过、标准覆盖或任何互动请求。

## Links

GitHub:

```text
https://github.com/aaronlab/browsertrace
```

Live demo:

```text
https://aaronlab.github.io/browsertrace/
```

Walkthrough:

```text
https://aaronlab.github.io/browsertrace/debug-browser-agent-failure.html
```

Launch kit:

```text
https://aaronlab.github.io/browsertrace/launch/
```

Public-safe demo export:

```text
https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html
```
