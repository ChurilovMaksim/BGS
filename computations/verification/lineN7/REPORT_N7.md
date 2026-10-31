# REPORT_N7: toward an unconditional Theorem R♯. (±2,16) closed; exact orbit lemma for all isotropic points; gap (a) reduced

*2026-10-31, Asia/Yekaterinburg (UTC+5).*
- Directory: `/workspace/bgs-lineN/N7`. Running log: NOTES_N7.md. Hashes: SHA256_N7.txt.
- Not modified: N2–N6, J3, Line F. J3 and Line F code was only *executed*, with all output written to N7.
- Nothing was pushed.
- The referee fixes for N6 are in **REPORT_N6_v2.md** (this directory).
- By the parent's split, gap (b) belongs to N7b. A note file was left at `/workspace/bgs-lineN/N7b/NOTES_FROM_N7.md`.

Labels:
- [P]: proved.
- [P-sketch]: argument complete in outline, details not written out.
- [CA]: computer-assisted, rigorous.
- [N]: numerics without error control.
- [H]: heuristic.

## 0. Summary
| # | Result | Label |
|---|---|---|
| 1 | **(±2,16) closed at every level.** J3's untwisted radius is sharpened from R ≤ 1.6677 to a dominant-eigenvalue enclosure **\|μ₁₆\| ≤ 1.635413**, with the rest < 0.95 (8 factors). Hence \|Z_(±2,16)\| ≤ 2.273e5·1.6355^m, Σ_ρ\|Z_ρ\|² ≤ 4\|Z₈\|² for m ≥ 51, and the Dev floor plus Robin's bound remove **all (±2,16) members at all levels for p ≥ 339**: their cost is ≤ 0.01·F_m. | [CA] + [P] |
| 2 | **Lemma P (family pattern), [P].** The twist sequence of the 16D = 1 family is given in closed form for all i (two exact representatives). Its windows, the A/B cores with a = (2−√2)/4 and b = √2/4, and the geometric tails all follow, with errors O(λ^{−k}). | [P]; exact check to 1e-390 |
| 3 | **Lemma P′ (all isotropic points), [P].** Every isotropic point at q = h_p is x = z + eγ/(8q), with z one of the 8 λ-fixed points and e ∈ O. An exact identity gives two windows per period, near z and near z + c(e). The two cores per period are the p-independent sequences emb₁(λ^jζ_{A,B}), with ζ_A = eε^{−(k mod 2)}/(4√2), up to O(\|e\|λ^{−k}). | [P]; checked exactly |
| 4 | **Reduction of gap (a).** Ẑ_x/Z_ρ → w(z, e, k mod 2), a p-independent limit (Prop X′). Gap (a) = (A1) a p-independent series over depth classes + (A2) deep points. | [P-sketch] (Prop X′) + [N] |
| 5 | **Numerics for (a)** (p = 29, 47, both bases): values are p-independent to 4–5 digits. Non-family part relative to Re w_fam: near-0 family (base 0, e = 2√2) 0.0889 in modulus, with Re > 0; remaining base-0 classes up to N ≤ 600: 2.6e-3; base-¼ classes up to N ≤ 600: 1.6e-3; sampled shells N ≥ 2^10 up to 2^27: about 8.5e-5 in total, decaying. Total ≈ 9.5% ≪ 1 − 2δ. | [N] |
| 6 | **Not closed:** (A1) convergence of the series with a certified bound, and (A2) deep points. The precise lemma needed is stated in §4.3. A sup-norm bound provably fails (§4.4); an averaged (Theorem C type) bound is needed. | open |
| 7 | **F6.** h_rho16 run (growth 1.6154). W/W⁺ dropped (it removes nothing), so no threshold p₁. **F7:** mixed iso/unit classes at composite h_p are assigned to (b′). The Monte Carlo *absolute* majorant is 15% ± 10% (A) and 2% (B) of the family term at p = 11, but only 0.23% and 0.32% at p = 13. The distribution is heavy-tailed (§5). | [N] / bookkeeping |
| 8 | **o_levels p = 7.** d = 1673: inherited 0.010724 + 0.005761i (positive), level-7 2.10e-4 + 2.97e-4i, mixed −2.1e-5 + 1.43e-4i. | [N] |

