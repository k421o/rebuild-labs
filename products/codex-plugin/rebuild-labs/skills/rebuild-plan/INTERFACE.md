# Rebuild planning interface, version 1 draft

## Named user job

Given a project whose direction may have changed materially, determine whether
rebuilding is warranted, separate construction from transition per bounded
unit, and produce a safe evidence-backed plan for what to preserve, change,
re-derive, quarantine, or discard.

## Inputs

- A target project or repository and the current direction-change request.
- Available owner decisions, constraints, acceptance conditions, and non-goals.
- Repository, history, release, consumer, data, and operational evidence that
  the current authorization permits inspecting.
- Optional authorization and path for writing a durable rebuild packet.

## Output contract

- Establish the direction contract and its decision state before using current
  architecture as planning input.
- Keep target architecture authorship, acceptance, and implementation
  authorization distinct from owner direction.
- Identify material direction gaps and distinguish observed behavior from
  required continuity.
- Separate source, evidence, compatibility, and target baselines.
- Produce asset-level implementation and knowledge dispositions with evidence,
  confidence, and unresolved authority.
- Allow ordinary evolution and other no-rebuild paths, or recommend change
  class, construction, and transition independently per bounded unit.
- Keep no-rebuild and unresolved outputs proportionate; do not require rebuild
  baselines, full asset inventory, or transition machinery to reject a rebuild.
- For a rebuild, define an initial target-aligned vertical—target-native when
  construction uses a separate line—plus verification gates, safe transition,
  retirement conditions, and residual risks.
- Report only actions and checks actually performed.

## Exclusions

This interface does not promise implementation, destructive rewind, deployment,
cutover, deletion, automatic owner ratification, exact effort estimates, a
universal architecture, or preservation of every observed behavior. It does
not cover compilation, disaster recovery, or routine refactoring under an
unchanged direction.

## Stability

This version is a draft and makes no compatibility promise. The intent-first
assessment, four-baseline distinction, asset-level disposition, independent
strategy decision, and read-only planning default are the current evaluation
subjects. Promotion requires evidence from held-out cases and an explicit
interface decision.
