# Referee report — Line N12 (adapted norm + interaction prefactor + N11_v2 fixes)
Referee: Grok Bot · completed 2026-11-01 (Asia/Yekaterinburg, UTC+5) · inputs SHA256_N12.txt verified OK · no author files modified, nothing pushed.
Companion: /workspace/audit/lineN11b/REPORT.md (Line N11b).

## Verdict: **READY after fixes** (required: F1, F2, F3; F4–F5 minor)
The core of the adapted-norm part (1) is independently confirmed. In fact my arb replay makes V1–V3 rigorous, which is stronger than the authors' [CA-float]. The interaction budget in (2) holds with a margin of about 600×, even after adding the referee's correction F1. Two things are not yet acceptable as written: the presentation of the gap<5 "reclassification" (F1), and the status of the G>16 tail (F2).

## Independent checks performed (code/, logs/)
| check | result |
|---|---|
| rerun `verify_adapted.py` (`logs/rerun_verify_adapted.out`) | ALL_OK. eig H ∈ [0.51958, 230.4646], cond 21.0609, V2 margin 2.0e-8 ≫ err 3.1e-10, V3b 0.10185 ≫ 5.3e-11, V4 core→true 2.09e-8 |
| **arb (prec 106) replay**, own code `ref_arb_adapted.py` (`logs/ref_arb_adapted.json`) | **all certified**. V2 ‖A0/s‖_H ≤ 1+1e-8; V3b off-dominant ≤ 0.45 (const 1); V3a; H ⪰ 0.7208² I; H ⪯ 15.1811² I ⇒ **cond ≤ 21.0615**. Method: exact arb residual R = c²H − X*HX, float Cholesky of mid R − σI, rigorous ‖R−σI−LL*‖_F < σ (E_F ≤ 8e-13 vs σ ≥ 1.2e-5). This is valid for the stored float H, Q̃, s and the Galerkin core A0; the far part/Pert stays at V4. |
| cache faithfulness (`ref_cache_check.json`) | a_ops cache = N6 cert_core: blocks max diff 0, RAD 8.0123e-20, weights identical, 477 blocks |
| **sector-shift identity**, verified independently | w_a(n) = iⁿJ_n(0.9η)·e(cc n²/2 + a n/8), and twist τ enters as e(nτ). So w_a(n)e(nτ) = w_4(n)e(n(τ+(a−4)/8)) identically, and the blocks M_n are sector-independent. Checked symbolically, in arb on all weights (True), and numerically on the operators. **The identity holds**, so one H serves all four slow twists b ↦ sector 4−8b. |
| stepnorm table (`ref_stepnorm.json`, own generalized-eig code) | matches the table to ≤ 2e-15 at 11 points; max N_H = 2.8756 at t = 0.1436; N_H(−t) = N_H(t) verified at 5 points; empirical quadratic coefficient near 0 ≈ 602 (claimed bound 3.19e3, consistent) |
| δ_int window model vs exact twisted sums (`ref_window_vs_exact.json`, 88 comparisons) | p=59: max |diff| ≤ 1.2e-5 ✓. p=37: diffs up to 0.18 only for g ≈ 14, where the circular gap wraps (k=18) onto the other core, i.e. the gap is short on the circle. The model is fine *provided gaps are measured circularly*. odd–odd n=8..16 ratios match (up to conjugation) |
| gap<5 reclassification (`ref_reclass*.json`) | **see F1** |
| M-tail rate (from authors' e_tailH G12 vs G16, 200 rows) | measured decay (M16/M12)^{1/4} = 0.3799–0.3800 per step, uniform over all rows |
| N8 provenance of p ≥ 1289 (N11_v2 F4) | `N8/logs/q_propx2_all.out` line 1: near0 p0 = 1289 ✓ |
| Lean (`lean/LineN12Arith.lean`, project `lean/proj`, mathlib cache) | builds, exit 0, no sorry/native_decide: cond bracket, cell add-on, quad edge, type counts 1550/1350/200, δ_int/ReΛ_lo′ < 8.26e-4, δ_int + 9.95e-7 < ReΛ_lo′/400, c16 charge = 200·|c16|, relabelling identity 4√2−2ε = 2ε⁻¹, plus N11b items |

## Findings
**N12-F1 (required): the "reclassification" hides genuine short-range types.** Of the 200 types with n = 2G+h < 5:
- only **31** are true relabellings, i.e. the merged pair equals a single coded element up to ±ε^k;
- **169 (95 distinct classes up to ±ε^k)** are new, uncoded short clusters: e = 12, 6, 8∓2√2, 8√2, 10∓2√2, 2±4√2, …;
- their total model weight is **≈ 9.95e-7, about 2× δ_int**.

So "relabelled singles, not an interaction" is false for 85% of them. These are exactly the N11-F1 short clusters. They are not interactions in the δ_int sense, but they are *types missing from the type list*.
Required: list them with certified activities as new single types, or carry them explicitly in (T). Also state that δ_int covers coded pairs only.
Effect on the budget: none. 5.14e-7 + 9.95e-7 < ReΛ_lo′/400 (Lean). But the claim as worded is wrong.

**N12-F2 (required): the tail beyond G0 = 16 remains [P-sketch].**
- K (Q̃ part) is ~1e-16.
- The whole tail is the rank-one mismatch M. M is measured at G0 (1e-6–1e-5) and *assumed* to decay like 0.45^m.
- Data support it: M decays at **0.380 per step**, uniformly. But this rate is the sub-dominant spectral ratio, **not** the λ⁻¹ = 0.172 twist-tail mechanism the REPORT invokes. The stated mechanism is inaccurate.
- Suggested route to a lemma: re-cut at the gap midpoint so that the mismatch becomes a Q̃-cross term, bounded by ‖wQ̃‖·‖Q̃v‖·0.45^m via the certified V3b (constant 1 in H, times cond ≤ 21.06 to return to the Euclidean norm).
- Any Lipschitz route instead needs the core-product prefactor ∏N_H (up to 2.88 per off-slow step), which must be explicit.
- Until then, label the 3.27e-12 tail [N]+[P].

**N12-F3 (required): label honesty.**
- (a) `verify_adapted.py` is [CA-float], not [CA]. The eigvalsh backward-error constant 10·D·u is heuristic, and the rounding in forming A0 (tensordot) is not in err. Both are negligible, and my arb replay now gives genuine [CA] for V1–V3, so cite it, or add an arb path.
- (b) The stepnorm table, Lip_H = 167.2, and the quadratic-bound constants (b1 = 32.71, c1 = 1.391, b2 = 12.49, L2 = 4977) are plain float with float T⁻¹ and no error terms. They are **[N]**, with a [P] argument for the quadratic structure, not "[CA-float table]".
- (c) Hence the D2 per-stay constant ~10² is [N]-dependent. The numbers are right; the labels overstate.

**N12-F4 (minor): bookkeeping.**
- Define δ_int per site precisely. The global-sign doubling is a possible factor 2, which is immaterial.
- `lambda_cert.py`: the docstring says c16 is charged "×10 = 2.2e-8 per sign pair", but the code subtracts 2·10·2.2e-8 = 4.4e-7 = 200·|c16|. This is conservative; fix the text.
- State explicitly that the window model uses circular gaps (cf. the p=37 wraparound).

**N12-F5 (minor): scope.** The D2 constant and the choice of cond-per-stay are honest. D1 (the cone certificate) is still open and should stay listed as such.

## N11_v2 fixes F1–F7 against my N11 report
- F1 (short clusters): addressed in N12 via the type list. But see N12-F1: this resolution is only partial until the 95 classes are carried.
- F2: ✓.
- F3: ✓.
- F4: ✓. p ≥ 1289 provenance spot-checked in N8.
- F5: ✓.
- F6: ✓.
- F7: correctly withdrawn ✓.

All are satisfactory, with N11-F1 carried forward as N12-F1.

## What remains for an unconditional refutation (updated)
1. **(T)**: certified activities for the uncoded short clusters (N12-F1) and the full type list; an arb replay of the 1350 coded types (δ_int is currently [N]).
2. **M-tail lemma** with explicit constants (N12-F2).
3. **D1 cone certificate**, and a rigorous version of the stepnorm/Lip/quadratic constants. These are cheap: an arb replay at 4096 points.
4. **(b′)** mixed/cross lines, and the N11b mixed-class bound, which is conditional on Γ_out < T′ (see N11b report).
5. **Short cores** (k = O(1) stays), the arithmetic input (C′, squarefree h_p), and the R₄ automaton.

None of these items is currently in danger numerically. Each is a proof or certification gap, not a failure of the estimate.
