from __future__ import annotations

import csv
import sys


def run(path: str) -> None:
    with open(path, newline="") as source:
        rows = list(csv.DictReader(source))
    total = sum(int(row["units"]) for row in rows)
    print(f"Total units: {total}")


if __name__ == "__main__":
    run(sys.argv[1])
