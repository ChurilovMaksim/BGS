# Referee report: Line N5 (the slow isotropic family at q = h_p)
Referee: Grok Bot. Date 2026-10-31, about 20:40 Asia/Yekaterinburg (UTC+5).
- Inputs: /workspace/bgs-lineN/N5. Read-only; SHA256_N5.txt verifies.
- Registry: main e4042ef2, record/claims.json, extracted to logs/claims_e4042ef2.json.
- Everything I wrote is under /workspace/audit/lineN5. Nothing was pushed.

## Verdict: NOT READY (major revision, N5-F1..F10)
**Sign error.**
- N5 states Ẑ(½,…,½) = +Z_ρ(1+O(θ^p)). In fact Ẑ(½,…,½) = **−Z_ρ**(1+O(θ^p)).
- N5's own d_excursion.py and c_true.py compare **moduli only**, which is how the sign was missed.
- Consequence: the 16D=1 family has Ẑ_β/Z_ρ = c*·e^{+0.518i} for ρ = (2,8) and c*·e^{−0.518i} for (−2,8).
- So Re > 0, not < 0. The family's cross part at level h_p is **positive**.

**The headline conclusions (§0 "Reassessment", §4) are therefore inverted.**
- The aliased family is not an obstruction to refuting R′. It is a new positive driver toward refutation, exponentially larger than the d = 7 term D7.
- The mathematics itself (Lemma H, the family, c*, the rate μ*λ^{−1/6}) checks out, with the sign corrected.

## 1. The bookkeeping question (frozen R′)
**Answer: the family is genuinely part of the deviation, not of the frozen main term. Nothing cancels it.**

- **What the frozen main term is.** In TRACE-206, Res_m = φ⁻¹Σ_ρ[(|Z_ρ|²−RMT) + Σ_{d incl.} n_d(|Z_ρ|²/d² − RMT)]. This is a fixed formula in |Z_ρ|, d and n_d only.
- **Which part of each member it captures.** By TRACE-212 (I2′), each member at level d is Z_t = q⁻²Σ_β Ẑ(β)G_t(β) = ω_t Z_ρ/d + Δ_t:
  - the main-term value |Z_ρ|²/d² is exactly the β = 0 (trivial-character) part;
  - every β ≠ 0 sits in Δ_t.
- **Where the β ≠ 0 parts go.** TRACE-213 gives W′ = W′_A + φ⁻¹Σ Dev_d(ρ), with Dev_d = Σ_{M_d}(|Z_ν|² − |Z_ρ|²/d²). TRACE-231(1) (with TRACE-237/255) then splits Dev into:
  - a cross part, which is O♮ for conductor ∉ {1, 7};
  - a square part, which is Q_m ≥ 0.
- **Where the family sits.** The 16D = 1 family consists of isotropic β ≠ 0 of conductor q = h_p.
- **Level d = h_p is included for m = 3p.** h_p ≈ λ^{m/6} ≤ √h_m, and |Z_ρ|²/h_p² ≥ 4m.
- **So the family contributes:**
  - D_q = q⁻¹Σ_{l(q)∖0}Ẑ_β, which enters O♮;
  - the squares |Δ_t|², which enter Q_m.
- **No double counting.**
  - Member sets are pairwise disjoint (TRACE-213).
  - The frozen levels are odd d | h; "level 4" is not a level.
  - The "¼-character" is ρ's own primary: Ẑ(½…½) = −Z_ρ, because e(Σn_i/2) = e(N(α_n)/2) shifts ν₀ → ν₀ + h.
  - TRACE-218's Möbius aliasing concerns non-unit residues, not member sets.
- **Exact form.** For a prime level, Z_t = ω_t Z_ρ(1+X)/q + (non-isotropic part), where X = Σ_{β iso ≠ 0} Ẑ_β/Z_ρ. The isotropic Gauss factor is G_t(β) = G_t(0) when N(β) ≡ 0.
  - So the frozen law under-predicts every member at level h_p by the factor |1+X|².
  - Dev_{h_p} = (q−2)|Z_ρ|²/q²·(2Re X + |X|²) plus a non-negative square term, minus an O(|Z_ρ|Σ_noniso|Ẑ|/q²) cross term.
- **Checks of this decomposition.**
  - `ref_i2_conv.py`: brute force at m = 5 confirms the pipeline to 4e-14.
  - At m = 21 the family cross part predicted from X_fam is 1.4825e7; the exact value is 14,824,825.9.

