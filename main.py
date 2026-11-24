#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

Deterministic, no network, no input: the joke is a constant string.
The joke's turn lands in its last words: the out-of-office reply --
meant to switch work off -- turns the vacation itself into the
passive-aggressive email it was quoting.
The output step never removes the output directory itself -- it only
clears the directory's contents, then writes entry.txt -- so the program
also works when /output is root-owned inside a sticky parent.
"""

import os
import shutil

JOKE = "I put 'per my last email' in my out-of-office reply, so now even my vacation is passive-aggressive."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
