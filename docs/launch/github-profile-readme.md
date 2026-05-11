# aaronlab GitHub Profile README Draft

This is the source draft for the live profile repository `aaronlab/aaronlab`.
GitHub only renders a personal profile README when the repository name matches
the account name exactly.

Current note: keep the live profile README in `aaronlab/aaronlab`. Do not use
the old profile redirect in launch copy.

## README Draft

```markdown
# Aaron Lab

I build AI agent systems, browser automation tools, and local-first developer
workflows.

## Featured Project

### BrowserTrace

Local flight recorder for AI browser agents.

![BrowserTrace social preview](https://raw.githubusercontent.com/aaronlab/browsertrace/main/docs/social-preview.png)

BrowserTrace helps Browser Use, Stagehand, Skyvern, Playwright + LLM, and
custom computer-use builders debug failed browser-agent runs with local step
timelines.

- Records screenshots, URLs, actions, model input/output, status, and errors.
- Opens failed runs in a local web UI.
- Exports standalone HTML traces.
- Supports public-safe exports that omit prompts, model I/O, screenshots, and
  URLs.
- Supports Browser Use run hooks, the Stagehand wrapper, and the Skyvern task/workflow wrapper.
- Includes Playwright + LLM examples and custom computer-use examples.
- MIT licensed and local-first.

Repo: https://github.com/aaronlab/browsertrace

Live demo: https://aaronlab.github.io/browsertrace/

Try locally from PyPI:

~~~bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace
~~~

Persistent install:

~~~bash
pip install "browsertrace[ui]"
browsertrace doctor
browsertrace demo
browsertrace
~~~

Stack guides:

- Browser Use: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

Runnable examples:
https://github.com/aaronlab/browsertrace/tree/main/examples

Roadmap: https://github.com/aaronlab/browsertrace/blob/main/ROADMAP.md

Launch feedback:
https://github.com/aaronlab/browsertrace/issues/3

Good first issue:
https://github.com/aaronlab/browsertrace/labels/good%20first%20issue

First PR Recipe:
https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.

Public-safe demo export:
https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html

## Troubleshooting

For profile-reader follow-up, local first-run issues, CI failures, or AI/coding-agent troubleshooting replies, ask for debugging/workflow details plus JSON CLI diagnostics when safe to share:

~~~bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
~~~

### Stack-Specific Reply Links

Use the closest guide when a profile-reader follow-up turns into a
workflow-specific debugging question:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## Current Focus

- AI browser-agent debugging
- Browser automation and computer-use agents
- LLM observability for local workflows
- Agent evaluation and tool reliability

## Open-Source Projects

| Project | Focus |
|---|---|
| [browsertrace](https://github.com/aaronlab/browsertrace) | Local traces for failed AI browser-agent runs |
| [claude-code-source-analysis](https://github.com/aaronlab/claude-code-source-analysis) | Claude Code source analysis and learning notes |
| [agent-bench-lite](https://github.com/aaronlab/agent-bench-lite) | Lightweight AI agent evaluation benchmark |
| [mcp-shield](https://github.com/aaronlab/mcp-shield) | MCP server security audit tooling |
| [openclaw](https://github.com/aaronlab/openclaw) | Personal AI assistant experiments |

## Feedback

If you build browser agents, the most useful BrowserTrace feedback is:

- Which framework do you use?
- What context is missing when a run fails?
- Are local HTML exports enough, or do you need hosted share links?
- Which adapter should be improved first?

Launch discussion:
https://github.com/aaronlab/browsertrace/discussions/6
```

## Owner Action

1. Keep the profile repository available as `aaronlab/aaronlab`.
2. Keep the draft above in `README.md`.
3. Keep BrowserTrace as the first featured project during launch.
4. Recheck the profile page after publishing profile changes.
