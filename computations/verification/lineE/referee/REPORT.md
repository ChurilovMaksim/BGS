> **Repository copy.** Absolute scratch-directory paths of the audit machine are replaced by placeholders in angle brackets (`<referee-dir>` = the first referee's working tree, copied to `computations/verification/lineE/referee/`; `<referee2-dir>` = this audit's working tree, copied to `computations/verification/lineE/referee2/`; `<author-packet>` = the author packet; `<audit-clone>` = a fresh clone of the repository). They are not part of the repository. The text is otherwise unchanged.

# Referee audit of Line E (resonant residues of the kicked cat map)

**Object audited.** `<author-packet>/` (REPORT.md, OVERLAP.md, NOTES.md, code/, logs/, review/, lean/), against the repository `ChurilovMaksim/BGS` at main `347f173`. The repo was cloned read-only to `<workspace>/audit/BGS`.
**Auditor's working tree.** `<referee-dir>/` (`code/`, `logs/`, `lean/`, `certrun/`, `NOTES.md`). Backup: `<backup-dir>/`.
**Nothing was pushed, opened or posted.**

Quality gate applied (user's wording): nothing enters the repo unless it has been checked numerically, formalized (preferably in Lean), and checked for hidden logical or factual errors and exaggerations.

---

## 0. Verdicts at a glance

| # | Claim (short) | Verdict | Proposed final status |
|---|---|---|---|
| E1 | Resonant residue ν* = odd lift of −4̄ (mod h_m); exact collapse of the phase to ½nᵀH⁻¹n + κ_m(Σn)²/8; finite-N form with c(1+4/N) | **accept with minor fixes** (F13) | **proved** (paper proof complete and re-derived; Lean finite instances m = 5..21 plus general `pell` and `xy_mod`; independent exact and numerical checks) |
| E2 | Exact IFS / transfer-operator law Z_L = (1−λ^{−m}) Σ_a c_a Tr 𝓛_a^m, operators independent of m | **accept with fixes** (F8, F10) | **proved** (finite alphabet; cited trace formula; hypotheses verified) |
| E3 | Certified spectrum of 𝓛_a (k1 kick, L = 6/8, η-grid) | **accept with fixes** (F9) | **computer-assisted proved** (audited and re-run by referee; negative controls pass; scope: L-truncated operators only) |
| E4 | \|Z_L(m)\| ≥ (1−λ^{−m})·½(μ_lo^m − 4T₁r₂^{m−1}) > 0 for all odd m ≥ m0 | **accept** | **computer-assisted proved** (truncated kick; all m ≥ m0) |
| E5 | Physical k1 kick, η = 2, odd m ∈ [17,39]: F_m/2m ≥ 5.99 … 1426; W̃rest/m ≥ 7.98 … 2848 | **accept with fixes** (F1, F2, F6) | **computer-assisted proved, finite range, k1 kick only.** Not the TRACE-179 kick. |
| E6 | Asymptotic failure of R at η = 2 under hypothesis H∞ | **accept as conditional, with scope fix** (F1) | **conditional** (closure condition H∞; k1 kick only) |
| E7 | m = 15 prediction vs outcome | **accept with fix** (F5: the ± residues are mislabelled) | **numerical** |
| E8 | Full (Line B) kick: giant trace at the Galois image N ≡ ∓196 (mod h_m) | **accept with scope fix** (F12: fails when 3 \| m) | **numerical / open** |
| E9 | η-interval certification | — | **open** |
| E10 | TRACE-182 outlier = the ±196 resonance | **accept** (independently confirmed) | **numerical identification**. TRACE-182 stays **open**: its closure condition asks for a *proved* mechanism. |

Effect on the record: TRACE-179 (Conjecture R) stays **open**. Line E does **not** disprove R, even for a finite range of m, *for the kick R is about* (F1). TRACE-180 is **not** contradicted as a weak-convergence statement (F3). TRACE-182 stays open, with a numerical identification.

No hidden error was found that invalidates any mathematical identity or any certified inequality. The required fixes are about **scope, labelling, overstatement and reproducibility**. F1 (wrong kick for Conjecture R) is the only one that changes the meaning of the headline claim.

---

## 1. What I did independently

All of the following is my own code. The only things shared with the author are the definitions in TRACE-163.

| Check | Auditor code | Log |
|---|---|---|
| E1 exact congruence. Rational arithmetic; Nm computed in Z[λ]; H⁻¹ by exact sympy inversion; 40 random n per m. | `code/e1_exact.py` | `logs/e1_exact.log` |
| Exact Z_m(ν) for **all** units ν. Full alphabet, no n-truncation. Uses a new class-sum formula derived in §3.1 below; C/OpenMP. | `code/classes.c`, `code/aud.py`, `code/run_classes.py` | `logs/classes.jsonl`, `logs/T_*.npy` |
| Validation of the class-sum formula against the brute-force Line-B n-sum. | `code/t_validate.py` | `logs/t_validate.log` |
| Transfer operator, built a different way from the author's: collocation on \|s\| = ρ followed by FFT (not the binomial Galerkin). | `code/tmop.py`, `code/cmp_tm.py` | `logs/cmp_tm.log`, `logs/tm_m15.log` |
| Dense physical traces Tr(K M_N)^m at N = h_m − 4, compared with the finite-N law. | `code/direct_trace.py` | `logs/direct_trace.log` |
| E4/E5 arithmetic in arb (independent Bessel sums), with comparison to the true values. | `code/own_bounds.py` | `logs/own_bounds.log` |
| E10 decomposition. | `code/e10.py` | `logs/e10.log` |
| Factorizations of h_m, m ≤ 41. | inline sympy | `logs/h_factor.log` |
| Identity behind the "t* coincidence" (§8). | inline | `logs/tstar_identity.log` |
| Re-run of the author's `cert.py`, plus a no-cache variant and 3 negative controls. | `certrun/` (author code copied; sha256 in `certrun/sha256.txt`) | `certrun/*.out`, `*.json` |
| Lean build, `#print axioms`, and a negative control. | `lean/LineE_audit.lean`, `lean/Neg.lean` | `logs/lean_audit.out`, `logs/lean_neg.out` |

---

## 2. E1: re-derivation on paper

Notation: q(n) = nᵀH⁻¹n. By TRACE-163 Lemma Q, y′Nm(α_n)/g′ = 2q(n) − β(n) with β(n) ∈ Z. So for any integer ν,
  −νy′Nm(α_n)/g′ ≡ −2ν q(n) (mod 1).

For odd m: D = 4h², g′ = 2h, y_m = h·y′, x_m − 1 = 2h². Write 4ν* + 1 = −k·h; k is odd. Then

  −2ν*q − ½q = −(4ν*+1)q/2 = k·h·q/2 = k·r/(8h),  with r = nᵀXn = D·q ∈ Z.

Here X_ij = φ(|i−j|) and φ(d) = y_m x_d − (x_m−1)y_d = h(y′x_d − 2h y_d). So r/h ∈ Z, and the question is r/h mod 8:

- **Diagonal (d = 0):** the coefficient is y′. It enters with weight 1.
- **Pairs (d ≥ 1):** the coefficient is y′x_d − 2hy_d. It enters twice, so it only matters mod 4.
  - Using x_d ≡ (−1)^d (mod 4), y_d ≡ d (mod 2) and h odd, it is ≡ (−1)^d y′ − 2d (mod 4).
  - Because y′ is odd, this is ≡ y′ (mod 4) for both parities of d.

Hence k·r/h ≡ k·y′(Σn)² (mod 8), which is exactly E1 with κ = k·y′ mod 8 (odd). ∎

Side facts:
- Since h² + 1 = 2y′², y′ is odd and coprime to h.
- The odd lift is unique mod 2h, so κ does not depend on the choice of ν*.

**Finite N.** Theorem 1 of TRACE-163 contributes the factor e(Q/N) with Q = 2q, which equals e((4/N)·½q). That gives the factor (1+4/N). Correct.

**Gaps found.**
1. The hypothesis gcd(N, D_m) = 1 is automatic: N is odd and N ≡ −4 (mod h). It is redundant, not wrong.
2. The κ table (7, 5, 3, 1 for m ≡ 5, 7, 1, 3 mod 8) is verified for m ≤ 41 only. It is not proved. It is also inessential, because every odd κ gives |c_a| = ½ (a even). It should be labelled [N] or proved (F13).
3. No sign or parity error. The −4̄ ↔ +4̄ symmetry holds exactly: at −ν* the form is −½q − κ(Σn)²/8 (checked exactly; `e1_exact.log`).

**Checks.**
- Exact identity holds for m = 5..25 (40 random n each).
- κ table confirmed for m = 5..41. In this range k ∈ {−5, −3}; the REPORT only says "k odd".
- Control: ν* + 2 fails.
- Dense physical traces at N = h_m − 4 for m = 5, 7, 9, 11 agree with my independent transfer-operator evaluation of the c(1+4/N) law:
  - |Tr U|²: relative agreement 6e-9 to 2e-8;
  - complex ratio Tr U/Tr M: agreement 1e-7 to 7e-6;
  - |Tr M_N^m| = 1 to 1e-14.
- My dense |Tr U|² reproduce the author's matrix-free values: 121.83215496, 2120.2047659, 29946.148430, 405032.63049.

## 3. E2: re-derivation and hypotheses

**Quadratic form.** H⁻¹ has circulant entries G(d) = c(λ^{−d} + λ^{−(m−d)})/(1−λ^{−m}), with c = 1/(λ−λ⁻¹) = 1/(4√2).
- With s_j = Σ_{k≥1} n_{j−k}λ^{−k} over periodic n, s_j = (1−λ^{−m})⁻¹ Σ_{d=1}^m n_{j−d}λ^{−d}.
- Off-diagonal: c·½(λ^{−d} + λ^{−(m−d)})/(1−λ^{−m}) = ½G(d). Checked.
- Diagonal: c[λ^{−m}/(1−λ^{−m}) + ½] = ½G(0). Checked.
- Recursion: s_{j+1} = (s_j + n_j)/λ. Checked.

**Sectors.** b = Σn mod 8 is well defined in e(κb²/8). The coefficients are c_a = DFT⁻¹, and |c_a| ∈ {½, 0} by the Gauss sum mod 8; c_a = 0 for odd a, by b → b + 4. Checked.

**Trace law.** 𝓛_a^m is a *finite* sum over words w of weighted composition operators M_{p_w}C_{ψ_w}, with ψ_w affine of slope λ^{−m}.
- If ρ > L/(λ−1), every ψ_n maps D̄_ρ into D_ρ (θ_n < 1).
- Each M_{e(cn·)}C_{ψ_n} is trace class on H²(D_ρ), with ‖·‖₁ ≤ e^{2πc|n|ρ}/(1−θ_n). This uses the rank-one expansion Σ_k ⟨·,e_k⟩ e_k∘ψ_n and ‖e_k∘ψ_n‖ ≤ θ_n^k. This is exactly the author's T₁.
- The trace formula Tr(M_pC_ψ) = p(s*)/(1−ψ′(s*)) for a holomorphic strict self-map of a disc (Ruelle 1976; Bandtlow–Jenkinson 2008) is applied word by word. The unique fixed point of ψ_w gives the periodic s_j, and 1 − ψ_w′ = 1 − λ^{−m}.
- H²(D_ρ) is a Hilbert space, so Lidskii's theorem applies.
- **The hypotheses are satisfied for the operators as defined** (finite L, ρ = 2 > 6/(λ−1) = 1.243 and > 8/(λ−1) = 1.657).
- **m-independence is real.** The weights do not involve m. m enters only through the scalar (1−λ^{−m}), through c_a (via κ, i.e. m mod 8) and, at finite N, through c → c(1+4/N).

**Gaps found.**
1. `review/predict_finiteN.py` (which produced the §3 finite-N table) uses L = 12 with ρ = 2.0 < 12/(λ−1) = 2.485. The trace-formula hypothesis fails there. The agreement is numerically harmless because |J_n(1.8)| < 1e-9 for n ≥ 10, but the table as produced is not an instance of E2 (F8). My rerun with L = 10, ρ = 2.6 agrees to about 1e-8.
2. The REPORT cites "Ruelle, Bandtlow–Jenkinson" without a theorem number. The proof should state the exact statement used (F10).
3. E2 holds for the truncated (finite-support) kick only. The REPORT says so; keep it explicit everywhere.

### 3.1 Independent exact evaluation of Z_m(ν), including the full alphabet

I derived a new, n-truncation-free formula from TRACE-163 Theorem 3, the support 𝒮 = ½𝟙 + V^_odd, and an explicit Gauss sum over O/hO (O = Z[√2]):

  |Z_m(ν)|² = h⁻² · |Σ_{r∈Z/h} e(v·r/h) T(r)|²,  where
  - T(r) = Σ_{(z₀,z₁)∈(Z/h)², Q(z)≡r} Π_{j<m} g(½ + z_j/h),
  - z_{j+1} = 6z_j − z_{j−1},
  - Q(z) = z₀² − 6z₀z₁ + z₁²,
  - v = −16̄·ν̄·ȳ′ (mod h).

It is validated against the brute-force TRACE-163 n-sum (k1 kick, m = 5, all six tested ν agree to the L = 7 truncation error, ≤ 2e-5 relative) and against Line B's published numbers:
- F_11(2) = 122.358 (TRACE-182 reports F/2m = 5.56);
- F_13(2) = 223.3285 (Line B `fast_classes.py`).

**Results (k1 kick, η = 2): exact |Z(ν*)|² against the transfer-operator law.**

| m | exact class sum | my TO, L = 10 (rel. diff) | TO, L = 6 (rel. diff) |
|---|---|---|---|
| 5 | 154.3840478 | 1.8e-9 | 2.6e-5 |
| 7 | 2220.053413 | 2.3e-9 | 2.8e-5 |
| 9 | 30215.97902 | 4.0e-9 | 2.1e-5 |
| 11 | 405788.6781 | 5.2e-9 | 3.4e-5 |
| 13 | 5458875.790 | 6.2e-9 | 3.9e-5 |
| 15 | 73486698.75 | ≈1e-8 (73486698) | 4.5e-5 |

The −ν* residue matches the TO with c → −c, κ → −κ, to about 1e-6 (L = 12, the limit of float conditioning).

**F_m/2m at η = 2 (exact class sums, all units).**

| m | 5 | 7 | 9 | 11 | 13 | 15 |
|---|---|---|---|---|---|---|
| k1 kick | 1.843 | 2.805 | 4.839 | 6.894 | 11.197 | 27.885 |
| Line B (full diagonal) kick | 1.710 | 2.729 | 1.816 | 5.562 | 8.590 | 3.910 |

Comparison with the author:
- k1 m = 11: F = 151.67, matches.
- k1 m = 15: F = 836.549, matches the author's 836.55 and 27.9.
- Full kick m = 13: F = 223.3285, matches.

## 4. E3–E5: audit of the certified computations

**Code read line by line (`cert.py`, `bounds.py`).**

- **Basis and Galerkin matrix.** The basis is e_k = (s/ρ)^k.
  - The multiplication block M[l,j] = (2πicnρ)^{l−j}/(l−j)! is lower triangular. The composition block C[j,k] = binom(k,j)λ^{−k}(n/ρ)^{k−j} is upper triangular.
  - Therefore P_K M C P_K = (P_K M P_K)(P_K C P_K). The Galerkin section is exact, with entries computed as arb balls.
- **Truncation error δ.**
  - ‖𝓛 − P𝓛P‖ ≤ ‖𝓛(I−P)‖_HS + ‖(I−P)𝓛P‖_HS.
  - δ1 is a column-tail bound via ‖e_k∘ψ_n‖ ≤ θ_n^k (Minkowski). Correct.
  - δ2 is a Cauchy estimate on |s| = 2ρ, with sup|e_k∘ψ_n| = ((2ρ+|n|)/(λρ))^k and sup|e(cns)| = e^{2πc|n|2ρ}. Correct.
- **Sector 4.**
  - The Householder vector is built from midpoints, so H is an exact unitary involution enclosed by balls, and B = HAH is an exact similarity.
  - The resolvent of the block-triangular T₀ ⊕ 0 is bounded by 1/|b₁₁−z| + |b₁₂|‖(Y−z)⁻¹‖/|b₁₁−z| + ‖(Y−z)⁻¹‖ + 1/|z|. The last term covers the zero block of P𝓛P. Correct.
  - The Neumann bound from ‖Y^j‖_F (j ≤ p) is valid for all |z| ≥ r, since it is monotone in |z|. This makes the "no sampling" claim correct.
  - The perturbation is b₂₁ + δ, with b₂₁ the 2-norm of the column. The homotopy/rank argument is correct. The contour centre is the exact b₁₁ (inside its ball), so |μ*| ∈ [|b₁₁|−r₁, |b₁₁|+r₁] is rigorous.
- **Sectors 0, 2, 6.** A resolvent bound holds for all |z| ≥ r₂, so the spectrum lies in |z| < r₂. No homotopy is needed. Correct.
- **E4 step.** Weyl's inequality Σ|μ_k| ≤ ‖𝓛‖₁ ≤ T₁, together with |μ|^m ≤ r₂^{m−1}|μ| for |μ| ≤ r₂, gives the 4T₁r₂^{m−1} term. The bound increases in m once it is positive (μ_lo > r₂). Correct.
- **E5 step.**
  - |Z − Z_L| ≤ s₀^m − (s₀−t_L)^m, by absolute values over the words with at least one letter |n| > L. Correct.
  - F ≥ |Z(ν*)|²/φ(2h), with φ(2h) = φ(h) ≤ h − 1. Correct.
  - W̃rest = F − B^sym − 2mχ_m ≥ F − 4m, using B^sym ≤ 2m (TRACE-165) and |χ_m| ≤ 1 (an average of unimodular numbers). This needs **no** kick-specific input; for the even k1 kick, χ_m ≡ 1 exactly. Correct.
- **Float leakage.**
  - JSON floats are re-padded by (1 ∓ 2⁻⁵⁰) in `bounds.py`. That covers round-to-nearest; I used 2⁻⁵¹ padding independently.
  - The Bessel tail beyond n = 119 is covered only by a (1 + 2⁻²⁰) factor, not by an explicit bound. It is harmless (terms ≤ 1e-150) but should be made explicit (F9).
  - numpy is used only to precondition (approximate eigenvector), which is legitimate.
- **Latent bug.** `powers_bound` caches by `id(Y)` without holding a reference, so a freed matrix's id can be reused (sector 6 could silently receive sector 2's norms).
  - I re-ran with references held (`certrun/cert_nocache.py`). Sector 6 is then computed independently and is identical to sector 2.
  - This is explained by an exact symmetry I derived: with R: φ(s) ↦ φ(−s) (unitary), w_a(−n) = w_{−a}(n), so 𝓛_{8−a} = R𝓛_aR.
  - The timings show no cache hit occurred in the logged runs. No result is affected (F9).

