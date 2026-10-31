# Line N15 — replay stop, REPORT_N14_v2 (F14.1 fix), collision-lemma pre-flight, KP weight
Grok Bot · 2026-11-01 · times are Asia/Yekaterinburg (UTC+5) · all jobs nice ≥ 5, one shared core.

**Labels.** [P] proof · [P-sketch] argument with steps not written out · [CA] arb ball arithmetic · **[CA-fp: IEEE standard model + libm ≤ 1 ulp]** = binary64 evaluation with explicit a-priori rounding bounds. The model is fl(a∘b) = (a∘b)(1+δ), |δ| ≤ u = 2⁻⁵³. Complex inner products of length n are bounded by √2·γ_{n+2} (Higham, Lemma 3.5), for every summation order, which covers BLAS, einsum and np.add.at. libm exp/cos/sin are assumed accurate to ≤ 1 ulp. This is not interval arithmetic. · [N] numerical evidence · [H] heuristic.

## 0. Summary
- **(0) Replay stopped** 01:41. The waiter PID 795603 was killed first, then c_replay PID 795495; no files were deleted. The 597 completed jobs (1194 windows) serve as a partial [CA] cross-check.
- **REPORT_N14_v2.** F14.1 is fixed: `code/c3_mid.py` uses derived constants and adds the etaT, dot-product and denominator terms. N_H is now SVD-free (`nh_table_rig.py`). The fixed radii are at most 6.9× the N14 radii, and the midpoints are identical.
  - **δ_int ≤ 5.14476e-7** [CA-fp: IEEE+libm]. The N14 number, rounded up as the referee asked, is 5.14416e-7.
  - ρ̄ ≤ 0.28 is re-certified **eigen-solver-free** with margin 3.49484e-6 vs 3.1e-13 (`b_cp3.py`).
  - Finite part A_bad (j ≤ 12) has been re-run with the fixed radii: 2·Σ_bad|w|_up at g₀ = 4 is 2.031569e-6 (N14: 2.031567e-6); all g₀ change by < 3e-12 absolute [CA-fp: IEEE+libm].
- **(1) Collision lemma: NOT proved.** This line produced:
  - the exact reduction to a finite carry alphabet |e| ≤ 15 [P];
  - the Bohr/torus-mean identity [P];
  - torus mean ≈ i.i.d. within 2% for n ≤ 5 [N];
  - phase-kept carry transfer for E = 1..4: rate always 0.272551 = ρ(𝒦), but the (0,0)-share 0.235, 0.150, 0.1154, 0.0931 does **not** show convergence. 1/share = 4.3, 6.7, 8.7, 10.7, i.e. +2 per unit E [N].
  - No phase-keeping certificate was built, and the box/aliasing constants were not computed (§3.4).
- **(2) KP weight** written out explicitly; the criterion holds with a = 5.933e-06 at g₀ = 4 [CA-fp finite part; P-sketch tail weighting]. The core→true conversion stays [P-sketch]: the H-product route is vacuous (§5).
- **Wrap-around exponent (corrected statement):** c < ln(1/q)·ℓ₀/ln d with q = (λρ̄²)^{3/2}. With ρ̄_true = 0.28028 this is c < 1.1718·ℓ₀/ln d = 0.6647·ℓ₀/log_λ d (ℓ₀ in λ-steps). The brief's "0.97·ℓ₀/log_λ d" uses ln(1/0.380) = 0.968 (ρ̄ = 0.30) and is correct only with **ln d**, not log_λ d (§6).

## 1. (0) Replay stop and partial cross-check
- **Kill order.** run_C2.sh (waiter, PID 795603) would have relaunched the resumable replay, so it was killed first; then c_replay.py (PID 795495) was killed. run_C.sh (789896) had already exited. N13 files are unchanged and are hashed in this manifest.
- **Partial cross-check** (`code/f_partial.py` → `logs/f_partial.json`, `logs/f_post_partial.json`, `logs/f_post2_samesubset.json`).
  - 597 jobs, 1194 windows: 0 disjoint boxes vs c2_mid.
  - The arb/mid radius ratio grows ×2.9 per G, reaching 1.26e6 at G = 15. This is the N13-F3 compounding.
  - f_post on the arb partial set: coded pairs 587, Σ|dev| ≤ 8.00e-7 [CA, partial]. The same subset from c2_mid gives 5.134e-7.
