# Go/GoCD: monotonic replacement on mainline

Source: Jez Humble, [Make Large Scale Changes Incrementally with Branch By
Abstraction](https://continuousdelivery.com/2011/05/make-large-scale-changes-incrementally-with-branch-by-abstraction/),
2011-05-05.

## Observed case

The Go continuous-integration product was migrating database access from
iBatis to Hibernate and UI pages from Java-oriented stacks to JRuby on Rails
while continuing new feature work and frequent mainline integration.

For persistence, repository classes provided a seam that hid the implementation
from services. New database calls used the target style, old calls moved as
needed, and the team proposed failing a build if the count of old-style queries
increased. For UI, new or substantially changed pages used the target stack;
URI routing switched callers when a replacement page was ready, after which
the old page was removed. Both UI stacks shared the service layer during
coexistence.

## Rebuild Labs interpretation

| Model question | Case evidence |
| --- | --- |
| Mode | Incremental architectural replacement |
| Seams | Repository layer for persistence; URI/servlet routing for pages |
| Slice | One repository responsibility or one page route |
| Monotonic signal | Old-style query use could only decrease |
| Coexistence | Old and new suppliers behind stable service-facing boundaries |
| Retirement | Old page removed when its URI moved; final abstraction removable after full replacement |

The case shows how an executable negative rule can prevent new work from
reinforcing a superseded path. It also shows that a useful seam may already
exist in one area and need different routing in another.

## Transferable practices

- Identify the smallest existing boundary that keeps callers independent of a
  supplier.
- Make all new work target-native so the old surface cannot grow.
- Track a monotonic legacy count or dependency rule in CI when it expresses a
  durable migration goal.
- Switch one observable route, then remove its old implementation.
- Remove transition abstractions after they stop serving a target contract.

## Limits

The source is a participant account, not a controlled comparison. The product
already had useful seams, and some legacy pages remained at publication. A
count rule should target semantically obsolete use, not freeze incidental text
or incentivize disguising legacy dependencies.
