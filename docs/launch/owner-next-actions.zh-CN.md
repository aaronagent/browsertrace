# BrowserTrace Owner 下一步动作

这是给 `aaronlab/browsertrace` 发布用的最短中文执行清单。这里列的都是
需要你本人登录账号、2FA、发帖或提交的动作。

不要买 star、刷 star、互赞、求 upvote、求转发。对外只问一件事：正在做
browser agent 的人，失败时最缺什么调试信息？

## 10 分钟 Owner 解锁顺序

如果你只有一小段时间，按这个顺序做；后面的验证、README 更新、指标记录和
issue comment 都交给 Codex 继续处理：

当前收录状态：已跟踪的外部 GitHub list 和 directory 投稿都还在 open，
上游默认分支里还没有正式收录 BrowserTrace。不要等这些 maintainer 合并后
再发 owner 渠道；先发个人账号内容和已经准备好的目录邮件。

最快的一条技术帖：先用 `docs/launch/channel-copy.md` 里的任意一个
Browser Use angle，可以放在 Day 1 正式帖子之前或一起发：
`#fresh-browser-use-debugging-angle` 针对 icon-only target 失败，
`#fresh-browser-use-remote-cdp-angle` 针对 remote-CDP hang 和 event-bus lock
timing。如果你的受众在做 custom computer-use agents，用
`#fresh-computer-use-persistent-browser-recovery-angle` 针对 persistent browser
session recovery。这些都是用具体失败场景来征集真实 workflow 反馈。

1. 用 `docs/launch/day-1-publish-packet.md` 发 X、LinkedIn、微信群、即刻，
   主素材用 `docs/demo.mp4`。平台支持 alt text 时，用
   `docs/launch/day-1-publish-packet.md#media-alt-text` 里的
   `Media Alt Text`。最短复制版在
   `docs/launch/owner-social-post-packet.md`。
2. 用 `docs/launch/directory-submission-sheet.md` 发送已经准备好的 owner
   email 投稿：发给 console.dev 的 `hello@console.dev`，以及发给 AgDex 的
   `agdex.ai@gmail.com`。最短复制版在
   `docs/launch/owner-email-send-packet.md`。
3. 如果还有第二小段时间，用 `docs/launch/directory-submission-sheet.md`
   提交这些浏览器表单目录：4agent.dev、AgentKart、OSS AI Hub、FOSSHUNTER、
   AgentsTide、BuilderAI Tools。AgentsTide 可用 `hello@agentstide.com`
   作为邮件兜底，BuilderAI Tools 分类用 `AI Observability & Evaluation`。
   这一批的字段已经整理在 `First Browser-Form Directory Field Notes`。如果
   AgentKart 或 AgentsTide 只接受可运行的 autonomous agent，不接受 agent
   开发工具，就跳过，不要把 BrowserTrace 硬归类成 agent。
4. 如果这一批已经做完，继续用 `docs/launch/directory-submission-sheet.md`
   里的第二批目录字段说明提交 CLIHunt、DeepYard、OpenAgent.bot、
   ForgeIndex、AgentShelf。
5. 如果还有时间做开发者工具目录，继续用同一个 sheet 提交 DevTool Center、
   ToolHunter、ToolShelf。CLIs.dev 已提交：
   https://github.com/victorcheeney/clis/issues/3；CliHub registry PR 已打开：
   https://github.com/clihub-ai/clihub/pull/1。

发完后，把帖子 URL、群名、邮件已发送备注或回复发给 Codex，我会记录指标并
更新跟踪 issue。

快速复制入口：

- Failure patterns page：
  `https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html`
- Fresh Browser Use angle：
  `docs/launch/channel-copy.md#fresh-browser-use-debugging-angle`
- Fresh Browser Use remote-CDP angle：
  `docs/launch/channel-copy.md#fresh-browser-use-remote-cdp-angle`
- Fresh computer-use persistent browser recovery angle：
  `docs/launch/channel-copy.md#fresh-computer-use-persistent-browser-recovery-angle`
- Fresh Chinese computer-use recovery angle：
  `docs/launch/channel-copy.md#fresh-chinese-computer-use-recovery-angle`