- **Against the fixed radii** (`code/c3_vs_arb.py`): 1194 windows, 0 disjoint. On the 270 windows where arb is tighter, max |mid_arb − mid_c3|/rad_c3 = 1.25e-6, so the c3 radii are ~1e6× conservative and consistent.

## 2. REPORT_N14_v2 (referee /workspace/audit/lineN14/REPORT.md)
### F14.1 (blocking): c2_mid → c3_mid with derived constants
Only N15 copies were changed (`code/c3_mid.py`, `code/rig.py`); the N14 files are frozen and hash-OK.
1. **Per-op constant (derived).**
   - Output block i receives at most M = 53 block contributions (np.add.at). Each is a complex 55-length inner product times ĉ_n.
   - The phase arg 2πnd takes 4 roundings, giving |Δarg| ≤ 4u·2π·30·½. cos/sin are accurate to 1 ulp; then C_n = fl(COEF0/s) and the product C·e follow. Together ε_c = 4.363e-14.
   - κ_der = (1+ε_c)(1+√2γ₅₇)(1+√2γ₂)(1+γ₅₃) − 1 = 5.862e-14.
   - **Used: KAP = max(1e-13, 1.25κ_der) + 2u = 1.00222e-13** (≥ 1e-13 as the referee asked). The bound applies entrywise to Xabs|v̂|.
   - The float evaluation of Xabs|v̂| is divided by (1 − γ_{K+M+6}).
2. **Data and twist terms.**
   - mid-rounding 2u relative, plus RAD·D·Σ|C_n|·‖v̂‖ = 4.96e-17·‖v̂‖.
   - Lip₂ = 2πΣ|n||C_n|‖M_n‖_F = 646.06. Frobenius is used, with no SVD.
3. **etaT term.**
   - η_T ≥ ‖T·Ti − I‖₂ is bounded by the Frobenius norm of the float product plus the rigorous matmul error: 1.92e-12.
   - ‖T‖₂ ≤ ‖T‖_F = 32.81 (rigorous; larger than the SVD 2-norm used before).
   - ‖ψT⁻¹‖ ≤ (‖fl(ψTi)‖ + √2γ_{D+2}‖|ψ||Ti|‖)/(1 − η_T) = 1.0100.
4. **Final dot product and denominator.**
   - Numerator error: npsi·e + √2γ_{497}·|ψ|·|v̂|.
   - Denominator error: ε_p = √2γ_{497}·|ψ|·|Φ| = 9.34e-14.
   - |r − r̂| ≤ E_a/(|p̂|−ε_p) + |â|ε_p/(|p̂|(|p̂|−ε_p)) + 1e-15|r̂|.
5. **N_H without an SVD** (`code/nh_table_rig.py` → `logs/nh_table_rig_2048.json`).
   - ‖S‖₂² ≤ ‖(S*S)^{2^7}‖_F^{1/2^7}, computed by scaled repeated squaring with tracked Frobenius errors (`rig.norm2_upper`). Overestimate ≤ rank^{1/512}.
   - Max over cells 2.91656; ratio to the old SVD table 1.0000373–1.0000383. For |d| ≤ 1/256 the [CA] quadratic bound is kept.
6. **Results** (`logs/c3_mid.jsonl`, `logs/f_post3.json`).
   - All 1560 jobs, midpoints identical to c2_mid. Radii at most 6.94× c2_mid, max radius 1.37e-7.
   - **coded Σ|dev| ≤ 5.144750e-7 ⇒ δ_int ≤ 5.14476e-7 [CA-fp: IEEE std model + libm ≤ 1 ulp]** (mid 5.14410e-7).
   - The old N14 value, rounded up as required, is 5.14416e-7 (referee 5.144157e-7). It is superseded because its radii were not proved.
7. **Finite part re-run** (`code/a_cert3.py`, `a_certpost3.py` → `logs/a_certpost3.json`): all 5109 classes (|N(α)| < 2¹³) re-run.

   | g₀ | 2 | 3 | 4 | 5 | 6 |
   |---|---|---|---|---|---|
   | 2Σ_bad|w|_up (c3, N15) | 6.661666e-07 | 1.287446e-06 | 2.031569e-06 | 2.804984e-06 | 3.664367e-06 |
   | N14 (c2 radii) | 6.661663e-07 | 1.287445e-06 | 2.031567e-06 | 2.804981e-06 | 3.664362e-06 |

   max rad/|r| = 0.00071. **A_bad (j ≤ 12) is unchanged at the stated precision; N14 §6 stands with the [CA-fp: IEEE+libm] label.**

