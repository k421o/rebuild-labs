# Rebuild Labs domain charter

## Purpose

Rebuild Labs studies how software projects should respond when their current
direction invalidates enough inherited assumptions that extending the existing
architecture becomes a source of waste. It turns that study into explicit
decision models, reproducible case evidence, practical playbooks, evaluation
methods, and optional agent capabilities.

The domain is concerned with intentional direction-change rebuilding. It is
not about compiling source code, restoring a broken deployment, recovering
lost data, or rewriting code merely because it is old or unfamiliar.

## Questions in scope

- What evidence distinguishes a foundational direction change from an ordinary
  feature, refactor, modernization, or maintenance problem?
- How should a project record the current owner's desired outcomes,
  constraints, exclusions, and acceptance conditions before inherited code
  anchors the solution?
- When is a complete rebuild from an empty or historical baseline preferable
  to staged replacement inside the operating system?
- Which historical point is a useful source baseline, and which current or
  released behavior remains a compatibility baseline?
- How can code, tests, schemas, data, interfaces, algorithms, operational
  knowledge, and decision history be evaluated independently rather than kept
  or discarded as one block?
- Which assets should be salvaged unchanged, refactored, re-derived,
  quarantined, or discarded, and what evidence supports each disposition?
- How can a new implementation avoid inheriting the architecture it is meant
  to replace while still learning from past failures and validated behavior?
- How should teams stage verification, data movement, consumer migration,
  cutover, rollback or forward recovery, and retirement of the old path?
- Which records preserve why the direction changed and prevent superseded
  assumptions from silently regaining authority?
- How can controlled scenarios test whether an agent resists both current-state
  anchoring and unnecessary rewrite enthusiasm?

## Outputs

The domain may produce:

- A vocabulary for direction discontinuities, baselines, rebuild modes,
  compatibility commitments, seams, slices, and asset dispositions.
- Rebuild records, disposition ledgers, target charters, decision logs,
  verification matrices, and cutover or retirement plans.
- Complete and incremental rebuild guides with practical sequencing and safety
  boundaries.
- Research syntheses with traceable primary sources, case studies, competing
  interpretations, and limitations.
- Controlled repositories, direction-change prompts, expected decisions,
  anti-findings, and execution records for agent evaluation.
- Canonical planning and implementation capabilities derived from the domain
  work.
- Generated adapters that package evaluated capabilities for a specific agent
  host without taking authority from their sources.

## Non-goals

Rebuild Labs does not:

- prescribe rewrites whenever a codebase is difficult, inconsistent, old, or
  poorly documented;
- define one universal architecture, language, framework, repository layout,
  or migration pattern;
- treat the current implementation as worthless merely because the target
  architecture changes;
- guarantee semantic equivalence when the owner has intentionally changed the
  product contract;
- turn all observed behavior into a compatibility requirement;
- authorize destructive Git operations, deployment, data deletion, consumer
  cutover, public release, or archival on behalf of a target owner;
- replace security, privacy, legal, data-governance, or incident-recovery
  review;
- store working copies of target projects or become a central architecture
  authority for them; or
- claim that code reuse, rewrite percentage, diff size, or elapsed time is a
  quality score.

## Stable domain core

The intended stable middle consists of:

1. A direction contract that separates current owner intent from inherited
   implementation assumptions.
2. A baseline model that separates historical source, current evidence,
   released compatibility, and target acceptance.
3. A rebuild decision that selects complete, incremental, ordinary refactor,
   defer, or investigate further from evidence rather than fashion.
4. An asset disposition model that can preserve knowledge without preserving
   its current representation.
5. A rebuild record linking decisions, slices, evidence, verification,
   cutover, retirement, and supersession over time.
6. Safety and authority rules for isolated work, external state, destructive
   actions, and acceptance.

Collectors, guides, evaluation runners, and product adapters may change while
preserving these contracts or versioning their replacements.

## Evidence hierarchy

Evidence is interpreted according to the claim it can support:

1. **Current owner direction** authorizes desired outcomes, constraints,
   intentional incompatibilities, and acceptance decisions for its scope.
2. **Normative external contracts** establish constraints from platforms,
   protocols, laws, consumers, and published compatibility promises.
3. **Executable and repository evidence** establishes what a pinned revision
   actually implements, tests, builds, stores, or exposes.
4. **Operational evidence** establishes observed production behavior,
   incidents, migrations, costs, and recovery boundaries within its recorded
   environment and time window.
5. **History and decision records** explain how the current state arose; they
   do not outrank a later owner-ratified direction merely because they are
   older or already implemented.
6. **Published case studies and patterns** supply candidate techniques and
   cautions, not automatic prescriptions for a different project.
7. **Agent inference** proposes interpretations and plans. It cannot ratify the
   target direction or declare a migration accepted.

Every consequential conclusion should name its source, revision or date,
scope, authority role, and important uncertainty.

## Decision states

Records distinguish at least these states:

1. **Observation** — pinned evidence about current or historical behavior.
2. **Hypothesis** — a proposed direction, disposition, or rebuild explanation.
3. **Owner-ratified direction** — the affected owner selected the target for
   the named scope.
4. **Planned rebuild** — mode, baseline, dispositions, gates, and authority
   boundaries are recorded.
5. **Implemented slice** — code or configuration realizes part of the plan.
6. **Verified slice** — named evidence meets its acceptance conditions.
7. **Cut over** — intended consumers or traffic use the target path.
8. **Retired** — the replaced path no longer owns live behavior or state.
9. **Superseded** — a later record replaces the decision and links back to it.

A merged pull request, passing test, or agent-authored plan does not silently
advance an owner-controlled state.

## Canonical ownership

`rebuild-labs` owns the editable rebuild-domain vocabulary, research
interpretation, evaluation contracts, and canonical capability sources. Each
target repository owns its direction, local architecture, implementation,
acceptance, deployment, data, and deletion decisions.

[`k421o/readme-labs`](https://github.com/k421o/readme-labs) is a structural
reference for this domain-first repository shape; it is not evidence for
rebuild conclusions. [`k421o/provenance-labs`](https://github.com/k421o/provenance-labs)
studies whether consequential requirements and guarantees have appropriate
authority and realistic evidence. Rebuild Labs consumes that distinction but
owns the separate question of how to transform a system after direction has
changed.

Agent Ops may coordinate a rebuild that crosses repositories. It does not
acquire the affected repositories' implementation authority.

## Change discipline

- Freeze an independently readable target charter before deep implementation
  inspection when practical, then record later discoveries as amendments.
- Separate observed behavior from behavior the target must preserve.
- Record disposition decisions per asset or coherent asset class; never label
  the whole old codebase “legacy” as if that decided its value.
- Use pinned Git identities and content hashes where a conclusion depends on
  exact bytes.
- Keep complete and incremental modules on one shared vocabulary while
  evaluating their different failure modes separately.
- Treat automated checks and agent evaluations as evidence. Owners or their
  designated reviewers retain promotion and acceptance authority.
- Add infrastructure, schemas, product adapters, or repositories only after a
  concrete case demonstrates the boundary.
