# Changelog

BrowserTrace uses small release tags while the project is still alpha. Dates are
UTC.

For small docs fixes while reading release history, use the
[First PR Recipe](https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe)
to keep the first contribution small and reviewable.

## Unreleased

## 0.1.20 - 2026-05-13

- Added `/api/compare/<failed_run_id>/<success_run_id>` so local tools and
  agents can fetch the same first-divergence payload as
  `browsertrace compare --json` while the web UI is running.

## 0.1.19 - 2026-05-13

- Added `browsertrace compare <failed_run_id> <success_run_id>` to find the
  first divergent action, URL, status, or error between two recorded runs.
- Documented compare-run debugging in the Browser Use guide, README, and
  examples command cheat sheet for the `v0.1.19` patch release.
- Centered the launch demo story on the Browser Use local `.html` upload
  failure: the run navigates to the uploaded filename and the upload preview
  never appears.

## 0.1.18 - 2026-05-13

- Refreshed the packaged README and PyPI long description around the Browser
  Use-first failure replay/debugging story.
- Updated current release links in launch copy and package metadata for the
  `v0.1.18` patch release.

## 0.1.17 - 2026-05-10

- Added compact `stagehand_evidence` summaries for Stagehand observe/action
  results, including selectors, descriptions, and methods when available.
- Improved standalone HTML exports with `lang`, `viewport`, and a responsive
  single-column layout for narrow screens.
- Added Open Graph URL, canonical, `llms.txt`, and JSON-LD discovery metadata
  to public Pages demo, launch, integration, and exported-trace surfaces.

## 0.1.16 - 2026-05-10

- Published BrowserTrace to PyPI with Trusted Publishing.
- Updated README, launch copy, release notes, and PyPI metadata to use the
  public `pip install "browsertrace[ui]"` path.

## 0.1.15 - 2026-05-10

- Added `create_run_hooks` for Browser Use apps that pass `on_step_start` and
  `on_step_end` directly to `agent.run(...)`.
- Improved Skyvern metadata extraction so nested task/workflow run IDs and
  statuses are promoted into step metadata.

## 0.1.14 - 2026-05-09

- Refreshed the roadmap and launch queues with the current `v0.1.14` release,
  open awesome-list PR status, and remaining owner-only blockers.
- Clarified the first-contribution path for good-first issues and PR templates.
- Added compact Browser Use browser-state context to adapter `model_input` and
  documented callback compatibility/troubleshooting in the Browser Use guide.
- Captured successful Stagehand wrapper return values as step `model_output`
  so `observe` and `extract` results are visible in exported traces.

## 0.1.13 - 2026-05-09

- Updated `browsertrace doctor` so missing UI dependency guidance points to the
  current GitHub release tag while PyPI publishing is still pending.
- Added a first-run `browsertrace doctor` troubleshooting note to the README.
- Updated launch, guide, and owner-action docs to point at `v0.1.13`.

## 0.1.12 - 2026-05-09

- Added a custom computer-use debugging guide and a no-browser
  observe-decide-act example for custom browser-agent loops.
- Added copy buttons to core guide quickstarts so users can run the GitHub tag
  demo with less manual selection.
- Updated launch, guide, and owner-action docs to point at `v0.1.12`.

## 0.1.11 - 2026-05-09

- Added `browsertrace doctor` to print local install, UI dependency, database,
  run, and next-step status without requiring an existing trace database.
- Updated GitHub install and `uvx` launch copy to point at `v0.1.11`.

## 0.1.10 - 2026-05-09

- Added `browsertrace export --public` as a single sharing-safe export mode
  that omits prompt/model I/O, screenshots, and URLs.
- Updated launch and tutorial copy to use the shorter public export command.
- Added `browsertrace-demo-public.html` as a public-safe release asset for
  privacy-sensitive reviews before installation.

## 0.1.9 - 2026-05-09

- Added `browsertrace export --redact-urls` so exported HTML traces can omit
  private domains, query strings, or internal paths from step URLs.
- Updated public sharing docs to show prompt/model I/O, screenshot, and URL
  redaction together.

## 0.1.8 - 2026-05-09

- Added `browsertrace export --redact-screenshots` so exported HTML traces can
  omit screenshots when page state may reveal private data.
- Updated sharing docs and launch copy to distinguish model I/O redaction from
  screenshot redaction.

## 0.1.7 - 2026-05-09

- Added a no-dependency Browser Use-shaped callback demo so users can inspect
  adapter output without installing Browser Use, using an API key, or launching
  a browser.
- Added a comparison page for BrowserTrace versus Playwright Trace Viewer,
  LangSmith, Langfuse, and Browserbase.
- Added a Playwright + LLM feedback issue and linked it from the guide and
  launch packet.

## 0.1.6 - 2026-05-09

- HTML exports now show both model input and model output by default, matching
  the recorded trace data and public positioning.
- `browsertrace export --redact` still omits both prompt/model I/O for public
  sharing.

## 0.1.5 - 2026-05-09

- Added `browsertrace demo`, a packaged no-browser/no-API demo command that
  creates a deterministic failed checkout-agent trace after installation.
- Updated launch copy and walkthroughs to use the lower-friction demo command.

## 0.1.4 - 2026-05-09

- Added `browsertrace export --redact` for shareable HTML traces that omit
  prompt/model I/O while keeping screenshots, actions, URLs, status, and errors.
- Pinned temporary GitHub install commands to `v0.1.4` while PyPI publishing is
  waiting on owner-side Trusted Publisher setup.
- Updated the public roadmap and launch tooling to track the current release.

## 0.1.3 - 2026-05-09

- Added a runnable examples guide under `examples/`.
- Added no-network wrapper examples for Stagehand and Skyvern.
- Added a checked-in GitHub Pages workflow.
- Improved package metadata for future PyPI publishing.
- Refreshed launch surfaces, discussion text, and release links to match the
  current launch-ready branch.

## 0.1.2 - 2026-05-09

- Added `browsertrace.integrations.skyvern.wrap_skyvern`.
- Added public `Run.close(error=None)` for integration-created runs.
- Published release assets: wheel, sdist, demo HTML, demo video, and poster.
- Updated the launch kit and public integration pages.

## 0.1.1 - 2026-05-09

- Prepared the first launch-ready release.
- Added the deterministic no-API failure demo.
- Added the live static demo and debugging walkthrough.
- Added launch materials for owner-run social, Show HN, Product Hunt, and
  targeted community posts.

## 0.1.0 - 2026-05-09

- Initial BrowserTrace SDK, local UI, CLI, SQLite storage, screenshots, model
  input/output, step status, search/filter, export, and optional AI summary
  endpoint.
