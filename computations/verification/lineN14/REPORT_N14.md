# REPORT_N14 — collective tail (A): second-moment pre-flight, certified core rate, collision structure; (C′) N13-F3 fix; REPORT_N13_v2
Labels: [P] proof, [P-sketch], [CA] arb, [CA-fp] IEEE binary64 with explicit a-priori rounding bounds (Weyl/Higham; not interval arithmetic), [N] numerics, [H] heuristic/assumption.
All numbers below refer to the sector-4 core operator (cert_core); the core→true conversion for composite windows is still open (as in N13 §3).

## 0. Summary
- **Pre-flight (float) confirms the budget fit by a wide margin [N].** Exact enumeration of **all 5,109 classes** α ∈ O mod ±ε^ℤ with |N(α)| < 2¹³ (seed e = 2α covers both backgrounds exactly once). Polymers are ε-digit clusters (internal zero-run < g₀). Per-site bad activity A_bad (all non-model clusters, incl. α = 4 and the 96 short-cluster classes):
  | g₀ | 2 | 3 | 4 | 5 | 6 |
  |---|---|---|---|---|---|
  | A_bad (j ≤ 12) | 6.66e-7 | 1.29e-6 | 2.03e-6 | 2.80e-6 | 3.66e-6 |
  | share of Re Λ_lo′ = 6.234e-4 | 0.11% | 0.21% | 0.33% | 0.45% | 0.59% |
  The shell sums follow the certified-rate law with a stable constant (C_emp ≈ 3e-5–4e-4, §2), extrapolated tail j > 12 ≲ 4e-9 [H: extrapolation]. With δ_int ≤ 5.14e-7 (§4): A_bad + δ_int ≤ 4.2e-6 ≪ Re Λ_lo′ (≈150× margin).
- **Certified finite part [CA-fp, core functional]:** the same sums recomputed through the rigorous mid-point chain (§4) — see §1.4 (final numbers in §6).
- **Rate certified [CA-fp]:** the i.i.d. second-moment operator 𝒦(Y) = Σ_n N_nYN_n* (N_n = c_nM_n/s) satisfies 𝒦(Y_c) ⪯ 0.30·Y_c for an explicit Y_c ≻ 0 (Neumann certificate; margin 3.7e-6 vs total error 7.3e-13); core→true: ≤ 0.3003. Hence λρ̄² = 0.525 < 1 and (λρ̄²)^{3/2} = 0.380 per λ-step for Σ_shell|w|. Tighter: ρ̄ ≤ 0.28 [CA-fp] (§6).
- **Collisions (lattice correlations):** the letterwise CP bound (Gram dilation + AM–GM per letter) is useless (κ_v up to 38). Keeping phases, the exact-collision carry system (carries |e| ≤ 1) has growth rate **0.272551 = ρ(𝒦)** to 6 digits [N] — correlations change only the prefactor ((0,0)-carry share 0.235), not the rate.
- **What is still missing for a [P] tail (precise):** the lattice→collision reduction with a small constant. With the certified rate the tail closes from J₀ = 12 iff the constant C in Σ_shell|r_Ar_B|² ≤ C·2^j·2^{−βj} is ≤ 0.036 (ρ̄ = 0.30) / 0.11 (ρ̄ = ρ(𝒦)); measured C_emp ≤ 4.4e-4. The generic CP conversion constants alone are (ψ*Y_cψ)(Φ*Y_c⁻¹Φ) = 3.4 per window, offset by ρ^{2·log_λ 32} ≈ 5e-3 from the core-length offset — so it is plausible but not proved. See §2.4.
- **(C′) N13-F3 fixed:** new rigorous mid-point replay (`code/c2_mid.py`) with H-norm a-posteriori error propagation: radii 2e-9–8e-9 flat in G (arb replay: 59% at G = 15). **δ_int (coded, 1350 pairs) ≤ 5.14415e-7 [CA-fp]**; 200 short types → 27 model relabellings + 4 to α = 4 + 169 rows / 96 genuine classes, Σ|w|_up = 9.970e-7 (per site ×2 = 1.99e-6).
- **Lemma D with the referee's constant (N13-F1):** absolute tail beyond G₀ = 16 is ≤ **1.56e-8** (was 5.76e-9).

