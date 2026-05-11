Replace every placeholder before requesting review. Keep the PR small enough to
review in one pass.

For the first contribution flow, use
`CONTRIBUTING.md#first-pr-recipe`; it keeps the first contribution small and reviewable.
Please also follow `CODE_OF_CONDUCT.md` in PR discussions and reviews.
For security-sensitive changes or private trace data, follow `SECURITY.md` before
sharing details publicly.

Relevant stack guides when changing an adapter, example, or stack-specific doc:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

When touching adapter docs, examples, exports, or troubleshooting copy, keep
the AOS mapping note research-only. BrowserTrace is not making an AOS
compliance claim yet. Current mapping research connects BrowserTrace fields to
tool request/result records, step correlation, URI-style screenshot/video
artifacts, URL metadata, model I/O summaries, and explicit redaction state.
Track the research in https://github.com/aaronlab/browsertrace/issues/237.

## Summary

- What changed:
- Why it matters:

## Linked Issue

- Fixes #123 or Refs #123
- If there is no linked issue, say why this PR is still focused.

## Test Plan

- [ ] I ran `uv run --python 3.11 --extra dev pytest -q`
- [ ] I included the exact error/output if a check could not be run.

Optional for PRs that touch issue reports, CI, or AI/coding-agent troubleshooting:

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

## Demo / Screenshots

If this changes UI, examples, exports, or README launch flow, attach a
screenshot, GIF, or exported trace.
