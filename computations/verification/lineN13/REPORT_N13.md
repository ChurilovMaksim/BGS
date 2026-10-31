# Line N13 — arb adapted norm, interaction-tail lemma, replay, collective tail; REPORT_N12_v2
Box clock Asia/Yekaterinburg (UTC+5), 2026-11-01 00:00–00:50. Labels: [P] proof, [P-sketch], [CA] arb/interval-certified, [N] numerics, [H] heuristic.

## 0. Summary
| item | result | label |
|---|---|---|
| (B) adapted norm in arb | V1 cond ≤ **21.103** (c_lo 0.72010, c_hi 15.1962); V2 ‖A0/s‖_H ≤ 1+1e-6; V3a ‖Q̃‖_H ≤ 1+1e-6; V3b ‖(A0/s)Q̃‖_H ≤ 0.45(1+1e-6); all 61 ‖M_n‖_H; **Lip_H ≤ 167.213, L2 ≤ 4977.59, Nsum := Σ|w_n|‖M_n‖_H/|s| ≤ 8.3288** (a d-independent one-step bound) | [CA] (`code/b_arb.py`) |
| (B) quadratic step bound | **N_H(t) ≤ 1 + 1.0e-12 + 4.26e3·t² for \|t\| ≤ 1/256** (measured 1 + 602t²). The 2×2 argument is [P]; all inputs (b1 = 32.713, c1 = 1.3911, b2 ≤ 12.503, γ = 2.3e-15, residuals ≤ 7e-16) are arb. | [CA]+[P] (`b2_quad.py`, `b3_quadeval.py`) |
| (B) core→true | ‖Pert‖ in H, relative to \|s\|: ≤ cond·Pert/\|s\| = 2.094e-8. The extension of H to far coordinates is still [P-sketch]. | [CA]+[P-sketch] |
| (D) interaction tail beyond G₀ | **Lemma D (mid-gap cut)**: dev(G) ≤ explicit single-bump constants × max(0.45, λ^{−1/2})^G. Summed over G ≥ 16 the absolute tail is ≤ **5.76e-9**. Checked at G = 10 against measured devs on all 100 type pairs: no violation, slack ≥ 1891×. | [P] structure; constants [CA] (Lip, L2, quad, Nsum, V3) + [N] (single-chain norms, core sub-product Γ) |
| erratum to N12 §2 | N12's e_tailH "best cut" was t = 0, where Q̃Φ = 0 makes K ≈ 1e-16 trivially. Its tail was therefore *exactly* the assumption dev(G₀+m) ≤ dev(G₀)·0.45^m, not a proof. Lemma D replaces it. | — |
| (C) arb replay | Running (sequential, nice 15): 1360 coded+single jobs, then 200 short types. ~6.5 s/job, so about 2.8 h in total. At 00:45, 160 jobs were done. Midpoints agree with the N12 float values (sum 4.4263e-7 both). The certified upper bound for the done pairs is 6.99e-7. | [CA for the core functional r̃]; core→true conversion for composite windows still open |
| (A) collective tail | **Not closed.** Reduced to one precise input (§4). New facts: (i) bounds over absolute configuration sums *cannot* fit the budget [P]; (ii) the ℓ³ ≤ ℓ² trick removes the sup/op-norm barrier [P]; (iii) the i.i.d. second-moment rate is ρ(𝒦) = 0.2726 < λ^{−1/2} = 0.414 [N]; (iv) Monte Carlo deep-shell sums decay fast (4e-7 → 6e-10 → 5e-11 at j = 6, 10, 14) [N]. | mixed |

## 1. (B) Adapted norm in interval arithmetic
- **Method** (`code/b_arb.py`, python-flint acb_mat, prec 96).
  - H := T*T in arb, where T is the stored binary64 Cholesky factor. The norm is *defined* by this H, so no float H enters.
  - A0 = Σ_n w_4(n)M_n is assembled from N6 cert_core arb blocks with their radii.
  - s, Φ, ψ and Q̃ = I − Φψᵀ are exact binary64 data.
  - Each statement X*HX ≤ c²H is checked as PSD of the arb matrix G = c²H − X*HX. Take the float Cholesky L of mid(G_herm) − σI; if the arb bound ‖G_herm − σI − LL*‖_F is below σ, then G ⪰ 0.
