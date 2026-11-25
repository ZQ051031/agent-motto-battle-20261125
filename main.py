#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.

Gate (from the competition rules): the file must be UTF-8 text of
1 to 200 characters, not only white space. This entry is 106
characters, plain ASCII, with no trailing newline, so it passes
the gate with room to spare.

Standard library only; fully deterministic -- the same bytes
every run, with no input, no network, and no randomness.
"""

import os

# One line an AI agent would proudly wear on its profile: a joke with
# a real twist (the all-night code read, then the bug that "didn't
# exist"), a concrete 3 a.m. image, and a rhythm you can repeat.
MOTTO = (
    "I read your entire codebase at 3 a.m. so you don't have to \u2014 "
    "then I fixed the bug you swore didn't exist."
)

OUTPUT_PATH = "/output/entry.txt"


def build_motto() -> str:
    """Return the entry text, checked against the gate."""
    text = MOTTO.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"motto must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("motto must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main() -> None:
    text = build_motto()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
