# Rebuild decision model, version 1 draft

## Central object: the rebuild record

A rebuild record connects the owner's current direction to a safe,
evidence-backed transformation. It should contain:

- project scope, repository identity, current revision, and dirty-state note;
- direction contract, deciding authority, status, date, and superseded
  decisions;
- target architecture hypothesis or accepted contract, its author and decision
  state, and implementation authorization;
- direction gaps and the inherited assumptions involved;
- source, evidence, compatibility, and target baselines;
- transformation decision per unit: proceed, defer, or investigate;
- for a selected path, change class (`no_rebuild` or `rebuild`), construction
  strategy (`evolve_in_place` or `target_native_line`), and transition strategy
  (`direct` or `staged`);
- asset disposition ledger with evidence and confidence;
- required invariants and intentional divergences;
- ordered implementation slices and dependency direction;
- verification gates and evidence locations;
- coexistence, data movement, cutover, recovery, and retirement conditions;
- unresolved authority, safety, security, legal, or operational questions; and
- state transitions, owner acceptances, and superseding records.

The record belongs with the target system. Rebuild Labs supplies the model and
templates, not a central registry of projects.

## Step 1: freeze the direction before inheriting the solution

Translate the direction change into an implementation-neutral direction
contract:

- What user or operator outcome changes?
- Which prior constraints are removed, replaced, or newly introduced?
- Which interfaces, data, identities, or service levels must remain continuous?
- Which former behaviors may intentionally disappear?
- What is explicitly out of scope?
- Who may decide unresolved tradeoffs and accept the result?
- What evidence would demonstrate a useful target vertical?

If these questions cannot distinguish the new destination from the current
system, the next action is clarification or a bounded experiment—not a
codebase-wide rebuild.

## Step 2: propose target architecture without inventing owner direction

Derive a target architecture hypothesis from the direction contract and
normative external obligations. Record:

- responsibilities and bounded ownership;
- durable state, identities, trust, and permission boundaries;
- interfaces and dependency direction;
- target runtime and deployment units where the direction constrains them;
- forbidden dependencies or inheritances; and
- evidence that would discriminate this proposal from alternatives.

Name the author and decision state. Agent-authored responsibilities and
dependency direction are hypotheses, not part of the owner-ratified direction
merely because they appear in the same document. If the project accepts the
hypothesis, record a target architecture contract. Separately record which
unit and phase the current task is authorized to implement.

## Step 3: map the direction gap

Inspect the inherited system by assumption rather than by directory. For each
material target need, ask whether the current architecture:

- **aligns** — its boundary directly supports the target;
- **can be isolated** — a seam can contain the mismatch;
- **conflicts** — its boundary or dependency direction actively resists the
  target;
- **is obsolete** — the target removes the need it served; or
- **is unknown** — evidence is missing or contradictory.

Common foundational gaps include changes to product identity, primary user,
trust model, ownership boundary, core data model, state authority, deployment
unit, availability contract, runtime platform, extension model, or dependency
direction. A large diff without one of these gaps can still be an ordinary
refactor; a small diff that changes state ownership can be a rebuild.

Use the counterfactual:

> If the current implementation disappeared but its verified knowledge
> remained, would we intentionally recreate its major boundaries for the
> target?

A credible “no” is evidence for rebuilding. It is not by itself a decision
between construction and transition strategies.

## Step 4: separate the baselines

Do not overload “the baseline.” Record four independently:

| Baseline | Question | Example evidence |
| --- | --- | --- |
| Source | Where should a target-native line begin, if selected? | Empty tree, pinned historical commit, or not applicable |
| Evidence | What revisions explain current and past behavior? | HEAD, releases, prior stable commits, incidents |
| Compatibility | What observable contract must survive? | Versioned API, data identity, CLI behavior, consumer lock |
| Target | What future conditions determine success? | Direction contract, accepted target architecture, and acceptance matrix |

Record source as not applicable for `evolve_in_place` construction and
no-rebuild paths. One commit can serve several other roles, but the record must
still name each role.
Starting a branch at an old stable point does not erase obligations introduced
later, and inspecting HEAD does not make its architecture the target.

Materialize a source baseline without disturbing the line being studied:

- historical Git ref → a new branch in a separate worktree;
- empty tree → a fresh isolated directory or repository, or an orphan line
  only inside a separately prepared worktree with a recorded integration path;
  and
- non-Git project → an immutable evidence snapshot plus an isolated
  destination.

Never reset, clean, mass-delete, or orphan the active checkout to simulate a
rewind.

## Step 5: classify assets, not eras

Evaluate each coherent asset on these dimensions:

| Dimension | Question |
| --- | --- |
| Target fit | Does the responsibility or knowledge still belong? |
| Behavioral evidence | Is its behavior understood and verified, merely asserted, or unknown? |
| Coupling | How much superseded architecture must travel with it? |
| State and identity | Does it own durable data, identifiers, compatibility, or externally visible state? |
| Transfer cost | Is it safer and cheaper to carry, adapt, or re-derive? |
| Risk and authority | Are licensing, security, privacy, ownership, or owner decisions unresolved? |

Then select one disposition:

| Disposition | Use when | Required record |
| --- | --- | --- |
| Salvage | The asset already fits the target and can move without importing a conflicting boundary. | Provenance, compatibility, integration verification |
| Refactor | Its responsibility remains valuable but representation or coupling must change. | Preserved contract, intended changes, focused tests |
| Re-derive | The knowledge or observable contract matters more than the old implementation. | Source evidence, new target model, equivalence or intentional-divergence check |
| Quarantine | Value or safety is unresolved and it should not shape the target yet. | Question, owner, resolution condition, location |
| Discard | No accepted target need depends on it or retaining it would perpetuate a superseded assumption. | Rationale, affected behavior, history/reference retained |

Disposition applies to the named unit only. A test suite, database schema, or
library is rarely one indivisible asset.

## Step 6: choose the smallest sufficient transformation

First decide whether evidence and authority support proceeding. Otherwise defer
for a named external condition or investigate a bounded unknown. When
proceeding, decide whether foundational replacement is needed at all.

### Prefer no rebuild when

- a changed product outcome or external contract can be implemented through
  boundaries the current architecture already supports;
- the work is ordinary feature evolution, refactoring, modernization, or an
  upgrade without replacing governing ownership or dependency direction;
- target fitness can be demonstrated by a bounded change; and
- rebuild transition machinery would add risk without removing a conflicting
  assumption.

Use **ordinary evolution** when direction changes but architecture remains fit.
Use **ordinary refactor** when direction and external behavior remain stable
and internal structure changes. Name modernization or upgrade directly when
that is the actual job.

### Prefer an ordinary refactor when

- the target direction and fundamental boundaries remain valid;
- work is primarily local structure, naming, decomposition, or dependency
  cleanup;
- compatibility obligations dominate the change; and
- a new implementation line would reproduce most current architecture.

For a rebuild, select construction and transition independently:

| Architectural discontinuity | Continuity requirement | Construction | Transition |
| --- | --- | --- | --- |
| High | Low or manageable | Target-native line | Direct or staged according to cutover risk |
| High | High | Target-native line or bounded in-place slices | Staged |
| Moderate with a strong seam | High | Evolve in place | Staged |

This is a diagnostic, not an automatic score.

### Prefer target-native construction when

- several foundational assumptions conflict and seams would mainly preserve
  boundaries the target rejects;
- an old source point or empty tree offers a materially clearer dependency
  graph;
- the target can be proven through independent verticals before cutover;
- necessary data and consumer transitions can be staged outside the internal
  old architecture; and
- the team can keep the old implementation stable while the new line matures.

### Prefer evolve-in-place construction when

- at least one reliable seam can route a bounded responsibility;
- valuable target-compatible components can remain in service;
- slices can reach independent acceptance and retirement conditions; and
- temporary coexistence can be made observable and time-bounded.

### Prefer staged transition when

- service continuity, data custody, or consumer migration forbids a single
  cutover;
- different cohorts, routes, capabilities, or data partitions can move
  independently; and
- observation and recovery improve the decision enough to justify temporary
  coexistence.

