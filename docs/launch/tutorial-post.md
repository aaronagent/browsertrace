# How to Debug an AI Browser Agent Failure with Screenshots and Model I/O

Your browser agent failed. The logs show tool calls, retries, and maybe a stack trace. They usually do not show the missing context: what the agent saw on the page, what it clicked, which URL it reached, and what the model returned immediately before the failure.

That gap is painful because browser-agent bugs are often visual or stateful:

- The button existed but was disabled.
- The selector matched the wrong element.
- The model interpreted stale page content.
- The page navigated but the next step assumed it had not.
- A modal appeared and changed the whole task.

BrowserTrace is a small open-source tool for recording that missing context locally.

## Install

```bash
git clone https://github.com/aaronlab/browsertrace
cd browsertrace
pip install -e ".[ui]"
```

## Run the no-API demo

```bash
python examples/no_api_failure_demo.py
browsertrace
```

Open `http://127.0.0.1:3000`, then click `demo: checkout agent fails on disabled button`.

The timeline shows the steps the agent took, including screenshots, actions, model input/output, and the failed step.

## What to inspect first

Start at the first red step. Ask:

1. What did the screenshot show at that moment?
2. Did the URL match the model's assumption?
3. Did the action target the element you expected?
4. Did the model output mention a selector, label, or page state that was not true?
5. Was the failure caused by the current step, or did an earlier step set up the wrong state?

That sequence usually finds the bug faster than reading logs from the top.

## Record your own run

The simplest API is the decorator:

```python
from browsertrace import trace

@trace
def my_agent(run, query: str):
    run.step(action=f"search: {query}", screenshot=...)
    run.step(action="click first result", screenshot=...)

my_agent("browser agent debugging")
```

For Playwright, use `run.snapshot(page, action=...)` to capture the current URL and screenshot without extra boilerplate.

## Export a trace

```bash
browsertrace list
browsertrace export <run_id> -o run.html
```

The export is a self-contained HTML file. You can attach it to an issue, send it to a teammate, or inspect it without running the local server.

## Why local-first?

Early browser-agent debugging often happens before you know what data is safe to upload. BrowserTrace stores runs under `~/.browsertrace/` by default, using SQLite and local screenshot files. You can override that with `BROWSERTRACE_HOME`.

Cloud sharing may make sense later for teams, but the first useful loop is local: record the failure, inspect the timeline, fix the agent.

## Try it

Repo: https://github.com/aaronlab/browsertrace

If you are building with Browser Use, Stagehand, Playwright + LLM scripts, Skyvern, or custom computer-use agents, the most useful feedback is: what state do you wish your traces captured at failure time?