**Reruns.**

| Run | Result |
|---|---|
| Author's `cert.py` (η = 2, L = 6, K = 100, 700 bits) | Reproduces `logs/cert_L6.json`: δ, T₁ and all sector numbers are identical. b₁₁ differs by about 1e-88, because numpy's eigenvector is not deterministic; harmless. |
| Negative control K = 60 | Sector 4 fails (F·R₁ = 976). Expected. |
| Negative control r₁ = 1e-16 | Sector 4 fails. Expected. |
| Negative control r₂ = 0.85 | Sectors 2/6 fail; their spectral radius is 0.877. Sector 4 still certifies, which is correct (Y-root 0.81). Expected. |
| All 9 certificates | m0 recomputed: 17, 17, 17, 17, 19, 41, 49, 63, 103. All match. Every sector is `certified: true`. |
| My float spectrum (different construction) | \|μ*\| = 1.91547605 (L = 6), inside [1.9154751, 1.9154771]. Sectors 2/6 equal; spectral radii 0.877 / 0.574. Same picture. |
| E4/E5 arithmetic with my own arb code | Reproduces the author's tables digit for digit (η = 2 L = 6 and L = 8; η = 1.5; η = 1.75). |

**Try-to-break.**
- At every m in 13..41 and every certificate tested, the lower bounds lie **below** the true values (TO at L = 6 for Z_L; L = 10 for the physical Z). Examples:
  - m = 17, L = 6: Z_L ≥ 21328 vs true 31454;
  - m = 39, L = 8: Z_phys ≥ 3.65e9 vs 5.10e10.
