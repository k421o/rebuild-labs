# Rebuild planning interface, version 1 draft

## Named user job

Given a project whose direction may have changed materially, distinguish a
rebuild from ordinary refactoring, select complete or incremental rebuilding
per bounded unit, and produce a safe evidence-backed plan for what to preserve,
change, re-derive, quarantine, or discard.

## Inputs

- A target project or repository and the current direction-change request.
- Available owner decisions, constraints, acceptance conditions, and non-goals.
- Repository, history, release, consumer, data, and operational evidence that
  the current authorization permits inspecting.
- Optional authorization and path for writing a durable rebuild packet.

## Output contract

- Establish target direction and its decision state before using current
  architecture as planning input.
- Identify material direction gaps and distinguish observed behavior from
  required continuity.
- Separate source, evidence, compatibility, and target baselines.
- Produce asset-level implementation and knowledge dispositions with evidence,
  confidence, and unresolved authority.
- Recommend ordinary refactor, complete rebuild, incremental rebuild, a named
  combination, defer, or investigation per bounded unit.
- Define an initial target-native vertical, verification gates, safe transition,
  retirement conditions, and residual risks.
- Report only actions and checks actually performed.

## Exclusions

This interface does not promise implementation, destructive rewind, deployment,
cutover, deletion, automatic owner ratification, exact effort estimates, a
universal architecture, or preservation of every observed behavior. It does
not cover compilation, disaster recovery, or routine refactoring under an
unchanged direction.

## Compatibility

Version 1 freezes the intent-first assessment, four-baseline distinction,
asset-level disposition, per-unit mode decision, and read-only default. The
record format remains a draft until evaluation cases demonstrate a stable
machine-checkable schema.
