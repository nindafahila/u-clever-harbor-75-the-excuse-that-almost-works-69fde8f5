#!/usr/bin/env python3
"""u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5 -- make.fun entry.

The entry is one line of plain text: the excuse a gamer texts the
boss to get out of work during GTA 6 launch week. This program
writes that line, byte for byte, to <output>/entry.txt, so every
run produces the exact same file: deterministic, no network, no
randomness, no clock. Python 3.13, standard library only.

Outside the grader's sandbox, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

ENTRY = (
    "Sorry, the plumber can only come today to fix the leak. "
    "I have to wait in. I'll be online later."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
