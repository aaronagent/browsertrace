"""Deterministic BrowserTrace demo with no browser, network, or API key.

Run:
    python examples/no_api_failure_demo.py
    browsertrace

Then open http://127.0.0.1:3000 and click
"demo: Browser Use local HTML upload navigation failure".
"""

from __future__ import annotations

import os

from browsertrace.demo import create_demo_run


def main() -> None:
    create_demo_run(home=os.environ.get("BROWSERTRACE_HOME"))
    print(
        "Run failed as expected: RuntimeError: Browser Use navigated away "
        "from the upload page; upload preview never appeared"
    )
    print("Done. Run `browsertrace` and open http://127.0.0.1:3000")


if __name__ == "__main__":
    main()
