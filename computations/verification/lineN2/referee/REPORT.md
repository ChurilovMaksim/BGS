# Referee report: Line N2 (/workspace/bgs-lineN/N2)

Referee: Grok Bot. Date: 2026-10-31, Asia/Yekaterinburg (UTC+5). I only read the repo and its clones, and I pushed nothing.
Compared against: main e4042ef2 (`record/claims.json`, TRACE-198, 206, 236–268) and my Line N report (`/workspace/audit/lineN/REPORT.md`).

## Verdict: **READY-after-fixes (N2-F1 … N2-F9)**

- **Theorems A, B and C, Prop E, and the barriers are sound.** Theorems A, B and C hold as implications, modulo the standing inputs. Prop E [CA] reproduces independently to 1e-12. The barriers in (d) are correct and are stated as method barriers.
- **One real gap sits in the conditional part.** It is the representation used for Λ (N2-F1). It does not touch any unconditional claim.
- **Numeric claims need tightening.** The [N] Λ value is a sampled *lower* estimate of a supremum. The (21,239) level split has now finished, and it contradicts one sentence of the report.
- **No merged claim is contradicted.** Nothing in main needs amending because of N2. The amendments to TRACE-246 and 258 come from N3 (my Line N report) and still stand.

## Independent checks
Scripts are in `code/` and their output is in `logs/`.

| Check | Result |
|---|---|
| A^p − I = h_p·B with det B = −4, all primes p ≤ 61 (`ref_n2.py`) | ✔ index 4. Lean `idx3`, `idx5` |
| **Prop E, independent arb certificate** (`ref_e_cert.py`): a *left* Collatz–Wielandt vector, AM=50 with its own Bessel tail bound, J1=20, C_pair and weights rebuilt from the TRACE-249/250 statements | r_2(4000) ≤ **1.05290115** (8V), 1.05192335 (8E), 1.05345567 (16V), 1.05292016 (16E). These match the author to ≤1e-11 and sit marginally *below* them (more exact boundary letters). ✔ |
| Exactness of the 441-state box | (i) Enlarging the box to E0=12 (625 states) gives the *identical* R. (ii) Raising V=40→48 changes R by 1e-13. (iii) BFS in an E0=30 box: the states that are both forward-reachable from (0,0) and co-reachable to it have max carry 9 ≤ ⌊V/4⌋=10. Green sum = 1/4 (Lean `green_quarter`). ✔ |
| C_pair at k=4000 vs the Line L final_op_cert (k=15) | 25.83170843406 vs 25.83170843453 (k-dependence only) ✔ |
| 1.0644, 1.428, 1.4923, 2.617 | μ*/λ^{1/3}=1.06437; μ*/λ^{1/6}=1.42786; μ*²/ξ_lo=1.49227=λ^{0.2271}; λ/1.49227²=2.6173 ✔ |
| Thresholds T³/r_2 | 2.00859 / 2.01046 / 3.04126 / 3.04280 ✔. Rates: (1.98242·r_2)^{1/3}=1.27799; (μ*·r_2)^{1/3}=1.26344 (margin 1.57%) ✔ |
| G, T·λ^{1/3} | Σ\|J_n(1.8)\| = 2.3693986 (= TRACE-260); T·λ^{1/3} = 2.3100 ✔ |
| Endpoints | 3 log μ* − log λ = 0.1871; 3 log T = 0.7490; log 1.26278 = 0.2333 < 0.2497 ✔ |
| μ*·T vs ξ_lo | 2.458680 < 2.458689 ✔ (needed in Theorem A step 2) |
| Author manifest SHA256_N2.txt | all 34 entries OK |
| Lean (`lean/LineN2Arith.lean`, v4.33.1, `decide +kernel`/`norm_num`, no `native_decide`) | Index identities p=3,5; Green 1/4; threshold, conditional-rate and free-k=24 inequalities; slow-orbit 1.0644. Compiles clean (`logs/lean.log`) |

## Item by item

**Theorem A [P as an implication].**
- The chain works: W2′ with clamp, then |Z_ρ| ≤ Cμ^m with μT_F ≤ ξ_lo, then Ω, then the open part is o(ξ_lo^m), so H♮_mid (TRACE-239) holds, and Theorem K (TRACE-240) gives R′ false.
- This is exactly the weighted form of the TRACE-246 proof route.
- The J3 weights are those of TRACE-237. All q | h_m split because h_m² − 2k_m² = −1. So the isotropic-line description is right.
- Non-triviality holds.
  - At c = h_p, β = 1 contributes ≈ p·4λ^{−p}·μ*^{3p}, which is 1.0644^m < T^m ✔.
  - **Stronger:** at *any* conductor, a slow N3 segment of length 2·log_λ c costs (μ*/T)^6/λ² = 0.325 per unit of log_λ c for rank p, and 0.066 for rank 3p. Both are < 1. So N3 slow orbits never violate the hypothesis at any level; worth stating (N2-F5).
- Needed wording: see N2-F3 and N2-F4 below.

