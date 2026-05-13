# BrowserTrace Owner Next Actions

This is the shortest owner-facing checklist. Use it when the repo is ready and
the owner can perform account/login actions personally.

Chinese version: `docs/launch/owner-next-actions.zh-CN.md`

Do not ask for stars, upvotes, reposts, vote swaps, or artificial engagement.
Ask for workflow feedback from people building browser agents.

## Current Decision

As of 2026-05-13, more broad directory work is not the highest-priority path.
BrowserTrace has already been repositioned Browser Use-first, one external list
has accepted it, and the remaining list PRs should wait for maintainer
feedback.

The current growth blocker is owner-channel publishing:

1. If you only have one minute, publish only the X single-post fallback from
   `docs/launch/owner-social-post-packet.md` with `docs/demo.mp4` attached.
   Do not wait until LinkedIn, WeChat, Jike, Show HN, or directories are also
   ready.
2. After that URL is logged, optionally mirror the same Browser Use-first story
   to LinkedIn, one or two relevant WeChat groups, and Jike.
3. Submit Show HN from `docs/launch/owner-launch-submission-packet.md` only if
   you can stay available for several hours to answer technical comments.
4. After any channel goes live, send the post URL, group name, or send note to
   Codex so metrics can be logged and replies can be monitored.

Do not open new low-conversion directory PRs just to create activity. Wait for
maintainer feedback on the existing PRs and respond only to concrete requests.

Current one-minute unblock: publish the X single-post fallback from
`docs/launch/owner-social-post-packet.md#x`. It now leads with the
local `.html` upload failure story and mentions `browsertrace compare` for
failed-vs-good Browser Use runs.
The current open good-first issue for contributor replies is
`https://github.com/aaronlab/browsertrace/issues/371`.

Browser Use official example PR: `browser-use/browser-use#4826` is open with an
optional `examples/observability/browsertrace.py` example. The fit is stronger
than more broad directory submissions because Browser Use has an existing
observability examples area. Current state: code-style, type-checker, tests,
GitGuardian, and review checks pass; the remaining blocker is `license/cla`.
Owner action: sign the CLA at
`https://cla-assistant.io/browser-use/browser-use?pullRequest=4826`. If the
status stays pending after signing, use the recheck link:
`https://cla-assistant.io/check/browser-use/browser-use?pullRequest=4826`.
Codex can re-check the PR after you finish, but cannot sign this for you.

## 10-Minute Owner Unblock

If you only have one short session, do these in order and let Codex handle the
follow-up verification, README updates, metrics, and issue comments:

Current listing status: one tracked external GitHub list has accepted
BrowserTrace: `Jenqyang/Awesome-AI-Agents#220` is merged and listed on the
default branch. The remaining tracked list and directory submissions are still
open. Do not wait for those maintainers before publishing owner-channel posts
or Show HN. New directory submissions are lower priority than posts that reach
Browser Use users directly.

Fastest fresh technical post: publish either Browser Use angle from
`docs/launch/channel-copy.md` before or alongside the Day 1 posts:
`#fresh-browser-use-debugging-angle` for icon-only target failures,
the multi-step form drift copy around Browser Use #4476, or
`#fresh-browser-use-remote-cdp-angle` for remote-CDP hangs and event-bus lock
timing. If your audience builds custom computer-use agents, use
`#fresh-computer-use-persistent-browser-recovery-angle` for persistent browser
session recovery. These ask for real workflow feedback through concrete failure
modes. If you prefer replying to an existing discussion instead of making a new
post, use
`docs/launch/day-3-targeted-communities-packet.md#current-reddit-reply-opportunities`.

1. If you are already logged into GitHub, sign the Browser Use CLA for
   `browser-use/browser-use#4826` first:
   `https://cla-assistant.io/browser-use/browser-use?pullRequest=4826`. This
   unblocks the strongest ecosystem PR. If the CLA remains pending after
   signing, use
   `https://cla-assistant.io/check/browser-use/browser-use?pullRequest=4826`.
2. Publish only the X single-post fallback first, using `docs/demo.mp4`. When
   the platform supports alt text, use `Media Alt Text` from
   `docs/launch/day-1-publish-packet.md#media-alt-text`. Do not batch this with
   LinkedIn, WeChat, Jike, Show HN, or directory submissions. The copy/paste
   version is in `docs/launch/owner-social-post-packet.md`:

   ```text
   Browser Use failed on a local `.html` upload: it navigated to the filename and the upload preview never appeared.

   BrowserTrace replays the run and v0.1.19 adds `browsertrace compare` for failed vs good runs.

   What should it capture?
   https://github.com/aaronlab/browsertrace
   ```