**Status of Theorem R♯.** W′_{3p} ≥ −4m + δF_m/φ → ∞ for p ≥ 1165 holds modulo:
- Ω♯ restricted to ρ = (±2,8): gaps (a), (b) and (b′);
- the [P-sketch] parts of Prop X (other-sector absorption and the η derivation);
- the [CA] inputs n_cert and TRACE-199/213.

The (±2,16) part and the pattern lemma are no longer hypotheses.

## 1. (±2,16) at all levels [CA + P]
- **Certificate** (`code/a_dom16.py`). J3's `certG_build16.py` rebuilds the operator deterministically (V, K0 = 3, ρ = 1.2, K = 40, β = 2.5; dim 560). J3's `rig_spec.py` is then run in 'dom' mode: Householder deflation, contours \|z − b11\| = r1 and \|z\| = R, float BLAS with a-priori γ bounds, scalars in arb.
  - This was done for the 8 untwisted V factors whose J3 rest certificate was only R = 1.6677: reps 0, 2, 9, 12, 16, 21, 24, 27.
  - All 8 certify with r1 = 0.02 and R = 0.95: \|b11\| = 1.6154129681, so \|μ\| ∈ [1.59541, 1.63542], F_R1 ≤ 6.11e-7, F_R2 ≤ 1.58e-7.
  - Logs: `logs/dom16_V_r*.json`.
- **Explicit bound** (`code/d_Z16.py`).
  - Cauchy on two contours gives ‖T^{m−1}‖ ≤ r1(\|b11\|+r1)^{m−1}·fullR₁/(1−F₁) + R^m·fullR₂/(1−F₂).
  - \|tr_J T^m\| ≤ ½‖T‖₁‖T^{m−1}‖.
  - J3 read-out Z = (1−λ^{−m})Σ_{8 blocks}[tr_J V^m − tr_J E^m] (TRACE-226 L16). Every other factor keeps its J3 rest certificate (R ≤ 0.9298).
  - Result: **\|Z_(±2,16)(m)\| ≤ C₁₆·1.6355^m, C₁₆ = 2.273e5**, for all 16 cases.
- **Consequences:**
  - (i) Σ_ρ\|Z_ρ\|² ≤ 4\|Z₈\|² for m ≥ 51, against TRACE-199's \|Z₈\| ≥ ½(1−λ^{−m})(1.9154712^m − 3012.3). This is the N6-F6 threshold.
  - (ii) **Theorem 16.** For ρ = (±2,16), Dev_d(ρ) ≥ −n_d\|Z_ρ\|²/d² at every level [P, N6 §1]. Summing over all d ∣ h_m:
    Σ_{ρ=(±2,16)} Σ_d Dev_d(ρ) ≥ −2C₁₆²·1.6355^{2m}·(e^γ ln ln h_m + 0.6483/ln ln h_m) (Robin 1984: σ(n)/n bound, n ≥ 3).
    This is ≤ 0.01·F_m, with F_m ≥ 2.06e-3·p\|Z₈\|²/h_p (worst-case composite weight, REPORT_N6_v2 F5), for every p ≥ 339. Checked in arb for 339 ≤ p ≤ 537; beyond that the ratio decreases like (1.6355²λ^{1/6}/μ*²)^m·poly(m) = 0.9780^m·poly(m).
  - The (±2,16) members therefore drop out of Ω♯ completely. The per-level targets 1.6399 (N6-F4) are no longer needed.
- **Numerics** (`logs/h_rho16.out`): \|Z₁₆\| = 665, 1.18e4, 3.74e6, 3.73e11 at m = 15, 21, 33, 57, which is growth 1.6154 per step and matches \|b11\|. The (2,16) family ratio at p = 19 is −1.45e-4 − 6.14e-4i (Re < 0), but it is covered by Theorem 16.

