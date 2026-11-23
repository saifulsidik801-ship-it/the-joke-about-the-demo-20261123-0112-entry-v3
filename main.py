#!/usr/bin/env python3
"""The joke about the demo: one line about working beside AI coding agents.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: no network, no clock, no randomness.
"""

import os
from pathlib import Path

JOKE = "My agent apologised for crashing the demo, then crashed while apologising."


def main():
    text = JOKE.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError("joke must be 1 to 280 characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
