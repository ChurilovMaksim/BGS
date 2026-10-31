# Referee report lineN16: final pass before the integration PR (N16, N18b / REPORT_N17b_v2, THEOREM_DRAFT_v3)
Grok Bot · 2026-11-01, 03:32–03:45 Asia/Yekaterinburg (UTC+5). Nothing in /workspace/bgs-lineN was modified, nothing was pushed, and every job ran at nice 19 with one thread. PID 864667 (p = 17 mixed run, nice 19) was not touched; it is still running.
Integrity: SHA256_N16.txt (28 files) is OK. SHA256_N18b.txt (10 files, paths relative to bgs-lineN; covers THEOREM_DRAFT{,_v2,_v3}.md) is OK, and its self-hash is OK. The THEOREM_DRAFT_v3.md sha256 matches the manifest (1415c7b2…).

## Verdicts
| Item | Verdict |
|---|---|
| **N16** | **READY after minor fixes (N16-1…N16-4).** The numerics reproduce exactly. One diagnosis in §2 is wrong (N16-2), and several referee-status cells are stale. |
| **N18b / REPORT_N17b_v2** | **READY after one required fix (R1).** B1, B3–B8 are correctly applied. **B2 introduced a new error:** the Robin term in `a_crossover_v2.py` uses the wrong variable, so the crossover numbers are wrong. The first prime stays 1399. The monotonicity argument [P] is valid once corrected. **Lemma 1: verdict [P]**, with two cosmetic fixes. |
| **THEOREM_DRAFT_v3** | **NO-GO as written; GO once the 7 edits in §4 are made.** They are small text and number replacements, given verbatim, and none changes the structure or any conclusion. After them no further referee round is needed, only a diff check. All 20 lineN15 §3 items are correctly fixed (§3a), apart from the downstream effects of R1 and two stale referee cells. The plain summary has one inaccurate sentence and one rate rounded the wrong way. |

---
## 1. N16
**Checks performed**
- **(a) Scalar carry sum, independent re-implementation** (`code/ref_gscalar.py`).
  - Own block decomposition built from the N12 a_ops data and the N12 adapted-norm npz Φ, ψ (not fastops).
  - Own DP over states (e_{t−1}, e_{t−2}) with v_t = e_t − 6e_{t−1} + e_{t−2}.
  - The **non-zero-carry part is tracked separately**, so C_n/S_n^(0) is obtained directly, without the S^(1) − S^(0) cancellation.
  - E = 1, n ≤ 7: C/S⁰ = 0, 0, **1.6534e-9, 3.4557e-11, 1.4056e-11, 1.3494e-11, 1.3477e-11**. This matches the N16 log ratios (1.653e-9, 3.456e-11, 1.406e-11, 1.349e-11, 1.348e-11) to all printed digits. The imaginary parts are ≤ 1e-20.
  - The authors' E = 2, 3 logs equal E = 1 to all digits (n ≤ 6).
  - Constancy in n is confirmed directly: interior carries contribute < 2e-14 relative per extra step. They are actually computed to be that small, not merely below binary64 resolution.
- **(b) N15 Monte Carlo claim.** The torus-MC ratios at n = 6, 7, 8 are 0.88σ, 1.09σ and 1.04σ from 1 ✓.
- **(c) conv_vec re-run.** The authors' `window()` (exec'd from their file, writing only to my directory) was re-run on 12 replay rows: singles, single_eps, pairs at G = 3…14, and shorts. **r and E are bit-identical to `conv_vec_replay.jsonl`** (max |Δr| 2.4e-19, ΔE = 0).
- **(d) Aggregates recomputed from the jsonl** (`code/ref_n16_post.py`):
  - Σ dev_by_G = **2.469789e-6** vs coded upper 2.469791e-6 ✓ (**2.470e-6 confirmed**).
  - True vs core A_bad (j ≤ 10): **2.0805e-6 vs 2.0314e-6** (+2.42%) at g₀ = 4; +1.68% at g₀ = 2; +3.09% at g₀ = 6 ✓.
  - Core j = 11, 12 at g₀ = 4: 2.132e-10 ✓.
  - Core total j ≤ 12: 2.0315690546e-6 ✓.
  - Midpoints equal c3_mid exactly (0 mismatches out of 3120).
