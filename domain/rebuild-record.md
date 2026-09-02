# Rebuild record, version 1 draft

The rebuild record is the durable, target-owned packet connecting current
direction to implementation, verification, transition, and retirement. A
small project can keep it in one Markdown document. A larger project can split
the sections across ADRs, migration plans, and evidence records when one
current index retains the relationships and states.

## Semantic requirements

The record must distinguish:

- owner direction from agent inference;
- current implementation from target architecture;
- observed behavior from required compatibility;
- source, evidence, compatibility, and target baselines;
- implementation disposition from knowledge disposition;
- planned, implemented, verified, cut-over, and retired state;
- code transition from data and consumer transition; and
- a reversible code selection from externally irreversible effects.

Exact fields remain a draft until independent cases demonstrate a stable
machine interchange. A project may adapt names while preserving these
distinctions.

## Compact template

### Identity and state

- Project and bounded scope:
- Repository and current revision:
- Working-tree and external-state note:
- Record status and date:
- Direction owner:
- Acceptance owner:
- Actions outside current authority:

### Direction brief

- Changed outcome:
- New or removed constraints:
- Required continuity:
- Intentional incompatibilities:
- Non-goals:
- Target responsibilities and ownership:
- Target dependency direction:
- Forbidden inheritances:
- Acceptance conditions:
- Unresolved owner questions:
- Superseded decisions:

### Direction-gap map

| Inherited assumption | Pinned evidence | Fit | Target impact | Decision state |
| --- | --- | --- | --- | --- |

Fit is `aligned`, `isolatable`, `conflicting`, `obsolete`, or `unknown`.

### Baselines

| Role | Pinned identity | Selection rationale | Limitations |
| --- | --- | --- | --- |
| Source | | | |
| Evidence | | | |
| Compatibility | | | |
| Target | | | |

### Behavior matrix

| Behavior | Evidence | Target state | Authority | Verification |
| --- | --- | --- | --- | --- |

Target state is required continuity, permitted continuity, intentional
divergence, remove, unresolved, or unknown.

### Asset disposition ledger

| Asset | Target obligation | Fit and coupling | Implementation | Knowledge | State | Evidence |
| --- | --- | --- | --- | --- | --- | --- |

Implementation is salvage, refactor, re-derive, quarantine, or discard.
Knowledge is current contract, test/oracle, rationale, historical evidence, or
no special retention.

### Mode map

| Rebuild unit | Mode | Why | Rejected alternative | First vertical |
| --- | --- | --- | --- | --- |

Mode is complete rebuild, incremental rebuild, ordinary refactor, defer, or
investigate. A combined project names the mode of each unit.

### Execution and verification

| Slice | Target outcome | Dependencies | Target gate | Continuity or divergence gate | Legacy retirement |
| --- | --- | --- | --- | --- | --- |

### Transition

- Consumers and route sequence:
- Data ownership and movement:
- Coexistence contract:
- Temporary architecture ledger:
- Observation and stop signals:
- Rollback or forward-recovery boundary:
- Cutover authority:
- Retirement conditions:

### Decision log

| Date | Scope | State | Decision or observation | Evidence | Authority | Supersedes |
| --- | --- | --- | --- | --- | --- | --- |

### Residual limits

- Owner decisions needed:
- Security, privacy, legal, or operational review needed:
- Checks run and results:
- Checks not run:
- Residual risks:
- Reevaluation triggers:

## Custody and evolution

The target repository owns the record. Rebuild Labs may retain a sanitized
case interpretation but not a second live project plan. Update the living
status as work advances, keep consequential decisions immutable, and link
superseding decisions rather than rewriting their predecessors.
