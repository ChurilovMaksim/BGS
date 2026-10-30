# Referee report: Line H, H2 (49-state certificate for the Line B kick f_B, η = 2, s = −1)

Referee: independent adversarial audit, 2026-10-30, ~20:40 UTC+5. Object: `/workspace/bgs-lineH/REPORT.md` §2.1–2.5, plus NOTES.md, code/,
lean/LineH.lean, data/, logs/. I did not modify `/workspace/bgs-lineH`. All experiments are in `/workspace/audit/lineH/`
(code/, out/, logs/, hashes in `logs/SHA256_audit.txt`). Nothing was pushed. H1 (§1) is outside the scope of this audit.

## Verdict: **ACCEPT AFTER FIXES**

I found no mathematical error in the certification argument and no unsafe rounding that changes any decision.
* The main certificate (V_0: exactly one, simple, eigenvalue in |z| > 1.5, inside D(b₁₁, 0.05)) was **re-certified with my own code**.
  That code uses a more conservative rounding model and a different deflation error analysis: F·R₁ = 0.895, F·R₂ = 0.592 (author: 0.914, 0.624).
* E_0 was re-certified with my own code: F·R = 0.024 at R = 1.0.
* All other certificates and the whole all-m chain were re-decided in exact rational arithmetic from the stored bounds, with safe padding.
* bounds49 reproduces byte-identically. The trace check reproduces exactly.
* 120 Galerkin entries were recomputed by an independent method and agree to ≤ 2.3e−14.

Fixes 1–5 below are required before anything enters the repository. Most are wording or rounding fixes; fix 1 is about provenance. Fixes 6–10 are recommended.

## 1. What was checked and how

| Item | Method | Result |
|---|---|---|
| bounds49.py from stored inputs | rerun (`out/bounds49_rerun.json`) | byte-identical to `logs/bounds49_final.json` (sha 6d48e502…) |
| All certificates and the all-m chain, exact rationals | `code/ref_bounds.py`: Fractions; JSON floats padded up by 1e−12; arb strings used for V_0 N_j and rows_j | V_0 dom (R = 1.5, r₁ = 0.05): F₁ = 0.91352, F₂ = 0.62352. V_2/4/6 at R = 1.45: 0.7316 / 0.8408 / 0.7321. E_0..6 at R = 1: 0.0530 each. First admissible m = 47 (m = 43 fails). Table values reproduced. ε₅₉₉ ≤ 5.5e−51. g ≥ 1.412799, C ≥ 0.25 − 1e−50 |
| Independent V_0 dom certificate | `code/ref_rig.py` on `data/prodV_b0_{mid,rad}.npy` (mid Frobenius norm matches the build JSON, so these are the certified matrices). Constant √2·γ_{2n+2}; a-posteriori Householder residual ‖HA − B̃H‖ (3.2e−10) instead of the a-priori ε_H; own power and row recursions | **certified**: R = 1.5, r₁ = 0.05: F₁ = 0.8947, F₂ = 0.5916, |μ*| ∈ [1.84683479522, 1.94683479523]. R = 1.55 also certified (`out/refV0.json`) |
| Independent E_0 rest certificate | same code | certified, F = 0.024 (R = 1.0), 0.016 (R = 1.2) |
| Analytic bounds (δ₁, δ₂, Δ, ‖X‖, trace norm) | re-ran the cert49_build bound part (`out/rebV.json`, `out/rebE.json`); line-by-line review (§2) | identical to `data/prodV.json`, `data/prodE.json`, `data/prodVr.json` |
| Galerkin entries, computed a different way | `code/ref_entries.py`: ĝ by FFT of exp(iηf_B) with f_B taken from `lineB/common/model.py fCoeff(k,0)` (not ghat_arb); Taylor coefficients by FFT on the unit circle (not the triangular M·C product) | V_0 and E_2: 60 random entries plus the 25 largest; max difference 2.2e−15 (random) and 2.3e−14 (largest, \|A\| ≤ 0.57) |
| tracechk | rerun of `tracechk.py` on stored tchk matrices | identical: rel 1.9e−9, 8.9e−9, 2.8e−9, 5.1e−9 (m = 5, 7, 11, 13) |
| κ and sector coefficients | Gauss sums for κ ∈ {1,3,5,7}, plus a parity argument (§2.6) | \|c_b\| = ½ for b even, 0 for b odd, for **all** odd m with 3 ∤ m |
| Lean | `lake env lean` in `/workspace/bgs-int/BGS/formalization` (Lean v4.33.1, Mathlib cache) | compiles with no errors or warnings. Axioms: propext, Classical.choice, Quot.sound. No sorry (the one grep hit is the docstring) |
| SHA256_H2.txt | `sha256sum -c` | all 11 files OK |