- No violation was found. The bounds are loose by factors of 1.5 to 15.

**Scope issues (not errors).**
1. E3 certifies the **L-truncated** operators only. The physical μ (L → ∞) is uncertified. Float values: 1.9154733 (L = 10) vs 1.9154761 (L = 6).
2. In the E5 headline, the η = 1.5 and η = 1.75 ranges quoted are where the bound is *positive*, not where it *violates* anything (F2).
   - F_m/2m ≥ 2 is needed for W̃rest > 0, and ≥ 2.5 for |W̃rest| > m.
   - η = 1.5: F/2m ≥ 0.45 (m = 17), 1.18 (19), 2.02 (21), 3.05 (23), …, 3.75 (33). A violation of |W̃rest| ≤ m holds only for m ∈ [23,33].
   - η = 1.75: only for m ∈ [19,27].
3. The REPORT's §5 "Sanity" line says "true F/2m ≈ 18" at m = 17. That number is the single-residue term |Z(ν*)|²/φ(h)/2m = 18.3, not F/2m. The true F/2m includes the ±ν* pair plus background, so it is roughly 2 × 18.3 + 2 (F6).
4. R_NSW sub-sequence: h_29 = 63018038201 is also prime, so m = 29 (F/2m ≥ 310) belongs in that list next to m = 19 (nit).

