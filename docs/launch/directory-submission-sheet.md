# BrowserTrace Directory And Newsletter Submission Sheet

Use this sheet after `v0.1.15`. Submit only where the target accepts tool
suggestions, launches, or editorial pitches. Do not ask for stars, votes,
upvotes, swaps, or artificial engagement.

## Canonical Links

- Repo: https://github.com/aaronlab/browsertrace
- Live demo: https://aaronlab.github.io/browsertrace/
- Raw trace: https://aaronlab.github.io/browsertrace/trace.html
- Comparison: https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html
- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Release: https://github.com/aaronlab/browsertrace/releases/tag/v0.1.15
- Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.15/browsertrace-demo-public.html

## Try-It Commands

Before PyPI publishing is enabled, use the `uvx` path first in directory replies
when an editor asks how to try the project:

```bash
uvx --from "browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15" browsertrace doctor
uvx --from "browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15" browsertrace demo
uvx --from "browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15" browsertrace list
uvx --from "browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15" browsertrace
```

Persistent install from the GitHub release tag:

```bash
pip install "browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.15"
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
optional redaction. The `v0.1.15` release includes the public-safe
`browsertrace export --public` mode, a packaged `browsertrace demo` command,
Browser Use/Stagehand/Skyvern/Playwright guides, and a no-dependency Browser
Use-shaped callback demo.

## Submission Queue

| Target | Fit | Entry point | Owner-only? | Link order | Status |
|---|---|---|---:|---|---|
| Product Hunt | Broad launch audience once assets and comments are ready | Product Hunt maker dashboard | Yes | Live demo, release, repo | Not submitted |
| Hacker News Show HN | OSS/devtools developers | https://news.ycombinator.com/submit | Yes | Repo, live demo, comparison | Not submitted |
| console.dev | Devtools newsletter readers | https://console.dev/ | Yes, from owner email/contact | Live demo, repo, comparison | Not submitted |
| AgentKart | Open-source AI agent marketplace readers | https://www.agentkart.ai/submit | Yes, owner account likely | Repo, live demo, Browser Use guide | Blocked: Sign-in button present; static form has no usable submit handler |
| Agent Hub | Agent/MCP/skill directory readers | https://agent-hub.dev/ | Maybe | Live demo, repo, integrations | Not submitted |
| AgDex | AI agent ecosystem directory readers | https://agdex.ai/ | Maybe | Live demo, repo, comparison | Not submitted |
| agentfirst.directory | Agent-first tooling ecosystem | https://agentfirst.directory/ | Maybe | Comparison, live demo, repo | Submitted PR: https://github.com/bradvin/agentfirst.directory/pull/30 |
| OSS AI Hub | Open-source AI tools and agents | https://ossaihub.com/submit | Yes, login required | Repo, live demo, public-safe export | Blocked: login required before submitting tools |
| FOSSHUNTER | Open-source tool discovery | https://fosshunter.com/submit | Yes, login required | Repo, live demo, release | Not submitted |
| AgentsTide | AI agents and browser-agent directory | https://agentstide.com/ | Yes, owner email | Live demo, repo, Browser Use guide | Blocked: contact email only; send owner-email pitch |
| BuilderAI Tools | Open-source AI developer tools | https://builderai.tools/submit | Yes, owner email and Cloudflare Turnstile required | Repo, live demo, public-safe export | Blocked: owner email and Cloudflare Turnstile required |
| GitHub awesome lists | Curated developer discovery lists | docs/launch/github-awesome-list-submissions.md | Yes | Repo, live demo, relevant guide | 9 PRs open; monitor feedback; e2b CLA blocked |
| Browser Use Discussions | Browser-agent practitioners | https://github.com/browser-use/browser-use/discussions | Yes | Browser Use guide, live trace, repo | Not posted |
| Stagehand Discussions | Browser automation and agent builders | https://github.com/browserbase/stagehand/discussions | Yes | Stagehand guide, live trace, repo | Not posted |
| Skyvern Discussions | Browser automation agent users | https://github.com/Skyvern-AI/skyvern/discussions | Yes | Skyvern guide, live trace, repo | Not posted |

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
Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.15/browsertrace-demo-public.html
Comparison: https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html
Release: https://github.com/aaronlab/browsertrace/releases/tag/v0.1.15
```

## Contribution Reply

If a directory reviewer or visitor asks how to make a small docs fix, point to
the current good first issue:
https://github.com/aaronlab/browsertrace/issues/225

Then share the First PR Recipe:
https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.

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

## Tracking

After each legitimate submission or post, append metrics:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after <target> submission: <URL or submitted>"
```

Also add the final submitted URL or note to issue #10:

https://github.com/aaronlab/browsertrace/issues/10
