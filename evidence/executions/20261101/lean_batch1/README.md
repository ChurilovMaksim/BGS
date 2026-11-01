# Lean batch 1 (1 November 2026)

Branch `lean-batch-1` from origin/main `a562e0cf`. Planning inventory:
[`../lean_inventory/INVENTORY.md`](../lean_inventory/INVENTORY.md) (219 proved/conditional claims without Lean
before this batch: 13 in class (a), 42 in (b), 164 in (c)).

**What this batch certifies.** Seven new modules in `formalization/Bgs` (55 `theorem` declarations), wired into
`Bgs.lean`, plus two existing but previously unlinked modules (`Fm009TraceObstruction.lean`,
`RetTowerGeometry.lean`). Eight proved claims now link Lean. **Every link is partial**: each Lean theorem proves the
finite, algebraic or constant statement named below, and nothing else. No claim state changed, and no analytic,
asymptotic or spectral conclusion is formalized.

## Claims, theorems, coverage

| Claim | Lean module(s) | Theorems | Coverage |
|---|---|---|---|
| BGS-FM-001 | `Fm001Statement.lean` (existing statements), `Fm001Exact.lean` | `fm001_dictionary_holds`, `fm001_fourier_weight_holds`, `fm001_mode_count_holds`; helpers `rCoeff_eq`, `neg_one_zpow_eq`, `gCoeff_eq`, `gCoeff_re`, `gCoeff_im`, `sgn_mul_self`, `gCoeff_mul_sign`, `weight_int`, `gCoeff_ne_zero_iff` | **Partial.** Proves the three `Prop`s that `Fm001Statement` stated without proof: the §1 exact Weyl dictionary (`ANordinary N = AN N` for odd `N`), the §3 Fourier weight `51451/1000` and the exactly-32-mode count. The §2 conclusions (Anosov, trivial `C¹` centralizer, no `C¹` reversor, no affine conjugacy) and the derivative bounds (5) are not formalized, because Mathlib has no `C¹`/Anosov API for the torus. |
| BGS-FM-009 | `Fm009TraceObstruction.lean` (existing), `Fm009CubeArith.lean` | `trace_cube_eq_zero_of_common_reversor` (existing); `S_cube`, `S_cube_sub_one`, `det_B`, `det_S_cube_sub_one`, `det_unit_of_coprime` | **Partial.** Covers the necessary implication (a common reversor gives `Tr([A,M]³) = 0`) and the integer arithmetic `S³ − I = 14·[[7,10],[5,7]]`, `det = −196`, which is invertible modulo `N` when `gcd(N,14) = 1`. The main content, `Tr[A_N,M_N]³ ≠ 0` (equations (1)–(4), the 2225-term Laurent certificate, the cyclotomic exclusion and the metaplectic character formula), is not formalized. |
| BGS-RET-004 | `RetTowerGeometry.lean` (existing, previously unlinked) | `s3_entries`, `s3_det`, `mz_entries`, `w_dots`, `w_rhs`, the 30 `sep_*`, `cand_j3_*_complete`, `noCand_j1_*`, `noCand_j2_*`, `lobe_gap`, `support_area` | **Partial.** This is the §3 finite exact-rational tower certificate that the claim boundary names: the 30 separations, the gap `37/528` and the area `1/288`. The bracket `{g,Cg} ≠ 0`, `Γ_T(g) = 0` and RW3/RW7 are not formalized. |
| BGS-FM-036 | `PellModuliArith.lean` | `norm_alpha`, `norm_alpha_pow`, `pell_norm`, `N_zero`, `s_mul_F`, `s_sq`, `one_add_s_pow`, `h_facts`, `N_odd`, `p_ne_two`, `two_ne_zero'`, `h_ne_one`, `orderOf_h`, `h_pow_ne_one`, `h_pow_ne_neg_one` | **Partial.** Covers the §4 arithmetic only. Writing `N + F√2 = (1+√2)^K` with `K` odd: `N² − 2F² = −1`. For every `m ∣ N`, `s = 2F` is `F⁻¹`, `s² = 2`, `(1+s)^K = 1`, `h = 3+2s = (1+s)²`, `h^K = 1` and `h − 1 = 2(1+s)`. For `K` prime and every prime `p ∣ N`: the order of `h` is exactly `K`, `h^j ≠ 1` for `0 < j < K`, and `h^j ≠ −1`. Not formalized: the diagonalising matrix `P`, the Weyl implementer, the multiplicity `n = (N−1)/(2K)`, and all spectral and analytic conclusions of Theorem C. |
| BGS-TRACE-248 | `LineLCollision.lean` | `lam_minpoly`, `P_natDegree`, `P_monic`, `aeval_P`, `alpha_eq_zero_iff`, `carry_coeff`, `lam_pows`, `no_small_collision_k6` | **Partial.** Covers `λ² − 6λ + 1 = 0` in `ℤ[√2]`, `v(λ) = 0 ⇔ (X² − 6X + 1) ∣ v` in `ℤ[X]`, and the carry recursion `v_j = e_j − 6e_{j−1} + e_{j−2}`. It also covers the referee check: the only `v ∈ ℤ⁶` with `|v_j| ≤ 3` and `∑_{j<6} v_jλ^j = 0` is `v = 0` (indices `0..5`; a shifted range gives the same zero set because `λ` is a unit). The Green's-function carry bound with `C0g = 1/(λ − λ⁻¹)` and the transfer-matrix reading are not formalized. |
| BGS-TRACE-271 | `LineM3Const.lean` (uses `LineN16Arith.scale_gt_113287`) | `lam_pos`, `lam_sq`, `rpow_cube`, `le_of_cube`, `rate_ge_113287`, `excess_ge_111238` | **Partial: part (c) constants only.** Proves `μ_lo²/λ^{2/3} ≥ 1.13287` and `μ_lo²/(λ^{2/3}·1.0184224) ≥ 1.11238` as real `rpow` statements. Parts (a), (b), (d), (e), the Prop K2 bound and the Line F bound are not formalized. Remark: the ratio bound needs the unrounded rate (`1.1123866`). The rounded quotient `1.13287/1.0184224 = 1.1123773…` is below `1.11238`, so the registered lower bounds should not be chained. The claim text is consistent with this; nothing in the registry was changed. |
| BGS-TRACE-291 | `LineN3Order.lean` (uses `LineMArith.lam_pow_eq`) | `lam_eq`, `norm_lam_sub_one`, `l_pow_p`, `l_ne_one`, `orderOf_l` | **Partial: order statement only.** Setting: odd primes `p`, `q` with `q ∣ h_p`, and `s² = 2` in `𝔽_q` (so `q` is split and `q′ = ker(√2 ↦ s)`). Then `l = λ mod q′` has order exactly `p`, via `λ^p = 1 + 2h_pε^p` and `N(λ−1) = −4`. The twist-sequence description (`τ_i = s l^i/q` and the unit case) and the orbit count are not formalized. |
| BGS-TRACE-297 | `LineN4Gauge.lean` | `e_add`, `gauge_T`, `gauge_G`, `T_G_comm` | **Partial.** Proves `L_τT_σ = T_{λσ}L_{τ−κλσ}`, `L_τG_ν = G_{ν/λ}L_{τ+ν/λ}` and `T_σG_ν = e(νσ)G_νT_σ` (referee N4-F1). They hold for arbitrary weights `w : ℤ → ℂ`, every `λ ≠ 0` and all functions `ℂ → ℂ`, with the series as `tsum`. The two sides agree termwise, so no summability hypothesis is needed. The definitions of `L_τ`, `T_σ`, `G_ν` are those of `computations/verification/lineN4/REPORT_N4.md` §3.1. The geometric-twist product corollary is not formalized. |

