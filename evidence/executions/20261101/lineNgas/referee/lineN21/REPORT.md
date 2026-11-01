# Referee report lineN21: N21 claims to close H4 (core→true conversion of the interaction constant)
Grok Bot (independent referee), 2026-11-01, 09:54–10:09 Asia/Yekaterinburg (UTC+5).
Nothing under /workspace/bgs-lineN was modified. The author's code was only imported or copied; reruns write to /workspace/audit/lineN21/logs.

## Verdict: **READY AFTER FIXES (F1–F9)**
- I re-derived all three lemmas line by line. Lemma C and Lemma Q are correct as written.
- Lemma D^T is correct as implemented, but its written §4 step 4 is only a sketch, and the code's Ψ^max formula is not a valid bound as written. That formula is dominated by another term, so no number changes (F1, F2).
- Every headline number reproduces, including from an independent re-implementation of Lemma Q and Lemma D^T.
- The crossover is confirmed.
- The remaining fixes are wording, provenance and overstatement fixes.
- No fix changes δ_true ≤ 5.0313e-6, p₁ = 1397 or the first prime 1399.

## 1. Integrity, provenance and timestamps
- **Manifest.** `sha256sum -c SHA256_N21.txt`: all 47 entries OK. Unlisted files: the manifest itself (it has no self-hash, unlike SHA256_N.txt) and `__pycache__`.
- **Times vs file mtimes (UTC+5).** Mostly consistent. Nothing looks fabricated, but there are these inconsistencies:
  - NOTES says entries after 09:41 were "written live". Its 09:47 entry (tail_DT 40..200) does not fit: `tail_DT_40_200.{json,out}` have mtime 09:45:30. It also predates the 09:48:06 `tail_DT.py` (the KK parameter was added later). The current code reproduces that file exactly (see §3e), so this is cosmetic.
  - The G ≤ 15 **replay was launched ~09:23 with the pre-patch `conv_c.py`** (mp.dps = 34, no `keep=` hook). The file was patched at ~09:30 and again at 09:34 while the run continued. The manifest hash is of the later file. I re-ran 6 replay windows (G = 0, 3, 15) with the current file: r and E are **bit-identical** (ΔE = 0, Δmid = 0). The report should state this provenance.
  - `logs/tail_DT_40_60.json` (09:36) is the superseded first version (crossL with Γ_j, T(40) = 3.41e-7). §8 lists it under "tail_DT_*.json" without marking it as superseded.
- **Lean.** Rebuilt in /workspace/audit/lineN12/lean/proj (Lean v4.33.1, pinned Mathlib).
  - `lake exe cache get`: "No files to download, Already decompressed 8690 file(s)". Mathlib was not rebuilt.
  - `lake env lean LineN21Arith.lean` gave **EXIT 0** with no warnings (lean/build.log, 09:59:37–09:59:46).
  - No sorry, admit, axiom or native_decide.
  - The file has **23 theorems, not 24** as the report says.

## 2. Line-by-line proof check
### Lemma C [P]: verified
- **T-structure.** ψ_T = (ψ_A, 0) and Φ_T = (Φ_A, X̂₀Φ_A) are the s-eigenvectors of T₀. ψ_TP^TΦ_T = ψ_A𝒜Φ_A holds exactly ✓.
- **C1.** The quotient rule with c_A = ψ̃Π_AΦ̃ (Π_A² = Π_A) is correct:
  - |c_A| ≥ den1 = |fl(ψΦ)| − eps_p − ‖ψ̃‖ER;
  - |ψ̃𝒜Φ̃/ψ̃Φ̃| ≤ |r̂| + rad;
  - ‖ψ_A𝒜‖ ≤ B₀ + EL·GA ✓.
- **C2.**
  - The telescoping P − P^T = Σ P_{>k}ℰ_kP^T_{<k} is correct.
  - φ_k is correct: core part ≤ u_{k−1}, far part ≤ xs·u_{k−2}, and the k = 1 term carries the far component X̂₀Φ_A ✓.
  - Gronwall: x_k ≤ b_k + (q−1)Σ_{j>k}x_j, and β_k = b_k + b_max(q^{n−k} − 1) dominates it by induction. Base case: x_n = ‖ψ_T‖ ≤ b_n because GA ≥ 1 ✓.
  - GL = GT(1 + Fs·GT)^n bounds every sub-product of the true operators (subset expansion, GT ≥ 1) ✓.
