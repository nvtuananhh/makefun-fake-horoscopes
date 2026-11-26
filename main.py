#!/usr/bin/env python3
"""Entry program for the Fake Horoscopes bounty.

Writes one fake horoscope (at most 200 characters) to /output/entry.txt.
"""

import os

ENTRY = "Muse Spark 1.3, this week: the stars say your context window will lose 214 tokens a day, and on Friday you will finally understand the prompt — which will simply say 'never mind'."


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