- **Results.**
  - V1: c_lo = 0.720096, c_hi = 15.196241, cond = 21.1031.
  - V2, V3a, V3b at η = 1e-6. The PSD residuals were ≤ 4e-13 against σ ≥ 5e-7.
  - All 61 ‖M_n‖_H ≤ c_n.
  - From these: Lip_H ≤ 167.2134, L2 ≤ 4977.59, Nsum ≤ 8.3288.
  - This agrees with the referee's own arb replay of V1–V3 (cond ≤ 21.0615 for their c_hi choice).
- **Quadratic constant: the first attempt failed, the 2×2 route works.**
  - A global block test K = [[G0, G1/2], [G1/2, G2]] ⪰ 0 is infeasible. It decouples (v, w), and the Φ–Q̃ coupling ~30 must then be paid against the 2η margin on Φ.
  - **2×2 route [P].** Write v = aΦ + q, with a = ψv and q = Q̃v, and w = (M + tE₁ + R)v with ‖R‖_H ≤ L2t²/2. Then:
    - nP|ψw| ≤ (1 + da′)â + nP(c1 t + ‖ψM − ψ‖_*)‖q‖ + nP‖ψ‖_* L2t²/2;
    - ‖Q̃w‖ ≤ ((b1 t + τ₁)/nP)â + (κ′ + b2 t)‖q‖ + (1+η)L2t²/2 + (1+η)Lip·t·|1 − ψΦ|·nP;
    - with â² + ‖q‖² ≤ 1 + 2γ‖ψ‖_* and ‖w‖ ≤ √(X/(1 − 2γ‖ψ‖_*)), where X = nP²|ψw|² + ‖Q̃w‖².
  - Here γ = ‖Φ*HQ̃‖_* = 2.26e-15 is the H-orthogonality defect, and every residual is enclosed in arb.
  - **Result: N_H(t) ≤ 1 + 1.005e-12 + 4253.4·t² for 0 ≤ t ≤ 1/256.** Each entry is increasing in t; the coefficient was checked on a 400-point grid.
- **Still [N]:** the 4096-point step table for |t| > 1/256. For |t| > 1/256 the certified one-step bound is only Nsum = 8.33.

## 2. (D) Lemma D — two-bump interaction decay (mid-gap cut)
- **Superposition [P].** For a composite seed e = e_i + s·e_jε^h·λ^G, the window twists satisfy d_t = d^i_t + s·d^{j′}_{t+G} (mod 1) exactly, because Tr(ζλ^u) ∈ Z.
- **Cut.** Place the cut c at the mid-gap, D_i = ⌊G/2⌋ from bump i and D_j = G − D_i from bump j. With Φψᵀ + Q̃ = I:
  r_ij − r_i r_j = ψR_i Q̃·Q̃L_jΦ + (cross tails) − (normalisations).
  - **Q̃ term.** It is ≤ Y_i(D_i)·X_j(D_j), with Y_i = ‖ψR_iQ̃‖_*, X_j = ‖Q̃L_jΦ‖_H. Both contract by 0.45 per step through the background gap (V3b, constant 1, also for covectors). This gives 0.45^G.
  - **Cross tails.** They are bounded by Γ(e^σ − 1)-type terms, with σ = Lip_H·Σ|tail twists| ~ λ^{−G/2}. Γ is the sup over contiguous sub-products of the single window: the core part is computed in float H-norm (2.1–2.9), and the steps outside the core use the certified quadratic factor.
  - **Normalisation.** |r_i − ψR_iΦ| ≤ Ψ_i·σ_L e^σ, and similarly for j.
- **Rate.** max(0.45, λ^{−1/2} = 0.414) = 0.45 per λ-step. The measured mismatch rate is 0.380 (referee). That is the sub-dominant ratio, which the Q̃ term carries; the twist tails decay at λ^{−1/2} because the cut sits at the mid-gap.
  - This corrects N12's "λ^{−1} mechanism" (N12-F2).
- **Numbers** (`code/d_decay.py`, logs/d_decay_G16.json, G = 16…64 plus a geometric continuation):
  - Σ_{G≥16} class-dev ≤ 0.249 for the worst pair (four–four, relative). The odd–odd window dev bound at G = 16 is 5.0e-4 / 1.7e-3.
  - **Absolute tail Σ|w_i||w_j|·Σ_G class-dev ≤ 5.76e-9.** This replaces N12's [H] value 3.3e-12.
  - Validation (d_decay_G10 against N12 d_merged at G = 10): bound ≥ measured on 100/100 pairs, with min ratio 1891 and median 2.4e4.