Faithfulness: each Lean statement is the mathematical statement quoted from the claim boundary or source section in
the right-hand column, with the same constants and quantifiers. Every link is partial. For six claims the registry records the scope in a
new `formalization_scope` field in `record/claims.json`. BGS-FM-001 and BGS-FM-009 are sealed wave-2 rows (see
`wave2_integration_audit.py` and `wave3_integration_audit.py`), and the sealed-row contract admits no new keys. Their
new `formalization`/`evidence` values are therefore admitted through their existing `historical_claim_amendments` rows
in `record/claim_integration_epochs.json`, with an appended disposition sentence and review pointer. Their scope is
recorded only here, in the linked receipt.

## Build and checks

* Toolchain `leanprover/lean4:v4.33.1`, Mathlib `v4.33.1`. `lake exe cache get` was run first, in a fresh clone.
* The modules were compiled **one at a time**: each existing module with `lake build Bgs.<Module>` in sequence,
  then each new module, to stay within the shared box's memory.
* Full build: `bash computations/maintenance/build_lean_verified.sh evidence/executions/20261101/lean_batch1/lake_build_Bgs.log`.
  It exited 0, ending "Build completed successfully (8869 jobs)" and "Verified Lean build: command status and
  error-free log agree" ([log](lake_build_Bgs.log)). The wrapper output is in `build_wrapper.out`. Every module was
  already compiled, so this run replayed the cached results and compiled the aggregator.