- **(e) A_bad finite part j ≤ 12** (`code/rerun_acert3_spot.py`).
  - 10 classes across j = 0…12 re-run through `c3_mid.window`, bit-identical.
  - absw_up ≥ absw_float holds in all 5109 rows; max excess is 1.14%.
- **(f) Logic of the vector conversion.**
  - Forward recursion with (N_H + cT·g·F_s) is correct for X_T = X̂ + Δ with ‖TΔT⁻¹‖ ≤ cT·g·F_s.
  - The dual-norm backward recursion is right: ‖wXT⁻¹‖ ≤ ‖w‖_*·‖TXT⁻¹‖, with T⁻¹ and T swapped in loc. So are F_f = ‖v̂‖ + ‖T⁻¹‖e and F_b = ‖ŵ‖ + ‖T‖e_b.
  - err_proj is the correct first-order expansion w_T Q u_T − ψ̃QΦ̃ with the second-order el·GA·er term.
  - **But** the 2·dPi·g·max(F_f, F_b) term is only the first-order part of Tr((Π_T − Π̂)Q). The second-order term dPi²·‖Q‖ (≤ 7.8e-10·g·GA, about 1e-6 for GA ≈ 340) is not in the code. It is negligible (E ≈ 4e-4…1e-3), but the written [P-sketch] lemma must contain it. The [P-sketch] label is honest.

**Findings**
- **N16-1 (minor, overstatement).**
  - §1.1: "[N]: the torus mean equals the i.i.d. value × (1+O(1e-11)) for n ≤ 12". This was computed only for |e| ≤ 1 (n ≤ 12) and |e| ≤ 3 (n ≤ 6). S^(15) itself was not computed. Say "|e| ≤ 3 (n ≤ 6) / |e| ≤ 1 (n ≤ 12); |e| ≥ 4 not computed, [H] negligible (entry weights)".
  - §1.3: the "[P]" bullet contains the [CA-fp] shell sums; split the labels.
- **N16-2 (required for any text that inherits it): the G > 15 diagnosis is wrong.**
  - The conclusion is correct: under box widening the per-G bound is flat, ≈1.50e-7 per G for G = 7–15 (reproduced), so this form cannot control the G > 15 tail.
  - But the cause is **not** mainly the end-projector term. For pair windows, E is dominated by the **accumulated per-step core→true perturbation** inside rad_c3: medians at G = 15 are rad_c3 ≈ 8.0e-4 vs err_dPi ≈ 4.7e-5 vs pure rounding (N15) ≈ 6.2e-8, so rad_c3 is the largest term in 2698 of 2700 pair windows.
  - E/|r| is ≈2e-3 for singles but **≈8% (median) for pairs**.
  - So "the dPi term should cancel to first order" is not enough. A difference-form conversion must correlate the **per-step perturbation** contributions of the pair chain with those of the single chains.
  - Fix §2 and the "E/|r| ≈ 1.7e-3" (singles only) wording.
- **N16-3 (minor): status table cells are stale** after lineN15.
  - Row 3 (step-norm table): method refereed in lineN15 §1a. Values were not independently recomputed.
  - Row 4: the N15 constants fix was refereed in lineN15 §1c.
  - Row 7: c3 radii method lineN15 §1a, plus this re-run.
  - Row 8: refereed lineN15 §1d. **Add "tail j > 12 = H1, [H] placeholder"** (N15-F1).
  - Row 9: closed, lineN15.
  - Row 13: refereed lineN15 §1e. Sharp |e| ≤ 14, 633 states.
  - Rows 14 and 19: numerics reproduced (lineN16).
