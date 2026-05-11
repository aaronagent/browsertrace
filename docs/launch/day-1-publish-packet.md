# BrowserTrace Day 1 Publish Packet

Use this packet when the owner is ready to publish from personal accounts. The
goal is real workflow feedback from people building browser agents, not stars,
upvotes, or artificial engagement.

## Before Publishing

- Repo: https://github.com/aaronlab/browsertrace
- Live demo: https://aaronlab.github.io/browsertrace/
- Walkthrough: https://aaronlab.github.io/browsertrace/debug-browser-agent-failure.html
- Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
- Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html
- Launch discussion: https://github.com/aaronlab/browsertrace/discussions/6
- Primary media: `docs/demo.mp4`
- Backup image: `docs/demo-poster.png`
- Copy source: `docs/launch/channel-copy.md`

## Media Alt Text

Use this when the platform supports alt text for `docs/demo.mp4` or
`docs/demo-poster.png`:

```text
BrowserTrace timeline for a failed AI browser-agent run, showing a screenshot,
URL, action, model output, status, and the failed step highlighted in red.
```

Run a baseline snapshot:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "before Day 1 owner posts"
```

## Publish Order

1. X
   - Attach `docs/demo.mp4`.
   - Paste each `## X` text block from `docs/launch/channel-copy.md` as a
     non-Premium-safe thread.
   - Post each `## X Follow-Up` text block 30-90 minutes later, or sooner if
     someone asks how to try it.
   - Pin only if the post gets real replies.
2. LinkedIn
   - Attach `docs/demo.mp4` or `docs/demo-poster.png`.
   - Paste the `## LinkedIn` draft.
   - Reply to comments with the live demo first, then the repo.
3. WeChat groups
   - Post to one or two relevant AI-builder groups only.
   - Paste the `## WeChat Group` draft.
   - Do not post to generic groups where people are not building agents.
4. Jike
   - Paste the `## Jike` draft.
   - Keep replies conversational and ask which agent stack people use.

After each post, save the URL or group name in the metrics log:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after <channel>: <post URL or group name>"
```

## Reply Shortcuts

Use these as notes, not pasted automation.

Trying it:

```text
The fastest path is the no-API demo with uvx:

uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace

Persistent install from PyPI:

pip install "browsertrace[ui]"
browsertrace doctor
browsertrace demo
browsertrace

Then open http://127.0.0.1:3000 and click the failed checkout demo.

If someone only wants to inspect a share-safe export first, send:
https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html
```

Privacy:

```text
It is local-first by default: SQLite plus screenshots under ~/.browsertrace/.
No signup and no cloud service are required. Export creates a standalone HTML
trace only when you choose to share one. For public sharing, use:

browsertrace export <run_id> --public -o public.html

`--public` omits prompt/model I/O, screenshots, and URLs. Use individual
redaction flags only when you want to keep some fields visible.
```

Integration:

```text
Which stack should I prioritize for a tighter adapter: Browser Use, Stagehand,
Playwright + LLM, Skyvern, or something else?

Tracking issue:
https://github.com/aaronlab/browsertrace/issues/new?template=integration_request.yml
```

Feedback:

```text
The most useful feedback is a real failure shape: which framework, which page
state disappeared from your logs, and what data you wish the trace had captured.
The launch thread is here:
https://github.com/aaronlab/browsertrace/discussions/6
```

Contributing:

```text
For a small first fix, start with the good first issue queue:
https://github.com/aaronlab/browsertrace/labels/good%20first%20issue

Then use the First PR Recipe:
https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.
```

Troubleshooting:

For local first-run issues, CI failures, or AI/coding-agent troubleshooting replies, ask for debugging/workflow details plus JSON CLI diagnostics when safe to share:

For security-sensitive reports or changes, or anything that includes private trace data, point people to the private path in the Security Policy before they share details publicly:
https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

## Stack-Specific Reply Links

Use the closest guide when a Day 1 reply turns into a workflow-specific
debugging question:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## Day 1 Log

| Channel | Published URL or group | Posted at | Replies to follow up | Metrics row added |
|---|---|---|---|---|
| X |  |  |  |  |
| X follow-up |  |  |  |  |
| LinkedIn |  |  |  |  |
| WeChat group 1 |  |  |  |  |
| WeChat group 2 |  |  |  |  |
| Jike |  |  |  |  |

## Stop Rules

- Do not ask anyone to star, upvote, repost, or trade engagement.
- Do not post the same link into many communities.
- Do not use generated replies verbatim on Hacker News or other high-signal
  developer communities.
- If a community pushes back on self-promotion, stop posting there and answer
  only direct technical questions.
