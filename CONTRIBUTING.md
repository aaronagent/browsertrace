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

When reporting local first-run or trace-inspection problems, include the compact
JSON CLI troubleshooting output when possible. These checks are also useful for
CI logs and AI/coding-agent debugging:

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

Please also follow `CODE_OF_CONDUCT.md` in issues, discussions, reviews, and
pull requests.

## Before Coding

For a new framework adapter or integration, open an integration request first:

https://github.com/aaronlab/browsertrace/issues/new?template=integration_request.yml

Include the target stack, the failure state you need to debug, and the hooks
BrowserTrace should wrap. This helps keep adapter work grounded in real
browser-agent failures instead of speculative APIs.

## Useful Local Checks

```bash
uv run --python 3.11 --extra dev pytest -q
uv build
uv run --python 3.11 python -m browsertrace.cli demo
browsertrace
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

- What user problem it solves.
- How to try it locally.
- Test commands run.
- Screenshots or exported traces for UI/demo changes. Use
  `browsertrace export <run_id> --public -o public.html` before attaching a
  real trace publicly.
