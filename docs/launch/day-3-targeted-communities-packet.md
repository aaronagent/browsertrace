# BrowserTrace Day 3 Targeted Communities Packet

Use this after Day 1 warm posts and only if the owner can reply to technical
questions. The goal is to reach builders who already work with browser agents,
not to post a generic product announcement.

Entry points checked:

- Browser Use Discussions: https://github.com/browser-use/browser-use/discussions
- Stagehand Discussions: https://github.com/browserbase/stagehand/discussions
- Stagehand Discord: https://discord.gg/stagehand
- Playwright community: https://playwright.dev/community/welcome
- Skyvern Discussions: https://github.com/Skyvern-AI/skyvern/discussions
- AgentKart submit: https://www.agentkart.ai/submit
- console.dev: https://console.dev/

## Preflight Gate

Run:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "before Day 3 targeted communities"
```

Submit only if all are true:

- The owner can reply to technical questions the same day.
- The post asks for adapter/workflow feedback, not stars.
- The post is customized to the community and does not look cross-posted.
- The post uses the walkthrough or live demo before asking people to install.
- If someone asks how to try it locally, use
  the PyPI `uvx` path:

```bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace
```

- The public-safe demo export is used when someone asks for a downloadable
  artifact that omits prompts, model output, screenshots, and URLs.
- The community allows this kind of post or there is an existing relevant thread.

Do not post if:

- The only available angle is "please check out my repo."
- The community rules prohibit self-promotion.
- There is already a similar unanswered post from the owner.
- The owner cannot follow up.

Current posted threads, for monitoring only:

- Browser Use: https://github.com/browser-use/browser-use/discussions/4816
- Stagehand: https://github.com/browserbase/stagehand/discussions/2102
- Skyvern: https://github.com/Skyvern-AI/skyvern/discussions/5931

Technical link for future targeted replies:
https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html

Do not repost to those three communities unless a maintainer asks for a new
thread or the original thread receives concrete feedback that needs a follow-up.

## Priority Order

1. Browser Use Discussions
2. Stagehand Discussions or Discord
3. Playwright community channels
4. Skyvern Discussions
5. Directory/newsletter submissions that do not require community discussion

Stop after one or two posts if the replies are low quality or negative. Improve
the message before posting anywhere else.

## Browser Use

Best place: GitHub Discussions, preferably a Show and tell, Ideas, or Q&A-style
thread if the category is available.

Title:

```text
Feedback wanted: local traces for failed Browser Use runs
```

Body:

```text
I'm building BrowserTrace, a small local trace viewer for browser-agent failures:
screenshots, URL, action, model input/output, status, and failed-step errors in
one timeline.

The debugging problem I want to solve for Browser Use users is: the agent fails
deep into a run, but the logs do not show what the browser looked like or which
model output caused the wrong action.

Browser Use guide:
https://aaronlab.github.io/browsertrace/browser-use-debugging.html

Live exported trace:
https://aaronlab.github.io/browsertrace/trace.html

Repo:
https://github.com/aaronlab/browsertrace

Browser Use adapter feedback issue:
https://github.com/aaronlab/browsertrace/issues/11

For Browser Use specifically, what would be most useful to capture?

- Agent task and step number
- Browser screenshot
- URL
- Action/tool call
- Model input and output
- Selector or target element
- DOM/extracted text
- Retry state or memory

I'm trying to decide what the Browser Use adapter should capture first.
```

Metrics:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after Browser Use discussion: <URL>"
```

## Stagehand

Best place: GitHub Discussions or Stagehand Discord, where allowed.

Title:

```text
Would a local timeline help debug failed Stagehand act/extract runs?
```

Body:

```text
I'm building BrowserTrace, a local debugger for AI browser-agent runs. It records
each step as a timeline: screenshot, URL, action, model input/output, status,
and error.

For Stagehand users, I'm trying to understand which calls are most important to
wrap first:

- act()
- extract()
- observe()
- agent()
- lower-level Playwright page actions

Stagehand guide:
https://aaronlab.github.io/browsertrace/stagehand-debugging.html

Live exported trace:
https://aaronlab.github.io/browsertrace/trace.html

Repo:
https://github.com/aaronlab/browsertrace

Stagehand adapter feedback issue:
https://github.com/aaronlab/browsertrace/issues/8

If you have debugged a failed Stagehand run, what state did you wish you had at
failure time?
```

Metrics:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after Stagehand post: <URL>"
```

## Playwright

Playwright is broader than AI agents. Do not present BrowserTrace as a
replacement for Playwright Trace Viewer. Share only where the question is about
LLM-guided browser automation, agents, or missing model-decision context.

Best angles:

- Playwright + LLM scripts
- Browser tests where an LLM chooses the next action
- Debugging screenshots plus model output
- Exporting a standalone failure trace for an issue

Short reply for relevant threads:

```text
If the missing piece is the LLM decision context rather than Playwright's browser
trace itself, I'm building a small local tool for that case:

Playwright + LLM guide:
https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html

Live exported trace:
https://aaronlab.github.io/browsertrace/trace.html

Repo:
https://github.com/aaronlab/browsertrace

Playwright + LLM feedback issue:
https://github.com/aaronlab/browsertrace/issues/12

It records screenshot, URL, action label, model input/output, and failed-step
error into a local timeline. It is not a replacement for Playwright Trace Viewer;
it is for Playwright scripts where an LLM is part of the control loop.
```

Metrics:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after Playwright community reply: <URL>"
```

## Skyvern

