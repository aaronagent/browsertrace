# BrowserTrace Directory And Newsletter Submission Sheet

Use this sheet after `v0.1.17`. Submit only where the target accepts tool
suggestions, launches, or editorial pitches. Do not ask for stars, votes,
upvotes, swaps, or artificial engagement.

## Canonical Links

- Repo: https://github.com/aaronlab/browsertrace
- Live demo: https://aaronlab.github.io/browsertrace/
- Raw trace: https://aaronlab.github.io/browsertrace/trace.html
- Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
- Comparison: https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html
- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Release: https://github.com/aaronlab/browsertrace/releases/tag/v0.1.17
- Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html

## Try-It Commands

Use the PyPI `uvx` path first in directory replies when an editor asks how to try the project:

```bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace list
uvx --from "browsertrace[ui]" browsertrace
```

Persistent install from PyPI:

```bash
pip install "browsertrace[ui]"
browsertrace demo
browsertrace
```

## One-Line Pitch

BrowserTrace is a local flight recorder for AI browser agents: screenshots,
URLs, actions, model input/output, status, errors, and standalone HTML exports
for failed Browser Use, Stagehand, Skyvern, Playwright + LLM, and computer-use
runs.

## Short Submission Description

BrowserTrace is an MIT-licensed local debugger for AI browser agents. It records
each browser-agent step as a timeline with screenshot, URL, action, model
input/output, status, and error, then exports a standalone HTML trace with
optional redaction. The `v0.1.17` release includes the public-safe
`browsertrace export --public` mode, a packaged `browsertrace demo` command,
Browser Use/Stagehand/Skyvern/Playwright guides, and a no-dependency Browser
Use-shaped callback demo.

## Submission Queue