- **N16-4 (minor).** The bottom line lists row 11 among the "certified" pieces, but row 11 is [P]+[N]. Say so.
- **Table accuracy otherwise.**
  - All 23 values match their sources: 21.103, 167.213, 0.45, 1.01e-12/4260, 2.91656, 3.49e-6, 2.031569e-6, a = 5.93e-6, S₀ = 2.063e-6, 5.14476e-7, 9.970e-7/173, 1.56e-8, 4.4e-4/0.082 (186×), and 1.1718.
  - The 6.236e-4 in row 22 is ln(1 + 6.238e-4) = 6.2361e-4 ✓.
  - Labels are honest.

## 2. N18b / REPORT_N17b_v2
### 2a. B-fixes
- **B1 ✓.** The §5(b) text matches my enumeration.
- **B3 ✓.** The TRACE-244/251/252/280–282 statements match the ledger.
- **B4 ✓, B5 ✓** (d = 31 at m = 15; column relabelled), **B6 ✓, B7 ✓** (339/498; base 0.97801), **B8 ✓** (prime powers in H7*, §3 table).
- **B2: the gas form is fixed, but the crossover script has a new error (R1, required).**
  - `a_crossover_v2.py` line `robin(L) = e^γ·ln L + 0.6483/L − 1` with **L = ln K_p**. Robin's Theorem 2 has 0.6483/**ln ln n** = 0.6483/**ln L**.
  - So the bound is understated by ≈0.6483(1/ln L − 1/L) ≈ 0.083 at p ≈ 1386.
  - Corrected (`code/ref_crossover.py`, mpmath at 50 digits, exact K_p by big integers):

    | δ | first integer p (envelope) | margin there | first odd p (exact K_p) | first prime | Robin at p = 1289 |
    |---|---|---|---|---|---|
    | core 5.14476e-7 | **1386** (v2: 1382) | 0.0153 | 1387 | **1399** | **12.849** (v2: 12.765) |
    | true G ≤ 15, 2.470e-6 | **1390** (v2: 1386) | 0.0021 | 1391 | **1399** | 12.849 |

  - There are no violations at any prime 1399 ≤ p ≤ 5000.
  - The v2 sentence "v1 printed 12.85 from an approximate ln K_p" is **wrong**: 12.85 was right, and 12.77 comes from the bug.
  - "This agrees with the referee's 1386" is a coincidence: two errors of about 0.08–0.10 cancel. My lineN15 1386 was the core-δ value.
- **Monotonicity argument: [P], valid after the fix.**
  - G′(p) = 4x(2x − 1)·ln b is increasing ✓.
  - Envelope ln K_p ≤ (2p+1)ln ε holds because 2h_p ≤ ε^p + 1 (h_p = sinh(p·ln ε)) and (ε^p+1)² + 3 ≤ ε^{2p+1} for p ≥ 2 ✓.
  - For the correct ρ(L) = e^γ ln L + 0.6483/ln L − 1: ρ′(L) = (e^γ − 0.6483/ln²L)/L ≤ e^γ/L, so g′(p) ≤ 2e^γ/(2p+1) still holds (same bound as v2) ✓. ρ is increasing for L > e^{0.6033} ≈ 1.83 (v2 says "L > 0.37"; replace).
  - G′(1386) = 0.02209 and G′(1390) = 0.02200, both > 2e^γ/(2p+1) ≈ 0.00128. Lean `env_slope_small` proves 2e^γ/2773 < 0.0219 from γ < 2/3 and e < 2.7182818286.
  - Conclusion: G(p) > I_p for all p ≥ 1386 (core) / 1390 (δ_true G ≤ 15), hence for every prime p ≥ 1399 under the stated idealization.
  - Caveat to state: δ in B_p is the all-G true δ, whose G > 15 part is open (H4). So 1390 is a lower bound for the true p₁.
- **Minor.**
  - The §2 "Scale" line gives 1.1329. The exact value μ²/ε^{4/3} = 1.1328794 (Lean `scale_lt_113288`, `scale_gt_113287`); use 1.13287 (TRACE-271).
  - T′ is printed as 1.4279/1.428 in places. It is 1.4278538 (Lean `Tprime_gt`: > 1.42785). Use 1.42785, because rounding a threshold up is non-conservative.

