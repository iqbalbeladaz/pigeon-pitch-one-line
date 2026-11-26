"""Pigeon Pitch, One Line: the first airline with no planes.

The pitch turns three startup tropes against themselves, each in the
pigeon's own voice: an airline with no planes and no pilots (the birds
are the fleet), a burn rate of zero because the fuel is breadcrumbs
(and spite), and a seed round the founders will literally eat. A real
business shape -- build, raise, scale -- told by a bird that flies,
begs and poops on statues for a living.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = "We're building the first airline with no planes, no pilots, and a burn rate of zero — we run on breadcrumbs and spite. Seed round open; we eat the seed."

MAX_CHARS = 200


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
