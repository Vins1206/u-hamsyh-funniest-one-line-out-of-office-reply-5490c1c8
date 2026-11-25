"""Funniest one-line out-of-office reply.

Writes exactly one line of plain text (120 characters, no trailing
newline) to /output/entry.txt: a real-looking auto-reply whose joke is
the auto-reply itself covering for its owner, and doing it better.
Python standard library only.
"""

import os

ENTRY = "I'm out of office until Monday. My auto-reply is covering for me and, honestly, it's doing a better job than I ever did."

# The sealed gate accepts 1 to 160 characters of UTF-8 text, one line.
OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= len(ENTRY) <= 160 or "\n" in ENTRY:
        raise ValueError("entry must be a single line of 1-160 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
