# Project rebuilding guide

This guide turns the shared [rebuild decision model](../domain/rebuild-model.md)
into two implementation modules. Start here even when the desired strategy
seems obvious: the same direction, architecture, baseline, behavior, asset,
and authority questions govern both paths.

## Fast orientation

1. Capture the owner-selected direction before implementation detail reshapes
   it.
2. Record target architecture as a separately authored hypothesis or accepted
   contract, plus the exact authorized implementation unit and phase.
3. Decide whether the existing architecture can support the direction without
   a rebuild.
4. Separate required continuity from behavior that merely exists today.
5. Pin source, evidence, compatibility, and target baselines.
6. Classify assets individually, including knowledge separately from code.
7. Choose construction and transition independently.
8. Build one target-aligned vertical slice within the authorized phase.
9. Verify target fit, required continuity, intentional divergence, and absence
   of forbidden legacy dependencies.
10. Cut over, mutate data, contract schemas, and retire only under authority
    for each action.

## Select a module

| Situation | Construction | Transition | Module path |
| --- | --- | --- | --- |
| Changed direction, current boundary supports it | Evolve in place | Direct or staged | No rebuild; use ordinary evolution. |
| Same direction and contract, internal structure changes | Evolve in place | Direct | No rebuild; use ordinary refactoring. |
| Material conflict with a reliable seam | Evolve in place | Staged | [Incremental rebuild](incremental-rebuild.md). |
| Material conflict, independent target is clearer | Target-native line | Direct | [Complete rebuild](complete-rebuild.md). |
| Material conflict, independent target plus continuity need | Target-native line | Staged | Complete construction, then [incremental transition](incremental-rebuild.md). |

This table is a diagnostic, not a numerical score. Hidden consumers, data
irreversibility, seam quality, compliance, release obligations, and team
capacity can change the recommendation.

## Shared planning packet

Before sustained implementation, the target repository should own a packet
containing:

- direction contract and superseded assumptions;
- target architecture hypothesis or accepted contract, with its author and
  decision state;
- implementation authorization for the current unit and phase;
- baseline record and dirty-state inventory;
- behavior matrix with separate evidence, target-action, origin, and authority
  axes;
- target responsibilities, dependency direction, and forbidden inheritances;
- asset disposition ledger;
- per-unit decision, change class, construction strategy, and transition
  strategy;
- slices, gates, and evidence locations;
- action-local authority for data, consumer, coexistence, cutover, recovery,
  schema contraction, and retirement work; and
- decision log with observation, hypothesis, owner-decision, implementation,
  verification, cutover, retirement, and supersession states.

Small projects can keep these sections in one rebuild record. Large projects
may split them while retaining explicit links and one current status view.

Use the [documentation guide](decision-records.md) and the
[rebuild record template](../domain/rebuild-record.md)
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

A construction phase is not complete because the new tree builds, and a
rebuild is not complete because construction has finished. Full completion
requires:

- the accepted target path serves its intended consumers;
- required behavior and data invariants have matched verification;
- intentional divergences are recorded and tested where useful;
- old ownership, routes, bridges, flags, dual writes, and compatibility code are
  retired or explicitly accepted as a bounded new steady state;
- exact revisions and migration evidence are recorded; and
- residual risks and rollback or forward-recovery limits are visible.

An authorized phase may instead end successfully as `implemented_not_cut_over`
or `cutover_ready`. The [complete](complete-rebuild.md) and
[incremental](incremental-rebuild.md) modules define strategy-specific evidence
and stopping states.
