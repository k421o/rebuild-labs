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

The left input authorizes the destination. The right input constrains factual
claims about the system. Neither alone decides how to rebuild it.

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
- source, evidence, compatibility, and target baselines;
- asset units and disposition decisions;
- rebuild record states and supersession;
- safety, authority, and verification boundaries; and
- criteria for selecting complete rebuild, incremental rebuild, ordinary
  refactor, defer, or further investigation.

The complete module owns the protocol for an isolated new implementation line.
It can begin from an empty tree, the beginning of the project, or a selected
stable revision. The old tree remains an evidence source and salvage quarry,
not the implicit skeleton.

The incremental module owns the protocol for replacing behavior through seams
and vertical slices while old and new paths coexist. It requires explicit
routing, compatibility, observation, and retirement conditions so “temporary”
dual architecture does not become permanent.

The modules may share a target charter, baseline record, disposition ledger,
and verification matrix. A project may switch modes or use both at different
boundaries, but the record must say which unit each decision covers.

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
2. Draft the target charter in implementation-neutral terms.
3. Record known external contracts and acceptance conditions.
4. Inspect repository topology, Git state, releases, data boundaries, and
   operational surfaces.
5. Inspect implementation details to test the charter, find constraints, and
   classify assets.
6. Amend the charter when new evidence reveals a real constraint, recording
   the source and decision rather than silently conforming to existing code.

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
