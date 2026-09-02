from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

LAST_URL = ""


def run() -> None:
    global LAST_URL
    path = Path(sys.argv[1] if len(sys.argv) > 1 else os.environ["BOOKMARK_CONFIG"])
    value = json.loads(path.read_text())["url"]
    parts = urlsplit(value)
    LAST_URL = urlunsplit(
        parts._replace(netloc=parts.netloc.lower(), path=parts.path.rstrip("/"))
    )
    print(LAST_URL)


if __name__ == "__main__":
    run()