| Target | Fit | Entry point | Owner-only? | Link order | Status |
|---|---|---|---:|---|---|
| Product Hunt | Broad launch audience once assets and comments are ready | Product Hunt maker dashboard | Yes | Live demo, release, repo | Not submitted |
| Hacker News Show HN | OSS/devtools developers | https://news.ycombinator.com/submit | Yes | Repo, live demo, comparison | Not submitted |
| console.dev | Devtools newsletter readers | https://console.dev/ | Yes, from owner email/contact | Live demo, repo, comparison | Not submitted |
| AgentKart | Open-source AI agent marketplace readers | https://www.agentkart.ai/submit | Yes, owner account likely | Repo, live demo, Browser Use guide | Owner login likely required; Submit Agent form asks for agent name, description, and GitHub repository; skip if only runnable autonomous agents are accepted |
| Agent Hub | Agent/MCP/skill directory readers | https://agent-hub.dev/ | Unknown | Live demo, repo, integrations | Blocked: no visible submit/contact route |
| AgDex | AI agent ecosystem directory readers | https://agdex.ai/ | Yes, owner email | Live demo, repo, comparison | Contact page accepts tool submissions; send owner-email pitch to agdex.ai@gmail.com |
| AgentsIndex | AI agent tool directory with observability category | https://agentsindex.ai/submit | Yes, owner sign-in | Live demo, repo, public-safe export | Submit tool after owner sign-in; use Observability and Monitoring fit and local-first browser-agent debugging angle |
| 4agent.dev | Agent-builder tool directory readers | https://4agent.dev/submit | Yes, browser submission | Live demo, repo, Browser Use guide | Submit Tool form is visible; use Observability or Browser category, and tags such as browser agents, debugging, Playwright, tracing |
| agentfirst.directory | Agent-first tooling ecosystem | https://agentfirst.directory/ | Maybe | Comparison, live demo, repo | Submitted PR: https://github.com/bradvin/agentfirst.directory/pull/30 |
| OSS AI Hub | Open-source AI tools and agents | https://ossaihub.com/submit | Yes, browser submission | Repo, live demo, public-safe export | JavaScript submission page; submissions are reviewed for quality, relevance, and community value |
| FOSSHUNTER | Open-source tool discovery | https://fosshunter.com/submit | Yes, login required | Repo, live demo, release | Not submitted |
| AgentsTide | AI agents and browser-agent directory | https://agentstide.com/ | Yes, owner action | Live demo, repo, Browser Use guide | Submit Free Listing link visible; use owner email fallback at hello@agentstide.com |
| BuilderAI Tools | Open-source AI developer tools | https://builderai.tools/submit | Yes, owner email required | Repo, live demo, public-safe export | Submit Tool for Review form; use AI Observability & Evaluation; limit is 3 submissions per day |
| CLIHunt | AI agent and developer-tool registry | https://clihunt.dev/ | Yes, owner account/form | Repo, install command, live demo | Submit Tool form accepts name, tagline, GitHub URL, category, and install command; use category Other if no developer-tools category is available |
| DeepYard | OSS-first AI agent and developer-tool directory | https://deepyard.dev/submit | Yes, browser submission | Repo, live demo, public-safe export | Submit a Tool page includes Dev Tools; submissions are reviewed before listing |
| OpenAgent.bot | Open AI stack project directory | https://openagent.bot/submit/ | Yes, browser submission | Repo, license/docs, live demo | Submit project as Tools; clear source, license, docs, and use-case details help review |
| ForgeIndex | Open-source local AI project index | https://forgeindex.ai/ | Yes, owner Google form | Repo, live demo, local-first positioning | Official form; use Local Agents & Automation fit and local-first debugging angle |
| AgentShelf | AI agent and tool directory | https://www.agentshelf.io/submit | Yes, owner account likely | Live demo, repo, Browser Use guide | List your AI tool path requires sign-up; use Coding & Development or Autonomous Agents when category is requested |
| CLIs.dev | CLI discovery for AI agents and automation | https://clis.dev/submit | No further owner action | Repo, install command, PyPI | Submitted issue: https://github.com/victorcheeney/clis/issues/3 |
| DevTool Center | Developer tools directory | https://www.devtool.center/submit | Yes, browser submission | Live demo, repo, docs | Submit Tool form asks for name, description, URL, category, pricing, and tags; use Developer Tools / free or open source fit |
| ToolHunter | Developer tools, AI agents, and open-source CLI directory | https://www.toolhunter.cc/ | Yes, browser submission | Repo, live demo, PyPI | Submit a Tool; use developer tools, AI agents, open-source CLI utilities angle |
| ToolShelf | Curated developer tools directory with CLI and AI coding categories | https://toolshelf.dev/ | Yes, browser submission | Repo, docs, PyPI | Submit a Tool; use CLI Tools, AI Coding, or Developer Productivity depending on category choices |
| CliHub | Agent-facing structured CLI registry | https://github.com/clihub-ai/clihub | No further owner action | Repo, PyPI, JSON CLI hints | Submitted PR: https://github.com/clihub-ai/clihub/pull/1; forked PR CI is action_required pending maintainer approval |
| GitHub awesome lists | Curated developer discovery lists | docs/launch/github-awesome-list-submissions.md | Yes | Repo, live demo, relevant guide | Tracked PRs are open, including Scottcjn/awesome-agents#16; monitor feedback; e2b CLA passed |
| Browser Use Discussions | Browser-agent practitioners | https://github.com/browser-use/browser-use/discussions/4816 | Yes | Browser Use guide, live trace, repo | Posted; no comments yet |
| Stagehand Discussions | Browser automation and agent builders | https://github.com/browserbase/stagehand/discussions/2102 | Yes | Stagehand guide, live trace, repo | Posted; no comments yet |
| Skyvern Discussions | Browser automation agent users | https://github.com/Skyvern-AI/skyvern/discussions/5931 | Yes | Skyvern guide, live trace, repo | Posted; no comments yet |

## First Browser-Form Directory Field Notes

Use these after the Day 1 posts and owner-email submissions. Submit once from
the owner's browser, and keep the ask to directory inclusion or editorial
feedback.

