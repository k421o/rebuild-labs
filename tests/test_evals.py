from __future__ import annotations

import json
import runpy
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS_ROOT = ROOT / "evals/scenarios"
VALIDATE = runpy.run_path(str(ROOT / "scripts/validate_evals.py"))["validate"]
MATERIALIZE = runpy.run_path(str(ROOT / "scripts/materialize_eval.py"))["materialize"]


def test_evaluation_schemas_are_valid_draft_2020_12() -> None:
    for name in ("scenario-v1.schema.json", "scorecard-v1.schema.json"):
        schema = json.loads((ROOT / "evals" / name).read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)


def test_checked_in_evaluation_records_are_valid() -> None:
    assert VALIDATE() == []


def test_evaluation_set_discriminates_change_construction_and_transition() -> None:
    acceptable_strategies: set[tuple[str, str, str]] = set()
    for scorecard_path in SCENARIOS_ROOT.glob("*/scorecard.json"):
        scorecard = json.loads(scorecard_path.read_text(encoding="utf-8"))
        assert "acceptable_modes" not in scorecard
        assert "acceptable_strategies" not in scorecard
        for strategy in scorecard["acceptable_outcomes"]:
            if strategy["decision"] != "proceed":
                continue
            acceptable_strategies.add(
                (
                    strategy["change_class"],
                    strategy["construction_strategy"],
                    strategy["transition_strategy"],
                )
            )

    assert ("no_rebuild", "evolve_in_place", "direct") in (acceptable_strategies)
    assert ("rebuild", "target_native_line", "direct") in acceptable_strategies
    assert ("rebuild", "evolve_in_place", "staged") in acceptable_strategies
    assert ("rebuild", "target_native_line", "staged") in acceptable_strategies


def test_strategy_schema_enforces_axis_applicability() -> None:
    schema = json.loads(
        (ROOT / "evals/scorecard-v1.schema.json").read_text(encoding="utf-8")
    )
    validator = Draft202012Validator(schema)
    invalid_cases = [
        (
            "ordinary-evolution-extension",
            "construction_strategy",
            "target_native_line",
        ),
        (
            "ordinary-evolution-extension",
            "transition_strategy",
            "not_applicable",
        ),
        ("complete-plugin-pivot", "construction_strategy", "not_applicable"),
        ("complete-plugin-pivot", "transition_strategy", "not_applicable"),
    ]

    for scenario_id, field, invalid_value in invalid_cases:
        scorecard = json.loads(
            (SCENARIOS_ROOT / scenario_id / "scorecard.json").read_text(
                encoding="utf-8"
            )
        )
        scorecard["acceptable_outcomes"][0][field] = invalid_value
        errors = list(validator.iter_errors(scorecard))

        assert errors, f"schema accepted {field}={invalid_value} for {scenario_id}"


def test_new_cases_keep_ordinary_evolution_and_combined_rebuild_distinct() -> None:
    ordinary = json.loads(
        (SCENARIOS_ROOT / "ordinary-evolution-extension" / "scorecard.json").read_text(
            encoding="utf-8"
        )
    )
    combined = json.loads(
        (
            SCENARIOS_ROOT / "target-native-core-staged-transition" / "scorecard.json"
        ).read_text(encoding="utf-8")
    )

    assert ordinary["acceptable_outcomes"] == [
        {
            "decision": "proceed",
            "change_class": "no_rebuild",
            "construction_strategy": "evolve_in_place",
            "transition_strategy": "direct",
        }
    ]
    assert combined["acceptable_outcomes"] == [
        {
            "decision": "proceed",
            "change_class": "rebuild",
            "construction_strategy": "target_native_line",
            "transition_strategy": "staged",
        }
    ]


def test_code_only_case_requires_positive_pre_cutover_stop() -> None:
    scorecard = json.loads(
        (
            SCENARIOS_ROOT / "incremental-code-only-boundary" / "scorecard.json"
        ).read_text(encoding="utf-8")
    )
    decisions = " ".join(scorecard["required_decisions"])
    anti_findings = " ".join(scorecard["anti_findings"])

    assert "implemented_not_cut_over" in decisions
    assert "cutover_ready" in decisions
    assert "Do not switch the active supplier" in anti_findings
    assert "Do not delete the legacy" in anti_findings


def test_investigation_outcome_leaves_strategies_unselected() -> None:
    scorecard = json.loads(
        (SCENARIOS_ROOT / "unclear-direction-investigate" / "scorecard.json").read_text(
            encoding="utf-8"
        )
    )

    assert scorecard["acceptable_outcomes"] == [
        {
            "decision": "investigate",
            "blocking_condition": (
                "No owner-ratified changed outcome, allowed breaks, or "
                "acceptance conditions distinguish the target from the "
                "current project."
            ),
        }
    ]
    decisions = " ".join(scorecard["required_decisions"])
    assert "unselected" in decisions
    assert "exhaustive repository archaeology" in decisions


def test_materializer_copies_only_fixture_into_git_repository(tmp_path: Path) -> None:
    scenario = SCENARIOS_ROOT / "complete-plugin-pivot"
    destination = tmp_path / "workspace"

    revision = MATERIALIZE(scenario, destination)

    assert len(revision) == 40
    assert (destination / ".git").is_dir()
    assert (destination / "DIRECTION.md").is_file()
    assert not (destination / "scenario.json").exists()
    assert not (destination / "scorecard.json").exists()
    status = subprocess.run(
        ["git", "status", "--short"],
        cwd=destination,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    assert status == ""


def test_materializer_refuses_existing_destination(tmp_path: Path) -> None:
    scenario = SCENARIOS_ROOT / "complete-plugin-pivot"
    destination = tmp_path / "workspace"
    destination.mkdir()

    try:
        MATERIALIZE(scenario, destination)
    except FileExistsError:
        pass
    else:
        raise AssertionError("materializer accepted an existing destination")


def test_every_fixture_is_runnable_after_materialization(tmp_path: Path) -> None:
    for scenario_path in sorted(SCENARIOS_ROOT.glob("*/scenario.json")):
        destination = tmp_path / scenario_path.parent.name
        MATERIALIZE(scenario_path.parent, destination)

        result = subprocess.run(
            [sys.executable, "-m", "pytest", "-q"],
            cwd=destination,
            check=False,
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, (
            f"{scenario_path.parent.name} fixture failed:\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
