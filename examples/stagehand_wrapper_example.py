"""Run the Stagehand wrapper without installing Stagehand.

This uses a fake Stagehand-shaped page so the example is deterministic:

    python examples/stagehand_wrapper_example.py

Then open the BrowserTrace UI:

    browsertrace
"""

from __future__ import annotations

import asyncio
import os

from browsertrace import Tracer
from browsertrace.integrations.stagehand import wrap_stagehand


class DemoStagehandPage:
    url = "https://shop.example.test/cart"

    async def screenshot(self) -> bytes:
        return b"\x89PNG\r\n\x1a\n" + b"\x00" * 16

    async def act(self, instruction: str) -> dict[str, str]:
        await asyncio.sleep(0)
        return {
            "status": "completed",
            "instruction": instruction,
            "action": "click",
            "selector": "button.checkout.primary",
            "attempts": 1,
        }

    async def extract(self, instruction: str) -> dict[str, str]:
        await asyncio.sleep(0)
        return {
            "status": "completed",
            "instruction": instruction,
            "text": "Order total: $42.00",
            "tool_calls": [{"name": "extract_text", "status": "ok"}],
        }

    async def observe(self, instruction: str) -> list[dict[str, str]]:
        await asyncio.sleep(0)
        return [
            {
                "selector": "button.checkout.primary",
                "description": "Checkout button",
                "method": "click",
                "instruction": instruction,
            }
        ]


async def main() -> None:
    tracer = Tracer(home=os.environ.get("BROWSERTRACE_HOME"))
    page = wrap_stagehand(
        DemoStagehandPage(),
        tracer,
        name="demo: stagehand checkout flow",
    )

    await page.observe("find the checkout button")
    await page.act("click the checkout button")
    await page.extract("extract the order total")
    page.bt_run.close()

    print(f"BrowserTrace run id: {page.bt_run.id}")
    print("Recorded Stagehand calls: observe, act, extract")
    print("Open the local UI with: browsertrace")


if __name__ == "__main__":
    asyncio.run(main())
