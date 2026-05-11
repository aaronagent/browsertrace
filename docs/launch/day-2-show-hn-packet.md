# BrowserTrace Day 2 Show HN Packet

Use this packet only when the owner can personally submit, watch the thread, and
reply for several hours. Hacker News is high-signal and unforgiving of launch
automation, vote requests, and generic replies.

Rules checked:

- https://news.ycombinator.com/showhn.html
- https://news.ycombinator.com/newsguidelines.html
- https://news.ycombinator.com/newsfaq.html#ring

## Preflight Gate

Run these checks before submitting:

```bash
gh repo view aaronlab/browsertrace --json stargazerCount,forkCount,watchers,url,homepageUrl
uv run --python 3.11 python scripts/launch_metrics.py --append --note "before Show HN"
```

Open these in a browser:

- https://github.com/aaronlab/browsertrace
- https://aaronlab.github.io/browsertrace/
- https://aaronlab.github.io/browsertrace/debug-browser-agent-failure.html
- https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html

Submit only if all are true:

- The owner can reply in the thread for at least the first 3-4 hours.
- The live demo works without signup, email, API keys, or paid services.
- The README first screen explains what BrowserTrace does and how to run it.
- The first comment is edited into the owner's real voice.
- No one is asked to upvote, comment, repost, or "support" the submission.

Defer if any are true:

- The owner is about to be offline.
- The demo page is down or slow.
- The project is not ready for strangers to try.
- The only available post would be a marketing landing page or blog post.

## Submission

Submission URL:

```text
https://github.com/aaronlab/browsertrace
```

Title:

```text
Show HN: BrowserTrace - record and replay AI browser-agent runs to find bugs
```

After submission, immediately add the first comment. Start from the `## Hacker
News` draft in `docs/launch/channel-copy.md`, but edit it before posting. Keep
it concrete:

- What you built.
- Which debugging failure caused you to build it.
- How people can try it without signing up.
- What feedback you want from browser-agent builders.

## First Comment Draft

```text
Hi HN,

I built BrowserTrace after repeatedly losing the state of failed browser-agent
runs. Logs showed tool calls, but not what the model saw in the browser, which
screenshot led to the decision, or where the first wrong assumption entered the
run.

One concrete failure shape: the screenshot shows the right plus icon, but the
agent clicks a nearby toolbar button because the tooltip text is not an
accessible name. That needs screenshot, URL, action, model decision, and
target evidence in one place; a normal stack trace usually cannot explain it.

Another failure shape is remote CDP state collection: a stale remote browser can
leave the websocket looking open while one CDP request never returns, and
event-bus lock timing determines whether one bad session blocks others. That
needs method timing and browser/session evidence, not just a generic timeout
line.

BrowserTrace records each step locally: screenshot, URL, action, model input,
model output, status, and error. You open the local UI, click a run, and jump
straight to the failed step.

It is MIT licensed, local-first, and has a deterministic no-API demo. The quickest trial is uvx from PyPI:

uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace

A persistent install from PyPI also works:

pip install "browsertrace[ui]"
browsertrace demo
browsertrace

There is also a zero-install exported trace:
https://aaronlab.github.io/browsertrace/

And a public-safe downloadable export with prompts, model output, screenshots,
and URLs omitted:
https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html

I would especially value feedback from people building Browser Use, Stagehand,
Playwright + LLM, Skyvern, or custom computer-use agents. What state do you
wish your traces captured when a run fails?
```

## Response Rules

Do:

- Reply as the owner, not as a generated support bot.
- Answer criticism directly and technically.
- Ask follow-up questions when someone describes a real workflow.
- Admit rough edges; BrowserTrace is v0.1.
- Link the live demo before asking someone to install locally.

Do not:

- Ask for votes, stars, reposts, or comments.
- Post generic "thanks for feedback" replies.
- Use generated replies verbatim.
- Defend the project against every negative comment.
- Delete and repost if the first submission performs badly.

## Stack-Specific Reply Links

Use the closest guide when a technical reply needs workflow-specific context:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## Likely Questions

How is this different from Playwright Trace Viewer?

```text
Playwright Trace Viewer is excellent for browser automation traces. BrowserTrace
is for the browser-agent layer: screenshot plus URL, action label, model
input/output, status, and failed-step error in one timeline. It is meant for
runs where the LLM decision is part of the bug.
```

How is this different from LangSmith or Langfuse?

```text
Those are strong for LLM call tracing. BrowserTrace is narrower: local
browser-agent failure replay, with screenshots and URL/action context next to
the model I/O.
```

Why not hosted?

```text
The OSS path is local-first on purpose. A hosted/team version may make sense
later for share links and CI ingestion, but the first useful loop is: record a
failed run locally, inspect it, export HTML if needed.
```

Does data leave my machine?

```text
No by default. It stores SQLite data and screenshots under ~/.browsertrace/
unless you override the home directory. The optional AI summary endpoint only
calls an OpenAI-compatible API if you configure a key and request a summary.
```

`uvx` is not installed on my machine.

```text
Install uv from the official uv installation guide, then rerun the PyPI uvx command. If you do not want to use uvx, the README also has a persistent PyPI pip install path.
```

Can I contribute a small fix?

```text
Yes. The good first issue queue keeps small fixes reviewable:
https://github.com/aaronlab/browsertrace/labels/good%20first%20issue

Use the First PR Recipe:
https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.

For adapter work, the most useful first step is an integration request
describing the framework and failure state you need to debug.
```

## Troubleshooting Reply

Use this as notes for a human-written HN reply. For Show HN technical follow-up, local first-run issues, CI failures, or AI/coding-agent troubleshooting replies, ask for debugging/workflow details plus JSON CLI diagnostics when safe to share:

For security-sensitive reports or changes, or anything that includes private trace data, point people to the private path in the Security Policy before they share details publicly:
https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

## Metrics

After submission:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after Show HN submit: <HN item URL>"
```

After the first comment window:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after Show HN first 4 hours: <HN item URL>"
```

Record thread data:

| HN item URL | Submitted at | First comment at | Stars before | Stars after 4h | Useful feedback | Follow-up issue |
|---|---|---|---:|---:|---|---|
|  |  |  |  |  |  |  |

## Follow-Up

Within 24 hours:

- Open issues for concrete bugs or adapter requests.
- Update `docs/launch/metrics-log.md` with the HN URL and star delta.
- Add a short launch discussion update with the most useful feedback.
- Do not repost the same Show HN.
