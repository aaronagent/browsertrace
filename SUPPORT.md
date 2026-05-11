# Support

BrowserTrace is early open-source software. The best support path depends on
what you need.

## Questions and Launch Feedback

Use the launch discussion:

https://github.com/aaronlab/browsertrace/discussions/6

Good topics:

- Which browser-agent stack you use.
- What failed run was painful to debug.
- What trace data you wish BrowserTrace captured.
- Whether portable HTML exports are enough for your team.

## Stack-Specific Guides

Check the closest guide before filing a detailed report:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## AOS Mapping Research

BrowserTrace is not an AOS compliance claim yet. Current research maps the
closest BrowserTrace concepts to tool request/result records, step correlation,
URI-style screenshot/video artifacts, URL metadata, model I/O summaries, and
explicit redaction state.

Tracker: https://github.com/aaronlab/browsertrace/issues/237

## Bugs

Open a bug report:

https://github.com/aaronlab/browsertrace/issues/new?template=bug_report.yml

Please include:

- BrowserTrace version.
- Python version.
- Agent/browser stack.
- Reproduction steps.
- Exported trace or `browsertrace show <id>` output if it is safe to share.
  Use `browsertrace export <run_id> --public -o public.html` before attaching a
  real trace publicly.

## Feature and Integration Requests

Open a feature request:

https://github.com/aaronlab/browsertrace/issues/new?template=feature_request.yml

Open an integration request:

https://github.com/aaronlab/browsertrace/issues/new?template=integration_request.yml

For hosted sharing or team workflows, open a cloud/team interest issue:

https://github.com/aaronlab/browsertrace/issues/new?template=cloud_interest.yml

Current roadmap:

https://github.com/aaronlab/browsertrace/blob/main/ROADMAP.md

Current milestone:

https://github.com/aaronlab/browsertrace/milestone/1

## Security

Do not post secrets, private screenshots, customer data, cookies, tokens, or
private prompts in public issues.

See `SECURITY.md` for security reporting guidance.
