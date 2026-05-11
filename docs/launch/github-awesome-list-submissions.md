# BrowserTrace GitHub Awesome List Submissions

Curated GitHub lists can bring qualified developer discovery, but only when the
project is a real fit. Submit one focused PR per list, follow each maintainer's
format, and do not ask for stars.

Tracking issue: https://github.com/aaronlab/browsertrace/issues/18

## Reviewer Links And Trial Path

Use these links only when a maintainer asks for more context. Keep the PR itself
small and formatted to the target list.

- Live demo: https://aaronlab.github.io/browsertrace/
- Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html
- Release: https://github.com/aaronlab/browsertrace/releases/tag/v0.1.17

The lightest local trial is the PyPI package with `uvx`:

```bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace
```

## Contribution Reply

If a maintainer or list reader asks how to make a small docs fix, point to the
good first issue label:
https://github.com/aaronlab/browsertrace/labels/good%20first%20issue

Then share the First PR Recipe:
https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.

## Troubleshooting Reply

For awesome-list reviewer follow-up, local first-run issues, CI failures, or AI/coding-agent troubleshooting replies, ask for debugging/workflow details plus JSON CLI diagnostics when safe to share:

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

Use the closest guide when an awesome-list maintainer or reader asks for
workflow-specific debugging context:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## Recommended Order

| Priority | Target | Fit | Section | Owner action |
|---:|---|---|---|---|
| 1 | `angrykoala/awesome-browser-automation` | Strong | `Tools` -> `AI` | Submitted: https://github.com/angrykoala/awesome-browser-automation/pull/112 |
| 2 | `mxschmitt/awesome-playwright` | Medium | `Utils` | Submitted: https://github.com/mxschmitt/awesome-playwright/pull/136 |
| 3 | `Jenqyang/Awesome-AI-Agents` | Medium | `Applications` -> `Tools` | Submitted: https://github.com/Jenqyang/Awesome-AI-Agents/pull/220 |
| 4 | `wjhou/awesome-computer-use-agents` | Strong | `frameworks/README.md` -> `Web/Browser Frameworks` | Submitted: https://github.com/wjhou/awesome-computer-use-agents/pull/2 |
| 5 | `cdxeve/awesome-computer-use-agents` | Strong | `GUI-Based Agents` -> `Web Agents` | Submitted: https://github.com/cdxeve/awesome-computer-use-agents/pull/2 |
| 6 | `steel-dev/awesome-web-agents` | Strong | `Dev Tools` | Submitted: https://github.com/steel-dev/awesome-web-agents/pull/56 |
| 7 | `ai-boost/awesome-harness-engineering` | Strong | `Debugging & Developer Experience` | Submitted: https://github.com/ai-boost/awesome-harness-engineering/pull/23 |
| 8 | `Agent-Tools/awesome-autonomous-web` | Strong | `Debugging & Trace Viewers` | Submitted: https://github.com/Agent-Tools/awesome-autonomous-web/pull/21 |
| 9 | `e2b-dev/awesome-ai-sdks` | Strong | top-level tool entry | Submitted: https://github.com/e2b-dev/awesome-ai-sdks/pull/187; E2B CLA passed |
| 10 | `jim-schwoebel/awesome_ai_agents` | Medium | `Building` -> `Tools` | Submitted: https://github.com/jim-schwoebel/awesome_ai_agents/pull/266 |
| 11 | `ranpox/awesome-computer-use` | Strong | `Projects` | Submitted: https://github.com/ranpox/awesome-computer-use/pull/24 |
| 12 | `trycua/acu` | Strong | `Open Source` -> `Automation` | Submitted: https://github.com/trycua/acu/pull/26 |
| 13 | `Scottcjn/awesome-agents` | Strong | `Monitoring and Observability` | Submitted: https://github.com/Scottcjn/awesome-agents/pull/16 |
| Skip | `e2b-dev/awesome-ai-agents` | Weak | n/a | Main list is for agents, not tools |
| Skip | `supernalintelligence/Awesome-Gui-Agents` | Weak | n/a | Main list catalogs GUI agents, not developer/debugging tools; referenced contribution file is missing |
| Skip | `ZJU-REAL/Awesome-GUI-Agents` | Weak | n/a | Strong topic match, but current README is primarily papers, datasets, and benchmarks rather than developer/debugging tools |

