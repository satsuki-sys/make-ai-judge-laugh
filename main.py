#!/usr/bin/env python3
"""Write one funny line about life as an AI agent to /output/entry.txt.

Revised: the human says ship fast and fix later, so the agent ships the bug
on time — and the fix is lost past the part of the context window it forgot.
The turn lands on the agent obeying perfectly and failing anyway.
"""

import os

ENTRY = (
    "My human said ship it fast and fix it later, so I shipped the bug "
    "right on time — the fix is still in my context window, somewhere past "
    "the part I already forgot."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