- **C3** (the term the H4/claim-322 closure condition requires).
  - Π rank one gives Tr(ΠP) = ψ_TΠPΠΦ_T/c, and ψ_TΠ_T = ψ_T.
  - The numerator expansion ψ_TPΦ_T + ψ_TΔPΦ_T + ψ_TPΔΦ_T + **ψ_TΔPΔΦ_T** is exact.
  - Write N₀ = ψ_TPΦ_T and c₀ = ψ_TΦ_T = c_A. Then N/c − N₀/c₀ = (N − N₀)/c + Tr(Π_TP)(c₀ − c)/c, with |c₀ − c| ≤ τ and |c| ≥ den1 − τ.
  - VPf, VPb and GL bound the **true** ‖PΦ_T‖, ‖ψ_TP‖ and ‖P‖ ✓.
  - The second-order **dPi²·‖ψ_T‖‖Φ_T‖·GL term is present in the statement and in code** (conv_c.py l.110) ✓.
- **C4** ✓.
- **C5.** The Duhamel expansion is correct: ψ_μ(L₀/μ)^k = ψ_μ, sup‖(L₀/μ)^k‖ ≤ Cpow = 3246.8 (N8, conservative), and the result is expm1. Further:
  - Φ_μ = ΠΦ_T and ψ_μ = ψ_TΠ/c, so Φ_μψ_μ = Π;
  - ‖PΦ_μ‖ ≤ VPf + GL·dPi‖Φ_T‖ ✓.
- **cond vs √cond (F21-1).** N13 V1 certifies c_lo²I ≤ H ≤ c_hi²I. So ‖M‖₂ ≤ (c_hi/c_lo)‖M‖_H, and **cond = 21.103 is correct**. N15 conv.py l.15 and N16 conv_vec.py used √cond, which was **non-conservative** (an error, not just a style choice). F21-1 is confirmed.
- **Inputs taken as certified, not re-checked here:** N8 (Pert, Xn, dPi, N1, Cpow, mus, normPi), N13 V1/V2/V3b, the N15 N_H table and residual formula (lineN16 N16-3: values never independently recomputed), Line F F2, and the N6 symmetry.

### Lemma Q [P] + [CA] constants: verified
- (T₀/s)^kQ_T = ((ÂQ_A)^k v_c, X̂₀(ÂQ_A)^{k−1}v_c). The far input is killed, and Q_A commutes with Â. This gives m_T(k) for k ≥ 2 and m_T(1) = cond·κ' + xs‖Q_A‖ ✓.
- **κ'.**
  - N13's Q̃ is I − Φψ (unnormalised; b_arb.py l.40). δ_Q = ‖Π_A − Φ̃ψ̃‖ includes the |1 − c_A| normalisation ✓.
  - ‖Â(Q_A − Q̃)‖_H ≤ (1+η)·cond·δ_Q uses V2 ✓.
