# Rebuild packet template

> Derived projection. This agent-facing template comes from the canonical
> semantic record at
`domain/rebuild-record.md` in Rebuild Labs. It is repeated inside the
capability so an installed skill can produce a complete packet without a source
checkout; changes originate in the domain record and are projected here.

Use this as a semantic template. Omit inapplicable sections with a reason rather
than leaving placeholders, and split the record only when the project needs
separate review or ownership.

## Identity and state

- Project and scope:
- Repository and current revision:
- Working-tree state:
- Record status and date:
- Direction owner and decision state:
- Architecture author and decision state:
- Acceptance owner:
- Authorized implementation unit and phase:
- Actions outside current authority:

## Direction contract

- Changed outcome:
- New or removed constraints:
- Required continuity:
- Intentional incompatibilities:
- Non-goals:
- Acceptance conditions:
- Unresolved owner questions:
- Superseded decisions:

## Target architecture

- Hypothesis or accepted-contract state:
- Target responsibilities and ownership:
- Target dependency direction:
- Forbidden inheritances:
- Competing hypotheses and discriminating evidence:

## Direction-gap map

| Inherited assumption | Evidence | Fit | Target impact | Decision state |
| --- | --- | --- | --- | --- |

## Baselines

| Role | Pinned identity | Rationale | Limitations |
| --- | --- | --- | --- |
| Source | | | |
| Evidence | | | |
| Compatibility | | | |
| Target | | | |

Use `not_applicable` for Source when construction is `evolve_in_place` or the
change class is `no_rebuild`; keep the current line in Evidence.

## Behavior matrix

| Behavior | Evidence | Evidence state | Target action | Origin interpretation | Authority state | Verification |
| --- | --- | --- | --- | --- | --- | --- |

## Asset disposition ledger

| Asset | Target obligation | Fit and coupling | Implementation | Knowledge | State | Evidence |
| --- | --- | --- | --- | --- | --- | --- |

## Transformation map

| Unit | Decision | Change class | Construction | Transition | Why | Rejected alternative | First vertical |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Execution and verification

| Unit and phase | Authorized scope | Success boundary | Target gate | Continuity/divergence gate | Stop threshold | Recovery action and authority | State |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Transition

- Consumers and route sequence:
- Data ownership and movement:
- Coexistence contract:
- Temporary architecture ledger:
- Observation and stop signals:
- Pre-authorized recovery actions and limits:
- Rollback or forward-recovery boundary:
- Deployment authority:
- Traffic or consumer-movement authority:
- External-data mutation authority:
- Old-write stop or ownership-transfer authority:
- Schema-contraction authority:
- Code and external-resource deletion authority:
- Retirement conditions:

## Source-line delta intake

- Live-line change owner and review cadence:
- Critical fixes and new obligations since source selection:
- Evidence invalidated by those changes:
- Selective intake decisions:
- Transition freeze window, if any:

## Decisions and residual limits

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