3. After the X URL is logged, mirror the same story to LinkedIn, one or two
   relevant WeChat groups, and Jike from `docs/launch/day-1-publish-packet.md`.
4. If you can stay available for several hours to answer technical comments,
   submit Show HN from `docs/launch/owner-launch-submission-packet.md`. Use the
   repo URL, the prepared title, and the first comment. Skip this step until you
   can reply in your own voice.
5. After the owner-channel posts are live, send the ready owner-email
   submissions from
   `docs/launch/directory-submission-sheet.md`:
   `hello@console.dev` and `agdex.ai@gmail.com` for console.dev and AgDex.
   The shortest copy/paste version is
   `docs/launch/owner-email-send-packet.md`.
6. If you have a second short pass after those higher-intent channels, submit
   the browser-form directories from
   `docs/launch/directory-submission-sheet.md`:
   4agent.dev, AgentKart, OSS AI Hub, FOSSHUNTER, AgentsTide, and BuilderAI
   Tools. Use `hello@agentstide.com` as the AgentsTide email fallback and
   `AI Observability & Evaluation` for BuilderAI Tools. Field-ready copy is
   under `First Browser-Form Directory Field Notes`; skip AgentKart or
   AgentsTide if the target only accepts runnable autonomous agents rather than
   developer tools for agents.
7. If that batch is already done, use the second-pass directory field notes in
   `docs/launch/directory-submission-sheet.md` for CLIHunt, DeepYard,
   OpenAgent.bot, ForgeIndex, and AgentShelf.
8. If you still have time for developer-tool directories, use the same sheet for
   DevTool Center, ToolHunter, and ToolShelf. CLIs.dev has already been
   submitted as https://github.com/victorcheeney/clis/issues/3, and the
   CliHub registry PR is open at https://github.com/clihub-ai/clihub/pull/1.

Send the posted URLs, email-sent note, or any replies so Codex can log metrics
and update the tracking issues.

Fast copy/paste blocks:

- Failure patterns page:
  `https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html`
- Fresh Browser Use angle:
  `docs/launch/channel-copy.md#fresh-browser-use-debugging-angle`
- Fresh Browser Use remote-CDP angle:
  `docs/launch/channel-copy.md#fresh-browser-use-remote-cdp-angle`
- Fresh computer-use persistent browser recovery angle:
  `docs/launch/channel-copy.md#fresh-computer-use-persistent-browser-recovery-angle`
- Fresh Chinese computer-use recovery angle:
  `docs/launch/channel-copy.md#fresh-chinese-computer-use-recovery-angle`
- X: `docs/launch/channel-copy.md#x`
- X follow-up: `docs/launch/channel-copy.md#x-follow-up`
- LinkedIn: `docs/launch/channel-copy.md#linkedin`
- WeChat group: `docs/launch/channel-copy.md#wechat-group`
- Jike: `docs/launch/channel-copy.md#jike`
- 5-minute owner social post packet:
  `docs/launch/owner-social-post-packet.md`
- Show HN: `docs/launch/day-2-show-hn-packet.md#first-comment-draft`
- Product Hunt: `docs/launch/day-4-product-hunt-packet.md#maker-comment`
- 5-minute HN/Product Hunt submission packet:
  `docs/launch/owner-launch-submission-packet.md`
- console.dev email:
  `docs/launch/directory-submission-sheet.md#consoledev-email-draft`
- AgDex email: `docs/launch/directory-submission-sheet.md#agdex-email-draft`
- 5-minute owner email packet:
  `docs/launch/owner-email-send-packet.md`
- First browser-form directories:
  `docs/launch/directory-submission-sheet.md#first-browser-form-directory-field-notes`
- Listing-fit maintainer reply:
  `docs/launch/response-templates.md#maintainer-asks-whether-it-fits-this-list`

Stack-specific guide links:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## 1. PyPI Published

PyPI is no longer the install blocker. BrowserTrace is published as version
`0.1.19`:

```text
https://pypi.org/project/browsertrace/
https://pypi.org/pypi/browsertrace/json -> HTTP 200
```

Use this install command in public posts:

```bash
pip install "browsertrace[ui]"
```

The no-install PyPI trial path is:

```bash
uvx --from "browsertrace[ui]" browsertrace doctor
uvx --from "browsertrace[ui]" browsertrace demo
uvx --from "browsertrace[ui]" browsertrace list
uvx --from "browsertrace[ui]" browsertrace
```

Publish verification completed:

```bash
uv venv --python 3.11 --seed /tmp/browsertrace-pypi-verify
/tmp/browsertrace-pypi-verify/bin/python -m pip index versions browsertrace
/tmp/browsertrace-pypi-verify/bin/python -m pip install "browsertrace[ui]"
/tmp/browsertrace-pypi-verify/bin/browsertrace --help
uvx --python 3.11 --from "browsertrace[ui]" browsertrace doctor --json
```

Tracking issue: https://github.com/aaronlab/browsertrace/issues/5

## 2. Maintain The GitHub Profile README

The live public profile README repo is `aaronlab/aaronlab`. Do not use the old
profile redirect in launch copy.

Use this source draft when refreshing the profile README:

```text
docs/launch/github-profile-readme.md
```

Keep BrowserTrace as the first featured project during launch.

Profile pin: completed. GraphQL now shows `aaronlab/browsertrace` in the
public profile pinned repositories.

Tracking issue: https://github.com/aaronlab/browsertrace/issues/13

## 3. GitHub Social Preview

Social preview: completed. GitHub now reports
`usesCustomOpenGraphImage=true` for `aaronlab/browsertrace`.

Keep the reusable asset here for future launches, Product Hunt galleries, and
manual link-preview checks:

```text
docs/social-preview.png
```

## 4. Submit The Sitemap To Search Consoles

Search indexing is a slower growth channel, but it compounds after launch. The
sitemap and robots file are already live:

```text
https://aaronlab.github.io/browsertrace/sitemap.xml
https://aaronlab.github.io/browsertrace/robots.txt
```

IndexNow has already been submitted by Codex for the current launch surface.
The owner-only remaining action is to submit the sitemap in Google Search
Console and Bing Webmaster Tools.

Use:

```text
docs/launch/search-indexing-submission.md
```

Tracking issue: https://github.com/aaronlab/browsertrace/issues/16

## 5. Publish Day 1 Posts

Use this packet:

```text
docs/launch/day-1-publish-packet.md
```

Recommended order:

1. X
2. LinkedIn
3. One or two relevant WeChat AI-builder groups
4. Jike

Use `docs/demo.mp4` as primary media and `docs/demo-poster.png` as backup.

Tracking issue: https://github.com/aaronlab/browsertrace/issues/9

## 6. Submit Directories And Newsletters

Use:

```text
docs/launch/directory-submission-sheet.md
docs/launch/outreach-targets.md
```

Submit once per target. Do not repeatedly submit or ask for votes.

Already-open GitHub listing PRs and issues:

| Target | PR or issue |
|---|---|
| `bradvin/agentfirst.directory` | `https://github.com/bradvin/agentfirst.directory/pull/30`, enrichment check passed |
| `angrykoala/awesome-browser-automation` | `https://github.com/angrykoala/awesome-browser-automation/pull/112` |
| `mxschmitt/awesome-playwright` | `https://github.com/mxschmitt/awesome-playwright/pull/136` |
| `Jenqyang/Awesome-AI-Agents` | `https://github.com/Jenqyang/Awesome-AI-Agents/pull/220`, merged/listed |
| `wjhou/awesome-computer-use-agents` | `https://github.com/wjhou/awesome-computer-use-agents/pull/2` |
| `cdxeve/awesome-computer-use-agents` | `https://github.com/cdxeve/awesome-computer-use-agents/pull/2` |
| `steel-dev/awesome-web-agents` | `https://github.com/steel-dev/awesome-web-agents/pull/56` |
| `ai-boost/awesome-harness-engineering` | `https://github.com/ai-boost/awesome-harness-engineering/pull/23` |
| `Agent-Tools/awesome-autonomous-web` | `https://github.com/Agent-Tools/awesome-autonomous-web/pull/21` |
| `e2b-dev/awesome-ai-sdks` | `https://github.com/e2b-dev/awesome-ai-sdks/pull/187`, CLA check passed |
| `jim-schwoebel/awesome_ai_agents` | `https://github.com/jim-schwoebel/awesome_ai_agents/pull/266` |
| `ranpox/awesome-computer-use` | `https://github.com/ranpox/awesome-computer-use/pull/24` |
| `trycua/acu` | `https://github.com/trycua/acu/pull/26` |
| `Scottcjn/awesome-agents` | `https://github.com/Scottcjn/awesome-agents/pull/16` |
| `browser-use/awesome-projects` | `https://github.com/browser-use/awesome-projects/pull/6`, official Browser Use ecosystem list PR |
| `danielrosehill/AI-Browser-Tools` | `https://github.com/danielrosehill/AI-Browser-Tools/pull/1`, AI browser tools index PR |
| `adriannovegil/awesome-observability` | `https://github.com/adriannovegil/awesome-observability/pull/71`, LLM & AI observability list PR |
| `tensorchord/Awesome-LLMOps` | `https://github.com/tensorchord/Awesome-LLMOps/pull/470`, LLMOps observability list PR |
| `caramaschiHG/awesome-ai-agents-2026` | `https://github.com/caramaschiHG/awesome-ai-agents-2026/pull/244`, AI agent observability list PR |
| `InftyAI/Awesome-LLMOps` | `https://github.com/InftyAI/Awesome-LLMOps/issues/430`, bot PR `https://github.com/InftyAI/Awesome-LLMOps/pull/431`, Runtime/Observation request |
| `clihub-ai/clihub` | `https://github.com/clihub-ai/clihub/pull/1`, forked PR CI needs maintainer approval before it can run |
| `backblaze-labs/awesome-agent-infrastructure` | `https://github.com/backblaze-labs/awesome-agent-infrastructure/pull/4`, agent infrastructure observability list PR |
| `victorcheeney/clis` | `https://github.com/victorcheeney/clis/issues/3`, CLIs.dev directory issue opened |