## 2. Mathematics, line by line

### 2.1 Galerkin and splitting (cert49_build.py): correct
* **Composition.** ψ(w) = δ/ρ + w/λ maps the unit disc into the disc of radius θ = |δ|/ρ + 1/λ < 1.
  * ‖C_ψ‖ ≤ (1−θ²)^{−1/2}, and ‖C_ψ‖₁ ≤ Σθ^i = 1/(1−θ) (rank-one expansion).
  * The multiplier sup is e^{2πc₀|x|ρ}.
  * The ratio ω_c/ω_{c′} is applied on the correct side (output/input).
* **E-lattice.** I re-derived |δ_E| ≤ 1/(2λ) from the transition condition.
* **Exactness.** P(MC)P = (PMP)(PCP) is exact, including the case K_in > K_out: M is lower triangular, so degrees ≥ K_out never feed rows < K_out.
* **δ₁.** Input degrees ≥ K_in give ‖·‖ ≤ θ^K/√(1−θ²) per letter. δ₂ is a correct Cauchy estimate on |w| = r: ψ^l is entire, |ψ| ≤ |δ|/ρ + r/λ, and Cauchy–Schwarz over the l < K_in inputs.
* **Block norms.** ‖T‖ ≤ ‖(‖T_ij‖)‖_F ≤ √(Σ_j(Σ_i‖T_ij‖)²) is used by columns (δ) and by rows (Δ, X). This is valid. The U_n factor has norm 1 and trace norm 49.
* **Decomposition.** L_cc = PLP + (1−P)LP + L(1−P) is exact.
  * X is the full core→far operator for |c| ≤ R_max and |n| ≤ N_max, so it sits inside T₀′.
  * Everything else goes into Δ: far→core, far→far, letters |n| > N_max, rows |c| > R_max.
* **Tails.** The weight bound for letters |n| > N_max is e^{β(|c|/λ+½)}e^{β|x|/λ}. For rows |c| > R_max, the two-case ratio bound and the geometric sums (c_min = R_max + ½) are correct.
* **Hypotheses of F1 (TRACE-197).** ρ = 0.85 > 0.6036 (V) and > 0.1036 (E); β = 3.5 > 0; ĝ is entire, so the α condition holds.

### 2.2 Perturbation, counting, simplicity: correct
* T₀′ = [[A ⊕ 0, 0], [X, 0]] is block lower triangular, so σ(T₀′) = σ(A) ∪ {0}, and the resolvent bound (κR_core + 1/|z|)(1 + ‖X‖/|z|) + 1/|z| holds.
* **Dom mode.** T₀ = [[b₁₁, b₁₂], [0, Y]].
  * The resolvent bound 1/|z−b₁₁| + ‖b₁₂R_Y‖/|z−b₁₁| + ‖R_Y‖ is correct.
  * Neumann convergence at ζ₁ = |b₁₁| − r₁ puts σ(Y) in |z| < ζ₁. So the disc D(b₁₁, r₁) contains only b₁₁, and |z| > R contains only b₁₁.
  * The homotopy T₀′ + t(L − T₀′) keeps the ranks of both Riesz projections (the disc, and the exterior of |z| = R) constant, equal to 1.
  * Hence L has exactly one eigenvalue, of algebraic multiplicity 1, in |z| > 1.5, and it lies in D(b₁₁, 0.05).
