from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CAPABILITIES_ROOT = ROOT / "capabilities"
CAPABILITY_NAMES = ("rebuild-plan", "rebuild-complete", "rebuild-incremental")


def frontmatter(path: Path) -> dict[str, object]:
    body = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", body, flags=re.DOTALL)
    assert match is not None, f"missing YAML frontmatter: {path}"
    parsed = yaml.safe_load(match.group(1))
    assert isinstance(parsed, dict)
    return parsed


def test_capability_set_is_explicit() -> None:
    assert {path.name for path in CAPABILITIES_ROOT.iterdir() if path.is_dir()} == set(
        CAPABILITY_NAMES
    )


def test_capabilities_have_named_interfaces_and_metadata() -> None:
    for name in CAPABILITY_NAMES:
        directory = CAPABILITIES_ROOT / name
        metadata = frontmatter(directory / "SKILL.md")
        openai = yaml.safe_load(
            (directory / "agents/openai.yaml").read_text(encoding="utf-8")
        )

        assert metadata["name"] == name
        assert isinstance(metadata["description"], str)
        assert metadata["description"].strip()
        assert f"${name}" in openai["interface"]["default_prompt"]


def test_capability_references_are_mapped_domain_projections() -> None:
    mapping = (CAPABILITIES_ROOT / "README.md").read_text(encoding="utf-8")
    references = sorted((CAPABILITIES_ROOT / "rebuild-plan/references").glob("*.md"))

    for reference in references:
        relative = reference.relative_to(CAPABILITIES_ROOT).as_posix()
        assert relative in mapping

    for canonical in (
        "domain/glossary.md",
        "domain/rebuild-model.md",
        "domain/rebuild-record.md",
        "docs/domain-charter.md",
    ):
        assert canonical in mapping


def test_capabilities_have_no_scaffold_placeholders() -> None:
    for path in CAPABILITIES_ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        assert "TODO" not in text
        assert "TBD" not in text
