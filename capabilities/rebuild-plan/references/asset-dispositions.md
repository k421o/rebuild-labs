# Asset disposition and re-entry gate

Treat the existing project as a quarry of small assets, not one legacy block.
Assets can include behavior, API and file-format contracts, domain rules,
algorithms, data semantics, tests, fixtures, operational knowledge, decisions,
source code, configuration, and generated artifacts.

## Two independent decisions

### Implementation disposition

- **Salvage:** transfer substantially unchanged because the asset already fits
  target boundaries.
- **Refactor:** preserve its responsibility or behavior while changing
  representation, coupling, or dependencies.
- **Re-derive:** use verified knowledge or contract as input to a target-native
  implementation without porting the old code structure.
- **Quarantine:** retain outside the target path until provenance, safety,
  behavior, or authority is resolved.
- **Discard:** exclude intentionally because no accepted target obligation
  depends on it or it would reintroduce a superseded assumption.

### Knowledge disposition

- preserve as current contract;
- preserve as test or validation oracle;
- preserve as domain or operational rationale;
- retain as historical evidence only; or
- no retention required beyond ordinary repository history.

Discarding implementation while preserving knowledge is often the most
important rebuild decision.

## Re-entry questions

For every transfer candidate, answer:

1. Which target obligation does it serve?
2. Is that obligation owner-ratified, externally required, permitted, changed,
   or merely inherited?
3. What direct evidence establishes the asset's present behavior?
4. Does it obey target ownership, state, trust, and dependency direction?
5. What superseded architecture would travel with it?
6. Is reuse or adaptation safer and cheaper than re-derivation after migration,
   integration, and verification costs?
7. Are origin, license, secrets, privacy, security, generated-source, and
   authorship constraints understood?
8. Which target and compatibility evidence will accept the transferred asset?
9. Which negative check can detect forbidden legacy coupling returning?

If a material answer is unknown, quarantine or raise an owner question rather
than defaulting to reuse or discard.

## Ledger fields

Use these fields directly or map them into a project-local record:

```text
asset_id
asset_kind
source_repository
source_revision
source_path_or_identity
content_hash_if_needed
observed_purpose
target_obligation
target_fit
behavior_evidence
coupling_and_forbidden_dependencies
state_or_identity_role
implementation_disposition
knowledge_disposition
decision_state
deciding_authority
rationale_and_alternatives
target_location
acceptance_evidence
residual_risk
```

Do not calculate a universal reuse score. False precision encourages agents to
maximize retained code rather than target alignment.

## Behavior matrix

Observed behavior receives one target state:

- `required_continuity`;
- `permitted_continuity`;
- `intentional_divergence`;
- `remove`;
- `unresolved`; or
- `unknown`.

Characterization evidence can establish the observation. It cannot choose the
target state. Link that state to an owner decision or external obligation.
