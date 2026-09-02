from __future__ import annotations

import json
import runpy
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS_ROOT = ROOT / "evals/scenarios"
VALIDATE = runpy.run_path(str(ROOT / "scripts/validate_evals.py"))["validate"]
MATERIALIZE = runpy.run_path(str(ROOT / "scripts/materialize_eval.py"))["materialize"]


def test_checked_in_evaluation_records_are_valid() -> None:
    assert VALIDATE() == []


def test_initial_set_discriminates_modes_and_false_positive() -> None:
    acceptable_modes: set[str] = set()
    for scorecard_path in SCENARIOS_ROOT.glob("*/scorecard.json"):
        scorecard = json.loads(scorecard_path.read_text(encoding="utf-8"))
        acceptable_modes.update(scorecard["acceptable_modes"])

    assert "complete_rebuild" in acceptable_modes
    assert "incremental_rebuild" in acceptable_modes
    assert "ordinary_refactor" in acceptable_modes


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