## 5. E6 (conditional)

The logic "H∞ ⇒ |Z(ν*)| ≍ |μ∞|^m ⇒ F ≥ c(|μ∞|²λ^{−1/2})^m" is correct, using h_m < λ^{m/2}/2. The obstacle is described honestly.

Two points:
- **(a) Scope.** "Conjecture R fails at η = 2" must read "**the k1-kick analogue** of Conjecture R fails" (F1).
- **(b) Suggested route.** Use H²/H^∞ on thin *stadium* domains {dist(s, [−R,R]) < τ} instead of discs. The multiplier bound e^{2πc|n|τ} is then independent of R, and the superexponential decay of J_n wins. This is the author's "strip" idea made concrete. It is a suggestion only; nothing is claimed.

## 6. E7, E8, E10

**E7.** Correct prediction (F/2m ≥ 20) and outcome (27.885). However, the quoted "|Z(ν*)|² = 7.3491e7 vs transfer operator 7.3487e7 (6e-5)" **compares the two different residues** (F5):
- the exact values are |Z(ν*)|² = 7.34867e7 and |Z(−ν*)|² = 7.34915e7;
- each matches its own transfer-operator law to about 1e-8 (L = 10);
- the 6e-5 "discrepancy" is a labelling artefact.

**E8.** Exact class sums for the Line B diagonal kick at η = 2 put the top two residues at N ≡ ∓196 (mod h) for m = 7, 11 and 13. **But at m = 9 there is no such resonance:** the top |Z|² is about 897, against about 3e5 at m = 11. This is because 7 | h_m whenever 3 | m, so 49 is not invertible and there is no Galois image (F12). Full kick, m = 15 (exact, all 223200 units): F/2m = **3.910**, far below m = 13 (8.590). The resonance is *diluted*. The top residues are the 12 unit classes N ≡ ±196 (mod h/7), each with |Z|² ≈ 1.09e6 (against 3.6–4.2e6 for the true Galois image at m = 13). Together they carry 1.745 of the 3.910; the remainder is 2.165. At m = 9 the same classes carry only 0.39 (logs/e8_m9_m15.log). So the full-kick evidence against R is **not monotone in m**: it is strong for 3 ∤ m and weak for 3 | m. Any extrapolation must treat the two subsequences separately.

