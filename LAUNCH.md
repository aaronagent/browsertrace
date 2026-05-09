# BrowserTrace Launch Control Room

Canonical repo: https://github.com/aaronlab/browsertrace
Current release: `v0.1.1`
Owner account: `aaronlab`

## Current State

- Repo is public, MIT licensed, and positioned as a local flight recorder for AI browser agents.
- Current audited star count should be checked before every public push:

```bash
gh repo view aaronlab/browsertrace --json stargazerCount,url,homepageUrl,owner
```

- Primary launch asset: `docs/demo.gif`
- Zero-install demo trace: `browsertrace-demo.html` attached to release `v0.1.1`
- Launch discussion: https://github.com/aaronlab/browsertrace/discussions/6

## Day 0 Asset Checklist

- [ ] `uv run --python 3.11 --extra dev pytest -q` passes.
- [ ] `python examples/no_api_failure_demo.py` creates a failed run without API keys.
- [ ] `browsertrace list` shows the deterministic demo run.
- [ ] `browsertrace export <run_id> -o demo.html` creates a standalone HTML report.
- [ ] `scripts/record_demo.py` records the latest failed run, or `BROWSERTRACE_DEMO_RUN_ID`.
- [ ] Demo GIF or screenshot sequence clearly shows the failed-step timeline.
- [ ] README first screen has hook, demo, install, and 60-second demo path.
- [ ] GitHub repo homepage points to `https://github.com/aaronlab/browsertrace`.
- [ ] Social preview image is ready at `docs/social-preview.png` or exported from `docs/social-preview.svg`.
- [ ] No launch copy directly asks for upvotes or stars.

## 7-Day Posting Calendar

| Day | Channel | Asset | Goal | Owner action |
|---|---|---|---|---|
| 0 | GitHub | README, demo GIF, release asset, social preview | Make the repo shareable | Upload social preview in repo settings |
| 1 | X + LinkedIn | `docs/launch/channel-copy.md` | Warm public launch and first feedback | Post from personal accounts |
| 1 | WeChat + Jike | `docs/launch/channel-copy.md` | Reach Chinese AI-builder circles | Post manually and monitor replies |
| 2 | Hacker News Show HN | Repo URL + HN first comment draft | Devtools discovery and hard feedback | Submit only when available to reply |
| 3 | Targeted communities | `docs/launch/outreach-targets.md` | Reach Browser Use, Stagehand, Playwright users | Post only where rules allow |
| 4 | Product Hunt draft | Product Hunt section in channel copy | Prepare broader maker launch | Create draft from personal account |
| 5 | Long-form tutorial | `docs/launch/tutorial-post.md` | Give people useful debugging content | Publish on preferred blog/social channel |
| 6 | Integration outreach | Outreach target list | Invite adapters and issue feedback | Comment or post manually |
| 7 | Retrospective | Metrics and feedback log | Pick next product improvement | Share results and next milestone |

## Owner-Only Actions

Codex can prepare assets, update the repo, write copy, audit links, and monitor GitHub. The owner must personally do these actions because they require platform login, 2FA, or human conversation:

- Upload `docs/social-preview.png` as the GitHub repository social preview in Settings -> Social preview. If PNG generation is unavailable, use `docs/social-preview.svg` as source for a manual export first.
- Publish X, LinkedIn, WeChat, Jike, Xiaohongshu, Reddit, Discord, and community posts.
- Submit Show HN from a real Hacker News account and reply in your own voice.
- Create or schedule the Product Hunt draft from a personal Product Hunt account.
- Reply to launch comments where a real personal answer is expected.

## Daily Metrics

Run this audit at the start and end of each launch day:

```bash
gh repo view aaronlab/browsertrace --json stargazerCount,forkCount,watchers,totalPullRequests,totalIssues,url
gh issue list --repo aaronlab/browsertrace --state all --limit 20
gh api repos/aaronlab/browsertrace/releases/tags/v0.1.1 --jq '.assets[] | {name, download_count}'
```

Record:

| Date | Stars | New issues | New discussions | Notable comments | Next action |
|---|---:|---:|---:|---|---|
| 2026-05-09 | 3 | 0 | 0 | Baseline before growth push | Finish launch assets |

The active objective is incomplete until `stargazerCount > 1000`.

## Launch Gates

Hacker News:

- Use the repo URL as the submission URL.
- Title must start with `Show HN:`.
- People must be able to try the project without signup or email.
- Do not ask friends to upvote or comment.
- Avoid generated comment replies; use the templates only as notes and answer in your own voice.

Product Hunt:

- Use a personal account, not a company account.
- Primary URL should be the product page or repo, not a press article.
- Prepare tagline, gallery, description, maker comment, and demo before scheduling.
- It is fine to share the launch link, but ask people to visit, try, or comment, not to upvote.

Reddit and Discord:

- Check each community's rules before posting.
- Prefer a useful debugging write-up over a direct link drop.
- Post in one or two highly relevant communities, not many generic ones.

## Links

- Channel copy: `docs/launch/channel-copy.md`
- Response templates: `docs/launch/response-templates.md`
- Outreach targets: `docs/launch/outreach-targets.md`
- Tutorial draft: `docs/launch/tutorial-post.md`
- Growth design: `docs/superpowers/specs/2026-05-09-browsertrace-7-day-launch-growth-design.md`
- Execution plan: `docs/superpowers/plans/2026-05-09-browsertrace-7-day-launch-growth.md`
