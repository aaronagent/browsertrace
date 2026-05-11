# BrowserTrace Owner Publish Queue

This queue lists the launch actions that require the owner's personal accounts,
login sessions, 2FA, and human replies. Codex can prepare and audit everything
around these steps, but the owner must click publish.

Do not ask for stars, upvotes, or vote swaps. Ask for workflow feedback from
people building browser agents.

## Ready Links

- Repo: https://github.com/aaronlab/browsertrace
- Live demo: https://aaronlab.github.io/browsertrace/
- Walkthrough: https://aaronlab.github.io/browsertrace/debug-browser-agent-failure.html
- Failure patterns: https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html
- Release: https://github.com/aaronlab/browsertrace/releases/tag/v0.1.17
- Public-safe demo export: https://github.com/aaronlab/browsertrace/releases/download/v0.1.17/browsertrace-demo-public.html
- Launch discussion: https://github.com/aaronlab/browsertrace/discussions/6
- Feedback issue: https://github.com/aaronlab/browsertrace/issues/3

Shortest owner checklist: `docs/launch/owner-next-actions.md`
Shortest owner social post packet: `docs/launch/owner-social-post-packet.md`
Shortest owner email packet: `docs/launch/owner-email-send-packet.md`
Shortest HN/Product Hunt packet: `docs/launch/owner-launch-submission-packet.md`

Current listing status: the tracked external GitHub list and directory
submissions are still open and have not listed BrowserTrace on their default
branches yet. Owner-channel posts and the prepared directory emails should not
wait for those merges.

## Media

- Primary video: `docs/demo.mp4`
- Poster image: `docs/demo-poster.png`
- Backup GIF: `docs/demo.gif`
- Social preview: `docs/social-preview.png`
- Public-safe demo export: `browsertrace-demo-public.html` attached to release `v0.1.17`
- Press kit: `docs/launch/press-kit.md`
- Search indexing submission: `docs/launch/search-indexing-submission.md`
- GitHub awesome list submissions: `docs/launch/github-awesome-list-submissions.md`

## Day 1 Warm Launch

Use `docs/launch/day-1-publish-packet.md` as the single owner-facing checklist.

0. GitHub pre-flight
   - Profile README: keep the live `aaronlab/aaronlab` README aligned with
     `docs/launch/github-profile-readme.md`.
   - Keep BrowserTrace as the first featured project during launch.
   - Profile pin: completed. The public GitHub profile now pins
     `aaronlab/browsertrace`.
   - Do not use the old profile redirect in launch copy.
   - Repository social preview: completed. GitHub reports
     `usesCustomOpenGraphImage=true`; keep `docs/social-preview.png` as the
     reusable launch and link-preview asset.
   - Search indexing: submit `https://aaronlab.github.io/browsertrace/sitemap.xml`
     in Google Search Console and Bing Webmaster Tools.
   - Search indexing tracking issue:
     https://github.com/aaronlab/browsertrace/issues/16
   - External GitHub list/directory PRs: fifteen focused PRs are open, including
     `steel-dev/awesome-web-agents#56` and
     `ai-boost/awesome-harness-engineering#23`, plus
     `Agent-Tools/awesome-autonomous-web#21` and
     `e2b-dev/awesome-ai-sdks#187`, and the broader
     `jim-schwoebel/awesome_ai_agents#266` tools-list PR. Focused computer-use
     list PRs include `ranpox/awesome-computer-use#24` and `trycua/acu#26`.
     The Scottcjn agent-ecosystem list PR is open at
     `Scottcjn/awesome-agents#16`. The CliHub registry PR is open at
     `clihub-ai/clihub#1`. The E2B CLA check has passed;
     monitor maintainer feedback and do not open additional list or registry
     PRs unless the target is clearly high-fit and non-duplicative.
   - Awesome list tracking issue:
     https://github.com/aaronlab/browsertrace/issues/18

1. X
   - Use each `## X` text block in `docs/launch/channel-copy.md` as a
     non-Premium-safe thread.
   - Attach `docs/demo.mp4`.
   - Pin the post for 48 hours only if it gets real replies.
2. LinkedIn
   - Use the `## LinkedIn` draft in `docs/launch/channel-copy.md`.
   - Attach `docs/demo.mp4` or `docs/demo-poster.png`.
   - Ask what context people need when their browser agent fails.
3. WeChat groups
   - Use the `## WeChat Group` draft in `docs/launch/channel-copy.md`.
   - Post to one or two relevant AI-builder groups first.
   - Reply with the live demo before asking anyone to install locally.