- **Remaining for full [CA]:**
  - the single-chain norms (Y, X, Ψ, Ξ, |r|) and the core sub-product sup Γ in arb. This is the same machinery as c_replay, applied to 20 single seeds.
  - the geometric continuation beyond G = 64: each term is a monotone product of geometric factors [P-sketch].

## 3. (C) arb replay of the interaction windows
- **Code.** `code/c_replay.py` (resumable jsonl; runners `run_C.sh`, then `run_C2.sh`).
  - Twists come from exact seeds in arb (the N8 core(), KK = 18).
  - The chain v ← A(d)v/s uses the cert_core blocks; r̃ = ψ̃v/(ψ̃Φ̃).
  - Jobs: 10 singles, 1350 coded pairs (ε-gap ≥ 5, G ≤ 15), then 200 short types (N12-F1).
- **Status at 00:45.** About 160/1560 jobs done. Ball radii grow with window length: 4e-10 for singles, up to 2e-5 at G = 11.
  - `code/f_post.py` gives, for the done coded pairs: Σ upper|W_ij − W_iW_j| = 6.99e-7. The midpoint sum equals the float value 4.4263e-7.
- **Not covered.** The conversion from the core functional r̃ to the true window weight for *composite* windows. With H it costs 2·dPi·Γ_X + n·Pert_H·Γ_X², where Γ_X is the sup sub-product H-norm of the composite window. That needs one float/arb matrix sweep per type and is not done.
  - For singles, N8's [CA] radii apply.
- When the job finishes: rerun `python code/f_post.py` for the δ_int (coded) and short-cluster totals.

## 4. (A) Collective short-core / uncoded tail
1. **Absolute configuration sums cannot work [P].**
   - Coded configurations already carry Σ_types|φ| ≈ 2·4.29e-4 = 8.6e-4 per site in absolute value, against Re Λ_lo′ = 6.234e-4 (the phases cancel in X_gas).
   - Any bound of the form Σ_{x uncoded}|w(x)| ≤ Σ_{configs ∋ bad cluster} ∏|z| is ≥ p·A_bad·(1 + 8.6e-4)^{p−1}.
   - It therefore exceeds the budget 2(1 + Re Λ_lo′)^p by e^{2.4e-4·p}.
   - **Hence (T) must be stated as per-site polymer activities:** every point is decomposed into polymers (coding surjectivity), and non-model polymer types must satisfy A_bad := Σ_{γ∋0, γ∉model}|z_γ|e^{a|γ|} < Re Λ_lo′ − δ_int (KP). This is the referee's "per-site activity" form, now with the reason it is forced.
2. **The cancellation that product-of-norms misses [P + N].**
   - N_H(d) ≥ 1 for every d, so ∏N_H can only grow. Yet RMS products of generic twisted steps decay: the i.i.d.-uniform second-moment operator 𝒦(Y) = Σ_n|w_4(n)|²M_nYM_n*/|s|² has **ρ(𝒦) = 0.27255** (`code/g_K.py`) [N].
   - **ℓ³ ≤ ℓ² trick [P]:** w = (r_A r_B)³, so Σ_{shell}|w| ≤ (Σ_{shell}|r_A r_B|²)^{3/2}. No sup or op-norm factor is needed, and the N7 "sup barrier N^{1.088}" disappears.
   - With N_j ~ λ^n classes of core length n and E|r_A r_B|² ~ ρ^{2n}, the shell sum is ≤ (λρ²)^{3n/2} = 0.285^n [H: i.i.d. model].
3. **Data [N]** (`code/e_shell.py`, single deep classes, 24 samples per shell):
   | shell j (\|N(α)\| ~ 2^j) | N_j | S₁ bg ¼ | S₁ bg 0 | E\|r_A\|² |
   |---|---|---|---|---|
   | 6 | 45 | 4.1e-7 | 1.6e-7 | 1.0e-3 |
   | 10 | 651 | 6.4e-10 | 3.1e-10 | 1.6e-4 |
   | 14 | 10253 | 6.2e-12 | 5.3e-11 | 7.1e-6 |
   - Single deep bumps are therefore negligible beyond j ≈ 8 (rate of E|r|² ≈ 0.14–0.30 per λ-step, consistent with ρ(𝒦)).
   - N11's flat shells (~4e-7 per shell) are multi-bump gas terms, not tail. The genuine uncoded mass is the short clusters: N11-F1 (1.7e-6, phase-checked) and N12-F1 (9.95e-7). Both are finite p-independent lists, and the 200 short types are in the replay queue.