Monitor maintainer feedback only. Do not open more awesome-list PRs unless the
target is high-fit, non-duplicative, and not a low-quality mass submission.

Tracking issue: https://github.com/aaronlab/browsertrace/issues/10

## 7. Monitor High-Fit GitHub Awesome List PRs

Use:

```text
docs/launch/github-awesome-list-submissions.md
```

Current tracked high-fit PRs:

- `bradvin/agentfirst.directory#30` - enrichment check passed.
- `angrykoala/awesome-browser-automation#112`
- `mxschmitt/awesome-playwright#136`
- `Jenqyang/Awesome-AI-Agents#220` - merged/listed; keep only for metrics and
  default-branch inclusion checks.
- `wjhou/awesome-computer-use-agents#2`
- `cdxeve/awesome-computer-use-agents#2`
- `steel-dev/awesome-web-agents#56`
- `ai-boost/awesome-harness-engineering#23`
- `Agent-Tools/awesome-autonomous-web#21`
- `e2b-dev/awesome-ai-sdks#187` - E2B CLA check has passed; monitor
  maintainer feedback.
- `jim-schwoebel/awesome_ai_agents#266`
- `ranpox/awesome-computer-use#24`
- `trycua/acu#26`
- `Scottcjn/awesome-agents#16`
- `browser-use/awesome-projects#6` - official Browser Use ecosystem list PR is open.
- `danielrosehill/AI-Browser-Tools#1` - AI browser tools index PR is open.
- `adriannovegil/awesome-observability#71` - LLM & AI observability list PR is open.
- `tensorchord/Awesome-LLMOps#470` - LLMOps observability list PR is open.
- `caramaschiHG/awesome-ai-agents-2026#244` - AI agent observability list PR is open.
- `InftyAI/Awesome-LLMOps#431` - bot-created Runtime/Observation PR is open;
  request issue is `InftyAI/Awesome-LLMOps#430`.
- `clihub-ai/clihub#1` - registry PR is open; forked PR CI needs
  maintainer approval before it can run.
- `backblaze-labs/awesome-agent-infrastructure#4` - agent infrastructure
  observability list PR is open.
- `victorcheeney/clis#3` - CLIs.dev directory issue is open.

Monitor maintainer feedback and do not open additional list PRs unless a target
is clearly high-fit and non-duplicative. Respond only when maintainers request
changes.

Tracking issue: https://github.com/aaronlab/browsertrace/issues/18

## Reply To Contribution Questions

If someone asks how to make a small docs fix, point to the current good first
issue queue:
https://github.com/aaronlab/browsertrace/labels/good%20first%20issue

Then share the First PR Recipe:
https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.

If someone says they want to work on it, acknowledge it and leave a short claim window
before implementing it yourself. If GitHub cannot assign the contributor, add
the `claimed` label so others know the issue has an active claimant. If
that issue is already finished, point them to the good first issue label
instead of letting the thread stall.

## Reply To Troubleshooting Questions

For local first-run issues, CI failures, or AI/coding-agent troubleshooting replies, ask for debugging/workflow details plus JSON CLI diagnostics when safe to share:

For security-sensitive reports or changes, or anything that includes private trace data, point people to the private path in the Security Policy before they share details publicly:
https://github.com/aaronlab/browsertrace/blob/main/SECURITY.md

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

## 8. Record Metrics After Each Action

After every public post, profile update, PyPI publish, or directory submission:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after <action>: <URL or note>"
uv run --python 3.11 python scripts/launch_metrics.py --json
```

The goal remains incomplete until GitHub reports more than 1000 stars:

```bash
gh repo view aaronlab/browsertrace --json stargazerCount,forkCount,watchers,url,homepageUrl
```
