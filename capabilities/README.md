# Canonical capability projections

The three capabilities form one atomic bundle: `rebuild-plan` is the shared
router and planning gateway; `rebuild-complete` owns target-native
construction; and, for the `rebuild` change class, `rebuild-incremental` owns
evolve-in-place construction and staged transition. The two implementation
modules may compose for one unit.

Domain contracts and guides are authoritative for Rebuild Labs. Capability
references repeat the minimum operational context needed after installation;
they are derived projections, not a second source of truth.

| Capability projection | Canonical sources |
| --- | --- |
| `rebuild-plan/references/direction-and-baselines.md` | `domain/glossary.md`, `domain/rebuild-model.md` steps 1–6 |
| `rebuild-plan/references/asset-dispositions.md` | `domain/rebuild-model.md` steps 5 and 7 |
| `rebuild-plan/references/evidence-and-safety.md` | `docs/domain-charter.md`, `domain/rebuild-model.md` step 8 and invariants |
| `rebuild-plan/references/rebuild-packet-template.md` | `domain/rebuild-record.md` |

Tests keep this mapping present and verify essential vocabulary. Product
generation copies all three capability directories byte for byte from an
explicit allowlist and records their source revisions and hashes.
