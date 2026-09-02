# Rebuild decision model, version 1 draft

## Central object: the rebuild record

A rebuild record connects the owner's current direction to a safe,
evidence-backed transformation. It should contain:

- project scope, repository identity, current revision, and dirty-state note;
- target charter, deciding authority, status, date, and superseded decisions;
- direction gaps and the inherited assumptions involved;
- source, evidence, compatibility, and target baselines;
- mode per rebuild unit: complete, incremental, ordinary refactor, defer, or
  investigate;
- asset disposition ledger with evidence and confidence;
- required invariants and intentional divergences;
- ordered implementation slices and dependency direction;
- verification gates and evidence locations;
- coexistence, data movement, cutover, recovery, and retirement conditions;
- unresolved authority, safety, security, legal, or operational questions; and
- state transitions, owner acceptances, and superseding records.

The record belongs with the target system. Rebuild Labs supplies the model and
templates, not a central registry of projects.

## Step 1: freeze the target before inheriting the solution

Translate the direction change into an implementation-neutral target charter:

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

## Step 2: map the direction gap

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
between complete and incremental modes.

## Step 3: separate the baselines

Do not overload “the baseline.” Record four independently:

| Baseline | Question | Example evidence |
| --- | --- | --- |
| Source | Where should a new implementation line begin? | Empty tree or pinned historical commit |
| Evidence | What revisions explain current and past behavior? | HEAD, releases, prior stable commits, incidents |
| Compatibility | What observable contract must survive? | Versioned API, data identity, CLI behavior, consumer lock |
| Target | What future conditions determine success? | Ratified charter and acceptance matrix |

One commit can serve several roles, but the record must still name the role.
Starting a branch at an old stable point does not erase obligations introduced
later, and inspecting HEAD does not make its architecture the target.

## Step 4: classify assets, not eras

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

## Step 5: choose the smallest sufficient transformation

### Prefer an ordinary refactor when

- the target direction and fundamental boundaries remain valid;
- work is primarily local structure, naming, decomposition, or dependency
  cleanup;
- compatibility obligations dominate the change; and
- a new implementation line would reproduce most current architecture.

### Prefer a complete rebuild when

- several foundational assumptions conflict and seams would mainly preserve
  boundaries the target rejects;
- an old source point or empty tree offers a materially clearer dependency
  graph;
- the target can be proven through independent verticals before cutover;
- necessary data and consumer transitions can be staged outside the internal
  old architecture; and
- the team can keep the old implementation stable while the new line matures.

### Prefer an incremental rebuild when

- service continuity, data custody, or consumer migration forbids a single
  cutover;
- at least one reliable seam can route a bounded responsibility;
- valuable target-compatible components can remain in service;
- slices can reach independent acceptance and retirement conditions; and
- temporary coexistence can be made observable and time-bounded.

### Investigate or defer when

- owner direction is not ratified enough to define intentional divergence;
- repository or operational evidence is too weak to identify state and
  consumers;
- no safe isolated environment exists for the proposed work;
- security, legal, privacy, or data authority is unresolved; or
- neither mode has a credible first vertical and stopping condition.

Projects may use complete rebuilding inside one boundary and incremental
replacement at another. Record each rebuild unit and its mode rather than
calling the whole effort “hybrid.”

## Step 6: preserve contracts selectively

Characterization tests answer “what happens now?” Target acceptance answers
“what should happen next?” For each observed behavior, classify it as:

- required continuity;
- permitted continuity;
- intentional divergence;
- historical accident; or
- unresolved owner decision.

Only the first category is automatically a compatibility gate. Permitted
continuity may be kept when cheap and harmless. Intentional divergence should
receive a target test that rejects the old behavior where practical. Accidents
should not enter the new suite merely because they are easy to snapshot.

## Step 7: verify the transformation, not the rewrite percentage

Evidence should cover the risks the selected mode introduces:

| Concern | Useful evidence |
| --- | --- |
| Target fit | End-to-end acceptance against the charter |
| Preserved behavior | Contract, differential, or replay tests scoped to required continuity |
| Intentional divergence | Tests and decisions showing the new behavior is deliberate |
| Data continuity | Migration rehearsal, reconciliation, invariant checks, restore or forward-recovery exercise |
| External consumers | Compatibility exercise against pinned consumers or protocols |
| Coexistence | Route, shadow, dual-read/write, divergence, and ownership observations |
| Retirement | No traffic or ownership remains on the old path; rollback window and archive state are explicit |

Lines reused, lines rewritten, commit count, and green unit tests are not
sufficient measures of alignment.

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
8. Agent inference cannot supply missing owner authority for direction,
   cutover, deletion, or externally visible commitments.