## 2. Independent computations (code/, logs/)
| item | result |
|---|---|
| exact Dev at q = h_p, p = 5 (m = 15) and p = 7 (m = 21), full Ẑ arrays, own I2′ pipeline | Dev/main = +0.153 and +0.281. Cross parts: fam +1.72e4, iso_rest −5.2e3, noniso +3.7e4 (p = 5); fam +1.48e7, iso_rest +1.1e6, noniso +1.6e6 (p = 7). Total cross is **positive**; square parts dominate at these small q |
| family phase | arg(Ẑ_fam/Z₀) = +0.718 (p = 5), +0.511 (7), +0.518 (19, 29, 47); −0.518 for the (−2,8) sign |
| Ẑ(½…½)/Z₀ | −1.0000003 (p = 7); −1 ± 1e-16 (p = 19, 29, 47). N5's d_excursion gives arg((r_A r_B)³) = −2.6236, so −(r_A r_B)³ has arg +0.518, consistent |
| complete isotropic line sums by depth class (`ref_depth_sum.py`) | Reproduces the exact p = 7 X (all 476 points) to all digits. X = Σ_{both lines}Ẑ/Z₀ = 4p·c*·e^{0.5175i}·(1+3e-4): p = 19: 0.030064; 29: 0.045882; 47: 0.074347. Depth classes 16D = 7, 9, 17, 23, 25, … contribute < 0.1%, and both lines are equal |
| generic isotropic points, p = 19, 300 random line points | max \|Ẑ/Z₀\| = 5e-12, median 1e-19. Monte Carlo bound on the generic part of X: ≤ 1.4e-6 (vs 0.030) |
| mixed classes at 7·h_p and 457·h_p (p = 19) | \|Ẑ/Z₀\| ≤ 4.4e-12 and 6e-18. So these levels carry only the inherited positive copies (TRACE-228, A′ ≈ 1.10) |
| other open levels (rank-3p primes) | iso parts in W′/m units: d = 457: 2e-11; d = 14593: −5e-11 (p = 19); d = 13921: −2e-16 (p = 29) |
| **h_p levels in W′/m units** (both ρ, ×A′, iso-coherent part, `ref_wprime_size.py`) | **m = 57: +2.95; m = 87: +125; m = 141: +1.07e5**. For comparison, the D7 scale 1.0184^m/m is 0.050, 0.056, 0.093, and the floor from W′_A is ≥ −4 |
| truncation (`ref_trunc.py`) | (L, K) = (6,24), (8,32), (10,40) agree to 1e-6 in \|ratio\| and 1e-6 in arg. twlaw breaks down at (12,48) (ρ grows with L): a tool caveat |
| c* | 3.95452e-4 reproduced (p = 19, both signs) |

## 3. Does it refute R′ along m = 3p?
**Numerically: yes, strongly. Rigorously: no.**
- **The numerics.** W′_m/m ≥ −4 + φ⁻¹(A_mX7 + X16 + Q_m + O♮)/m. Here:
  - Q_m ≥ 0;
  - the h_p-level iso deviation alone gives +3, +125 and +1.1e5 at m = 57, 87, 141, growing like (μ*²λ^{−1/6}/λ^{1/2})^m = 1.1329^m;
  - every other piece I could compute is smaller by more than 10 orders of magnitude.
- **So, if the transfer-law numerics are right,** frozen R′ fails along m = 3p with h_p prime, at least from p = 29 on. S+ is not needed, because D7 is negligible next to this term.
- **Rigorous form (proposed, [P] given the inputs listed).** For m = 3p with h_p squarefree, frozen R′ forces Σ_{levels d with h_p ∤ d} cross_d ≤ −(F_m − 4m·φ) + o(·), where F_m := Σ_ρ Σ_{e} (n_e/e²)·Dev_{h_p}(ρ) > 0.
- **This is a much stronger dichotomy than Corollary K3.**
  - The budget is 2.735^m instead of ξ_lo^m, so the per-level rate target relaxes from T = 1.28359 to μ*λ^{−1/6} = 1.4279 for (±2,8), and to about 1.64 for (±2,16).
  - Theorem C′ unit-point rates (1.274, 0.803, 1.458, 0.778; N4 [CA]) already meet the relaxed target.
- **What is missing for a proof:**
  1. A [CA] lower bound for F_m, uniform in p:
     - write out Prop X's θ^p errors and the analytic continuation of Φ to radius ρ + 0.83;
     - certify c* and the phase in arb;
     - show Re(−(r_A r_B)³) > 0 rigorously;
     - give a one-sided relative bound on the non-family isotropic and non-isotropic cross terms at h_p.
  2. A one-sided bound on the other open levels' isotropic cross parts against the relaxed target. These are the generic isotropic points at levels ≠ h_p (rank-3p primes, proper divisors of h_p) plus composite mixed classes. Numerically they are negligible, but this is not proved.
  3. Infinitely many p with h_p squarefree (or the family argument without squarefreeness), and K_p-levels as before.
- **Registry consequence.** H_mean (TRACE-256) is **numerically false** at q = h_p for h_p prime, p ≥ 19: |D_iso| has rate 1.4279 > T. TRACE-257 is therefore vacuous along those m.
- **H-natural and H-natural_mid (TRACE-232, 239)** are one-sided lower bounds. The h_p term is positive, so it does not violate them; it supports them.

