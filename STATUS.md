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
**2026-10-30**. **280 registered claims.**

| Registered state | Claims |
|---|---:|
| proved | 229 |
| verification-pending | 15 |
| conditional | 15 |
| open | 21 |
| **Total** | **280** |

“Proved” reports the project registry at its stated scope, not
external refereeing. The complete per-claim surface is the generated
[`record/claim_registry.md`](record/claim_registry.md).

## Claims by family and state

| Family | proved | verification-pending | conditional | open | Total |
|---|---:|---:|---:|---:|---:|
| BGS | 0 | 0 | 0 | 1 | 1 |
| CAYLEY | 9 | 1 | 0 | 1 | 11 |
| CUE | 2 | 0 | 0 | 0 | 2 |
| FLOW | 25 | 0 | 0 | 0 | 25 |
| FM | 35 | 0 | 2 | 0 | 37 |
| FORMAL | 3 | 0 | 0 | 0 | 3 |
| FUP | 1 | 0 | 0 | 0 | 1 |
| INFO | 0 | 0 | 0 | 1 | 1 |
| LOOP | 0 | 0 | 1 | 0 | 1 |
| RES | 20 | 1 | 1 | 1 | 23 |
| RET | 3 | 0 | 1 | 0 | 4 |
| TRACE | 131 | 13 | 10 | 17 | 171 |
| **Total** | 229 | 15 | 15 | 21 | **280** |

## Open programme obligations

21 registered claims are open. Their closure
conditions are registered per claim in `record/claims.json` and
rendered in full in the [claim registry](record/claim_registry.md).

| Claim | Title | Authoritative source |
|---|---|---|
| `BGS-BGS-001` | Fixed-strength microscopic BGS universality for the maintained frozen map | [mathematics/fixed-map/fixed_map_resolvent_frontier.md](mathematics/fixed-map/fixed_map_resolvent_frontier.md) |
| `BGS-CAYLEY-005` | Sharp centered pointwise Cayley energy target | [mathematics/open_questions.md](mathematics/open_questions.md) |
| `BGS-INFO-001` | Full vanishing-noise tomography transition | [mathematics/open_questions.md](mathematics/open_questions.md) |
| `BGS-RES-003` | All-members analytic resonance nondegeneracy | [mathematics/open_questions.md](mathematics/open_questions.md) |
| `BGS-TRACE-005` | Model-specific signed Heisenberg-scale desymmetrized joint-trace estimate | [mathematics/open_questions.md](mathematics/open_questions.md) |
| `BGS-TRACE-136` | Free-with-parity revival law at even order (conjecture) | [mathematics/fixed-map/revival_closure_law.md](mathematics/fixed-map/revival_closure_law.md) |
| `BGS-TRACE-137` | Exponential revival law at odd order for generic dimensions (conjecture) | [mathematics/fixed-map/revival_closure_law.md](mathematics/fixed-map/revival_closure_law.md) |
| `BGS-TRACE-148` | Scaling-limit conjecture for the Haar diagonal-phase cat-map form factor | [mathematics/fixed-map/random_phase_encounter_pairs.md](mathematics/fixed-map/random_phase_encounter_pairs.md) |
| `BGS-TRACE-155` | B_m^sym < 2m for even m beyond the computed range | [mathematics/fixed-map/band_limited_kick_bridge.md](mathematics/fixed-map/band_limited_kick_bridge.md) |
| `BGS-TRACE-159` | 1/N coefficient for uniform phases (J0) at large eta | [mathematics/fixed-map/band_limited_kick_bridge.md](mathematics/fixed-map/band_limited_kick_bridge.md) |
| `BGS-TRACE-161` | Intermediate band K = kappa N | [mathematics/fixed-map/band_limited_kick_bridge.md](mathematics/fixed-map/band_limited_kick_bridge.md) |
| `BGS-TRACE-162` | Crossover conjecture: R-scaling of the band-limited deviation and the mode threshold | [mathematics/fixed-map/band_limited_kick_bridge.md](mathematics/fixed-map/band_limited_kick_bridge.md) |
| `BGS-TRACE-177` | Numerical observations: ND^(2) at small m, mu(eta) spectrum, m_* crossover, W~rest tables, fixed-eta CLT numerics, torsion-split numbers | [mathematics/fixed-map/derandomized_fixed_kick.md](mathematics/fixed-map/derandomized_fixed_kick.md) |
| `BGS-TRACE-179` | Conjecture R / R_NSW: W~rest_m(eta) = o(m) uniformly on compact eta-ranges | [mathematics/fixed-map/derandomized_fixed_kick.md](mathematics/fixed-map/derandomized_fixed_kick.md) |
| `BGS-TRACE-180` | Fixed-eta (nu-only) central limit law | [mathematics/fixed-map/derandomized_fixed_kick.md](mathematics/fixed-map/derandomized_fixed_kick.md) |
| `BGS-TRACE-181` | Non-degeneracy ND_m for composite h_m and for even m | [mathematics/fixed-map/derandomized_fixed_kick.md](mathematics/fixed-map/derandomized_fixed_kick.md) |
| `BGS-TRACE-182` | The (m, eta) = (11, 2) outlier | [mathematics/fixed-map/derandomized_fixed_kick.md](mathematics/fixed-map/derandomized_fixed_kick.md) |
| `BGS-TRACE-189` | Line E E7: m = 15 prediction versus outcome (k1 kick, eta = 2) | [mathematics/fixed-map/resonant_residue_lineE.md](mathematics/fixed-map/resonant_residue_lineE.md) |
| `BGS-TRACE-190` | Line E E8: Line B kick, giant traces at N == -/+196 mod h_m when 3 does not divide m | [mathematics/fixed-map/resonant_residue_lineE.md](mathematics/fixed-map/resonant_residue_lineE.md) |
| `BGS-TRACE-191` | Line E E9: eta-interval (not grid) certification of the resonant growth | [mathematics/fixed-map/resonant_residue_lineE.md](mathematics/fixed-map/resonant_residue_lineE.md) |
| `BGS-TRACE-192` | Line E E10: the TRACE-182 (m, eta) = (11, 2) outlier is the +-196 resonance | [mathematics/fixed-map/resonant_residue_lineE.md](mathematics/fixed-map/resonant_residue_lineE.md) |

## Corrections

Errata registry schema `bgs-errata-v1`; updated
**2026-10-30**; **64 registered entries**.
The status authority for corrections is
`record/retractions.md`; the generated reader-facing index
is [`ERRATA.md`](ERRATA.md).

## Registry integration record

Epoch record schema `bgs-follow-on-claim-epoch-v1`, base epoch
`2026-10-07-wave3`, reviewed **2026-10-29**.
It records 177 follow-on claims adopted after
wave 3 and 93 historical claim
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
