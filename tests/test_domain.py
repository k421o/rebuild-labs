from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_domain_defines_two_primary_rebuild_modules() -> None:
    readme = read("README.md")
    model = read("domain/rebuild-model.md")

    assert "Complete rebuild" in readme
    assert "Incremental rebuild" in readme
    assert "ordinary refactor" in model.casefold()
    assert "Projects may use complete rebuilding" in model


def test_domain_separates_four_baselines() -> None:
    model = read("domain/rebuild-model.md")
    glossary = read("domain/glossary.md")

    for name in (
        "Source baseline",
        "Evidence baseline",
        "Compatibility baseline",
        "Target baseline",
    ):
        assert name.split()[0] in model
        assert name in glossary


def test_domain_preserves_knowledge_separately_from_code() -> None:
    model = read("domain/rebuild-model.md")
    record = read("domain/rebuild-record.md")

    for disposition in ("Salvage", "Refactor", "Re-derive", "Quarantine", "Discard"):
        assert disposition in model
    assert "Implementation" in record
    assert "Knowledge" in record
    assert "knowledge is current contract" in record.casefold()


def test_rewind_is_non_destructive() -> None:
    combined = "\n".join(
        read(path)
        for path in (
            "README.md",
            "domain/glossary.md",
            "guides/complete-rebuild.md",
            "capabilities/rebuild-complete/SKILL.md",
        )
    )

    normalized = " ".join(combined.split())
    assert "Never move, reset, clean, or delete the active checkout" in normalized
    assert "does not mean moving or deleting the active branch" in combined


def test_guide_consumes_domain_record_not_capability_private_template() -> None:
    guide = read("guides/README.md")

    assert "../domain/rebuild-record.md" in guide
    assert "../capabilities/" not in guide