## 2. Exact orbit lemmas [P]
**Notation.**
- p = 2k + 1, q = h_p = x_p, ε = 1 + √2, ε′ = 1 − √2 = −1/ε.
- γ := x_{k+1} + y_k√2 = (ε^{k+1} − ε′^k)/√2.
- N(γ) = γγ̄ = −½[ε^{k+1}ε′^{k+1} − ε^{2k+1} − ε′^{2k+1} + ε^kε′^k] = q, using εε′ = −1 and ε^p + ε′^p = 2q.
- 2q = ε^p − ε^{−p}, since ε′^p = −ε^{−p}.

**Identity (I) [P].** For every e ∈ O and i ∈ Z:
  λ^i·eγ/(8q) = eε^{2i−k}/(4√2) + e·[ε^{2i−3k−1} − (−1)^kε^{2i−k}]/(8√2 q).
*Proof.* λ^ieγ = e(ε^{2i+k+1} − ε^{2i}ε′^k)/√2. Then ε^{2i+k+1} = ε^{2i−k}ε^p = ε^{2i−k}(2q + ε^{−p}), and ε^{2i}ε′^k = (−1)^kε^{2i−k}. Divide by 8q. ∎
- The first term c_i := eε^{2i−k}/(4√2) lies in (1/(4√2))O = ½O^∨ (O^∨ = (√2/4)O).
- Since λ ≡ 1 mod 2O, c_i ≡ c_0 mod O^∨ for all i, and Tr(c_i) ∈ ½Z is constant mod 1.

**Lemma P′ [P].**
- (i) Every point of the isotropic line ((1/q)𝔮 + O^∨)/O^∨, where 𝔮 = (γ), has the form x = z + eγ/(8q) for each of the 8 λ-fixed points z ∈ (1/8)O/O^∨, with some e ∈ O.
  - Proof: an isotropic point is x = γa/q with a ∈ O. Since q = γγ̄, x − z = γ(8a − 8zγ̄)/(8q), so take e = 8a − 8zγ̄ ∈ O (8z ∈ O).
  - The conjugate line uses γ̄.
- (ii) With W1_i := λ^ieγ/(8q) and W2_i := W1_i − c_i, the twist satisfies τ_i ≡ Tr(z) + Tr(W1_i) ≡ Tr(z) + Tr(c_0) + Tr(W2_i) (mod 1) for every i.
- (iii) Embeddings, with e = (e₁, e₂), relative errors ≤ 2ε^{−2p}:
  - emb₁W1_i = e₁ε^{2i−k}/(4√2)·(1 + O(ε^{−2p})) − (−1)^ke₁ε^{2i−3k−1}/(8√2q)·…;
  - emb₂W1_i = e₂ε^{−2i−k−1}/(4√2)·(1 + O(ε^{−2k}));
  - emb₁W2_i = −(−1)^k e₁ε^{2i−3k−1}/(4√2)·(1 + O(ε^{−2k}));
  - emb₂W2_i = (−1)^k e₂ε^{k−2i}/(4√2)·(1 + O(ε^{−2k})).
  
  Hence there are two windows per period:
  - window 1 = {i : \|e₁\|ε^{2i−k}, \|e₂\|ε^{−2i−k−1} ≤ θ}, near z;
  - window 2 = {i : \|e₁\|ε^{2i−3k−1}, \|e₂\|ε^{k−2i} ≤ θ}, near z + c_0.
  
  Each has length k ∓ O(1) − ½log_ε(\|e₁e₂\|/θ²) = k − log_λ\|N(e)\| + O(1).
- (iv) **Cores.** At i = ⌊k/2⌋ + j, the deviation τ_i − Tr(z) ≡ emb₁(λ^jζ_A) (mod 1), with ζ_A := eε^{−(k mod 2)}/(4√2), up to O(\|e\|λ^{−k+\|j\|}).
  - For j ≥ 0 the same value is ≡ −emb₂(λ^jζ_A) + Tr(c_0), which decays.
  - The core at i = ⌊(3k+1)/2⌋ + j is the analogue with ζ_B = −(−1)^k eε^{2⌊(3k+1)/2⌋−3k−1}/(4√2).
  - Both are **p-independent** apart from k mod 2. ∎