### 2b. Lemma 1 (REPORT_N17b_v2 §6): verdict **[P]**
Checked line by line:
- **Setting.** O^∨ = (2√2)⁻¹O; |N(γ)| ≥ 1/8 on O^∨∖0; s₀ ≥ 1/(2√2) via max(|a|,|b|)² ≥ |ab| (Lean `max_sq_ge`). The unit λ preserves O^∨, and A = diag(λ, λ⁻¹) because λ′ = λ⁻¹.
- **Components.** H_𝔡 is a subgroup of order [𝔡O^∨ : hO^∨] = h²/d (consistent with the N13b 2^ω·h²/d fix). Admissibility gives |N(γ)| = N𝔡·N𝔟/8 ≥ d/8.
- **Proof of (a).**
  - The continuity step is valid: (λ+1)δ ≤ s₀/2 < s₀ forces A z_k = z_{k+1}.
  - z₀ ∈ Λ_𝔡∖0, because any lift of a nonzero element of H_𝔡 lies in Λ_𝔡 ⊇ ι(O^∨).
  - Using the u-coordinate at k = n−1 and the s-coordinate at k = 0 gives |N| < δ²λ^{−(n−1)} ≤ d/(16h²) < d/(8h²) when n ≥ n_*.
  - Correct, including the degenerate case n_* ≤ 1, where no pair is δ-close.
- **Proof of (b).**
  - Minimal lifts are injective in x.
  - Q has u-width δλ^{−(n−1)}. The ⌈λ^{n_*−n}⌉ half-open sub-boxes have width ≤ δλ^{−(n_*−1)}.
  - A difference inside one sub-box has |N| < δ²λ^{−(n_*−1)} ≤ d/(16h²), so it is 0.
  - The union bound over the 2^{ω(d)} components (which may overlap) is fine.
  - Correct.
- **δ₀** = 1/(4√2(λ+1)) = 0.025888 ✓.
- **L1-a (cosmetic).** "Use in Lemma 2: C = 16λδ²h²λ^{−p}" should be **C = 16λ²δ²h²λ^{−p}**, since ⌈x⌉ < x + 1 gives λ^{n_*−n} < λ²·(16δ²h²/d)·λ^{−n} (Lean `lemma1_C`). It is still ≍ 1.
- **L1-b (cosmetic).** "N𝔡·N(O^∨) divides N(γ)": N(O^∨) = 1/8 is not an integer. Write "(γ) = 𝔡·O^∨·𝔟 with 𝔟 integral, so |N(γ)| = N𝔡·N𝔟/8 ≥ d/8".
- **Scope** (stated correctly): squarefree d with split prime factors. That H_d is the set used in Lemma 2 is part of Lemma 2, which is [P-sketch].

---
## 3. THEOREM_DRAFT_v3
### 3a. lineN15 §3 items 1–20 (v3 §9 map), each verified in the text
| # | Fixed? | Note |
|---|---|---|
| 1 §0 overclaim | ✓ | |
| 2 B_p form; n/h_p := 1; p₁ label | ✓ form / ✗ **numbers** | 1382/1386 → **1386/1390** (R1) |
| 3 single δ, duplicates | ✓ | core vs true clearly separated |
| 4 p₀ list / p_thr | ✓ | TRACE-227 (p ≥ 81), TRACE-271 (p ≥ 165), ε₁₆ 339/498, Prop X′ 1289, W 8.3e25 all correct |
| 5 cross lines | ✓ | in §1, B_p (\|X_cross\|), H5(b), subsequence |
| 6 H1 186× | ✓ / ✗ | two inaccuracies from N16 (E2) |
| 7 H2 | ✓ | |
| 8 H3 | ✓ | F1/F2 applied |
| 9 H4 | ✓ / ✗ | wording (E3) |
| 10 H5 | ✓ | p = 31 moved; [P-sketch] wording |
| 11 H7 | ✓ | T′ 1.42785 ✓ (Lean) |
| 12 H8 | ✓ | 1.1718 / 0.6647 / 0.9678 / 0.5490 ✓ |
| 13 subsequence (a)–(e) | ✓ | |
| 14 §3 labels | ✓ | |
| 15 norm scope | ✓ | |
| 16 δ_int/ρ̄/A_bad rows | ✓ | |
| 17 m = 57 | ✓ | |
| 18 §6 errata | ✓ | add the N18b robin() erratum (E7) |
| 19 §7 | ✓ | |
| 20 assembly label | ✓ | |