4agent.dev:

```text
Tool name: BrowserTrace
Website URL: https://aaronlab.github.io/browsertrace/
Repository: https://github.com/aaronlab/browsertrace
Category: Observability, or Browser if only one category is accepted
Tags: browser agents, debugging, Playwright, Browser Use, trace viewer
Short description: Local-first trace viewer for failed AI browser-agent runs, with screenshots, URLs, actions, model I/O, errors, and public-safe HTML exports.
```

AgentsIndex:

```text
Tool name: BrowserTrace
Website URL: https://aaronlab.github.io/browsertrace/
Repository: https://github.com/aaronlab/browsertrace
Category: Observability and Monitoring
Short description:
Local-first trace viewer for debugging failed AI browser-agent and computer-use
runs with screenshots, URLs, actions, model I/O, status, errors, and redacted
shareable HTML exports.
Owner note: submit from the owner's signed-in browser session at
https://agentsindex.ai/submit.
```

AgentKart:

```text
Agent Name: BrowserTrace
Description:
BrowserTrace is not an autonomous agent; it is an MIT-licensed debugging tool
for AI browser-agent projects. It records failed Browser Use, Stagehand,
Skyvern, Playwright + LLM, and custom computer-use runs with screenshots, URLs,
actions, model I/O, status, errors, and public-safe HTML exports.
GitHub Repository: https://github.com/aaronlab/browsertrace
Owner note: if AgentKart only accepts runnable autonomous agents, skip this
submission instead of misclassifying BrowserTrace. Owner login likely required.
```

OSS AI Hub:

```text
Tool name: BrowserTrace
Website URL: https://aaronlab.github.io/browsertrace/
GitHub URL: https://github.com/aaronlab/browsertrace
Category: Developer Tools, AI Agents, or Observability if offered
Short description:
Open-source local trace viewer for debugging failed AI browser-agent and
computer-use runs.
Full description:
BrowserTrace records screenshots, URLs, actions, model input/output, status,
and errors for Browser Use, Stagehand, Skyvern, Playwright + LLM, and custom
computer-use workflows. It runs locally, includes a PyPI package, and can export
public-safe HTML traces for sharing without sensitive screenshots, URLs,
prompts, or model output.
```

FOSSHUNTER:

```text
Tool name: BrowserTrace
Repository: https://github.com/aaronlab/browsertrace
Website: https://aaronlab.github.io/browsertrace/
Category: Agentic Development, or AI Automation if Agentic Development is not available
Short description:
MIT-licensed local debugger for AI browser-agent failures, with screenshots,
URLs, actions, model I/O, errors, and redacted HTML exports.
Owner note: login is required before the submit form is available.
```

AgentsTide:

```text
Agent/tool name: BrowserTrace
Website: https://aaronlab.github.io/browsertrace/
Repository: https://github.com/aaronlab/browsertrace
Category: Browser Agents, or Coding if Browser Agents is not available
Pricing: Free / open source
Short description:
BrowserTrace is a local debugging tool for teams building browser agents. It
records the failed-step timeline for Browser Use, Stagehand, Skyvern,
Playwright + LLM, and custom computer-use runs, then exports public-safe HTML
traces for review.
Owner note: if AgentsTide only accepts autonomous agent products, submit only
as a browser-agent developer tool or skip.
```

BuilderAI Tools:

```text
Tool Name: BrowserTrace
Website URL: https://aaronlab.github.io/browsertrace/
GitHub URL: https://github.com/aaronlab/browsertrace
Description:
BrowserTrace is an MIT-licensed local debugger for failed AI browser-agent
runs. It records screenshots, URLs, actions, model I/O, status, errors, and
exports public-safe HTML traces for Browser Use, Stagehand, Skyvern,
Playwright + LLM, and custom computer-use workflows.
Category: AI Observability & Evaluation
Tags: browser agents, debugging, observability, Playwright, open source
Your Email: use the owner's email address
```

