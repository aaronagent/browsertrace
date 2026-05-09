# BrowserTrace Examples

Use these examples to create local traces before wiring BrowserTrace into a real
agent. The first three examples do not require API keys or hosted browser
accounts.

## Fastest Path

```bash
pip install "browsertrace[ui] @ git+https://github.com/aaronlab/browsertrace@v0.1.10"
browsertrace demo
browsertrace
```

Open `http://127.0.0.1:3000` and inspect
`demo: checkout agent fails on disabled button`. From a source checkout,
`python examples/no_api_failure_demo.py` creates the same trace.

For a downloadable public-safe export that omits prompt/model I/O, screenshots,
and URLs, inspect the release asset:

```text
https://github.com/aaronlab/browsertrace/releases/download/v0.1.10/browsertrace-demo-public.html
```

## Example Matrix

| Example | Use when | Extra services | Command |
|---|---|---:|---|
| `no_api_failure_demo.py` | You want the fastest failing trace | None | `python examples/no_api_failure_demo.py` |
| `browser_use_callback_demo.py` | You want to see Browser Use-shaped step callbacks recorded | None | `python examples/browser_use_callback_demo.py` |
| `stagehand_wrapper_example.py` | You want to see Stagehand-style `act` and `extract` calls recorded | None | `python examples/stagehand_wrapper_example.py` |
| `skyvern_wrapper_example.py` | You want to see Skyvern-style task calls recorded | None | `python examples/skyvern_wrapper_example.py` |
| `basic_example.py` | You want the smallest manual SDK example | None | `python examples/basic_example.py` |
| `failure_example.py` | You want a deterministic failed run with richer steps | None | `python examples/failure_example.py` |
| `playwright_example.py` | You have Playwright installed and want browser screenshots | Local Chromium | `python examples/playwright_example.py` |
| `multipage_failure.py` | You want a multi-page Playwright failure demo | Local Chromium | `python examples/multipage_failure.py` |
| `browseruse_example.py` | You already use Browser Use and want to attach tracing | Browser Use + LLM | `python examples/browseruse_example.py` |

For Playwright examples, install the browser runtime first:

```bash
pip install playwright
playwright install chromium
```

## Troubleshooting

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

### Finding Your Demo Run

To list all local BrowserTrace demo runs:

```bash
browsertrace list
```

This shows run IDs, timestamps, and status for each stored trace.

### Creating a Share-Safe Export

To export a trace without sensitive data (prompt/model I/O, screenshots, URLs):

```bash
browsertrace export <run_id> --public -o public.html
```

This creates a share-safe HTML file suitable for sharing with others.

## Where Traces Are Stored

By default BrowserTrace stores SQLite data and screenshots in
`~/.browsertrace/`. To keep example output isolated, set `BROWSERTRACE_HOME`:

```bash
BROWSERTRACE_HOME=/tmp/browsertrace-demo python examples/stagehand_wrapper_example.py
BROWSERTRACE_HOME=/tmp/browsertrace-demo browsertrace
```