**Theorem B [P given TRACE-266].**
- The Fourier/cyclic-path identity is correct, since the average over (1/h)Z²/Z² detects Σ(Aᵀ)^i k_i ∈ hZ².
- The Bowen-ball lemma is correct.
  - Distinct points of Fix(A^p) are (p,ε)-separated for ε below the expansivity constant.
  - Bowen balls have volume ≍ ε²λ^{−(p+k)}, where the extra +k comes from the k-step look-ahead of φ.
  - |G_p| = h_p² ≍ λ^p/4.
- Gap: TRACE-266 is registered for *prime* q with r(q) = p ("if r(q) = ord_q(λ) = p"). Theorem B uses it at the composite c = h_p. The cyclicity proof does not use primality, but the registry statement does not cover composite levels (N2-F2).

**Theorem C [P mod O1 (TRACE-249/250), Bowen, TRACE-266].** The steps check out.
1. |Tr(J M³)| ≤ ‖J‖‖M‖_op‖M‖²_HS.
2. HS norms are submultiplicative. The geometric mean over k shifts costs only constants.
3. max(a², f_k) ≤ a + f_k for a ≤ 1.
4. Hölder over residue classes plus T-invariance.
5. The integral equals a sum over exact concatenated collisions (TRACE-248), majorised via |c_γ| ≤ C_pair·Σ Πρ_i (TRACE-250).
6. Gap: **Λ must be the op-norm in the same Hilbert space as the O1 HS bounds**, i.e. the lattice-lifted spaces with ρ = 0.75, β = 0.25 for 8V, etc. The text says "computed in *any* valid representation (e.g. Line F lifted K0=4, ρ=1.2, β=2.5)". The trace inequality needs one common space. Changing representations needs an intertwining lemma: bounded restriction R and a smoothing first step L̃ with ‖M^{O1}‖ ≤ ‖R‖‖P^{F}_{p−1}‖‖L̃‖, where the constants are independent of p. That lemma is not given (N2-F1). The [N] Λ values were computed in the Line F lift, which is truncated (K0 = 3), so they are not yet even numerically about the right object.

**Proposition E [P structure + CA]: confirmed and rerun independently** (table above).
- The structural steps hold: ρ̂ = |û|² ≥ 0; the pointwise majorant g_i with tail ε_i; the carry bound |e_j| ≤ V/4 via the Green kernel; and Collatz–Wielandt with ⟨0|B^Q|0⟩ ≤ R^Q.
- One minor point: the author's Perron vector has entries clipped at 1e-200. That is still rigorous (any x > 0 works), but say so.

**Conditional rate 1.2780 (Λ only [N]).** The arithmetic is right, (1.98242·1.0529012)^{1/3} = 1.27799 < 1.28359, and the label "[P+CA, conditional on Λ]" is right. But:
- (i) 1.98242 comes from sampling plus local refinement, which only gives a **lower** bound on sup_y. The claim "Λ ≤ 2.0085" is not even numerically established; it is "no point found above". Label it so (N2-F6).
- (ii) The margin is thin. The k′=20 value 2.01677 and the free-family k=24 maximum 2.01382 both **exceed** the 8V threshold 2.00859 (Lean `free24`). So any certificate needs k′ ≳ 30. On the free route, it must beat the boundary transients with a margin of ≤ 1.3%.
- (iii) The 16-family Λ (< 3.04) was not computed, but the corollary needs it.
- (iv) N2-F1 (representation) applies here.

**(d) Barrier: a barrier for the method only, and stated as such ✔.**
- Each item is labelled a method barrier: "the method loses the subgroup index", "the pressure method does not handle them", and "obstruction ... methodological, not observed".
- The [P] content is a lower bound on *the majorant*, not on the true sums:
  - **Isotropic lines:** the weight is ≈ 1/q and the Bowen majorant includes the μ* ball, so the majorant ≥ (μ*/λ^{1/6})^m = 1.428^m. For q < h_p the bound is worse.
  - **K_p and rank-3p levels:** the index ≥ λ^m/L_m², which gives a factor 2.617 per m. With clamp a = 1 the Lebesgue integral is ≥ 1, so the majorant is ≥ 2.617^m > T^m.
- Wording fix: write "[P] (lower bound for the pressure majorant)" in §5 and in the ledger (§6 currently says only "[P] … the barriers"), and state the a = 1 clamp used for the 2.617 lower bound (N2-F7).
- The barrier is consistent with TRACE-260 (phase-blind barrier, same G) and TRACE-264 (Gauss-side 1.8808^m above L_m).

**Level-split numerics (now finished).** `logs/d_level_split.jsonl` now contains (m,q) = (21,239):
- unit-part rate 1.1342, isotropic-part rate **1.1604**;
- max single unit-point rate 1.5616, max single isotropic-point rate **1.2780**.

So at (21,239) the isotropic part *is* the larger one. §5's "The isotropic part is not numerically worse" is false as written, and the table row still says "pending" (N2-F8). Both parts remain below T = 1.28359, so no conclusion changes. But the isotropic barrier may not be purely methodological; mark that as [N] with no trend claim.

