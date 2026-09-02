# Current owner direction

Decision state: owner-ratified for this exercise.

The released report-rendering library must now produce CSV as well as JSON.
The existing `register_renderer` extension boundary, row model, Python runtime,
and library delivery remain current. JSON output remains a supported contract.

The owner wants CSV implemented as another renderer with its own tests. No
state ownership, persistence, deployment, trust boundary, or dependency
direction changes. There are no consumers or data to migrate between old and
new implementations.
