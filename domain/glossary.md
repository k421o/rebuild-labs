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

**Target charter**
: An implementation-neutral record of the current direction, acceptance
  conditions, required continuity, intentional incompatibilities, non-goals,
  authority, and unresolved decisions.

**Direction gap**
: The material difference between the target charter and assumptions required
  by the inherited architecture.

## Baselines

**Source baseline**
: The empty tree or pinned historical revision from which a complete rebuild
  implementation line begins. It is a construction choice, not the complete
  statement of required behavior.

**Evidence baseline**
: Pinned current and historical revisions inspected to establish what exists,
  how it behaves, and why it changed.

**Compatibility baseline**
: A release, interface, data state, observable behavior set, or consumer
  contract the owner still requires the rebuild to support.

**Target baseline**
: The accepted direction and verification conditions against which rebuild
  progress is judged.

**Stable point**
: A pinned revision with known identity and enough verified behavior to serve
  a useful source or comparison point. “Stable” is always relative to a named
  purpose; it does not mean universally correct.

## Rebuild modes

**Complete rebuild**
: Construction of a new implementation line whose architecture is derived
  from the target charter rather than evolved in place from the current tree.
  Selected old assets may still be imported, adapted, or re-derived.

**Incremental rebuild**
: Replacement of an operating architecture through explicit seams and
  independently verifiable slices while old and new paths coexist for a
  bounded period.

**Ordinary refactor**
: An internal structural change that preserves the governing direction and
  external contract. Refactoring may be difficult without constituting a
  rebuild.

**Hybrid rebuild**
: Different bounded units use different rebuild modes under one target
  charter. “Hybrid” must name each unit; it is not a substitute for deciding.

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
  mode, slices, verification, cutover, retirement, and later supersession.

**Intentional divergence**
: A prior behavior or contract the target owner explicitly chooses not to
  preserve.

**Characterization evidence**
: An observation or test that captures current behavior. It proves what was
  observed within its scope, not that the target must retain that behavior.

**Acceptance evidence**
: Evidence matched to a target condition and accepted by its named authority.

**Knowledge quarry**
: The old codebase viewed as a source of facts, tests, cases, algorithms,
  constraints, and lessons rather than a blueprint whose shape must survive.
