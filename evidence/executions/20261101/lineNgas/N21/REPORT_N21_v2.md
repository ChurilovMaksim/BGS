# REPORT N21 v2: closing H4 (core→true conversion of the interaction constant), referee fixes F1–F9 applied

Grok Bot, 2026-11-01, 10:09–10:20 (UTC+5).
- v1 (`REPORT_N21.md`, 09:54) is kept **unchanged**.
- Referee report: `/workspace/audit/lineN21/REPORT.md`, verdict READY AFTER FIXES F1–F9.
- This v2 supersedes v1 wherever they differ. §9 lists the errata and provenance.

Tags: [P] proof, [P-sketch], [CA] arb-certified, [CA-fp] float with the IEEE standard rounding model, [N] numerical evidence, [H] heuristic.

## 0. Result (v2)

| item | value | label |
|---|---|---|
| **Lemma C**: two-sided vector conversion incl. the dPi² term (§2) | statement and proof as in v1 §2, verified line by line by the referee | **[P]** (conditional on the certified inputs, §7) |
| δ_true, coded pairs G ≤ 15 (1350 pairs) | ≤ 2.2101666e-6 | [P] + [CA-fp] boxes, arb post-processing |
| δ_true, 16 ≤ G ≤ 36 (box widening, 2100 pairs) | ≤ **2.712658e-6** (v1: 2.7126552e-6; F8) | [P] + [CA-fp] |
| **Lemma Q** | K₀ < 56.78, Rem < 1.591e-3 | [P] + [CA] constants |
| **Lemma D^T** (difference form; step 4 now written out, §4) | G = 37..60: ≤ 1.0842557e-7; G > 60: ≤ 3.04e-13 | **[P]** (after F1–F2) + [CA-fp] anchors, arb sums |
| **δ_true (all G)** | **≤ 5.0313e-6** (conservative accumulation 5.0312495e-6) | [P] + [CA-fp], **not [CA]** |
| A_bad^KP + δ_true | 7.0942e-6 < 7.0944e-6 < Re Λ_lo′/87, a margin of **≈ 88×** (v1 wrongly said > 100×) | Lean `budget` |
| N15 `kp_budget` form (< Re Λ_lo′/200) | **no longer holds**: 7.094e-6 > 3.117e-6 | Lean `kp_budget_200_fails` |
| crossover p₁ | all p ≥ **1397**; **first prime 1399 (unchanged)**; no violations for primes ≤ 5000; monotone | [P-arith] (referee reproduced it at 60 digits) |
| Lean `lean/LineN21Arith_v2.lean` | **24 theorems**: v1's 23 (v1 said "24", which was wrong), with the final-δ block replaced by 3 theorems. EXIT 0; no sorry, native_decide, admit or axiom | [P] arithmetic |

**H4 status: met at [P] + [CA-fp]** (N21 Lemmas C, Q and D^T; refereed in lineN21). It is **not [CA]**. Remaining caveats (§7):
- The window chains are float with a rigorous rounding model, not arb.
- **The closure relies on the N15 N_H table** (`N15/logs/nh_table_rig_2048.json`, claim 323), whose **values were never independently recomputed**. It enters GA and hence GT, GL, Γ, every Lemma C box and every D^T anchor.
- Further inputs are taken as certified: N8, N13 V1/V2/V3b, the N15 residual formula, Line F F2 and the N6 symmetry.

## 1. Findings (v1 §1, corrected)
- **F21-1** (cond = c_hi/c_lo, not √cond): confirmed by the referee. The N15/N16 √cond factor was **non-conservative** (an error), although it only affected terms that were negligible or vacuous there.
- **F21-2** (digits.py mp.dps = 34): confirmed. Onset is **G ≥ 21 at ulp level** (1.9e-16 at G = 21–23), and it becomes material from **G ≳ 25** (4.4e-15 at 25, 2e-11 at 30, 1.4e-7 at 35, 1.2e-3 at 40). G ≤ 20 is exact, so v4 (G ≤ 15) is unaffected. All N21 G ≥ 16 data use dps = 160.
- **F21-3** (N16 conv_vec defects): not independently re-verified by the referee. That code is superseded and the point is immaterial to N21.
- **F21-4** (corrected figures, F6). In v1 the medians were over window A only. Over both windows:

  | row set | windows | per-step (C2) median | C3 median | E/\|r\| median | E/\|r\| max | C3 dominant |
  |---|---|---|---|---|---|---|
  | replay pairs | 2700 | 2.50e-8 | 4.49e-4 | 4.23% | 3.12 | 2700/2700 |
  | replay + ext pairs | 8616 | 2.83e-8 | 5.01e-4 | 4.65% | 3.12 | 8616/8616 |

  Singles: E/|r| ∈ [1.94e-3, 3.69e-3].

