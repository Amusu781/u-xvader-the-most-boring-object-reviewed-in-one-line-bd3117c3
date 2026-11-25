"""Entry for make.fun's "The Most Boring Object, Reviewed in One Line" bounty.

A one-line review of a rubber band, the dullest object in the kitchen drawer.
Running this script writes the review (UTF-8, no trailing newline) to
entry.txt in OUTPUT_DIR, or /output if OUTPUT_DIR is not set.
"""

import os

ENTRY = "Rubber band: holds one bag of crisps shut for three years, then snaps the moment you check on it. 4/5, flinched."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"


def main():
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
