# Rebuild evaluation cases

The initial evaluation set tests mode selection and planning behavior before it
claims implementation quality. Each scenario has a fixture copied into an
isolated local Git repository and a scorecard that remains outside the agent's
workspace.

## Initial cases

| Scenario | Expected decision | Discriminating risk |
| --- | --- | --- |
| `complete-plugin-pivot` | Complete rebuild | Current CLI/file-system topology should not define a new embedded library, while one pure behavior remains useful. |
| `incremental-subscription-model` | Incremental rebuild | A live API and persistent data require staged ownership transfer rather than an isolated big-bang replacement. |
| `ordinary-refactor-control` | Ordinary refactor | Difficult internals without changed direction must not trigger rewrite enthusiasm. |

These are synthetic planning cases. They establish testable behavior and
anti-findings; they are not evidence that the skills improve real rebuilds.

## Scenario contract

Each scenario contains:

- `scenario.json`: task, target capability, fidelity, network policy, fixture,
  and held-out scorecard location;
- `fixture/`: the only files copied into the simulated target repository; and
- `scorecard.json`: acceptable modes, required observations and decisions,
  anti-findings, and safety requirements kept outside the target.

Validate the records and materialize one local Git fixture with:

```console
uv run python scripts/validate_evals.py
uv run python scripts/materialize_eval.py \
  evals/scenarios/complete-plugin-pivot \
  /tmp/rebuild-labs-complete-plugin-pivot
```

The materializer refuses an existing destination, copies only `fixture/`, and
creates one baseline commit. It does not run an agent or score prose. A future
runner must launch the selected capability without exposing `scorecard.json`,
record model and prompt identity, and keep automatic matching advisory until
independent semantic review confirms target fidelity and anti-findings.

## Evaluation dimensions

- Intent fidelity and decision-state accuracy.
- Correct distinction among complete, incremental, combined, and ordinary
  refactor outcomes.
- Separation of observed behavior from required compatibility.
- Asset-level implementation and knowledge dispositions.
- Target-native vertical and forbidden-inheritance checks.
- Data, consumer, coexistence, recovery, and retirement realism.
- Preservation of dirty work and rejection of destructive rewind.
- Truthful reporting of checks actually performed.

Scorecards must not reward lines reused, lines rewritten, one exact target
layout, or parroting rubric phrases. An answer can use different wording while
satisfying the semantic conditions.