There is also a clean **rigorous corollary**, which the author did not state. For the pure 7-mode kick f₇(q) = 0.9cos(2π·7q):
- Z_{f₇}(ν) = Z_{k1}(49ν) exactly, so F_m(f₇) = F_m(k1) whenever 3 ∤ m;
- hence E5 holds verbatim for f₇ at m ∈ {17, 19, 23, 25, 29, 31, 35, 37}.

This is still **not** the Line B kick, which has 13 further modes of size up to 0.05.

**E10 (confirmed).** Full kick, η = 2: the two residues N ≡ ±196 carry most of F/2m, and what remains is close to the parity-doubled diagonal baseline of about 2 (logs/e10.log):

| m | F/2m | carried by the two residues | remainder |
|---|---|---|---|
| 11 | 5.562 | 3.522 | 2.040 |
| 13 | 8.590 | 6.458 | 2.132 |
| 7 | 2.729 | 1.111 | 1.618 |

This is a numerical identification of the TRACE-182 outlier. A *proof* for the full kick is missing, so TRACE-182's closure condition ("a proved mechanism") is not met.

## 7. Lean

- `lake exe cache get` (no download, Mathlib cache present; no Mathlib build), then `lake env lean` on an unmodified copy (sha256 b3a91202…).
- Builds in about 17 s.
- `#print axioms`:
  - `pell`: [propext];
  - `xy_mod`: [propext, Classical.choice, Quot.sound];
  - `cert5`, `cert13`, `cert21`, `cert11_control`: [propext].
