# Direction contract

Decision state: owner-ratified for this exercise.

Customers can now own many subscriptions. Subscriptions must become independent
domain records while the released `/v1/customers/{id}` representation remains
available through a compatibility adapter for six months.

The service receives writes continuously. Existing customer and subscription
identifiers must remain valid, and the API cannot take a maintenance window.
The internal JSON storage format is not a compatibility promise.

# Target architecture contract

Decision state: accepted for this exercise.

The existing service process, deployment unit, and API boundary remain the
target-owned boundary. Subscription records move behind that service's
data-access seam. A second subscription service is out of scope because it
would introduce distributed write coordination and duplicate identity
authority that the target rejects.

The owner must approve production routing, data backfill, write cutover, and
removal of the v1 adapter separately after reconciliation evidence is reviewed.
