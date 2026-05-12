"""Run the Browser Use run-hooks adapter without installing Browser Use.

This uses a fake Browser Use-shaped agent that calls:

    await agent.run(on_step_start=hooks.on_step_start, on_step_end=hooks.on_step_end)

Run it from a source checkout:

    python examples/browser_use_run_hooks_demo.py

Then open the BrowserTrace UI:

    browsertrace
"""

from __future__ import annotations

import asyncio
import os

from browsertrace import Tracer
from browsertrace.integrations.browser_use import create_run_hooks


class DemoBrowserState:
    def __init__(self, url: str, title: str):
        self.url = url
        self.title = title
        self.tabs = ["Search", "Result"]


class DemoBrowserSession:
    def __init__(self):
        self._state = DemoBrowserState("https://example.com/search", "Search")

    async def get_browser_state_summary(self):
        return self._state

    def set_state(self, url: str, title: str) -> None:
        self._state = DemoBrowserState(url, title)


class DemoHistory:
    def __init__(self):
        self._thoughts = []
        self._outputs = []
        self._actions = []
        self._content = []
        self._urls = []

    def record(
        self,
        *,
        thought: str,
        output: dict,
        action: dict,
        extracted_content: str,
        url: str,
    ) -> None:
        self._thoughts.append(thought)
        self._outputs.append(output)
        self._actions.append([action])
        self._content.append(extracted_content)
        self._urls.append(url)

    def model_thoughts(self):
        return self._thoughts

    def model_outputs(self):
        return self._outputs

    def model_actions(self):
        return self._actions

    def extracted_content(self):
        return self._content

    def urls(self):
        return self._urls


class DemoBrowserUseRunHookAgent:
    task = "Find BrowserTrace with Browser Use hooks"

    def __init__(self):
        self.browser_session = DemoBrowserSession()
        self.history = DemoHistory()

    async def run(self, *, on_step_start, on_step_end) -> None:
        await on_step_start(self)
        self.history.record(
            thought="search for the project",
            output={"next_goal": "open BrowserTrace result"},
            action={"search_google": {"query": "BrowserTrace"}},
            extracted_content="Search results page",
            url="https://example.com/search",
        )
        await on_step_end(self)

        self.browser_session.set_state("https://example.com/results", "Result")
        await on_step_start(self)
        self.history.record(
            thought="open the first useful result",
            output={"next_goal": "inspect repository"},
            action={"click": {"selector": "#result-1"}},
            extracted_content="BrowserTrace repository",
            url="https://example.com/results",
        )
        await on_step_end(self)


async def main() -> None:
    tracer = Tracer(home=os.environ.get("BROWSERTRACE_HOME"))
    agent = DemoBrowserUseRunHookAgent()
    hooks = create_run_hooks(tracer, name="demo: browser-use run hooks flow")

    with hooks:
        await agent.run(
            on_step_start=hooks.on_step_start,
            on_step_end=hooks.on_step_end,
        )

    print(f"BrowserTrace run id: {hooks.run.id}")
    print("Recorded Browser Use run-hook steps: search_google, click")
    print("Open the local UI with: browsertrace")


if __name__ == "__main__":
    asyncio.run(main())
