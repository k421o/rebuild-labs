# Direction-change rebuilding source companion

Collected: **2026-09-02**

This record describes why each source was selected and the bounded claim it
can support. Links are live locators; consequential use should pin an archived
copy or exact repository revision when custody and licensing allow it.

## Replacement and displacement patterns

| Source | Role | Supported use | Limitation |
| --- | --- | --- | --- |
| Martin Fowler, [Sacrificial Architecture](https://martinfowler.com/bliki/SacrificialArchitecture.html), 2014-10-20 | Primary pattern essay | Architecture suited to early learning or one scale can be intentionally replaced later; modularity supports replacement. | Illustrative cases, not a comparative success study; cautions that newcomer dislike is weak evidence and distributed designs add complexity. |
| Martin Fowler, [Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html), 2024-08-22 | Primary pattern account | Outcome-first gradual displacement through seams, small parts, coexistence, and organizational change. | Does not make gradual replacement easy or universally applicable. |
| Ian Cartwright, Rob Horn, and James Lewis, [Patterns of Legacy Displacement](https://martinfowler.com/articles/patterns-legacy-displacement/), revised 2024-03-05 | Practitioner synthesis | Technology-first, feature-parity, and non-decommissioning traps; break work into outcome-bearing parts. | Experience report rather than controlled research; legacy displacement is broader than direction-change rebuilding. |
| Thoughtworks, [Transitional Architecture](https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html), 2022-03-28 | Primary pattern catalog entry | Temporary routers, mimics, repositories, and replicated state can reduce transition risk when their removal is designed. | Transitional structures can become permanent and must be funded and owned. |
| Martin Fowler, [Branch By Abstraction](https://martinfowler.com/bliki/BranchByAbstraction.html), 2014-01-07 | Primary pattern essay | Put an abstraction around a changing subsystem, build the replacement, move clients, and remove old implementation. | Requires a useful seam and carries coexistence cost. |
| Jez Humble, [Make Large Scale Changes Incrementally with Branch By Abstraction](https://continuousdelivery.com/2011/05/make-large-scale-changes-incrementally-with-branch-by-abstraction/), 2011-05-05 | Participant account and technique | Go/GoCD persistence and UI migrations show mainline change, existing seams, monotonic checks, URI routing, and old-page removal. | Tool and organization context may not transfer; some legacy pages remained at publication. |
| Martin Fowler, [Parallel Change](https://martinfowler.com/bliki/ParallelChange.html), 2014-05-13 | Primary pattern essay | Expand, migrate, and contract interfaces or schemas so consumers move without one coordinated release. | Complexity remains until contract/removal finishes. |

## Behavioral and migration evidence

| Source | Role | Supported use | Limitation |
| --- | --- | --- | --- |
| Michael Feathers, [Working Effectively with Legacy Code](https://www.pearson.com/en-us/subject-catalog/p/working-effectively-with-legacy-code/P200000008984/9780131177055), 2004 | Primary book publisher record and established method | Characterization tests create feedback around observed behavior before change. | The publisher page alone does not reproduce the method; observed behavior can still be undesirable. |
| Jest, [Snapshot Testing](https://jestjs.io/docs/snapshot-testing) | Official tool documentation | Captured output can expose regressions and reviewed changes. | Snapshots are easy to approve mechanically and can encode nondeterminism or obsolete output. |
| GitHub, [Scientist](https://github.com/github/scientist/blob/main/README.md) | First-party open-source implementation | Run control and candidate code, return the control, compare cleaned or custom results, ramp experiments, and publish mismatches. | Duplicate candidate work affects cost and latency; side effects and concurrent state need special handling. |
| Stripe, [Online migrations at scale](https://stripe.com/blog/online-migrations), 2017-02-02 | First-party engineering case | Dual write, backfill, migrate reads, migrate writes, reconcile, and remove old state while staying online. | One Stripe data-model migration; dual writes introduce risks that must not be copied uncritically. |

## First-party rebuild cases

| Source | Role | Supported use | Limitation |
| --- | --- | --- | --- |
| Meta, [React 16: an API-compatible rewrite](https://engineering.fb.com/2017/09/26/web/react-16-a-look-inside-an-api-compatible-rewrite-of-our-frontend-ui-library/), 2017-09-26 | First-party engineering case | Complete internal rewrite beside old code, public-API test reuse, implementation-coupled test revision, monotonic progress, dogfooding, and staged rollout. | React intentionally prioritized API parity; not every direction change should. |
| GitHub, [A brief history of code search](https://github.blog/engineering/a-brief-history-of-code-search-at-github/), 2021-12-15 | First-party historical case | Prior solutions and failed constraints informed explicit goals for a custom code-search engine and a research prototype. | Narrative written during preview; product and architecture continued evolving. |
| GitHub, [The technology behind GitHub's new code search](https://github.blog/engineering/the-technology-behind-githubs-new-code-search/), 2023-02-06 | First-party technical case | Domain-specific UX, query semantics, scale, and resource constraints justified a Rust implementation built from scratch and tested through preview/beta. | Bounded subsystem at exceptional scale; not evidence for whole-project rewrites. |

## Decisions, agents, and source preservation

| Source | Role | Supported use | Limitation |
| --- | --- | --- | --- |
| Michael Nygard, [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), 2011-11-15 | Originating ADR proposal and experience report | Small records preserve context, decision, status, and consequences; longer-term rearchitecture intent can avoid obstructive current choices. | Early practitioner report; record use still depends on maintenance and accessibility. |
| Rashmini Ramesh, [Research, Review, Rebuild](https://martinfowler.com/articles/research-review-rebuild.html), 2025-08-27 | First-person agent-assisted migration case | Reverse engineer behavior, have domain experts classify what survives, then rebuild against explicit scenarios and target conventions. | One healthcare UI modernization, with author-reported outcomes and domain-specific constraints. |
| Birgitta Böckeler et al., [Context Anchoring](https://martinfowler.com/articles/reduce-friction-ai/context-anchoring.html), 2026-03-17 | Practitioner agent-workflow pattern | A living decision/status document carries constraints, rejected alternatives, open questions, and implementation state across agent sessions. | Experience-based pattern; overhead is not justified for every short task. |
| Git project, [`git-worktree`](https://git-scm.com/docs/git-worktree), [`git-tag`](https://git-scm.com/docs/git-tag), and [`git-bundle`](https://git-scm.com/docs/git-bundle) | Official version-control documentation | Multiple worktrees, immutable tag identities, and portable reachable Git objects support non-destructive historical baselines. | Git does not automatically preserve untracked files, secrets, hooks, all configuration, deployments, or external state. |
| W3C, [PROV Overview](https://www.w3.org/TR/prov-overview/), 2013-04-30 | Web standard overview | Entities, activities, agents, and derivation relationships provide vocabulary for tracing transferred assets. | General model; does not select rebuild direction or guarantee truthful records. |

## Interpretation boundary

The central Rebuild Labs rules—four baselines, target-first inspection, dual
implementation/knowledge dispositions, target-native verticals, forbidden
inheritance checks, and explicit extinction gates—are a synthesis across these
sources and the motivating owner request. They are hypotheses owned here, not
quotes or requirements imposed by the source authors.