### ρ̄ ≤ 0.28: eigen-solver-free (`code/b_cp3.py` → `logs/b_cp3_0.28.json`) [CA-fp: IEEE+libm]
- **Positive-definiteness without an eigen-solver accuracy assumption.** With fl-eigh output V, Λ, the residual R = W − VΛV* and E = V*V − I give λ_min(W) ≥ min Λ·(1−‖E‖) − ‖R‖. All norms are Frobenius with matmul error bounds.
- **Y_c ≻ 0:** λ_min ≥ 1.248157e-5.
- **W = 0.28Y_c − 𝒦(Y_c):** λ_min ≥ 3.49484e-6. Derived rounding: E_round = 2.74e-13. Every block product has inner length 55 (one block per (n, row block)), so κ_round = (2√2γ₅₇ + 16u + γ₆₁ + 3u)/(1−γ) = 2.68e-14 × ‖P‖_F. E_input = 3.3e-14.
- **Margin 3.494840e-6 ⇒ 𝒦(Y_c) ⪯ 0.28·Y_c, Y_c ≻ 0 ⇒ ρ(𝒦) ≤ 0.28** (CP Perron–Frobenius).
- cond(Y_c) ≤ ‖Y_c‖_F/λ_lo = 8.33e5 (rigorous, looser than 3.8e5). The core→true step gives ρ̄_true ≤ 0.280280.
- This replaces the asserted γ_n and eigvalsh backward-error constants with derived bounds. An arb residual was not needed.

### Labels, wording, manifest
- **Labels.**
  - Core→true conversion: **[P-sketch]** (everywhere in N14: §0, §2.2, §6).
  - The tensor joint-pair claim (Y_c⊗Y_c certifies ρ̄² per λ-step, N14 §2.2): **[H]**.
  - c2_mid radii: superseded by c3_mid [CA-fp: IEEE+libm].
- **Short-type wording.** "27 model relabellings + 4 relabellings to α = 4 = 31 short relabellings; 173 rows incl. α=4 (169 rows excluding α = 4); 96 classes incl. α = 4 (95 genuine + α = 4); Σ|w| = 9.970e-7". MODEL in a_certpost excludes α = 4 explicitly ({(1,0),(0,1),(2,0),(0,2)}).
- **N14 manifest self-hash.** N14 is frozen, so the hash is recorded here: `sha256(N14/SHA256_N14.txt) = def72f999543c45e89b5b75a88aa7b05a684e03b5872a89ecc5aecf596b1bb60`. Re-check at 02:22: 42/42 OK.

## 3. (1) Collision-constant lemma — pre-flight and status
Target: S2(j) := Σ_{shell j, bad}|r_A r_B|² ≤ C·2^j·2^{−βj}, β = −2 ln ρ̄/ln λ, with C ≤ C_needed(J₀=12) = 0.082 at ρ̄ = 0.28. Measured: C_emp(j) ≤ 4.4e-4 for j ≤ 12, flat in j [N; the finite part is certified].
1. **Exact carry reduction [P].**
   - Fourier-expand every step: X(d) = Σ_n N_n e(nd), n ∈ [−30, 30]. Along the cat-map twist sequence d_{t+2} = 6d_{t+1} − d_t, the torus mean of a product of X ⊗ X̄ keeps exactly the letter pairs with V(x) = Σ v_t x^t vanishing at λ and λ′ (v_t = n_t − m_t).
   - Since x² − 6x + 1 is monic irreducible, V = (x² − 6x + 1)E with E ∈ ℤ[x] (Gauss). That is, v_t = e_t − 6e_{t−1} + e_{t−2} with integer carries supported in the window.
   - **Carry bound:** e is the unique bounded solution, e = g * v. The Green kernel of 1 − 6S + S² is g(k) = λ^{−|k|}/(4√2) > 0 with Σ_k g(k) = 1/(6−2) = 1/4. So |e_t| ≤ max|v|/4 ≤ 60/4 = **15**. The carry alphabet {−15..15} is exact, not a truncation.
