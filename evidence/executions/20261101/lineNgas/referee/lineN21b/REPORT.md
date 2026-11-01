# lineN21b — Referee follow-up on N21 v2 (Grok Bot)
Window: 10:13–10:49 (UTC+5), Sun 1 Nov 2026. /workspace/bgs-lineN was only read, never modified. Mathlib was never built.

## Verdicts
| Task | Verdict |
|---|---|
| 1. Delta check of F1–F9, hashes, Lean v2 | **PASS** (2 cosmetic nits) |
| 2. Independent N_H table, \|t\|>1/256 (BGS-TRACE-323) | **PASS — CONFIRMED.** Full table [CA-fp]; 20 cells [CA] |
| 3. Downstream uses of the 200× kp_budget / 88× margin | **PASS for KP, H3, N14/N20 budgets. One CONDITIONAL item:** the crossover "first prime 1399" holds only with A_bad^KP = 0 |

## Task 1 — Delta check
- **Hashes.**
  - SHA256_N21_v2.txt and its .sha256 both verify. SHA256_N21.txt.sha256 also verifies.
  - code/v1/{tail_DT,f_postC,final_delta}.py match the v1 hashes.
  - The T(G) values are bit-identical to v1.
- **F1–F9.** All are applied and honest.
  - F6 explanation, re-verified: window A median 2.30e-8 (5.16 %); window B median 2.57e-8 (3.69 %).
  - Final δ_true = 5.0312477e-6 (log final_delta_v2).
  - Σ_{16..36} = 2.71265528e-6 (log f_postC_v2).