## Second-Pass Directory Field Notes

Use these only after the first directory/email batch is submitted. Submit once,
from the owner's account or browser, and wait for review.

CLIHunt:

```text
Name: BrowserTrace
Tagline: Local trace viewer for AI browser agents
GitHub URL or Website: https://github.com/aaronlab/browsertrace
Category: Other
Install Command: uvx --from "browsertrace[ui]" browsertrace
Optional demo command: uvx --from "browsertrace[ui]" browsertrace demo
Open UI after demo: uvx --from "browsertrace[ui]" browsertrace
```

DeepYard:

```text
Tool Name: BrowserTrace
Website / GitHub URL: https://github.com/aaronlab/browsertrace
Category: Dev Tools
Description: BrowserTrace is an MIT-licensed local trace viewer for failed AI browser-agent runs, with screenshots, URLs, actions, model I/O, errors, and public-safe HTML exports.
```

OpenAgent.bot:

```text
Project name: BrowserTrace
Repository URL: https://github.com/aaronlab/browsertrace
Homepage URL: https://aaronlab.github.io/browsertrace/
Category: Tools
Summary: Local-first trace viewer for debugging Browser Use, Stagehand, Skyvern, Playwright + LLM, and custom computer-use agent runs.
```

ForgeIndex:

```text
Project: BrowserTrace
Topic fit: Local Agents & Automation
Repository: https://github.com/aaronlab/browsertrace
Homepage: https://aaronlab.github.io/browsertrace/
Summary: Open-source local debugger for AI browser-agent failures, with redacted shareable exports.
```

AgentShelf:

```text
Tool name: BrowserTrace
Category: Coding & Development, or Autonomous Agents if only agent categories are available
Website: https://aaronlab.github.io/browsertrace/
Repository: https://github.com/aaronlab/browsertrace
Short description: Local flight recorder for AI browser-agent failures.
```

Developer-tool directory addendum:

```text
CLIs.dev: submitted as https://github.com/victorcheeney/clis/issues/3; monitor for maintainer review and avoid duplicate submission.
CliHub: submitted as https://github.com/clihub-ai/clihub/pull/1; monitor for maintainer review and wait for CI approval on the forked PR.
DevTool Center: use Developer Tools, free/open-source pricing, and tags such as AI agents, debugging, observability, Playwright, CLI.
ToolHunter: use developer tools, AI agents, and open-source CLI utilities positioning.
ToolShelf: use CLI Tools, AI Coding, or Developer Productivity depending on the category picker.
```

CLIs.dev GitHub issue template fields:

```text
Title: Add CLI: BrowserTrace
CLI Name: BrowserTrace
Canonical Source URL: https://github.com/aaronlab/browsertrace
Category: AI & LLM Tools
Install Command: pip install "browsertrace[ui]"
Website or Docs URL: https://aaronlab.github.io/browsertrace/
Description:
BrowserTrace is an MIT-licensed local CLI and web UI for debugging AI
browser-agent failures. It records Browser Use, Stagehand, Skyvern,
Playwright + LLM, and custom computer-use runs as timelines with screenshots,
URLs, action labels, model input/output, status, errors, and public-safe HTML
exports. It is useful for humans and agents because `browsertrace doctor
--json`, `browsertrace list --json`, and `browsertrace show <run_id> --json`
provide machine-readable diagnostics, while the local UI helps inspect the
failed browser step.
Agent Compatibility: check "Supports JSON Output (--json flag or similar)"
Language: Python
Source Type: Open-source CLI
```

DevTool Center submit fields:

```text
Tool Name: BrowserTrace
Description:
BrowserTrace is an MIT-licensed local debugger for failed AI browser-agent runs. It records screenshots, URLs, actions, model I/O, status, errors, and exports public-safe HTML traces for Browser Use, Stagehand, Skyvern, Playwright + LLM, and custom computer-use workflows.
Tool URL: https://aaronlab.github.io/browsertrace/
Category: AI Helpers
Pricing: Free
Tags: AI agents, debugging, observability, Playwright, CLI
```

