# Complete rebuild

## Purpose

Use a complete rebuild when the target direction rejects enough foundational
assumptions that evolving the current tree would make those assumptions more
expensive to remove. Build a new implementation line from an empty tree, the
beginning of the project, or a selected stable point. Keep later history
available as evidence and admit assets deliberately.

“Complete” applies to architectural derivation. It does not require throwing
away every asset, matching no prior behavior, hiding work on a long-lived
branch, or switching every consumer in one event.

## Entry conditions

Before selecting this mode, establish that:

- a current owner-ratified direction names the desired outcome and permitted
  breaks;
- several material inherited assumptions conflict with that direction, or the
  current skeleton would dominate the new one through adapters;
- a target-native vertical slice can be built and evaluated independently;
- current production or released behavior can remain supported while the new
  line develops, when support is required;
- data, consumer, security, licensing, and operational boundaries are known
  enough to avoid unsafe transfer; and
- the repository has a safe isolated worktree or equivalent environment.

If the real problem is local complexity under the same architecture, use an
ordinary refactor. If continued operation makes the target impossible to
validate independently, begin with the incremental module or use incremental
cutover around a complete target core.

## Phase 1: establish authority and preserve state

1. Read applicable project instructions and the explicit direction-change
   request.
2. Record the target scope, decision owner, current decision state, acceptance
   owner, and actions that still require separate approval.
3. Inventory the active branch, remotes, releases, worktrees, uncommitted and
   untracked files, submodules, generated assets, large files, credentials,
   databases, deployments, and other externally visible state.
4. Pin the current evidence revision and any relevant release or historical
   refs. Capture dirty state without exposing secrets when it bears on the
   rebuild.
5. Create a new branch or worktree at the chosen source baseline. Never move,
   reset, clean, or delete the active checkout to simulate a rewind.

This phase makes the old state recoverable and inspectable. It does not make
all of it a compatibility obligation.

## Phase 2: freeze the target model

Before detailed source mining, draft:

- the user and operator outcomes;
- core domain responsibilities and state ownership;
- required interfaces, identities, data invariants, service levels, and
  external obligations;
- intentional incompatibilities and removed jobs;
- target dependency direction and forbidden legacy dependencies;
- one smallest useful end-to-end target slice; and
- evidence that would make the owner accept that slice.

The target may be amended after implementation evidence reveals a real
constraint. Every amendment should name the evidence and decision instead of
quietly bending the new design around the old structure.

An optional anti-anchoring technique separates three passes:

1. A direction pass receives current intent and external constraints but not
   internal topology, and drafts the target contract.
2. An archaeology pass receives that frozen contract and mines repository
   behavior, history, consumers, and assets.
3. An integration pass challenges both legacy anchoring and impractical target
   assumptions, then records any accepted amendment.

This can be done by separate reviewers or by one agent with explicit context
boundaries. It is a hypothesis to evaluate, not a reason to conceal evidence
from final decision-makers.

## Phase 3: choose the source baseline

Compare at least the empty tree, project genesis, and each plausible stable
point. Prefer the baseline that minimizes accidental inheritance while
retaining genuinely useful setup, identity, and history.

For each candidate, record:

- full immutable revision or “empty tree”;
- known build and behavior state;
- architecture it would reintroduce by default;
- later obligations that still apply despite starting earlier;
- setup, migration, and verification cost; and
- why it is better or worse for the first target slice.

Do not choose an old commit because its tree is smaller, or HEAD because it is
newer. A stable point is relative to the reconstruction job.

## Phase 4: build the contract and asset quarry

Inspect current and historical code after the target draft is visible. Build a
behavior matrix with these states:

- preserve as required continuity;
- preserve if cheap and target-compatible;
- intentionally change;
- remove;
- unresolved owner decision; or
- unknown because evidence is insufficient.

Use characterization, snapshot, approval, contract, or replay tests to capture
observed behavior. Then label which observations are actual target or
compatibility requirements. Never accept a golden master wholesale as the new
specification.

Break the old system into small assets. Ask the re-entry questions for each:

1. Which target obligation does it serve?
2. Is that obligation current, intentionally changed, or merely inherited?
3. Does the asset obey target ownership and dependency direction?
4. Is its behavior understood strongly enough to transfer?
5. Is carrying or adapting it safer than re-deriving the responsibility?
6. Are provenance, license, security, privacy, secrets, and generated-source
   concerns resolved?
7. Which negative check will detect the rejected architecture returning with
   it?

Select salvage, refactor, re-derive, quarantine, or discard, and separately
state what knowledge survives.

## Phase 5: implement target-native verticals

1. Establish only the target-native skeleton needed for the first accepted
   vertical. Avoid copying the old directory structure for orientation.
2. Implement one end-to-end behavior from the target model using target
   boundaries and dependency direction.
3. Add target-fitness tests, not only compatibility tests. Verify that the new
   slice embodies the changed reason for rebuilding.
4. Transfer admitted assets one at a time or in coherent reviewed groups.
5. Record source revision, path, disposition, transformation, destination, and
   evidence for each transfer.
6. Add negative architecture checks for forbidden imports, frameworks,
   ownership paths, schemas, or dependency directions when deterministic
   checks can express them without freezing incidental layout.
7. Integrate frequently with the target line. A complete rebuild should not use
   a long-lived opaque branch as a substitute for controlled boundaries.

Repeat by vertical value rather than old-module order. Porting `utils/`, then
`models/`, then `services/` often reconstructs old layers before any target
behavior can be judged.

## Phase 6: verify compatibility and divergence

Use separate evidence streams:

| Stream | What it answers |
| --- | --- |
| Target acceptance | Does the new system achieve the changed goal? |
| Required continuity | Does it preserve specifically accepted prior contracts? |
| Intentional divergence | Does it avoid or reject behavior the target superseded? |
| Architecture fitness | Are target boundaries present and forbidden dependencies absent? |
| Operational readiness | Can it build, observe, migrate, recover, and run in the target environment? |
| Consumer and data migration | Can real identities, protocols, and state move safely? |

Differential or shadow execution can compare deterministic behavior without
routing user-visible writes to both systems. Investigate mismatches according
to the behavior matrix rather than assuming the old answer is correct.

## Phase 7: prepare transition

A complete target may still need incremental transition. Prepare:

- exact source and target revisions;
- consumer groups and route order;
- data snapshot, transformation, reconciliation, and ownership movement;
- observation thresholds and stop conditions;
- rollback or forward-recovery window and what it can actually restore;
- handling for writes during transition;
- security and permission changes;
- owner acceptance points; and
- legacy archive and retirement conditions.

Exercise the smallest realistic rehearsal available. A build and unit suite do
not prove cutover safety.

## Phase 8: cut over and retire

Only perform cutover or destructive retirement when that action is explicitly
authorized. Move bounded consumers or traffic, observe, reconcile, and stop on
named failure signals. Record the actual result, not only the planned command.

After acceptance:

- stop legacy writes and ownership before deletion;
- remove routes, bridges, flags, dual writes, and target constraints created
  solely for transition;
- retain immutable history and required audit evidence;
- update current documentation while superseding rather than rewriting old
  decisions; and
- record remaining legacy islands as explicit current decisions with owners
  and reevaluation conditions.

## Failure patterns

- **Clean-slate amnesia:** discarding code also discards contracts, data
  semantics, incidents, edge cases, and operational knowledge.
- **Old-tree scaffolding:** copying directories first causes the former
  architecture to define the new dependency graph.
- **Golden-master government:** every observed behavior becomes mandatory.
- **Framework migration disguised as direction:** new technology appears but
  responsibilities and ownership remain unchanged.
- **Big-bang equation:** complete architecture replacement is incorrectly tied
  to one irreversible launch.
- **Second-system expansion:** the target solves speculative future problems
  instead of the smallest changed job.
- **Branch archaeology:** an isolated branch becomes opaque, stale, and
  difficult to integrate.
- **History destruction:** branches or dirty work are reset because “we are
  starting over.”

## Exit conditions

The complete module exits when the target implementation is accepted for its
scope, required consumers and data have transitioned, legacy ownership is
retired or explicitly retained, temporary architecture is removed, and the
rebuild record points to verified evidence and residual limits. If only the
new code exists, implementation may be complete while the rebuild remains in
transition.
