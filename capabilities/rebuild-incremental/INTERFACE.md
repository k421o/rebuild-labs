# Incremental rebuild interface, version 1 draft

## Named user job

Given an explicitly authorized direction-change rebuild that needs
evolve-in-place construction or staged transition, implement one end-to-end
responsibility through a controlled seam, verify the target path, and perform
only separately authorized consumer, state, and retirement actions.

## Inputs

- Target project and applicable owner guidance.
- Owner-ratified direction contract.
- Target architecture hypothesis or accepted contract with its author and
  state.
- Explicit implementation authority for the named unit and phase.
- Compatibility envelope plus independent construction and transition choices.
- Current flows, consumers, data, operations, and evidence baselines.
- Access needed for the requested implementation and verification scope.

## Output contract

- Keep target architecture and legacy topology distinct.
- Select a viable seam and target-owned vertical slice.
- Define coexistence, observation, recovery, acceptance, and retirement before
  increasing target responsibility.
- Apply asset-level implementation and knowledge dispositions.
- Migrate bounded callers, traffic, or state only under action-local authority
  and with recorded evidence.
- Remove the replaced path and transition-only artifacts within authorized
  scope, or report their exact residual state and owner decision.
- Report only checks, migrations, and cutovers actually performed.
- Stop positively as `implemented_not_cut_over` or `cutover_ready` when a later
  transition action is outside current authority.

## Exclusions

This interface does not promise production routing, deployment, irreversible
data migration, external consumer changes, old-system deletion, or permanent
compatibility without explicit authority. It does not cover ordinary
evolution or refactoring under a `no_rebuild` decision. It does not own
target-native construction; it may own separately authorized staged transition
to the resulting line.

## Stability

This version is a draft and makes no compatibility promise. Target-owned seams,
end-to-end slices, bounded coexistence, independent evidence, action-local
authority, and legacy extinction are the current evaluation subjects. Exact
routing, rollout, and data mechanisms remain target-specific.
