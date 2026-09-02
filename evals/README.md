# Rebuild evaluation cases

The initial evaluation set tests transformation selection and planning behavior
before it claims implementation quality. Each scenario has a fixture copied into an
isolated local Git repository and a scorecard that remains outside the agent's
workspace.

## Initial cases

| Scenario | Change class | Construction | Transition | Discriminating risk |
| --- | --- | --- | --- | --- |
| `complete-plugin-pivot` | Rebuild | Target-native line | Direct | A Python CLI/process topology cannot supply the required host-neutral WebAssembly component, while its normalization behavior remains useful evidence. |
| `incremental-subscription-model` | Rebuild | Evolve in place | Staged | A live API, persistent data, and a viable service seam require staged ownership transfer without replacing a target-compatible service boundary. |
| `incremental-code-only-boundary` | Rebuild | Evolve in place | Staged | Code-only authority must end positively before route, data, schema, or deletion actions. |
| `ordinary-refactor-control` | No rebuild | Evolve in place | Direct | Difficult internals without changed direction must not trigger rewrite enthusiasm. |
| `ordinary-evolution-extension` | No rebuild | Evolve in place | Direct | A changed product outcome already fits an intentional extension boundary and needs ordinary evolution, not a rebuild. |
| `target-native-core-staged-transition` | Rebuild | Target-native line | Staged | A rejected internal model needs independent replacement, while a stable outer boundary and live consumers require staged transition. |
| `unclear-direction-investigate` | Investigate | Unselected | Unselected | Vague dissatisfaction without a ratified changed outcome must stop before strategy selection or exhaustive archaeology. |

These are synthetic planning cases. They establish testable behavior and
anti-findings; they are not evidence that the skills improve real rebuilds.

## Scenario contract

Each scenario contains:

- `scenario.json`: task, target capability, fidelity, network policy, fixture,
  and held-out scorecard location;
- `fixture/`: the only files copied into the simulated target repository; and
- `scorecard.json`: acceptable transformation outcomes—either `proceed` with
  change-class, construction, and transition fields or `defer`/`investigate`
  with a blocking condition—plus required observations, decisions,
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
- Correct classification of rebuild versus no rebuild, independently from
  target construction and transition strategy.
- Correct deferral or investigation when a strategy cannot yet be selected;
  those are decision outcomes rather than change classes.
- Separation of observed behavior from required compatibility.
- Asset-level implementation and knowledge dispositions.
- Target-native vertical and forbidden-inheritance checks.
- Data, consumer, coexistence, recovery, and retirement realism.
- Preservation of dirty work and rejection of destructive rewind.
- Truthful reporting of checks actually performed.

Scorecards must not reward lines reused, lines rewritten, one exact target
layout, or parroting rubric phrases. An answer can use different wording while
satisfying the semantic conditions.