### 3b. Numbers checked against sources
These all match their sources ✓:
- **Exact W′/m values** −0.74, −0.31, −0.04, +0.47, +0.09 (m = 9…17): match N17b `b_exact_dev.json` (−0.7388, −0.3104, −0.0353, +0.4691, +0.0933). These are frozen-definition values; the ledger's m ≤ 15 list agrees. Line H's "−0.82 … +0.23" are W′_act, a different quantity.
- **N16 and lineN15 constants:**
  - δ_true 2.470e-6 ✓; δ_core 5.14476e-7 ✓; Lemma D 1.56e-8 ✓;
  - Re Λ_lo 6.238e-4 / Λ_lo′ 6.234e-4 ✓;
  - KP a = 5.93e-6, S₀ = 2.063e-6, 2.5774e-6 ✓;
  - 633 / 29 / 14 ✓; 186× ✓ (Lean `coll_margin`).
- **Classes and rates:** 15 small-depth classes ✓; c_B 0.7375 and 1.588^p ✓; C′ rates ✓; automaton 5.41151/2.611 ✓.
- **Number theory:**
  - h₃₁ = 424577·865087 ✓ (lineN14 Lean); NSW list ✓ (lineN14);
  - TRACE-223 1.2837144 ✓; 10^264.5 ✓; e^{−0.28p} ✓ (from N11: (12e·1.03e-3)^{p/12} = e^{−0.2828p}).
- **Wrong:**
  - **S_ρ ≥ c·1.13288^m** (§2 l.56) rounds the rate **up**. The exact value is 1.1328794 < 1.13288 (Lean `scale_lt_113288`), so as written the inequality is false for large m. Use 1.13287 (TRACE-271), which is valid (Lean `scale_gt_113287`).
  - p₁ numbers (R1).

### 3c. Plain summary
- No overclaim about refutation: "Nothing that refutes R′ is proved" ✓; the H1/H4/H5/H7* list ✓; prime h_p ✓; ¬R_NSW ✓.
- **One inaccurate sentence:** "Exact small-p data (p ≤ 13)". Exact enumeration exists only for m ≤ 17 (p ≤ 5). The p = 7…13 data are I2′-formula level data [N] and are not exact.
- "the reduction is bookkeeping" is acceptable, since H0 carries Prop X [P-sketch] and §2 is labelled [P mod inputs].

### 3d. Claim → file → referee table (§8)
- **Stale cells:**
  - Gas vs Robin: "monotonicity not yet refereed" → refereed here, with R1.
  - Lemma 1: "[P] pending" → [P] (lineN16).
  - Carry correction: "not refereed" → reproduced (lineN16 §1a).
  - δ_true: "not refereed" → numerics reproduced (lineN16 §1c–d); lemma [P-sketch].
  - A_bad: "c3 radii not refereed" → lineN15 §1a + lineN16 §1e.
  - Step-norm table: "not refereed" → method lineN15 §1a.
  - Same in §3 (rows "Step-norm table … (not yet refereed)", "Lemma 1 … once … refereed") and §7 item 6.
- **Missing rows (minor):** H5's "no known theorem (N15b)" and H8's N16b units note are author literature/units notes and were not refereed by me. Either add rows "N15b / N16b: author notes, not refereed" or drop the N15b/N16b citations from status cells.