- **Lemma P** is the case z = ¼, e = 2. Here ζ_A ∈ {1/(2√2), ε^{−1}/(2√2)} = {b, a}, which reproduces the N5 pattern exactly; one A core and one B core per period, spaced (p ∓ 1)/2 apart.
- **Exact checks:**
  - `code/b_pattern.py`: closed forms against exact integer twists mod 1, error ≤ 1e-167 (p ≤ 59) and 5e-390 (p = 163, 400 digits); slow count p − 5.
  - `code/g_patgen.py`: identity (ii) holds with error 0 at 600 digits, for e ∈ {2, −2−4√2, −6, −2+6√2, −10−2√2, 2√2, −4−2√2, 6√2} and p = 19, 29, 47, 59. The core formula (iv) has error 9e-6 (p = 19), 6e-10 (29), 1.7e-16 (47) and 4e-21 (59), i.e. ∝ \|e\|λ^{−k}.

## 3. Prop X′ (the p-independent limit) [P-sketch]
- For fixed (z, e) and p → ∞, the twist sequence consists of six windows of length k − log_λ\|N(e)\| + O(1) near fixed points with twist values in {0, ¼, ½, ¾}, and six cores given by Lemma P′(iv).
- The proof of Prop X goes through verbatim:
  - rank-one collapse on windows, by the sector gap at twists 0 and ½ (Line F; complement 0.769);
  - exact core products;
  - contamination by Lemma P′(iii).
- Result: **Ẑ_x/Z_ρ = w(z, e, k mod 2) + O_e(λ^{−c·p})**, with w = σ_z·(r_A(ζ_A)·r_B(ζ_B))³, where σ_z = ±1 is the sector sign.
- For the family, w = w* (N6 [CA]). For other e the constants depend on the core length ~ log_λ\|N(e)\|. Making them uniform in e is exactly what (A1)/(A2) need.
- [N] p-independence (`code/e_isodepth*.py`, `logs/e_isodepth*_p29*`, `*_p47*`): for every class with N(α) ≤ 60, p = 29 and p = 47 agree to 4–5 digits. α, εα and −α give identical values, which is an extra ε-symmetry [N]. Examples:

| base, α | N(α) | w (p = 29) | w (p = 47) |
|---|---|---|---|
| ¼, 1 (family) | 1 | 3.4358e-4 + 1.9580e-4i | 3.4358e-4 + 1.9580e-4i |
| 0, 1 (near-0 family, e = 2√2) | 1 | 2.9866e-5 − 6.599e-6i | same |
| ¼, −1∓2√2 | 7 | 1.766e-8 + 1.043e-8i | 1.7660e-8 + 1.0427e-8i |
| ¼, −3 | 9 | 9.002e-8 − 2.078e-7i | 9.0018e-8 − 2.0784e-7i |
| 0, −1∓2√2 | 7 | 1.160e-7 + 2.80e-8i | – |

## 4. Gap (a): reduction, numerics, and what is missing
### 4.1 Reduction [P mod Prop X′]
- At q = h_p, the isotropic sum in Lin_{h_p} is (2n/q²)·Re(Z̄ Σ_{x iso≠0} Ẑ_x).
- Classify each x by a representation (z, e) of minimal depth \|N(e)\| (Lemma P′(i)).
- Fix D_p := λ^{p/4}. Then:
  - (A1) **shallow** points (depth ≤ D_p) contribute Σ_{(z,e)≠fam} mult·[w(z, e, k mod 2) + O_e(λ^{−cp})];
  - (A2) **deep** points (depth > D_p) are the rest.
- Here mult = 2p per line (the λ-orbit, with α ~ εα ~ −α [N]).
- The **family**, (¼, 2), is the driver F_m.
- Gap (a) is closed once Σ_{(A1)∖fam}\|·\| + Σ_{(A2)}\|·\| ≤ (1−2δ)·4p·Re w*_lo.

### 4.2 Numerics [N]
`logs/h_series_partial.out`, `logs/i_shells_p47.out`; p = 47. Values are relative to Re w_fam = 3.4358e-4, and the multiplicity is the same for every class.
- **Base 0:**
  - near-0 family \|w\| = 3.055e-5 (0.0889), Re > 0;
  - all other base-0 classes with N ≤ 600: Σ\|w\| ≈ 8.7e-7 (0.0025).
