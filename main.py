#!/usr/bin/env python3
"""Write one joke about the demo to /output/entry.txt.

The joke is about working beside an AI coding agent: the agent ends up
doing the whole demo while its human sits beside it, nodding along.
"""

import os
from pathlib import Path

TEXT = (
    "My AI agent wrote the demo, tested the demo, and presented the demo "
    "\u2014 I just sat there nodding like the intern it thinks I am."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