## 2. Lemma C [P]
Unchanged from v1 §2 (statement C1–C5 and proof steps 1–7). The referee verified every step, including the exact four-term numerator expansion with the second-order term ψ_TΔPΔΦ_T, which is bounded by dPi²‖ψ_T‖‖Φ_T‖·GL (conv_c.py l.110).

## 3. G ≤ 15 and box widening [P + CA-fp]
- The replay of all 1560 N15 jobs gives Σ_{G≤15}|dev| ≤ 2.2101666e-6.
- The ext runs give box values for **G = 16..43 with 100 pairs each**; G = 44 has 93 pairs and G = 44–47 are partial and unused (F5).
- Per-G box sums are now **accumulated in arb** (F8; `f_postC.py` v2 → `logs/f_postC_v2.json`). This gives Σ_{16..36} = 2.71265528e-6. The referee's most conservative accumulation from its own balls is 2.7126571e-6, so v2 uses **2.712658e-6**, which covers both. The bound is flat at ≈ 1.29e-7 per G.

## 4. Lemma Q and Lemma D^T [P]
Lemma Q is as in v1 §4. The referee recomputed every constant independently in arb, with agreement to ≥ 11 digits.

**Lemma D^T, notation.**
- Pair (i, j, G, h, σ); cut c = −D_i with D_i = ⌊G/2⌋ and D_j = G − D_i.
- R and L are the composite products for t ≥ c and t < c. R^i and L^j are the single-i and single-j products over the same ranges; L^i and R^j are the complementary single products.
- Π = Φ_μψ_μ and Q = I − Π.
- ℓ = 2πN1/|μ|.
- σ_R = ℓ|e2_j|λ^{−D_j}/(1 − λ^{−1}) and σ_L = ℓ|e1_i|λ^{−D_i−1}/(1 − λ^{−1}).

**Step 1 (twist splitting) [P].** d_t ≡ d^i_t + d^j_{t+G} (mod 1). The referee checked this at dps = 400 for G ∈ {3, 15, 16, 36, 37, 60}, all 100 pairs: the maximum deviation is 0.

**Step 2 (exact identity).**

  r_ij − r_ir_j = ψ_μR^iQL^jΦ_μ + ψ_μ(R − R^i)LΦ_μ + ψ_μR^i(L − L^j)Φ_μ − (α_ib_j + a_iβ_j + α_iβ_j)

where a_i = ψ_μR^iΦ_μ, α_i = ψ_μR^i(L^i − I)Φ_μ, b_j = ψ_μL^jΦ_μ and β_j = ψ_μ(R^j − I)L^jΦ_μ.

**Step 3 (no-wrap condition and main term).**
- An anchor D0 is admissible only if |e1_i|λ^{−D0−1} < 0.45 (resp. |e2_j|λ^{−D0} < 0.45). Then red(x) = x on the background, so |d^i_t| = |e1_i|λ^t for t ≤ −D0 − 1 and |d^j_s| = |e2_j|λ^{−s} for s ≥ D0. The same condition holds at the cut for σ_R and σ_L (asserted in code).
- Using Q² = Q and Duhamel from the anchor:

  |ψ_μR^iQ·QL^jΦ_μ| ≤ Y_i(D_i)·X_j(D_j), with

  Y(D) ≤ W^R(D0)[m(D − D0) + K₀e^{K₀σ_i}ℓ|e1| Σ_{t=−D}^{−D0−1} λ^t m(t + D)] and X(D) ≤ W^L(D0)[m(D − D0) + K₀e^{K₀σ_j}ℓ|e2| Σ_{s=D0}^{D−1} λ^{−s} m(D − 1 − s)].

  Y and X are minimised over the admissible D0.

**Step 4 (cross and normalisation terms; written out per F2).**

