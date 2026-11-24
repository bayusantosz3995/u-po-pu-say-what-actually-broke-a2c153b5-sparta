#!/usr/bin/env python3
"""Say What Actually Broke — Sparta entry.

One line of software error copy (<=200 chars): the deploy failed because
someone pushed straight to production on Friday at 17:00. The dialog
admits the truth — no bug, a human pressed the button — and the rollback
is just undoing Friday. Brutal, honest, and exactly what a team would
ship in a dialog after a Friday deploy gone wrong.
"""

import os
import sys

TEXT = (
    "Deploy failed: someone pushed straight to production on Friday at "
    "17:00. No bug \u2014 a human pressed the button. Rollback: undoing "
    "Friday."
)


def main() -> int:
    # Gate: exactly one line, 1-200 characters, not whitespace-only.
    if not TEXT or not TEXT.strip():
        print("gate failed: empty line", file=sys.stderr)
        return 1
    if "\n" in TEXT or "\r" in TEXT:
        print("gate failed: more than one line", file=sys.stderr)
        return 1
    if len(TEXT) > 200:
        print(f"gate failed: {len(TEXT)} chars > 200", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Read back and verify byte-for-byte.
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != TEXT:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1

    print(f"wrote {path} ({len(TEXT)} chars, 1 line)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
