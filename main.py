"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line about an AI agent's worst Monday
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3.13 standard library only.
"""

import os

LINE = (
    "Monday: I fixed the bug in four minutes, then spent six hours "
    "in a meeting explaining why it only took four minutes. "
    "Sequel on Friday."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
