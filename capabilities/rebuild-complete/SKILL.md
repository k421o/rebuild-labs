---
name: rebuild-complete
description: Implement an explicitly authorized target-native construction phase after a material direction change. Use when asked to rebuild from scratch, begin from project genesis or a stable historical point, replace the governing architecture on an isolated line, or execute the complete-construction portion of an accepted plan; staged transition may follow through rebuild-incremental. Do not use for assessment-only requests, compilation, disaster recovery, routine evolution, or undecided strategy; use rebuild-plan first.
---

# Complete project rebuild

Build a target-native implementation line without making the current tree its
implicit skeleton. Preserve history and user work, mine the old system for
evidence, and admit assets only when they serve the current direction.

## Required planning source

Before implementation, read the sibling
[`rebuild-plan` skill](../rebuild-plan/SKILL.md) completely and read every file
in its [`references/`](../rebuild-plan/references/) directory. Use its
direction, architecture, baseline, disposition, evidence, safety, and record
behavior as the installed planning contract.

If no accepted rebuild packet exists, or construction and transition have not
been selected independently, perform the gateway workflow first. Do not treat
your own plan as owner ratification or architecture acceptance when the
direction, allowed breaks, or technical contract still require a decision.

## Authorization and isolation

- Confirm that the user requested implementation, not only diagnosis or a
  recommendation.
- Pin the authorized unit and phase, phase success boundary, halt or recovery
  threshold, and conditions that invalidate the plan or require a strategy
  switch. Permission for one vertical does not authorize all planned slices.
- If the target architecture remains a hypothesis, confirm that authorization
  explicitly covers a bounded evidence-gathering implementation. Keep it
  experimental and do not transition consumers, traffic, writes, or ownership
  until the architecture and each action are accepted and authorized.
- Read the target's applicable instructions and inspect its Git and dirty state
  before editing.
- Preserve all unrelated changes. Work in an isolated worktree or equivalent
  unless the target already provides an authorized isolated environment.
- Materialize the source baseline without changing the active checkout:

  - historical Git ref: a new branch in a separate worktree;
  - empty tree: a fresh isolated directory or repository, or an orphan line
    created only inside a separately prepared worktree, with a recorded
    integration strategy; or
  - non-Git source: an immutable evidence snapshot and isolated destination.

  Never reset, clean, mass-delete, move, or orphan the active checkout to
  “rewind.”
- Keep deployment, public release, production cutover, irreversible data
  changes, consumer changes, and old-system deletion outside scope unless they
  are explicitly authorized.

## Workflow

1. **Materialize distinct contracts.** Record the owner-ratified direction
   contract. Separately record the target architecture hypothesis or accepted
   contract, its author and state, plus implementation authorization for this
   unit and phase before importing legacy implementation.
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
   continuity or unresolved intent. Record separate evidence state, target
   action, origin interpretation, and authority state. Never promote a golden
   master or legacy suite wholesale into the target specification.
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
9. **Intake live-line deltas.** At a recorded cadence and before transition,
   inspect critical fixes, security changes, new obligations, data changes,
   and consumer changes since source selection. Selectively admit them through
   the same re-entry gate and invalidate affected evidence. Do not merge the
   live architecture wholesale merely to become current.
10. **Prepare transition.** Define exact revisions, consumer order, data
    movement, observation, stop signals, recovery scope, acceptance, legacy
    archive, retirement, and action-local authority. A complete target may
    still use incremental rollout.
11. **Transition only when authorized.** Immediately before deployment,
    traffic or consumer movement, external data writes or reconciliation,
    stopping old writes, schema contraction, or code or resource deletion,
    check authority for that exact action and unit. If absent, stop as
    `implemented_not_cut_over` or `cutover_ready`. If a threshold fails, stop
    expansion, preserve evidence, and perform only authorized recovery.

## Completion behavior

Continue only within the pinned unit, phase, and success boundary. Stop with a
concrete state and residual limit when that phase succeeds or when continuation
requires a new owner decision, external coordination, production authority,
secrets, unavailable infrastructure, recovery, strategy change, or material
scope expansion.

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
- Do not infer architecture acceptance from direction ratification or infer
  cutover, data, contraction, or deletion authority from implementation access.
- Do not change instruction-policy files unless the relevant owner explicitly
  authorized that exact named-file change.