## 1. (A) Setting, polymers, normalisation
1. **Classes and seeds.** Every α ∈ O∖{0} mod ±ε^ℤ, fundamental domain 1 ≤ σ₁(α)/|σ₂(α)| < λ, σ₁ > 0. Seed e = 2α: bg ¼ ⇔ N(α) odd, bg 0 ⇔ α ∈ √2·O, disjoint and exhaustive. The model types are exactly α ∈ {1, √2, 2, 2√2} (fam, near0, z0_e4, z0_e4s2 — the four terms of Re Λ_lo); α = 4 ("four", c₁₆) is bad, as in lambda_cert.
2. **ε-digit language [P-sketch].** Interleaving the A and B windows (B = A at half λ-steps, sign-flipped) gives the ε-chain twists τ_k; E_k := −(τ_k − 2τ_{k−1} − τ_{k−2}) ∈ ℤ, |E_k| ≤ 2, and τ = G_ε * E. Words of the model types: odd = [1], sq2 = [1,−1], two = [1,0,−1], 2sq2 = [1,0,1], four = [1,−1,0,1,1] (`code/digits.py`). Class ↔ admissible word is a bijection.
3. **Polymers.** Maximal subwords with internal zero-runs < g₀. Classes with an internal run ≥ g₀ are gas configurations of smaller polymers (excluded from A_bad; their interaction is δ_int-type). g₀ is a free design parameter: increasing it moves mass from δ_int into A_bad; the table in §0 shows that every g₀ ≤ 6 fits.
4. **Per-site normalisation.** Re Λ = 2 Σ_model Re w (one factor 2 per class mod ±ε^ℤ per site). Hence **A_bad := 2 Σ_{bad clusters} |w| · e^{a|γ|}** and the target is A_bad < Re Λ_lo′ − δ_int. The KP weight e^{a|γ|} and the log→modulus step remain [P-sketch] (referee 2d). With a ≤ 0.05 per ε-site and spans ≤ 20 it costs < e¹, still ≫ margin.
5. **Data:** `logs/a_enum.jsonl` (5,109 classes, float), `logs/a_post.json` (table), `logs/a_cert.jsonl` + `logs/a_certpost.json` (rigorous chain).

## 2. (A) Second-moment certificate
1. **ℓ³ ≤ ℓ² [P]** (Lean `l3_le_l2`, referee): Σ_shell|w| ≤ (Σ_shell|r_A r_B|²)^{3/2}. The data (CS form) is 2× the direct sum at small j, which is harmless.
2. **Rate [CA-fp]** (`code/b_cp2.py`, `logs/b_cp2_0.3.json`).
   - 𝒦 is CP with ρ(𝒦) = 0.272551 [N], but its Perron matrix is singular. Y* + εI therefore only certifies 0.62 (`b_cp.py`, kept as a record).
   - Neumann certificate: Y_c = Σ_{k≤120} ρ̄^{−k}𝒦^k(Y₀), Y₀ = Y* + 1e-4‖Y*‖I, gives 𝒦(Y_c) ⪯ ρ̄Y_c iff λ_max(Y₀^{−1/2}𝒦^{121}Y₀Y₀^{−1/2}) ≤ ρ̄^{121}: 4.9e-69 ≤ 5.4e-64 ✓.
   - Verified directly: λ_min(ρ̄Y_c − fl𝒦(Y_c)) = 3.74e-6 > E_round 7.3e-13 + E_input 9e-15 + eig_err 4e-15. cond(Y_c) = 1.1e5. Core→true (‖ΔX‖ ≤ Pert/|s|): ρ̄_true ≤ 0.3003.
   - Consequence [P given the certificate]: for every start Y ⪰ 0, 𝒦^m(Y) ⪯ ρ̄^m·(sup Y/Y_c)·Y_c. For the joint pair (A at even ε-steps, B at odd steps) Y_c⊗Y_c certifies ρ̄² per λ-step.