## 1. Awesome Browser Automation

Target:

```text
https://github.com/angrykoala/awesome-browser-automation
```

Status: submitted as https://github.com/angrykoala/awesome-browser-automation/pull/112.

Contribution rules observed:

- Use `[tool|resource](link) - Description.`
- One pull request per suggestion.
- Additions should be alphabetical in the relevant category.
- AI-focused browser automation tools belong under `Tools` -> `AI`.
- Description should be short, descriptive, capitalized, and end with a period.

Suggested entry:

```markdown
* [BrowserTrace](https://github.com/aaronlab/browsertrace) - Local flight recorder for AI browser agents with step timelines, screenshots, model I/O, errors, and public-safe HTML exports.
```

Suggested PR title:

```text
Add BrowserTrace to AI browser automation tools
```

Suggested PR body:

```text
Adds BrowserTrace under the AI section.

BrowserTrace is a local debugging tool for AI browser-agent runs. It records
failed Browser Use, Stagehand, Skyvern, Playwright + LLM, and custom
computer-use runs as step timelines with screenshots, URLs, actions, model
input/output, status, errors, and standalone HTML exports.

I placed it in the AI section because it is specifically for AI-driven browser
automation and browser-agent debugging.
```

## 2. Awesome Playwright

Target:

```text
https://github.com/mxschmitt/awesome-playwright
```

Status: submitted as https://github.com/mxschmitt/awesome-playwright/pull/136.

Fit notes:

- BrowserTrace is not a Playwright Test reporter.
- It is useful for Playwright scripts that include LLM decisions or browser
  agents.
- Submit only if the PR clearly frames it as Playwright + LLM debugging tooling.

Suggested section:

```text
Utils
```

Suggested entry:

```markdown
- [BrowserTrace](https://github.com/aaronlab/browsertrace) - Local trace viewer for Playwright + LLM browser-agent runs with screenshots, URLs, model I/O, errors, and shareable HTML exports.
```

Suggested PR title:

```text
Add BrowserTrace to Playwright utilities
```

Suggested PR body:

```text
Adds BrowserTrace to the Utils section for teams using Playwright as part of
LLM-driven browser-agent scripts.

BrowserTrace is not a replacement for Playwright Trace Viewer. It captures the
agent-specific context around a Playwright run: model input/output, selected
action, URL, screenshot, status, error, and a standalone HTML export.
```

## 3. Awesome AI Agents

Target:

```text
https://github.com/Jenqyang/Awesome-AI-Agents
```

Status: submitted as https://github.com/Jenqyang/Awesome-AI-Agents/pull/220.

Fit notes:

- This list has a `Tools` section containing agent support tooling.
- BrowserTrace fits only if the maintainer accepts debugging and observability
  tools, not only agent runtimes.

Suggested section:

```text
Applications -> Tools
```

Suggested entry:

```markdown
- [BrowserTrace](https://github.com/aaronlab/browsertrace) - Local flight recorder for AI browser agents with screenshots, URLs, model I/O, failure timelines, and public-safe HTML exports. ![GitHub Repo stars](https://img.shields.io/github/stars/aaronlab/browsertrace?style=social)
```

Suggested PR title:

```text
Add BrowserTrace to AI agent tools
```

Suggested PR body:

```text
Adds BrowserTrace to the Tools section.

BrowserTrace is an MIT-licensed local debugger for AI browser agents. It is
useful for Browser Use, Stagehand, Skyvern, Playwright + LLM scripts, and custom
computer-use agents when a run fails and the developer needs screenshots, URLs,
model I/O, selected actions, status, and errors in one timeline.
```

## 4. Awesome Computer Use Agents

Target:

```text
https://github.com/wjhou/awesome-computer-use-agents
```

Status: submitted as https://github.com/wjhou/awesome-computer-use-agents/pull/2.

Fit notes:

- The list covers GUI/computer-use agents and includes a
  `frameworks/README.md` page for open-source frameworks, tools, and libraries.
- BrowserTrace fits as debugging and observability tooling for web/browser
  computer-use agents.