ToolHunter submit guidance:

```text
Tool name: BrowserTrace
Tagline: Local debugger for AI browser-agent failures
Website: https://aaronlab.github.io/browsertrace/
Repository: https://github.com/aaronlab/browsertrace
Category or positioning: Developer Tools, AI agents, open-source CLI utilities
Short description:
BrowserTrace is an MIT-licensed local trace viewer for failed Browser Use,
Stagehand, Skyvern, Playwright + LLM, and custom computer-use runs. It records
screenshots, URLs, actions, model I/O, status, errors, and public-safe HTML
exports.
Install command: pip install "browsertrace[ui]"
```

ToolShelf submit guidance:

```text
Tool name: BrowserTrace
Tagline: Replay failed AI browser-agent runs
Website: https://aaronlab.github.io/browsertrace/
Repository: https://github.com/aaronlab/browsertrace
Category: CLI Tools, or AI Coding if only one category is accepted
Pricing/license: Free, open source, MIT
Short description:
Local-first CLI and web UI for debugging AI browser-agent failures with
screenshots, URLs, actions, model I/O, error status, and redacted HTML exports.
Tags: CLI, AI agents, debugging, observability, Playwright
```

## Product Hunt Draft

Tagline:

```text
Local flight recorder for AI browser agents
```

Description:

```text
BrowserTrace records failed AI browser-agent runs locally: screenshots, URLs,
actions, model input/output, status, and errors. Open a step timeline, jump to
the first failed browser state, and export a standalone HTML trace with optional
redaction.
```

Maker comment:

```text
I built BrowserTrace because browser-agent failures are usually not explained by
logs alone. When a Browser Use, Stagehand, Skyvern, or Playwright + LLM run
fails, I want the screenshot, URL, action, model decision, and first error in
one local timeline.

The current release is intentionally small and OSS. The most useful feedback is:
what browser state do your current agent logs miss at failure time?
```

## Directory Pitch

Subject:

```text
BrowserTrace: local flight recorder for AI browser agents
```

Body:

```text
BrowserTrace is an MIT-licensed local debugger for AI browser agents.

It records each browser-agent step as a timeline with screenshot, URL, action,
model input/output, status, and error, then exports a standalone HTML trace with
optional redaction.

It is useful for Browser Use, Stagehand, Skyvern, Playwright + LLM scripts, and
custom computer-use agents.

Repo: https://github.com/aaronlab/browsertrace
Live demo: https://aaronlab.github.io/browsertrace/
Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html
Comparison: https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html
Release: https://github.com/aaronlab/browsertrace/releases/tag/v0.1.17
```

## console.dev Email Draft

Use this only from the owner's email account. console.dev features interesting
developer tools and beta releases; this is not a sponsored review request.

```text
To: hello@console.dev
Subject: Devtools suggestion: BrowserTrace

Hi console.dev team,

I wanted to suggest BrowserTrace for your developer tools queue.

BrowserTrace is an MIT-licensed local debugger for AI browser-agent runs. It
records each browser-agent step as a timeline with screenshot, URL, action,
model input/output, status, and error, then exports a standalone HTML trace
with optional redaction.

A concrete failure case: a Browser Use agent can see the right plus icon in a
screenshot, but click a nearby toolbar button because the tooltip text is not an
accessible name. BrowserTrace keeps the screenshot, URL, action, model decision,
and failed-step evidence together so that kind of bug can be inspected.

Another failure case: remote CDP state collection can hang while the websocket
still appears open, and event-bus lock timing can decide whether one stale
browser session blocks others. BrowserTrace is aimed at keeping that kind of
method timing, browser/session evidence, and failed-step context inspectable.

A third failure case: persistent browser recovery can fail before any screenshot
or URL exists. BrowserTrace docs now call out the useful setup evidence:
session_mode, redacted profile id, profile lock or stale process signal,
CDP attach/probe timing, recovery action, and final connection state.

Why it may fit console.dev:
- It is interesting and useful to developers building Browser Use, Stagehand,
  Skyvern, Playwright + LLM, or custom computer-use agents.
- It can be a regular-use developer tool for investigating failed AI browser
  automation runs, especially when logs do not show what the agent saw.
- It is self-service: live demo, PyPI install, and no signup or sales call are
  required to try the local demo.
- It is local-first and open source, with a public-safe export path for sharing
  traces without prompts, screenshots, URLs, or model output.

Repo: https://github.com/aaronlab/browsertrace
Live demo: https://aaronlab.github.io/browsertrace/
Comparison: https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html
Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html

This is not a sponsored review request. I would value any editorial feedback if
it is not a fit.
```

