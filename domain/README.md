# Rebuild domain

This directory owns the shared vocabulary and decision model used by both
rebuild modules.

- [`glossary.md`](glossary.md) defines the terms that prevent direction,
  history, baselines, compatibility, and implementation from collapsing into
  one idea.
- [`rebuild-model.md`](rebuild-model.md) defines the direction-gap assessment,
  asset dispositions, no-rebuild decision, independent construction and
  transition selection, record structure, and invariants.
- [`rebuild-record.md`](rebuild-record.md) defines the durable target-owned
  packet and a compact semantic template.

The contracts are intentionally semantic before they are machine schemas.
Initial cases should test whether the fields are stable enough to version
before JSON structure is treated as canonical.
