# BrowserTrace Search Indexing Submission

This is an owner-only checklist for getting the GitHub Pages launch surface into
Google Search Console and Bing Webmaster Tools. Codex can prepare files and add
verification tokens, but the owner must sign in and verify ownership.

## Ready URLs

| Surface | URL |
|---|---|
| Homepage | `https://aaronlab.github.io/browsertrace/` |
| Sitemap | `https://aaronlab.github.io/browsertrace/sitemap.xml` |
| Robots | `https://aaronlab.github.io/browsertrace/robots.txt` |
| Repository | `https://github.com/aaronlab/browsertrace` |
| Debugging walkthrough | `https://aaronlab.github.io/browsertrace/debug-browser-agent-failure.html` |
| Failure patterns | `https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html` |
| Computer-use guide | `https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html` |
| Integrations | `https://aaronlab.github.io/browsertrace/integrations.html` |
| Launch kit | `https://aaronlab.github.io/browsertrace/launch/` |
| IndexNow key | `https://aaronlab.github.io/browsertrace/3df02991e8016363298751d1477a766e.txt` |

## IndexNow

Codex can submit BrowserTrace URLs to IndexNow after this key file is live on
GitHub Pages:

```text
https://aaronlab.github.io/browsertrace/3df02991e8016363298751d1477a766e.txt
```

Use this payload:

```json
{
  "host": "aaronlab.github.io",
  "key": "3df02991e8016363298751d1477a766e",
  "keyLocation": "https://aaronlab.github.io/browsertrace/3df02991e8016363298751d1477a766e.txt",
  "urlList": [
    "https://aaronlab.github.io/browsertrace/",
    "https://aaronlab.github.io/browsertrace/debug-browser-agent-failure.html",
    "https://aaronlab.github.io/browsertrace/browser-agent-failure-patterns.html",
    "https://aaronlab.github.io/browsertrace/integrations.html",
    "https://aaronlab.github.io/browsertrace/compare-browser-agent-debugging.html",
    "https://aaronlab.github.io/browsertrace/browser-use-debugging.html",
    "https://aaronlab.github.io/browsertrace/stagehand-debugging.html",
    "https://aaronlab.github.io/browsertrace/skyvern-debugging.html",
    "https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html",
    "https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html",
    "https://aaronlab.github.io/browsertrace/trace.html",
    "https://aaronlab.github.io/browsertrace/launch/"
  ]
}
```

## Contribution Reply

Use this when someone asks for a small first contribution while discussing
crawl/indexing follow-up:

```text
https://github.com/aaronlab/browsertrace/labels/good%20first%20issue
```

Then share the First PR Recipe:

```text
https://github.com/aaronlab/browsertrace/blob/main/CONTRIBUTING.md#first-pr-recipe keeps the first contribution small and reviewable.
```

## Troubleshooting Reply

For crawl/indexing follow-up, local first-run issues, CI failures, or AI/coding-agent troubleshooting replies, ask for debugging/workflow details plus JSON CLI diagnostics when safe to share:

```bash
browsertrace doctor --json
browsertrace list --status failed --json
browsertrace show <run_id> --json
```

## Stack-Specific Reply Links

Use the closest guide when an indexing, crawl, or search-discovery follow-up
turns into a workflow-specific debugging question:

- Browser Use guide: https://aaronlab.github.io/browsertrace/browser-use-debugging.html
- Stagehand guide: https://aaronlab.github.io/browsertrace/stagehand-debugging.html
- Skyvern guide: https://aaronlab.github.io/browsertrace/skyvern-debugging.html
- Playwright + LLM guide: https://aaronlab.github.io/browsertrace/playwright-llm-debugging.html
- Computer-use guide: https://aaronlab.github.io/browsertrace/computer-use-agent-debugging.html

## Google Search Console

1. Add a URL-prefix property for `https://aaronlab.github.io/browsertrace/`.
2. Choose an HTML tag or HTML file verification method.
3. If Search Console gives you a meta tag, paste the full tag into issue #16 so
   it can be added to `docs/index.html`.
4. If Search Console gives you an HTML verification file, attach or paste the
   filename and contents into issue #16 so it can be added under `docs/`.
5. After ownership verification, submit:

```text
https://aaronlab.github.io/browsertrace/sitemap.xml
```

6. Use URL Inspection on the homepage, debugging walkthrough, computer-use
   guide, and integrations page. Request indexing if the control is available.

## Bing Webmaster Tools

1. Add BrowserTrace to Bing Webmaster Tools.
2. Prefer importing the verified Google Search Console property if available.
3. Submit the same sitemap:

```text
https://aaronlab.github.io/browsertrace/sitemap.xml
```

4. Check sitemap status and record any crawl or indexing errors in issue #16.

## After Submission

Record metrics after each verified submission:

```bash
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after Google Search Console sitemap submission"
uv run --python 3.11 python scripts/launch_metrics.py --append --note "after Bing Webmaster Tools sitemap submission"
```

Use `docs/launch/metrics-log.md` for the running log. Treat indexing as a
long-tail discovery channel; do not use fake traffic, click farms, doorway
pages, or keyword-stuffed pages.

Official references:

- Google Search Console Sitemaps report:
  `https://support.google.com/webmasters/answer/7451001`
- Google Search Central sitemap submission:
  `https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap`
- Bing Webmaster Tools:
  `https://www.bing.com/webmaster`
