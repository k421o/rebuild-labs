---
name: rebuild-incremental
description: Implement an explicitly authorized evolve-in-place construction or staged transition when a material direction change has been classified as a rebuild. Use when asked to replace a system slice by slice, route consumers to a target-native replacement in stages, use strangler or branch-by-abstraction techniques, or preserve continuous operation during an accepted rebuild. Do not use merely because continuity is desirable, for assessment-only work, compilation, disaster recovery, ordinary evolution, or undecided strategy; use rebuild-plan first.
---

# Incremental project rebuild

Move an operating project toward its target architecture through explicit
seams and vertical slices. Make coexistence observable and bounded, give every
slice a retirement condition, and require actual retirement for a fully
transitioned slice without forcing it into a code-only phase.

## Required planning source

Before implementation, read the sibling
[`rebuild-plan` skill](../rebuild-plan/SKILL.md) completely and read every file
in its [`references/`](../rebuild-plan/references/) directory. Use its
direction, architecture, baseline, disposition, evidence, safety, and record
behavior as the installed planning contract.

If no accepted rebuild packet exists, or construction and transition have not
been selected independently, perform the gateway workflow first. Keep owner
direction, architecture hypothesis and acceptance, implementation authority,
verification, cutover, data mutation, deletion, and retirement in distinct
decision states.

## Authorization and preservation

- Confirm implementation is requested.
- Pin the authorized unit and phase, phase success boundary, halt or recovery
  threshold, and invalidation or strategy-switch conditions. Authority for one
  slice is not authority for every planned slice.
- If the target architecture remains a hypothesis, confirm that authorization
  explicitly covers a bounded evidence-gathering implementation. Keep it
  experimental and do not transition consumers, traffic, writes, or ownership
  until the architecture and each action are accepted and authorized.
- Read applicable target instructions and inspect Git, dirty state, releases,
  consumers, data, deployments, and external ownership before mutation.
- Preserve unrelated work and use the isolation strategy required by the
  repository.
- Do not infer production routing, deployment, irreversible data migration,
  consumer cutover, or deletion authority from permission to edit code.
- State what rollback or forward recovery can actually restore before relying
  on it.

## Workflow

1. **Materialize distinct contracts.** Record the owner-ratified direction
   contract. Separately record the target architecture hypothesis or accepted
   contract, its author and state, required compatibility, intentional
   divergences, and implementation authorization for this unit and phase.
2. **Map observed flows.** Pin current evidence and inventory callers, routes,
   protocols, jobs, identities, data stores, writes, ownership transitions,
   observability, and recovery paths. Map behavior, not only file structure.
3. **Select one seam.** Choose a bounded routing, interface, repository, event,
   command, page, file-format, consumer, or data-access boundary with observable
   input/output, controllable selection, and a credible removal path. Reject a
   seam that makes the target permanently depend on the rejected model.
4. **Define one vertical slice.** Name the target outcome, consumers and data,
   admitted assets, required continuity, intentional changes, coexistence
   contract, acceptance evidence, phase success boundary, stop signals,
   temporary artifacts, authorized recovery scope, and old-path retirement
   condition.
5. **Make the target own the contract.** Introduce a target-facing abstraction
   or route, adapt legacy concepts at the boundary, and keep old behavior stable
   through a separately verified preparatory step. Avoid a “neutral” union of
   every old and new concept.
6. **Implement the target path.** Build the complete slice using target
   boundaries. Apply the asset re-entry gate. Add target-fitness and negative
   legacy-dependency checks before increasing its responsibility.
7. **Expand and observe within authority.** When explicitly authorized, expand
   APIs or schemas so both paths can work temporarily. Use shadow execution,
   comparison, canaries, cohort routing, or carefully designed dual operations
   according to risk. Normalize nondeterminism and protect side effects,
   privacy, latency, and capacity.
8. **Migrate bounded ownership only under its grant.** Immediately before
   moving a caller, cohort, request class, or data partition, check routing,
   consumer, and data-mutation authority for that exact action. For data,
   record canonical ownership, backfill, concurrent writes, restartability,
   reconciliation, and recovery. Treat old mismatches as observations to
   classify, not automatic target truth.
9. **Verify the route.** Exercise target acceptance, required continuity,
   intentional differences, architecture fitness, data invariants, operational
   health, and the stated stop or recovery path. Record the actual observation
   window and traffic; absence of alerts alone is not proof.
10. **Contract and extinguish only under action-local authority.** Check
    separate grants before stopping old traffic or writes, contracting schemas
    or compatibility, and deleting code or external resources. Acceptance is
    not retirement authority. If a grant is absent, record
    `implemented_not_cut_over` or `cutover_ready` and stop without treating the
    phase as failed.

## Temporary architecture ledger

Every router, adapter, flag, façade, dual write, legacy mimic, replicated
store, or fallback introduced for coexistence must record:

- purpose and creating slice;
- owner;
- exact dependency and data boundaries;
- observation and failure behavior;
- removal condition;
- expected removal point or reevaluation trigger; and
- verification that removal occurred.

Do not call indefinite compatibility “temporary.” If a legacy island must
remain, convert it into an explicit current boundary with an owner and contract.

## Action-local authority

Check authority immediately before each deployment, traffic or consumer move,
external data write/backfill/reconciliation, stopping old writes, canonical
ownership transfer, schema contraction, code deletion, or external-resource
deletion. Record the exact unit, environment, operation, and phase. A broad
request to edit code and a target acceptance decision authorize none of these
implicitly.

## Completion behavior

The invocation completes at its authorized phase boundary. A code-only phase
may complete as `implemented_not_cut_over`; a verified transition plan may
complete as `cutover_ready`. A fully transitioned slice additionally requires
the target path to serve its accepted scope, the old path to stop receiving
that traffic or owning that state, and transition-only artifacts to be removed
or explicitly retained by decision. A project completes when all planned
slices meet that condition or remaining legacy islands are accepted as the
current architecture.

When a stop threshold fires, stop expansion, preserve the observation, execute
only the pre-authorized recovery action, and mark affected evidence or the plan
invalidated. Do not continue to another cohort or retire the legacy path until
the named authority re-plans or accepts an explicit exception.

Report:

- target slices and route/ownership state;
- old and target behavior evidence;
- asset and knowledge dispositions;
- data migration and reconciliation results;
- temporary architecture still present;
- old paths actually retired;
- checks actually executed; and
- owner decisions, external coordination, or evidence still required.

## Guardrails

- Do not equate a new façade with migrated ownership.
- Do not pursue exhaustive feature parity before delivering target outcomes.
- Do not let fallbacks, feature flags, dual writes, or deprecated schemas
  survive without extinction gates.
- Do not route user-visible writes through shadow execution.
- Do not accept the old output automatically when differential results differ.
- Do not declare a path retired while traffic, data ownership, fallback, or a
  forbidden dependency remains.
- Do not infer transition, data, contraction, or deletion authority from
  implementation access or target acceptance.
- Do not change instruction-policy files unless the relevant owner explicitly
  authorized that exact named-file change.
