# Direction-change codebase rebuilding, initial synthesis

Status: **exploratory synthesis**

As of: **2026-09-02**

## Question

How can a project replace architecture that no longer fits its direction
without either fighting the old design indefinitely or losing the behavior,
data, and knowledge that still matter?

## Method

The bootstrap review selected primary pattern descriptions, official platform
documentation, and first-party engineering accounts covering deliberate
replacement, incremental displacement, large refactors, behavioral comparison,
online data migration, architecture decisions, Git isolation, and agent context.
The [source companion](codebase-rebuilding-v1-sources.md) records claim scope
and limitations. Four first-party examples are interpreted separately under
[`case-studies/`](case-studies/).

This is a qualitative synthesis. The sources were not sampled to estimate how
often a method succeeds, and successful organizations publish selectively.

## Findings

### 1. Changed assumptions, not bad code, justify rebuilding

Sacrificial Architecture argues that software can deliver genuine value and
still become the wrong architecture as scale and needs change. Patterns of
Legacy Displacement likewise treats outcomes and business process as the
starting point, warning that technology-only replacement and full feature
parity can reproduce obsolete constraints.

Operational implication: require a direction contract and assumption-gap map. A
new language, untidy code, low coverage, or unfamiliar design is not itself a
direction discontinuity. Conversely, code can be well engineered for its prior
job and still be wrong for the new one.

### 2. Construction strategy and transition strategy are independent

React Fiber completely rewrote React internals while developing old and new
renderers side by side and rolling the new path out gradually. GitHub built a
bespoke code-search engine after off-the-shelf systems failed explicit domain
and scale constraints, then exposed it through preview and beta stages. These
cases combine target-native construction with incremental validation and
adoption.

Operational implication: “complete rebuild” should describe how target
architecture is derived. It should not force one big-bang cutover. A common
high-discontinuity, high-continuity plan is complete target core plus
incremental consumer and data transition.

### 3. Incremental replacement needs an extinction path

Strangler Fig, Branch by Abstraction, Parallel Change, and Transitional
Architecture all rely on temporary coexistence: routers, abstractions,
expanded contracts, adapters, flags, or replicated state let old and new paths
operate while responsibility moves. Each pattern also includes removing the
old implementation or contracting the expanded interface.

Patterns of Legacy Displacement describes repeated modernization programs that
added new layers without decommissioning old systems. The code changed while
the intended cost and risk outcomes remained unmet.

Operational implication: define retirement before creating a bridge. Every
slice should transfer a bounded route or ownership and delete or deliberately
retain the corresponding old path. “Temporary” architecture needs an owner,
observation, removal condition, and reevaluation point.

### 4. Current behavior is evidence, not the target specification

Characterization, snapshot, and differential tests can make unknown
behavior visible. React reused public-API tests while rewriting tests that
depended on old internals. Scientist makes control/candidate comparison
observable and customizable. Yet legacy-displacement accounts warn that exact
feature parity can consume years reproducing behavior no longer wanted.

Operational implication: after encountering a behavior, record whether its
evidence is observed, inferred, or unknown; independently decide whether the
target must preserve it, may preserve it, changes it, removes it, or still
needs a decision; and separately interpret whether its origin was intentional,
accidental, or unknown. Only current authority or an external obligation can
select the target action. A golden master can detect change; it cannot decide
whether the change is wrong.

### 5. Preserve knowledge separately from implementation

The engineering cases reuse lessons, constraints, public contracts, tests,
algorithms, and operational evidence even when they replace core code. The
Research, Review, Rebuild account explicitly separates reverse engineering
from domain review, then chooses what to retain, redesign, defer, or discard.

Operational implication: every asset receives both an implementation
disposition and a knowledge disposition. This makes it possible to discard
framework glue while preserving a domain invariant, incident lesson, edge-case
test, or algorithmic insight.

### 6. State movement needs a different safety model from code movement