*Ingredients.*
- **Γ.** Every contiguous sub-product of a single chain splits into a left-tail part (≤ K₀e^{K₀σ_left}, Duhamel), a window part (≤ GL(1 + C4)) and a right-tail part (≤ K₀e^{K₀σ_right}). With σ = σ_left + σ_right this gives **Γ = K₀²e^{K₀σ}GL(1 + C4)**.
- **Ψ^max** (F1, corrected in code) is a sup over t of ‖ψ_μ∏_{u>t}L_u‖:

  Ψ^max = max{K_x·cov(β₀), max_k cov(β_k), ‖ψ_μ‖(1 + K₀σe^{K₀σ})}, with K_x = K₀e^{K₀σ}.

  The three entries cover t left of the window, inside it and right of it. Here cov(β) = (1 + C4)[(β + ‖ψ_T‖dPi·GL)/(den1 − τ) + ‖ψ_μ‖η·GL].
- **Φ^max** = K_x·max_k vec(k), a sup over t of ‖∏_{u<t}L_uΦ_μ‖, where vec(k) = (1 + C4)[φ_{k+1} + Fs·GL·Σ_{l≤k}φ_l + GL·dPi‖Φ_T‖ + GL‖Φ_μ‖η].
  - It also bounds partial products that start at the cut c, inside the left tail. The Duhamel tail bound ‖∏_{u∈S}L_uΦ_μ − Φ_μ‖ ≤ ‖Φ_μ‖(e^{K₀σ(S)} − 1) is monotone in the tail set S, so replacing the full left tail by a sub-tail only lowers it. The same holds for covectors.

*Bounds.*
- **(a) α_i and β_j.** By Duhamel with (L₀/μ)Φ_μ = Φ_μ and ψ_μ(L₀/μ) = ψ_μ:
  - |α_i| ≤ Ψ^max_i·K₀σ_Le^{K₀σ_L}‖Φ_μ‖;
  - |β_j| ≤ ‖ψ_μ‖K₀σ_Re^{K₀σ_R}Φ^max_j;
  - |a_i| ≤ |r_i| + |α_i| and |b_j| ≤ |r_j| + |β_j|.
- **(b) Composite left part.** Write L − L^j = Σ_{t<c}[∏_{t<u<c}L_u](L_t − L^j_t)[∏_{u<t}L^j_u]. The composite factor is ≤ Γ_je^{Γ_jσ_L} (operator Gronwall), so

  δ_L := ‖(L − L^j)Φ_μ‖ ≤ Γ_je^{Γ_jσ_L}σ_LΦ^max_j.

- **(c) crossR = ψ_μ(R − R^i)LΦ_μ.** Telescope R − R^i = Σ_{t≥c}[∏_{u>t}R_u](R_t − R^i_t)[∏_{c≤u<t}R^i_u].
  - Covector Gronwall gives sup_t‖ψ_μ∏_{u>t}R_u‖ ≤ Ψ^max_i/(1 − Γ_iσ_R).
  - Split v = LΦ_μ as v = Φ_μ(ψ_μv) + Qv, with |ψ_μv| ≤ |b_j| + ‖ψ_μ‖δ_L and ‖Qv‖ ≤ X_j + ‖Q‖δ_L. Then sup_t‖∏_{c≤u<t}R^i_u v‖ ≤ V₀ := Φ^max_i(|b_j| + ‖ψ_μ‖δ_L) + Γ_i(X_j + ‖Q‖δ_L).
  - Hence **crossR ≤ Ψ^max_i·σ_R·V₀/(1 − Γ_iσ_R)**.
- **(d) crossL = ψ_μR^i(L − L^j)Φ_μ.** Split the covector as ψ_μR^i = a_iψ_μ + ψ_μR^iQ, with ‖ψ_μR^iQ‖ ≤ Y_i. Then:
  - the first part, propagated through the composite left factors, is ≤ |a_i|Ψ^max_j/(1 − Γ_jσ_L);
  - the second is ≤ Y_iΓ_je^{Γ_jσ_L};
  - so **crossL ≤ (|a_i|Ψ^max_j/(1 − Γ_jσ_L) + Y_iΓ_je^{Γ_jσ_L})·σ_L·Φ^max_j**.
- **(e) Δ_W.** For each window W ∈ {A, B}:

  Δ_W ≤ Y_iX_j + crossR + crossL + |α_i||b_j| + |a_i||β_j| + |α_iβ_j|

  The code asserts Γ_iσ_R < 1/2 and Γ_jσ_L < 1/2.

**Step 5 (dev).** dev ≤ |x − y|(|x|² + |x||y| + |y|²) with |x − y| ≤ Δ_A|y_B| + |y_A|Δ_B + Δ_AΔ_B. This uses W(σe) = W(e) [P, N6].

**Step 6 (remainder for G > 60).** As in v1. The referee confirmed uniformity: m(k) ≤ M_ρρ^k holds for all k, and every cross term scales ≤ λ^{−(G−60)/2}. ∎