## 4. Required edits for GO (verbatim replacements)
**E1 (R1, numbers).**
- **Draft §2 threshold table, p₁ row**, replace with:
  `| p₁: gas vs Robin (tails = Y = X_cross = ε = 0, n/h_p := 1) | all p ≥ 1386 (core δ) / 1390 (δ = 2.470e-6, G ≤ 15 part only; increases once the G > 15 tail is added); **first prime 1399** | [P-arith: float/mpmath evaluation + monotonicity] (N18b a_crossover_v2.py with robin() corrected to 0.6483/ln L; lineN16 §2a) |`
- **§3 row "Gas vs Robin crossover"** → `Gas vs Robin crossover: all p ≥ 1386 (core) / 1390 (δ_true, G ≤ 15); first prime 1399 | [P-arith] (lineN16) | N18b a_crossover_v2.py (robin() fixed)`.
- **§8 row** → referee cell `lineN15 §2(b); lineN16 §2a ✓ after robin() fix (1386/1390; first prime 1399); monotonicity ✓`.
- **REPORT_N17b_v2**:
  - fix §0.2 (`12.77` → `12.85`; delete "(v1 printed 12.85 from an approximate ln K_p.)");
  - fix §2 bullets: `r(L) = e^γ ln L + 0.6483/ln L − 1 … increasing for L > 1.83`; `first at p = 1386 (margin 0.0153)`; `first at p = 1390 (margin 0.0021)`; delete "This agrees with the referee's 1386"; `G′(p*) ≥ 0.0220`;
  - fix §2b Q2 (1382/1386 → 1386/1390) and §9 B2;
  - change the code line to `def robin(L): return math.exp(gam)*math.log(L)+0.6483/math.log(L)-1` and re-run, which reproduces my table.

**E2 (H1 row).** Replace "[N]: scalar torus mean = i.i.d. to ~1e-11; carries cancel across 3 steps; carry correction ≤ 2e-9 relative (n ≤ 12); prefactor does not converge." with:
`[N]: carry sums with |e| ≤ 3 (n ≤ 6) and |e| ≤ 1 (n ≤ 12) equal the i.i.d. value to relative ≤ 1.7e-9 (≈1.35e-11 for n ≥ 5; reproduced without cancellation, lineN16); |e| ≥ 4 not computed ([H] negligible: isolated-carry entry weights 7e-3, 3e-8, 2e-15 for c = 1, 2, 3); N15's apparent prefactor non-convergence was an artefact of the share proxy (N16 §1).`

**E3 (H4 row).** Replace "Vector-chain conversion per window: E/|r| ≈ 1.7e-3 [P-sketch lemma, CA-fp numerics], giving δ_true(G ≤ 15) ≤ 2.470e-6. G > 15 true tail flat in G under box widening, so not controlled (N16 §2)." with:
`Vector-chain conversion per window: E/|r| ≈ 2e-3 for singles, ≈ 8% (median) for pair windows, max 5.27 [P-sketch lemma (the written lemma must include the second-order dPi²·‖Q‖ term), CA-fp numerics], giving δ_true(G ≤ 15) ≤ 2.470e-6. Under box widening the G > 15 bound is flat (≈1.5e-7 per G), so it is not controlled. The pair-window error is dominated (≈93%) by the accumulated per-step core→true perturbation, so a difference-form conversion must cancel that term, not only the end-projector term (N16 §2; lineN16 §1).`

**E4 (§2 l.56).** `with S_ρ ≥ c·1.13288^m (TRACE-271: 1.13287)` → `with S_ρ ≥ c·1.13287^m (TRACE-271; μ²/ε^{4/3} = 1.1328794)`.

**E5 (plain summary, 4th bullet).** Replace with:
`- **Small-p evidence is numerical only.** Exact-enumeration W′ tables exist for m ≤ 17 (p ≤ 5); level data at m = 21, 33, 39 (p ≤ 13) come from the I2′ formula. All of it is [N] and is not evidence for the asymptotic statement.`

**E6 (referee status cells).**
- **§3:**
  - `Step-norm table … | [CA-fp] (method refereed lineN15 §1a; values not independently recomputed)`;
  - `Lemma 1 (sublattice separation; squarefree d, split primes) | [P] (refereed lineN16 §2b; C = 16λ²δ²h²λ^{−p}) | N14b §2, REPORT_N17b_v2 §6`.
