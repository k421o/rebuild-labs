# Current owner direction

Decision state: owner-ratified for this exercise.

The released authorization service must replace its process-global role table
with a relationship-based policy engine. Relationships and resource ownership,
not roles, become the target's source of permission truth. The new core must be
buildable and testable without importing the legacy role engine.

The gateway request shape, boolean decision response, tenant identifiers,
resource identifiers, and continuous availability remain supported contracts.
The gateway can select an engine per tenant, so the owner requires comparison
and cohort rollout before retiring the role engine. Implementation, traffic
movement, policy-data movement, and retirement require separate approval.
