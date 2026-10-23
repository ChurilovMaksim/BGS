# Programme status

This file is generated from `record/claims.json`, `record/errata.json`
and `record/claim_integration_epochs.json` by
`computations/maintenance/render_status.py`. Do not edit it by hand.

It is the single current-status page of the programme, and it is a
navigation surface, not a status authority. Registered statuses are
controlled by [`record/claims.json`](record/claims.json); see
[`SOURCE_OF_TRUTH.md`](SOURCE_OF_TRUTH.md) for how disagreements
between surfaces are resolved. The dated narrative of status changes
and scope is [`record/claim_ledger.md`](record/claim_ledger.md).

## Registered claims

Registry schema `bgs-claims-v1`; registry updated
**2026-10-22**. **197 registered claims.**

| Registered state | Claims |
|---|---:|
| proved | 171 |
| verification-pending | 12 |
| conditional | 9 |
| open | 5 |
| **Total** | **197** |

“Proved” reports the project registry at its stated scope, not
external refereeing. The complete per-claim surface is the generated
[`record/claim_registry.md`](record/claim_registry.md).

## Claims by family and state

| Family | proved | verification-pending | conditional | open | Total |
|---|---:|---:|---:|---:|---:|
| BGS | 0 | 0 | 0 | 1 | 1 |
| CAYLEY | 8 | 1 | 0 | 1 | 10 |
| CUE | 2 | 0 | 0 | 0 | 2 |
| FLOW | 25 | 0 | 0 | 0 | 25 |
| FM | 34 | 0 | 2 | 0 | 36 |
| FORMAL | 3 | 0 | 0 | 0 | 3 |
| FUP | 1 | 0 | 0 | 0 | 1 |
| INFO | 0 | 0 | 0 | 1 | 1 |
| LOOP | 0 | 0 | 1 | 0 | 1 |
| RES | 20 | 1 | 1 | 1 | 23 |
| RET | 3 | 0 | 1 | 0 | 4 |
| TRACE | 75 | 10 | 4 | 1 | 90 |
| **Total** | 171 | 12 | 9 | 5 | **197** |

## Open programme obligations

5 registered claims are open. Their closure
conditions are registered per claim in `record/claims.json` and
rendered in full in the [claim registry](record/claim_registry.md).

| Claim | Title | Authoritative source |
|---|---|---|
| `BGS-BGS-001` | Fixed-strength microscopic BGS universality for the maintained frozen map | [mathematics/fixed_map_resolvent_frontier.md](mathematics/fixed_map_resolvent_frontier.md) |
| `BGS-CAYLEY-005` | Sharp centered pointwise Cayley energy target | [mathematics/open_questions.md](mathematics/open_questions.md) |
| `BGS-INFO-001` | Full vanishing-noise tomography transition | [mathematics/open_questions.md](mathematics/open_questions.md) |
| `BGS-RES-003` | All-members analytic resonance nondegeneracy | [mathematics/open_questions.md](mathematics/open_questions.md) |
| `BGS-TRACE-005` | Model-specific signed Heisenberg-scale desymmetrized joint-trace estimate | [mathematics/open_questions.md](mathematics/open_questions.md) |

## Corrections

Errata registry schema `bgs-errata-v1`; updated
**2026-10-22**; **59 registered entries**.
The status authority for corrections is
`record/retractions.md`; the generated reader-facing index
is [`ERRATA.md`](ERRATA.md).

## Registry integration record

Epoch record schema `bgs-follow-on-claim-epoch-v1`, base epoch
`2026-10-07-wave3`, reviewed **2026-10-23**.
It records 94 follow-on claims adopted after
wave 3 and 67 historical claim
amendments admitted through the epoch amendment channel, and an
external-dependency extension of 18 external IDs.

## Reading the status surfaces

- [Source of truth](SOURCE_OF_TRUTH.md) — the authority order for
  resolving disagreements between surfaces.
- [Claim ledger](record/claim_ledger.md) — dated narrative of
  status changes and evidentiary scope.
- [Claim registry](record/claim_registry.md) — the complete
  generated per-claim view of the registry.
- [Theorem families and their limits](mathematics/results.md) —
  analytical index of the theorem families, with generated
  registry family tables.
- [Open questions](mathematics/open_questions.md) — the maintained
  open-problem surface.
- [Corpus atlas](docs/corpus_atlas.md) — generated navigation
  over the whole corpus.
