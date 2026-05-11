# BrowserTrace Press Kit

Use this when creating Product Hunt drafts, community posts, newsletter blurbs,
or short descriptions for people who want to share BrowserTrace.

## Product

- Name: BrowserTrace
- Tagline: Replay failed AI browser-agent runs
- Category: Open-source developer tool
- License: MIT
- Primary URL: https://github.com/aaronlab/browsertrace
- Live demo: https://aaronlab.github.io/browsertrace/
- Walkthrough: https://aaronlab.github.io/browsertrace/debug-browser-agent-failure.html
- Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
- Release: https://github.com/aaronlab/browsertrace/releases/tag/v0.1.17
- Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html
- Feedback discussion: https://github.com/aaronlab/browsertrace/discussions/6

## Stack-Specific Guides

Use these when an editor, community moderator, or reader asks for the closest
workflow-specific context:

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

Track the browser/GUI artifact mapping research here:
https://github.com/aaronlab/browsertrace/issues/237

## Short Description

BrowserTrace is a local flight recorder for AI browser agents. It records each
step with screenshots, URL, action, model input/output, status, and error so you
can jump straight to the first failed browser state.

## One-Sentence Blurb

BrowserTrace helps Browser Use, Stagehand, Playwright + LLM, Skyvern, and
computer-use builders debug failed browser-agent runs with local step timelines.

## Product Hunt Description

BrowserTrace records each AI browser-agent step locally: screenshot, URL,
action, model input/output, status, and error. Open a timeline, jump to the
failed step, and export a shareable HTML trace.

## Trial Path

Use the verified PyPI trial path:

```bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace
```

Persistent install from the same tag:

```bash
pip install "browsertrace[ui]"
browsertrace doctor
browsertrace demo
browsertrace
```

## Audience

- Browser-agent builders
- Browser Use users
- Stagehand users
- Playwright engineers adding LLM decisions to automation scripts
- Skyvern and computer-use workflow builders
- AI devtools and observability users who need local-first debugging

## Media Assets

| Asset | Path | Use |
|---|---|---|
| Demo video | `docs/demo.mp4` | X, LinkedIn, Product Hunt gallery, Jike |
| Poster image | `docs/demo-poster.png` | Product Hunt gallery, Xiaohongshu cover, LinkedIn image |
| Backup GIF | `docs/demo.gif` | README and platforms where MP4 upload is inconvenient |
| Social preview | `docs/social-preview.png` | GitHub social preview, Product Hunt gallery, link preview |
| Editable social preview | `docs/social-preview.svg` | Manual edits before exporting another PNG |
| Raw exported trace | `docs/trace.html` | Zero-install proof that export is self-contained |
| Public-safe demo export | `browsertrace-demo-public.html` release asset | Share-safe proof with prompt/model I/O, screenshots, and URLs omitted |

## Product Hunt Gallery Order

1. `docs/social-preview.png` as the first image.
2. `docs/demo.mp4` as the primary video demo.
3. `docs/demo-poster.png` as a still screenshot of the failed-step timeline.

## Proof Points

- No signup.
- No cloud required.
- Local SQLite storage.
- Exports a self-contained HTML trace.
- Includes a no-API-key deterministic failure demo.
- Works with generic Python code and has Browser Use, Stagehand, Skyvern, and
  Playwright examples or wrappers.
- External contributor PRs have started landing.

## Contribution Links

- Good first issue: https://github.com/aaronlab/browsertrace/labels/good%20first%20issue
- Integration request: https://github.com/aaronlab/browsertrace/issues/new?template=integration_request.yml
- Contributor guide: https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md
- First PR Recipe: https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.

## Troubleshooting Reply

For press/editorial follow-up, local first-run issues, CI failures, or AI/coding-agent troubleshooting replies, ask for debugging/workflow details plus JSON CLI diagnostics when safe to share:

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

## Safe Ask

Ask for workflow feedback from real browser-agent builders:

```text
What browser state do you wish your current agent logs captured at failure time?
```

Do not ask for stars, upvotes, vote swaps, or artificial engagement.
