---
name: rebuild-plan
description: Plan a codebase or project rebuild after a material direction change. Use when asked whether to start over, rewind to an earlier stable point, choose complete versus incremental rebuilding, rearchitect around a new goal, decide what legacy code or knowledge to salvage, or prepare a pivot/rebuild plan. This is read-only by default. Do not use for compiling software, disaster recovery, routine refactoring, or implementation of an already accepted rebuild; use rebuild-complete or rebuild-incremental for implementation.
---

# Rebuild planning

Determine whether the project has a genuine direction discontinuity, then
produce an evidence-backed plan that lets the target direction govern the new
architecture without erasing useful behavior or knowledge.

## Required domain sources

Before planning, read every file in this skill's
[`references/`](references/) directory. They are the shared source for target
direction, baselines, asset disposition, evidence, safety, and rebuild-record
behavior used by the sibling implementation skills.

## Mutation boundary

Planning is read-only by default. Inspect files, history, manifests, tests,
releases, and safe operational evidence as authorized, but do not edit the
target, create branches or worktrees, install dependencies, change external
state, or begin the rebuild unless the user explicitly requests that action.

If the user asks to write the plan into the target repository, resolve the
authorized path and applicable instructions before editing. A request to
assess or advise does not imply that write authority.

## Workflow

1. **Pin the request and authority.** Record the target scope, repository and
   current revision when available, the latest owner direction, its decision
   state, applicable guidance, and which actions remain outside scope. Separate
   an owner's current request from older code, ADRs, tests, branch names, and
   agent-authored plans.
2. **Draft an intent-first direction brief.** Before deep implementation
   inspection, restate the desired outcomes, constraints, required continuity,
   allowed breaks, non-goals, acceptance conditions, and unresolved owner
   questions in implementation-neutral terms. Do not invent missing product
   intent merely to make a rebuild actionable.
3. **Inventory factual state.** Inspect repository topology, Git status,
   worktrees, remotes, releases, consumers, interfaces, data, deployments,
   security boundaries, build and test surfaces, and relevant history. Pin
   evidence to revisions or dates. Record dirty and untracked work without
   exposing sensitive content.
4. **Map inherited assumptions.** Identify assumptions about product job,
   domain model, state ownership, trust, runtime, deployment, interfaces,
   extension model, and dependency direction. Classify each as aligned,
   isolatable, conflicting, obsolete, or unknown relative to the direction
   brief.
5. **Separate four baselines.** Name source-baseline candidates, current and
   historical evidence baselines, required compatibility baselines, and the
   target acceptance baseline. Never treat one commit as all four without
   explaining each role.
6. **Build the behavior matrix.** For material behavior, distinguish observed
   behavior from required continuity, permitted continuity, intentional
   divergence, historical accident, and unresolved intent. Characterization
   tests describe the old system; they do not decide the target.
7. **Classify assets.** Apply the asset-level re-entry gate from
   [asset dispositions](references/asset-dispositions.md). Select salvage,
   refactor, re-derive, quarantine, or discard for implementation, and record
   knowledge retention independently.
8. **Choose transformation per unit.** Recommend ordinary refactor, complete
   rebuild, incremental rebuild, a named combination, defer, or further
   investigation. Consider architectural discontinuity and continuity needs,
   then test the recommendation against seam quality, hidden consumers, data
   reversibility, operational risk, and a credible first vertical.
9. **Design execution and evidence.** Define target-native vertical slices,
   dependency order, target-fitness tests, compatibility tests, intentional
   divergence checks, negative legacy-dependency checks, data and consumer
   movement, coexistence, recovery boundaries, cutover authority, legacy
   retirement, and stopping conditions.
10. **Challenge both biases.** Ask whether the plan carries the old
    architecture forward because it is familiar, and whether it proposes a
    clean-slate system that ignores real constraints or solves speculative
    problems. Revise only from evidence or an owner decision.

## Output contract

Return a concise rebuild packet with:

- scope, repository state, authority, and evidence limits;
- direction brief and superseded assumptions;
- direction-gap map;
- four baselines and source-baseline alternatives;
- behavior matrix and compatibility envelope;
- initial asset disposition ledger;
- mode recommendation per rebuild unit, including rejected alternatives;
- first target-native vertical and ordered follow-on slices;
- verification, coexistence, cutover, recovery, and retirement gates;
- decisions requiring owner input; and
- checks actually executed plus residual uncertainty.

Use the templates in this skill's references when a durable packet is
requested. Keep observations, hypotheses, and owner-ratified decisions visibly
distinct.

## Decision standard

Recommend a rebuild only when the changed direction conflicts with material
inherited assumptions or when repeated accommodation would preserve boundaries
the target rejects. Code age, messiness, low coverage, a large backlog, a new
framework preference, or agent frustration are not sufficient.

Recommend complete rebuilding only when a target-native line can be proven
more directly and continuity can be managed. Recommend incremental rebuilding
only when a viable seam and retirement path exist. If neither has a credible
first vertical, report the missing evidence or authority instead of producing
false precision.

## Reporting discipline

Do not claim a command, build, test, consumer check, or migration rehearsal was
run unless the current task's tool record contains that execution. State
unperformed checks as not run without inventing a reason. Do not quantify
“percent reusable” unless a recorded method and unit make the number meaningful;
prefer explicit asset decisions.
