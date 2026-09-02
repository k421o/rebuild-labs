---
name: rebuild-incremental
description: Implement an explicitly authorized incremental architectural rebuild after a material direction change. Use when asked to migrate in stages, replace a legacy system slice by slice, use strangler or branch-by-abstraction techniques, preserve continuous operation, or execute an accepted incremental-rebuild plan. Do not use for assessment-only requests, compilation, disaster recovery, routine refactoring, or an isolated complete replacement; use rebuild-plan or rebuild-complete instead.
---

# Incremental project rebuild

Move an operating project toward its target architecture through explicit
seams and vertical slices. Make coexistence observable and bounded, and retire
the corresponding legacy path as part of every completed slice.

## Required planning source

Before implementation, read the sibling
[`rebuild-plan` skill](../rebuild-plan/SKILL.md) completely and read every file
in its [`references/`](../rebuild-plan/references/) directory. Use its target,
baseline, disposition, evidence, safety, and record behavior as the shared
source.

If no accepted rebuild packet exists, perform that planning workflow first.
Keep owner direction, external obligations, agent inference, implementation,
verification, cutover, and retirement in their distinct decision states.

## Authorization and preservation

- Confirm implementation is requested.
- Read applicable target instructions and inspect Git, dirty state, releases,
  consumers, data, deployments, and external ownership before mutation.
- Preserve unrelated work and use the isolation strategy required by the
  repository.
- Do not infer production routing, deployment, irreversible data migration,
  consumer cutover, or deletion authority from permission to edit code.
- State what rollback or forward recovery can actually restore before relying
  on it.

## Workflow

1. **Freeze target and continuity.** Record the target architecture,
   responsibilities, state ownership, dependency direction, forbidden
   inheritances, required compatibility, intentional divergence, acceptance,
   and retirement state.
2. **Map observed flows.** Pin current evidence and inventory callers, routes,
   protocols, jobs, identities, data stores, writes, ownership transitions,
   observability, and recovery paths. Map behavior, not only file structure.
3. **Select one seam.** Choose a bounded routing, interface, repository, event,
   command, page, file-format, consumer, or data-access boundary with observable
   input/output, controllable selection, and a credible removal path. Reject a
   seam that makes the target permanently depend on the rejected model.
4. **Define one vertical slice.** Name the target outcome, consumers and data,
   admitted assets, required continuity, intentional changes, coexistence
   contract, acceptance evidence, stop signals, temporary artifacts, recovery
   scope, and old-path retirement condition.
5. **Make the target own the contract.** Introduce a target-facing abstraction
   or route, adapt legacy concepts at the boundary, and keep old behavior stable
   through a separately verified preparatory step. Avoid a “neutral” union of
   every old and new concept.
6. **Implement the target path.** Build the complete slice using target
   boundaries. Apply the asset re-entry gate. Add target-fitness and negative
   legacy-dependency checks before increasing its responsibility.
7. **Expand and observe.** When needed, expand APIs or schemas so both paths can
   work temporarily. Use shadow execution, comparison, canaries, cohort
   routing, or carefully designed dual operations according to risk. Normalize
   nondeterminism and protect side effects, privacy, latency, and capacity.
8. **Migrate bounded ownership.** Move one caller, cohort, request class, or
   data partition at a time. For data, record canonical ownership, backfill,
   concurrent writes, restartability, reconciliation, and recovery. Treat old
   mismatches as observations to classify, not automatic target truth.
9. **Verify the route.** Exercise target acceptance, required continuity,
   intentional differences, architecture fitness, data invariants, operational
   health, and the stated stop or recovery path. Record the actual observation
   window and traffic; absence of alerts alone is not proof.
10. **Contract and extinguish.** After explicit acceptance, stop old traffic and
    writes, remove fallback, compatibility surface, adapters, flags, dual
    operations, obsolete schemas, code, tests, and transition-only monitoring.
    Record legacy absence and the next slice.

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

## Completion behavior

A slice completes only when the target path serves its accepted scope, the old
path no longer receives that traffic or owns that state, and transition-only
artifacts are removed or explicitly retained by decision. A project completes
when all planned slices meet that condition or remaining legacy islands are
accepted as the current architecture.

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
- Do not change instruction-policy files unless the relevant owner explicitly
  authorized that exact named-file change.