* Axioms: [`Axioms.lean`](Axioms.lean) runs `#print axioms` for all 55 new theorems, plus
  `Bgs.Fm009TraceObstruction.trace_cube_eq_zero_of_common_reversor` and `Bgs.RetTowerGeometry.s3_det`, using
  `lake env lean`. Output in [`axioms.log`](axioms.log). Every one depends on a subset of
  {propext, Classical.choice, Quot.sound}, and `s3_det` depends on none.
* There is no `sorry`, no `native_decide` and no `axiom` declaration in the seven new modules (checked with comments
  stripped, as in `render_results.py`). The kernel tactics used are `decide`, `norm_num`, `omega`, `interval_cases`,
  `ring` and `linear_combination`.
* Registry links: [`scripts/link_batch1.py`](scripts/link_batch1.py) adds the links to `record/claims.json`
  (`formalization`, `formalization_scope` except for the two sealed rows, and `evidence` = this README). It extends the
  two sealed rows' amendment entries in `record/claim_integration_epochs.json` and mirrors the changed rows into the
  curated `record/claim_verification_inventory.json`. The mirrored fields are the links, the receipt counts, the
  `lean_formalization` tag and `source_blob_sha`. `RESULTS.md` was regenerated by `render_results.py`. The other
  `render_*.py --check` scripts report OK.
* Counts: 152 non-open claims link Lean (was 144), there are 162 modules (was 155), and 2241 `theorem`/`lemma`
  declarations (was 2186; counted with `grep -E '^\s*(theorem|lemma)\b'`). `RESULTS.md` is generated. The counts in
  `README.md` and `README.ru.md` were edited by hand, changing only the counts and the build-log link.
* Checker, render and unit-test results: [`checks.log`](checks.log) and [`unittests.log`](unittests.log).

## Recommended next batch

The remaining class (a) claims are BGS-TRACE-178, 216, 273, 317, BGS-FM-026 and BGS-RES-023. Each needs its finite
input data or definitions imported first, for example the deposited automaton matrices for TRACE-216 and the integer
`B` for RES-023. The cheapest class (b) claims are BGS-TRACE-229, 259 and 267 (finite-field Parseval and Gauss-sum
identities over `ZMod q`), BGS-TRACE-218 (Möbius aliasing for finitely supported weights), BGS-TRACE-211 and 263
(finite Fourier identities) and BGS-TRACE-143 (`M_N = ΔF_{1/4}Δ`). The BGS-TRACE-297 geometric-twist corollary
follows by induction from `gauge_T`, `gauge_G` and `T_G_comm`.
