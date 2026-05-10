# BrowserTrace Examples

Use these examples to create local traces before wiring BrowserTrace into a real
agent. The no-service examples do not require API keys, hosted browser accounts,
or network access.

## Fastest Path

The quickest no-install path is `uvx` from PyPI:

```bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace list
uvx --from "browsertrace[ui]" browsertrace
```

### Check a healthy local install

`browsertrace doctor` prints the local install and trace-store status before
you open the UI:

```text
BrowserTrace doctor
Python: 3.11.x
Home: /tmp/browsertrace-demo
Database: /tmp/browsertrace-demo/db.sqlite
Runs: 0
Steps: 0
Next: browsertrace demo
UI dependencies: available
```

Windows PowerShell:

```powershell
$env:BROWSERTRACE_HOME = "$env:TEMP\browsertrace-demo"
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace
```

Persistent install from PyPI:

```bash
pip install "browsertrace[ui]"
browsertrace doctor
browsertrace demo
browsertrace
```

Open `http://127.0.0.1:3000` and inspect
`demo: checkout agent fails on disabled button`. From a source checkout,
`python examples/no_api_failure_demo.py` creates the same trace.

For a downloadable public-safe export that omits prompt/model I/O, screenshots,
and URLs, inspect the release asset:

```text
https://github.com/aaronlab/browsertrace/releases/download/v0.1.16/browsertrace-demo-public.html
```

### Discover CLI options

Use the built-in help when you want to inspect available commands or export
flags from the terminal:

```bash
browsertrace --help
browsertrace export --help
browsertrace export <run_id> --public -o public.html
```

### BrowserTrace command cheat sheet

| Command | Use when |
|---|---|
| `browsertrace doctor` | Check the local install and trace-store status |
| `browsertrace demo` | Create a deterministic failed run |
| `browsertrace list` | Find recent run IDs |
| `browsertrace show <run_id>` | Inspect a run timeline in the terminal |
| `browsertrace export <run_id> --public -o public.html` | Create a public-safe HTML export |

## Example Matrix

| Example | Use when | Extra services | Command |
|---|---|---:|---|
| `no_api_failure_demo.py` | You want the fastest failing trace | None | `python examples/no_api_failure_demo.py` |
| `browser_use_callback_demo.py` | You want to see Browser Use-shaped step callbacks recorded | None | `python examples/browser_use_callback_demo.py` |
| `stagehand_wrapper_example.py` | You want to see Stagehand-style `act` and `extract` calls recorded | None | `python examples/stagehand_wrapper_example.py` |
| `skyvern_wrapper_example.py` | You want to see Skyvern-style task calls recorded | None | `python examples/skyvern_wrapper_example.py` |
| `playwright_llm_loop_example.py` | You want Playwright + LLM-shaped prompt, DOM, selector, retry, and failure fields without a browser | None | `python examples/playwright_llm_loop_example.py` |
| `computer_use_loop_example.py` | You want a generic observe-decide-act computer-use trace | None | `python examples/computer_use_loop_example.py` |
| `basic_example.py` | You want the smallest manual SDK example | None | `python examples/basic_example.py` |
| `failure_example.py` | You want a deterministic failed run with richer steps | None | `python examples/failure_example.py` |
| `playwright_example.py` | You have Playwright installed and want browser screenshots | Local Chromium | `python examples/playwright_example.py` |
| `multipage_failure.py` | You want a multi-page Playwright failure demo | Local Chromium | `python examples/multipage_failure.py` |
| `browseruse_example.py` | You already use Browser Use and want to attach tracing | Browser Use + LLM | `python examples/browseruse_example.py` |