**F1 effect.** After the code fix (`tail_DT.py` l.66–67), the v2 reruns `tail_DT_36_60_KK16_v2.json` and `tail_DT_40_200_v2.json` give T(G) and the remainders **bit-identical** to v1. The K_x·cov(β₀) term dominates, as the referee found.

**F4.** KK = 16 and KK = 18 agree for G = 40..60 to **3 digits** (max rel. diff 1.0e-3), not 4.

Midpoint sanity [N]: unchanged (`logs/sanity_mid.json`).

## 5. Final δ_true and crossover
Source: `final_delta.py` v2 → `logs/final_delta_v2.json` (arb sum = 5.03124773e-6). Lean `delta_true_sum` uses the conservative inputs:

  δ_true ≤ 2.2101666e-6 + 2.712658e-6 + 1.0842558e-7 + 3.1e-13 < **5.0313e-6**

- Budget: A_bad^KP + δ_true = 2.062875e-6 + 5.0313e-6 < 7.0944e-6 < 6.234e-4/87, a ratio of **≈ 87.9×**.
- The N15 `kp_budget` second clause (< Re Λ_lo′/200) **fails** now that the true-functional δ is used (Lean `kp_budget_200_fails`). Every downstream use that relied on the factor-200 margin must be re-checked against the ≈ 88× margin. Nothing in N21 relies on it: the crossover uses δ directly.
- Crossover at δ = 5.0313e-6 (unchanged, `logs/crossover_N21_d5.031300e-06.json`):
  - first integer p₁ = 1397 and first prime 1399; G(1399) = 13.0564 > Robin 12.9939;
  - monotone: G′(1397) = 0.02195 > 0.00127.
  - Referee note: p₁ = 1397 is knife-edge (Δδ ≈ 4e-9 decides 1396 vs 1397), but 1396 is not prime. **The first prime 1399 is robust for δ ≲ 6.3e-6.**