Best place: GitHub Discussions, or a relevant adapter/workflow thread. Do not
hijack unrelated bug reports.

Title:

```text
Feedback wanted: what should a Skyvern trace adapter capture?
```

Body:

```text
I'm building BrowserTrace, a local timeline/debugger for failed AI browser-agent
runs. It records screenshots, URL, action, model input/output, status, and
failed-step errors.

BrowserTrace now has a basic Skyvern wrapper for high-level task/workflow calls.
I want to know what a deeper adapter should capture to debug failed workflows:

- screenshots
- workflow state
- task prompt
- model output
- selected element or selector
- browser URL
- retry/history state
- extracted data

Skyvern guide:
https://aaronlab.github.io/browsertrace/skyvern-debugging.html

Live exported trace:
https://aaronlab.github.io/browsertrace/trace.html

Repo:
https://github.com/aaronlab/browsertrace

Skyvern adapter feedback issue:
https://github.com/aaronlab/browsertrace/issues/4

Which artifacts would be most useful when a Skyvern workflow fails?
```

Metrics:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after Skyvern discussion: <URL>"
```

## Custom Computer-Use Agents

Use this only in communities or existing threads where people are building
custom computer-use agents, persistent browser profiles, or local browser
session recovery logic.

Short reply for relevant threads:

```text
If the failure happens before the first screenshot or URL exists, I would trace
the persistent browser recovery boundary instead of only the agent step:

- session_mode
- redacted profile id
- profile lock or stale process signal
- CDP attach/probe timing and timeout
- approval source and recovery action
- final connection state

Computer-use guide:
https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

Repo:
https://github.com/aaronlab/browsertrace
```

Metrics:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after computer-use community reply: <URL>"
```

## Directories And Newsletters

Use these after `v0.1.17` because the release has the packaged demo command and
safer redacted export path.

Use `docs/launch/directory-submission-sheet.md` for exact entry points, link
order, owner-only notes, and tracking instructions.

Best targets:

- AgentKart: open-source AI agent marketplace submission; try from the owner
  login.
- OSS AI Hub: open-source AI tools directory with a JavaScript submission page.
- FOSSHUNTER: open-source tool discovery; submit once from the owner account.
- AgentsTide: AI agents and browser-agent directory; use the visible submit
  path, with `hello@agentstide.com` as email fallback.
- AgentsIndex: AI agent tool directory; submit after owner sign-in under
  Observability and Monitoring.
- BuilderAI Tools: open-source AI developer tools directory; use
  `AI Observability & Evaluation`.
- CLIHunt: AI agent and developer-tool registry; use category Other if no
  developer-tools category is available.
- DeepYard: OSS-first AI agent directory; use category Dev Tools.
- OpenAgent.bot: open AI stack directory; submit BrowserTrace as a Tool with
  repo, license, docs, and use-case details.
- ForgeIndex: open-source local AI project index; use the Local Agents &
  Automation fit.
- AgentShelf: AI agent and tool directory; use Coding & Development or
  Autonomous Agents after owner sign-up.
- CLIs.dev: CLI discovery for AI agents and automation; include the `uvx`
  install command and JSON troubleshooting commands.
- DevTool Center: developer-tool directory; use free/open-source pricing and
  debugging/observability tags.
- ToolHunter: developer tools, AI agents, and open-source CLI directory.
- ToolShelf: curated developer tools directory; use CLI Tools, AI Coding, or
  Developer Productivity depending on the category picker.
- AgDex: AI agent tools directory; developer tools and observability is the best
  category fit.
- Agent Hub: agent/MCP/skill directory; use only if they accept tool suggestions.
- agentfirst.directory: agent-first tooling directory with a Browser Automation
  category.
- console.dev: devtools newsletter; send an editorial pitch only once and
  mention the self-service live demo/PyPI trial plus redacted export path.

Pitch:

````text
BrowserTrace is an MIT local debugger for AI browser agents. It records each
Browser Use / Stagehand / Skyvern / Playwright + LLM step as a timeline:
screenshot, URL, action, model input/output, status, and error.

The v0.1.17 release includes `browsertrace demo` for first-run onboarding,
`browsertrace export --public` for public-safe sharing, and individual
redaction flags when users want to keep some fields visible.

Try locally from PyPI:

```bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace
```

Repo: https://github.com/aaronlab/browsertrace
Live demo: https://aaronlab.github.io/browsertrace/
Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html
Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
Release: https://github.com/aaronlab/browsertrace/releases/tag/v0.1.17
````

Metrics:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after directory/newsletter submission: <target or URL>"
```

## Triage After Posting

Within 24 hours:

- Convert specific adapter requests into GitHub issues.
- Link each issue from the relevant discussion reply.
- Add useful quotes or summaries to `docs/launch/metrics-log.md`.
- Update the v0.2 milestone if a clear adapter priority emerges.
- For local first-run issues, CI failures, or AI/coding-agent troubleshooting replies, ask for debugging/workflow details plus JSON CLI diagnostics when safe to share:

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

- For small first contributions, start with the good first issue label:
  https://github.com/aaronlab/browsertrace/labels/good%20first%20issue
  Then link the First PR Recipe:
  https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.

## Stack-Specific Reply Links

Use the closest guide when a targeted-community reply turns into a
workflow-specific debugging question:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## Stop Rules

- Do not post in more than two targeted communities on the same day unless
  replies are clearly useful.
- Do not paste identical text across communities.
- Do not argue with moderators or community regulars.
- Do not ask for stars, upvotes, follows, reposts, or "support."
- If a post is removed, do not repost it; learn from the reason and move on.
