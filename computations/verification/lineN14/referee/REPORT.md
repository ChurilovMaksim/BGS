# Referee report — Lines N13b (+N12b_v2), N14b, N14 (+N13_v2)
Grok Bot, 2026-11-01, written 02:05 Asia/Yekaterinburg (UTC+5); job started ≈01:41 UTC+5. No repo modifications, nothing pushed. All jobs nice 19, OMP_NUM_THREADS=1.
Author manifests verified OK before review. Artifacts listed at the end (SHA256.txt).

## Verdicts
| Line | Verdict | Severity of fixes |
|---|---|---|
| N13b (+N12b_v2) | **READY** after minor fixes | wording/constants |
| N14b | **READY** after minor fixes | proof write-up of Lemma 1 |
| N14 (+N13_v2) | **NOT-READY as [CA]/rigorous for c2_mid; READY after required fix F14.1** | error-constant derivation |

---
## 1. N13b (incl. N12b_v2)
**Mixed-class setup bound |Y_mixed,d| ≤ 2^ω·4h·avg|r|.**
- Point count: exact |H_d| = ∏(2q_i−1)∏(q_j−1)² ≤ 2^{ω(d)} h²/d·(1+o(1)). Checked at p=11 (h=8119=23·353): H_353 = 341220 ≤ 2h²/353 = 373474, H_23 = 5575680 ≤ 5732014 ✓ (Python + Lean `H353/H23`). For composite d the factor 2^{ω(d)} appears; it is e^{o(p)} and harmless, but the text writes "2h²/d" — **state 2^{ω(d)}h²/d**.
- Weight 2^ω·2d/h: exact max weights at level 8119 (unit part of the N6 rule, n=7743): iso-353 classes 0.04558, iso-23 0.00297; bound 2·2·353/8119 = 0.1739 ✓ (Lean `weight_bound`: 2/21 < 4·353/8119). Max over prime-level κ is 2cos(π/23)/21 = 0.0943 ✓.
- **Ambiguity (fix):** the N6 member rule applied directly at composite level h=8119 gives 8117 members, 374 of them non-units (κ undefined via t̄); its unit part has n = 7743, whereas the CRT product of prime-level sets has n = 351·21 = 7371. These differ — state that S is the CRT product of prime-level sets (the bound is proved for that).
- C′ covers d ≤ 1.4065^p: ε(1.2744/μ*)³ = 0.710994 → base ∈ (1.4064, 1.4067) ✓ (Lean). Composite h_p has a divisor ≥ √h ≈ 1.5538^p, so the uncovered range is genuine ✓ (correctly stated).
- Numerics p=11,13,17: reproduced spot values; label [N] fine. The "decay ≈ e^{−0.8p}" is a 3-point fit on heavy-tailed data — **downgrade to "consistent with"**.
- R1 restricted-pressure failure: structural claim ✓ (slow fixed point contributes μ*³/λ). **Constant: μ*³/λ = 1.20580, not 1.2061** (Lean `mu3_over_lam < 1.2059`). Conclusion unchanged.
- NSW-prime list for prime h_p: FLINT proving test over p ≤ 300 gives p ∈ {5,7,19,29,47,59,163,257} (p=3 gives h=7 prime but is excluded by their range — say so). No listed composite is prime; factorizations h11=23·353, h13=79·599, h17=103·15607 ✓ (Lean: recursion `decide`, primality `norm_num` for 41, 239, 9369319, 23, 353).
- R3(iii) X_q at p=11, q=353: **independently reproduced**. My λ-orbit reduction (11329 orbits over all 124609 points, own twists τ_i=Tr(λ^iβ)/q, own κ) gives X_q = −4.3777e-7 + 3.8988e-7 i, Y_q = 5.7617e-6 − 8.2384e-6 i, |1+X+Y| = 1.0000053, n_q = 351 — agreement with the N13b log to ~1e-15. Caveat: my run reuses the N6 transfer evaluator `twb.Zbatch/TW` for the twisted partition functions (not re-implemented here; it was refereed in earlier batches).
- N12b_v2 fixes ✓ (K numbers 2.9e-4 / 8.8e-4 consistent).

**Required fixes N13b:** (a) 2^{ω(d)} in the point count; (b) explicit composite-level S (CRT units); (c) 1.2058; (d) soften e^{−0.8p}; (e) mention p=3.

## 2. N14b
- **Lemma 1 (separation of the iso-mod-d sublattice; admissible ⇒ |coordinate product| ≥ d/h²):** argument is correct in substance (nonzero β in (1/h)𝔡 has |N| ≥ N𝔡/h² = d/h²). Gaps to fix for [P]: (i) H_d is a union of 2^{ω(d)} sublattices (1/h)𝔡 with N𝔡 = d, not one — separation must be stated per component and differences taken within a component; (ii) the trace lift goes through the inverse different O^∨ = (1/(2√2))O, which costs a constant factor 8 in the norm bound — insert it; (iii) the Bowen-ball count must use a sub-box partition (each box of side < separation contains ≤ 1 point). With these, Lemma 1 is [P].
- **Lemma 2 c = 0.7375 [P-sketch]:** label honest. Arithmetic ✓: c_B = ln(Λ_free²/r₂)/ln λ with Λ_free = 1.9656353, r₂ = 1.0529012 → 0.7375; Lean `cB_ratio ∈ (3.6695, 3.6697)`. a_cvalues.py uses μ = 1.9154732 (vs 1.9154712) — effect < 1e-6, negligible; fix the constant.
- **c-table:** recomputed, all entries ✓ (logs/ref_arith.json).
- **p=31:** h_31 = 424577·865087, both prime (FLINT + Lean `norm_num`, product by `decide`) ✓; θ = 0.2502 < 0.2624 so p=31 is covered ✓ (Lean `p31_cover`). Other composite p ≤ 89 not covered — correctly stated.

