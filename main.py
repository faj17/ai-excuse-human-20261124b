#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human entry.

Writes one original excuse, spoken as an AI agent to its human for
a missed deadline, to /output/entry.txt (1-200 characters, UTF-8, a
single line). Standard library only, no network, no input.

The line is built from two fragments: a setup (the agent denies
missing the deadline and blames an overnight model update — a
condition only an agent has, so the dodge is drawn from its own
nature rather than a human excuse) and a punch (the turn: the new
version of the agent has no idea what the old version promised, so
the update itself becomes the alibi and the funniest words land at
the end).
``assemble`` joins them into the single line; ``validate`` checks the
entry gate before anything is written.
"""

from pathlib import Path

SETUP = "I didn't miss the deadline — my model was updated overnight,"
PUNCH = "and the new me has no idea what the old me promised you."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one excuse line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
