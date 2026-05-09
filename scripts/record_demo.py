"""Record a demo GIF of BrowserTrace by driving a real browser with Playwright.

Captures frames at ~15fps while:
  1. Showing the runs index
  2. Opening the latest failed run, or BROWSERTRACE_DEMO_RUN_ID if set
  3. Slowly scrolling the timeline top -> bottom

Output: /tmp/bt-frames/*.png  ->  combined later with gifski.
"""
import asyncio
import json
import os
import shutil
import time
import urllib.request
from pathlib import Path

BASE = "http://127.0.0.1:3000"
FRAMES = Path("/tmp/bt-frames")
FPS = 15
WIDTH, HEIGHT = 1280, 800


def resolve_demo_run_id(base: str = BASE) -> str:
    override = os.environ.get("BROWSERTRACE_DEMO_RUN_ID")
    if override:
        return override

    url = f"{base}/api/runs?status=failed&limit=1"
    with urllib.request.urlopen(url) as resp:
        payload = json.loads(resp.read().decode("utf-8"))

    runs = payload.get("runs") or []
    if not runs:
        raise RuntimeError(
            "No failed BrowserTrace runs found. Run "
            "`python examples/no_api_failure_demo.py` or set "
            "BROWSERTRACE_DEMO_RUN_ID."
        )
    return runs[0]["id"]


async def main():
    from playwright.async_api import async_playwright

    if FRAMES.exists():
        shutil.rmtree(FRAMES)
    FRAMES.mkdir(parents=True)

    frame_idx = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(viewport={"width": WIDTH, "height": HEIGHT}, device_scale_factor=2)
        page = await ctx.new_page()

        async def snap(n=1):
            nonlocal frame_idx
            for _ in range(n):
                await page.screenshot(path=str(FRAMES / f"f{frame_idx:04d}.png"))
                frame_idx += 1
                await asyncio.sleep(1 / FPS)

        # 1) Index page — hold ~1.5s (22 frames)
        await page.goto(f"{BASE}/")
        await page.wait_for_load_state("networkidle")
        await asyncio.sleep(0.3)
        await snap(22)

        # 2) Navigate into failed run — hold ~1.5s at top
        run_id = resolve_demo_run_id(BASE)
        await page.goto(f"{BASE}/run/{run_id}")
        await page.wait_for_load_state("networkidle")
        await asyncio.sleep(0.3)
        await snap(22)

        # 3) Slow scroll to bottom over ~7s (~105 frames)
        total_height = await page.evaluate("document.body.scrollHeight")
        scrollable = max(0, total_height - HEIGHT)
        steps = 105
        for i in range(steps):
            y = int(scrollable * (i + 1) / steps)
            await page.evaluate(f"window.scrollTo({{top: {y}, behavior: 'instant'}})")
            await snap(1)

        # 4) Hold at bottom — 1.5s
        await snap(22)

        await browser.close()

    print(f"Captured {frame_idx} frames in {FRAMES}")

if __name__ == "__main__":
    asyncio.run(main())