2. **Bohr/torus-mean identity [P].** The full exact-collision sum equals the Lebesgue mean over T² of |ψ Π X(d_t) Φ|² along the cat-map orbit. Any two consecutive twists are i.i.d. uniform, so the diagonal (e ≡ 0) part is exactly the i.i.d. second moment ψ⊗ψ̄ 𝒦ⁿ Φ⊗Φ̄.
3. **Numerics [N].**
   - Torus/i.i.d. ratio (`logs/g_torus_8_20000_1.json`, 2e4 samples): 1.001, 0.992, 0.987, 0.979, 0.979 for n = 1..5. For n ≥ 6 the samples are heavy-tailed near the slow fixed point d = 0, and the MC error dominates.
   - Phase-kept carry transfer with |e| ≤ E (`g_carry.py`; E = 4 run in N15, `logs/g_carry_E4.{out,json}`): rate 0.272551 = ρ(𝒦) for E = 1, 2, 3, 4.
   - The Perron share of the (0,0) carry state is 0.235, 0.150, 0.1154, 0.0931; 1/share = 4.26, 6.67, 8.67, 10.74.
   - So **the carry-range prefactor is not seen to converge by E = 4**; it grows about linearly (+2 per unit E). The alphabet is finite (|e| ≤ 15, item 1), so the prefactor is finite. Linear extrapolation gives 1/share ≈ 33 at E = 15, about 8× the E = 1 value [H].
   - The share is a proxy, not the scalar collision prefactor. The measured exact shell sums (C_emp ≤ 4.4e-4, flat in j) remain the relevant [N] evidence, and a factor ~8 would still sit inside the ≈190× margin.
   - The brief's route "show the prefactor converges as the carry range grows" is therefore **not supported by the data at E ≤ 4**. A certificate must handle the full |e| ≤ 15 alphabet, or bound large carries by a Gram (phase) estimate.