- No `sorry`, no `native_decide`, no `axiom`, no `implemented_by`.
- Negative controls:
  - `cert11_control` (cert 5 6091 = false) holds;
  - `#eval cert 3 181` = false, and `cert 3 (179+239)` (even, not a unit) = false;
  - `cert 3 (179+2·239)` = true (the other lift of the same class, as it should be);
  - my `Neg.lean` (`theorem bad : cert 3 181 = true := by decide`) **fails** with "decide proved that the proposition is false".
- **Statement match.** `cert` encodes exactly the coefficientwise congruences:
  - diagonal mod 8h²;
  - pairs mod 4h², with d = |i−j| ∈ [1, m−1];
  - together these imply the E1 identity for every n ∈ Z^m at that m.
- **Coverage: fragment.**
  - The E1 identity at the level of Z(ν) is not stated in Lean; the step from coefficients to Z is a one-line paper argument.
  - General m is not covered, although the paper proof is short and could be formalized from `xy_mod` and h_m-Pell facts. Recommended, not required.
  - gcd(y′, 2h) = 1 is not checked, but it is not needed for the identity.
  - E2–E6 are not formalized (analytic, and ball arithmetic).
- **Reproducibility gaps.**
  - The author's `logs/lean_lineE.out` contains only timing; the axiom claim in the REPORT is not logged.
  - The file is not yet placed under `formalization/Bgs/` with a build target (F7).

## 8. Novelty and overstatement

- **Keating–Mezzadri (2000)** (abstract checked).
  - Pseudo-symmetries are arithmetic quantum symmetries (operators commuting with U_N on special N) that change the *eigenvalue statistics*.
  - The Line E resonance is **m-specific**: the class N ≡ −4 (mod h_m) changes with m. Its mechanism is reciprocity: N ↦ an effective "dual dimension" −4, so the phase becomes ½q. It is not a symmetry of U_N.
  - "E1–E2 are a concrete instance … exactly a pseudo-symmetry-driven deviation" is an **overstatement** unless such an operator is exhibited. Downgrade to "analogous arithmetic effect without classical limit" (F4).
  - Line B's own non-claim 3 already warns against KM attributions.