## Consistency with main e4042ef2 and with Line N
- **TRACE-240 (Theorem K) is `conditional` in main.** Theorem A therefore yields "R′ false" only under its own Ω hypothesis. Register Theorem A as a *proved implication* (like TRACE-257) plus a new open hypothesis, not as a refutation. The report's §0 row says this correctly ("whether the hypothesis can be verified").
- **TRACE-246 / 258.** N2 adopts N3, which says K2′'s conclusion is true for p ≥ p₀ (effective, not computed). The amendments I proposed in the Line N report (replace the "[H] covers all or most m") stand. N2 adds nothing that contradicts TRACE-246's [P] statement.
- **TRACE-256 (H_mean), 266, 267, 268.** These are compatible. On TRACE-268 (Lemma E), the β = 1 excursions at h_p have length ≈ p − O(t), within its bound log_λ(264ε²h_p²)+1 = p + O(1), which is consistent.
- **TRACE-198.** N2 §2 follows my N-F2 (per-family ρ(L₀^F) ≥ μ*). Its §1.3 places μ* at twist ½ in sector 0, i.e. untwisted in sector 4, and says the E family and the other sectors have ρ < 1. So "per family" must mean "for the family F that carries μ*". TRACE-246/258 need only *some* F, so this is fine; say it explicitly (N2-F4).
- **Line N report.** Index 4 is adopted, N-F1/N-F2 are incorporated, and t_F ≈ 40 is labelled [H]. ✔ Theorem A is the "β-weighted target" that my report recommended in place of L §6.

## Fixes
- **N2-F1 (substantive, conditional part only).** Theorem C needs Λ computed in the O1 (lattice-lifted ρ/β) space. Otherwise, add an intertwining lemma with p-independent constants. Delete "in any valid representation". Note that the existing [N] Λ values are in the truncated Line F lift.
- **N2-F2.** Theorem B uses TRACE-266 at the composite level h_p. Either extend TRACE-266's statement to any c with ord_c λ = p (the proof is unchanged), or cite it as "[P, TRACE-266 proof]".
- **N2-F3.** Theorem A should say "m ≥ m₁ (TRACE-245)". It should also name the Weil-range and composite-below-c_W·p² levels as covered by TRACE-245 and by the TRACE-246 definition of "open", matching TRACE-239's O♮^{<L}.
- **N2-F4.** State the family explicitly. The N3 lower bound uses the family F that carries μ* (TRACE-198); Theorem A needs the *upper* bound μ_F·T_F ≤ ξ_lo for every F, with 16-family μ_F ≤ 1.6677 per TRACE-253.
- **N2-F5.** Extend the non-triviality remark to all conductors: the slow-segment factor is 0.325 for rank p and 0.066 for rank 3p, both < 1.
- **N2-F6.** Λ [N] is a sampled lower estimate of a supremum. Say that the k′=20 and free k=24 values exceed the threshold. List the 16-family Λ as missing in the corollary's hypothesis.
- **N2-F7.** The barriers are lower bounds for the method's majorant. Say so in §5 and §6, and state the a = 1 clamp used for 2.617.
- **N2-F8.** Fill in the (21,239) row (1.1342 / 1.1604 / 1.5616 / 1.2780). Delete "isotropic part not numerically worse". Add `d_level_split.jsonl` to the manifest.
- **N2-F9 (unit weights).** |W| ≤ 2^{ω(h_p)}/h_p² assumes h_p is squarefree (J3 weights are stated for q ∥ h). Either state the prime-power weights (TRACE-246's "open" includes prime powers) or assume squarefreeness explicitly. Note 2^{ω} = e^{O(p/log p)}.

## Suggested registry states
| Item | State |
|---|---|
| Index-4 identity (A^p − I = h_p B, det B = −4) | proved (+ Lean for small p; general via lam_pow_eq) |
| Theorem A | proved implication ("Ω-hypothesis ⇒ H♮_mid ⇒ R′ false", like TRACE-257); its Ω-hypothesis = new **open** item |
| Theorem B (exact form, Fourier form, Bowen lemma) | proved (after N2-F2) |
| Theorem C | proved mod standing inputs (after N2-F1 wording) |
| Proposition E | proved [P] + [CA] (certificate independently reproduced) |
| Conditional corollary (rate ≤ 1.2780 at h_p, unit points) | conditional on Λ (open; [N] evidence only, lower-bound type) |
| (d) barriers | proved, as statements about the pressure majorant (not about the sums) |
| Level split | numerical |

## Cheap Lean targets
- **Done:** see `lean/LineN2Arith.lean`.
- **General `A^p − 1 = h_p·B` with det B = −4.** Proof route: Tr(A^p) = λ^p + λ^{−p}, so 2 − Tr = −4h_p²; reuse Line M lam_pow_eq.
- **The carry lemma** |e_j| ≤ ⌊V/4⌋ for finite E with (X²−6X+1)E = v: as a finite statement for a bounded box it is decidable, and as an ℓ¹ convolution bound it is a short real-analysis proof.
- **Collatz–Wielandt** (Bx ≤ Rx, x > 0 ⇒ ⟨0|B^Q|0⟩ ≤ R^Q) for nonnegative matrices: short and general.
- **Rational constants:** r_2 thresholds and 0.325 < 1.