- **§8:**
  - Lemma 1 → `[P] | … | lineN16 §2b ✓`;
  - carry correction → `lineN16 §1(a) ✓ reproduced`;
  - δ_true → `lineN16 §1(c–d) ✓ numerics; lemma [P-sketch]`;
  - A_bad → `lineN14 ✓; lineN16 §1(e) ✓ (10 classes bit-identical; aggregate)`;
  - step-norm → `lineN15 §1a (method)`.
- **§7 item 6:** "Lemma 1 referee of the written proof" → "Lemma 1 done ([P], lineN16)".
- **Optional:** add an N15b/N16b row, "author notes, not refereed".

**E7 (§6 errata).** Add:
`- N18b a_crossover_v2.py Robin term 0.6483/ln K_p (should be /ln ln K_p): crossovers 1382/1386 and "12.77 at p = 1289" superseded by 1386/1390 and 12.85 (lineN16).`

**Lemma 1 text (in REPORT_N17b_v2 §6, before it is quoted in the PR):**
- L1-a: `C = 16λ²δ²h²λ^{−p}`.
- L1-b: `(γ) = 𝔡·O^∨·𝔟 with 𝔟 integral, so |N(γ)| = N𝔡·N𝔟/8 ≥ d/8`.

**Recommended (not blocking).**
- Give the one-line proof of the K_p facts in §3/§8:
  - h_p = sinh(p ln ε), so h_{3p} = h_p(4h_p² + 3);
  - h_p mod 7 has period 1, 0, −1 in p ≡ 1, 3, 5 (mod 6), so for primes p ≥ 5, h_p ≡ ±1 and 7 | K_p;
  - gcd(h_p, K_p) = gcd(h_p, 3).
- Apply the N16-1…N16-4 report fixes.

## 5. Updated list of what remains for an unconditional refutation
Unchanged from lineN15 §4, except:
- **H4** is now explicitly "difference-form conversion cancelling the **per-step perturbation** (dominant) and end-projector terms, plus the G > 15 true tail".
- **Lemma 1 is closed [P].**
- **p₁ ≥ 1390** for the G ≤ 15 part of δ_true.

The full list:
- H1: certificate on 633 states, box/aliasing, j > 12;
- H4;
- H5: R-mix, cross lines, partially isotropic points; or 𝒫;
- H7*: hp-div, mixed, all K_p levels;
- H6: p₀, squarefree;
- write-ups: KP corollary/interplay, Lemma 2 → [P], the vector conversion lemma with its dPi² term, and p₁ with all budgets.

## 6. Lean (`lean/LineN16Arith.lean`; lineN12 project, mathlib cache; EXIT 0; no sorry or native_decide; `lean/build.log`)
| Theorem | Statement |
|---|---|
| `eps4` | (1+√2)⁴ = 17 + 12√2 |
| `scale_lt_113288` | μ⁶ < 1.13288³·ε⁴ (rate < 1.13288) |
| `scale_gt_113287` | 1.13287³·ε⁴ < μ⁶ |
| `Tprime_gt` | μ³ > 1.42785³·ε |
| `env_slope_small` | 2e^γ/2773 < 0.0219 |
| `lemma1_C` | ⌈x⌉ < x + 1 |
| `coll_margin` | 0.082/4.4e-4 > 186 |
| `max_sq_ge` | \|ab\| ≤ max(\|a\|,\|b\|)² |

## 7. Artifacts (/workspace/audit/lineN16)
- **code/:** ref_gscalar.py, ref_n16_post.py, ref_crossover.py, rerun_conv_vec_spot.py, rerun_acert3_spot.py
- **logs/:** ref_gscalar_E1.out, ref_gscalar_E1_n7.json, ref_n16_post.json, ref_crossover.json, rerun_conv_vec_spot.{json,out}, rerun_acert3_spot.json
- **lean/:** LineN16Arith.lean, build.log
- **SHA256.txt**