Do not ask for stars, votes, backlinks, or reciprocal placement. The ask is
only editorial consideration for a relevant developer tool.

## AgDex Email Draft

Use this only from the owner's email account.

```text
To: agdex.ai@gmail.com
Subject: Tool submission: BrowserTrace

Tool name: BrowserTrace
Website URL: https://aaronlab.github.io/browsertrace/
Category: Developer tools / observability

Short description:
BrowserTrace is an MIT-licensed local debugger for AI browser-agent runs. It
records each browser-agent step as a timeline with screenshot, URL, action,
model input/output, status, and error, then exports a standalone HTML trace
with optional redaction. It is useful for Browser Use, Stagehand, Skyvern,
Playwright + LLM scripts, and custom computer-use agents.

Example use case: debugging a Browser Use run where the screenshot shows the
right plus icon, but the agent clicks a nearby toolbar button because tooltip
text is not an accessible name.

Second use case: diagnosing a remote-CDP browser-agent run where a browser state
collection request hangs while the websocket appears connected, so method
timing and browser/session evidence matter as much as the final timeout.

Third use case: diagnosing persistent browser recovery before the first
screenshot exists, where profile lock state, redacted profile id,
session_mode, CDP attach/probe timing, recovery action, and final connection
state are the useful debugging evidence.

Repository: https://github.com/aaronlab/browsertrace
Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html
Comparison: https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html
```

Do not ask for stars, votes, backlinks, or reciprocal placement. The ask is
only editorial consideration for a relevant AI-agent developer tool.

## Contribution Reply

If a directory reviewer or visitor asks how to make a small docs fix, point to
the good first issue label:
https://github.com/aaronlab/browsertrace/labels/good%20first%20issue

Then share the First PR Recipe:
https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.

If they say they want to work on an issue, acknowledge the claim and leave a
short claim window before implementing it yourself. If GitHub cannot assign
them, add the `claimed` label so the handoff is visible.

## Troubleshooting Reply

For local first-run issues, CI failures, or AI/coding-agent troubleshooting replies, ask for debugging/workflow details plus JSON CLI diagnostics when safe to share:

If the follow-up involves security-sensitive reports or changes, credentials,
or private trace data, route contributors to the
[Security Policy](https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md)
before they share details publicly.

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

## Stack-Specific Reply Links

Use the closest guide when a directory reviewer, listing editor, or visitor asks
for workflow-specific debugging context:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## AOS Mapping Research

If a directory reviewer asks how BrowserTrace relates to OWASP AOS, keep the
answer research-only. BrowserTrace is not an AOS compliance claim yet. Current
research maps the closest BrowserTrace concepts to tool request/result records,
step correlation, URI-style screenshot/video artifacts, URL metadata, model I/O summaries,
and explicit redaction state.

Tracker: https://github.com/aaronlab/browsertrace/issues/237

## Tracking

After each legitimate submission or post, append metrics:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after <target> submission: <URL or submitted>"
```

Also add the final submitted URL or note to issue #10:

https://github.com/aaronlab/browsertrace/issues/10