4. **What is missing for [P]/[CA]** (not done in N15):
   - (a) A certificate for the sesquilinear carry transfer with all |e| ≤ 15. That is 961 carry states × 495² Hermitian blocks, about 3.7 GB per iterate, out of reach on one shared core. Alternatively, an analytic tail for E > 3.
     - The letterwise route provably fails: an isolated carry c costs κ_c κ_{6c} κ_c relative to ρ̄³. For c = 1 that is ≈ 0.9·40·0.9 ≈ 33 vs ρ̄³ = 0.022.
     - The N14 plan of "bound the tail by the 0.2803 rate × carry decay" therefore needs a phase-sensitive (Gram) estimate of the carry blocks, not norms. This is the core open step.
   - (b) Box/aliasing constants of the Poisson reduction [P-sketch idea]: lattice sum = (#points) × bi-infinite Bohr mean + junction-crossing carries. **Not computed.**
   - (c) Markov-partition CP alternative: not built.
   - Status of the lemma: **OPEN at [P]; [N]-closed with ≈190× margin** (C_emp 4.4e-4 vs 0.082).

## 4. (2) Kotecký–Preiss weight, explicit (`code/kp.py` → `logs/kp_a_cert3.json`)
- **Polymers.** γ is a bad cluster word under the a_post rule (internal zero-runs < g₀). Its exclusion length is ℓ(γ) = span(γ) + g₀, and its activity is |w(γ)| ≤ absw_up (a_cert3) with factor 2 per site. The model types are the background and are not polymers ([P-sketch] interplay, as in N14 §1.4).
- **KP condition** [P, 1D form of Kotecký–Preiss 1986], with weight a(γ) = a·ℓ(γ). A polymer γ′ incompatible with γ has its anchor in a set of ≤ ℓ(γ) + ℓ(γ′) sites, so
  Σ_{γ′≁γ}|w(γ′)|e^{aℓ(γ′)} ≤ ℓ(γ)S₀(a) + S₁(a),  where S₀ = 2Σ_anch|w|e^{aℓ} and S₁ = 2Σ_anch|w|ℓe^{aℓ}.
  KP holds if S₀ + S₁/(1+g₀) ≤ a. Then the per-site bad log-correction is ≤ S₀(a) (the cluster sum anchored at a site is ≤ Σ|w(γ)|e^{a(γ)}).
- **Tail j > 12.** The Lemma D tail 1.56e-8 is included, weighted by ℓ ≤ 2·13 + g₀ + 2/(1−ρ̄) [P-sketch: the ℓ-weighting of the tail uses the span ≤ 2j ratio seen up to j = 12].
- **Numbers:**
  | g₀ | a | S₀(a) = A_bad^KP | S₁(a) | S₀+S₁/(1+g₀) ≤ a | plain 2Σ|w| + tail |
  |---|---|---|---|---|---|
  | 2 | 2.3291e-06 | 6.973770e-07 | 4.5625e-06 | ✓ | 6.817666e-07 |
  | 3 | 3.9523e-06 | 1.318684e-06 | 9.7816e-06 | ✓ | 1.303046e-06 |
  | 4 | 5.9325e-06 | 2.062875e-06 | 1.7936e-05 | ✓ | 2.047169e-06 |
  | 5 | 8.0056e-06 | 2.836413e-06 | 2.8728e-05 | ✓ | 2.820584e-06 |
  | 6 | 1.0315e-05 | 3.696009e-06 | 4.2895e-05 | ✓ | 3.679967e-06 |

  (S₀ counts the 1.56e-8 tail twice, which is conservative.) Against the budget: A_bad^KP(g₀=4) + δ_int = 2.0629e-06 + 5.14476e-7 = 2.5774e-06 ≪ Re Λ_lo′ = 6.234e-4.
  The KP weight therefore costs < 1% on A_bad. The N14 statement "a ≤ 0.05, spans ≤ 20, costs < e" is superseded: a ~ 1e-5 suffices.

## 5. (2) Composite core→true conversion — status [P-sketch]
- The N8 conversion lemma (n8_cert.excursion) was applied per window, with GA ≤ √cond_H·∏N̄_H(d_t) (`code/conv.py` → `logs/conv_replay.jsonl`). It is **vacuous**: GA = 40–340, giving error radii 0.033 (odd) up to 38 (pairs). The H-norm product discards the averaging that makes ρ̄ small.
- **What is needed:** a vector-chain version. Propagate the perturbation ΔX = X_true − X_core along the actual vector v_k (‖ΔX v‖ ≤ (Pert/|s|)‖v‖), as in c3_mid's error recursion, rather than through operator-norm products.
  - This is the same a-posteriori recursion with loc_k += ‖T‖·(Pert/|s|)·‖v̂_{k−1}‖. Pert = 1.9e-9 (N8) is ≫ the 1e-13 rounding constant, so the radii are expected to grow ~1e4× [H, not computed]; whether this fits the δ_int budget, and how the projection terms behave, is unchecked.
  - `code/conv_est.py` was started and killed unfinished for the referee fix; no output.
- Label: **[P-sketch]**.

## 6. Wrap-around composite-h points (delegated to the subgroup line)
- The per-site wrap activity of a bad cluster of span ℓ (λ-steps) is ≤ C_wrap·d^{c}·q^{ℓ}, q = (λρ̄²)^{3/2}, *given* the subgroup second-moment lemma E_{H_d}|r|² ≤ C·d^{c}·E_G|r|² (N13b R2 object, at second-moment level).
- Summing ℓ ≥ ℓ₀ gives C_wrap·d^c·q^{ℓ₀}/(1−q). This must tend to 0 (with margin e^{−ηp} for summation over p), i.e.
  **c < (1−η)·ln(1/q)·ℓ₀ / ln d**.
- With ρ̄_true = 0.28028 [CA-fp]: q = 0.30982, ln(1/q) = 1.1718, so c < 1.1718·ℓ₀/ln d = 0.6647·ℓ₀/log_λ d. With ρ̄ = 0.30: q = 0.3799, c < 0.9678·ℓ₀/ln d = 0.5490·ℓ₀/log_λ d.
- **Correction:** the brief's "0.97·ℓ₀/log_λ d" is the ρ̄ = 0.30 constant with the wrong log base. It must be ln d, or equivalently 0.549·ℓ₀/log_λ d.
- ℓ₀ must be measured in λ-steps (= 2 ε-steps). The numerical threshold follows by inserting the subgroup line's ℓ₀(p) and d ≤ h_p.
- **Not duplicated here.**

## 7. Open after N15
1. **Collision-constant lemma.** Needs a phase-keeping certificate for the full |e| ≤ 15 carry system, or an analytic Gram tail for E > 3, plus the box/aliasing constants.
2. **Core→true conversion** in vector-chain form.
3. **KP–background interplay and the tail ℓ-weighting** (both [P-sketch]).
4. **Wrap-around exponent** via N13b.

## 8. Artifacts
- **code/:** rig.py, nh_table_rig.py, c3_mid.py, b_cp3.py, a_cert3.py, a_certpost3.py, c3_vs_arb.py, kp.py, run_v2.sh, run_v3.sh, run_v4.sh, f_partial.py, nh_table.py, g_carry.py, g_torus.py, conv.py, conv_est.py (unfinished).
- **logs/:** see SHA256_N15.txt (written last). The manifest also covers N13/logs/c_replay.{jsonl,out}, the stopped partial replay.