Browser Use users who pass run hooks directly to
`agent.run(on_step_start=..., on_step_end=...)` should use
`create_run_hooks`; see the
[Browser Use debugging guide](https://aaronlab.github.io/browsertrace/browser-use-debugging.html)
for the current run-hook path.

If you are adapting the no-service wrapper examples, see the
[Stagehand debugging guide](https://aaronlab.github.io/browsertrace/stagehand-debugging.html)
or the
[Skyvern debugging guide](https://aaronlab.github.io/browsertrace/skyvern-debugging.html)
for the current integration paths.

For Playwright examples, install the browser runtime first:

```bash
pip install playwright
playwright install chromium
```

## Contributing Example Fixes

For a docs or example fix, start with the
[First PR Recipe](../CONTRIBUTING.md#first-pr-recipe); it keeps the first contribution small and reviewable.
Keep example changes narrow and include the command you used to verify the
changed example or docs check.

### Playwright sync API snapshot

Use `snapshot_sync` when your code uses sync Playwright instead of
`playwright.async_api`:

```python
from browsertrace import Tracer
from playwright.sync_api import sync_playwright

tracer = Tracer()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    with tracer.run("sync Playwright example") as run:
        page.goto("https://example.com")
        run.snapshot_sync(page, action="opened example.com")

    browser.close()
```

## Troubleshooting

### First-run troubleshooting checklist

Run these commands in order when a first run does not look right:

```bash
browsertrace doctor
browsertrace demo
browsertrace list
browsertrace show <run_id>
browsertrace export <run_id> --public -o public.html
```

### JSON CLI checks for automation

For scripts, CI, or AI/coding-agent troubleshooting, use JSON output to check
the local install, find failed runs, and inspect one run:

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

For compact AI/coding-agent troubleshooting context, use
[`docs/llms.txt`](../docs/llms.txt); it includes JSON CLI checks, project links,
and prompts.

### Environment variable quick reference

Use these variables when you want to change local BrowserTrace behavior without
editing code:

| Variable | What it changes |
|---|---|
| `BROWSERTRACE_HOME` | changes the trace store directory |
| `BROWSERTRACE_PORT` | changes the local UI port |

### Port Already in Use

If `http://127.0.0.1:3000` is already in use, you may see an error like:

```
Error: listen EADDRINUSE 127.0.0.1:3000
```

To resolve, either:

- Find the process using port 3000, then stop only that process:

```bash
lsof -nP -iTCP:3000 -sTCP:LISTEN
kill <PID>
```

- Or run BrowserTrace on another port:

```bash
BROWSERTRACE_PORT=4000 browsertrace
```

Windows PowerShell:

```powershell
$env:BROWSERTRACE_PORT = "4000"
browsertrace
```

### Finding Your Demo Run

To list all local BrowserTrace demo runs:

```bash
browsertrace list
```

This shows run IDs, timestamps, and status for each stored trace.

### Show only recent runs

Use `--limit` when you only need the most recent runs before choosing one to
inspect or export:

```bash
browsertrace demo
browsertrace list --limit 5
browsertrace show <run_id>
browsertrace export <run_id> --public -o public.html
```

### Inspect a failed run in the terminal

Use `show` when you want to confirm the failed step before opening the UI or
exporting HTML:

```bash
browsertrace demo
browsertrace list
browsertrace show <run_id>
browsertrace export <run_id> --public -o public.html
```

`browsertrace show <run_id>` prints the run status, error, and step timeline in
the terminal, including the failed step.

### Creating a Share-Safe Export

To export a trace without sensitive data (prompt/model I/O, screenshots, URLs):

```bash
browsertrace export <run_id> --public -o public.html
```

This creates a share-safe HTML file suitable for sharing with others.

### Attach a public-safe export to an issue

When asking for help, attach `public.html` to a GitHub issue or PR comment and
include the run status or error text from `browsertrace show <run_id>`. The
public export omits prompt/model I/O, screenshots, and URLs.

## Where Traces Are Stored

By default BrowserTrace stores SQLite data and screenshots in
`~/.browsertrace/`. To keep example output isolated, set `BROWSERTRACE_HOME`:

```bash
BROWSERTRACE_HOME=/tmp/browsertrace-demo python examples/stagehand_wrapper_example.py
BROWSERTRACE_HOME=/tmp/browsertrace-demo browsertrace
```

Windows PowerShell:

```powershell
$env:BROWSERTRACE_HOME = "$env:TEMP\browsertrace-demo"
python examples/no_api_failure_demo.py
browsertrace
```

### Testing with isolated trace storage

Use a temporary trace store when adding BrowserTrace to pytest suites so test
runs do not write to `~/.browsertrace/`. This recipe uses no browser, network,
or API key:

```python
def test_browsertrace_trace_uses_temp_store(tmp_path, monkeypatch):
    monkeypatch.setenv("BROWSERTRACE_HOME", str(tmp_path))

    from browsertrace import Tracer

    tracer = Tracer()
    with tracer.run("pytest isolated trace") as run:
        run.step(
            action="record deterministic step",
            model_input={"task": "exercise trace storage"},
            model_output={"status": "ok"},
        )

    assert (tmp_path / "db.sqlite").exists()
```

If your test module imports BrowserTrace before setting `BROWSERTRACE_HOME`,
pass the temp path explicitly instead:

```python
tracer = Tracer(home=tmp_path)
```
## Public Export Flow

After creating a demo run, export it for safe sharing:

```bash
browsertrace demo
browsertrace list
browsertrace export <run_id> --public -o public.html
```

Windows PowerShell:

```powershell
browsertrace demo
browsertrace list
browsertrace export <run_id> --public -o public.html
```

### Run ID Prefixes For Export

`browsertrace list` prints a short run ID prefix for each local run.
`browsertrace export` accepts the full run ID or any unique prefix:

```bash
browsertrace list
browsertrace export <run_id> --public -o public.html
```

If export reports more than one matching run, copy more characters from the full
`Run ID:` printed by `browsertrace demo`, then rerun the export command.

> Note: `--public` omits prompts/model I/O, screenshots, and URLs.
> BrowserTrace does not upload the file anywhere; attach the generated
> `public.html` file manually to share it.

### GitHub Actions artifact for public-safe exports

Use an Actions artifact when a CI job should keep a public-safe trace for review.
BrowserTrace does not upload traces by itself; the upload step below is the
standard GitHub artifact action.

```yaml
- name: Install BrowserTrace
  run: |
    python -m pip install \
      "browsertrace[ui]"

- name: Create public-safe BrowserTrace export
  shell: bash
  run: |
    export BROWSERTRACE_HOME="$RUNNER_TEMP/browsertrace"
    RUN_ID=$(browsertrace demo | awk -F': ' '/Run ID:/ {print $2}')
    browsertrace export "$RUN_ID" --public -o public.html

- name: Upload public-safe BrowserTrace export
  uses: actions/upload-artifact@v4
  with:
    name: browsertrace-public-export
    path: public.html
```

### GitLab CI artifact for public-safe exports

Use GitLab CI artifacts when a pipeline should keep a public-safe trace for
review. BrowserTrace does not upload traces by itself; GitLab stores the
`public.html` file because it is listed under `artifacts`.

```yaml
browsertrace-public-export:
  image: python:3.11
  script:
    - python -m pip install "browsertrace[ui]"
    - export BROWSERTRACE_HOME="$CI_PROJECT_DIR/.browsertrace"
    - RUN_ID=$(browsertrace demo | awk -F': ' '/Run ID:/ {print $2}')
    - browsertrace export "$RUN_ID" --public -o public.html
  artifacts:
    when: always
    paths:
      - public.html
```