- **Base ¼:**
  - all non-family classes with N ≤ 600 (exact enumeration): Σ\|w\| = 5.57e-7 (0.0016);
  - sampled shells N ∈ [2^j, 2^{j+1}), j = 4 … 26, 40 random classes per shell (Haar-uniform in the unit fundamental domain), class count 0.234·2^j (exact count for j ≤ 14). Table: `logs/i_shells_p47_table.out`.
    - j ≤ 9: ≤ 2.4e-4 per shell, consistent with exact enumeration;
    - j = 10, 11: 5.7e-7, 7.9e-8;
    - j = 12: 8.4e-5, caused by one outlier class at 1.1e-9;
    - j = 13 … 16: ≤ 3.3e-7;
    - j = 17 … 26: ≤ 1.1e-8, decaying to 2e-15 at j = 26.
    - Total over j ≥ 10: ≈ 8.5e-5.
  - The per-class distribution is **heavy-tailed**: max/mean is up to 37 per shell, with isolated classes far above the shell mean, so the sampling is indicative only. The trend is clear decay beyond N ~ 2^12, roughly like N^{−1.3} or faster.
- **Total** non-family: ≈ 0.09 + 0.005 ≈ **9.5%** of Re w_fam, with the dominant piece positive. This is consistent with N6 (X = 4p(w* + c₀) with < 0.6% residual) and the referee's ≈ 8% near-0 share.
- So, numerically, gap (a) holds with a margin of about 10× (1 − 2δ against 0.095).

### 4.3 The precise missing lemma
**Lemma A∞ (needed).** There are θ < 0.9 and p₂ such that for all p ≥ p₂:
  Σ_{x iso at h_p, x ∉ fam} \|Ẑ_x\| ≤ θ·4p·Re w*_lo·\|Z_ρ\|,
and the same at the inherited levels e·h_p ≤ L*.
- The inherited levels follow from the level-h_p statement by TRACE-228 inheritance: the same Ẑ, positive weights.

A sufficient split:
- **(A1′) [CA] for finitely many classes plus a uniform tail.** For depth ≤ K₀, certify w(z, e) as n_cert did for w*. The near-0 family needs only \|w\| ≤ 3.1e-5 or Re w ≥ 0, so the same machinery with base-0 cores applies. Then show Σ_{K₀ < N(e) ≤ D_p}\|w(z,e)\| ≤ θ′·Re w*.
- **(A2′) deep-point bound.** Σ_{depth > D_p}\|Ẑ_x\| ≤ θ″·p·\|Z_ρ\|.