- X：`docs/launch/channel-copy.md#x`
- X follow-up：`docs/launch/channel-copy.md#x-follow-up`
- LinkedIn：`docs/launch/channel-copy.md#linkedin`
- 微信群：`docs/launch/channel-copy.md#wechat-group`
- 即刻：`docs/launch/channel-copy.md#jike`
- 5 分钟 owner 社交帖发送包：
  `docs/launch/owner-social-post-packet.md`
- Show HN：`docs/launch/day-2-show-hn-packet.md#first-comment-draft`
- Product Hunt：`docs/launch/day-4-product-hunt-packet.md#maker-comment`
- 5 分钟 HN/Product Hunt 提交包：
  `docs/launch/owner-launch-submission-packet.md`
- console.dev 邮件：
  `docs/launch/directory-submission-sheet.md#consoledev-email-draft`
- AgDex 邮件：`docs/launch/directory-submission-sheet.md#agdex-email-draft`
- 5 分钟 owner 邮件发送包：
  `docs/launch/owner-email-send-packet.md`
- 第一批浏览器表单目录：
  `docs/launch/directory-submission-sheet.md#first-browser-form-directory-field-notes`

Stack 调试指南：

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## 1. PyPI 已发布

PyPI 已经不再是安装阻塞。BrowserTrace 已发布为 `0.1.17`：

```text
https://pypi.org/project/browsertrace/
https://pypi.org/pypi/browsertrace/json -> HTTP 200
```

公开文案使用这个安装命令：

```bash
pip install "browsertrace[ui]"
```

无持久安装的 PyPI 试用路径：

```bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace list
uvx --from "browsertrace[ui]" browsertrace
```

发布验证已完成：

```bash
uv venv --python 3.11 --seed /tmp/browsertrace-pypi-verify
/tmp/browsertrace-pypi-verify/bin/python -m pip index versions browsertrace
/tmp/browsertrace-pypi-verify/bin/python -m pip install "browsertrace[ui]"
/tmp/browsertrace-pypi-verify/bin/browsertrace --help
uvx --python 3.11 --from "browsertrace[ui]" browsertrace doctor --json
```

跟踪 issue: https://github.com/aaronlab/browsertrace/issues/5

## 2. 维护 GitHub 个人 Profile README

当前真正会渲染个人主页的 profile repo 是 `aaronlab/aaronlab`。
发布文案里不要使用旧的 profile redirect。

正确的 repo 是：

```text
aaronlab/aaronlab
```

刷新 README 时使用这个源草稿：

```text
docs/launch/github-profile-readme.md
```

Profile pin：已完成。GraphQL 现在可以看到 `aaronlab/browsertrace` 已经在
公开 profile pinned repositories 里。

跟踪 issue: https://github.com/aaronlab/browsertrace/issues/13

## 3. GitHub Social Preview

Social preview：已完成。GitHub 现在对 `aaronlab/browsertrace` 返回
`usesCustomOpenGraphImage=true`。

以后 Product Hunt 图集、发布素材、链接预览测试仍然复用这个文件：

```text
docs/social-preview.png
```

## 4. 提交搜索引擎收录

sitemap 和 robots 已经在线：

```text
https://aaronlab.github.io/browsertrace/sitemap.xml
https://aaronlab.github.io/browsertrace/robots.txt
```

按这个文件操作：

```text
docs/launch/search-indexing-submission.md
```

跟踪 issue: https://github.com/aaronlab/browsertrace/issues/16

## 5. 发 Day 1 warm launch

使用：

```text
docs/launch/day-1-publish-packet.md
docs/launch/channel-copy.md
```

推荐顺序：

1. X
2. LinkedIn
3. 一两个真正相关的微信 AI builder 群
4. 即刻

主素材用：

```text
docs/demo.mp4
```

备用图：

```text
docs/demo-poster.png
```

跟踪 issue: https://github.com/aaronlab/browsertrace/issues/9

## 6. 提交目录、newsletter、awesome lists

目录和 newsletter：

```text
docs/launch/directory-submission-sheet.md
docs/launch/outreach-targets.md
```

GitHub awesome lists：

```text
docs/launch/github-awesome-list-submissions.md
```

已经打开的 PR：

