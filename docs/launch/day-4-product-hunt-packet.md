# BrowserTrace Day 4 Product Hunt Packet

Use this only after Day 1-3 have produced at least some real feedback or a clear
message that people understand. Product Hunt should amplify a working story, not
fix unclear positioning.

Official references checked:

- Product Hunt Launch Guide: https://www.producthunt.com/launch/
- Product Hunt Definitions: https://www.producthunt.com/launch/definitions
- Hunter vs Makers: https://help.producthunt.com/en/articles/10082986-hunter-vs-makers-and-how-to-change-them

## Launch Gate

Run:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "before Product Hunt prep"
```

Launch only if all are true:

- The owner can use a personal Product Hunt account.
- The owner can reply on launch day.
- The live demo loads quickly.
- The GitHub repo first screen is understandable without explanation.
- The gallery assets are ready: `docs/demo.mp4`, `docs/demo-poster.png`,
  `docs/social-preview.png`, and `docs/demo.gif`.
- The maker comment is edited into the owner's real voice.
- No channel asks people directly to upvote.

Defer if any are true:

- Day 1-3 posts produced no useful feedback.
- The owner cannot reply throughout launch day.
- The only call to action would be "please support us."
- Product Hunt would be the first time strangers see the product.

## Timing

Product Hunt says the best launch day is the day you are most prepared, and
12:01 AM Pacific Time is the recommended time for makers planning ahead. In
May, 12:01 AM Pacific is usually 3:01 PM in Beijing/Shanghai, but verify the
time conversion on the launch date.

## Listing Fields

Name:

```text
BrowserTrace
```

Tagline:

```text
Replay failed AI browser-agent runs
```

Primary URL:

```text
https://aaronlab.github.io/browsertrace/
```

Secondary URL for maker comment and replies:

```text
https://github.com/aaronlab/browsertrace
```

Failure patterns URL for technical replies:

```text
https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
```

Public-safe demo export for replies:

```text
https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html
```

Browser Use debugging guide for replies:

```text
https://aaronlab.github.io/browsertrace/browser-use-debugging.html
```

Try locally from PyPI:

```bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace
```

Good first issue queue for contributors:

```text
https://github.com/aaronlab/browsertrace/labels/good%20first%20issue
```

First PR Recipe:

```text
https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.
```

Description:

```text
BrowserTrace records each AI browser-agent step locally: screenshot, URL,
action, model input/output, status, and error. Open a timeline, jump to the
failed step, and export a shareable HTML trace.
```

Topics:

```text
AI Agents, Developer Tools, Open Source, Debugging, Productivity
```

Gallery order:

1. `docs/demo-poster.png`
2. `docs/demo.mp4`
3. `docs/social-preview.png`
4. `docs/demo.gif`

## Media Alt Text

Use this for Product Hunt gallery assets when alt text is available:

```text
BrowserTrace timeline for a failed AI browser-agent run, showing a screenshot,
URL, action, model output, status, and the failed step highlighted in red.
```

## Maker Comment

Edit before posting.

```text
I built BrowserTrace after losing too much time debugging browser-agent failures
from logs alone.

The agent would fail at step 47, but by then the browser state was gone. I
could see which code ran, but not what the model saw, clicked, or returned.

One recent failure shape: a Browser Use agent saw the right plus icon in the
screenshot, but clicked a nearby toolbar button because the tooltip text was not
an accessible name. That is the kind of bug where screenshot, URL, action,
model decision, and target evidence need to sit together.

Another recent failure shape: a remote browser session over CDP can look alive
while a state-collection request never returns. If event-bus lock timing is part
of the failure, you need method timing, browser/session IDs, and recovery state
beside the failed step.

For custom computer-use agents, persistent browser recovery can fail before any
screenshot or URL exists. Profile lock files and process names are not enough;
the useful evidence is session mode, a redacted profile id, CDP attach/probe
timing, recovery action, and final connection state.

BrowserTrace keeps the missing context locally:

- screenshots
- URLs
- actions
- model input/output
- failed-step errors
- exportable HTML traces, including public-safe exports that omit prompts,
  model output, screenshots, and URLs

It is MIT licensed and designed for Browser Use, Stagehand, Playwright + LLM
scripts, Skyvern-style workflows, and custom computer-use agents.

Live demo:
https://aaronlab.github.io/browsertrace/

GitHub:
https://github.com/aaronlab/browsertrace

Try locally:
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace

Good first issue:
https://github.com/aaronlab/browsertrace/labels/good%20first%20issue

I would especially like feedback from people running browser agents in tests or
production. What would make this useful in your workflow?
```

## Launch Share Copy

Use after the Product Hunt page is live. Do not ask for upvotes.

```text
BrowserTrace is live on Product Hunt today.

Local flight recorder for AI browser-agent failures: screenshots, URLs, actions,
model I/O, failed-step timelines.

Builder feedback welcome from Browser Use, Stagehand, Skyvern, and Playwright +
LLM workflows.

[Product Hunt link]
```

## Reply Notes

Use the same rules as other launch channels:

- Reply as the maker, not as a generated support account.
- Lead with the live demo when people want to inspect it.
- Link GitHub when people ask how to install, fork, or contribute.
- Link https://github.com/aaronlab/browsertrace/labels/good%20first%20issue when someone asks for
  a small first contribution.
- Ask which browser-agent stack they use.
- Convert concrete adapter requests into GitHub issues.
- For security-sensitive reports or changes, or anything that includes private trace data,
  point people to the private path in the Security Policy before they share details publicly:
  https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md
- For local first-run issues, CI failures, or AI/coding-agent troubleshooting replies, ask for debugging/workflow details plus JSON CLI diagnostics when safe to share:

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

## Stack-Specific Reply Links

Use the closest guide when a technical reply needs workflow-specific context:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## AOS Mapping Research

Use this only if a Product Hunt commenter asks whether BrowserTrace maps to
OWASP AOS. BrowserTrace is not an AOS compliance claim yet. Current research
maps the closest BrowserTrace concepts to tool request/result records, step correlation,
URI-style screenshot/video artifacts, URL metadata, model I/O summaries, and
explicit redaction state.

Tracker: https://github.com/aaronlab/browsertrace/issues/237

## Metrics

Immediately after launch:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after Product Hunt launch: <PH URL>"
```

After the first 4 hours:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after Product Hunt first 4 hours: <PH URL>"
```

End of launch day:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "end of Product Hunt day: <PH URL>"
```

Record:

| Product Hunt URL | Launched at | Stars before | Stars after 4h | Stars end of day | Useful comments | Follow-up issue |
|---|---|---:|---:|---:|---|---|
|  |  |  |  |  |  |  |

## Stop Rules

- Do not ask directly for upvotes.
- Do not buy Product Hunt engagement.
- Do not use vote rings or launch pods.
- Do not spam unrelated communities with the Product Hunt link.
- Do not relaunch without a significant product change.
