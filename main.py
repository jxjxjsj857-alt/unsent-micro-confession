#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt: a To: line naming
who it was meant for, and the unsent line itself, exactly as typed.
"""

import os

CONFESSION = (
    "To: my little sister, who still thinks I was the brave one\n"
    "I was the one who locked the door that night, not you, "
    "and I have let you carry it for eleven years.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