| 目标 | PR |
|---|---|
| `bradvin/agentfirst.directory` | `https://github.com/bradvin/agentfirst.directory/pull/30`，enrichment check 已通过 |
| `angrykoala/awesome-browser-automation` | `https://github.com/angrykoala/awesome-browser-automation/pull/112` |
| `mxschmitt/awesome-playwright` | `https://github.com/mxschmitt/awesome-playwright/pull/136` |
| `Jenqyang/Awesome-AI-Agents` | `https://github.com/Jenqyang/Awesome-AI-Agents/pull/220` |
| `wjhou/awesome-computer-use-agents` | `https://github.com/wjhou/awesome-computer-use-agents/pull/2` |
| `cdxeve/awesome-computer-use-agents` | `https://github.com/cdxeve/awesome-computer-use-agents/pull/2` |
| `steel-dev/awesome-web-agents` | `https://github.com/steel-dev/awesome-web-agents/pull/56` |
| `ai-boost/awesome-harness-engineering` | `https://github.com/ai-boost/awesome-harness-engineering/pull/23` |
| `Agent-Tools/awesome-autonomous-web` | `https://github.com/Agent-Tools/awesome-autonomous-web/pull/21` |
| `e2b-dev/awesome-ai-sdks` | `https://github.com/e2b-dev/awesome-ai-sdks/pull/187`，CLA 已通过，继续等待维护者反馈 |
| `jim-schwoebel/awesome_ai_agents` | `https://github.com/jim-schwoebel/awesome_ai_agents/pull/266` |
| `ranpox/awesome-computer-use` | `https://github.com/ranpox/awesome-computer-use/pull/24` |
| `trycua/acu` | `https://github.com/trycua/acu/pull/26` |
| `clihub-ai/clihub` | `https://github.com/clihub-ai/clihub/pull/1`，registry PR 已打开，forked PR CI 需要维护者批准后才能运行 |
| `victorcheeney/clis` | `https://github.com/victorcheeney/clis/issues/3`，CLIs.dev 目录 issue 已打开 |

现在只监控维护者反馈；不要再追加新的 awesome-list PR，除非先确认目标高度匹配、非重复，并且不会变成低质量群发。

目录/newsletter 跟踪 issue: https://github.com/aaronlab/browsertrace/issues/10

Awesome list 跟踪 issue: https://github.com/aaronlab/browsertrace/issues/18

## 回复小贡献问题

如果有人问怎么做一个小的文档贡献，先给当前 good first issue 队列：

```text
https://github.com/aaronlab/browsertrace/labels/good%20first%20issue
```

然后给 First PR Recipe：

```text
https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.
```

如果对方说想做这个任务，先回复确认并留出一个短的认领窗口，不要马上自己实现同一个 issue。如果 GitHub 不能把 issue assign 给这个贡献者，就加 `claimed` label，避免其他人重复接同一个任务。如果这个任务已经完成，改为指向当前 good first issue。

## 回复本地首跑 / CI / agent 调试问题

遇到 local first-run issues, CI failures, or AI/coding-agent troubleshooting replies 时，先问对方补充 debugging/workflow details；如果可以安全分享，再让对方贴这组 JSON CLI diagnostics：

如果问题涉及 security-sensitive reports or changes 或 private trace data，先让对方走 Security Policy，不要公开贴敏感细节：
https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

### Stack 调试指南链接

当回复变成具体工作流调试问题时，优先给最贴近的指南：

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

### AOS mapping research 回复

如果有人问 BrowserTrace 和 OWASP AOS 的对应关系，保持研究口径：

- BrowserTrace is not an AOS compliance claim yet.
- Current AOS mapping research maps BrowserTrace concepts to tool request/result
  records, step correlation, URI-style screenshot/video artifacts, URL metadata,
  model I/O summaries, and explicit redaction state.
- Tracker: https://github.com/aaronlab/browsertrace/issues/237

不要把这段写成认证、审计通过、标准覆盖或任何互动请求。

## 7. 每做完一个动作就记录指标

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after <action>: <URL or note>"
uv run --python 3.11 python scripts/launch_metrics.py --json
```

目标只有一个：GitHub 实时显示超过 1000 stars 才算完成。

```bash
gh repo view aaronlab/browsertrace --json stargazerCount,forkCount,watchers,url,homepageUrl
```