4. Jike
   - Use the `## Jike` draft in `docs/launch/channel-copy.md`.
   - Keep the tone conversational and ask for builders who use Browser Use,
     Stagehand, Playwright + LLM, or computer-use agents.

After each post, append a metrics row and save the post URL plus notable replies
in `docs/launch/metrics-log.md`.

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after X post: <post URL>"
```

## Day 2 Developer Discovery

1. Hacker News Show HN
   - Use `docs/launch/day-2-show-hn-packet.md` as the submission checklist.
   - Use the `## Hacker News` title and first comment draft in
     `docs/launch/channel-copy.md`.
   - Submit only when the owner can reply for several hours.
   - Do not ask anyone to upvote.
2. Targeted communities
   - Use `docs/launch/outreach-targets.md` to pick one high-fit community.
   - Prefer Browser Use, Stagehand, Playwright, or Skyvern users over generic AI
     communities.
   - Browser Use, Stagehand, and Skyvern GitHub Discussions are already posted;
     monitor those threads instead of reposting.
   - Check rules first; if self-promotion is restricted, share the walkthrough
     only when it answers an existing debugging thread.

## Day 3-5 Broader Posts

Use `docs/launch/day-3-targeted-communities-packet.md` before any additional
targeted community post. Browser Use, Stagehand, and Skyvern GitHub Discussions
are already posted; the packet is now mainly for monitoring, Playwright, Reddit,
Discord where allowed, and replies.

0. PyPI publishing
   - Completed. `https://pypi.org/pypi/browsertrace/json` returns HTTP 200.
   - Package page: `https://pypi.org/project/browsertrace/`.
   - Current PyPI version: `0.1.17`.
   - Use `pip install "browsertrace[ui]"` in public posts.
   - Future releases should use the manual `Publish` workflow after the version
     and GitHub release artifacts are ready.
1. Reddit or Discord
   - Use the value-first Reddit draft in `docs/launch/channel-copy.md`.
   - Lead with the debugging walkthrough, not the repo.
2. Product Hunt draft
   - Use `docs/launch/day-4-product-hunt-packet.md` as the listing checklist.
   - Use the Product Hunt tagline, description, maker comment, and first comment
     from `docs/launch/channel-copy.md`.
   - Prepare the listing before launch day; do not launch unless the owner can
     reply throughout the day.
3. Xiaohongshu
   - Use the `## Xiaohongshu` draft in `docs/launch/channel-copy.md`.
   - Use `docs/demo-poster.png` as the first image and mention
     `aaronlab/browsertrace` plainly.
4. Chinese long-form
   - Use `docs/launch/chinese-tutorial-post.md`.
   - Publish only where technical OSS posts are welcome.
   - Ask for browser-agent debugging workflow feedback, not stars or reposts.

## Reply Workflow

- Use `docs/launch/response-templates.md` as notes, not as copy-paste replies.
- For workflow-specific guide links, use the closest page:
  - Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
  - Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
  - Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
  - Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
  - Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html
- For AOS mapping research questions, say BrowserTrace is not an AOS compliance claim yet.
  The current research maps BrowserTrace concepts to tool request/result
  records, step correlation, URI-style screenshot/video artifacts, URL metadata,
  model I/O summaries, and explicit redaction state.
  Tracker: https://github.com/aaronlab/browsertrace/issues/237
- For small contribution questions, point to the good first issue label:
  https://github.com/aaronlab/browsertrace/labels/good%20first%20issue
  Then share the First PR Recipe:
  https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.
- For security-sensitive reports or changes, or private trace data, point
  contributors to https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md
  before they share details publicly.
- For bug reports, ask the user to open an issue with their agent stack, trace
  type, and whether the failing step involved screenshots, selectors, or model
  output.
- For public trace sharing, ask them to run
  `browsertrace export <run_id> --public -o public.html` before attaching files
  to issues or posts. Use individual redaction flags only when they want to keep
  some fields visible.
- For local first-run issues, CI failures, or AI/coding-agent troubleshooting replies, ask for debugging/workflow details plus JSON CLI diagnostics when safe to share:

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

- For integration requests, point to the v0.2 milestone and ask which adapter
  would unblock them first.

## Metrics Check

Run after each major post:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after <channel>: <post URL>"
uv run --python 3.11 python scripts/launch_metrics.py --json
gh issue list --repo aaronlab/browsertrace --state all --limit 20
```