Stripe's online subscription migration used staged dual writes, backfill, read
movement, write movement, reconciliation, and old-data removal while the
service remained available. Scientist illustrates shadow comparison where the
control result remains authoritative. Both make mismatches observable, but
duplicating writes adds partial-failure and reconciliation risk that read-only
comparison avoids.

Operational implication: record canonical ownership, identity, concurrent
writes, restartability, reconciliation, and the real recovery window for every
data phase. Do not infer that switching binaries reverses writes already made
under the new model.

### 7. Decisions must survive agent and project context turnover

Architecture Decision Records preserve context, decision, status, and
consequences. Later accepted records can supersede earlier decisions while
retaining their historical content. Context Anchoring
describes a living decision document that carries rejected options,
constraints, open questions, and implementation state between independent
agent sessions.

Operational implication: pair accepted, historically retained decision records
with one living rebuild status. Explicit states let agents distinguish old
implementation from current direction. A stale ADR remains valuable history
without governing the target after a named superseding decision.

### 8. Isolation should preserve history, not destroy it

Git worktrees provide a separate working directory at another ref without
moving the primary checkout, but share repository object storage and are not an
independent backup. Annotated tags can name exact objects with metadata, while
bundles can transport selected refs and reachable committed history. Tag names
can move. Bundles do not include index or working-tree changes, the stash,
hooks, or per-repository configuration, and Git does not archive deployments or
external stores. Conversely, a bundle does include any secrets committed in
its reachable history and therefore requires appropriate custody.

Operational implication: define rewind as creating isolated state at an exact
ref. Inventory dirty and external state separately. Never make a destructive
reset the default implementation of “start over.”

## Proposed domain rules

The evidence supports these initial hypotheses for evaluation:

1. Freeze an implementation-neutral direction contract before deep source
   mining when the owner request permits it.
2. Record target architecture as a separately authored hypothesis or accepted
   contract; do not encode agent design inside owner direction.
3. Permit a no-rebuild result when the changed direction is already supported
   by the current architecture.
4. Separate source, evidence, compatibility, and target baselines.
5. Decide implementation and knowledge disposition per asset rather than per
   directory or era.
6. Require a target-native vertical before broad porting in complete rebuilds.
7. Require a route and legacy extinction condition for each incremental slice.
8. Verify target fitness, required continuity, intentional divergence, and
   forbidden legacy absence independently.
9. Treat full code replacement and incremental rollout as compatible choices.
10. Preserve old decisions with supersession links and one current status
   record.

These are proposed Rebuild Labs rules, not direct statements from any single
source. Controlled code cases and real rebuilds must test their utility and
false-positive behavior.

## Evaluation agenda

- Compare target-first and code-first agent planning on a repository whose
  current folders strongly imply a rejected architecture.
- Test whether an asset re-entry gate preserves a valuable algorithm while
  preventing framework coupling from crossing.
- Test whether characterization suites cause agents to reproduce intentionally
  removed behavior.
- Test complete target construction with incremental traffic transition.
- Test data migration plans for ownership, partial writes, reconciliation, and
  honest recovery limits.
- Test whether retirement gates reduce leftover flags, adapters, and old
  dependencies.
- Include controls where ordinary refactoring is the correct answer so the
  domain does not reward rewrites indiscriminately.
- Include changed-direction controls where an existing architecture supports
  ordinary evolution without a rebuild.
- Test that code-only authorization stops at `implemented_not_cut_over` or
  `cutover_ready` rather than moving traffic or deleting old state.

## Limitations

- First-party retrospectives may omit failed approaches, organizational cost,
  or conditions that do not generalize.
- Several sources address legacy modernization rather than a changed product
  direction exactly; the synthesis infers their relevance.
- The initial cases are large, well-resourced projects. Small prototypes and
  solo projects may have different continuity and coordination costs.
- No controlled Rebuild Labs agent run yet demonstrates that the proposed
  protocol produces better code or decisions.
- Security, regulated data, hardware, embedded systems, real-time constraints,
  and multi-repository governance need dedicated cases.
