---
name: rebuild-plan
description: Determine whether rebuilding is warranted after a possible direction change, then plan construction and transition independently. Use when asked whether to start over, rewind to a stable point, choose a rebuild strategy, rearchitect around a new goal, classify legacy assets, prepare a pivot plan, or implement a rebuild whose strategy is undecided. This gateway is read-only during planning and may route explicitly authorized implementation to rebuild-complete or rebuild-incremental. Do not use for compilation, binary reconstruction, disaster recovery, or routine implementation with no rebuild decision.
---

# Rebuild planning

Determine whether the project has a genuine direction discontinuity, then
produce an evidence-backed plan that lets the target direction govern the new
architecture without erasing useful behavior or knowledge.

## Required domain sources

Before planning, read every file in this skill's
[`references/`](references/) directory. They are installed projections of the
canonical Rebuild Labs domain and carry the direction, architecture, baseline,
asset, evidence, safety, and rebuild-record behavior needed by all three
skills.

## Mutation boundary

Planning is read-only by default. Inspect files, history, manifests, tests,
releases, and safe operational evidence as authorized, but do not edit the
target, create branches or worktrees, install dependencies, change external
state, or begin the rebuild unless the user explicitly requests that action.

If the user asks to write the plan into the target repository, resolve the
authorized path and applicable instructions before editing. A request to
assess or advise does not imply that write authority.

When the user explicitly asks to implement and delegates strategy selection,
keep the planning phase read-only, select a strategy from evidence, then route
only the authorized unit and phase as described below. Do not use a planning
request itself as implementation authority.

## Workflow

1. **Pin the request and authority.** Record the target scope, repository and
   current revision when available, the latest owner direction, its decision
   state, applicable guidance, the authorized unit and phase if implementation
   was requested, and which actions remain outside scope. Separate an owner's
   current request from older code, ADRs, tests, branch names, and agent plans.
2. **Draft an intent-first direction contract.** Before deep implementation
   inspection, restate the desired outcomes, constraints, required continuity,
   allowed breaks, non-goals, acceptance conditions, and unresolved owner
   questions in implementation-neutral terms. Do not invent missing product
   intent merely to make a rebuild actionable.
3. **Run bounded triage.** To answer “should we start over?”, inspect only the
   direction, normative obligations, representative governing boundaries, and
   enough repository state to test for a foundational conflict. If the
   architecture already supports the changed direction, return ordinary
   evolution or another no-rebuild path. Do not inventory the entire system
   merely to earn permission to decide.
4. **Gate planning depth.** If direction or authority is insufficient, return
   `defer` or `investigate` with the blocking condition and leave strategies
   unselected. For `no_rebuild`, inspect only what the ordinary change and its
   verification require. Continue through the full rebuild packet only after
   bounded evidence supports the `rebuild` change class.
5. **Propose architecture separately.** For a rebuild candidate, record target
   responsibilities, state
   and trust ownership, dependency direction, forbidden inheritances, and
   competing alternatives as an authored hypothesis. An agent-authored
   architecture is not owner direction. Record acceptance and implementation
   authorization as separate states.
6. **Inventory factual state proportionately.** If triage warrants deeper
   investigation, inspect repository topology, Git status, worktrees, remotes,
   releases, consumers, interfaces, data, deployments,
   security boundaries, build and test surfaces, and relevant history. Pin
   evidence to revisions or dates. Record dirty and untracked work without
   exposing sensitive content.
7. **Map inherited assumptions.** Identify assumptions about product job,
   domain model, state ownership, trust, runtime, deployment, interfaces,
   extension model, and dependency direction. Classify each as aligned,
   isolatable, conflicting, obsolete, or unknown relative to the direction
   contract and architecture hypothesis.
8. **Separate baseline roles.** Name current and historical evidence baselines,
   required compatibility baselines, and the target acceptance baseline. For
   target-native construction, compare and select source-baseline candidates;
   for evolve-in-place construction, record the source baseline as not
   applicable rather than inventing a rewind. Never let one commit silently
   stand for several roles.
9. **Build the behavior matrix.** For material behavior, record evidence state
   (`observed`, `inferred`, `unknown`), target action (`preserve_required`,
   `preserve_optional`, `change`, `remove`, `unresolved`), origin
   interpretation (`intentional`, `accidental`, `unknown`), and authority
   state. Characterization describes the old system; it does not decide the
   target.
10. **Classify assets.** Apply the asset-level re-entry gate from
   [asset dispositions](references/asset-dispositions.md). Select salvage,
   refactor, re-derive, quarantine, or discard for implementation, and record
   knowledge retention independently.