3. **Collisions.**
   - The class sum is a lattice sum, not an i.i.d. average. Fourier-expanding each step, exact collisions are pairs of letter sequences with Σ v_tλ^t = 0, i.e. v = e − 6e₋₁ + e₋₂ with integer carries e (N2 structure).
   - (i) Letterwise CP bound, Gram dilation with balanced weights: κ_v = 0.90, 1.8, 4.4, …, 38 (v = 1…14). The bound diverges. The off-diagonal pairs are not small letterwise because ‖N_{±3}‖ = 2.43 and ‖N_{±6}‖ = 0.81 [N, `b_cp2`].
   - (ii) Phases kept, carries |e| ≤ 1: rate 0.272551 = ρ(𝒦) [N] (`code/g_carry.py`, `logs/g_carry_E1.out`). E = 2 (§6): same rate; prefactor grows with the carry range.
   - So the lattice structure does not change the exponential rate [N], but a certificate must keep phases. It is sesquilinear, not CP. A positive formulation exists via a Markov partition of the toral automorphism (twist cells × Y ⪰ 0), which is the R1/Bowen route [P-sketch, not built].
4. **Constant needed vs measured** (`code/a_need.py`, `logs/a_need.json`). Model: S2(j) := Σ_{shell j, bad}|r_Ar_B|² ≤ C·2^j·2^{−βj}, β = −2 ln ρ̄/ln λ. Tail T(J₀) = 2Σ_{j>J₀}S2(j)^{3/2} ≤ (Re Λ_lo′ − 1e-6)/2:
   | | J₀=8 | 10 | 12 | 14 | 16 | 20 | 25 |
   |---|---|---|---|---|---|---|---|
   | C_needed, ρ̄ = ρ(𝒦) | 0.030 | 0.058 | 0.111 | 0.215 | 0.415 | 1.55 | 8.0 |
   | C_needed, ρ̄ = 0.30 | 0.013 | 0.022 | 0.036 | 0.060 | 0.100 | 0.28 | 0.98 |
   - Measured C_emp(j), j = 2…12, ρ̄ = ρ(𝒦): 3e-5 … 4.4e-4, flat in j. So the rate law holds with a ≥ 250× constant margin at J₀ = 12.
   - **The open lemma (minimal extra input):** a lattice→collision reduction for the shell sums, with constant ≤ C_needed(J₀). The ingredients are a Beurling–Selberg box majorant, frozen padding vectors on sub-boxes (padding where |d| < 1/256 is controlled by the [CA] quadratic step bound), and the phase-kept carry system. The finite part j ≤ J₀ is then certified by direct evaluation (§1.5, done to J₀ = 12).
   - Status of the constant: unproved. The generic CP conversion (ψ*Y_cψ)(Φ*Y_c⁻¹Φ) = 1.53·2.22 = 3.4 per window is offset by the core-length offset ρ^{2 log_λ 32} ≈ 6e-3. Box/aliasing constants are not yet computed. **(T) therefore remains OPEN at [P] level, and is closed at [N] level with ≈150× margin.**