For a rebuild, staged transition can follow either construction strategy. The
complete module owns a target-native line; the incremental module owns staged
transition and in-place slice construction. A single rebuild unit can therefore
use both modules in sequence without becoming conceptually ambiguous. A staged
rollout of ordinary no-rebuild work does not enter either rebuild module merely
because its delivery is staged.

### Investigate or defer when

- owner direction is not ratified enough to define intentional divergence;
- repository or operational evidence is too weak to identify state and
  consumers;
- no safe isolated environment exists for the proposed work;
- security, legal, privacy, or data authority is unresolved; or
- no strategy has a credible first vertical and stopping condition.

Record decision, change class, construction, and transition for each bounded
unit. A no-rebuild path ordinarily evolves in place; it may still use a normal
direct or staged product rollout without becoming an incremental rebuild. Do
not use “hybrid” as a substitute for these fields.

## Step 7: preserve contracts selectively

Characterization tests answer “what happens now?” Target acceptance answers
“what should happen next?” Use separate axes for each material behavior:

- **evidence state:** observed, inferred, or unknown;
- **target action:** preserve required, preserve optional, change, remove, or
  unresolved;
- **origin interpretation:** intentional, accidental, or unknown; and
- **authority state:** the source and decision state for the target action.

Only `preserve_required` is automatically a compatibility gate. Optional
continuity may remain when cheap and harmless. A `change` or `remove` action
should receive a target check that distinguishes it from old behavior where
practical. An accidental origin does not automatically imply removal, and an
unknown evidence state does not decide the target action.

## Step 8: verify the transformation, not the rewrite percentage

Evidence should cover the risks the selected strategies introduce:

| Concern | Useful evidence |
| --- | --- |
| Target fit | End-to-end acceptance against the direction and target architecture contracts |
| Preserved behavior | Contract, differential, or replay tests scoped to required continuity |
| Intentional divergence | Tests and decisions showing the new behavior is deliberate |
| Data continuity | Migration rehearsal, reconciliation, invariant checks, restore or forward-recovery exercise |
| External consumers | Compatibility exercise against pinned consumers or protocols |
| Coexistence | Route, shadow, dual-read/write, divergence, and ownership observations |
| Retirement | No traffic or ownership remains on the old path; rollback window and archive state are explicit |

Lines reused, lines rewritten, commit count, and green unit tests are not
sufficient measures of alignment.

## Step 9: bound execution and keep evidence current

Before each implementation invocation, pin:

- the authorized unit and phase;
- its positive success boundary;
- halt and recovery thresholds;
- which recovery actions are already authorized; and
- changes that invalidate evidence or require a construction or transition
  strategy decision again.

An implementation phase may finish as `implemented_not_cut_over`. A verified
transition preparation may finish as `cutover_ready`. Neither state is failure,
and neither supplies authority for the next action.

For a target-native line, inspect changes on the live evidence line at a
recorded cadence and again before transition. Security fixes, new external
obligations, data changes, and consumer changes can invalidate earlier
acceptance evidence. Admit those deltas selectively through the asset gate;
do not merge the old topology wholesale merely to become current. Record a
transition freeze window when one is required.

If an observation threshold fails during staged transition, stop expansion,
preserve the evidence, execute only an already authorized recovery action, and
return to the named decision owner. Do not infer permission for traffic or
consumer movement, external data mutation, stopping old writes, schema
contraction, or code or resource deletion from direction ratification,
architecture acceptance, or implementation authority.

## Invariants

1. Current direction outranks historical implementation for the destination,
   within the owner's authority and external obligations.
2. Existing code remains evidence even when its architecture is superseded.
3. Rewind creates new isolated state; it does not destroy the active checkout.
4. Every preserved behavior is tied to a current requirement, external
   contract, or explicit low-cost compatibility choice.
5. Every discarded asset has a stated unit and rationale; Git history is not
   erased to prove commitment.
6. Every incremental slice has a target route and legacy retirement condition.
7. A build, test, or migration can be implemented without being accepted; the
   record keeps those states separate.
8. Direction ratification, target-architecture acceptance, implementation,
   deployment, traffic or consumer movement, external data mutation, stopping
   old writes, schema contraction, and deletion are distinct grants.
9. Agent inference cannot supply missing owner authority for direction,
   cutover, deletion, or externally visible commitments.