## 4. Other N5 claims
- **Lemma H [P] ✓.** ε^p + ε′^p = 2h_p and ε′^p = −ε^{−p}, so 2h_pδ ∈ ½O ⊂ O^∨. It holds for **all** δ with 4qδ ∈ O, isotropic or not, and at every level q | h_m with p → m.
  - N4 §3 really is superseded: there are two windows per period, not one of length p/2.
  - So **N4's remainder rates 1.2426/1.0672/0.9165 and the "G ≤ 1.547" target must be withdrawn**. Correct my N4 registry rows.
  - The gauge lemma and the 16D = 1 identification in N4 stand.
- **Prop X: [P-sketch] ✓ with the sign fix.** The correct statement is Ẑ_β = −(r_A r_B)³ Z_ρ (1+O(θ^p)). The "1e-14 match" is a match of moduli.
- **c* = 3.9545e-4 [N] ✓.** The rate μ*λ^{−1/6} = 1.42785 ✓ (N5 writes 1.42775). The cross rate is μ*²λ^{−1/6} = 2.7350 (N5: 2.7348).
- **7·h_p unit points.** I accept them as [P mod the Theorem C inputs], with one constant to state: the support of ν lies on the 1/(7h_p) lattice, so the Bowen-ball spacing loses a p-independent factor 7.
  - Checks: 7 ∤ h_p for p > 3; v₇(h_{3p}) = 1 for p ≠ 7 (2 at p = 7); there are 36 unit β₇, and Σ|W₇| ≤ 72/49 < 2.
- **Composite h_p [N]:** plausible. I did not recheck it.

## 5. Fixes
- **N5-F1 (major).** Correct the sign everywhere: Ẑ(½…½) = −Z_ρ; Prop X gets a minus sign; arg = ±0.518 and Re > 0. Phase checks must go into d_excursion.py and c_true.py.
- **N5-F2 (major).** Rewrite §0 rows 3 and 5 and §4. The family is part of the deviation (O♮ cross plus Q_m square). It is positive and exponentially dominant, which gives a refutation route with a relaxed target, not an obstruction. Add the bookkeeping argument of §1.
- **N5-F3.** Add the depth-class completeness (X = 4pc*e^{0.518i}(1+O(1e-3))) and the generic-point bound.
- **N5-F4.** Annotate H_mean (TRACE-256) as numerically false at q = h_p (p ≥ 19, h_p prime).
- **N5-F5.** State explicitly that N4 §3.3 (remainder rates, G target) is withdrawn.
- **N5-F6.** List the missing estimates in Prop X: uniform rank-one errors, and the continuation radius ρ + 0.83.
- **N5-F7.** 7·h_p: state the spacing constant.
- **N5-F8.** Fix the constants: 1.42785 and 2.7350 (with μ* = 1.9154712).
- **N5-F9.** Document the twlaw truncation range (L ≤ 10) and the instability at L = 12.
- **N5-F10.** §4 item 2 ("cancellation across levels containing h_p"): the levels containing h_p inherit **positive** multiples (TRACE-228), and the mixed classes are numerically negligible, so they cannot cancel it.

## 6. Registry states (proposed)
| claim | state |
|---|---|
| TRACE-206 frozen R′ | **open**. Annotation [N]: the level-h_p deviation gives W′/m ≈ +3, +125, +1.1e5 at m = 57, 87, 141 (h_p prime); this is strong numerical evidence of failure along m = 3p. Not a disproof |
| Lemma H (half-period identity) | proved |
| Prop X (closed form, sign corrected) | P-sketch |
| c*, phase ±0.518, X(p) = 4pc*e^{±0.518i} | numerical |
| Dichotomy: R′ forces the other open levels to cancel F_m (relaxed targets 1.4279 / ≈1.64) | proposed; register as proved only once F_m has a [CA] lower bound |
| TRACE-256 H_mean | open → annotate numerically false at q = h_p; TRACE-257 vacuous there |
| TRACE-232 and 239 | unchanged; the new term is positive |
| 7·h_p unit points | proved mod the Theorem C inputs (spacing constant stated) |
| N4 §3.3 remainder rates, G ≤ 1.547 | withdrawn (superseded by Lemma H) |
| N4 gauge lemma, 16D = 1 identification | proved (unchanged) |

## Files
- code: ref_i2_conv.py, ref_level_dev.py, ref_depth_sum.py, ref_line_sample.py, ref_mixed.py, ref_other_levels.py, ref_levels.py, ref_wprime_size.py, ref_trunc.py
- logs: the corresponding .json and .out files; claims_e4042ef2.json
- lean: LineN5Arith.lean (compiles): rate inequalities, and the Lemma H norm at p = 5
- SHA256.txt
