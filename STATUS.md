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
**2026-11-05**. **434 registered claims.**

| Registered state | Claims |
|---|---:|
| proved | 350 |
| verification-pending | 17 |
| conditional | 24 |
| open | 42 |
| refuted | 1 |
| **Total** | **434** |

“Proved” reports the project registry at its stated scope, not
external refereeing. The complete per-claim surface is the generated
[`record/claim_registry.md`](record/claim_registry.md).

## Claims by family and state

| Family | proved | verification-pending | conditional | open | refuted | Total |
|---|---:|---:|---:|---:|---:|---:|
| BGS | 0 | 0 | 0 | 1 | 0 | 1 |
| CAYLEY | 9 | 1 | 0 | 1 | 0 | 11 |
| CUE | 2 | 0 | 0 | 0 | 0 | 2 |
| FLOW | 25 | 0 | 0 | 0 | 0 | 25 |
| FM | 35 | 0 | 2 | 0 | 0 | 37 |
| FORMAL | 3 | 0 | 0 | 0 | 0 | 3 |
| FUP | 1 | 0 | 0 | 0 | 0 | 1 |
| INFO | 0 | 0 | 0 | 1 | 0 | 1 |
| LOOP | 0 | 0 | 1 | 0 | 0 | 1 |
| RES | 20 | 1 | 1 | 1 | 0 | 23 |
| RET | 3 | 0 | 1 | 0 | 0 | 4 |
| TRACE | 252 | 15 | 19 | 38 | 1 | 325 |
| **Total** | 350 | 17 | 24 | 42 | 1 | **434** |

## Open programme obligations

