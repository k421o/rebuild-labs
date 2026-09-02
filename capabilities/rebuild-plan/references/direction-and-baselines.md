# Direction, discontinuity, and baselines

## Direction brief

Capture these fields before deep implementation inspection when the request
provides enough intent:

- scope and affected project units;
- decision owner and current decision state;
- changed user or operator outcome;
- new and removed constraints;
- required continuity;
- allowed and intended breaks;
- non-goals;
- target responsibilities, ownership, and dependency direction;
- forbidden inheritances from the old architecture;
- acceptance evidence and accepting authority; and
- unresolved owner questions.

If implementation discovery later reveals a real constraint, amend the brief
with its evidence and decision. Do not silently convert “the code currently
does this” into “the target must do this.”

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
setup, known behavior, and later obligations—not age alone.

### Evidence baseline

Pinned revisions, releases, incidents, and operational observations used to
understand what exists and why. HEAD and historical revisions can both be
evidence without becoming construction starting points.

### Compatibility baseline

The exact interfaces, releases, data identities, observable behavior, and
consumers the owner or external contract still requires. Compatibility may be
narrower than current behavior.

### Target baseline

The owner-ratified direction and acceptance matrix used to judge progress. It
can supersede implemented decisions while remaining subject to normative
external obligations.

## Mode decision

Start with two axes:

| Discontinuity | Continuity | Default investigation |
| --- | --- | --- |
| Low | Any | Ordinary refactor |
| Moderate | High | Incremental rebuild |
| High | Manageable | Complete rebuild |
| High | High | Complete target construction plus incremental transition |

Then examine:

- whether a seam can route a meaningful vertical;
- whether the seam preserves a target-rejected model;
- hidden consumers and published compatibility;
- data reversibility and write ownership;
- independent target verification;
- security, privacy, licensing, and operational constraints;
- team capacity to support coexistence; and
- an explicit old-path retirement condition.

Choose modes per bounded unit. A project may build a core completely while
migrating consumers incrementally.
