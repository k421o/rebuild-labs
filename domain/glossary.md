# Rebuild glossary

## Direction terms

**Current direction**
: The outcomes, constraints, exclusions, and priorities currently selected by
  the owner for a named project scope. It may supersede implemented decisions.

**Direction discontinuity**
: A change that invalidates one or more foundational assumptions of the
  existing architecture, so local extension is no longer obviously the
  shortest safe path to the target.

**Inherited assumption**
: A premise encoded in current structure, dependencies, data, deployment, or
  behavior. An inherited assumption may still be valid, intentionally
  superseded, or merely accidental.

**Direction contract**
: An implementation-neutral record of owner-selected outcomes, constraints,
  required continuity, allowed breaks, non-goals, acceptance conditions,
  authority, and unresolved product or operational decisions.

**Target architecture hypothesis**
: A proposed technical interpretation of the direction contract: target
  responsibilities, state ownership, trust boundaries, dependency direction,
  and forbidden dependencies. It remains a hypothesis until the authority for
  that project accepts it.

**Target architecture contract**
: A target architecture hypothesis accepted for a named scope. Its acceptance
  does not by itself authorize implementation, deployment, cutover, data
  mutation, or deletion.

**Implementation authorization**
: The exact technical unit and phase an actor may change. It is distinct from
  direction, architecture acceptance, and authority over external transition.

**Direction gap**
: The material difference between the direction contract or accepted target
  architecture and assumptions required by the inherited architecture.

## Baselines

**Source baseline**
: The empty tree or pinned historical revision from which a complete rebuild
  implementation line begins. It is a construction choice, not the complete
  statement of required behavior. Record it as not applicable for
  `evolve_in_place` construction or a no-rebuild path; the current line still
  belongs in the evidence baseline.

**Evidence baseline**
: Pinned current and historical revisions inspected to establish what exists,
  how it behaves, and why it changed.

**Compatibility baseline**
: A release, interface, data state, observable behavior set, or consumer
  contract the owner still requires the rebuild to support.

**Target baseline**
: The direction contract, accepted target architecture where one exists, and
  verification conditions against which work is judged.

**Stable point**
: A pinned revision with known identity and enough verified behavior to serve
  a useful source or comparison point. “Stable” is always relative to a named
  purpose; it does not mean universally correct.

## Transformation strategies

**Transformation decision**
: `proceed`, `defer`, or `investigate` for a named unit. Proceeding requires an
  explicit change class, construction strategy, and transition strategy;
  deferral or investigation retains the blocking condition rather than
  inventing a strategy.

**Change class**
: `no_rebuild` when existing governing boundaries can support the direction,
  or `rebuild` when a foundational boundary must be replaced.

**No rebuild**
: The direction can be realized without replacing a foundational architecture
  boundary. The work proceeds as ordinary evolution, refactoring,
  modernization, or an upgrade.

**Ordinary evolution**
: A changed product outcome or external contract implemented through an
  architecture that already supports or is neutral toward it. Direction can
  change without requiring a rebuild.

**Complete rebuild**
: Construction of a new implementation line whose architecture is derived
  from the direction contract and target architecture rather than evolved in
  place from the current tree. Selected old assets may still be imported,
  adapted, or re-derived. Transition may be direct or staged.

**Incremental rebuild**
: Replacement through explicit seams and independently verifiable slices. It
  can construct the target in place, transition a separately built target line
  in stages, or do both while old and new paths coexist for a bounded period.

**Ordinary refactor**
: An internal structural change that preserves the governing direction and
  external contract. Refactoring may be difficult without constituting a
  rebuild.

**Construction strategy**
: How the target is built: `evolve_in_place` through seams or
  `target_native_line` on an independently derived implementation line.

**Transition strategy**
: How responsibility reaches the target: `direct` at one accepted boundary or
  `staged` by consumer, route, capability, or data partition.

**Combined rebuild**
: Target-native construction followed by staged transition for the same unit.
  The complete module owns construction and the incremental module owns the
  staged transition. Different units may independently choose other pairings.

**Rewind**
: Selection of a pinned historical point for a new isolated branch or worktree.
  It does not mean moving or deleting the active branch, working tree, or
  remote reference.

## Asset terms

**Asset**
: A coherent unit considered for transfer: source code, tests, schema, data,
  interface, dependency knowledge, algorithm, configuration, fixture,
  operational procedure, incident lesson, documentation, or decision record.

**Salvage**
: Carry an asset substantially unchanged because it fits the target and its
  behavior, provenance, license, and coupling are understood.

**Refactor**
: Adapt an asset while preserving a named responsibility or behavior that
  still belongs in the target.

**Re-derive**
: Preserve the verified knowledge, contract, example, or lesson expressed by
  an asset while implementing a new representation from the target model.

**Quarantine**
: Retain an asset or reference outside the target path while its value,
  authority, safety, or compatibility remains unresolved.

**Discard**
: Intentionally exclude an asset and record why no target requirement depends
  on it. Discarding implementation does not imply erasing Git history.

**Disposition ledger**
: The evidence-bearing set of asset decisions, including unit, target
  relevance, coupling, selected disposition, verification, confidence, and
  owner questions.

## Incremental replacement terms

**Seam**
: A controlled boundary where traffic, calls, data, or ownership can be routed
  between old and target implementations.

**Vertical slice**
: The smallest end-to-end unit that delivers and verifies one meaningful
  target behavior across every layer it actually needs.

**Coexistence contract**
: The temporary rules for identity, routing, data ownership, compatibility,
  observability, and recovery while old and new paths are both present.

**Retirement condition**
: Evidence and owner acceptance required before the old path for a slice stops
  receiving traffic, owning state, or constraining the target.

## Record and evidence terms

**Rebuild record**
: The target-owned chain connecting direction, baseline, gap, dispositions,
  construction, transition, slices, verification, cutover, retirement, and
  later supersession.

**Evidence state**
: Whether a behavior is `observed`, `inferred`, or `unknown` in the pinned
  evidence.

**Target action**
: What the current direction does with a behavior: `preserve_required`,
  `preserve_optional`, `change`, `remove`, or `unresolved`.

**Origin interpretation**
: Whether prior behavior appears `intentional`, `accidental`, or `unknown`.
  This explains history; it does not decide the target action.

**Intentional divergence**
: A prior behavior or contract the target owner explicitly chooses not to
  preserve.

**Characterization evidence**
: An observation or test that captures current behavior. It proves what was
  observed within its scope, not that the target must retain that behavior.

**Acceptance evidence**
: Evidence matched to a target condition and accepted by its named authority.

**Implemented, not cut over**
: Code or configuration realizes the authorized target scope, but external
  traffic, consumers, writes, or ownership have not moved.

**Cutover ready**
: The planned preconditions for an external transition are verified, but the
  action awaits its own authority or operating window.

**Knowledge quarry**
: The old codebase viewed as a source of facts, tests, cases, algorithms,
  constraints, and lessons rather than a blueprint whose shape must survive.