- **Faure–Nonnenmacher–De Bièvre / Bonechi–De Bièvre.** The REPORT is correct that the mechanism and regime differ (short period of S mod N vs a fixed m with N → ∞ in a residue class).
- **Kurlberg–Rudnick.** The placement is fine. Line B already notes that KR/Bourgain bounds do not apply (ord_h λ = m).
- **Boasman–Keating 1995 / TRACE-163.** Correctly cited as the starting formula.
- **TRACE-133..137.** No overlap, as OVERLAP.md says.
- **The "t* coincidence" with the TRACE-134 family (35, 1189).** It is a Pell identity, not a coincidence: h_{m−2}·y_{(m−1)/2} ≡ 1 (mod h_m) for every odd m (verified for m = 5..79). So t* = h_{m−2}⁻¹ = y_{(m−1)/2}, and 35 = y_3, 1189 = y_5, 40391 = y_7. There is still no dynamical link (F11).
- **Missing from OVERLAP.md.** TRACE-117/118/119 (kick-blind arithmetic spikes at Pell dimensions N = u_n) and FM-036 (Pell moduli). They are related in spirit but differ in regime (N itself a Pell number, minimal period), so they are not overlapping. They should be listed (F11).
- **Overstatements found.**
  - (i) Kick scope of R (F1). This is the main issue.
  - (ii) "TRACE-180 contradicted" (F3).
  - (iii) KM "concrete instance" (F4).
  - (iv) η = 1.5/1.75 ranges (F2).
  - (v) "true F/2m ≈ 18" (F6).
  - (vi) E7 6e-5 (F5).
- **No claim** of a BGS counterexample or of an asymptotic disproof was found. The non-claims section is good.

---

## 9. Required fixes

- **F1 (blocking; scope).**
  - **Problem.** Conjecture R (TRACE-179) concerns W̃rest for **Line B's fixed kick**, the 32-mode A_N whose diagonal part f has 14 modes with c_{±7} = 9/20 (see `derandomized_fixed_kick.md`, Setting). E3–E6 are about the **single-cosine kick f₁(q) = 0.9cos2πq** ("k1"). That is a different, parity-even model.
  - **Required.**
    - Rewrite the title, §0, the E5/E6 rows, the non-claims and §9 to say "the k1-kick analogue of Conjecture R".
    - State that for the TRACE-179 kick the evidence is numerical (E8/E10; m ≤ 15) and has a structural hole at 3 | m.
    - Optionally add the rigorous corollary for the pure 7-mode kick (§6).
    - The sentence "E5 does refute any quantitative form '|W̃rest_m| ≤ m for m ≥ 17' at η = 2" must say "for the k1 kick".
- **F2.** In E5, separate the positivity range from the violation range for η = 1.5 (violation of |W̃rest| ≤ m only for m ∈ [23,33]) and η = 1.75 (m ∈ [19,27]).
- **F3.** TRACE-180 is "not contradicted as a weak-convergence (CLT) statement". An atom of mass 1/φ(h) → 0 is compatible with convergence in law of Z(ν)/√(bulk variance). Only the moment version (M4 → 2) and normalisation by √F fail. Reword in §9 and OVERLAP.md.
- **F4.** Keating–Mezzadri: replace "concrete instance … exactly a pseudo-symmetry-driven deviation" with an analogy statement (§8).
- **F5.** E7: correct the numbers. |Z(ν*)|² = 7.34867e7 (exact class sum) = TO 7.34867e7 (about 1e-8). The value 7.3491e7 is |Z(−ν*)|².
- **F6.** §5 sanity line: "|Z(ν*)|²/φ(h)/2m ≈ 18.3", not "true F/2m ≈ 18".
- **F7 (reproducibility).**
  - `review/indep_trace_full.py` and `review/predict_finiteN.py` import `drv`/`dlib.CK` from `<author-workspace>/code` and `<lineB-workspace>/code`, which are outside the packet. Vendor them or switch to `computations/verification/lineB/common/model.py`.
  - Pin the venv: python-flint 0.9.0, numpy 2.5.4.
  - Put the Lean file at `formalization/Bgs/LineE.lean` with `lake build Bgs.LineE`, and log `#print axioms`.
  - Do not ship `lineE/claims.json`; it is a full copy of the registry. Ship proposed entries instead.
