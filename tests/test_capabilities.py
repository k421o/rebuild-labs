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
        interface = (directory / "INTERFACE.md").read_text(encoding="utf-8")
        openai = yaml.safe_load(
            (directory / "agents/openai.yaml").read_text(encoding="utf-8")
        )

        assert metadata["name"] == name
        assert isinstance(metadata["description"], str)
        assert len(metadata["description"]) >= 120
        assert "Named user job" in interface
        assert "Output contract" in interface
        assert "Exclusions" in interface
        assert f"${name}" in openai["interface"]["default_prompt"]


def test_capability_trigger_boundaries_do_not_overlap_silently() -> None:
    plan = (CAPABILITIES_ROOT / "rebuild-plan/SKILL.md").read_text(encoding="utf-8")
    complete = (CAPABILITIES_ROOT / "rebuild-complete/SKILL.md").read_text(
        encoding="utf-8"
    )
    incremental = (CAPABILITIES_ROOT / "rebuild-incremental/SKILL.md").read_text(
        encoding="utf-8"
    )

    assert "Planning is read-only by default" in plan
    assert "Confirm that the user requested implementation" in complete
    assert "Confirm implementation is requested" in incremental
    assert "use rebuild-plan" in complete.split("---", 2)[1]
    assert "use rebuild-plan" in incremental.split("---", 2)[1]


def test_implementation_skills_consume_all_shared_plan_sources() -> None:
    references = sorted((CAPABILITIES_ROOT / "rebuild-plan/references").glob("*.md"))
    assert len(references) == 4
    for name in ("rebuild-complete", "rebuild-incremental"):
        skill = (CAPABILITIES_ROOT / name / "SKILL.md").read_text(encoding="utf-8")
        assert "read every file" in skill
        assert "../rebuild-plan/references/" in skill


def test_capability_references_are_mapped_domain_projections() -> None:
    mapping = (CAPABILITIES_ROOT / "README.md").read_text(encoding="utf-8")
    references = sorted((CAPABILITIES_ROOT / "rebuild-plan/references").glob("*.md"))

    for reference in references:
        text = reference.read_text(encoding="utf-8")
        relative = reference.relative_to(CAPABILITIES_ROOT).as_posix()
        assert "Derived projection" in text
        assert relative in mapping

    for canonical in (
        "domain/glossary.md",
        "domain/rebuild-model.md",
        "domain/rebuild-record.md",
        "docs/domain-charter.md",
    ):
        assert canonical in mapping


def test_draft_interfaces_make_no_compatibility_freeze() -> None:
    for name in CAPABILITY_NAMES:
        interface = (CAPABILITIES_ROOT / name / "INTERFACE.md").read_text(
            encoding="utf-8"
        )
        assert "makes no compatibility promise" in interface
        assert "Version 1 freezes" not in interface


def test_plan_is_gateway_and_transition_authority_is_action_local() -> None:
    plan = (CAPABILITIES_ROOT / "rebuild-plan/SKILL.md").read_text(encoding="utf-8")
    complete = (CAPABILITIES_ROOT / "rebuild-complete/SKILL.md").read_text(
        encoding="utf-8"
    )
    incremental = (CAPABILITIES_ROOT / "rebuild-incremental/SKILL.md").read_text(
        encoding="utf-8"
    )

    assert "mandatory gateway" in plan
    assert "ordinary evolution" in plan
    assert "implemented_not_cut_over" in complete
    assert "implemented_not_cut_over" in incremental
    assert "action-local authority" in complete
    assert "Action-local authority" in incremental


def test_capabilities_have_no_scaffold_placeholders() -> None:
    for path in CAPABILITIES_ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        assert "TODO" not in text
        assert "TBD" not in text
