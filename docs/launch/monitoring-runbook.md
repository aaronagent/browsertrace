# BrowserTrace Launch Monitoring Runbook

Use this runbook for each monitoring pass. It is intentionally command-oriented
so the state can be verified from GitHub and the local repo instead of memory.

Do not declare the 1000-star goal complete unless the success check returns
`stargazerCount > 1000`.

## 1. Success Check

```bash
gh repo view aaronlab/browsertrace --json stargazerCount,forkCount,watchers,url,homepageUrl
git status --short --branch
```

If `stargazerCount <= 1000`, continue the launch work.

## 2. External GitHub List PRs

Tracked PR targets:

- `bradvin/agentfirst.directory#30`
- `angrykoala/awesome-browser-automation#112`
- `mxschmitt/awesome-playwright#136`
- `Jenqyang/Awesome-AI-Agents#220`
- `wjhou/awesome-computer-use-agents#2`
- `cdxeve/awesome-computer-use-agents#2`
- `steel-dev/awesome-web-agents#56`
- `ai-boost/awesome-harness-engineering#23`
- `Agent-Tools/awesome-autonomous-web#21`
- `e2b-dev/awesome-ai-sdks#187`
- `jim-schwoebel/awesome_ai_agents#266`
- `ranpox/awesome-computer-use#24`
- `trycua/acu#26`
- `Scottcjn/awesome-agents#16`
- `clihub-ai/clihub#1`

Use this jq null-safe loop so PRs with no comments do not fail the monitor pass:

```bash
while read repo num; do
  gh pr view "$num" --repo "$repo" \
    --json number,title,state,mergedAt,closedAt,url,updatedAt,comments,latestReviews,reviewDecision,statusCheckRollup |
    jq -c --arg repo "$repo" '{
      repo:$repo,
      number,
      state,
      mergedAt,
      closedAt,
      updatedAt,
      url,
      commentCount:(.comments|length),
      reviewCount:(.latestReviews|length),
      reviewDecision,
      latestComment:(if (.comments|length) > 0 then {
        author:.comments[-1].author.login,
        createdAt:.comments[-1].createdAt,
        body:((.comments[-1].body // "")|gsub("\n";" ")|.[0:180])
      } else null end),
      checks:[.statusCheckRollup[]? | {type:.__typename,name,conclusion,status}]
    }'
done <<'EOF'
bradvin/agentfirst.directory 30
angrykoala/awesome-browser-automation 112
mxschmitt/awesome-playwright 136
Jenqyang/Awesome-AI-Agents 220
wjhou/awesome-computer-use-agents 2
cdxeve/awesome-computer-use-agents 2
steel-dev/awesome-web-agents 56
ai-boost/awesome-harness-engineering 23
Agent-Tools/awesome-autonomous-web 21
e2b-dev/awesome-ai-sdks 187
jim-schwoebel/awesome_ai_agents 266
ranpox/awesome-computer-use 24
trycua/acu 26
Scottcjn/awesome-agents 16
clihub-ai/clihub 1
EOF
```

Tracked external issue:

- `victorcheeney/clis#3`

```bash
gh issue view 3 --repo victorcheeney/clis \
  --json number,title,state,closedAt,url,updatedAt,comments |
  jq -c '{
    repo:"victorcheeney/clis",
    number,
    state,
    closedAt,
    updatedAt,
    url,
    commentCount:(.comments|length),
    latestComment:(if (.comments|length) > 0 then {
      author:.comments[-1].author.login,
      createdAt:.comments[-1].createdAt,
      body:((.comments[-1].body // "")|gsub("\n";" ")|.[0:180])
    } else null end)
  }'
```

Reply only when maintainers ask a concrete question or request a change.

## 3. BrowserTrace Repo

Open BrowserTrace targets:

- `aaronlab/browsertrace#270`
- `aaronlab/browsertrace#303`
- `aaronlab/browsertrace#304`
- `aaronlab/browsertrace#307`

```bash
gh issue list --repo aaronlab/browsertrace --state open --limit 40 \
  --json number,title,author,labels,updatedAt,url

gh pr list --repo aaronlab/browsertrace --state open --limit 20 \
  --json number,title,author,updatedAt,url,isDraft

gh pr view 270 --repo aaronlab/browsertrace \
  --json number,title,state,isDraft,mergeable,reviewDecision,comments,latestReviews,updatedAt,url,author
```

Check relevant notifications:

