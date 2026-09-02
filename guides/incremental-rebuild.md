# Incremental rebuild

## Purpose

Use an incremental rebuild when the target direction changes foundational
architecture but service continuity, data custody, consumer migration, or
valuable stable boundaries make in-place staged replacement safer than a
single new implementation line and cutover.

Incremental rebuilding is not endless refactoring. Each slice is governed by a
target architecture, receives traffic or ownership deliberately, and has an
explicit condition for extinguishing the legacy path it replaces.

## Entry conditions

Establish that:

- a current target charter identifies the changed direction and required
  continuity;
- one or more inherited boundaries conflict with it materially;
- a seam can route a bounded responsibility, consumer, request class, data
  access, or workflow;
- old and target behavior can coexist under explicit temporary rules;
- the first slice has target acceptance and legacy retirement conditions; and
- temporary routing, compatibility, data duplication, and observation have
  owners and a bounded lifetime.

If there is no material direction discontinuity, use ordinary refactoring. If
every useful seam preserves the rejected architecture and continuity is
manageable elsewhere, build a complete target core and transition to it.

## Phase 1: establish target and topology

1. Record owner direction, required continuity, intentional divergences,
   non-goals, and acceptance authority.
2. Pin current, release, historical, and consumer evidence revisions.
3. Inventory dirty work, deployments, data stores, queues, identities,
   protocols, clients, scheduled jobs, operators, and failure recovery.
4. Draw current flows and state ownership using observed behavior rather than
   class or directory names.
5. Draw the target responsibilities, state ownership, dependency direction,
   and forbidden legacy dependencies independently.
6. Map the gaps and identify where a routing or ownership seam can contain
   them.

The target architecture must be visible before the migration map. Otherwise
the sequence can optimize movement without ever approaching the new direction.

## Phase 2: choose a seam

A useful seam has:

- a bounded input and observable output;
- a named caller, router, owner, or data-access boundary;
- enough isolation to select old or target behavior;
- a way to measure correctness and operational health;
- a recovery or stop path proportionate to its risk; and
- a credible removal path for transitional code.

Common seams include request routing, service façades, repositories or data
access, command handlers, events, file formats, feature switches, protocol
versions, page routes, or consumer-specific adapters.

Reject a seam when it merely wraps the old architecture and makes the target
depend on it permanently. An anti-corruption boundary translates temporary
legacy concepts into target concepts; it should not let legacy ownership leak
through disguised names.

## Phase 3: define a vertical slice

Choose the smallest slice that can demonstrate a meaningful target behavior
and retire something real. Record:

- target outcome and responsible boundary;
- consumers or traffic included and excluded;
- state read, written, migrated, or synchronized;
- accepted prior behavior and intentional changes;
- target acceptance evidence;
- coexistence and observation method;
- rollback or forward-recovery limit;
- temporary artifacts introduced; and
- the exact retirement condition for old code, routes, data, flags, and
  bridges.

Prefer slices by outcome, caller cohort, request type, or data partition over
horizontal layers that cannot be exercised end to end.

## Phase 4: introduce target-owned abstraction

When branch by abstraction or parallel change fits:

1. Define the target-facing contract at the seam.
2. Route existing behavior through it without changing observable results.
3. Prove the preparatory move separately.
4. Implement the target supplier or representation behind the contract.
5. Move bounded consumers or data to the target path.
6. Remove the legacy supplier and then any abstraction needed only for
   transition.

The target side owns the enduring vocabulary. Legacy adapters translate at the
edge. Avoid designing a “neutral” contract that is actually a union of every
old and new concept.

For APIs and schemas, use expand → migrate → contract:

- **Expand:** add the new representation while old consumers still work.
- **Migrate:** move consumers and data, measuring and reconciling behavior.
- **Contract:** remove the deprecated representation after retirement gates
  pass.

Contract is part of the rebuild, not optional cleanup.

## Phase 5: handle data and writes explicitly

Data migration can dominate incremental risk. Record:

- canonical owner of each datum in every phase;
- transformation and identity rules;
- backfill order and restartability;
- handling of writes during backfill;
- reconciliation query or invariant;
- tolerated divergence and escalation threshold;
- rollback scope after new writes occur; and
- when old schema or storage can stop accepting reads and writes.

Prefer shadow reads and result comparison when side effects can be suppressed.
Dual writes require idempotency, failure handling, reconciliation, and a plan
for partial success; they are not automatically safe because both calls
returned once.

Never describe a database backup, Git ref, exception handler, or reverse
migration as “rollback” without stating which actors, resources, writes, and
time window it can actually restore.

## Phase 6: run bounded coexistence

Possible techniques include:

- feature switches for a named cohort;
- shadow execution with side effects disabled;
- old/new response comparison after normalizing nondeterminism;
- canary traffic or consumer-by-consumer routing;
- dual reads with target preference and explicit fallback;
- dual writes with reconciliation when unavoidable; and
- target-only execution for newly created entities.

For each technique, state privacy, security, cost, latency, write, and failure
implications. Capture divergences as evidence and classify them against the
behavior matrix; do not automatically change the target to match legacy.

Temporary architecture needs an owner, creation reason, observability, removal
condition, and deadline or reevaluation trigger.

## Phase 7: verify and move the route

Before increasing traffic or ownership, verify:

- the slice meets target acceptance;
- specifically required compatibility holds;
- intentional differences are accepted and visible;
- target code does not depend on forbidden legacy internals;
- data invariants and reconciliation meet thresholds;
- failure and recovery behavior matches the stated scope;
- operational telemetry distinguishes old and target paths; and
- the stop or reversal procedure has been exercised in proportion to risk.

Move one bounded cohort, observe for the declared window, and record actual
evidence. “No alerts” is useful only when relevant alerts and traffic were
confirmed.

## Phase 8: extinguish the old slice

Once the retirement condition is accepted:

1. Stop routing new work to the old path.
2. End legacy writes and ownership.
3. Remove fallback after its accepted window.
4. Remove adapters, flags, dual operations, deprecated interfaces, schemas,
   code, tests, and monitoring that exist only for coexistence.
5. Retain history and required audit evidence without leaving a second live
   implementation.
6. Add or update negative checks that prevent the forbidden dependency or old
   route from returning.
7. Record the retired state and next slice.

If a legacy island remains for a valid reason, give it a current owner,
contract, and reevaluation condition. Do not call it temporary indefinitely.

## Progress measures

Useful measures are monotonic and target-related:

- target behaviors accepted;
- consumers, routes, or entities moved;
- legacy traffic and state ownership reduced;
- forbidden dependencies removed;
- temporary bridges remaining and their age;
- reconciliation error rate and unresolved divergences; and
- old code or schema surface whose retirement gates are satisfied.

Lines changed, percent rewritten, adapter count, and a green combined suite can
hide a migration that never transfers ownership.

## Failure patterns

- **Permanent strangler:** routing exists, but nothing is ever retired.
- **Feature parity trap:** obsolete behavior is recreated before any new
  outcome can ship.
- **Legacy-owned contract:** the target API preserves the old model as its
  permanent vocabulary.
- **Horizontal migration:** layers move while no user-visible path is complete.
- **Unowned dual writes:** mismatch recovery and data authority are undefined.
- **Fallback gravity:** every target failure routes to old code, so confidence
  never grows and the old system remains mandatory.
- **Flags without extinction:** switches accumulate with no removal gate.
- **Green-suite illusion:** tests demonstrate coexistence but not target fit or
  legacy absence.
- **Migration without organizational change:** code boundaries move while
  ownership and delivery constraints recreate the former system.

## Exit conditions

The incremental module exits for a slice when target consumers and state use
the accepted path, the corresponding legacy path is retired, temporary
architecture is removed, and evidence is linked from the rebuild record. The
project exits the overall rebuild when every planned slice is complete or each
remaining legacy island has been accepted as an intentional current boundary.