### 4.4 Why a sup-norm bound cannot work [P], and the averaged route [H]
- With only sup-norms on the cores, \|Ẑ_x\|/\|Z_ρ\| ≤ C^6·(Λ^{8V}/μ*)^{6ℓ}, where ℓ ≈ log_λ N(e).
- (Λ^{8V}/μ*)^{6/ln λ} = N(e)^{+0.088} grows, while the class count per shell grows like 0.234·N.
- So Σ_shell ≥ N^{1.088}·…: it diverges, and the deep part reaches ~q^{1.09}/q ≫ p. This is the index-loss barrier again.
- **Averaged route** (the referee's suggestion, made concrete).
  - Use the op·HS·HS trick of Theorem C on one period: \|Tr Q³\| ≤ ‖Q‖_op‖Q‖²_HS, with Q the product over one period.
  - Average ‖Q‖²_HS over a depth shell. By Lemma P′(iv), the cores are orbit segments emb₁(λ^jζ) of the lattice points ζ ∈ (1/(4√2))O in a box of area ~N. These are Bowen-equidistributed at scale log_λ N, which is exactly the setting of Theorem C's collision count.
  - Convergence needs the HS² growth rate h₂ of the cores to satisfy Λh₂/μ*³ < λ^{−1/2}, i.e. **h₂ < 1.481 per step**. Theorem C's collision automaton gives r₂ ≈ 1.053 for the full torus, so the margin looks large [H].
  - The missing piece is a *box-restricted* version of Theorem C's Bowen-ball step: the shell is not T-invariant. Its error must be controlled uniformly in N.
  - Not done in N7.

## 5. F7: mixed iso/unit classes at composite h_p [N, Monte Carlo]
- **Method** (`code/f_mixed.py`): d = h_p = q₁q₂.
  - Class A: β isotropic-or-0 mod q₁, unit mod q₂. Class B: the reverse.
  - The **absolute** majorant S = Σ_class\|κ_d\|·\|Ẑ_β\|/\|Z_ρ\| is used, with \|κ_q\| = q − 2 on the isotropic component and ≤ 2 on the unit component. It is compared with the family term 4p·n_d·Re w_fam in the same normalisation.
- **p = 11** (h = 23·353, m = 33, 3000 samples per class):
  - S_A/fam = **0.149 ± 0.098**; the estimate is dominated by rare large samples, with max \|Ẑ\|/\|Z\| = 1.4e-4;
  - S_B/fam = 0.022 ± 0.006.
  - So at small p the mixed classes are **not** negligible in absolute value. This is an upper estimate; signs were not used.
- **Heuristic scaling [H].** Mixed points have only O(log_λ q₁)-length slow windows, so S/fam ~ h_p·E\|Ẑ\|/(p\|Z\|) ~ (1.274·λ^{1/6}/μ*)^m = 0.892^m. That is small for p ≳ 40, but it is not proved.
- **p = 13** (h = 79·599, m = 39, 2000 samples per class): S_A/fam = **0.0023 ± 0.0007**, S_B/fam = 0.0032 ± 0.0011, with max \|Ẑ\|/\|Z\| ≈ 1.4e-7.
  - So the p = 11 value is driven by rare, near-slow samples (heavy tail). The p = 13 value fits the predicted decay.
- These classes are assigned to (b′) in REPORT_N6_v2. Note: the N5 referee's "mixed classes ≤ 4.4e-12 relative" figure must concern a different class set. Its scope should be re-checked against this run.

## 6. Other items
- **o_levels p = 7** (`logs/o_levels_p7.json`): levels with h_p ∣ d are 239 and 1673. At d = 1673, the CRT split is:
  - inherited (β₇ = 0): 0.010724 + 0.005761i, equal to X at h_p and positive;
  - level-7 isotropic: 2.10e-4 + 2.97e-4i;
  - mixed: −2.1e-5 + 1.43e-4i, 1.3% of inherited in modulus.
  
  p = 7 is atypical, since 7² ∣ h_21. p = 11 and 13 were not run, because the CRT orbit count (~2e5) is too large without orbit reduction.
- **Pattern lemma upgrade.** Done: Lemma P [P]. The remaining [P-sketch] parts of Prop X are other-sector absorption and the uniform η constants (N6-F1).

## 7. Ledger
- **[P]:**
  - Identity (I) and Lemma P / P′;
  - Theorem 16 as an implication from C₁₆;
  - the reduction of (a) to A∞ (mod Prop X′);
  - the sup-norm barrier (§4.4).
- **[CA]:**
  - dom16 certificates (8 factors);
  - C₁₆ = 2.273e5 at rate 1.6355;
  - m₁ = 51 and p₁₆ = 339 (arb).
  
  Float BLAS with a-priori γ bounds, as in J3/Line F.
- **[P-sketch]:** Prop X′ (p-independent limit w(z, e)).
- **[N]:**
  - p-independence;
  - shell sums;
  - the ε-symmetry;
  - h_rho16;
  - o_levels p = 7;
  - mixed-class Monte Carlo.
- **Open:**
  - **gap (a)** = Lemma A∞, either (A1′) certified small depths plus a uniform tail, or (A2′) deep points;
  - **gap (b)/(b′)** (N7b).

**What is now proved, overall.** Frozen R′ fails along m = 3p (p ≥ 1165) modulo:
- (a) one inequality at the single level h_p, with a ~10× numerical margin;
- (b)/(b′), for ρ = (±2,8) only;
- the P-sketch parts of Prop X.