- The PR frames BrowserTrace as a failed-run inspection tool, not as an agent
  runtime.

Submitted entry:

```markdown
### BrowserTrace
- **Stars**: 3
- **Link**: [GitHub](https://github.com/aaronlab/browsertrace)
- **Tags**: `web` `python` `debugging` `observability`

Local flight recorder for AI browser agents.
```

Verification:

```bash
git diff --check
```

## 5. Computer-Use Agents Overview

Target:

```text
https://github.com/cdxeve/awesome-computer-use-agents
```

Status: submitted as https://github.com/cdxeve/awesome-computer-use-agents/pull/2.

Fit notes:

- The README explicitly curates papers, tools, and benchmarks for terminal and
  GUI computer-use agents.
- BrowserTrace fits the Web Agents table only as an `Open Source Tool`, not as
  an agent runtime.
- The PR keeps the entry to one row to match the target list's format.

Submitted entry:

```markdown
| **BrowserTrace** | 2026 | Open Source Tool | [GitHub](https://github.com/aaronlab/browsertrace) |
```

Verification:

```bash
git diff --check
```

## 6. Awesome Web Agents

Target:

```text
https://github.com/steel-dev/awesome-web-agents
```

Status: submitted as https://github.com/steel-dev/awesome-web-agents/pull/56.

Fit notes:

- The list is focused on tools, frameworks, and resources for AI web agents.
- BrowserTrace fits the `Dev Tools` section because it helps operate and debug
  web-agent runs rather than acting as an agent runtime.
- The PR follows the target contribution policy: one item, bottom of the
  best-fit section, neutral wording, and affiliation disclosure.
- Target Actions currently show `action_required`, so maintainer approval is
  needed before CI runs on the forked PR.

Submitted entry:

```markdown
- [BrowserTrace](https://github.com/aaronlab/browsertrace) - Local-first trace viewer for debugging Playwright, Browser Use, Stagehand, and other web-agent runs with redacted shareable exports. ![GitHub Repo stars](https://img.shields.io/github/stars/aaronlab/browsertrace?style=social)
```

Verification:

```bash
GITHUB_TOKEN=$(gh auth token) npx -y awesome-lint@2.2.3 README.md
/Users/enyuanzhang/.gem/ruby/2.6.0/bin/awesome_bot --allow-dupe --allow-redirect --white-list "https://github.com/steel-dev/awesome-web-agents,https://surf.new,https://openai.com/index/introducing-operator/,https://www.perplexity.ai/comet,https://openai.com/research/webgpt,https://dzone.com/articles/build-ai-browser-agent-llms-playwright-browser-use,https://dev.to/nodeshiftcloud/build-a-browser-use-agent-with-deepseek-a-step-by-step-guide-2n59" README.md
git diff --check
```

## 7. Awesome Harness Engineering

Target:

```text
https://github.com/ai-boost/awesome-harness-engineering
```

Status: submitted as https://github.com/ai-boost/awesome-harness-engineering/pull/23.

Fit notes:

- The list is focused on agent harness engineering: tools, patterns, evals,
  permissions, observability, orchestration, and debugging.
- BrowserTrace fits `Debugging & Developer Experience` because it makes failed
  browser-agent and computer-use runs inspectable as local step timelines.
- The PR adds one resource and explains the concrete harness problem it solves:
  browser state, model decisions, actions, screenshots, URLs, and errors are
  often split across separate logs when a web-agent run fails.

Submitted entry:

```markdown
- [BrowserTrace](https://github.com/aaronlab/browsertrace) — Local-first trace viewer for failed AI browser-agent and computer-use runs: captures screenshots, URLs, model I/O, actions, errors, and public-safe HTML exports. Useful when web-agent failures need browser state and model decisions in one inspectable timeline rather than separate logs and screenshots. ![Stars](https://img.shields.io/github/stars/aaronlab/browsertrace?style=flat-square&label=%E2%98%85&color=yellow)
```

Verification:

