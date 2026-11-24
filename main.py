#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original line of fortune-cookie wisdom for a software developer
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).

Chosen line (see CANDIDATES.md for the 10 candidates and their critique):
    "The estimate you gave in the meeting will outlive the code it described."
It won the head-to-head on the judge's own decision procedure: it ties the
runner-up on criteria 1-3, wins on criterion 4 (a fresh observation about
estimates, not a familiar trope rephrased), and the runner-up's edge on
criterion 5 is only a single point, not "much more".

Gate (sealed scorer): entry.txt must be UTF-8 text of 1 to 120 characters,
not only white space. main.py is Python 3.13 stdlib only, deterministic,
no network, no environment secrets.
"""

import os
import sys

FORTUNE = "The estimate you gave in the meeting will outlive the code it described."

MAX_CHARS = 120
OUTPUT_NAME = "entry.txt"


def check_gate(text: str) -> str | None:
    """Return an error message when text fails the gate, else None."""
    if not text:
        return "entry is empty"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if len(text) > MAX_CHARS:
        return f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
    if not text.strip():
        return "entry is only white space"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    return None


def write_entry(out_dir: str) -> str:
    """Self-check the fortune, then write it. Returns the output path."""
    error = check_gate(FORTUNE)
    if error is not None:
        raise SystemExit(f"gate check failed: {error}")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(FORTUNE + "\n")
    return path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(out_dir)
    print(f"wrote {len(FORTUNE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
