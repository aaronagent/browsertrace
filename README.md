# BrowserTrace

> Local flight recorder for AI browser agents.

[![CI](https://github.com/aaronlab/browsertrace/actions/workflows/ci.yml/badge.svg)](https://github.com/aaronlab/browsertrace/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/aaronlab/browsertrace?color=blue)](https://github.com/aaronlab/browsertrace/releases)
[![PyPI](https://img.shields.io/pypi/v/browsertrace.svg)](https://pypi.org/project/browsertrace/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Contributors](https://img.shields.io/github/contributors/aaronlab/browsertrace)](https://github.com/aaronlab/browsertrace/graphs/contributors)
[![Good first issues](https://img.shields.io/github/issues/aaronlab/browsertrace/good%20first%20issue?label=good%20first%20issues)](https://github.com/aaronlab/browsertrace/labels/good%20first%20issue)
[![GitHub stars](https://img.shields.io/github/stars/aaronlab/browsertrace?style=social)](https://github.com/aaronlab/browsertrace/stargazers)

![demo](docs/demo.gif)

**MIT · local-first · no signup · no cloud · Python 3.11+**

---

Your AI browser agent failed. Logs say what code ran, but not what the agent
actually saw, clicked, or decided.

BrowserTrace records each browser-agent step as a timeline: screenshot, URL,
action, model input, model output, status, and error. Open the local UI and jump
straight to the failure.

It is a local debugging artifact channel, not another prompt-history blob:
screenshots, URLs, and model I/O stay in the local trace store, and
`browsertrace export --public` omits prompts/model I/O, screenshots, and URLs
for public bug reports.

Built for Browser Use, Stagehand, Skyvern, Playwright + LLM scripts, and custom
computer-use agents.

**Try it:** [live demo](https://aaronlab.github.io/browsertrace/) ·
[debugging walkthrough](https://aaronlab.github.io/browsertrace/debug-browser-agent-failure.html) ·
[integrations](https://aaronlab.github.io/browsertrace/integrations.html) ·
[Browser Use guide](https://aaronlab.github.io/browsertrace/browser-use-debugging.html) ·
[Stagehand guide](https://aaronlab.github.io/browsertrace/stagehand-debugging.html) ·
[Skyvern guide](https://aaronlab.github.io/browsertrace/skyvern-debugging.html) ·
[Playwright + LLM guide](https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html) ·
[computer-use guide](https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html) ·
[examples](examples/) ·
[integration request](https://github.com/aaronlab/browsertrace/issues/new?template=integration_request.yml) ·
[launch discussion](https://github.com/aaronlab/browsertrace/discussions/6)

For AI/coding agents, [`llms.txt`](llms.txt) provides concise project context,
links, and troubleshooting prompts. The hosted copy lives at
[`docs/llms.txt`](docs/llms.txt).

## See a failure trace in 60 seconds

The quickest no-install path is `uvx` from PyPI:

```bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace list
uvx --from "browsertrace[ui]" browsertrace
```

If you see `uvx: command not found`, install `uv` from the
[official uv installation guide](https://docs.astral.sh/uv/getting-started/installation/),
or use the persistent `pip install` path below.

`browsertrace doctor` is safe to run before any trace exists. On a fresh
machine, `Database: missing` and `Runs: 0` mean setup is working and the next
step is `browsertrace demo`. If it reports missing UI dependencies, install
the package with `[ui]` as shown below.
For a healthy output sample, see
[Check a healthy local install](examples/#check-a-healthy-local-install), which
shows healthy `browsertrace doctor` output for the `Home:`, `Database:`,
`Runs:`, and `UI dependencies:` status lines.

Open `http://127.0.0.1:3000`, click
`demo: checkout agent fails on disabled button`, and inspect the failed step.

## Install From PyPI

BrowserTrace is published on PyPI:
https://pypi.org/project/browsertrace/

Requires Python 3.11+.

```bash
# SDK only
pip install browsertrace

# SDK + local web UI
pip install "browsertrace[ui]"
browsertrace doctor
browsertrace demo
browsertrace
```

Useful local checks:

- `browsertrace doctor` is a safe local status check for install and trace-store status.
- `browsertrace doctor --json` prints install and trace-store status as JSON with database, run, step, and UI dependency fields.
- The healthy doctor output recipe shows expected `Home:`, `Database:`, `Runs:`, and `UI dependencies:` status lines; see [Check a healthy local install](examples/#check-a-healthy-local-install).
- `browsertrace demo` runs without API keys or external services.
- The deterministic no-API demo creates a trace without a browser, network, or API key; from a source checkout, run `python examples/no_api_failure_demo.py`.
- The local trial requires no signup, cloud account, or hosted browser service.
- After `browsertrace demo`, `browsertrace list` shows demo run IDs you can open or export.
- `browsertrace list` shows run IDs with timestamps and status.
- `browsertrace list --json` prints recent runs as JSON with id, name, status, and created timestamp.
- `browsertrace list --status failed` filters recent runs by status; combine with JSON, for example `browsertrace list --status completed --json`.
- `browsertrace demo` prints a `Run ID:` line you can copy into `browsertrace show` or `browsertrace export`.

For scripts, CI, or AI/coding-agent troubleshooting, use the JSON CLI checks:

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

For compact AI/coding-agent troubleshooting context, use
[`llms.txt`](llms.txt); it includes the same JSON CLI checks plus project links
and prompts. The hosted copy is [`docs/llms.txt`](docs/llms.txt).

- The first-run troubleshooting checklist walks through `browsertrace doctor`, `browsertrace demo`, `browsertrace list`, `browsertrace show`, and public-safe export; see the [checklist](examples/#first-run-troubleshooting-checklist).
- The live static demo and public-safe demo export let you inspect a trace before installing anything; open the [live static demo](https://aaronlab.github.io/browsertrace/) or download [`browsertrace-demo-public.html`](https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html).
- The command cheat sheet summarizes `browsertrace doctor`, `browsertrace demo`, `browsertrace list`, `browsertrace show`, and public-safe export commands; see the [cheat sheet](examples/#browsertrace-command-cheat-sheet).
- The v0.1.17 release notes summarize what changed in the current release; read the [v0.1.17 release notes](https://github.com/aaronlab/browsertrace/releases/tag/v0.1.17).
- The PyPI package page is the canonical package listing after publishing: https://pypi.org/project/browsertrace/.
- `uvx` can run the PyPI package without a persistent install, and `pip install` is the persistent install path.
- `[ui]` is needed for the local web UI, while SDK-only install is enough for trace capture integrations.
- SDK-only install can still use terminal commands like `browsertrace list`, `browsertrace show`, and `browsertrace export`; `[ui]` is only needed for the local web UI.
- The PyPI install path requires Python 3.11+.
- `browsertrace list --limit 5` narrows recent runs before choosing one to inspect or export; see the [recent-runs recipe](examples/#show-only-recent-runs).
- First-run feedback after `browsertrace demo`: https://github.com/aaronlab/browsertrace/issues/3.
- Workflow discussion after `browsertrace demo`: https://github.com/aaronlab/browsertrace/discussions/6.
- Use the [example matrix](examples/#example-matrix) to choose another runnable demo after `browsertrace demo`.
- The example matrix lists no-service examples.
- `browsertrace show <run_id>` inspects a listed run from the terminal.
- `browsertrace show <run_id>` prints the selected run's step timeline, including action labels, status, and errors.
- `browsertrace show <run_id> --json` prints one run as JSON with run details and step actions.
- `browsertrace export <run_id> --public -o public.html` creates a public-safe HTML export from a listed run.
- `browsertrace export <run_id> --public -o public.html` writes a self-contained HTML report you can attach to a bug report or issue.
- `-o public.html` chooses the export filename; without `-o`, `browsertrace export` writes `<run_id>.html`.
- `browsertrace export` prints `Wrote <path>` after writing the HTML file.
- Public-safe export omits model I/O, screenshots, and URLs.
- `--redact` only omits model I/O, while `--public` also omits screenshots and URLs.
- A longer run ID prefix fixes ambiguous `browsertrace show` or `browsertrace export` matches; see the [run ID prefix recipe](examples/#run-id-prefixes-for-export).
- `BROWSERTRACE_PORT=3001 browsertrace` starts the local UI on another port when 3000 is busy.
- The local UI binds to `127.0.0.1` by default; `BROWSERTRACE_PORT` changes only the port.
- After `browsertrace` starts the local UI, open `http://127.0.0.1:3000` and inspect the demo run.
- `browsertrace` prints `BrowserTrace UI: http://127.0.0.1:<port>` when the local server starts.
- The demo run is named `demo: checkout agent fails on disabled button` in the local UI.
- `BROWSERTRACE_HOME=/tmp/browsertrace-demo browsertrace demo` writes demo traces to an isolated trace store.
- By default, BrowserTrace stores local traces under `~/.browsertrace/`; set `BROWSERTRACE_HOME` to use an isolated trace store.
- Windows PowerShell users can set `$env:BROWSERTRACE_HOME = "$env:TEMP\browsertrace-demo"` before running BrowserTrace commands.
- `browsertrace --help` lists local CLI commands and options.
- `browsertrace export --help` lists export options before creating a public-safe HTML report.

If install or demo startup fails, use the
[first-run troubleshooting checklist](examples/#first-run-troubleshooting-checklist).

For changes in this release, read the
[v0.1.17 release notes](https://github.com/aaronlab/browsertrace/releases/tag/v0.1.17).

Want to inspect an exported trace before installing anything? Open the
[live static demo](https://aaronlab.github.io/browsertrace/) or download
[`browsertrace-demo.html`](https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo.html)
or the public-safe
[`browsertrace-demo-public.html`](https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html)
from the latest release.

For a walkthrough, read
[How to debug an AI browser-agent failure](https://aaronlab.github.io/browsertrace/debug-browser-agent-failure.html).
For custom browser agents, read
[Debug custom computer-use agent failures](https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html).

For all runnable examples, including no-browser Playwright + LLM and custom
computer-use loops, see the [examples guide](examples/).
To choose a runnable demo, use the
[example matrix](examples/#example-matrix), which lists no-service examples and
their commands.

For a compact command cheat sheet covering `browsertrace doctor`, `browsertrace demo`,
`browsertrace list`, `browsertrace show`, and public-safe export, see
[BrowserTrace command cheat sheet](examples/#browsertrace-command-cheat-sheet).

For CLI help, see [Discover CLI options](examples/#discover-cli-options),
covering `browsertrace --help` and `browsertrace export --help`.

After `browsertrace demo`, the
[demo run lookup recipe](examples/#finding-your-demo-run) uses
`browsertrace list` to show run IDs, timestamps, and status.

To narrow recent runs before choosing one to inspect or export, use the
[recent runs list-limit recipe](examples/#show-only-recent-runs) with
`browsertrace list --limit 5`.

If `browsertrace export <run_id>` matches more than one run, the
[run ID prefix troubleshooting recipe](examples/#run-id-prefixes-for-export)
shows how to copy a longer unique prefix.

If a first local run fails, the
[first-run troubleshooting checklist](examples/#first-run-troubleshooting-checklist)
walks through `browsertrace doctor`, `browsertrace demo`, `browsertrace list`,
`browsertrace show`, and public-safe export.

If the local UI port is already in use, the
[port already in use recipe](examples/#port-already-in-use) shows how to switch
ports with `BROWSERTRACE_PORT`.

To inspect a failed step timeline in the terminal, use the
[failed-run terminal inspection recipe](examples/#inspect-a-failed-run-in-the-terminal)
with `browsertrace show <run_id>`.

For help threads, the
[public-safe attachment note](examples/#attach-a-public-safe-export-to-an-issue)
shows how to attach an export to a GitHub issue or PR comment; public-safe
export omits prompt/model I/O, screenshots, and URLs.

For CI runs, the
[GitHub Actions artifact recipe](examples/#github-actions-artifact-for-public-safe-exports)
uploads `public.html` as a GitHub Actions artifact.
BrowserTrace does not upload traces by itself.

For GitLab pipelines, the
[GitLab CI artifact recipe](examples/#gitlab-ci-artifact-for-public-safe-exports)
stores `public.html` as a GitLab CI artifact.
BrowserTrace does not upload traces by itself.

For pytest tests, the
[isolated trace storage recipe](examples/#testing-with-isolated-trace-storage)
uses `BROWSERTRACE_HOME` with a temp directory for pytest isolation and needs
no browser, network, or API key.

For a real browser demo with screenshots from Wikipedia:

```bash
pip install playwright
playwright install chromium
python examples/multipage_failure.py
browsertrace
```

## Use it in your own code

For Browser Use, Stagehand, Skyvern, and Playwright guide paths, see the
[integrations overview](https://aaronlab.github.io/browsertrace/integrations.html).
For Browser Use, Stagehand, Skyvern, or Playwright adapter requests, open an
[integration request](https://github.com/aaronlab/browsertrace/issues/new?template=integration_request.yml).

### Decorator (simplest)

`@trace` works on both sync and async functions. The first argument receives the
active `Run`, so you can call `run.step(...)` (or `await run.snapshot(page)`)
from inside.

```python
from browsertrace import trace

# sync
@trace
def my_agent(run, query: str):
    run.step(action=f"search: {query}", screenshot=...)
    run.step(action="click first result", screenshot=...)

# async
@trace
async def my_async_agent(run, page, query: str):
    await run.snapshot(page, action=f"search: {query}")
    await run.snapshot(page, action="click first result")

my_agent("browser agent debugging")
```

### Playwright shortcut

If you have a Playwright `page`, use `run.snapshot(page, action=...)` to skip
the `url=page.url, screenshot=await page.screenshot()` boilerplate:

```python
async with tracer.run("my-task") as run:
    await page.goto("https://example.com")
    await run.snapshot(page, action="opened example.com")
    await page.click("#login")
    await run.snapshot(page, action="clicked login")
```

For `playwright.sync_api`, use `run.snapshot_sync(page, ...)` instead. The
[Playwright sync API snapshot](examples/#playwright-sync-api-snapshot) recipe
shows `snapshot_sync` for sync Playwright users.

### Context manager (more control)

```python
from browsertrace import Tracer

tracer = Tracer()

with tracer.run("my-task") as run:
    run.step(
        action="click login button",
        url=page.url,
        screenshot=await page.screenshot(),     # bytes or path; optional
        model_input={"prompt": "..."},          # optional
        model_output={"selector": "#login"},    # optional
        retries=0,                              # extra metadata via kwargs
    )
```

If the `with` block raises, the run is marked `failed` and the error message
is recorded against the last step.

### Browser Use integration

```python
from browser_use import Agent
from browsertrace import Tracer
from browsertrace.integrations.browser_use import attach_tracer, create_run_hooks

tracer = Tracer()
agent = Agent(task="...", llm=ChatOpenAI(model="gpt-4o"))

with attach_tracer(agent, tracer, name="my run"):
    await agent.run()
```

The adapter records the step URL, screenshot when exposed by Browser Use,
action summary, model thought/actions, and compact browser-state context such
as step count, title, tabs, and whether a screenshot was captured.
For Browser Use apps that pass lifecycle hooks directly to `agent.run(...)`,
use the run-hook helper instead:

```python
hooks = create_run_hooks(tracer, name="my run")
with hooks:
    await agent.run(on_step_start=hooks.on_step_start, on_step_end=hooks.on_step_end)
```

For Browser Use callback compatibility, see
[Debug Browser Use failures with BrowserTrace](https://aaronlab.github.io/browsertrace/browser-use-debugging.html),
including `register_new_step_callback` and `create_run_hooks` notes.

### Stagehand integration

```python
from stagehand import Stagehand
from browsertrace import Tracer
from browsertrace.integrations.stagehand import wrap_stagehand

tracer = Tracer()
stagehand = await Stagehand(...).init()
page = wrap_stagehand(stagehand.page, tracer, name="my run")

await page.goto("https://example.com")
await page.act("click the login button")   # auto-recorded
await page.extract("get the headline")      # auto-recorded
page.bt_run.close()
```

The wrapper records method args/kwargs as `model_input`, then writes the
successful Stagehand return value back to the same step as `model_output`.
For Stagehand `act` and `extract` debugging, see
[Debug Stagehand runs with BrowserTrace](https://aaronlab.github.io/browsertrace/stagehand-debugging.html).

For a no-network wrapper demo that does not require a Stagehand install, run
`python examples/stagehand_wrapper_example.py`.

### Skyvern integration

Wrap a Skyvern-shaped client to record high-level task and workflow calls.

```python
from skyvern import Skyvern
from browsertrace import Tracer
from browsertrace.integrations.skyvern import wrap_skyvern

tracer = Tracer()
skyvern = wrap_skyvern(Skyvern(...), tracer, name="my skyvern run")

await skyvern.run_task(
    url="https://example.com",
    prompt="extract the invoice total",
    wait_for_completion=True,
)

skyvern.close()
```

For a no-network wrapper demo that does not require a Skyvern install, run
`python examples/skyvern_wrapper_example.py`.
For Skyvern task and workflow debugging, see
[Debug Skyvern task failures with BrowserTrace](https://aaronlab.github.io/browsertrace/skyvern-debugging.html).

### Playwright

See `examples/playwright_example.py`, `examples/failure_example.py`, and
`examples/multipage_failure.py`. If you want a no-browser deterministic demo,
run `browsertrace demo`; for Playwright + LLM-shaped prompt, DOM, selector,
retry, and error fields, run `examples/playwright_llm_loop_example.py`; for a
generic observe-decide-act loop, run `examples/computer_use_loop_example.py`.
For Playwright + LLM trace fields, see
[Debug Playwright + LLM failures with BrowserTrace](https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html),
which covers prompt, DOM, selector, retry, and error fields.

## Storage and config

| What | Where | How to override |
|---|---|---|
| SQLite db + screenshots | `~/.browsertrace/` | `Tracer(home="...")` or `BROWSERTRACE_HOME=/path browsertrace` |
| UI port | `3000` | `BROWSERTRACE_PORT=4000 browsertrace` |

For where local traces live, see
[Where Traces Are Stored](examples/#where-traces-are-stored), which covers the
default `~/.browsertrace/` store and `BROWSERTRACE_HOME`.

For a compact list, see the
[environment variable quick reference](examples/#environment-variable-quick-reference),
which covers `BROWSERTRACE_HOME` and `BROWSERTRACE_PORT`.

Windows PowerShell equivalents:

```powershell
$env:BROWSERTRACE_HOME = "$env:TEMP\browsertrace-demo"
python examples/no_api_failure_demo.py
browsertrace

$env:BROWSERTRACE_PORT = "4000"
browsertrace
```

## What gets recorded per step

| field           | type              | notes                                  |
|-----------------|-------------------|----------------------------------------|
| `action`        | string            | human description: "click", "type x"   |
| `url`           | string            | page URL at the time                   |
| `screenshot`    | PNG bytes / path  | saved to `~/.browsertrace/screenshots/`|
| `model_input`   | any JSON-able     | prompt / messages sent to the LLM      |
| `model_output`  | any JSON-able     | LLM response / decision                |
| `status`        | `"ok"` / `"error"`| step-level status (red badge if error) |
| `error`         | string            | error message if status is `"error"`   |
| `**metadata`    | any JSON-able     | retries, latency, anything else        |
| `timestamp`     | float (epoch)     | auto                                   |

## Programmatic access

Every trace is also a JSON object you can feed back to an LLM for self-debugging
or pipe into other tools.

For AI summaries, install the `ai` extra:

```bash
pip install "browsertrace[ui,ai]"
```

```bash
# List runs (most recent first; ?status=failed and ?q= filters work)
curl http://127.0.0.1:3000/api/runs
curl 'http://127.0.0.1:3000/api/runs?status=failed&q=tokyo&limit=20'

# Full timeline for one run
curl http://127.0.0.1:3000/api/run/<run_id>

# AI root-cause summary (set OPENAI_API_KEY first)
curl http://127.0.0.1:3000/api/run/<run_id>/summary
```

Each run JSON includes the run, every step, model I/O, status, errors, relative
timestamps, and `first_error_index` so an LLM can jump straight to what broke.

## Command line

```bash
browsertrace                      # serve the web UI
browsertrace doctor               # Print local install and trace-store status
browsertrace demo                 # create a deterministic failed demo run
browsertrace list                 # list recent runs in the terminal
browsertrace show <id-or-prefix>  # print a run's timeline
browsertrace export <id> -o run.html   # self-contained HTML bundle (screenshots inlined)
browsertrace export <id> --public -o public.html   # omit model I/O, screenshots, and URLs
browsertrace export <id> --redact -o redacted.html # only omit model I/O
```

`export` produces a single HTML file you can email, attach to an issue, or
upload anywhere. No server, no DB, fully portable. Use `--public` before
sharing a real trace publicly to omit prompt/model I/O, screenshots, and URLs.
Use the individual `--redact`, `--redact-screenshots`, and `--redact-urls`
flags when you want to keep some fields visible.

## Share A Public-Safe Trace

Use this flow when someone asks for a bug report or feedback thread example:

```bash
browsertrace demo
browsertrace list
browsertrace export <run_id> --public -o public.html
```

For the compact recipe, see
[Creating a Share-Safe Export](examples/#creating-a-share-safe-export), which
uses `browsertrace export <run_id> --public -o public.html`.

Attach `public.html` yourself to the issue, discussion, or message. BrowserTrace
does not do a hosted upload.
The `--public` export omits prompts/model I/O, screenshots, and URLs.
That makes the standalone file safer to share publicly.

Do not include private prompts, credentials, cookies, tokens, customer data, or
private screenshots in docs, examples, issues, or community posts.

## Report A Browser-Agent Failure

When reporting a real failure from Browser Use, Stagehand, Skyvern, Playwright + LLM, or custom computer-use users, include:

- agent framework and version.
- failure symptom and what you expected the agent to do.
- `browsertrace show <run_id>` output for the failed run.
- A public-safe export when available: `browsertrace export <run_id> --public -o public.html`.

For ordinary workflow feedback and broader browser-agent workflow feedback, use the
[launch discussion](https://github.com/aaronlab/browsertrace/discussions/6).
For private or sensitive reports, follow [SECURITY.md](SECURITY.md) instead of
opening a public issue.

## Why not just use ___?

For a longer comparison with LLM tracing and hosted browser/runtime tools, see
the [browser-agent debugging comparison](https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html).

| Tool | Strength | Why you might still want BrowserTrace |
|---|---|---|
| Langfuse / LangSmith / Helicone | LLM call tracing, prompt/cost/latency, evals, monitoring | BrowserTrace adds the visual browser failure story: screenshot, URL, action, model I/O, status, and first failed step |
| Browserbase | Hosted browser runtime, live debugging, session recordings | BrowserTrace is local-first and runtime-agnostic for Playwright, Browser Use, Stagehand, Skyvern, and custom code |
| Browserbase browser-trace skill | Raw CDP firehose, screenshots, DOM dumps, and per-page searchable buckets | BrowserTrace is a Python local viewer for agent step timelines, model I/O, and public-safe failure reports |
| Playwright Trace Viewer | Deep Playwright action, DOM, console, network, and timing inspection | BrowserTrace adds the LLM decision context and a standalone browser-agent failure report |
| Laminar | Agent observability with browser session replay | BrowserTrace is smaller, local-first, and focused on shareable failed browser-agent traces |
| **BrowserTrace** | **Local replay debugger built around the browser-agent failure loop** | OSS, runtime-agnostic, no signup, JSON API for AI self-debug |

Smallest useful thing for "my browser agent failed, what happened" — drop in,
fix the bug, get back to building.

## Cloud / Team (coming soon)

Local BrowserTrace will always be free OSS. We're working on a hosted version
for teams that need:

None of these hosted features are required for the current local OSS workflow.

- **One-click share links** for failed runs (send to a teammate, paste in a Slack
  thread, attach to a GitHub issue, no `git clone` required)
- **CI ingestion** — upload traces from your test runs, get a digest of failures
- **Multi-run regression detection** — "this DOM changed since last passing run"
- **Team workspaces, comments, retention beyond a single laptop**

If you want it, **[open a cloud/team interest issue](https://github.com/aaronlab/browsertrace/issues/new?template=cloud_interest.yml)** describing your agent setup and team size. Pricing will likely be:

| Tier | Price | For |
|---|---:|---|
| OSS Local | Free | Solo, local debugging |
| Solo Cloud | $19/mo | Individual dev, hosted share + AI summaries |
| Team | $99/mo | 5 seats, CI, workspaces, regression detection |
| Scale | $249/mo | High-volume, long retention |
| Enterprise | Custom | SSO, VPC, SOC2 |

Real-world feedback shapes what ships first.

## Roadmap

More detail: [ROADMAP.md](ROADMAP.md).

- [x] **v0.1**: SDK + local UI + screenshots + model I/O + step status
- [x] **CLI export**: `browsertrace export <run_id>` static HTML bundle
- [x] **Search/filter**: Filter the run list by status and query text
- [x] **AI summaries**: Optional OpenAI-compatible root-cause endpoint
- [x] **Skyvern wrapper**: Trace high-level task/workflow calls
- [ ] **Multi-run comparison**: "Did this regression appear after my last commit?"
- [ ] **Deeper Skyvern adapter**: Capture workflow state and selected elements
- [ ] **Optional cloud share links**

## Contributing

This is a v0.1 alpha. The fastest way to help:

For the small, issue-based contribution path, local checks, and First PR Recipe,
read [CONTRIBUTING.md](CONTRIBUTING.md). The recipe keeps your first contribution small and reviewable.
For concise contributor expectations and a welcoming baseline, read
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
To choose the right bug, feature, integration, or cloud/team template, use the
[issue template chooser](https://github.com/aaronlab/browsertrace/issues/new/choose).
Before opening a PR, use the [pull request template](.github/PULL_REQUEST_TEMPLATE.md)
and include a linked issue and test commands.
For security-sensitive reports or private trace data, follow
[SECURITY.md](SECURITY.md) before sharing details publicly.

1. Try it on a real agent. Open an issue with what broke or what you wished worked.
2. Pick the good first issue label:
   https://github.com/aaronlab/browsertrace/labels/good%20first%20issue
   Use the [good first issue label](https://github.com/aaronlab/browsertrace/labels/good%20first%20issue)
   for the full queue of small documentation or example tasks.
3. If you need a Browser Use / Stagehand / Skyvern / Playwright adapter,
   [open an integration request](https://github.com/aaronlab/browsertrace/issues/new?template=integration_request.yml).
4. If you have a public-safe screenshot or exported trace from a real failure,
   share it in the launch discussion.

Launch discussion: [BrowserTrace launch thread](https://github.com/aaronlab/browsertrace/discussions/6).

Changelog: [CHANGELOG.md](CHANGELOG.md).

## License

MIT — see [LICENSE](LICENSE).