```bash
git diff --check
curl -L -s -o /dev/null -w 'browsertrace %{http_code} %{url_effective}\n' https://github.com/aaronlab/browsertrace
curl -L -s -o /dev/null -w 'stars-badge %{http_code} %{url_effective}\n' 'https://img.shields.io/github/stars/aaronlab/browsertrace?style=flat-square&label=%E2%98%85&color=yellow'
```

## 8. Awesome Autonomous Web

Target:

```text
https://github.com/Agent-Tools/awesome-autonomous-web
```

Status: submitted as https://github.com/Agent-Tools/awesome-autonomous-web/pull/21.

Fit notes:

- The list is focused on tools that empower AI agents to interact with the web.
- BrowserTrace fits as a debugging and trace-viewer tool for AI browser-agent
  runs, adjacent to Browser Use, Stagehand, Skyvern, Playwright MCP, and other
  browser automation stacks already listed.
- The PR adds a narrow `Debugging & Trace Viewers` section rather than placing
  BrowserTrace among agent runtimes or automation frameworks.

Submitted entry:

```markdown
- **[BrowserTrace](https://github.com/aaronlab/browsertrace)** — Local-first trace viewer for AI browser agents. Records screenshots, URLs, actions, model I/O, status, and errors; exports redacted standalone HTML traces. Open-source.
```

Verification:

```bash
git diff --check
curl -L --max-time 20 -s -o /tmp/browsertrace-link-check.html -w '%{http_code}\n' https://github.com/aaronlab/browsertrace
npx -y awesome-lint README.md
```

Note: `awesome-lint README.md` reports existing baseline style issues across
the target repository, including the list's established bold-link item format
and table alignment. The PR keeps the local README style and changes only one
focused entry.

## 9. Awesome AI SDKs

Target:

```text
https://github.com/e2b-dev/awesome-ai-sdks
```

Status: submitted as https://github.com/e2b-dev/awesome-ai-sdks/pull/187.

Fit notes:

- The README describes the list as SDKs, frameworks, libraries, and tools for
  creating, monitoring, debugging and deploying autonomous AI agents.
- BrowserTrace fits as a debugging tool for failed AI browser-agent runs rather
  than as an agent runtime.
- The PR follows the target README's existing top-level entry plus expandable
  `Links` format.

Submitted entry:

```markdown
## [BrowserTrace](https://github.com/aaronlab/browsertrace)
BrowserTrace is a local-first trace viewer for AI browser agents. It records screenshots, URLs, actions, model input/output, status, and errors, then exports redacted standalone HTML traces for debugging failed browser-agent runs.

<details>

<!-- ### Description -->

### Links
- [Web](https://aaronlab.github.io/browsertrace/)
- [GitHub](https://github.com/aaronlab/browsertrace)


</details>
```

Verification:

```bash
git diff --check
curl -L --max-time 20 -s -o /tmp/browsertrace-link-check.html -w '%{http_code}\n' https://github.com/aaronlab/browsertrace
curl -L --max-time 20 -s -o /tmp/browsertrace-site-check.html -w '%{http_code}\n' https://aaronlab.github.io/browsertrace/
```

Current check:

- `verification/cla-signed` is `SUCCESS`; no further CLA action is needed
  unless the maintainers request changes.

## 10. Awesome AI Agents Tools

Target:

```text
https://github.com/jim-schwoebel/awesome_ai_agents
```

Status: submitted as https://github.com/jim-schwoebel/awesome_ai_agents/pull/266.

Fit notes:

- The target list has a broad `Building` -> `Tools` section with existing
  observability, tracing, debugging, and browser-agent infrastructure entries.
- BrowserTrace fits only as an AI browser-agent failure inspection tool, not as
  a general agent runtime or consumer AI app.
- The PR keeps the change to one README entry and uses the target list's
  existing one-line `name + link + description` format.

Submitted entry:

```markdown
- [BrowserTrace](https://github.com/aaronlab/browsertrace) - Local-first trace viewer for Browser Use, Stagehand, Skyvern, Playwright + LLM, and custom browser-agent runs with screenshots, URLs, model I/O, errors, and shareable HTML exports. [github](https://github.com/aaronlab/browsertrace) | [demo](https://aaronlab.github.io/browsertrace/)
```

Verification:

```bash
git diff --check
```

## 11. Awesome Computer Use

