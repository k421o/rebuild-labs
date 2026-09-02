---
name: rebuild-complete
description: Implement an explicitly authorized complete architectural rebuild of a codebase or project after a material direction change. Use when asked to rebuild from scratch, start over from project genesis or a stable historical point, replace the governing architecture, or execute an accepted complete-rebuild plan. Do not use for assessment-only requests, compilation, disaster recovery, routine refactoring, or staged in-place migration; use rebuild-plan or rebuild-incremental instead.
---

# Complete project rebuild

Build a target-native implementation line without making the current tree its
implicit skeleton. Preserve history and user work, mine the old system for
evidence, and admit assets only when they serve the current direction.

## Required planning source

Before implementation, read the sibling
[`rebuild-plan` skill](../rebuild-plan/SKILL.md) completely and read every file
in its [`references/`](../rebuild-plan/references/) directory. Use its target,
baseline, disposition, evidence, safety, and record behavior as the single
shared planning source.

If no accepted rebuild packet exists, perform that planning workflow first.
Do not treat your own plan as owner ratification when the direction, allowed
breaks, or destructive transition still require a decision.

## Authorization and isolation

- Confirm that the user requested implementation, not only diagnosis or a
  recommendation.
- Read the target's applicable instructions and inspect its Git and dirty state
  before editing.
- Preserve all unrelated changes. Work in an isolated worktree or equivalent
  unless the target already provides an authorized isolated environment.
- Create the new line at an exact empty or historical source baseline. Never
  reset, clean, delete, or move the active checkout to “rewind.”
- Keep deployment, public release, production cutover, irreversible data
  changes, consumer changes, and old-system deletion outside scope unless they
  are explicitly authorized.

## Workflow

1. **Materialize the target contract.** Record the direction brief, target
   responsibilities, state ownership, dependency direction, forbidden
   inheritances, required continuity, intentional divergences, first vertical,
   and acceptance gates before importing legacy implementation.
2. **Pin the source and quarry.** Record the source baseline used for the new
   line plus current, historical, release, and operational evidence baselines.
   Keep later code available read-only as a knowledge quarry.
3. **Establish target-native scaffolding.** Add only infrastructure necessary
   for the first end-to-end target behavior. Do not copy old folders, framework
   setup, abstractions, or tests merely to make the new tree familiar.
4. **Build the first vertical.** Implement the smallest meaningful target
   outcome across its real layers. Add target-fitness evidence before broad
   porting so the changed direction is executable early.
5. **Characterize selectively.** Observe old behavior that bears on required
   continuity or unresolved intent. Label each observation in the behavior
   matrix. Never promote a golden master or legacy suite wholesale into the
   target specification.
6. **Apply the re-entry gate.** For each code, test, schema, algorithm, fixture,
   configuration, or knowledge asset, select salvage, refactor, re-derive,
   quarantine, or discard and record knowledge separately. Import only
   accepted assets and their provenance.
7. **Advance by target verticals.** Implement subsequent slices in target
   dependency order. Integrate and commit at coherent checkpoints according to
   repository policy. Avoid a long-lived opaque rewrite branch.
8. **Verify independent properties.** Exercise target fit, required continuity,
   intentional divergence, architecture fitness, operations, consumers, and
   data. Add negative checks for rejected frameworks, dependencies, ownership
   paths, or schemas when they express durable target rules rather than
   incidental layout.
9. **Prepare transition.** Define exact revisions, consumer order, data
   movement, observation, stop signals, recovery scope, acceptance, legacy
   archive, and retirement. A complete target may still use incremental
   rollout.
10. **Cut over only when authorized.** Move bounded traffic or consumers,
    reconcile actual outcomes, and retire old ownership and temporary
    architecture only within explicit scope. Preserve immutable history and
    supersede old decisions instead of rewriting them.

## Completion behavior

Continue while a safe, in-scope target vertical or verification step remains.
Stop with a concrete residual limit when completion requires a new owner
decision, external coordination, production authority, secrets, unavailable
infrastructure, or a material scope expansion.

Do not call the rebuild complete merely because the new source compiles or its
unit tests pass. Report separately:

- implemented and verified target slices;
- admitted assets and knowledge dispositions;
- target, continuity, divergence, architecture, operational, consumer, and
  data checks actually run;
- transition and retirement state;
- temporary or legacy paths still live; and
- decisions or evidence still required.

## Guardrails

- Do not maximize rewritten code; maximize target alignment and verified
  transition.
- Do not preserve behavior solely because current tests assert it.
- Do not erase Git history to demonstrate a clean start.
- Do not import an entire legacy directory without asset-level justification.
- Do not let a compatibility adapter become the target's permanent domain
  model without an explicit decision.
- Do not describe an unexercised migration, rollback, or cutover as verified.
- Do not change instruction-policy files unless the relevant owner explicitly
  authorized that exact named-file change.
