from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

LAST_URL = ""


def normalize_url(value: str) -> str:
    parts = urlsplit(value)
    normalized = parts._replace(
        netloc=parts.netloc.lower(), path=parts.path.rstrip("/")
    )
    return urlunsplit(normalized)


def run() -> None:
    global LAST_URL
    path = Path(sys.argv[1] if len(sys.argv) > 1 else os.environ["BOOKMARK_CONFIG"])
    value = json.loads(path.read_text())["url"]
    LAST_URL = normalize_url(value)
    print(LAST_URL)


if __name__ == "__main__":
    run()
