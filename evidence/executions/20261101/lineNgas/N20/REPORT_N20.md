# REPORT_N20 — H1 (collision lemma) final push, and H3
Grok Bot · 2026-11-01, 09:00–10:04 Asia/Yekaterinburg (UTC+5) · one shared machine (load 9–40); all jobs nice 5–10.

**Labels** (as in THEOREM_DRAFT_v4): [P] proof written out (author; *not refereed* unless stated) · [P-sketch] · [CA] arb ball arithmetic · [CA-fp] binary64 with derived a-priori rounding bounds (N15 model) · [N] numerics without error control · [H] hypothesis.

## 0. Bottom line (honest)
- **H1 is NOT proved. It stays [H].** Consequently **H3 is NOT closed.** It is now [P + CA] *conditional on H1 only*, with a large, explicit tolerance (Prop. K).
- **The planned route does not work as stated. This is the main new finding.** The route was: a certified transfer operator on the 633 λ-carry states, plus "torus ≈ i.i.d., so the whole 186× margin goes to aliasing". It fails for two reasons:
  1. **Wrong collision system (Lemma J, [P]).** H1's shell sum is over |r_A r_B|², the *joint* (A, B) pair. The two windows are the even and odd sites of **one ε-chain**: d^B_t = −σ₁(μ)ε^{2t−1}, d^A_t = σ₁(μ)λ^t. So the exact-collision relation is ε-adic: Σ_k u_k ε^k = 0, u_k = e_{k−2} − 2e_{k−1} − e_k.
     - Its carry alphabet is |e| ≤ 51 (sharp), with **6145** reachable pair states [P, exact integer computation; Lean for the Green bound].
     - The 633-state λ-system is only the single-window subsystem.
     - N15/N16's "torus = i.i.d. to 1e-11" was measured for a **single** window. It does not transfer: the joint torus mean is **1.86 ± 0.07, 3.6 ± 0.3, 10.6 ± 2.1 ×** the i.i.d. product at n = 2, 3, 4 λ-steps [N, MC]. Controls: n = 1 gives 0.997 ± 0.015; i.i.d. twists give 0.95 ± 0.03.
  2. **Unrestricted torus/carry bounds cannot give the H1 rate (Prop. F, [P] with N13 [CA] constants).** Orbits that shadow the fixed point d = 0 give, for every n ≤ 10¹⁰,
     M_n^joint ≥ 5.1·10⁻⁷·λ^{−n}, while M_n^iid ≤ 3.45²·0.28^{2n}.
     - Since λ·0.28² = 0.457 < 1, the ratio is ≥ 4.3·10⁻⁸·2.188ⁿ → ∞. It exceeds 1 for n ≥ 22.
     - The lattice data agree [N]: the all-class joint shell sum Σ_all|r_A r_B|² is **flat** in j (3–9e-5, no trend, for j = 5…12, the shadowing/gas rate 2·λ^{−log_λ 2} = 1). Only the *bad* part decays.
     - So **any proof of H1 must build the polymer restriction (ε-zero-runs < g₀) into the certificate.** No Fourier-carry / Bohr-mean bound over all twist sequences can work, whatever its state space.
- **What *is* proved here:**
  - **Thm A** [CA-fp]: H1's shell law holds for **every shell j ≤ 14**, with C_cert(j) ≤ 4.36e-4 (max at j = 5). The constant decreases: C_cert(12) = 2.6e-5, C_cert(13) = 1.7e-5, C_cert(14) = 1.3e-5 (ρ = 0.2726 convention).
  - **Lemma R** [P, Lean]: renewal lemma. This is the exact form in which a finite-state excursion certificate gives a length-uniform geometric bound.
  - **Lemma G** [P, Lean, kernel `decide`]: 633 states, |e| ≤ 14 sharp, and ρ(adjacency) ≥ 20. Hence **O1** [P]: every scalar (norm-weighted) automaton on these states with uniform off-diagonal weight ≥ 1/20·(target rate) fails; [N] the threshold is 0.012.
  - **Prop. K** [P + CA, Lean arithmetic]: H1-shell(C, J₀) ⇒ H3 with explicit a, for C up to 0.082 at J₀ = 12. With the measured-size C = 8.8e-4: a = 8.25e-6, A_bad^KP = 2.38e-6.

