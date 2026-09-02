# Rebuild record, version 1 draft

The rebuild record is the durable, target-owned packet connecting current
direction to implementation, verification, transition, and retirement. A
small project can keep it in one Markdown document. A larger project can split
the sections across ADRs, migration plans, and evidence records when one
current index retains the relationships and states.

## Semantic requirements

The record must distinguish:

- owner direction from agent inference;
- owner direction from an agent-authored target architecture hypothesis;
- target-architecture acceptance from implementation authorization;
- current implementation from target architecture;
- observed behavior from required compatibility;
- source, evidence, compatibility, and target baselines;
- implementation disposition from knowledge disposition;
- `planned`, `implemented_not_cut_over`, `verified`, `cutover_ready`,
  `cut_over`, `retired`, `invalidated`, and `superseded` state;
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
- Direction owner and decision state:
- Architecture author and decision state:
- Acceptance owner:
- Authorized implementation unit and phase:
- Actions outside current authority:

### Direction contract

- Changed outcome:
- New or removed constraints:
- Required continuity:
- Intentional incompatibilities:
- Non-goals:
- Acceptance conditions:
- Unresolved owner questions:
- Superseded decisions:

### Target architecture

- Hypothesis or accepted-contract state:
- Target responsibilities and ownership:
- Target dependency direction:
- Forbidden inheritances:
- Competing hypotheses and discriminating evidence:

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

Use `not_applicable` for Source when construction is `evolve_in_place` or the
change class is `no_rebuild`; keep the current line in Evidence.

### Behavior matrix

| Behavior | Evidence | Evidence state | Target action | Origin interpretation | Authority state | Verification |
| --- | --- | --- | --- | --- | --- | --- |

Evidence state is `observed`, `inferred`, or `unknown`. Target action is
`preserve_required`, `preserve_optional`, `change`, `remove`, or `unresolved`.
Origin interpretation is `intentional`, `accidental`, or `unknown`. Evidence
and origin do not select the target action; its authority must be recorded.

### Asset disposition ledger

| Asset | Target obligation | Fit and coupling | Implementation | Knowledge | State | Evidence |
| --- | --- | --- | --- | --- | --- | --- |

Implementation is salvage, refactor, re-derive, quarantine, or discard.
Knowledge is current contract, test/oracle, rationale, historical evidence, or
no special retention.

### Transformation map

| Unit | Decision | Change class | Construction | Transition | Why | Rejected alternative | First vertical |
| --- | --- | --- | --- | --- | --- | --- | --- |

Decision is `proceed`, `defer`, or `investigate`. When proceeding, change class
is `no_rebuild` or `rebuild`; construction is `evolve_in_place` or
`target_native_line`; and transition is `direct` or `staged`. Leave strategies
unselected with an explicit blocking condition when deferring or investigating.
For `no_rebuild`, name the ordinary path: evolution, refactor, modernization,
or upgrade.

### Execution and verification

| Unit and phase | Authorized scope | Success boundary | Target gate | Continuity or divergence gate | Stop threshold | Recovery action and authority | State |
| --- | --- | --- | --- | --- | --- | --- | --- |

State may include `planned`, `implemented_not_cut_over`, `verified`,
`cutover_ready`, `cut_over`, `retired`, `invalidated`, or `superseded`. A phase
can finish positively without receiving permission to perform the next one.

### Transition

- Consumers and route sequence:
- Data ownership and movement:
- Coexistence contract:
- Temporary architecture ledger:
- Observation and stop signals:
- Pre-authorized recovery actions and limits:
- Rollback or forward-recovery boundary:
- Authority for deployment:
- Authority for traffic or consumer movement:
- Authority for external data writes, backfill, and reconciliation:
- Authority for stopping old writes:
- Authority for schema contraction:
- Authority for code and external-resource deletion:
- Retirement conditions:

### Source-line delta intake

- Live-line change owner and review cadence:
- Critical fixes and new obligations since source selection:
- Evidence invalidated by those changes:
- Selective intake decisions:
- Transition freeze window, if any:

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
status as work advances. Retain accepted decision context and link superseding
decisions rather than silently rewriting their predecessors.
