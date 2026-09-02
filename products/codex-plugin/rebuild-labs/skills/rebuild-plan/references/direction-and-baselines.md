# Direction, discontinuity, and baselines

> Derived projection. Canonical semantics live in `domain/glossary.md` and
> steps 1–6 of `domain/rebuild-model.md`. This installed copy is operational
> context; changes originate in those domain sources.

## Direction contract

Capture these fields before deep implementation inspection when the request
provides enough intent:

- scope and affected project units;
- decision owner and current decision state;
- changed user or operator outcome;
- new and removed constraints;
- required continuity;
- allowed and intended breaks;
- non-goals;
- acceptance evidence and accepting authority; and
- unresolved owner questions.

If implementation discovery later reveals a real constraint, amend the
contract through its direction authority with the evidence and decision. Do
not silently convert “the code currently does this” into “the target must do
this.”

## Target architecture and implementation authorization

Record target responsibilities, state and trust ownership, dependency
direction, forbidden inheritances, alternatives, and discriminating evidence
as a separately authored target architecture hypothesis. If the relevant
project authority accepts it, record an accepted target architecture contract.

Neither a direction contract nor architecture acceptance supplies
implementation authority. Record the exact unit and phase the current actor
may change, plus the success boundary and actions that remain outside scope.

## Direction discontinuity

Look for conflict in foundational assumptions rather than diff size:

- primary user, job, or product identity;
- domain vocabulary or core data model;
- state, trust, security, or permission ownership;
- public interface or compatibility promise;
- runtime, deployment unit, availability, or offline/online model;
- extension, plugin, tenancy, or integration boundary;
- dependency direction and source authority; or
- organizational ownership and delivery flow when it constrains architecture.

Classify each relevant inherited assumption:

- `aligned`: supports the target directly;
- `isolatable`: conflicts locally but can be contained behind a credible seam;
- `conflicting`: would make the target depend on a rejected boundary;
- `obsolete`: serves a job the target removes; or
- `unknown`: current evidence cannot determine fit.

## Four baselines

### Source baseline

The empty tree or immutable historical revision used to start a complete target
line. Compare candidates on target clarity, accidental inheritance, useful
setup, known behavior, and later obligations—not age alone. Record
`not_applicable` for evolve-in-place construction or a no-rebuild path; keep
the current line in the evidence baseline.

### Evidence baseline

Pinned revisions, releases, incidents, and operational observations used to
understand what exists and why. HEAD and historical revisions can both be
evidence without becoming construction starting points.

### Compatibility baseline

The exact interfaces, releases, data identities, observable behavior, and
consumers the owner or external contract still requires. Compatibility may be
narrower than current behavior.

### Target baseline

The owner-ratified direction, accepted target architecture where one exists,
and acceptance matrix used to judge progress. It can supersede implemented
decisions while remaining subject to normative external obligations.

## Transformation decision

First allow a no-rebuild result, then select construction and transition
independently:

| Situation | Change class | Construction | Transition |
| --- | --- | --- | --- |
| Changed direction, architecture already supports it | `no_rebuild` (ordinary evolution) | `evolve_in_place` | `direct` or `staged` |
| Direction and external contract unchanged | `no_rebuild` (ordinary refactor) | `evolve_in_place` | `direct` |
| Material conflict with a strong seam | `rebuild` | `evolve_in_place` | `staged` |
| Material conflict, independent target clearer | `rebuild` | `target_native_line` | `direct` or `staged` |

For a rebuild candidate, then examine:

- whether a seam can route a meaningful vertical;
- whether the seam preserves a target-rejected model;
- hidden consumers and published compatibility;
- data reversibility and write ownership;
- independent target verification;
- security, privacy, licensing, and operational constraints;
- team capacity to support coexistence; and
- an explicit old-path retirement condition.

Choose all three fields per bounded unit. `rebuild-complete` owns
`target_native_line` construction. Within the `rebuild` change class,
`rebuild-incremental` owns `evolve_in_place` construction and each `staged`
transition, including the transition to a completely rebuilt target core. A
normal staged rollout of no-rebuild feature work does not invoke a rebuild
module merely because its transition is staged.