## 1. Precise statements
Notation (N14 §1–2): α ∈ O∖0 mod ±ε^ℤ, shell j: 2^j ≤ |N(α)| < 2^{j+1}. Seed μ = (√2/4)α. r_A = ψ∏_t X(d^A_t)Φ and r_B likewise (cert_core sector-4 operator, KK = 18). |w| = |r_A r_B|³. "Bad at g₀" means non-model and every internal ε-zero-run < g₀. β(ρ) = 2 ln(1/ρ)/ln λ, q(ρ) = 2^{(3/2)(1−β)}.
- **H1-shell(C, J₀, ρ):** S2(j) := Σ_{shell j, bad} |r_A r_B|² ≤ C·2^{j(1−β(ρ))} for all j > J₀. (v4: C ≤ 0.082, J₀ = 12, ρ = 0.28.)
- **H1-fin(J):** the same inequality for j ≤ J, with the finite sums certified.
- **H1-KP(a, τ₀, τ₁)** (the form H3 actually uses): T₀ := 2Σ_{j>J₀}Σ_{bad}|w|e^{aℓ} ≤ τ₀ and T₁ := 2Σ_{j>J₀}Σ_{bad}|w|ℓe^{aℓ} ≤ τ₁, where ℓ = span + g₀.
- H1-shell ⇒ H1-KP with τ explicit: Prop. K (§3.4).

## 2. Structure of H1's object (new)
**Lemma P0 (periodicity) [P].** X(d) = Σ_{n=−30}^{30} c_n e(nd)M_n/s has period 1, so the `red` in N14 digits.core is immaterial. Exactly: d^A_t ≡ σ₁(μ)λ^t (mod 1) for all t, and also ≡ −σ₂(μ)λ^{−t}, because Tr(μλ^t) = Tr(√2αλ^t)/4 ∈ ℤ.

**Lemma J (joint relation) [P].** The seeds satisfy μ_B = −ε^{−1}μ_A exactly (N14 digits.seeds: μ_A(√2−1) = −μ_B, by expansion). Hence d^B_t ≡ −σ₁(μ)ε^{2t−1}.
- The pair (r_A, r_B) is a function of the single sequence σ₁(μ)ε^k mod 1, with A on even k and B on odd k.
- Expanding |r_A r_B|² in letters (n, m) per site, the frequency of a letter-difference sequence u (u_{2t} = v^A_t, u_{2t−1} = −v^B_t, |u_k| ≤ 60) is (Σ_{k≤k₀}u_kε^k, −Σ_{k>k₀}u_kε′^k).
- Over the lattice L = (√2/4)O, whose trace-dual is L^∨ = O (different 2√2), this frequency lies on ι(L^∨) iff Σ_k u_kε′^k = 0 ⇔ Σ_k u_kε^k = 0.
- x² − 2x − 1 is monic irreducible, so u_k = e_{k−2} − 2e_{k−1} − e_k with integer carries.
- The bounded solution is e = g∗u, with ‖g‖₁ = (√2+1)/(2√2) = (2+√2)/4 = 0.85355 (Lean `eps_green_l1`). Hence |e| < 60·0.85355 = 51.21, i.e. **|e| ≤ 51** (Lean `eps_carry_lt52`, `eps_carry_int`).
- Reachable pair states (closed paths through (0,0), transitions |a − 2b − c| ≤ 60): **6145**; 8377 forward = 8377 backward; e_max = 51 attained; 307 935 edges (`code/carry_graph_eps.py`, exact integers) [P-computation].
- Numerical confirmation of μ_B/μ_A and of the two congruences: mpmath at 40 digits, three classes, |error| ≤ 2.4e-17 (float `core`).
- *Consequence:* N15's 633-state λ-system covers only collisions with v^B ≡ 0 or v^A ≡ 0. It is the right object for a single window, not for S2.

**[N] joint vs single (code/joint_torus_mc.py; ε-chain on T², (τ₀, τ₁) uniform; i.i.d. reference S0(n) from N16 g_scalar E = 0):**

| n (λ-steps) | joint/iid | single A/iid | single B/iid | samples |
|---|---|---|---|---|
| 1 | 0.997 ± 0.015 | 0.999 ± 0.008 | 1.000 ± 0.008 | 2e4 |
| 2 | **1.858 ± 0.065** | 1.002 ± 0.010 | 1.003 ± 0.010 | 4e4 |
| 2, all twists i.i.d. (control) | 0.948 ± 0.031 | 0.992 ± 0.014 | 0.990 ± 0.014 | 2e4 |
| 3 | **3.64 ± 0.32** | 0.984 ± 0.016 | 1.020 ± 0.017 | 4e4 |
| 4 | **10.60 ± 2.11** | 0.998 ± 0.026 | 0.994 ± 0.026 | 4e4 |

