# Recording a rebuild without preserving stale authority

Documentation should let a future developer or agent reconstruct what changed,
which facts remain true, and which implemented decisions are no longer the
destination. It should not flatten project history into one always-current
architecture story.

## Keep decision state explicit

Use the canonical record identifiers in the
[domain charter](../docs/domain-charter.md): `observation`, `hypothesis`,
`owner_ratified_direction`, `target_architecture_hypothesis`,
`target_architecture_accepted`, `implementation_authorized`, `planned`,
`implemented_not_cut_over`, `verified`, `cutover_ready`, `cut_over`, `retired`,
`invalidated`, and `superseded`.

Each record should name:

- author or deciding authority;
- scope and affected repositories or components;
- creation and decision dates;
- immutable evidence revisions where possible;
- current state and who may advance it;
- relationships to prior and superseding records; and
- unresolved questions and reevaluation triggers.

Do not rewrite an old architecture decision to sound as if the new direction
was always intended. Mark it superseded, preserve the forces it responded to,
and link the replacement. This keeps genuine historical knowledge while
preventing prior implementation from impersonating current authority.

## Minimum packet

### Direction contract

Records the current outcome, constraints, non-goals, required continuity,
allowed breaks, acceptance evidence, and deciding authority.

### Target architecture record

Records target responsibilities, ownership, dependency direction, forbidden
inheritance, alternatives, evidence, author, and hypothesis or accepted state.
Acceptance of this record is not implementation or transition authority.

### Baseline record

Names current and dirty state, source baseline candidates, selected immutable
ref, evidence revisions, compatibility releases or consumers, and selection
rationale.

### Behavior matrix

For each user-, operator-, protocol-, or data-visible behavior, separately
records evidence state (`observed`, `inferred`, `unknown`), target action
(`preserve_required`, `preserve_optional`, `change`, `remove`, `unresolved`),
origin interpretation (`intentional`, `accidental`, `unknown`), and authority
state.

### Asset disposition ledger

Names the asset unit, source identity, observed purpose, target obligation,
fit, coupling, implementation disposition, knowledge disposition, confidence,
decision state, destination, and verification.

### Execution and verification plan

Names rebuild units, proceed/defer/investigate decisions, change class,
construction and transition strategies,
authorized phases, vertical slices, dependency order, data and consumer
movement, coexistence, target gates, compatibility gates, intentional
divergence checks, negative architecture checks, and stopping conditions.

### Cutover and retirement receipt

Records what actually moved, exact revisions, data and consumer state,
observation window, acceptance, remaining recovery scope, removed temporary
architecture, retained legacy islands, and follow-up owners.

The plan and receipt name separate authority for deployment, traffic or
consumer movement, external data writes and reconciliation, stopping old
writes, schema contraction, and code or resource deletion.

## Avoid ambient stale guidance

- Keep the current target document easy to locate and name its status.
- Link superseded ADRs from their replacement and vice versa.
- Update operational and contributor docs when a route changes; do not make
  readers infer current behavior from a migration diary.
- Keep historical explanations in decision or migration records rather than
  scattering “formerly” notes through current interfaces.
- Do not edit an instruction-policy file merely because the rebuild revealed a
  useful rule. Route that exact change to the authority that owns the file.
- Keep one status view that points to detailed records; multiple independent
  “current plan” documents create a new provenance problem.

## Record actual evidence

A planned command is not an executed check. A passing test proves only the
property expressed by its oracle. A generated report does not advance an owner
decision. Record commands as run, attempted, failed, or not run according to
the actual task evidence and retain outputs only within security and privacy
boundaries.

Use small immutable decisions for consequential choices and a living rebuild
status for current execution. When the living status changes, Git history
preserves its evolution; when the governing direction changes, create a
superseding decision that explains why.