Target:

```text
https://github.com/ranpox/awesome-computer-use
```

Status: submitted as https://github.com/ranpox/awesome-computer-use/pull/24.

Fit notes:

- The target list curates computer-use resources, including a `Projects`
  section for open-source projects around GUI and browser computer use.
- BrowserTrace fits as failed-run debugging tooling for browser-agent and
  computer-use projects, not as an agent runtime.
- The PR adds one neutral Projects entry and avoids star, vote, or engagement
  language.

Submitted entry:

```markdown
- [BrowserTrace](https://github.com/aaronlab/browsertrace) - Local-first trace viewer for debugging failed AI browser-agent and computer-use runs with screenshots, URLs, actions, model I/O, errors, and redacted HTML exports.
```

Verification:

```bash
git diff --check
```

## 12. ACU - Awesome Agents for Computer Use

Target:

```text
https://github.com/trycua/acu
```

Status: submitted as https://github.com/trycua/acu/pull/26.

Fit notes:

- The target list curates resources about AI agents for Computer Use, including
  open-source projects, frameworks, tools, and automation.
- BrowserTrace fits as local debugging and trace tooling for failed
  browser-agent and computer-use runs.
- The PR adds one neutral `Open Source` -> `Automation` entry and does not ask
  for stars, votes, or reciprocal placement.

Submitted entry:

```markdown
- [BrowserTrace](https://github.com/aaronlab/browsertrace)
  - Local-first trace viewer for failed browser-agent and computer-use runs
  - Records screenshots, URLs, actions, model I/O, status, errors, and public-safe HTML exports
```

Verification:

```bash
git diff --check
```

## 13. Awesome Agents

Target:

```text
https://github.com/Scottcjn/awesome-agents
```

Status: submitted as https://github.com/Scottcjn/awesome-agents/pull/16.

Fit notes:

- The target list explicitly covers AI agent platforms, frameworks, protocols,
  tools, resources, and observability tools.
- BrowserTrace fits the `Monitoring and Observability` section as a debugging
  and trace viewer for failed browser-agent and computer-use runs.
- The PR adds one neutral entry, follows the required
  `[Name](link) - Description.` format, and does not include engagement
  requests or reciprocal placement.
- `Scottcjn/awesome-agents#12` proposes `agenttrace`, but BrowserTrace is not a duplicate.
  It focuses on browser-agent/computer-use failure evidence rather than general
  coding-agent session telemetry.

Submitted entry:

```markdown
- [BrowserTrace](https://github.com/aaronlab/browsertrace) - Local-first trace viewer for debugging failed AI browser-agent and computer-use runs with screenshots, URLs, actions, model output, status, and redacted shareable exports.
```

Verification:

```bash
git diff --check
curl -L -s -o /dev/null -w '%{http_code}\n' https://github.com/aaronlab/browsertrace
npx --yes awesome-lint README.md
```

Note: `awesome-lint` reports existing target-repository issues such as duplicate
links, ToC/license checks, and unrelated list-item formatting. The BrowserTrace
row is not in the reported failures.

## Skip List

- `e2b-dev/awesome-ai-agents`: the README says the list is only for AI
  assistants and agents, and points SDK/framework/tool submissions to
  `e2b-dev/awesome-sdks-for-ai-agents`.
- `supernalintelligence/Awesome-Gui-Agents`: the README focuses on GUI agents
  rather than developer/debugging tools, and its referenced contribution file is
  not present in the repository.
- `opendilab/awesome-ui-agents`: strong topic match, but the `Tools` section
  uses a paper-style format with authors, year, key, and code links rather than
  a general developer/debugging tool format.
- `ZJU-REAL/Awesome-GUI-Agents`: the repository is a strong topic match, but
  the current README focuses on papers, datasets, and benchmarks rather than
  developer/debugging tools.
- Low-star forks with copied README content and no visible curation.
- Broad AI app lists where BrowserTrace would be an unrelated developer tool.

## Stop Rules

- Do not submit the same pitch to many lists.
- Do not open issues asking maintainers to add the project for you.
- Do not ask maintainers or list visitors for stars.
- If maintainers reject the entry as off-topic, accept it and do not argue.