42 registered claims are open. Their closure
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
| `BGS-TRACE-180` | Fixed-eta (nu-only) central limit law | [mathematics/fixed-map/derandomized_fixed_kick.md](mathematics/fixed-map/derandomized_fixed_kick.md) |
| `BGS-TRACE-181` | Non-degeneracy ND_m for composite h_m and for even m | [mathematics/fixed-map/derandomized_fixed_kick.md](mathematics/fixed-map/derandomized_fixed_kick.md) |
| `BGS-TRACE-182` | The (m, eta) = (11, 2) outlier | [mathematics/fixed-map/derandomized_fixed_kick.md](mathematics/fixed-map/derandomized_fixed_kick.md) |
| `BGS-TRACE-189` | Line E E7: m = 15 prediction versus outcome (k1 kick, eta = 2) | [mathematics/fixed-map/resonant_residue_lineE.md](mathematics/fixed-map/resonant_residue_lineE.md) |
| `BGS-TRACE-190` | Line E E8: Line B kick, giant traces at N == -/+196 mod h_m when 3 does not divide m | [mathematics/fixed-map/resonant_residue_lineE.md](mathematics/fixed-map/resonant_residue_lineE.md) |
| `BGS-TRACE-191` | Line E E9: eta-interval (not grid) certification of the resonant growth | [mathematics/fixed-map/resonant_residue_lineE.md](mathematics/fixed-map/resonant_residue_lineE.md) |
| `BGS-TRACE-192` | Line E E10: the TRACE-182 (m, eta) = (11, 2) outlier is the +-196 resonance | [mathematics/fixed-map/resonant_residue_lineE.md](mathematics/fixed-map/resonant_residue_lineE.md) |
| `BGS-TRACE-202` | Line F F6: float growth window eta in (0.951, 3.212) for the k1 sector-4 eigenvalue | [mathematics/fixed-map/lifted_transfer_lineF.md](mathematics/fixed-map/lifted_transfer_lineF.md) |
| `BGS-TRACE-205` | Line G classification record: resonant families, growth rates, G5 (h_d \| h_m), G6 (sparsity), G7 (moment heuristic), eta-scan | [mathematics/fixed-map/resonance_classification_lineG.md](mathematics/fixed-map/resonance_classification_lineG.md) |
| `BGS-TRACE-206` | Line G: Conjecture R' (corrected mean law for the k1 kick at eta = 2) with a pre-registered m = 17 test | [mathematics/fixed-map/resonance_classification_lineG.md](mathematics/fixed-map/resonance_classification_lineG.md) |
| `BGS-TRACE-210` | Conjecture R_NSW: W~rest_m(eta) = o(m) along m with h_m prime | [mathematics/fixed-map/derandomized_fixed_kick.md](mathematics/fixed-map/derandomized_fixed_kick.md) |
| `BGS-TRACE-220` | Line I: Conjecture R'_A (amended mean law with actual dilation-member values) for the k1 kick at eta = 2 | [mathematics/fixed-map/lineI_rprime_reduction.md](mathematics/fixed-map/lineI_rprime_reduction.md) |
| `BGS-TRACE-232` | Line J3 hypothesis H-natural: the conductor-not-in-{1,7} part O-natural_m does not cancel the d = 7 term on infinitely many m in S+ | [mathematics/fixed-map/lineJ_d7_twisted_coefficient.md](mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) |
| `BGS-TRACE-233` | Line J3 hypothesis H_arg: arg(xi_2:1)/2 pi is irrational | [mathematics/fixed-map/lineJ_d7_twisted_coefficient.md](mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) |
| `BGS-TRACE-239` | Line K hypothesis H-natural_mid: for some delta > 0 and infinitely many m in S+, O-natural_m^{<L} >= -(1 - delta) 0.98 (K_j/2) xi_lo^m | [mathematics/fixed-map/lineK_harg_removal.md](mathematics/fixed-map/lineK_harg_removal.md) |
| `BGS-TRACE-247` | Line K Conjecture C1: for the true twisted operator families, lim_k (I_k^F)^{1/k} = 1 | [mathematics/fixed-map/lineK_harg_removal.md](mathematics/fixed-map/lineK_harg_removal.md) |
| `BGS-TRACE-256` | Line L2 hypothesis H_mean: for some delta > 0 and infinitely many m in S+, \|D_iso(q) - E_b(q)/q\| <= ((1 - delta) target)^m at every open prime level q, with the analogue at open composite levels | [mathematics/fixed-map/lineL_op_open_range.md](mathematics/fixed-map/lineL_op_open_range.md) |
| `BGS-TRACE-274` | Line M M4c (open): the (+-2,16) inclusion rule degenerates (no borderline level) for m >~ 85 | [mathematics/fixed-map/lineMN_conductor_structure.md](mathematics/fixed-map/lineMN_conductor_structure.md) |
| `BGS-TRACE-276` | Line M M6 (open, conditional on C1-C4): the +-rho pairing law at all levels (cross_+ + cross_- = 2 Re sum_{a,b} conj(c_a z_a) c_b y_b (1 + s_a s_b)) | [mathematics/fixed-map/lineMN_conductor_structure.md](mathematics/fixed-map/lineMN_conductor_structure.md) |
| `BGS-TRACE-282` | Line N (open [H]): Theorem W for composite conductors c \| h_{3p} with c <= p^C (at least two prime factors >= 2p + 1) via Bourgain's finite-ring theorem | [mathematics/fixed-map/lineMN_conductor_structure.md](mathematics/fixed-map/lineMN_conductor_structure.md) |
| `BGS-TRACE-287` | Line N2 Omega-hypothesis (open): for infinitely many m in S+ with m >= m1 and every family F, the beta-weighted pressure sum Omega^F_m(k,a) is <= e^{o(m)} ((1 - delta) T_F)^m for some fixed k, a, delta > 0 | [mathematics/fixed-map/lineN2N4_inherited_level.md](mathematics/fixed-map/lineN2N4_inherited_level.md) |
| `BGS-TRACE-298` | Line N3/N4 open item: the isotropic part at q \| h_p (and at the mixed levels 7q), i.e. a bound \|D_q + D_qbar\| <= ((1 - delta) T)^m for the isotropic lines at every prime q \| h_p, together with composite d \| h_p having an isotropic prime component | [mathematics/fixed-map/lineN2N4_inherited_level.md](mathematics/fixed-map/lineN2N4_inherited_level.md) |
| `BGS-TRACE-300` | Line N hypothesis H1 (open [H]): collision lemma - lattice-to-collision reduction for shell sums with constant C <= 0.082 at J0 = 12, plus the A_bad tail j > 12 | [mathematics/fixed-map/lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-301` | Line N hypothesis H3 (open): Kotecky-Preiss polymer weight e^{a\|gamma\|} with a = 5.93e-6 at g0 = 4 (log -> modulus), finite part certified, tail j > 12 = H1 | [mathematics/fixed-map/lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-303` | Line N hypothesis H5 (open): composite h_p - (a) mixed classes (R-mix) E_{mixed,d} F_p <= e^{o(p)} d^c r_2^p with c < 0.387 uniformly in d \| h_p; (b) the 2^omega - 2 cross lines; (c) partially isotropic points; or p in P = {h_p prime} | [mathematics/fixed-map/lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-304` | Line N hypothesis H6 (open): inputs of Theorem C' - an explicit p0 and squarefreeness of h_p (or conductor-q^a weights) | [mathematics/fixed-map/lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-305` | Line N hypothesis H7* (open): for included levels d not in {h_p} u {e h_p}, d < L_fl = h_p^{1+o(1)}: \|Lin_d\| <= eps_d \|Z_rho\|^2/h_p with sum eps_d <= kappa0, i.e. cross-correlation growth < T' = 1.42785; needed even for prime h_p | [mathematics/fixed-map/lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-306` | Line N hypothesis H8 (open): deep wrap-around points of gap (a) at composite h_p - free if per-point weights are not d-amplified, otherwise need c < 1.1718 l0 / ln d (= 0.6647 l0 / log_lambda d) | [mathematics/fixed-map/lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-336` | Line N hypothesis H1, re-scoped by N20 (open [H]): (H1-bad) bad-cluster (polymer-restricted) joint (A,B) second moment on the eps-chain, sum_{bad, shell j} \|r_A r_B\|^2 <= C 2^{j(1 - beta(0.28))} for j > J0 = 12 with C <= 0.082, plus (H1-ali) the near-collision/box constants | [mathematics/fixed-map/lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |

## Corrections

Errata registry schema `bgs-errata-v1`; updated
**2026-11-01**; **65 registered entries**.
The status authority for corrections is
`record/retractions.md`; the generated reader-facing index
is [`ERRATA.md`](ERRATA.md).

## Registry integration record

Epoch record schema `bgs-follow-on-claim-epoch-v1`, base epoch
`2026-10-07-wave3`, reviewed **2026-10-29**.
It records 331 follow-on claims adopted after
wave 3 and 93 historical claim
amendments admitted through the epoch amendment channel, and an
external-dependency extension of 29 external IDs.

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