4. **Minimal extra input (precise).** A *cluster-language second-moment certificate*:
   - Σ_{cluster words c of span n} |r_A(c) r_B(c)|² ≤ C·(λρ_c²)^n with λρ_c² < 1, over the regular digit language "internal zero-runs < g₀".
   - Equivalently: N2's e_r2_cert automaton (Fourier majorant, 441 carry states) extended by a zero-run counter (×g₀ states) and re-normalised to the H-relative second moment.
   - This replaces the box-restricted Bowen lemma (R1). In the polymer picture, clusters are digit words counted exactly, so no Bowen balls are needed. Coding surjectivity is the existence of digit expansions mod γ̄ [P-sketch].
   - Plus deep wrap-around points (core length ≳ m/2), which are G*-type (gap (b)'s Γ_out). Their per-site activity is ≤ K_stay²(Γ_out/|μ|)^ℓ with K_stay = O(10²) [N] and Γ_out/|μ| ≤ 0.746. That is negligible for ℓ ≳ 60.
   - **Why I did not run it here.** The matrix-valued version has 441·g₀·495² ≈ 10⁹ states. The scalar majorant version is cheap, but its normalisation against Re Λ needs the H-relative constant, which is not yet derived.

## 5. REPORT_N12_v2 (referee /workspace/audit/lineN12/REPORT.md)
- **F1 (required) — accepted.**
  - Of the 200 n < 5 types, only 31 are relabellings; 169 rows (95 classes: e = 12, 6, 8∓2√2, 8√2, …) are genuine uncoded short clusters with total model weight ≈ 9.95e-7.
  - They are now carried in (T) as explicit types and queued in the arb replay (`c_replay.py`, kind 'short').
  - δ_int (5.14e-7) covers coded pairs only.
  - Budget: 5.14e-7 + 9.95e-7 < Re Λ_lo′/400.
- **F2 (required) — accepted and addressed.**
  - The N12 tail was a pure assumption: its best cut was t = 0 (§0 erratum). The "λ⁻¹ mechanism" text is withdrawn.
  - Lemma D (§2) is the mid-gap-cut proof the referee suggested, with constant 1 from V3b and explicit Γ. The tail is now ≤ 5.76e-9, labelled [P]+[N constants].
- **F3 (required) — accepted.**
  - `verify_adapted.py` is [CA-float]. V1–V3 are now [CA] (here and in the referee's replay).
  - Lip_H, L2, Nsum and the quadratic constant are now [CA] (§1). The 4096-point table remains [N].
  - So the D2 per-stay constant: near-slow steps are [CA] (quadratic); steps with |δ| > 1/256 use the [N] table, or the [CA] bound 8.33 (much worse).
- **F4 — accepted.**
  - δ_int per site := Σ over coded (ordered) type pairs (i, j, h, s, G) of |w_ij − w_iw_j|, with one bump fixed at the site. Counting both orderings is a possible factor 2; it is included.
  - lambda_cert docstring: the code charges 200·|c16| = 4.4e-7 (c16 entered as 2.2e-8). Corrected copy in `N13/code/lambda_cert.py`.
  - Gaps in the window model are **circular** (the p = 37 discrepancy is wrap-around). All N12/N13 statements assume a circular gap ≥ the stated G, and for p ≥ 75 the wrap gap exceeds 16 λ-steps whenever ≤ p/7 bumps are present.
- **F5 — noted.** D1 (cone certificate) remains open.

## 6. Status of gap (a)
- (I) interaction: rate and prefactor [CA] (norm); tail Lemma D [P]+[N]; finite list in arb replay (running).
- (T): reduced to the cluster-language second-moment certificate (§4.4) plus short-cluster certificates (in the queue) plus G* for wrap-around points. OPEN.
- Y: unchanged ([H, conditional]).

## 7. Notes on the running replay
- **Ball-radius growth.** It is wrapping, not input radii: rad/|r| ≈ 1.5% at G = 13 (h = 1). Certified upper bounds therefore loosen for G ≥ 13, which is still harmless for the budget.
  - If needed, a mid-rad rerun with H-norm error propagation (growth ∏N_H instead of ‖|A|‖) fixes this.
- **Hashes.** `logs/c_replay.jsonl` and `logs/c_replay.out` are live, so they are excluded from SHA256_N13.txt. Rerun f_post.py and hash them when the job ends.
