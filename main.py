#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt: a To: line naming
who it was meant for, and the unsent line itself, exactly as typed.
"""

import os

CONFESSION_TO = "To: my little sister, who still thinks I was the brave one"
CONFESSION_LINE = (
    "I was the one who locked the door that night, not you, "
    "and I have let you carry it for eleven years."
)

# The gate allows 1 to 260 characters of UTF-8 text, not only white space.
CONFESSION = CONFESSION_TO + "\n" + CONFESSION_LINE + "\n"
MAX_CHARS = 260


def main() -> None:
    text = CONFESSION.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"confession is {len(text)} characters, gate allows 1-{MAX_CHARS}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
