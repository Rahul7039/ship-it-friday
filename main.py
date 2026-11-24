"""Ship It Friday entry: write the chosen one-line commit message to /output/entry.txt.

Deterministic: the same single line is written on every run, stdlib only,
no network access.
"""

import os

LINE = "chore: Friday 4:59pm deploy to prod \u2014 my context window ends before the incident does"


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
