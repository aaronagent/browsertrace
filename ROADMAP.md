# BrowserTrace Roadmap

BrowserTrace is a local replay debugger for Browser Use failures. The roadmap
keeps Browser Use as the primary path while making Stagehand, Skyvern,
Playwright + LLM, and computer-use runs easier to inspect, export, and discuss
as secondary integrations.

## Current Release

`v0.1.19` is the current launch release.

Shipped:

- Local SDK and CLI for recording browser-agent steps.
- Local web UI for inspecting runs.
- Screenshots, URLs, actions, model input/output, status, and errors.
- `browsertrace demo` for a deterministic first run without API keys.
- `browsertrace doctor` for first-run environment checks before any trace
  database exists.
- `browsertrace export` for standalone HTML traces.
- `browsertrace export --public` for public-safe sharing without prompt/model
  I/O, screenshots, or URLs.
- Basic Browser Use, Stagehand, and Skyvern-shaped integration examples.
- A generic computer-use loop example for custom observe-decide-act browser
  agents.
- GitHub Pages live demo, integration guides, launch kit, and public-safe demo
  asset.

## Launch Blockers

These are owner-only account actions. They are important for growth, but they
cannot be completed by a contributor PR.

| Issue | Status | Why it matters |
|---|---|---|
| [#5 PyPI publishing](https://github.com/aaronlab/browsertrace/issues/5) | Completed | Enables normal `pip install "browsertrace[ui]"` instead of GitHub install URLs. |
| [#15 Social preview](https://github.com/aaronlab/browsertrace/issues/15) | Completed | Makes shared repo links show the BrowserTrace card. |
| [#16 Search console submission](https://github.com/aaronlab/browsertrace/issues/16) | Owner action needed for search consoles; IndexNow submitted | Starts long-tail indexing for the GitHub Pages docs and demos. |
| [#9 Day 1 warm launch posts](https://github.com/aaronlab/browsertrace/issues/9) | Owner action needed | Publishes from the owner's X, LinkedIn, WeChat, and Jike accounts. |
| [#10 Directory and newsletter submissions](https://github.com/aaronlab/browsertrace/issues/10) | Owner action needed | Reaches curated developer-tool directories and newsletters without repeated submissions. |
| [#18 Awesome list submissions](https://github.com/aaronlab/browsertrace/issues/18) | Monitoring open PRs | One focused PR is merged/listed (`Jenqyang/Awesome-AI-Agents#220`); remaining focused PRs are open; E2B CLA check has passed; wait for maintainer feedback before any more list submissions. |

Completed launch prep:

- [#13 GitHub profile README](https://github.com/aaronlab/browsertrace/issues/13)
  now points the `aaronlab` profile at BrowserTrace.
- GitHub Release `v0.1.19` includes the wheel, sdist, full demo export,
  public-safe demo export, demo video, poster, and GIF.
- PyPI is live as `browsertrace==0.1.19`, with
  `pip install "browsertrace[ui]"` as the canonical persistent install path.
- `v0.1.19` keeps the `browsertrace doctor` onboarding fix, packaged
  `browsertrace demo` path, and explicit `browsertrace compare` CLI path for
  failed-vs-successful Browser Use runs.
- IndexNow submission is prepared and submitted for the main GitHub Pages
  launch URLs.

## v0.2 Product Tracks

| Track | Current issue | Good contribution shape |
|---|---|---|
| Browser Use trace fields | [#11](https://github.com/aaronlab/browsertrace/issues/11) | Add fields that real Browser Use failures expose safely, with no required API keys in tests. |
| Stagehand adapter depth | [#8](https://github.com/aaronlab/browsertrace/issues/8) | Capture `act`, `extract`, `observe`, or agent calls with small examples and focused tests. |
| Skyvern workflow depth | [#4](https://github.com/aaronlab/browsertrace/issues/4) | Capture task/workflow status, selected elements, and failure state where the API exposes them. |
| Playwright + LLM trace shape | [#12](https://github.com/aaronlab/browsertrace/issues/12) | Document and test fields that help LLM-guided Playwright scripts explain failures. |
| Multi-run comparison | Open an issue with a real regression case | Compare two runs enough to answer whether a failure appeared after a code or prompt change. |
| Export ergonomics | Open a focused issue | Improve redaction, attachment flow, or public-safe trace sharing without hosted infrastructure. |

## Contribution Guidelines

Good roadmap PRs are narrow and testable:

- Keep optional framework dependencies optional.
- Avoid network access, real API keys, and hosted browser accounts in tests.
- Use `BROWSERTRACE_HOME` for isolated local data in examples and tests.
- Use `browsertrace export <run_id> --public -o public.html` before sharing a
  real trace publicly.
- Include the exact command used to verify the change.

Start with `CONTRIBUTING.md#first-pr-recipe`; it keeps the first contribution small and reviewable.
Then open an integration request if the work depends on a specific
browser-agent framework.

Stack-specific guide context:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## Success Signals

The project is moving in the right direction when:

- New users can install with `pip install "browsertrace[ui]"`.
- Browser-agent builders report which trace fields they need.
- External issues and PRs include real failure shapes instead of generic feature
  requests.
- Public posts and directory submissions ask for workflow feedback, not stars or
  upvotes.
- The live GitHub audit eventually reports more than 1000 stars.
