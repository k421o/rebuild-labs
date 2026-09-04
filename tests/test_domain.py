from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_guide_consumes_domain_record_not_capability_private_template() -> None:
    guide = read("guides/README.md")

    assert "../domain/rebuild-record.md" in guide
    assert "../capabilities/" not in guide