* **Similarity bookkeeping.** For H_f = I − τww^H with float τ and w: H_f² = I + τ(τn−2)ww^H, so κ ≤ (1+dev)/(1−dev). The relation A = H_f⁻¹(T₀ + E′)H_f puts κ(ε_H + |b₂₁|) into the perturbation. Correct.
* **Neumann bound.** ‖R_Y(z)‖ ≤ Σ_{j<p}N_j|z|^{−j−1}/(1 − N_p|z|^{−p}) is correct and monotone in |z|. N_j = ‖fl-power‖ + Σ_i‖E_i‖N_{j−i} is correct (I checked the indices for powers and for the b₁₂Y^j rows). The final-power bound ‖M‖₂² ≤ ‖fl(MᴴM)‖_F + γ‖M‖_F² is correct.
* **Rest mode.** Correct. Certification at |z| = R means no spectrum in |z| ≥ R.

### 2.3 All-m chain: correct (subject to the cited inputs)
* Lidskii and Weyl on the weighted Hilbert spaces: Σ_{k≠*}|μ_k|^m ≤ R^{m−1}‖L‖₁, with a sector-independent trace norm, since the sector enters only through the unimodular e(bn/8).
* The triangle step uses |c_b| = ½ for b ∈ {0,2,4,6}.
* F_m ≥ |Z|²/φ(2h_m), with φ(2h) = φ(h) ≤ h − 1 because h_m is odd. W̃rest ≥ F − 4m follows from TRACE-165 (B^sym ≤ 2m) and TRACE-170 (|χ| ≤ 1).
* **Tail.** h_m − 1 < λ^{m/2}/2, ε_m is decreasing, and g^m/m is increasing for m ≥ 3. The explicit rows cover every admissible m ≤ 599, and the tail covers m ≥ 599. The threshold m₀ = 47 is right: m = 43 gives a negative bound, and 45 is divisible by 3.
* **Cited inputs exist with matching hypotheses.**
  * TRACE-194 [proved]: the 49-state law, a = 7 iff 3 ∤ m; γ and λ₇⁻¹ are m-independent for every m (source §10.2).
  * TRACE-197 [proved]: the lifted identity for the full alphabet, "real shifts (the 49-state law) are covered".
  * TRACE-165 and TRACE-170 [proved].
  * The F ≥ |Z|²/φ(2h) step is the same as in Line F §4 (TRACE-199, audited).
* **Independent support for the conventions.** tracechk agrees to ~1e−8 with the exact class sums. This rules out phase, sector and U_n errors.

### 2.4 Floating point
* **BLAS build.** numpy 2.5.4 uses scipy-openblas 0.3.34, DYNAMIC_ARCH; the runtime core is **SkylakeX** (queried with `scipy_openblas_get_corename64_`). OpenBLAS has no Strassen. zgemm3m (the 3M method) is used only when it is called explicitly, and numpy calls cblas_zgemm. So "classical dot products" holds.
* **The constant 2(n+2)u is not justified for every kernel path** (fix 2).
  * The SkylakeX main kernel (`zgemm_kernel_4x2_skylakex.c`, m4 path) keeps separate accumulators for a_r·b and a_i·b, which gives ≲ √2γ_{n+2}.
  * The m2 edge path (`vfmaddsub231pd` twice into one accumulator) accumulates both real products of each complex term in **one** accumulator. Its worst case is √2γ_{2n} ≈ 2.83nu > 2(n+2)u. Our D = 6762 and 6761 are not multiples of 4, so that path is used.
  * **Impact: nil.** The propagated rounding error is about 1e−8 relative to N_j (2.9e−4 out of 1.9e4 at j = 32), and ε_H/pert ≈ 3e−7. My rerun with √2γ_{2n+2}, which covers any summation order and FMA, certifies with the same margins.
* **Directions.**
  * arb decides every inequality.
  * bounds49 pads JSON floats by 2^−40.
  * However, `float(arb.upper())` rounds toward zero: I verified that float((1/3).upper()) < (1/3).upper(). So every "upper bound" stored in a JSON can be up to 1 ulp low.
  * rig_spec.py consumes δ₁, δ₂, Δ, ‖X‖ from the build JSON **unpadded** (fix 3). The impact is ~1e−16 relative against a ≥ 8.6% margin. ref_bounds.py re-decides everything with 1e−12 padding.
