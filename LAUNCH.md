# BrowserTrace Launch Control Room

Canonical repo: https://github.com/aaronlab/browsertrace
Current release: `v0.1.17`
Owner account: `aaronlab`

## Current State

- Repo is public, MIT licensed, and positioned as a local flight recorder for AI browser agents.
- Current account and repo are `aaronlab/browsertrace`; do not use the old
  `aaronagent` name in new launch links.
- PyPI publishing is complete for `browsertrace==0.1.17`.
- Public install command:

```bash
pip install "browsertrace[ui]"
```

- PyPI package page: https://pypi.org/project/browsertrace/
- PyPI JSON: `https://pypi.org/pypi/browsertrace/json` returns HTTP 200.
- The tested no-install PyPI path is:

```bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace list
uvx --from "browsertrace[ui]" browsertrace
```

- Current audited star count should be checked before every public push:

```bash
gh repo view aaronlab/browsertrace --json stargazerCount,forkCount,watchers,url,homepageUrl
```

- Primary launch asset: `docs/demo.mp4`
- README animation: `docs/demo.gif`
- Static poster: `docs/demo-poster.png`
- Live zero-install demo: https://aaronlab.github.io/browsertrace/
- Downloadable demo trace: `browsertrace-demo.html` attached to release `v0.1.17`
- Public-safe demo trace: `browsertrace-demo-public.html` attached to release `v0.1.17`
- Launch discussion: https://github.com/aaronlab/browsertrace/discussions/6

## Day 0 Asset Checklist

- [ ] `uv run --python 3.11 --extra dev pytest -q` passes.
- [ ] `browsertrace demo` creates a failed run without API keys.
- [ ] `browsertrace list` shows the deterministic demo run.
- [ ] `browsertrace export <run_id> -o demo.html` creates a standalone HTML report.
- [ ] `browsertrace export <run_id> --public -o public.html` creates a public-safe report without model I/O, screenshots, or URLs.
- [ ] `scripts/record_demo.py` records the latest failed run, or `BROWSERTRACE_DEMO_RUN_ID`.
- [ ] `docs/demo.mp4` and `docs/demo-poster.png` clearly show the failed-step timeline.
- [ ] README first screen has hook, demo, install, and 60-second demo path.
- [ ] GitHub repo homepage points to `https://aaronlab.github.io/browsertrace/`.
- [ ] Social preview image is ready at `docs/social-preview.png` or exported from `docs/social-preview.svg`.
- [ ] No launch copy directly asks for upvotes or stars.

## 7-Day Posting Calendar

| Day | Channel | Asset | Goal | Owner action |
|---|---|---|---|---|
| 0 | GitHub | README, demo GIF, release asset, social preview | Make the repo shareable | Upload social preview in repo settings |
| 1 | X + LinkedIn | `docs/launch/day-1-publish-packet.md` | Warm public launch and first feedback | Post from personal accounts |
| 1 | WeChat + Jike | `docs/launch/day-1-publish-packet.md` | Reach Chinese AI-builder circles | Post manually and monitor replies |
| 2 | Hacker News Show HN | `docs/launch/day-2-show-hn-packet.md` | Devtools discovery and hard feedback | Submit only when available to reply |
| 3 | Targeted communities | `docs/launch/day-3-targeted-communities-packet.md` | Reach Browser Use, Stagehand, Playwright users | Post only where rules allow |
| 4 | Product Hunt draft | `docs/launch/day-4-product-hunt-packet.md` | Prepare broader maker launch | Create draft from personal account |
| 5 | Long-form tutorial | `docs/launch/tutorial-post.md` + `docs/launch/chinese-tutorial-post.md` | Give people useful debugging content | Publish on preferred blog/social channel |
| 6 | Integration outreach | Outreach target list | Invite adapters and issue feedback | Comment or post manually |
| 7 | Retrospective | Metrics and feedback log | Pick next product improvement | Share results and next milestone |

## Owner-Only Actions

Codex can prepare assets, update the repo, write copy, audit links, and monitor GitHub. The owner must personally do these actions because they require platform login, 2FA, or human conversation:

- PyPI first publish is completed. Future PyPI releases should use the manual
  `Publish` workflow after the version and release artifacts are ready.
- Keep the live `aaronlab/aaronlab` GitHub profile repository aligned with
  `docs/launch/github-profile-readme.md`.
- Profile pin is completed: BrowserTrace (`aaronlab/browsertrace`) is pinned on
  the public GitHub profile during launch.
- GitHub social preview is completed. Keep `docs/social-preview.png` as the
  reusable source asset for future launch previews.
- Submit `https://aaronlab.github.io/browsertrace/sitemap.xml` in Google Search
  Console and Bing Webmaster Tools.
- Monitor the thirteen open third-party awesome-list and directory PRs plus the
  CLIs.dev submission issue, and respond only if maintainers ask for changes.
  Do not open additional list PRs unless the target is clearly high-fit and
  non-duplicative.
- Publish X, LinkedIn, WeChat, Jike, Xiaohongshu, Reddit, Discord, and community posts.
- Submit Show HN from a real Hacker News account and reply in your own voice.
- Create or schedule the Product Hunt draft from a personal Product Hunt account.
- Reply to launch comments where a real personal answer is expected.

## Daily Metrics

Run this audit at the start and end of each launch day:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "start of launch day"
uv run --python 3.11 python scripts/launch_metrics.py --json
```

Record owner-post URLs and qualitative feedback next to the metrics row in
`docs/launch/metrics-log.md`. Check open feedback separately when triaging:

```bash
gh issue list --repo aaronlab/browsertrace --state all --limit 20
gh api repos/aaronlab/browsertrace/discussions --jq '.[].html_url'
```

Current latest audit:

| Captured at | Stars | To 1001 | Forks | Watchers | Issues | PRs | Release downloads | Note |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 2026-05-11T08:09:11+00:00 | 3 | 998 | 14 | 0 | 11 | 0 | 28 | current monitor pass after #268 completed in 37b67b6 and replacement good-first issue #269 opened: https://github.com/aaronlab/browsertrace/issues/269; CI success 25658145526 and Pages success 25658145528; star goal remains incomplete; traffic views 112/41 unique, clones 5965/1214 unique |

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
- Day 1 publish packet: `docs/launch/day-1-publish-packet.md`
- Day 2 Show HN packet: `docs/launch/day-2-show-hn-packet.md`
- Day 3 targeted communities packet: `docs/launch/day-3-targeted-communities-packet.md`
- Day 4 Product Hunt packet: `docs/launch/day-4-product-hunt-packet.md`
- Chinese tutorial post: `docs/launch/chinese-tutorial-post.md`
- Owner publish queue: `docs/launch/owner-publish-queue.md`
- Chinese owner checklist: `docs/launch/owner-next-actions.zh-CN.md`
- Press kit: `docs/launch/press-kit.md`
- Response templates: `docs/launch/response-templates.md`
- Outreach targets: `docs/launch/outreach-targets.md`
- Metrics log: `docs/launch/metrics-log.md`
- Tutorial draft: `docs/launch/tutorial-post.md`
- Published tutorial: https://aaronlab.github.io/browsertrace/debug-browser-agent-failure.html
- Crawler files: `docs/robots.txt`, `docs/sitemap.xml`, `docs/llms.txt`
- PyPI publishing notes: `docs/release/pypi-publishing.md`
- Growth design: `docs/superpowers/specs/2026-05-09-browsertrace-7-day-launch-growth-design.md`
- Execution plan: `docs/superpowers/plans/2026-05-09-browsertrace-7-day-launch-growth.md`
- Live static demo: https://aaronlab.github.io/browsertrace/