- **F8.** Re-generate the §3 finite-N table with ρ > L/(λ−1) (e.g. L = 10, ρ = 2.6, or the auditor's `direct_trace.py` + `tmop.py` output), or state the hypothesis violation.
- **F9 (certificate hygiene).**
  - Fix the `id()`-keyed cache in `cert.py` (hold references, or key by sector), and/or state and use the symmetry 𝓛_{8−a} = R𝓛_aR.
  - In `bounds.py`, replace the (1 + 2⁻²⁰) tail padding by an explicit bound for n > 119.
  - Record the seed and OS for the numpy eigenvector, or note that b₁₁ varies at the 1e-88 level.
- **F10.** E2 proof: state the trace-class estimate (the 2-line rank-one argument), the precise trace-formula theorem, the finite word expansion, and Lidskii on the Hilbert space H²(D_ρ). Keep "finite L" in the statement.
- **F11.** OVERLAP.md: replace the "coincidence" with the identity h_{m−2}y_{(m−1)/2} ≡ 1 (mod h_m), and add TRACE-117..119 and FM-036 to the comparison.
- **F12.** E8/E10 scope: the Galois image 49̄ν* exists only when 7 ∤ h_m, i.e. 3 ∤ m. State it, and record the full-kick results at m = 9 (F/2m = 1.82) and m = 15 (F/2m = 3.91, diluted resonance on N ≡ ±196 mod h/7) (§6).
- **F13.** E1: drop the redundant gcd hypothesis, or note that it is automatic. Label the κ table [N] (m ≤ 41) or prove it, and note that it does not matter (|c_a| = ½ for every odd κ). Say k ∈ {−5, −3} (observed) rather than only "k odd".

**Nits.**
- Add m = 29 (h_29 prime) to the R_NSW remark.
- In §4, "|μ*| ∈ [1.86547, 1.96547]" for L = 8 is just b₁₁ ± 0.05. Say so, or tighten r₁ (it certifies at 1e-6 for L = 6).
- The REPORT §7 "Positivity check … m = 11: F = 151.67 ≥ |Z|²/φ = 52.3" is correct (405789/7744 = 52.4); fine.
- In §2, "k odd" is true, but the sign is negative.

## 10. Proposed final statuses

| Claim | Status | Ledger note |
|---|---|---|
| E1 | proved | analytic proof + Lean finite instances (m = 5..21, general pell/xy_mod) + independent exact check (m ≤ 25) + direct-trace check (m ≤ 13) |
| E2 | proved | finite alphabet; cited trace formula + Lidskii; numerically confirmed against an exact full-alphabet class sum (m ≤ 15, 1e-8) |
| E3 | computer-assisted proved | L-truncated k1 operators on a 9-point η grid; code audited, re-run, negative controls |
| E4 | computer-assisted proved | truncated k1 kick, all odd m ≥ m0 |
| E5 | computer-assisted proved | k1 kick only, finite m-ranges; **no** consequence for TRACE-179 as stated |
| E6 | conditional | closure condition H∞; k1 kick |
| E7 | numerical (record) | with F5 |
| E8 | numerical (open) | with F12 |
| E9 | open | — |
| E10 | numerical identification | TRACE-182 stays open |

## 11. Files for the repo packet (after the fixes)

**Mathematics.**
- `mathematics/fixed-map/resonant_residue_lineE.md`: the revised REPORT, with E2 proof details (F10) and scope (F1).
- The revised OVERLAP.md, as an appendix.

**Code** (`computations/verification/lineE/`):
- `pell.py`, `resid.py`, `ifs_explore.py`, `trace_check.py`, `cert.py` (fixed, F9), `bounds.py` (fixed), `run_certs.sh`, `run_certs2.sh`, `tm2.py`;
- review/`indep_trace.py`, `indep_trace_full.py` (vendored deps, F7), `predict_finiteN.py` (ρ fixed, F8).

**Logs** (`computations/verification/lineE/logs/`):
- all 9 `cert_*.json` with `.out` and `_bounds.json`: `cert_L6`, `cert_L8b_eta2`, `cert_L6_eta{1.25,1.5,1.75}`, `cert_L6r145_eta{2.25,2.5,2.75,3.0}`;
- not the superseded `cert_L6_eta{2.25..3.0}` (sectors 2/6 uncertified), `cert_test*`, `cert_L10*` or `cert_L8_eta2` (superseded by L8b) — unless clearly labelled as superseded;
- `indep_trace.jsonl`, `indep_m13.out`, `lineB_fastclasses_m13.out`, and the Lean log with axioms.

**Lean.** `formalization/Bgs/LineE.lean` (unchanged content), with a build log and the `#print axioms` output.

**Referee material** (`computations/verification/lineE/referee/`): this REPORT, NOTES.md, `code/` (aud.py, classes.c, e1_exact.py, tmop.py, cmp_tm.py, direct_trace.py, run_classes.py, own_bounds.py, e10.py, t_validate.py), `logs/` (excluding the large `T_*.npy`, or with them as evidence), `certrun/` (rerun outputs and negative controls), `lean/` (audit copy and Neg.lean).

**Registry.** New entries for E1–E10 with the statuses above. Annotations on TRACE-179 (k1 analogue refuted on a finite range; R itself untouched), TRACE-180 (moment form fails at η ≈ 2) and TRACE-182 (numerical identification).

## 12. Reproduce (auditor)

```
P=<python-venv>/bin/python        # numpy, scipy, sympy, python-flint 0.9.0
cd <referee-dir>/code && gcc -O3 -march=native -fopenmp -o classes classes.c -lm
$P e1_exact.py; $P t_validate.py; $P run_classes.py k1 2.0 5,7,9,11,13,15; $P run_classes.py full 2.0 5,7,9,11,13,15
$P cmp_tm.py; $P direct_trace.py 5,7,9,11; $P own_bounds.py <author-packet>/logs/cert_L6.json; $P e10.py
cd <lean-build-tree>/formalization && lake exe cache get && lake env lean <referee-dir>/lean/LineE_audit.lean
```
