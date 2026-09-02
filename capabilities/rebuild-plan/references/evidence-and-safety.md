# Evidence, safety, and authority

## Evidence roles

Keep these sources distinct:

1. Current owner direction authorizes outcomes, allowed breaks, and acceptance
   within its scope.
2. Normative external contracts constrain the target.
3. Pinned code, tests, manifests, and executable observations establish current
   or historical behavior.
4. Operational records establish bounded production facts and failure lessons.
5. ADRs and history explain prior forces and decisions; superseded records do
   not remain current because code still implements them.
6. patterns and case studies suggest techniques; they do not select a target
   project's mode.
7. Agent analysis remains a hypothesis until the relevant owner decides.

Tests written beside a change can validly verify an accepted contract. Passing
them cannot prove that the contract was required. Conversely, historical tests
are not automatically authoritative merely because they predate the pivot.

## Repository safety

Before mutation:

- read the nearest applicable instructions;
- inspect branch, status, remotes, worktrees, submodules, large-file handling,
  generated files, and repository owner;
- preserve unrelated and uncommitted work;
- identify exact source and target revisions;
- prefer an isolated worktree or repository-native equivalent; and
- avoid destructive reset, clean, checkout, force-push, history rewrite, or
  broad recursive deletion unless the user explicitly authorizes the exact
  operation and target.

“Rewind” always creates a new isolated line at a pinned ref. It does not mutate
the line being studied.

## External-state safety

Inventory data stores, queues, object storage, caches with authority, secrets,
deployments, scheduled jobs, users, downstream clients, and platform
configuration before claiming a reversible transition.

Deployment, public release, production traffic changes, irreversible schema or
data mutation, account changes, consumer cutover, and old-system deletion need
the target owner's authority. A request to implement code does not silently
authorize those actions.

State exactly what “rollback” can restore. After target-only writes or external
consumer changes, forward recovery or compensation may be more realistic than
returning to an earlier binary.

## Verification layers

- **Target fitness:** changed outcomes and boundaries work end to end.
- **Required continuity:** specifically accepted old contracts remain valid.
- **Intentional divergence:** removed or changed behavior differs deliberately.
- **Architecture fitness:** target ownership and dependency direction hold;
  forbidden legacy paths are absent.
- **Operational fitness:** build, deploy, observe, migrate, recover, and support
  behavior match the stated environment.
- **Transition fitness:** consumers and data can move with bounded coexistence
  and a credible retirement path.

Report only commands and checks that the current task actually executed. Pin
revisions, environment, configuration, and important limitations where a
result depends on them.

## Rebuild record states

Use: observation, hypothesis, owner-ratified direction, planned rebuild,
implemented slice, verified slice, cut over, retired, and superseded. Automated
checks can support verification; they cannot ratify direction, authorize
cutover, or accept retirement on behalf of the owner.
