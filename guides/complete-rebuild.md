# Complete rebuild

## Purpose

Use complete-rebuild construction when the target direction rejects enough
foundational assumptions that evolving the current tree would make those
assumptions more expensive to remove. Build a target-native implementation
line from an empty tree, the beginning of the project, or a selected stable
point. Keep later history available as evidence and admit assets deliberately.

“Complete” applies to architectural derivation. It does not require throwing
away every asset, matching no prior behavior, hiding work on a long-lived
branch, or switching every consumer in one event.

## Entry conditions

Before selecting this construction strategy, establish that:

- a current owner-ratified direction contract names the desired outcome,
  constraints, continuity, and permitted breaks;
- the target architecture is an explicitly authored hypothesis or an accepted
  contract rather than an unnamed extension of owner intent;
- the implementation unit and current phase are authorized;
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
2. Record the target scope, direction owner and state, architecture author and
   state, acceptance owner, authorized implementation unit and phase, and
   actions that require separate authority.
3. Inventory the active branch, remotes, releases, worktrees, uncommitted and
   untracked files, submodules, generated assets, large files, credentials,
   databases, deployments, and other externally visible state.
4. Pin the current evidence revision and any relevant release or historical
   refs. Capture dirty state without exposing secrets when it bears on the
   rebuild.
5. Materialize the chosen source baseline safely:

   - for a historical Git ref, create a new branch in a separate worktree;
   - for an empty tree, use a fresh isolated directory or repository, or create
     an orphan line only inside a separately prepared worktree, and record how
     it will integrate with the source repository; and
   - for a non-Git project, create an immutable evidence snapshot and a
     separate destination.

   Never move, reset, clean, mass-delete, or orphan the active checkout to
   simulate a rewind.

This phase makes the old state recoverable and inspectable. It does not make
all of it a compatibility obligation.

## Phase 2: freeze direction and propose the target model

Before detailed source mining, keep two records distinct.

The direction contract contains:

- the user and operator outcomes;
- required interfaces, identities, data invariants, service levels, and
  external obligations;
- intentional incompatibilities and removed jobs;
- non-goals and acceptance conditions; and
- the owner and decision state.

The target architecture hypothesis contains:

- core domain responsibilities and state ownership;
- target dependency direction and forbidden legacy dependencies;
- one smallest useful end-to-end target slice;
- alternatives and evidence that discriminate among them; and
- its author and acceptance state.

The architecture may be revised after implementation evidence reveals a real
constraint. The direction changes only through its own authority. Every
amendment should name the evidence and decision instead of quietly bending the
new design around the old structure.

An optional anti-anchoring technique separates four passes:

1. A direction pass receives current intent and external constraints but not
   internal topology, and drafts the direction contract.
2. An architecture pass proposes target responsibilities and boundaries from
   the direction without claiming owner authority.
3. An archaeology pass receives those frozen artifacts and mines repository
   behavior, history, consumers, and assets.
4. An integration pass challenges both legacy anchoring and impractical target
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

Inspect current and historical code after the target draft is visible. Use
characterization, snapshot, contract, or replay tests to capture observed
behavior. For each material behavior, record `evidence_state` as `observed`,
`inferred`, or `unknown`; `target_action` as `preserve_required`,
`preserve_optional`, `change`, `remove`, or `unresolved`; and
`origin_interpretation` as `intentional`, `accidental`, or `unknown`. Record the
authority for the target action. Evidence and origin do not decide which
behaviors become target or compatibility requirements. Never accept a golden
master wholesale as the new specification.

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

At the start of each invocation, pin the currently authorized unit and phase,
its success boundary, stop or recovery threshold, and conditions that
invalidate the plan or require a different strategy. Finishing that boundary
is a valid stopping point; it is not permission to implement every later
vertical in the plan.

## Phase 6: intake live-line deltas

The evidence line may continue changing while the target line matures. At a
recorded cadence and again before transition:

1. Inspect critical fixes, security changes, new external obligations, data
   changes, and consumer changes since source selection.
2. Decide asset by asset whether to salvage, refactor, re-derive, quarantine,
   discard, or amend the direction or architecture through its authority.
3. Invalidate affected acceptance evidence and rerun it after selective
   intake.
4. Never merge the live line wholesale merely to become current; that can
   reintroduce the architecture being replaced.
5. Declare a bounded freeze window when transition risk requires one, with an
   owner for emergency exceptions.

## Phase 7: verify compatibility and divergence

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

## Phase 8: prepare transition

A complete target may still need incremental transition. Prepare:

- exact source and target revisions;
- consumer groups and route order;
- data snapshot, transformation, reconciliation, and ownership movement;
- observation thresholds and stop conditions;
- rollback or forward-recovery window and what it can actually restore;
- handling for writes during transition;
- security and permission changes;
- owner acceptance points and action-local authority for deployment, traffic
  or consumer movement, external data writes and reconciliation, stopping old
  writes, schema contraction, and deletion; and
- legacy archive and retirement conditions.

Exercise the smallest realistic rehearsal available. A build and unit suite do
not prove cutover safety.

## Phase 9: cut over and retire

Only perform each external or destructive action when that action is explicitly
authorized. Acceptance of the target is not cutover authority. Before moving
traffic or consumers, writing or reconciling external data, stopping old
writes, contracting a schema, or deleting code or resources, check the grant
for that exact unit and phase. Record the actual result, not only the planned
command.

When a stop threshold fires, stop expansion, preserve evidence, and execute
only the pre-authorized recovery action. Mark affected evidence or the plan
invalidated and return to the deciding authority; do not continue rollout
because the target implementation itself passed tests.

After corresponding acceptance and action-local authorization:

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

The complete module exits at the boundary of the authorized phase. Valid states
include `implemented_not_cut_over`, verified construction, and
`cutover_ready`. Full rebuild completion additionally requires that accepted
consumers and data have transitioned, legacy ownership is retired or
explicitly retained, temporary architecture is removed, and the rebuild record
points to verified evidence and residual limits. If staged transition remains,
hand that phase to the incremental module without relabeling the target-native
construction.
