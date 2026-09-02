# Incremental rebuild interface, version 1 draft

## Named user job

Given an explicitly authorized direction-change rebuild that must transition
in stages, replace one end-to-end responsibility at a time through a controlled
seam, verify the target path, transfer bounded consumers or state, and retire
the corresponding legacy path and temporary architecture.

## Inputs

- Target project and applicable owner guidance.
- Explicit implementation authority.
- Target direction, compatibility envelope, and mode decision.
- Current flows, consumers, data, operations, and evidence baselines.
- Access needed for the requested implementation and verification scope.

## Output contract

- Keep target architecture and legacy topology distinct.
- Select a viable seam and target-owned vertical slice.
- Define coexistence, observation, recovery, acceptance, and retirement before
  increasing target responsibility.
- Apply asset-level implementation and knowledge dispositions.
- Migrate bounded callers, traffic, or state with recorded evidence.
- Remove the replaced path and transition-only artifacts within authorized
  scope, or report their exact residual state and owner decision.
- Report only checks, migrations, and cutovers actually performed.

## Exclusions

This interface does not promise production routing, deployment, irreversible
data migration, external consumer changes, old-system deletion, or permanent
compatibility without explicit authority. It does not cover ordinary
refactoring under an unchanged direction or an isolated complete replacement.

## Compatibility

Version 1 freezes target-owned seams, end-to-end slices, bounded coexistence,
separate target and compatibility evidence, and legacy extinction as part of
completion. Exact routing, rollout, and data mechanisms remain target-specific.
