# Stripe subscriptions: incremental rebuild of live data ownership

Source: Stripe, [Online migrations at
scale](https://stripe.com/blog/online-migrations), 2017-02-02.

## Observed case

Stripe changed a subscriptions data model after growing beyond an earlier
one-subscription-per-customer assumption. The service had hundreds of millions
of objects and needed continued availability and accurate data.

The published sequence created the new storage, gradually enabled dual writes,
backfilled older objects using offline discovery and distributed work, checked
for missing data, moved read paths, moved write paths, and finally removed
dependence on the outdated representation. Operational metrics and staged
ramp-up limited load risk.

## Rebuild Labs interpretation

| Model question | Case evidence |
| --- | --- |
| Direction gap | A one-subscription-per-customer cardinality assumption and co-located storage no longer fit product behavior. |
| Continuity | API availability and data accuracy remained required. |
| Construction and transition | Evolve in place through staged expand, migrate, and contract phases |
| Controlled migration surfaces | Application read/write paths and old/new storage representations |
| Temporary architecture | Dual writes and two synchronized representations |
| Verification | Gradual dual-write metrics, offline missing-ID audit, [Scientist](https://github.com/github/scientist/blob/504a396e987f655a21c6bf2ed57935aadaa40859/README.md) production read comparison, and an explicit error on obsolete-field access |
| Retirement | Old-data dependence removed after reads and writes moved |

The case demonstrates why code and data transition cannot share one simple
rollback story. During coexistence, ownership and repair for partial writes
must be explicit, and removal is a distinct phase.

## Transferable practices

- Separate creation of target storage, backfill, read movement, write movement,
  and contraction.
- Ramp extra production work while observing capacity and latency.
- Make backfill restartable and run reconciliation after it appears complete.
- State the canonical source for each phase and how concurrent writes are
  handled.
- Remove the old representation only after target ownership is established.

## Limits

The article presents one successful migration and not every partial-failure
mechanism. Dual writing is not safe by default: target projects must define
idempotency, partial success, ordering, reconciliation, and recovery for their
stores. The specific batch tooling is not a general requirement.
