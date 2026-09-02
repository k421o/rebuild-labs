# React Fiber: complete construction, incremental exposure

Source: Meta, [React 16: A look inside a rewrite of our
frontend UI library](https://engineering.fb.com/2017/09/26/web/react-16-a-look-inside-an-api-compatible-rewrite-of-our-frontend-ui-library/),
2017-09-26.

## Observed case

Meta describes React 16 as a complete rewrite of React's internals with the
public API kept essentially stable. The new core was designed to support future
asynchronous rendering, although React 16 initially ran it in a synchronous
compatibility mode. It also enabled features that were difficult in the former
implementation.

The team developed the Fiber renderer beside the old renderer in the same
repository and selected the path at one entry point with a feature flag. It
used the existing Jest suite as a compatibility target because most tests
exercised public APIs. Tests tied to old implementation details were rewritten.
Passing-test progress was tracked monotonically, and the new path was exercised
against real components before full parity, first for small internal cohorts
and then more broadly. Dogfooding exposed previously undocumented lifecycle
ordering. The team sometimes preserved the behavior and sometimes repaired
brittle clients and documented the intentional break. Rollout also watched
product metrics, performance, and error logs, and an early regression caused an
experiment to be reset before continuing.

## Rebuild Labs interpretation

| Model question | Case evidence |
| --- | --- |
| Construction strategy | Complete internal architecture replacement |
| Transition strategy | Incremental coexistence, dogfooding, and rollout |
| Compatibility baseline | Public React API and behavior-oriented tests |
| Preserved continuity and validation surface | Public API, behavior-facing tests, real components, and ecosystem compatibility |
| Asset refactor | Tests that encoded old internals |
| Target fitness | New renderer capabilities plus production exercise |
| Temporary architecture | Old/new renderer switch at a single entry point |

The case shows why construction and transition strategies must be separate. It
also shows an asset-level test disposition: the suite was valuable, but tests
that made old implementation details authoritative needed change.

## Transferable practices

- Keep one controlled selection boundary between old and target paths.
- Track progress monotonically without treating raw rewritten lines as value.
- Reuse behavior-facing contracts while challenging white-box oracles.
- Exercise the target against realistic use before the compatibility suite is
  perfect.
- Roll out to bounded cohorts and use actual behavior to refine confidence.

## Limits

React's goal included broad API parity, so the case cannot justify parity for a
project whose owner wants intentional product changes. The published account
does not expose every cost, rollback event, or internal decision. A library
renderer also has different state-migration risks from a persistent service.