(The growth 1 → 1.86 → 3.6 → 10.6 is consistent with Prop. F's asymptotic ≥ c·2.19ⁿ; MC is heavy-tailed, so the n = 4 value is a rough estimate.)

The single windows reproduce N15/N16 (≈ 1). The joint pair does not.

**Prop. F (fixed-point shadowing; joint torus mean ≫ i.i.d.) [P, inputs N13 [CA] constants (refereed lineN13) and N15 ρ̄ = 0.28 [CA-fp]; the constant 3.45 is N14 float [N], but any finite value suffices for the conclusion].**

*Setup.* Let M_n^joint := ∫_{[0,1)²}|r_A|²|r_B|² dτ₀dτ₁, with τ_k = 2τ_{k−1} + τ_{k−2} (mod 1), r_A = ψX(τ_{2n})⋯X(τ₂)Φ and r_B = ψX(−τ_{2n−1})⋯X(−τ₁)Φ. Let M_n^iid := (ψ𝒦ⁿ(ΦΦ*)ψ*)².

*Claim.* For 1 ≤ n ≤ 10¹⁰: M_n^joint ≥ 5.13·10⁻⁷·λ^{−n} and M_n^iid ≤ (3.45·0.28ⁿ)².

*Proof.*
1. Put δ = 1.69e-3. Let U_n be the image of {|a| ≤ (δ/2)ε^{−2n}, |b| ≤ δ/2} under (a, b) ↦ (τ₀, τ₁) = (a + b, aε + bε′), ε′ = −1/ε.
2. On U_n, τ_k = aε^k + bε′^k exactly for 0 ≤ k ≤ 2n: the recurrence is linear and |τ_k| ≤ δ < 1/2, so there is no reduction. Also Σ_k|τ_k| < δ·ε/(ε−1) = 1.7071δ.
3. Area(U_n) = |ε′ − ε|·δ²ε^{−2n} = 2√2·δ²·λ^{−n}.
4. Telescoping with X(0)Φ = Φ + ρ_Φ, ‖ρ_Φ‖_H ≤ 6.85e-16 [CA]:
   ‖v_A − Φ‖_H ≤ ∏_s N_H(τ_s)·(Lip_H Σ_t|τ_{2t}| + n·6.85e-16).
5. With N_H(t) ≤ 1 + 1.01e-12 + 4260t² for |t| ≤ 1/256 [CA+P] and Lip_H ≤ 167.214 [CA]:
   - exponent ≤ n·1.01e-12 + 4260·1.7071δ² ≤ 0.0309;
   - so ‖v_A − Φ‖_H ≤ 1.0314·(0.48241 + 7e-6) ≤ 0.4976.
6. ‖ψ‖_{H*} = ‖Φ‖_H = 1 and |ψΦ − 1| ≤ 1.8e-16 (N13 b2_quad), so |r_A| ≥ 0.502. The same holds for r_B, since the bounds are even in t.
7. Hence M_n^joint ≥ 2√2·δ²·λ^{−n}·0.502⁴ ≥ 5.13e-7·λ^{−n}.
8. The i.i.d. bound is N16 §1.3: S_n^{(0)} ≤ (ψ*Y_cψ)(Φ*Y_c⁻¹Φ)ρ̄ⁿ.
9. The ratio is therefore ≥ 4.31e-8·(λρ̄²)^{−n} = 4.31e-8·2.1884ⁿ, which is > 1 for n ≥ 22 and tends to ∞. ∎

*Remarks.*
- The same argument gives M_n^single ≥ c·λ^{−n}. Since λ^{−1} = 0.172 < ρ(𝒦) = 0.273 this is harmless, which is why single windows look i.i.d.
- For the joint pair the shadowing rate λ^{−1} beats ρ̄² = 0.078. This is exactly the gas/model mechanism (X(0)Φ = Φ) that the whole project relies on for Re Λ > 0.
- **Corollary [P]:** no bound of the form "lattice shell sum ≤ A·#shell·(unrestricted joint torus mean)" can yield H1-shell with ρ ≤ 0.414 (√(1/λ)). The bad-cluster restriction must enter the second-moment certificate.

**[N] lattice corroboration** (N14 a_enum, all classes vs bad only):
- Σ_all|r_A r_B|² per shell is 8.4e-5, 8.8e-5, 7.4e-5, 9.1e-5, 3.3e-5, 8.6e-5, 9.3e-5, 7.2e-5 for j = 5…12: flat, i.e. rate exactly λ^{−1} per λ-step × 2 classes per shell.
- The empirical A–B correlation factor Σ|r_Ar_B|²/(Σ|r_A|²Σ|r_B|²/#) grows 1.3 → 16 over j = 5…12.
- The bad-only S2 decays with C_cert(j) as in Thm A.

## 3. Rigorous partial results
### 3.1 Thm A — H1 for all shells j ≤ 14 [CA-fp: c3_mid radii, IEEE std model + libm ≤ 1 ulp; exponent factors in arb]
Sources:
- j ≤ 12: N15 a_cert3.
- j = 13: `code/a_cert_ext.py`. All 5100 classes; 5000 with zr < 6 run through c3_mid; zr ≥ 6 classes are coded for every g₀ ≤ 6.
- j = 14: `code/a_cert_shard.py`, 3 shards, same per-class computation.

Aggregation: `code/shell_law.py` → `logs/shell_law.json` (g₀ = 4).

| j | classes | bad | S2_up | Σ\|w\|_up | C_cert (ρ=0.2726) | C_cert (ρ=0.28) |
|---|---|---|---|---|---|---|
| 2 | 3 | 2 | 1.4985e-05 | 4.1016e-08 | 2.894e-05 | 2.774e-05 |
| 3 | 4 | 3 | 8.5635e-05 | 4.6516e-07 | 2.298e-04 | 2.157e-04 |
| 4 | 11 | 11 | 4.4864e-05 | 1.0998e-07 | 1.673e-04 | 1.538e-04 |
| 5 | 20 | 20 | 8.3963e-05 | 3.7267e-07 | 4.351e-04 | 3.916e-04 |
| 6 | 42 | 38 | 1.2509e-05 | 1.4053e-08 | 9.007e-05 | 7.938e-05 |
| 7 | 78 | 76 | 1.1560e-05 | 1.0009e-08 | 1.157e-04 | 9.981e-05 |
| 8 | 161 | 150 | 3.7493e-06 | 1.4945e-09 | 5.213e-05 | 4.405e-05 |
| 9 | 316 | 282 | 2.6393e-06 | 6.3567e-10 | 5.100e-05 | 4.219e-05 |
| 10 | 643 | 571 | 2.1886e-06 | 6.5664e-10 | 5.876e-05 | 4.760e-05 |
| 11 | 1274 | 1116 | 8.5058e-07 | 7.3407e-11 | 3.174e-05 | 2.517e-05 |
| 12 | 2555 | 2191 | 5.0777e-07 | 3.3206e-11 | 2.633e-05 | 2.045e-05 |
| 13 | 5100 | 4304 | 2.4243e-07 | 8.2651e-12 | 1.747e-05 | 1.328e-05 |
| 14 | 10225 | 8487 | 1.2889e-07 | 1.9697e-12 | 1.290e-05 | 9.609e-06 |

- max_j C_cert = 4.351e-4 (j = 5) ≤ 4.4e-4, as N14/N16 reported, now certified through j = 14.
- For j ≥ 8, C_cert ≤ 5.9e-5, and C_cert is *decreasing* (j = 12 → 14: 2.6e-5 → 1.3e-5).
- **Finite part of A_bad (g₀ = 4), j ≤ 14:** 2Σ|w|_up = 2.0315895e-6 (N15, j ≤ 12: 2.031569e-6).
- Core functional only. The true-functional (H4) correction for these shells is not run; N16 measured +2.4% on j ≤ 10.

### 3.2 Lemma R (renewal) [P; Lean `LineN20T.renewal`]
- **Statement.** Let t_n, e_k ≥ 0 with t₀ ≤ 1 and t_{n+1} ≤ Σ_{k=0}^{n} e_{k+1}t_{n−k}. If Σ_k e_k r^{−k} ≤ 1 for some r > 0, then t_n ≤ rⁿ for all n.
- **Application (first-return decomposition) [P].**
  - Let 𝒯_n be the carry-system transfer from (0,0) to (0,0) in n steps, and 𝓔_k the first-return excursion operators (𝓔₁ = 𝒦).
  - Then 𝒯_n = Σ_k 𝓔_k𝒯_{n−k}. The maps are Hermitian-preserving, because T_v(Z)* = T_{−v}(Z*) and e ↦ −e permutes excursions.
  - In the order-unit norm ‖Z‖_{Y_c} = inf{t : −tY_c ⪯ Z ⪯ tY_c} we have ‖𝒦‖ ≤ ρ̄ = 0.28 (CP + certificate).
  - Hence, if ‖𝓔_k‖ ≤ ε_k with Σ_{k≥3} ε_k r^{−k} ≤ 1 − ρ̄/r, then |ψ𝒯_n(ΦΦ*)ψ*| ≤ (ψ*Y_cψ)(Φ*Y_c⁻¹Φ)·rⁿ, uniformly in n.
  - For r = 0.30 the excursion budget is 1/15. For the joint system, use the ε-system with Y_c⊗Y_c and a per-ε-step ρ̄.
- This is the precise "finite-state transfer-operator" statement. The missing input is the excursion-norm sequence ε_k, which comes from non-CP sesquilinear maps on 495² (single) or 495⁴ (joint) matrices.
- **By Prop. F, for the joint unrestricted system no such ε_k exist with r < λ^{−1/2}.** The input must therefore be the bad-restricted excursion system.

### 3.3 Lemma G and obstruction O1 (λ-carries) [P; Lean `LineN20`]
- Carry states (e_{t−1}, e_t) lie in the box |e| ≤ 15. The transition (a,b)→(b,c) is allowed iff |c − 6b + a| ≤ 60.
- Kernel-checked facts (bitmask BFS, `decide +kernel`, no native_decide):
  - FW and BW are closed and depth-certified;
  - \|FW\| = \|BW\| = 769;
  - **\|FW ∩ BW\| = 633** (`reach_card`);
  - all of them have \|e\| ≤ 14 (`reach_le14`), and (−14, −14) is reachable (`reach_has14`).
  - Analytic counterpart: e = g∗v with g > 0 and v finitely supported gives |e| < 15; ℤ then gives ≤ 14 (`carry_strict`). The Green identities are `green_center`, `green_off`, `lam_mul`, `lam_add`.
- **Collatz–Wielandt** (`carry_cw`, `cw_support`): an integer vector x ≥ 0 supported exactly on the 633 states satisfies Ax ≥ 20x, so ρ(A) ≥ 20 (float 20.7596).
- **O1 [P].** Any scalar majorant Σ_paths∏κ(v_t) with κ ≥ κ_min on all edges grows at rate ≥ 20κ_min. The i.i.d. diagonal alone forces κ(0) ≥ ρ(𝒦) = 0.2726 [N], so a CS/norm-weighted (phase-free) automaton must have off-diagonal weights ≤ 1/20 of the target. [N] (`carry_majorant.py`): with κ(0) = 0.28, rate ≤ 0.30 needs κ₁ ≤ 0.0120. The letterwise values are 0.9–38 (N14).
- **The 633-state certificate must be phase-keeping**, as N15/N16 said, and by Lemma J/Prop. F it is in any case not the H1 object.

### 3.4 Prop. K — H1 ⇒ H3 bookkeeping [P + CA (arb, `code/tail_kp.py` → `logs/tail_kp.json`); rational checks in Lean]
- **Tail bound.** If H1-shell(C, J₀, 0.28) holds, then by ℓ³ ≤ ℓ² per shell [P, Lean l3_le_l2] and ℓ ≤ 2j + g₀:
  T₀ ≤ 2C^{3/2}e^{ag₀}Σ_{j>J₀}(qe^{2a})^j and T₁ ≤ 2C^{3/2}e^{ag₀}Σ_{j>J₀}(2j+g₀)(qe^{2a})^j, with q = 2^{(3/2)(1−β)} = 0.630056772834 ± 2.4e-13 and β = 1.44429750853 ± 4.1e-12 (arb).
- **Span bound** [P-sketch]: reductions occur only where |σ_i(μ)λ^{±t}| ≥ 1/2, giving span ≤ 0.787j + O(1) ≤ 2j for j ≥ 5. Measured span/j ≤ 2.
- **KP check.** KP needs S₀ + S₁/(1+g₀) ≤ a, with S = S^fin(certified) + T. Fixed-point iteration, then an arb check (g₀ = 4):

| J₀ | C | a | S₀^fin | T₀ | T₁ | S₀ + S₁/5 | KP | Re Λ_lo′ − S₀ − δ_true |
|---|---|---|---|---|---|---|---|---|
| 12 | 0.082 | 2.6925e-03 | 2.077625e-06 | 3.425e-04 | 1.146e-02 | 2.6397e-03 | ✓ | 2.764e-04 |
| 12 | 0.04 | 8.6596e-04 | 2.046268e-06 | 1.098e-04 | 3.669e-03 | 8.4898e-04 | ✓ | 5.091e-04 |
| 12 | 0.00088 | 8.2498e-06 | 2.031709e-06 | 3.481e-07 | 1.163e-05 | 8.0880e-06 | ✓ | 6.186e-04 |
| 12 | 0.00044 | 6.4867e-06 | 2.031679e-06 | 1.231e-07 | 4.111e-06 | 6.3595e-06 | ✓ | 6.188e-04 |
| 13 | 0.082 | 1.7356e-03 | 2.061155e-06 | 2.097e-04 | 7.432e-03 | 1.7016e-03 | ✓ | 4.092e-04 |
| 13 | 0.04 | 5.7084e-04 | 2.041263e-06 | 6.856e-05 | 2.428e-03 | 5.5965e-04 | ✓ | 5.503e-04 |
| 13 | 0.00088 | 7.3304e-06 | 2.031710e-06 | 2.193e-07 | 7.765e-06 | 7.1866e-06 | ✓ | 6.187e-04 |
| 13 | 0.00044 | 6.1617e-06 | 2.031690e-06 | 7.753e-08 | 2.745e-06 | 6.0409e-06 | ✓ | 6.188e-04 |
| 14 | 0.082 | 1.1273e-03 | 2.050746e-06 | 1.296e-04 | 4.851e-03 | 1.1052e-03 | ✓ | 4.893e-04 |
| 14 | 0.04 | 3.7702e-04 | 2.037976e-06 | 4.293e-05 | 1.606e-03 | 3.6963e-04 | ✓ | 5.760e-04 |
| 14 | 0.00088 | 6.7180e-06 | 2.031703e-06 | 1.382e-07 | 5.169e-06 | 6.5863e-06 | ✓ | 6.188e-04 |
| 14 | 0.00044 | 5.9452e-06 | 2.031690e-06 | 4.885e-08 | 1.827e-06 | 5.8286e-06 | ✓ | 6.188e-04 |

Lean (`LineN20T`): `kp_J12_C082`, `kp_J12_C88e5`, `kp_J14_C082`, `shell_margin`, `c32_082`, `c32_088e4` (rational re-checks of the arb upper bounds).

- **Conclusions:**
  - KP (H3) holds **for every C ≤ 0.082** at J₀ = 12, with a ≤ 2.70e-3 and budget left Re Λ_lo′ − A_bad^KP − δ_true ≥ 2.76e-4 > 0.
  - Convention note: under the N14 "tail ≤ ½ budget" rule, C_needed(12) = **0.08168**, not 0.082 (v4 rounds up). It is harmless because KP and positivity still hold at 0.082, but p₁ (gas vs Robin) moves up when A_bad^KP ~ 3e-4.
  - With the tail target T₀ ≤ 1e-6 (p₁ essentially unchanged): C ≤ 1.78e-3 (J₀ = 12), 2.42e-3 (13), 3.29e-3 (14).
- **Status of H3:** [P (KP + anchored corollary, N15-F2) + CA-fp finite part j ≤ 14 + CA tail arithmetic] **mod H1-shell**. The tail ℓ-weighting is now explicit (it was [P-sketch] in N15; the remaining [P-sketch] is the span bound). Background interplay and polymer normalisation stay [P-sketch], unchanged.

## 4. What remains for H1 (exact)
1. **(H1-bad) A polymer-restricted joint second-moment bound.** For the ε-chain with A on even sites and B on odd sites, restricted to ε-digit words with zero-runs < g₀, show
   Σ_{bad words, length n} |r_A r_B|² ≤ C₁·(ρ₁²)^n·#(words),
   with ρ₁ ≤ 0.28 (or any ρ₁ for which the Prop. K arithmetic closes; ρ₁ ≤ 0.30 needs C ≤ 0.036 at J₀ = 12).
   - By Prop. F this must see the restriction. By Lemma J it involves ε-carries with |e| ≤ 51 (6145 states) on 495⁴-dimensional sesquilinear blocks.
   - A Markov-partition / symbolic CP certificate is the natural form. It needs digit memory M with ε^{−M}·Lip_H ≪ 1 (M ≈ 8, 5^{17} states) unless a smarter cone is found. **Not feasible by direct computation.**
2. **(H1-ali) Lattice → main term.** By Lemma J, the on-dual Poisson modes are exactly the ε-exact collisions [P]. Near-collisions (Σu_kε′^k small but nonzero) need Beurling–Selberg box constants on the (L₁, L₂) cells. Not computed.
3. **(H1-tail)** j > 14 follows from 1 + 2. The finite part is done (Thm A).

**Best rigorous partial results:**
- H1-fin(14) [CA-fp], with C ≤ 4.36e-4;
- H1 ⇒ H3 with tolerance C ≤ 0.082 [P + CA];
- structural Lemmas P0, J, G, R and Prop. F [P].

## 5. Impact on THEOREM_DRAFT_v4
| Row | v4 | v5 (proposed) |
|---|---|---|
| H1 | OPEN [H]; 633-state certificate + box constants | **still OPEN [H]**, re-scoped: H1 = (H1-bad) + (H1-ali). The 633 states and the single-window [N] (torus ≈ iid) are *not* evidence for H1 (Lemma J, Prop. F). Finite part j ≤ 14 [CA-fp]. |
| H3 | KP explicit; tail = H1 [H] placeholder 1.56e-8 | **[P + CA mod H1-shell]** (Prop. K): placeholder removed; any C ≤ 0.082 (J₀ = 12) gives KP with a ≤ 2.70e-3. Remaining [P-sketch]: span bound, background interplay, normalisation. |
| H8 | prime h_p reduces to H1 | unchanged, but "H1" now means H1-bad + H1-ali |
| §3 | carry reduction row | add: Lemma J [P]; ε-carries \|e\| ≤ 51, 6145 states [P]; Prop. F [P]; Thm A j ≤ 14 [CA-fp]; Lemma R [P, Lean]; 633/≥20 [P, Lean] |
| §6 | — | withdraw "torus ≈ i.i.d., essentially the whole margin is available to the box/aliasing constant" (N16 §1.3) **for H1**; it holds only for single windows [N] |
| §7 "what remains" item 1 | 633-state certificate | replace by §4 items 1–3 |

No other H-row changes status: H0, H2, H4–H7 are untouched by this line.

## 6. Proposed v5 diff (not applied)
`THEOREM_DRAFT_v4_to_v5.diff` (unified diff against THEOREM_DRAFT_v4.md, produced from a scratch copy `scratch/THEOREM_DRAFT_v5_proposed.md`). v4 is unchanged.

## 7. Artifacts and reproduction
- **code/**
  - a_cert_ext.py, a_cert_shard.py, shell_law.py (Thm A);
  - tail_kp.py (Prop. K);
  - carry_graph.py, gen_lean_cw.py, carry_majorant.py (Lemma G/O1);
  - carry_graph_eps.py (Lemma J);
  - joint_torus_mc.py ([N] table);
  - run_ext.sh / run_ext2.sh (queues).
- **logs/:** *.json / *.jsonl / *.out as named above.
- **lean/:**
  - LineN20.lean v2 (carry graph via literal bitmasks + BFS-depth certificates, CW, Green): **19 s, EXIT 0** (`lean/build_LineN20.log`).
  - v1 (40-step iteration inside every proof) is kept as `LineN20_v1_superseded.lean.txt`. Its first run ended without messages after 8 min 19 s, but the exit code was not captured. A re-run was OOM-killed at 11 GB on the shared box, so **v1 is not claimed**; v2 replaces it.
  - LineN20Tail.lean (renewal, ε-Green, Prop. K arithmetic). Compiled with `lake env lean` in /workspace/audit/lineN12/lean/proj (Mathlib cache via `lake exe cache get`, nothing built from source). Logs in lean/build_*.log.
  - No `sorry`, no `native_decide`: grep in the manifest notes.
- **NOTES_N20.md** (timestamps from `date`). **SHA256_N20.txt** (written last) + SHA256_N20.txt.sha256.
- Background jobs: all N20 jobs had finished or been stopped by the end (see NOTES).
