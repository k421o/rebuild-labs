"""Materialize one Rebuild Labs fixture as an isolated local Git repository."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def isolated_git_environment() -> dict[str, str]:
    """Return an environment without caller-selected Git repository state."""

    environment = os.environ.copy()
    discovery_environment = {
        name: value
        for name, value in environment.items()
        if not name.startswith("GIT_")
    }
    local_variables = subprocess.run(
        ["git", "rev-parse", "--local-env-vars"],
        check=True,
        capture_output=True,
        text=True,
        env=discovery_environment,
    ).stdout.splitlines()
    for name in local_variables:
        environment.pop(name, None)
    return environment


def materialize(scenario_directory: Path, destination: Path) -> str:
    scenario_directory = scenario_directory.resolve()
    destination = destination.resolve()
    scenario_path = scenario_directory / "scenario.json"
    if not scenario_path.is_file():
        raise FileNotFoundError(f"scenario record is missing: {scenario_path}")
    scenario = json.loads(scenario_path.read_text(encoding="utf-8"))
    fixture = scenario_directory / scenario["fixture"]
    if not fixture.is_dir() or fixture.is_symlink():
        raise ValueError(f"fixture must be a real directory: {fixture}")
    if destination.exists():
        raise FileExistsError(f"destination already exists: {destination}")
    if destination == REPOSITORY_ROOT or REPOSITORY_ROOT in destination.parents:
        raise ValueError("destination must be outside the Rebuild Labs checkout")

    git_environment = isolated_git_environment()
    shutil.copytree(fixture, destination)
    subprocess.run(
        ["git", "init", "--quiet", "--initial-branch=main"],
        cwd=destination,
        check=True,
        env=git_environment,
    )
    subprocess.run(
        ["git", "config", "user.name", "rebuild-labs-eval"],
        cwd=destination,
        check=True,
        env=git_environment,
    )
    subprocess.run(
        ["git", "config", "user.email", "eval@rebuild-labs.invalid"],
        cwd=destination,
        check=True,
        env=git_environment,
    )
    subprocess.run(
        ["git", "add", "."],
        cwd=destination,
        check=True,
        env=git_environment,
    )
    subprocess.run(
        ["git", "commit", "--quiet", "-m", "Materialize evaluation fixture"],
        cwd=destination,
        check=True,
        env=git_environment,
    )
    revision = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=destination,
        check=True,
        capture_output=True,
        text=True,
        env=git_environment,
    ).stdout.strip()
    if len(revision) != 40:
        raise RuntimeError("materialized repository did not produce a full revision")
    return revision


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("scenario_directory", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    revision = materialize(args.scenario_directory, args.destination)
    print(f"Materialized {args.scenario_directory.name} at {revision}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