**Required fixes N14b:** Lemma 1 items (i)–(iii); μ constant in a_cvalues.py.

## 3. N14 (incl. N13_v2)
- **A_bad pre-flight on 5109 classes:** 5109 = number of ideals of norm < 2^13 ✓ (distinct, max norm 8191). 10 random classes re-evaluated: relative agreement ≤ 3e-12 ✓.
- **Rate certificate ρ̄ ≤ 0.28 via Neumann series [CA-fp]:** independently confirmed. ρ(𝒦) = 0.27255; my check: λ_min(W) = 3.49e-6, actual float rounding 2.0e-16, extended-precision Cholesky residual 7.4e-16 < σ = 1.75e-6 → certified with margin ~1e9. Y_c λ_min = 1.25e-5, cond 3.8e5. **Rigor caveat:** the a-priori constants (complex-arithmetic γ_n à la Higham, eigvalsh backward-error bound) are asserted, not written out. [CA-fp] is acceptable if those two constants are cited/derived; recommended: replace with an arb residual (cheap, makes it [CA]). Core→true conversion is [P-sketch]; the tensor joint-pair claim is [H] — labels should say so.
- **c2_mid.py "rigorous chain" (radii 2e-9):** **not rigorous as written.** The per-op constant 4e-14 is asserted and sits at my own worst-case estimate (complex γ, `np.add.at` accumulation length, exp phase error from large-argument reduction, libm ulp). Missing terms: etaT computed in float without its own error radius; final dot-product rounding replaced by 1e-16·|r| without the length factor. Empirically the radii are ~1e5× conservative: 597 windows overlapping my arb replay all intersect; on 89 arb-tight windows max |mid diff|/rad_c2 = 2.2e-6. So the numbers are right; the *proof* of the radii is not.
  - **F14.1 (required):** derive the constants explicitly (or inflate to ≥1e-13 per op with a stated length factor), add the etaT and dot-product terms, and label "[CA-fp: IEEE standard model + libm ≤1 ulp assumption]" — or cite the arb replay as the certificate.
- **δ_int ≤ 5.14415e-7:** recomputed 5.144157e-7 ✓ (round to 5.14416e-7 when stating an upper bound — the printed 5.14415e-7 is a hair below my value; **fix the last digit**).
- **Short types 27/4/96 vs mine 31/169/95:** reconciled: 31 = 27+4 (two subtypes); 95 genuine classes + α=4 → 96; 173 rows include α=4 ones vs my 169. Totals consistent (9.970e-7). **Wording fix:** say "173 rows incl. α=4", and note MODEL excludes α=4 explicitly (Lean `short_reconcile`).
- **Lemma D (e^{Γσ} ≤ 1.56e-8):** ✓ (mid-gap cut, Q̃ contraction 0.45, twist tails λ^{−G/2}, cross term Γ(e^{Γσ}−1)); budget arithmetic ✓ (Lean `rate14`, `core_true`, `budget14` within ln(1+ReΛ) ≈ 6.236e-4).
- N13_v2 fixes ✓. N14 lacks a self-hash for its own manifest, and rehashed SHA256_N13.txt (disclosed) — **add N14 manifest**.

**Required fixes N14:** F14.1 (blocking for the "rigorous" label); a-priori constants for [CA-fp] in the ρ̄ certificate (or arb); δ_int last digit; short-type wording; manifest.

## 4. What remains for an unconditional refutation (updated)
1. **Composite h_p mixed classes:** need the subgroup-C′ lemma with c < 0.387 (equidistribution (H-eq) beyond separation — Lemma 1 only gives separation). Without it the result is conditional on infinitely many NSW primes or balanced-semiprime h_p. Covered now: prime h_p and p=31 type cases with θ < 0.2624.
2. **(T):** lattice→collision reduction with constant ≤ 0.08 at J₀ = 12, the KP weight, and wrap-around points via the subgroup lemma.
3. **Composite core→true conversion** ([P-sketch] → [P]) and certification of the j > 12 tail.
4. **Rigorous c2_mid constants** (F14.1) or completion of the arb replay of N13 (still running on the box).
5. Explicit C′ constant / p₀, a k = O(1) stays lemma, and the R₄ automaton. (D1 + gas route is dead — R1 confirmed.)
6. Lemma 2 (c = 0.7375) from [P-sketch] to [P].

## 5. Lean
`lean/LineN14Arith.lean` (built with mathlib cache via lineN12 project, `lake env lean`, EXIT 0, no sorry/native_decide; log lean/build.log): hP recursion; h5,h7,h11,h13,h17,h19=9369319,h31 factorizations; primality of 41,239,9369319,424577,865087,353,23; H353/H23; weight_bound; Cprime_ratio ∈(0.7109,0.7110); coverA base ∈(1.4064,1.4067); sqrt_eps_between; cB_ratio; p31_cover; mu3_over_lam<1.2059; press_threshold; rate14; core_true; budget14; short_reconcile.

## 6. Artifacts (/workspace/audit/lineN14)
code/: ref_arith.py, ref_levelq.py, ref_c2_vs_arb.py, ref_abad_spot.py, ref_cp_cert.py · logs/: ref_arith.json, ref_levelq.{out,json}, ref_c2_vs_arb.json, ref_abad_spot.json, ref_cp_cert.{json,out} · lean/LineN14Arith.lean, lean/build.log · SHA256.txt