* **Small norm-error constants.** The 1e−7 inflation of Frobenius and absolute-sum norms covers n·u for 4.6e7 terms. The a-priori ε_H constants ("6u", "×2") are loosely argued, but my a-posteriori residual bound (3.2e−10) is below the author's 1.36e−9.

### 2.5 Provenance (fix 1)
* `logs/prodV_rig0.log` ended at 17:58:19 after 1211 s, so it started at ≈ 17:38. But `code/rig_spec.py` was last modified at **17:43:29**.
* `logs/prodV_dom0.json` contains `"scan": null`, which the current code cannot produce.
* So **the V_0 certificate was produced by an earlier, unarchived version of rig_spec.py.** The rest runs (V_2/4/6, E) post-date the current file.
* The scan reconstruction `prodV_dom0_scan.json` is identical to the 30 JSON lines of the log (checked). It is still the output of the unarchived code.
* My independent re-certification (`out/refV0.json`) closes the gap mathematically, but the repo must record a certificate produced by the archived code.

### 2.6 κ lemma (used for all m, stated nowhere in the REPORT)
* κ = −k·u·y′ (mod 8), where:
  * u = 49⁻¹ ≡ 1 (mod 8);
  * k = (196ν + s)/h is odd, because the numerator is odd and h is odd;
  * y′ is odd, because h² + 1 = 2y′² and gcd(y′, 2h) = 1. The same identity forces h to be odd.
* So κ is odd, and the Gauss sum gives |c_b| = ½ for b even and 0 for b odd.
* tracechk checks this only for m ≤ 13, and bounds49 silently assumes it for all m. Add the paragraph (fix 4d).

## 3. Required fixes (numbered, concrete)

1. **Provenance of the V_0 certificate.** Do one of the following:
   * (a) re-run `rig_spec.py ../data/prodV 0 dom 1.5,1.55,… 0.05,… 32 …` with the archived code (~25 min at load 20), store the JSON with its scan, and re-run bounds49 on it; or
   * (b) adopt the referee's `ref_rig.py` and `out/refV0.json` as the certificate of record for V_0, and record the code version and hash.

   Also archive the hashes of the code files used for each run.
2. **Rounding constant.** Replace gc = 2(n+2)u by √2·γ_{2n+2}, where γ_k = ku/(1−ku). This bound is independent of summation order and FMA, so it covers the OpenBLAS SkylakeX m2/m1 edge kernels. Restate §2.2 item 3 and §2.4 accordingly. With this constant the certificates hold (referee rerun: V_0 F₁ = 0.895, F₂ = 0.592; E_0 F = 0.024). The rest certificates' margins are unaffected, because rounding contributes ~1e−8 relative.
3. **Safe direction of JSON floats.** float(arb.upper()) rounds down.
   * Pad δ₁, δ₂, Δ, ‖X‖ upward when rig_spec reads them, or store arb strings.
   * Note in the JSON that "lower/upper" floats are display values.
   * The JSON tail constant `"C": 0.25` is the nearest double to a number 1e−50 below 0.25. Print C ≥ 0.2499.
4. **REPORT wording and table.**
   * (a) **Table "lower bounds rounded down" is partly rounded up.** Correct values:
     * F_m/2m: m = 53: 2.8e5 (not 2.9e5; exact bound 2.885e5); m = 71: 1.5e8 (not 1.6e8; 1.582e8); m = 85: 1.6e10 (not 1.7e10; 1.680e10).
     * W̃rest/m: m = 49: 7.6e4 (not 7.7e4; 7.66e4); m = 53: 5.7e5 (5.77e5); m = 71: 3.1e8 (3.165e8); m = 85: 3.3e10 (3.359e10).
     * The other entries are correct.
   * (b) **Sign error.** "s = −1, b = 0 resonance (N ≡ −196 family)" is wrong. With TRACE-194's convention N ≡ −s·4a², s = −1 is the **N ≡ +196 (mod h_m)** family (cmp_full prints N_mod_h = −s·196).
   * (c) **Citations.**
     * The lifted operators come from Line F **§2 (F1, TRACE-197)** applied to the TRACE-194 law; Line F §7 is the 49-state remark. They do not come from "Line F §5 (TRACE-195 law)": TRACE-195 is Prop. G and the m = 11/13 certificates.
     * State explicitly that φ(2h_m) = φ(h_m) ≤ h_m − 1 because h_m is odd.
   * (d) Add the κ-odd lemma of §2.6, since bounds49 needs it for every m.
