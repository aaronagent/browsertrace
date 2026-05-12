# Contributing to BrowserTrace

Thanks for helping improve BrowserTrace.

BrowserTrace is intentionally small: a local-first recorder for AI browser
agent runs. Good contributions make failed browser-agent runs easier to inspect,
export, or integrate with real agent frameworks.

## Development Setup

```bash
git clone https://github.com/aaronlab/browsertrace
cd browsertrace
uv run --python 3.11 --extra dev pytest -q
```

The test suite should pass before opening a pull request.

Please also follow `CODE_OF_CONDUCT.md` in issues, discussions, reviews, and
pull requests.

## Before Coding

For a new framework adapter or integration, open an integration request first:

https://github.com/aaronlab/browsertrace/issues/new?template=integration_request.yml

Include the target stack, the failure state you need to debug, and the hooks
BrowserTrace should wrap. This helps keep adapter work grounded in real
browser-agent failures instead of speculative APIs.

For a `good first issue`, docs fix, or small example improvement:

- Comment if you plan to work on it so others can avoid duplicating effort.
- Open a draft PR early if you are unsure about scope.
- Link the issue in the PR body with `Fixes #<issue>` or `Refs #<issue>`.
- Keep the first PR small enough to review in one pass.

## First PR Recipe

For a docs fix or small example:

1. Comment on the good first issue so maintainers know you are working on it.
   Good first issue label: https://github.com/aaronlab/browsertrace/labels/good%20first%20issue
   A maintainer should treat that comment as an active claim and leave a
   short claim window before maintainers take the same issue directly.
2. Create a branch with a short descriptive name.
3. Make the smallest useful change and keep it small enough to review in one pass.
4. Run `uv run --python 3.11 --extra dev pytest -q`,
   `git diff --check`, `git diff --stat`, and `git diff --summary`.
   Read the diff summary before opening the PR and confirm there are no
   unexpected deleted or renamed files.
5. Open a PR and link the issue in the body with `Fixes #<issue>` or
   `Refs #<issue>`.

For security-sensitive reports or private trace data, follow
[SECURITY.md](SECURITY.md) before sharing details publicly.

## Useful Local Checks

```bash
uv run --python 3.11 --extra dev pytest -q
uv build
uv run --python 3.11 python -m browsertrace.cli demo
browsertrace
```

For docs-only changes, still run the full pytest command. It is quick and keeps
release, workflow, and packaging checks covered.

For Browser Use-shaped no-service checks from a source checkout:

```bash
python examples/browser_use_callback_demo.py
python examples/browser_use_run_hooks_demo.py
browsertrace list --limit 5
browsertrace show <run_id>
```

Expect the listed runs to include `demo: browser-use callback flow` and
`demo: browser-use run hooks flow`. Viewing either run should show the demo step
labels `search_google(query=BrowserTrace)` and `click(selector=#result-1)`.

For issue reports, CI, or AI/coding-agent troubleshooting, include the compact
JSON CLI checks when the problem involves a local first run or trace inspection:

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

## Contribution Areas

Roadmap context:

https://github.com/aaronlab/browsertrace/blob/main/ROADMAP.md

- Good first issues:
  https://github.com/aaronlab/browsertrace/labels/good%20first%20issue
- Framework integrations: Browser Use, Stagehand, Skyvern, Playwright, and
  computer-use agents.
- Export improvements: portable HTML, redaction, and issue attachments.
- Debugging workflow: clearer failure markers, search, filters, and summaries.
- Documentation: short examples from real browser-agent failures.

Framework guide context:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## Adapter Contribution Checklist

For Browser Use, Stagehand, Skyvern, Playwright + LLM, or custom computer-use
adapters, a good first PR should:

- Keep the dependency optional.
- Capture URL, screenshot, action/tool name, status, and error where available.
- Capture model input/output only when the framework exposes it safely.
- Include a small example script.
- Include focused tests that do not require network access or real API keys.
- Avoid sending trace data to any hosted service.

## Design Principles

- Keep the base SDK dependency-light.
- Keep data local by default.
- Prefer small, inspectable features over broad observability-platform scope.
- Add tests for behavior changes.
- Keep optional framework integrations optional.
- Do not include private prompts, secrets, credentials, or customer data in
  issues, traces, screenshots, or tests.

## Pull Requests

For each PR, include:

- Linked issue, if any.
- What user problem it solves.
- How to try it locally.
- Test commands run.
- Screenshots or exported traces for UI/demo changes. Use
  `browsertrace export <run_id> --public -o public.html` before attaching a
  real trace publicly. The examples guide has a focused recipe for
  [attaching a public-safe export to an issue](examples/README.md#attach-a-public-safe-export-to-an-issue).
