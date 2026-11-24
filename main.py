#!/usr/bin/env python3
"""One Letter for Your Day — entry program.

The entry is a single letter, K, standing for the word "knackered":
utterly exhausted after a long day, flattened on the sofa with your
shoes still on. It was chosen over nine other candidates (amazing,
zero sleep, Friday-feeling, hungover, tired, meltdown, doomscrolling,
procrastinated, jetlagged) because it is the most vivid, funniest and
truest of them, and because K has one dominant day-word behind it
where the obvious letters split across several weaker ones. See
README.md for the full candidate table.

The program writes exactly that one letter, and nothing else, to
/output/entry.txt, then verifies the file holds exactly one ASCII
letter A-Z before exiting.
"""

import os
import sys

LETTER = "K"
WORD_BEHIND_IT = "knackered"
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

    # Self-check: the gate accepts exactly one ASCII letter, A-Z, and
    # nothing else — no word, no gloss, no punctuation, no newline.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if len(written) != 1 or not ("A" <= written <= "Z"):
        print(f"invalid entry: {written!r}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
