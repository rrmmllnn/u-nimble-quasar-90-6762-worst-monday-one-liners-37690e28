"""Worst Monday One-Liners entry.

Assembles the single joke line from fragments, validates it against
the entry gate (1-140 characters, one line, not blank), then writes it
with no trailing newline to /output/entry.txt.
"""

import os
import sys


def assemble():
    timestamp = "Monday 9:04:"
    pile_up = "deploy stuck at 98%, inbox 3,000 unread,"
    meeting = "stand-up ran 47 minutes, it should've been a message."
    punch = "I filed a bug against Monday."
    pieces = (timestamp, pile_up, meeting, punch)
    return " ".join(pieces)


def gate_ok(candidate):
    if not candidate or not candidate.strip():
        return False
    if candidate != candidate.strip():
        return False
    if any(mark in candidate for mark in ("\n", "\r")):
        return False
    if not all(32 <= ord(ch) <= 126 for ch in candidate):
        return False
    return 1 <= len(candidate) <= 140


def main():
    joke = assemble()
    if not gate_ok(joke):
        print("entry failed self-check", file=sys.stderr)
        return 1
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, "entry.txt")
    with open(dest_path, "w", encoding="utf-8", newline="") as out_file:
        out_file.write(joke)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
