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
    assert "target-native line" in model
    assert "staged transition can follow either construction strategy" in model


def test_domain_allows_no_rebuild_and_separates_strategy_axes() -> None:
    model = read("domain/rebuild-model.md")
    record = read("domain/rebuild-record.md")

    assert "ordinary evolution" in model
    assert "no_rebuild" in record
    assert "Change class" in record
    assert "Construction" in record
    assert "Transition" in record


def test_domain_separates_direction_architecture_and_authority() -> None:
    record = read("domain/rebuild-record.md")
    glossary = read("domain/glossary.md")

    assert "Direction contract" in record
    assert "Target architecture" in record
    assert "Authorized implementation unit and phase" in record
    assert "Target architecture hypothesis" in glossary
    assert "Implementation authorization" in glossary


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
    assert "Never reset, clean, mass-delete" in normalized
    assert "does not mean moving or deleting the active branch" in combined


def test_empty_baseline_and_live_line_delta_have_safe_protocols() -> None:
    model = read("domain/rebuild-model.md")
    complete = read("guides/complete-rebuild.md")

    assert "orphan line" in model
    assert "separate worktree" in model
    assert "non-Git project" in model
    assert "intake live-line deltas" in complete.casefold()
    assert "Never merge the live line wholesale" in complete


def test_guide_consumes_domain_record_not_capability_private_template() -> None:
    guide = read("guides/README.md")

    assert "../domain/rebuild-record.md" in guide
    assert "../capabilities/" not in guide


def test_behavior_contract_uses_independent_axes() -> None:
    record = read("domain/rebuild-record.md")

    for axis in (
        "Evidence state",
        "Target action",
        "Origin interpretation",
        "Authority state",
    ):
        assert axis in record


def test_transition_authorities_and_positive_stop_states_are_explicit() -> None:
    record = read("domain/rebuild-record.md")
    model = read("domain/rebuild-model.md")

    for authority in (
        "traffic or consumer movement",
        "external data writes",
        "stopping old writes",
        "schema contraction",
        "deletion",
    ):
        assert authority in record.casefold() or authority in model.casefold()
    assert "implemented_not_cut_over" in model
    assert "cutover_ready" in model