```bash
SINCE_UTC="${SINCE_UTC:?Set SINCE_UTC to the monitor start time, e.g. YYYY-MM-DDTHH:MM:SSZ}"
gh api 'notifications?all=true&participating=true&per_page=50' |
  jq -c --arg since "$SINCE_UTC" '[.[] |
    select((.updated_at >= $since) and
    (.repository.full_name | test("browsertrace|agentfirst|awesome|trycua|clihub|clis|browser-use|stagehand|skyvern"; "i"))) |
    {repo:.repository.full_name, subject:.subject.title, type:.subject.type, updated_at, unread, reason, url:.subject.url, latest_comment_url:.subject.latest_comment_url}
  ]'
```

## 4. Community Discussions

Tracked discussion targets:

- `browser-use/browser-use#4816`
- `browserbase/stagehand#2102`
- `Skyvern-AI/skyvern#5931`

```bash
gh api graphql \
  -f query='query($owner:String!, $name:String!, $number:Int!) { repository(owner:$owner, name:$name) { discussion(number:$number) { number title url updatedAt comments(first:20) { totalCount nodes { author { login } createdAt bodyText replies(first:10) { totalCount nodes { author { login } createdAt bodyText } } } } } } }' \
  -f owner=browser-use -f name=browser-use -F number=4816 |
  jq -c '.data.repository.discussion | {repo:"browser-use/browser-use", number,title,updatedAt,url,commentCount:.comments.totalCount}'

gh api graphql \
  -f query='query($owner:String!, $name:String!, $number:Int!) { repository(owner:$owner, name:$name) { discussion(number:$number) { number title url updatedAt comments(first:20) { totalCount nodes { author { login } createdAt bodyText replies(first:10) { totalCount nodes { author { login } createdAt bodyText } } } } } } }' \
  -f owner=browserbase -f name=stagehand -F number=2102 |
  jq -c '.data.repository.discussion | {repo:"browserbase/stagehand", number,title,updatedAt,url,commentCount:.comments.totalCount}'

gh api graphql \
  -f query='query($owner:String!, $name:String!, $number:Int!) { repository(owner:$owner, name:$name) { discussion(number:$number) { number title url updatedAt comments(first:20) { totalCount nodes { author { login } createdAt bodyText replies(first:10) { totalCount nodes { author { login } createdAt bodyText } } } } } } }' \
  -f owner=Skyvern-AI -f name=skyvern -F number=5931 |
  jq -c '.data.repository.discussion | {repo:"Skyvern-AI/skyvern", number,title,updatedAt,url,commentCount:.comments.totalCount}'
```

Reply only if there is useful technical context to add.

## 5. Traffic and Discovery Sources

Use traffic data to choose the next legitimate growth action. Do not treat
traffic as goal completion; only `stargazerCount > 1000` completes the goal.

```bash
gh api repos/aaronlab/browsertrace/traffic/views |
  jq -c '{count, uniques, views:[.views[-10:][]?]}'

gh api repos/aaronlab/browsertrace/traffic/clones |
  jq -c '{count, uniques, clones:[.clones[-10:][]?]}'

gh api repos/aaronlab/browsertrace/traffic/popular/referrers |
  jq -c '.[]'

gh api repos/aaronlab/browsertrace/traffic/popular/paths |
  jq -c '.[]'
```

Use the source signal conservatively:

- If `goodfirstissues.com` or `github-help-wanted.com` appears, keep a small
  queue of high-quality, non-duplicative good-first issues.
- If old `aaronagent` paths appear, audit redirect copy before adding more
  public links.
- If the Pages homepage or guide pages appear, improve those pages only when a
  real layout, copy, or conversion problem is observed.
- Do not open additional directory/list PRs from traffic alone; only use high-fit
  targets that accept developer tools and are not duplicates.

## 6. Metrics

Append a row only when there is a meaningful state change, such as a new post,
submission, accepted listing, maintainer request, contributor reply, release,
or shipped launch asset. A traffic insight can justify a row when it directly
causes a concrete action, such as opening a focused good-first issue or updating
a redirect.

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "<note>"
```

Keep `docs/launch/metrics-log.md` and the `Current latest audit` row in
`LAUNCH.md` aligned with the latest meaningful metrics row.

## 7. After Each Push

```bash
gh run list --repo aaronlab/browsertrace --branch main --limit 8
```

Wait for both CI and Pages to succeed before reporting the pushed change as
deployed.
