# Domain-first architecture

Rebuild Labs keeps research, shared rebuild contracts, guides, evaluations,
canonical capabilities, and generated products in one repository while they
share a lifecycle. Colocation does not make every artifact authoritative.

## Authority flow

```text
Target owner direction                    Pinned system evidence
          |                                        |
          +----------------+-----------------------+
                           v
          Target-architecture hypothesis / contract
                           |
                           v
                 Rebuild domain model
          direction gap / baselines / dispositions
                           |
             +-------------+-------------+
             |                           |
             v                           v
       Human playbooks             Evaluation cases
             |                           |
             +-------------+-------------+
                           v
                Canonical capabilities
                           |
                           v
                 Generated host adapters
```

The left input authorizes outcomes and constraints. The right input constrains
factual claims about the system. The architecture between them is a proposal
until the target project's authority accepts it; acceptance still does not
authorize implementation, cutover, data mutation, or deletion.

## Artifact classes

| Class | Purpose | Authority |
| --- | --- | --- |
| Research record | Interpret sources and cases with limitations. | Evidence and hypothesis only. |
| Domain contract | Define shared terms, record roles, dispositions, and invariants. | Canonical for Rebuild Labs vocabulary, not for a target architecture. |
| Guide | Explain how to apply a module in human-readable form. | Practical synthesis; target owners still choose direction and acceptance. |
| Evaluation case | Expose a discriminating behavior or failure mode. | Test evidence only; fixtures do not become universal rules. |
| Canonical capability | Project an evaluated user job into agent instructions. | Editable agent behavior for this domain. |
| Product adapter | Package pinned capabilities for a host. | Mechanical distribution only. |
| Target rebuild record | Record a particular project's direction, decisions, evidence, and state. | Owned by the target repository, never by this repository. |

## Shared core and two modules

The shared core owns:

- target-direction and architectural-discontinuity vocabulary;
- direction-contract, architecture-hypothesis, and authorization states;
- source, evidence, compatibility, and target baselines;
- asset units and disposition decisions;
- rebuild record states and supersession;
- safety, authority, and verification boundaries; and
- criteria for proceeding, deferring, or investigating and, when proceeding,
  selecting no rebuild or rebuild plus independent construction and transition
  strategies.

The complete module owns target-native construction on an isolated new line.
It can begin from an empty tree, the beginning of the project, or a selected
stable revision. The old tree remains an evidence source and salvage quarry,
not the implicit skeleton.

For the `rebuild` change class, the incremental module owns evolve-in-place
construction and staged transition through seams and vertical slices while old
and new paths coexist. It requires explicit routing, compatibility,
observation, action-local authority, and retirement conditions so “temporary”
dual architecture does not become permanent. Staged delivery of ordinary
no-rebuild work does not enter this module automatically.

The modules share a direction contract, architecture record, baselines,
disposition ledger, and verification matrix. A unit may use the complete module
to construct a target-native core and the incremental module to transition to
it in stages. The record names change class, construction, and transition per
unit instead of hiding this composition behind one “mode.”

## Dependency rules

1. Owner direction and normative obligations constrain the rebuild model.
2. Current code and history inform dispositions; they do not define the target
   merely by existing.
3. Research may challenge the domain model but cannot silently change a
   capability's released interface.
4. Guides derive from the current domain contracts.
5. Capabilities derive from domain contracts, guides, and evaluated evidence.
6. Products are generated from an explicit capability allowlist and never
   become editable forks.
7. A target repository consumes a pinned capability but owns every local
   rebuild decision and artifact.

## Target inspection order

Inspection order affects agent anchoring. The default sequence is:

1. Read applicable owner instructions and the explicit direction-change
   request.
2. Draft the direction contract in implementation-neutral terms.
3. Record known external contracts and acceptance conditions.
4. Propose target responsibilities and dependency direction as an explicitly
   authored architecture hypothesis.
5. Inspect repository topology, Git state, releases, data boundaries, and
   operational surfaces.
6. Inspect implementation details to test the direction and hypothesis, find
   constraints, and classify assets.
7. Amend the direction only through its authority; revise or accept the
   architecture through its own decision state. Record the evidence rather
   than silently conforming either artifact to existing code.

This is not a ban on reading code. It is a way to keep code discovery from
quietly rewriting the owner's target before the difference is visible.

## Repository growth

The bootstrap begins as a domain module with guides, research, narrow
evaluation cases, and experimental canonical capabilities. It does not copy
README Labs' mature ingestion yard, corpus, artifact catalog, experiment
library, or release history.

Add a boundary when repeated work demonstrates it:

- add a versioned schema when multiple records need stable interchange;
- add a runner when one scenario can be executed without exposing its oracle;
- add a corpus when bounded comparative claims require a sampling method;
- add candidate intake when external methods need reproducible comparison;
- add another product only when a real host requires a distinct adapter; and
- extract shared infrastructure only after an independent domain proves the
  interface.