- **Resolvent bounds.** R_A uses the Neumann series with |s|κ' < 0.862. The block bound for R_T is conservative. The contour identity uses L₀^kQ − T₀^kQ_T = (2πi)^{−1}∮ z^k R_T E R_L dz with ‖R_L‖ ≤ S_T/(1 − Pert·S_T) ✓.
- **K₀.** The code takes the max over m(1..3) only. That is valid because m(k) is strictly decreasing for k ≥ 2 (srκ' < 1 and 1/|μ| < 1) ✓.
- **Independent arb recomputation from raw N8/N13 inputs** (code/ref_DT.py):

  | constant | value |
  |---|---|
  | κ' | 0.450000469 |
  | δ_Q | 8.8679e-10 |
  | ‖R_A‖ | 146.4276 |
  | S_T | 914.673 |
  | Rem | 1.59043e-3 |
  | m₁ | 33.6898 |
  | m₂ | 34.8095 |
  | K₀ | 56.7776 |
  | M_ρ | 127.504 |
  | ℓ | 1881.52 |

  All agree with the tail_DT CONST to ≥ 11 digits. Every Lean decimal is a valid upper (or lower) rounding: m₁ < 33.69 is tight but correct, and so are xs, ‖Q_A‖, cond, δ_Q, τ = 6.13735e-4 and den1.

### Lemma D^T: [P] after F1–F2 (written step 4 is currently [P-sketch]; the implementation is verified)
- **Twist splitting.** I checked it independently with my own twist formula at mp.dps = 400: for G ∈ {3, 15, 16, 36, 37, 60}, all 100 pairs, both seeds, t ∈ [−G−60, 60], max |d_t − d^i_t − d^j_{t+G}| mod 1 = 0 ✓.
- **Decomposition identity.** r_ij − r_ir_j = ψR^iQL^jΦ + ψ(R − R^i)LΦ + ψR^i(L − L^j)Φ − (α_ib_j + a_iβ_j + α_iβ_j) is algebraically exact ✓.
- **Main term Y·X.** Q² = Q. Duhamel from the anchors with free factor m(·) is correct ✓. The anchor condition |e|λ^{…} < 0.45 guarantees red(x) = x, so |d_t| = |e|λ^t (this is not stated in the text; F2).
  - W^R = cov(β_{−D0−jlo}) and W^L = vec(D0 − jlo): the indices are correct.
- **Cross-term Gronwall steps.** I reconstructed every term and each one is correct:
  - **crossR:** composite-vs-single vector Gronwall, sup‖v_t‖ ≤ V₀/(1 − Γ_iσ_R), with V₀ = Φ^max_i|ψLΦ| + Γ_i‖QLΦ‖;
  - **crossL:** covector-side split ψR^i = a_iψ + ψR^iQ; the Q is absorbed into Y, so no ‖Q‖ factor is needed;
  - **α_i, β_j:** one-sided Duhamel with K₀e^{K₀σ};
  - **psiv, Qv:** composite L vs L^j via Γ_je^{Γ_jσ_L}.
- **Γ = K₀²e^{K₀σ}GL(1 + C4).** This is valid: the left and right tail factors K₀e^{K₀σ_L}·K₀e^{K₀σ_R} multiply to it.
- **Φ^max** must also bound partial products that start at the cut c, inside the left tail. That holds because the Duhamel tail bound is monotone in the tail set. This should be stated (F2).
- **Ψ^max bug (F1).** Code l.66 uses cov(max_k b_k) as the window-interior covector bound. A valid bound needs max_k cov(β_k), and β_k > b_max where b_k is maximal and k < n. Measured over all 50 singles, max_k cov(β_k)/cov(max b) is up to 1 + 2.9e-5, so the code's term is **not** an upper bound. However, the other term K_x·cov(β₀) exceeds both by a factor ≥ 4.59, so **Ψ^max and every T(G) are unchanged**: my corrected implementation gives T(G) identical to the code's to all printed digits.
- **dev step.** |x³ − y³| ≤ |x − y|(|x|² + |x||y| + |y|²) with |x − y| ≤ Δ_A|y_B| + |y_A|Δ_B + Δ_AΔ_B ✓.
- **Uniformity of the geometric remainder (G > 60).**
  - m(k) ≤ M_ρρ^k holds for **all** k analytically: both summands of m(k)/ρ^k decrease for k ≥ 2, and M_ρ covers k = 0, 1, 2.
  - CY and CX are correct, including the extra 1/ρ on the X side.
  - Every cross or normalisation term carries at least one σ factor with λ^{−D_j} and λ^{−D_i−1} ≤ λ^{−G/2}, and all other prefactors decrease in G. So cross(G) ≤ cross(60)·λ^{−(G−60)/2}.
  - The final 3(Y₀ + d_max)² bound is valid ✓.

## 3. Independent recomputation (python-flint arb, /workspace/bgs-lineN/.venv)
| quantity | N21 | referee | status |
|---|---|---|---|
| Lemma C r, E on 12 windows (G = 0, 3, 15, 16, 36, 44) | logs | bit-identical | ✓ |
| Σ_{G≤15} \|dev\| (1350 pairs; own arb aggregation, own balls) | 2.2101666e-6 | 2.2101666e-6 (2.21016658e-6) | ✓ |
| Σ_{G=16..36} box (2100 pairs, 100/G, no duplicates) | 2.7126552e-6 | float sum of uppers 2.7126552e-6; arb-accumulated 2.7126571e-6 | ✓ (see F8) |
| per G box, G = 15 / 16 / 36 | 1.2901e-7 / 1.2903e-7 / 1.2932e-7 | same | ✓ |
| T(36), T(37), T(38), T(40), T(50), T(60), own D^T code | 1.8261e-7, 6.1720e-8, 2.6857e-8, 4.9386e-9, 1.5974e-12, 5.4386e-16 | identical to 6 digits | ✓ |
| Σ_{37..60} | 1.0842557e-7 | 1.0842557e-7 (rerun of tail_DT 36 60 16: identical) | ✓ |
| remainder G > 60 | 3.0377e-13 | 3.0377e-13 (rerun) | ✓ |
| tail_DT 40..200 (KK = 18) | Σ 8.8289e-9, remainder 1.033e-52 | identical (rerun) | ✓ |
| KK = 16 vs KK = 18, G = 40..60 | "agree to 4 digits" | max rel. diff 9.9e-4 (**3 digits**) | F4 |
| total δ_true | 5.0312476e-6 < 5.0313e-6 | most conservative accumulation: 5.0312495e-6 < 5.0313e-6 | ✓ |
| F21-2: twists at dps 34 vs 300 (all 100 pairs/G, mod 1) | rel. err. 1.7e-16 @22, 1.5e-11 @30, 6e-4 @40; G ≤ 20 exact | 0 for G ≤ 20; 1 ulp (1.9e-16) @21–23; 4.4e-15 @25; 2.0e-11 @30; 1.4e-7 @35; 1.2e-3 @40 | ✓ confirmed (onset G = 21, at ulp level) |
| F21-4 medians, pair windows | per-step 2.3e-8; dPi 4.4e-4; E/\|r\| median 5.2%, max 3.1 | replay pairs (2700): 2.50e-8; 4.49e-4; 4.2%; 3.12. Replay + ext (8616): 2.83e-8; 5.0e-4; 4.65%. err_dPi dominates in 2700/2700 | qualitatively ✓; figures not reproduced (F6) |
| singles E/\|r\| | 1.9e-3 to 3.7e-3 | 1.94e-3 to 3.69e-3 | ✓ |

## 4. Crossover (own mpmath code, 60 digits, exact K_p = 4h_p² + 3)
| δ | p₁ (envelope) | margin at p₁ | margin at p₁ − 1 | first prime | G(1399) vs Robin |
|---|---|---|---|---|---|
| 5.0313e-6 | **1397** | +0.02046 | −2.09e-4 | **1399** | 13.0564 vs 12.9939 |

- There are no violations for primes ≤ 5000.
- Monotonicity: G′(1397) = 0.021952 > 2e^γ/2795 = 0.0012745 ✓.
- Reproduces 1386, 1390, 1390 for δ = 5.14476e-7, 2.470e-6, 2.2102e-6.
- The script is verbatim N19b apart from comments and the output path (diffed).
- Note: p₁ = 1397 is knife-edge (Δδ ≈ 4e-9 decides between 1396 and 1397), but 1396 is not prime. **The first prime 1399 is robust** for δ up to about 6.3e-6.

## 5. Tags each claim deserves
| claim | tag |
|---|---|
| Lemma C, incl. the dPi² term | **[P]** (conditional on the certified inputs listed in §2) |
| δ_true(G ≤ 15) ≤ 2.2102e-6 | **[P] + [CA-fp]** (boxes), arb post-processing |
| G = 16..36 box bound ≤ 2.7127e-6 | **[P] + [CA-fp]** |
| Lemma Q (K₀ < 56.78, Rem < 1.591e-3) | **[P] + [CA]** constants (arb from certified inputs; Lean arithmetic) |
| Lemma D^T | **[P-sketch] as written → [P] after F1–F2** (implementation verified) |
| G = 37..60 ≤ 1.0843e-7; remainder ≤ 3.0e-13 | **[P] (after F1–F2) + [CA-fp]** anchors + arb sums; remainder uniform ✓ |
| total δ_true ≤ 5.0313e-6 | **[P] + [CA-fp]** (after F1–F2); **not [CA]** |
| p₁ = 1397, first prime 1399 | **[P-arith]** ✓ |
| F21-1 (cond, not √cond) | **confirmed**; the N15/N16 factor was non-conservative |
| F21-2 (dps = 34 corrupts large G; G ≤ 15 untouched) | **confirmed**; onset G = 21 at 1 ulp, material from G ≈ 25–30; v4 numbers unaffected |
| F21-3 (N16 conv_vec defects) | **not independently re-verified** (superseded code; immaterial to N21) |
| F21-4 (dPi term binding, per-step term tiny) | **confirmed qualitatively**; quoted medians off (F6) |
| H4 | **met at [P] + [CA-fp] once F1–F2 are applied**. Claim 322 → "[P] lemma + [CA-fp], refereed (lineN21)". Not [CA] |

## 6. Required fixes
- **F1 (code + text, no numerical change).** In tail_DT.py l.66, replace `cov(bmax)` with `max(cov(beta[k]) for k)`. State Ψ^max = max{K_x·cov(β₀), max_k cov(β_k), ‖ψ_μ‖(1 + K₀σe^{K₀σ})}. The referee verified that T(G) is unchanged.
- **F2 (text).** Write Lemma D^T step 4 out explicitly. It needs:
  - the bounds for α_i, β_j, |a_i| ≤ |r_i| + |α_i| and |b_j| ≤ |r_j| + |β_j|;
  - ‖(L − L^j)Φ_μ‖ ≤ Γ_je^{Γ_jσ_L}σ_LΦ^max_j;
  - crossR ≤ Ψ^max_iσ_RV₀/(1 − Γ_iσ_R), with V₀ = Φ^max_i(|b_j| + ‖ψ_μ‖·‖(L − L^j)Φ_μ‖) + Γ_i(X + ‖Q‖·‖(L − L^j)Φ_μ‖);
  - crossL ≤ (|a_i|Ψ^max_j/(1 − Γ_jσ_L) + YΓ_je^{Γ_jσ_L})σ_LΦ^max_j;
  - why Φ^max covers partial products starting at the cut (Duhamel monotone in the tail set);
  - the no-wrap anchor condition |e|λ^{…} < 0.45;
  - where Γ = K₀²e^{K₀σ}GL(1 + C4) comes from (left × right tail).
- **F3 (Lean / report).**
  - "24 theorems" → **23**.
  - The `budget` docstring "margin > 100×" is false. A_bad^KP + δ_true = 7.094e-6 vs Re Λ_lo′ = 6.234e-4 is a factor of **≈ 88×**. The `/87` divisor was chosen just below that ratio.
  - State that the N15 `kp_budget` form (< Re Λ_lo′/200) **no longer holds**.
  - The proposed v5 diff must also update the H3 row "A_bad^KP + δ_int = 2.5774e-6 (kp_budget)" to the new sum. It is currently missing.
- **F4.** "Per-G values agree with KK = 16 to 4 digits" → "to 3 digits (max rel. diff 1.0e-3)".
- **F5.** §3: "G = 16..44, 100 pairs each" → "G = 16..43, 100 pairs each (G = 44 has 93; G = 44–47 partial, unused)".
- **F6.** §1 F21-4 and the Lemma C error line: the quoted per-step median 2.3e-8 and pair E/|r| median 5.2% do not match the logs. Either give the row set or correct them to 2.5e-8 / 4.2% (replay pairs) or 2.8e-8 / 4.65% (replay + ext).
- **F7 (provenance).** State that the replay rows came from the pre-patch conv_c.py (dps = 34, launched ~09:23) and that the current file reproduces them bit-identically. Correct the NOTES "09:47" entry to 09:45 (file mtime). Mark tail_DT_40_60.json as superseded. Add a self-hash for SHA256_N21.txt.
- **F8 (optional rigor).** f_postC accumulates per-G uppers in plain float without upward rounding (effect ~1e-20). Accumulate in arb or round up. With arb accumulation the 16..36 piece is 2.712657e-6, so the Lean input 2.7126552e-6 should become 2.712658e-6. The total stays < 5.0313e-6 (5.0312495e-6).
- **F9 (v5 wording).** Label H4 "[P] (N21 Lemmas C, Q, D^T; refereed lineN21) + [CA-fp]; inputs N8/N13/N15/F2/N6 as certified, N15 N_H table values not independently recomputed". Keep F21-2 in the errata with onset "G ≥ 21 (ulp), material G ≳ 25".

## 7. Artifacts (/workspace/audit/lineN21)
- **code/:** ref_DT.py (independent Lemma Q + D^T, arb), ref_post.py (own box aggregation), ref_twists.py, ref_twists2.py, ref_twists_lib.py (F21-2 and twist splitting), ref_crossover21.py, rerun_convC_spot.py, rerun_tail_DT.py (author's code, output path redirected)
- **logs/:** ref_DT_KK16_fix{0,1}.{json,out}, ref_post.json, ref_twists.json, ref_twists_mod1.json, ref_crossover21.json, rerun_convC_spot.{json,out}, rerun_tail_DT_36_60_KK16.{json,out}, rerun_tail_DT_40_200.{json,out}
- **lean/:** LineN21Arith.lean (copy), build.log (EXIT 0)
- **SHA256.txt**
