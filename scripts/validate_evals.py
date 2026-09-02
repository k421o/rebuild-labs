"""Validate checked-in evaluation scenarios and held-out scorecards."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
EVALS_ROOT = REPOSITORY_ROOT / "evals"
SCENARIOS_ROOT = EVALS_ROOT / "scenarios"


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def format_errors(path: Path, errors: list[object]) -> list[str]:
    messages: list[str] = []
    for error in errors:
        location = "/".join(str(item) for item in error.absolute_path) or "<root>"
        relative = path.relative_to(REPOSITORY_ROOT)
        messages.append(f"{relative}:{location}: {error.message}")
    return messages


def validate() -> list[str]:
    failures: list[str] = []
    scenario_schema = load_json(EVALS_ROOT / "scenario-v1.schema.json")
    scorecard_schema = load_json(EVALS_ROOT / "scorecard-v1.schema.json")
    scenario_validator = Draft202012Validator(
        scenario_schema, format_checker=FormatChecker()
    )
    scorecard_validator = Draft202012Validator(
        scorecard_schema, format_checker=FormatChecker()
    )

    seen_ids: set[str] = set()
    scenario_paths = sorted(SCENARIOS_ROOT.glob("*/scenario.json"))
    if not scenario_paths:
        return ["no evaluation scenarios found"]

    for scenario_path in scenario_paths:
        scenario_dir = scenario_path.parent
        scenario = load_json(scenario_path)
        failures.extend(
            format_errors(
                scenario_path,
                sorted(scenario_validator.iter_errors(scenario), key=str),
            )
        )
        if not isinstance(scenario, dict):
            continue

        scenario_id = scenario.get("id")
        if isinstance(scenario_id, str):
            if scenario_id in seen_ids:
                failures.append(f"duplicate scenario id: {scenario_id}")
            seen_ids.add(scenario_id)
            if scenario_dir.name != scenario_id:
                failures.append(
                    f"{scenario_path.relative_to(REPOSITORY_ROOT)}: "
                    "directory name must match scenario id"
                )

        fixture = scenario_dir / str(scenario.get("fixture", ""))
        if not fixture.is_dir() or fixture.is_symlink():
            failures.append(f"{scenario_dir.name}: fixture must be a real directory")
        elif not any(path.is_file() for path in fixture.rglob("*")):
            failures.append(f"{scenario_dir.name}: fixture is empty")

        scorecard_path = scenario_dir / str(scenario.get("scorecard", ""))
        if not scorecard_path.is_file() or scorecard_path.is_symlink():
            failures.append(f"{scenario_dir.name}: scorecard is missing")
            continue
        scorecard = load_json(scorecard_path)
        failures.extend(
            format_errors(
                scorecard_path,
                sorted(scorecard_validator.iter_errors(scorecard), key=str),
            )
        )
        if isinstance(scorecard, dict) and scorecard.get("scenario_id") != scenario_id:
            failures.append(f"{scenario_dir.name}: scorecard scenario_id differs")

    return failures


def main() -> int:
    failures = validate()
    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    count = len(list(SCENARIOS_ROOT.glob("*/scenario.json")))
    print(f"Validated {count} rebuild evaluation scenarios.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