## 3. Wrap-around deep points — what is needed, and from whom
- **Definition.** A point of the level-h_p circle whose bad cluster has span ℓ comparable to the circle (ℓ ≥ ℓ₀(p), e.g. ℓ₀ = p/2 ε-steps). The window model (and hence A_bad per site) does not apply to it, because the window wraps.
- **What (A) itself gives.** The same CP certificate applies verbatim on the circle: the operator is unchanged and ρ̄ = 0.30 per step [CA-fp]. Only the lattice changes, from O to the finite group O/γ̄. So the per-site wrap activity is ≤ C_wrap·(λρ̄²)^{3ℓ/2} once a second-moment equidistribution statement is available on the circle's point set.
- **The input that is NOT gap-(a) work.**
  - For h_p prime, the circle point set is the full group, and Parseval is exact. No new input is needed beyond the constant [P-sketch].
  - For composite h_p, the isotropic points form a coset of a subgroup H_d. The needed input is the subgroup second-moment / equidistribution lemma E_{H_d}|r|² ≲ e^{o(p)}·E_G|r|². This is the same object as N13b's route R2 subgroup lemma (E_{H_d}|r| ≤ e^{o(p)}d^c(…)^{3p}, c < 0.387).
  - **I do not duplicate it.** Gap (a)'s wrap-around points become a corollary of whatever N13b proves for H_d, at second-moment level. Exponent needed for (a): any c with d^{c}·(0.380)^{ℓ₀} → 0, i.e. c < 0.97·ℓ₀/log_λ d — much weaker than N13b's 0.387.
- G*-type stay bounds are no longer used: N13b and the referee closed the D1 + gas route negatively.

## 4. (C′) N13-F3: replay radii — fixed by a-posteriori H-norm propagation
- **Method** (`code/c2_mid.py`). The chain v̂ ← fl(X(d̂)v̂) is run in binary64 on the same cert_core data, stored s̃, Φ̃, ψ̃, exact seeds (mpmath), KK = 18, and the identical job list/order.
  - Error recursion: ‖e_k‖_H ≤ N_H(d_k)‖e_{k−1}‖_H + ‖T‖(4e-14‖X_abs|v̂|‖ + Lip₂|Δd|‖v̂‖).
  - N_H bounds: [CA] quadratic bound 1 + 1.01e-12 + 4260d² for |d| ≤ 1/256. For larger |d|, a cell bound (width 2e-4) from the float SVD of T·X·T⁻¹ plus formation error, divided by (1 − ‖TT̃⁻¹ − I‖), plus Lip_H·h/2 [CA-fp]; 1,373 cells were used.
  - |ψ̃e| ≤ ‖ψ̃T⁻¹‖·‖e‖_H.
  - Radii do not compound: 2.2e-9 (A) and 8.1e-9 (B) for odd+odd at every G = 5…15, against 4.5e-9 → 59% in the arb replay. All 1560 jobs run in 7 minutes.