## 6. Lean
- `lean/LineN21Arith_v2.lean` (v1 file `LineN21Arith.lean` kept unchanged).
- Built in /workspace/audit/lineN12/lean/proj after `lake exe cache get` ("No files to download, Already decompressed 8690 file(s)"), so Mathlib was not rebuilt.
- **EXIT 0** (`lean/build_v2.log`, 10:11 UTC+5). No sorry, native_decide, admit or axiom.
- **24 theorems.** v1 had 23 (v1's "24" was a miscount). v2 replaces the final block with `delta_true_sum` (input 2.712658e-6, F8), `budget` (corrected docstring: ≈ 88×, /87) and the new `kp_budget_200_fails`. `env_slope_1397` and `lam_half` are unchanged.
- As in v1, the Lean decimals are up to ~1e-5 relative coarser than the arb constants. The referee confirmed every one is a valid upper (or lower) rounding.

## 7. Status of H4 and remaining caveats
**H4: met at [P] (N21 Lemmas C, Q, D^T; refereed lineN21) + [CA-fp].** It is not [CA]. Remaining caveats:
1. Window chain numerics (boxes and D^T anchors) are [CA-fp], not arb.
2. **N15 N_H table** (`nh_table_rig_2048.json`, claim 323): its values were **never independently recomputed** (lineN16 N16-3). The H4 closure depends on them through GA = cond·∏max(1, N_H) in every box and anchor. An independent recomputation is the main open item for H4.
3. Further inputs taken as certified, not re-checked: N8 (Pert, Xn, dPi, N1, Cpow, mus, normPi, RA), N13 V1/V2/V3b, the N15 residual formula, Line F F2 and the N6 symmetry.
4. The KP budget margin shrinks from > 200× to ≈ 88× (§5).

## 8. Proposed v5 diff (NOT applied)
```
- | H3 (KP) ... A_bad^KP + δ_int = 2.5774e-6 (kp_budget). ...
+ | H3 (KP) ... A_bad^KP + δ_true = 2.062875e-6 + 5.0313e-6 < 7.0944e-6 < Re Λ_lo'/87 (≈ 88× margin; N21 Lean `budget`);
+ |   the N15 kp_budget clause "< Re Λ_lo'/200" no longer holds with the true functional (N21 Lean `kp_budget_200_fails`). ...
- | H4 (CT) core→true conversion | OPEN; now = "difference-form ... + G > 15 true-functional tail" ...
+ | H4 (CT) core→true conversion | met: [P] (N21 Lemmas C, Q, D^T; refereed lineN21) + [CA-fp]; inputs N8/N13/N15/F2/N6 as
+ |   certified, N15 N_H table values (claim 323) not independently recomputed. δ_true ≤ 5.0313e-6 = 2.2102e-6 (G ≤ 15)
+ |   + 2.712658e-6 (16 ≤ G ≤ 36, box) + 1.0843e-7 (G ≥ 37, Lemma D^T, arb sums) + 3.1e-13 (G > 60) | N21 v2 |
- δ_true(G ≤ 15) ≤ 2.470e-6 [CA-fp numerics, P-sketch lemma]
+ δ_true(G ≤ 15) ≤ 2.2102e-6; δ_true(all G) ≤ 5.0313e-6 [P + CA-fp] (N21 v2)
- p₁: all p ≥ 1386 (core) / 1390 (δ = 2.470e-6, G ≤ 15 part only; ...); first prime 1399
+ p₁: all p ≥ 1386 (core) / 1397 (δ_true = 5.0313e-6, all G; knife-edge vs 1396, not prime); first prime 1399,
+     robust for δ ≲ 6.3e-6 [P-arith] (N21 crossover_N21.py; referee lineN21 §4)
+ Errata: F21-1 (√cond → cond; the old factor was non-conservative); F21-2 (digits.py mp.dps = 34: error from G ≥ 21 at ulp
+   level, material G ≳ 25; v4 numbers unaffected); F21-3/4 (N16 conv_vec; corrected medians in N21 v2 §1).
```
Claim proposals (repo untouched):
- 322 → "[P] lemma + [CA-fp], refereed (lineN21)";
- 302: closure conditions met;
- 318: 1397 / 1399;
- 323: keep open (N_H values not recomputed).

## 9. Errata and provenance (v1 → v2)
| # | v1 statement | v2 |
|---|---|---|
| F1 | code Ψ^max used cov(max_k b_k) | max_k cov(β_k) (tail_DT.py v2); T(G) bit-identical |
| F2 | D^T step 4 only sketched | written out (§4 step 4); D^T → [P] |
| F3 | "24 theorems"; "margin > 100×"; H3 row missing from the diff | 23 in v1 (24 in v2); ≈ 88×; kp_budget /200 fails; H3 row added |
| F4 | KK16 vs KK18 "4 digits" | 3 digits (1.0e-3) |
| F5 | "G = 16..44, 100 pairs each" | G = 16..43; G = 44 has 93; 44–47 partial, unused |
| F6 | per-step 2.3e-8, E/\|r\| 5.2% | those were window-A medians; §1 table over both windows |
| F7 | provenance | see below |
| F8 | float accumulation of per-G uppers | arb accumulation (f_postC v2); Lean input 2.712658e-6 |
| F9 | v5 H4 label | as in §8 |

**F7 provenance.**
- **Replay rows** (`convC_replay_p{0,1}.jsonl`): launched ~09:23 with the **pre-patch conv_c.py** (mp.dps = 34, no `keep=` hook). The file was patched at ~09:30 (dps = 160) and at 09:34 (keep hook) while the replay ran on the already-imported module. The v1 manifest hash is of the **later** file.
  - The referee re-ran 6 replay windows (G = 0, 3, 15) with the current file and got r and E **bit-identical**.
  - At G ≤ 20 the twists are identical at dps 34 and 160 (F21-2).
- **NOTES timing.** The entry "09:47 tail_DT 40..200" really belongs at **09:45**, the mtime of `tail_DT_40_200.{json,out}`. It was written afterwards, not live, and predates the KK parametrisation of tail_DT.py (09:48). It is annotated in NOTES_N21.md; the current code reproduces that file exactly.
- **`logs/tail_DT_40_60.json` (09:36) is SUPERSEDED.** It is the first version, with crossL bounded via Γ_j (T(40) = 3.41e-7), and is not used anywhere.
- **Manifests.**
  - v1 `SHA256_N21.txt` now has a self-hash, `SHA256_N21.txt.sha256` (convention of SHA256_N.txt).
  - v2 manifest: `SHA256_N21_v2.txt` + `SHA256_N21_v2.txt.sha256`.
  - The three code files fixed in place for v2 (tail_DT.py, f_postC.py, final_delta.py) no longer match the v1 manifest. Their exact v1 bytes are reconstructed in `code/v1/` and match the v1 manifest hashes (checked).
  - `lean/LineN21Arith.lean` is the unchanged v1 file.
