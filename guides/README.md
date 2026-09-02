# Project rebuilding guide

This guide turns the shared [rebuild decision model](../domain/rebuild-model.md)
into two implementation modules. Start here even when the desired mode seems
obvious: the same direction, baseline, behavior, asset, and authority questions
govern both paths.

## Fast orientation

1. Capture the current direction before implementation detail reshapes it.
2. Separate required continuity from behavior that merely exists today.
3. Pin source, evidence, compatibility, and target baselines.
4. Classify assets individually, including knowledge separately from code.
5. Choose how the target is constructed and how consumers transition.
6. Build one target-native vertical slice.
7. Verify target fit, required continuity, intentional divergence, and absence
   of forbidden legacy dependencies.
8. Cut over and retire only under explicit authority.

## Select a module

| Architectural discontinuity | Continuity need | Starting recommendation |
| --- | --- | --- |
| Low | Any | Use an ordinary refactor unless stronger evidence appears. |
| Moderate | High | [Incremental rebuild](incremental-rebuild.md) through one reliable seam. |
| High | Low or manageable | [Complete rebuild](complete-rebuild.md) on an isolated implementation line. |
| High | High | Build a complete target core, then use incremental cutover around it. |

This table is a diagnostic, not a numerical score. Hidden consumers, data
irreversibility, seam quality, compliance, release obligations, and team
capacity can change the recommendation.

## Shared planning packet

Before sustained implementation, the target repository should own a packet
containing:

- target charter and superseded assumptions;
- baseline record and dirty-state inventory;
- behavior matrix: preserve, intentionally change, remove, or unresolved;
- target responsibilities, dependency direction, and forbidden inheritances;
- asset disposition ledger;
- rebuild-unit and mode map;
- slices, gates, and evidence locations;
- data, consumer, coexistence, cutover, recovery, and retirement plan; and
- decision log with observation, hypothesis, owner-decision, implementation,
  verification, cutover, retirement, and supersession states.

Small projects can keep these sections in one rebuild record. Large projects
may split them while retaining explicit links and one current status view.

Use the [documentation guide](decision-records.md) and the
[rebuild packet template](../capabilities/rebuild-plan/references/rebuild-packet-template.md)
to create the packet without turning past architecture into current policy.

## Common asset decision

Decide implementation and knowledge separately:

| Implementation | Knowledge that may still survive |
| --- | --- |
| Salvage unchanged | Contract, tests, rationale, operational notes |
| Refactor | Preserved responsibility and edge cases |
| Re-derive | Behavior, domain rule, example, failure lesson |
| Quarantine | Provenance questions and bounded reference |
| Discard | Decision history explaining intentional exclusion |

Do not maximize code reuse or rewrite percentage. Optimize for target fit,
verified continuity, understandable dependency direction, and safe transition.

## Completion standard

A rebuild is not complete because the new tree builds. Completion requires:

- the accepted target path serves its intended consumers;
- required behavior and data invariants have matched verification;
- intentional divergences are recorded and tested where useful;
- old ownership, routes, bridges, flags, dual writes, and compatibility code are
  retired or explicitly accepted as a bounded new steady state;
- exact revisions and migration evidence are recorded; and
- residual risks and rollback or forward-recovery limits are visible.

The [complete](complete-rebuild.md) and
[incremental](incremental-rebuild.md) modules define mode-specific evidence.