- **Lean.**
  - Setup: lean/LineN21Arith_v2.lean (sha 33b06a92…, identical to the author's file), built in the lineN12 project. `lake exe cache get` reported "No files to download"; Mathlib was not rebuilt.
  - Result: `lake env lean` gave EXIT 0 with no warnings (lean/build.log).
  - Contents: 24 theorems, including kp_budget_200_fails. No sorry or native_decide; the only match is in the header comment.
  - Axioms: `#print axioms` shows all 24 use only [propext, Classical.choice, Quot.sound] (lean/axioms.log).
- **Nits.**
  - (a) The REPORT_N21_v2 header says the work ended at 10:20, but the file mtimes are 10:12:52.
  - (b) §9 does not mention that NOTES_N21.md (now annotated) also no longer matches the v1 manifest.

## Task 2 — Independent N_H table (main)
**Object.** N_H(t) = ‖T Â_t T⁻¹‖₂, with D = 495 and all 61 terms n = −30..30 (no truncation).
- Grid: N15's grid of 2048 cells of width h = 1/2048, centred on the odd points of the 1/4096 grid. The cell bound is centre_up + Lip·h/2.

**Code.** I wrote my own code in code/nh_fp.py and did not reuse N15's rig.py.
- Coefficients w₄(n)/s come from arb.
- Each centre gets a full float SVD plus a residual certificate: ‖S‖ ≤ σ_max‖U‖‖V‖ + ‖S − UΣV*‖_F, with ‖U‖ ≤ √(1 + ‖U*U − I‖).
- A Higham γ-bound covers forming S and the residual. The largest residual term is dS ≤ 1.757e-9.
- T⁻¹ is handled through η ≥ ‖T·Ti − I‖, with η = 2e-15 against an arb value of 1.30e-15. The bound is divided by (1 − η).
- This is a different method from N15's SVD-free repeated squaring.

**Lipschitz.**
- Bound used: |N_H(t) − N_H(c)| ≤ ‖d/dt T Â_t T⁻¹‖ ≤ (2π/|s|)·Σ|n||w_n|‖T M_n T⁻¹‖/(1 − η).
- My own bound is Lip_ref = 167.19673 (logs/nh_fp_lip.json), which is ≤ N13/N15's Lip_H = 167.21345.
- I re-checked N15's argument (via N13 b_arb.py c_n from the PSD check of c²H − M*HM). It is valid.
- Every result below holds under either Lipschitz constant.

**Results** (logs/post.json; all 2048 cells computed in about 70 s using 3 low-memory processes):
| Set | #cells | max cell bound (Lip_N13) | at t | min margin vs N15 bound | cells exceeding N15 |
|---|---|---|---|---|---|
| \|t\|>1/256 | 2032 | **2.9164480** | −0.143799 (k=729) | **+3.93e-5** (k=1032) | **0** |
| cells N21 uses | 946 (from 9156 windows) | 2.9164480 | k=729 | +3.93e-5 | 0 |
| all | 2048 | 2.9164480 | k=729 | +3.89e-5 (k=1024) | 0 |

- With Lip_ref instead of Lip_N13, the max is 2.9164439.
- The N15 claimed max is 2.9165597, so my independent max sits **1.12e-4 below** N15's.
- Every cell is ≤ N15's bound for that cell. The 16 excluded cells (|t| ≤ 1/256) include none of the cells N21 uses.

**arb cross-check** (code/nh_arb.py, full acb ball arithmetic: certified norm via SVD + residual in arb):
- 20 cells computed: k = 0, 2, 3, 4, 6, 7, 10, 12, 14, 21, 24, 35, 42, 51, 72, 768, 1024, plus **k = 729 (the max cell)** and **k = 1032 (the min-margin cell)**.
- In every case fp_up − arb_up ∈ [2.0e-9, 2.44e-9] and is > 0, so the float certificate is always conservative.
  - k=729: arb centre 2.8756243768, fp 2.8756243793.
  - k=1032: arb 1.0102715626, fp 1.0102715646.
- Running arb on all cells was impractical: about 90 s and 2 GB per cell.

**Tag.**
- **[CA-fp]** for the full table. "fp" means IEEE standard-model bounds with arb coefficients; the error analysis was checked on 20 cells by arb.
- **[CA]** for the 20 arb cells, which include the max cell, so the max-cell centre is [CA].
- TRACE-323 (max 2.91656) is **confirmed, with margin**.

## Task 3 — Where the 200× / 88× margins are used
- **KP, recomputed** (code/ref_kp.py, logs/ref_kp.json).
  - At g0 = 4: S0 = 2.062875e-6, S1 = 1.793574e-5, lhs = S0 + S1/5 = **5.650022e-6 ≤ a = 5.93e-6**, a margin of ×1.0496. The criterion holds.
  - The KP criterion does **not** involve δ, so changing δ_true does not affect H3/KP.
  - g0 = 2, 3, 5, 6 also hold (×1.05).
- **Budget.**
  - A_bad^KP + δ_true = 2.062875e-6 + 5.0313e-6 = 7.0942e-6. Against Re Λ_lo′ = 6.234e-4 this gives a ratio of **87.87×**.
  - Leftover: 6.163e-4; using ln(1 + ReΛ), 6.161e-4.
  - The "/200" clause (N15 Lean kp_budget) **fails**. It held only with the core δ (241.9×) and already failed with N16's δ (137.5×).
- **What depended on /200 or /400.**
  - N15's kp_budget and N13's "/400" are display-only: nothing downstream uses the factor itself. The N21 v2 Lean replaces them with the true 87× inequality (kp_budget_200_fails, plus budget < 6.234e-4/87).
  - **N14 a_need.** C_needed scales by ≈0.9935 (0.08168 → ≈0.0812). It still passes.
  - **N20 Prop K.** The leftover "Re Λ_lo′ − S₀ − δ_true" falls from 2.764e-4 to ≈2.739e-4. It still passes.
  - **N16 row 22 (Lean budget14).** Still holds, because only 88× is needed, not 200×.
  - **THEOREM_DRAFT_v4 §2.** The B_p formula uses δ alone, which is fine at 88×.
- **Break (not caused by 200×; it is the crossover bookkeeping)** (code/ref_crossover21b.py, logs/ref_crossover21b.json):
  - The p₁ / first-prime crossover charges only δ_true and omits A_bad^KP. With δ_true = 5.0313e-6 alone: first odd 1397, **first prime 1399**, G(1399) − Robin = +0.0625.
  - If A_bad^KP is charged too (δ_eff = 7.0944e-6): first odd **1401**, **first prime 1409**, G(1399) − Robin = −0.0399.
  - The first prime stays at 1399 only for δ_eff ≲ 6.28e-6, a slack of ≈1.25e-6 over δ_true. Since A_bad^KP = 2.06e-6, this needs about 0.8 × 2.06e-6 removed from the charge.
  - v4 §2's p₁ row already lists idealisations (tails = Y = X_cross = ε = 0, n/h_p := 1, "p₁ with all budgets: not computed").
  - **Fix needed:** either (i) state "first prime 1399" as holding under A_bad^KP = 0, (ii) quote 1409 when all budgets are charged, or (iii) justify why A_bad^KP does not enter the crossover rate.

## Incident note (shared box)
- At about 10:25 (UTC+5), eight parallel arb workers of mine exhausted RAM. The OOM killer ended 3 python processes (kernel pids 490489, 490493, 490495); I believe these were my own.
- Another agent's `ref_mc.py 2 20000 11` (pid 480408) was gone afterwards. **I cannot tell whether it finished normally or was OOM-killed.** Its owner should check its output and re-run it if needed.
- I killed my remaining arb workers and switched to low-memory float code.

## Files
code/{nh_fp.py, nh_arb.py, post.py, used_cells.py, ref_kp.py, ref_crossover21b.py}; logs/*; lean/{LineN21Arith_v2.lean, build.log, axioms.log}. Manifest: SHA256.txt.