5. **Scope statements.**
   * (a) **"Removes H∞,7 / closes TRACE-196" is imprecise.** H∞,7 is stated for the TRACE-194 operators on a single-disc space. What H2 proves is the **conclusion** of TRACE-196, unconditionally modulo the computer-assisted certificate and the cited TRACE-165/170/194/197, on the lifted space. Use Line F's wording for TRACE-188 ("H∞ as stated is neither proved nor needed"), or argue explicitly that the lifted weighted Hardy-lattice space is the "suitable Banach space" of the closure condition. The change of registry state is for the maintainers to decide.
   * (b) **The REPORT does not state its main consequence.**
     * W̃rest_m(2)/m ≥ 1.4e4 for every odd m ≥ 47 with 3 ∤ m, so **Conjecture R (TRACE-179), as stated, is false** for every compact η-range containing 2.
     * For R_NSW (h_m prime ⇒ m prime ⇒ 3 ∤ m), the bound violates it at every such m ≥ 47. Whether that set is infinite is not known.
     * The REPORT must say this, or say why not, with the dependency list. It must also note that "this conjecture's kick" is the l = 0 (diagonal) Line B kick (TRACE-163/195 usage; f_B = model.py fCoeff(k,0), which I checked).
     * This consequence contradicts the current TRACE-179 annotation ("R is not disproved"), so it needs an explicit registry update and a second look by the maintainers.
   * (c) **"Not covered" list.**
     * Replace "13 ≤ m < 47" by: odd m with 3 ∤ m in {17, 19, 23, 25, 29, 31, 35, 37, 41, 43} (m = 11, 13 are TRACE-195; m = 5, 7: nothing).
     * Add: every m with 3 | m; η ≠ 2; s = +1 not certified (not needed); the Hardy-space/trace-class framework is the lifted one only.

## 4. Recommended (non-blocking)
6. **Write out the 49-state version of F1.** Cite TRACE-197's "real shifts" clause and add the three-line argument:
   * the trace of a closed-chain block is Tr(M_pC_ψ)·Tr(U_{n_{m−1}}⋯U_{n_0});
   * the series converges absolutely in trace norm, which extends TRACE-194 (whose boundary says "finite alphabet only") to the full alphabet.

   The current support is one sentence each in Line F §2/§7 plus tracechk at ~1e−8.
7. **Lean.** REPORT §2.5 points at `/workspace/lineB_mainbuild/formalization`; use the repo's `formalization` (where it compiles). If it enters the repo, move it to `Bgs/LineH.lean` and import it from `Bgs.lean`. The lemmas are generic (no certificate numbers), and the REPORT says so correctly.
8. **Margin.** F·R₁ = 0.914 at r₁ = 0.05 leaves an 8.6% margin. That is sufficient but thin. Consider quoting r₁ = 0.1 (F·R₁ = 0.59) as a robustness cross-check; m₀ stays 47.
9. **Deleted matrices.** V_2/4/6 matrices were deleted. Their certificates were re-decided only from stored scalars (exact rationals), not re-run. If disk allows, keep `prodVr_b4` (the tightest, F = 0.841) or re-run it once.
10. **Clock note.** NOTES.md says "box clock (Europe/Amsterdam)", but the box clock is UTC+5. This is cosmetic.

## 5. Files
* Code:
  * `code/ref_rig.py` (independent certificate);
  * `code/ref_bounds.py` (exact-rational re-decision of all certificates and the all-m chain);
  * `code/ref_entries.py` (independent entries);
  * copies of the author's code.
* Outputs: `out/refV0.json`, `out/refE0.json`, `out/bounds49_rerun.json`, `out/rebV.json`, `out/rebE.json`.
* Logs: `logs/*.log`; Lean: `LineH.lean`, `LineH_ax.lean`, `logs/lean*.log`; hashes: `logs/SHA256_audit.txt`.