11. **Choose transformation per unit.** First choose `proceed`, `defer`, or
    `investigate`. When proceeding, choose change class (`no_rebuild` or
    `rebuild`), construction (`evolve_in_place` or `target_native_line`), and
    transition (`direct` or `staged`) independently. Test the recommendation
    against seam quality, hidden consumers, data reversibility, operational
    risk, and a credible first vertical.
12. **Design execution and evidence.** For each rebuild unit, define the
    authorized unit and phase, phase success boundary, target-aligned vertical
    slices, dependency order, target-fitness tests, compatibility tests,
    intentional divergence checks, negative legacy-dependency checks, data and
    consumer movement, coexistence, action-local authority, recovery
    boundaries, legacy retirement, invalidation triggers, and stopping
    conditions. Require target-native verticals when construction is
    `target_native_line`.
13. **Challenge both biases.** Ask whether the plan carries the old
    architecture forward because it is familiar, and whether it proposes a
    clean-slate system that ignores real constraints or solves speculative
    problems. Revise only from evidence or an owner decision.

## Output contract

Always return a concise transformation assessment with:

- scope, repository state, authority, and evidence limits;
- direction contract and superseded assumptions;
- decision (`proceed`, `defer`, or `investigate`) and its evidence;
- decisions requiring owner input; and
- checks actually executed plus residual uncertainty.

For `no_rebuild`, add the named ordinary evolution, refactor, modernization, or
upgrade path; relevant construction and delivery choice; one target-aligned
change or vertical; and proportionate verification. Do not manufacture a
source-baseline comparison, system-wide asset ledger, coexistence plan, or
retirement program.

For `rebuild`, add:

- target architecture hypothesis or accepted contract, its author and state;
- direction-gap map;
- evidence, compatibility, and target baselines;
- for `target_native_line`, source-baseline alternatives and selection;
- behavior matrix with separate evidence, action, origin, and authority axes;
- initial asset disposition ledger;
- change class, construction, and transition per unit, including rejected
  alternatives;
- first target-aligned vertical and ordered follow-on slices, with target-native
  derivation when construction is `target_native_line`; and
- verification, coexistence, action-local authority, recovery, cutover, and
  retirement gates.

For `defer` or `investigate`, leave change class and strategies unselected and
state the bounded evidence, owner decision, or external condition required to
resume.

Use the rebuild-record template in this skill's references only when a durable
rebuild packet is warranted and requested. Keep observations, hypotheses, and
owner-ratified decisions visibly distinct.

## Decision standard

Recommend a rebuild only when the changed direction conflicts with material
inherited assumptions or when repeated accommodation would preserve boundaries
the target rejects. Code age, messiness, low coverage, a large backlog, a new
framework preference, or agent frustration are not sufficient.

Recommend ordinary evolution when direction changes but an existing extension
boundary remains fit. Recommend target-native construction only when that line
can be proven more directly. Recommend evolve-in-place construction or staged
transition only when a viable seam and retirement path exist. If no strategy
has a credible first vertical, report the missing evidence or authority
instead of producing false precision.

## Implementation routing

This skill is the mandatory gateway when implementation is requested but the
strategy is undecided:

- `no_rebuild`: report the ordinary evolution, refactor, modernization, or
  upgrade path; do not invoke a rebuild implementation skill;
- `rebuild + target_native_line`: route the authorized construction phase to
  `rebuild-complete`;
- `rebuild + evolve_in_place`: route construction to `rebuild-incremental`;
- `rebuild + staged`: route that transition phase to `rebuild-incremental`,
  including after target-native construction; and
- unresolved allowed breaks, scope, authority, or architecture acceptance
  required by the requested phase: stop for the named decision rather than
  choosing implicitly.

An explicitly authorized, bounded implementation may test an architecture
hypothesis as an experiment. Label it as evidence gathering, do not treat its
code as architecture acceptance, and do not transition consumers, traffic, or
state until the architecture and each action are accepted and authorized.

Continue into a sibling implementation workflow only when the user explicitly
requested implementation, delegated strategy choice, and supplied authority
for the selected unit and phase. Otherwise return the plan and stop.

## Reporting discipline

Do not claim a command, build, test, consumer check, or migration rehearsal was
run unless the current task's tool record contains that execution. State
unperformed checks as not run without inventing a reason. Do not quantify
“percent reusable” unless a recorded method and unit make the number meaningful;
prefer explicit asset decisions.