- **Results** (`code/f_post2.py` → `logs/f_post2.json`, same formulas as N13 f_post):
  - **coded pairs (1350): Σ|W_ij − W_iW_j| ≤ 5.14415e-7 [CA-fp]** (midpoint 5.14405e-7). By G: 2.5e-7 (G = 3), 9.1e-8, 3.4e-8, …, 3.0e-12 (G = 15); ratio ≈ 0.38/step.
  - singles agree with the arb replay boxes (e.g. odd |w| ≤ 3.95451e-4).
  - short types (`code/f_short.py`): 27 model relabellings, 4 relabellings to α = 4, 169 genuine rows = 96 distinct classes (the referee's 31/169/95 when α = 4 is counted as a relabelling). **Σ_distinct |w|_up = 9.970e-7**, i.e. 1.99e-6 per site; these classes are inside A_bad (§0).
- **Arb replay (N13 c_replay.py).** It is still running (sequential, nice), at 457/1560 at 01:23 +05. It is kept as an independent [CA] cross-check of c2_mid for G ≤ 13.
  - Per N13-F3, its certified deviations are near-vacuous for G ≥ 14. δ_int is therefore quoted from c2_mid.
  - When it finishes: run `N13/code/f_post.py`, hash `N13/logs/c_replay.{jsonl,out}`, and compare against f_post2. **Not done in this run**: about 8 h of CPU remain at ~7 s/job.

## 5. REPORT_N13_v2 (referee /workspace/audit/lineN13/REPORT.md)
- **F1 (Lemma D constant) — accepted.** Every e^{σ} − 1 is replaced by e^{Γσ} − 1 with the matching Γ (`code/d_decay2.py`). Worst relative class-dev sum 0.249 → 0.691. **Absolute tail beyond G₀ = 16: 5.76e-9 → 1.56e-8** (referee estimate ≲ 2e-8). Immaterial.
- **F2 (quadratic constant) — accepted.** The bound is quoted as N_H(t) ≤ 1 + 1.01e-12 + 4.26e3·t² on |t| ≤ 1/256, citing the referee's arb partition (30,364 cells, `ref_quad_partition.py`). The 400-point grid maximum 4253.4 is withdrawn as a bound. This constant is used in d_decay2 and c2_mid.
- **F3 (replay radii) — accepted and fixed (§4).** The §7 "≈1.5% at G = 13" statement of N13 is withdrawn. Certified δ_int ≤ 5.144e-7 [CA-fp] for the core functional.
- **F4 (minor) — done.**
  - `N13/SHA256_N13.txt` regenerated; all 27 entries OK. N13 files are frozen from now on.
  - The wrap-gap sentence is replaced by: "all gaps are circular; all statements use circular gaps".
- **F5 (minor) — accepted.** "ℓ³ ≤ ℓ² removes the sup barrier" holds conditionally on the second-moment (lattice→collision) certificate of §2.4.
- **Composite core→true conversion** is still open, for both δ_int and A_bad finite parts.

## 6. Late results (filled at end of run)
- **Certified finite part of A_bad [CA-fp, core functional]** (`code/a_cert.py` → `logs/a_cert.jsonl`, `code/a_certpost.py` → `logs/a_certpost.json`). All 5,109 classes with |N(α)| < 2¹³ were run through the c2_mid chain. 2·Σ_bad|w|_up:
  | g₀ | 2 | 3 | 4 | 5 | 6 |
  |---|---|---|---|---|---|
  | certified | 6.6617e-7 | 1.28744e-6 | 2.03157e-6 | 2.80498e-6 | 3.66436e-6 |

  These agree with the float values to < 0.2%.
- **Tighter rate [CA-fp]** (`logs/b_cp2_0.28.json`). ρ̄ = 0.28 (m = 400). Margin 3.49e-6 against errors 2.5e-12; cond(Y_c) = 3.8e5. Core→true: ρ̄_true ≤ 0.28028. Conversion product (Φ*Y_c⁻¹Φ)(ψ*Y_cψ) = 0.653·5.277 = 3.45.
  - λρ̄² = 0.457, and (λρ̄²)^{3/2} = 0.309 per λ-step.
  - C_needed at J₀ = 12 becomes 0.082.
- **Collision carries |e| ≤ 2** (`logs/g_carry_E2.out`). Rate 0.272551 = ρ(𝒦) again [N].
  - The (0,0) share falls from 0.235 (E = 1) to 0.150 (E = 2): the collision **prefactor** grows with the carry range (total/diagonal mass 4.3 → 6.7) while the rate stays the same.
  - Whether the prefactor converges as E → ∞ is not established. It is part of the open constant in §2.4. Carries are bounded by |e| ≤ 15 for |v| ≤ 60, so E = 15 is exact, but that run is out of reach at this size (961 states).

**Bottom line for (A).**
- Numerically closed, with ≈150× margin for every g₀ ≤ 6.
- Certified pieces:
  - the finite part j ≤ 12 [CA-fp];
  - the rate ρ̄ ≤ 0.28 [CA-fp];
  - δ_int ≤ 5.144e-7 [CA-fp];
  - Lemma D tail ≤ 1.56e-8 [P+N].
- Still open:
  - one lemma, the lattice→collision reduction with constant ≤ 0.08 at J₀ = 12. This needs a phase-keeping (sesquilinear) carry certificate or a Markov-partition CP certificate; the letterwise CP bound provably cannot work (§2.3(i));
  - the composite core→true conversion;
  - the KP weight;
  - wrap-around points via N13b's subgroup lemma.
