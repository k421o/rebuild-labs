# rebuild-labs

`rebuild-labs` is a research and evaluation repository for changing the
architecture of a software project after its direction has moved far enough
that extending the inherited design is the wrong optimization. It studies how
to restart from an earlier baseline or replace a system in controlled slices
while preserving the behavior, data, decisions, and hard-won knowledge that
still serve the new goal.

The repository's installable skills are applications of that work. They are
not the authority for a target project's direction, and they do not turn a
request for ordinary refactoring into permission to rewrite a codebase.

## The problem

Coding agents are rewarded for making the next change fit the repository in
front of them. That is usually useful. It becomes costly after the owner has
changed the product direction, operating model, data boundary, runtime, or
other foundational constraint: the current architecture is then strong
evidence about the past, but weak authority for the future.

Without an explicit rebuild protocol, an agent tends to preserve accidental
boundaries, add compatibility layers around assumptions that are no longer
wanted, and cite the resulting complexity as a reason not to change course.
The opposite failure is a context-free rewrite that throws away validated
behavior, migration knowledge, and operational lessons.

Rebuild Labs develops a middle discipline:

> Let current owner direction govern the destination. Treat existing code and
> history as evidence to classify, not architecture to inherit automatically.

## Initial modules

| Module | Use it when | Governing idea |
| --- | --- | --- |
| [Complete rebuild](guides/complete-rebuild.md) | Foundational assumptions conflict with the target and carrying the existing structure forward costs more than selectively re-deriving it. | Start an isolated implementation line from a chosen historical or empty baseline, then import only target-compatible knowledge and assets. |
| [Incremental rebuild](guides/incremental-rebuild.md) | A rebuild is warranted and the system must keep operating, valuable boundaries remain usable, or data and consumers require staged replacement. | Establish a target-owned seam, replace vertical slices, verify each transfer, and retire the corresponding legacy path. |

Both modules consume the same [rebuild decision model](domain/rebuild-model.md).
The model separates eight questions that agents often collapse:

1. What current direction has the owner actually selected?
2. Which target architecture is proposed or accepted, and by whom?
3. Which inherited assumptions no longer fit it?
4. Is rebuilding warranted at all?
5. If so, should the target be constructed in place or on a target-native line,
   and should transition be direct or staged?
6. Which baseline makes the new direction easiest to realize and verify?
7. Which assets should be salvaged, refactored, re-derived, quarantined, or
   discarded?
8. What evidence will show that the new path works and that the old path can be
   retired?

## Repository model

```text
Owner direction + project evidence + history
                    |
                    v
      direction / architecture / gap / baselines
                    |
                    v
     rebuild record + asset disposition ledger
                    |
          +---------+----------+
          |                    |
          v                    v
  complete rebuild     incremental rebuild
          |                    |
          +---------+----------+
                    |
                    v
      verification, cutover, and learning
                    |
                    v
       evaluated agent capabilities
```

The stable middle is the domain vocabulary, evidence rules, rebuild record,
asset dispositions, and strategy-selection boundaries. Guides and skills
consume that core. Target repositories retain authority over their product
direction, architecture acceptance, implementation, deployment, transition,
data mutation, and deletion decisions.

## Core safeguards

- A new direction must be explicit enough to distinguish a real architectural
  discontinuity from frustration with difficult code. A real direction change
  may still be ordinary evolution when the current architecture supports it.
- “Rewind” means create an isolated branch or worktree at a pinned baseline;
  it never means destructively reset a user's working tree.
- Dirty work, releases, data, credentials, and externally visible state are
  inventoried before mutation.
- Compatibility is preserved only when the target still requires it. Existing
  behavior does not become a requirement merely because a characterization
  test can capture it.
- Code may be discarded while knowledge, tests, schemas, algorithms, fixtures,
  incident lessons, and decision provenance are retained.
- A parallel implementation is not progress by itself. Incremental work pairs
  every new slice with a route, acceptance evidence, and a retirement condition
  for the path it replaces.
- Architecture acceptance, implementation, traffic movement, consumer change,
  data writes, schema contraction, deletion, and publication are distinct
  grants; an agent-generated plan is not any of them.

## Project layout

```text
domain/         Rebuild vocabulary, records, dispositions, and strategy selection
research/       Findings, primary sources, case studies, and limitations
guides/         Complete and incremental rebuild playbooks
capabilities/   Canonical agent-facing projections of the domain work
evals/          Controlled direction-change scenarios and held-out expectations
products/       Generated installation adapters for evaluated capabilities
docs/           Charter, architecture, provenance, and release records
scripts/        Deterministic repository and packaging validation
tests/          Domain, capability, evaluation, and adapter contract checks
```

Directories are added only when current work justifies them. Rebuild Labs does
not begin as a migration platform, a code-transformation framework, or a store
for copies of projects being rebuilt.

## Initial capability bundle

- `rebuild-plan` is the mandatory read-only gateway for undecided work. It
  first decides whether rebuilding is warranted, then separates construction
  and transition choices and produces a disposition ledger.
- `rebuild-complete` implements an explicitly authorized complete rebuild in an
  isolated target-native line, transferring selected behavior and knowledge
  without treating current structure as a template.
- `rebuild-incremental` implements an explicitly authorized staged rebuild
  through target-owned seams and vertical slices, or stages transition to a
  target-native line built by `rebuild-complete`.

The [domain charter](docs/domain-charter.md) defines scope and evidence rules.
The [architecture](docs/architecture.md) defines authority and dependency
direction. The [guide index](guides/README.md) is the human-facing path through
the two modules.

## Status

The domain model and capability bundle are experimental. The initial guidance
is a testable synthesis, not a universal rule that rewrites are better than
refactors. Case evidence and controlled evaluations must challenge both false
inertia and false rewrite enthusiasm before a capability is promoted.

## Development

Python 3.12+ and [`uv`](https://docs.astral.sh/uv/) are used for deterministic
validation and product generation.

```console
uv sync --locked --dev
uv run ruff check .
uv run pytest
uv run python scripts/validate_evals.py
uv run python scripts/check_markdown_links.py
uv run python scripts/build_plugin.py --check
```

## License

MIT
