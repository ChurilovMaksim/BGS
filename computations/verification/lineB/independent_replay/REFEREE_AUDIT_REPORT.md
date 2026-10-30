# Referee report: BGS derandomization, Line B, phases 2 and 3 (and the phase-1 fix check)

Referee: independent audit, 2026-10-29 (Europe/Berlin). Audited: /workspace/bgs-derand/{REPORT.md, phase2/REPORT2.md, phase3/REPORT3.md} with their code/, logs/ and lean/. Nothing was pushed and nothing was written outside /workspace/audit/derand23 and /home/box/audit_derand23_backup.

All my code is in /workspace/audit/derand23/code. I wrote it from scratch from the *definitions* (phase-1 Theorem 3 / Prop R): Smith normal form of H via PARI, the Fourier transform on V, and a CRT split. None of the project's `Orbits`, `fast_classes`, `p2lib` or transfer code is used. The only shared input is the 14 exact rational coefficients c_k of the l = 0 kick row. I used my own venv (numpy, scipy, sympy, mpmath, cypari2 2.2.x / PARI 2.17.2, gmpy2). Logs are in /workspace/audit/derand23/logs, and a tarball backup is in /home/box/audit_derand23_backup/.

## 0. Verdict table

| # | Claim | Verdict | Evidence (own) |
|---|---|---|---|
| P1 | Phase-1 fix list (12 items, marked [ref-fix]) | **APPLIED** (2 small residual wording issues, F1–F2) | §1 |
| A | Prop K (Ramanujan kernel) | **CORRECT** | t1: h²K = μ(q)/φ(q) to ≤ 1.8e-15 for all units, m = 3, 5, 7, 9 (composite h₉ = 7·199 gives the values −1/6, −1/198, 1/1188, 1) |
| B | Lemma S + Addendum (𝒮 = ½·𝟙 + V^_odd), Lemma F, Theorem D | **CORRECT** | Support identical for every sampled ν, m ≤ 9. Deficits 1, 59, 1009, 11675, 112913, **982299 (m = 11, new)** equal the closed form. Lean `audit_thmD_m11` |
| C3 | Symbol structure | **CORRECT-WITH-FIXES** (sign typo) | Lean `shifted_real_parts` |
| N | Theorem N: \|B_m − B^sym_m\| ≤ 8m²N_m/h_m for NSW-prime m | **CORRECT-WITH-FIXES** (hypotheses (a), (b) are *automatic*; "B_m → 2m" overstated) | t4: all 11 m pass (a), (b), h > 28m, ord λ = m. The bound log₁₀ values reproduce to 0.01 |
| Cert | ECPP certificates m = 59 … 1493 | **CORRECT** (all 7 verified twice) | a1: my own Atkin–Morain checker plus PARI `primecertisvalid`. A tampered control is rejected |
| C5 | ND^(2) for m = 2, 3, 5, 7 | **CORRECT-WITH-FIXES** (label "exact" → high-precision float) | t8: m = 3, 5 at 60 digits, minimal pair-sum gaps 1.7e-3 and 5.8e-9 |
| G | Theorem G (moment CLT, conditional) | **CORRECT-WITH-FIXES** (conditional; ND must also cover unequal-length relations; "unconditional for verified k" is meaningless for a limit) | t7: M4/B² = 1.873843, 1.993972, 1.999754 reproduced |
| D2 | Phase-2 "Reduction [P]" (Δ_m, κ^{(m−1)/2}) | **UNSUPPORTED as [P]** → [S]; superseded by phase 3 | κ(25) = 6.0e-3 and κ(100) = 1.7e-3 reproduced (t5) |
| U | Theorem U (window m ≤ (1−ε)c(η)log X) | **CORRECT-WITH-FIXES**: the error estimate is right. The *interpretation* ("derandomized ramp", "B_m/2m → 1 throughout it") is **WRONG** | t5: s0 and c(η) reproduced. Phase 3's own data show F_m(η) ≈ 2m(1+χ_m) ≠ 2m in that window |
| C | Prop C (exact Ramanujan-class formula for F_m(η)) | **CORRECT** (the gap for p² \| h closes, see §3.1) | t2: matches a full-G FFT computation without the split to ≤ 1e-11, m = 3, 5, 7, 9 |
| C′ | "Self-duality" Kloosterman orthogonality | **CORRECT-WITH-FIXES** (only for s, s′ ≠ 0, h prime) | t6: dev ≤ 1.5e-11 for s, s′ ≠ 0; fails in the s = 0 row |
| W | Parity split F = B^sym + 2mχ + W^rest + E, \|E\| ≤ 4m²/h | **CORRECT-WITH-FIXES**: the identity holds, but every tabulated "W^rest" is actually W^rest + E | t2, m = 3–11: \|E\| = 3.4, 1.8, 0.61, 0.17, 0.045 against bounds 5.1, 2.4, 0.82, 0.23, 0.060 |
| T | Theorem T: χ_m = Σ(−1)^a Tr M_a^m | **CORRECT** (identity), with a tail-bound fix and a validation-claim fix | t3 vs t2: agreement ≤ 1e-6 for η ≤ 50. Spectrum table reproduced to all digits |
| μ | μ(η) ≈ exp(−2‖f_odd‖²η²), 800²‖f_odd‖² = 60 | **CORRECT** as a small-η law (−log μ/η² = 1.8750e-4 at η = 0.1). It holds within 0.04% at η = 10 and 1.2% at η = 25, and fails for η ≥ 50 | t3 |
| χ→0 | "2mχ_m = o(m), exponentially, at every fixed η ≠ 0" | **UNSUPPORTED as a theorem** ([N] only; upgradable, §3.4) | |
| m_* | 4m → 2m crossover at m_* ≈ 5333/η² | **CORRECT-WITH-FIXES** (only for η ≲ 25; the Ehrenfest-window comparison and the Keating–Mezzadri attribution are wrong) | t3, t2 |
| R | Conjecture R ("quadratic large sieve") | Honestly labelled [C]. The **"equivalent to a large-sieve statement" framing is UNSUPPORTED**. Not known, not refuted | §3.6 |
| CLT | Fixed-η CLT numerics | **CORRECT** (reproduced exactly) with a disclosure fix: small η is strongly non-Gaussian | t2: m = 11, η ≥ 10: M4 1.936–2.004, KS 0.0062–0.0134. η = 2: M4 = 1556 |
| L | Lean files (phase 1/2/3) | **CORRECT** (build clean in my copy; finite instances only) | 41 theorems: 33 axiom-free, 7 [propext], 1 [propext, Quot.sound]; no sorry or native_decide |

## 1. Phase-1 fix check

I checked all 12 items of /workspace/audit/derand/REPORT.md §6 against the current REPORT.md.
- Items 1–8 and 10–12 are applied verbatim or equivalently.
- Item 9 is applied with a small overstatement (F1).
- F1 (§8). "δ_m is certified by exact class computation for m ≤ 8 (referee)" → replace with: "The *distinctness* of the S-classes (δ_m > 0) is certified exactly for m ≤ 8 by the referee's cyclotomic class computation. The numerical value of δ_m is a float with error ~1e-14 ≪ δ_m."
- F2 (§0 item 3). "proved for the admissible NSW-prime m in phase 2, Theorem N" → replace with: "bounded unconditionally by phase-2 Theorem N for NSW-prime m. The bound 8m²N_m/h_m is < 1 only from m = 29 on. B_7 = B_7^sym holds by the exact ND check."
- Cosmetic. Phase 2 says "Phase-1 REPORT.md is frozen", but it was edited (the [ref-fix] items). Say "frozen except for the [ref-fix] items".

## 2. Phase 2

### 2.1 Prop K, Lemma S, Addendum, Lemma F, Theorem D: correct
I re-derived Prop K line by line. The cocycle step uses νν̄² ≡ ν̄ and the quadratic homogeneity of 𝒬, and the representative-independence argument gives t ∈ (1/g′)Z. Both are fine.

The Addendum argument is correct and clean: H𝟙 = 4𝟙, 𝒬(𝟙) = m/2, and mθ ≡ ½ gives θ = ½.

Numerically (t1_structure.log), from raw Fourier sums on the SNF coordinates of G, for m = 3, 5, 7, 9:
- supp k_ν = {ξ : hξ_j ≡ ½} for every sampled ν;
- |k|² = 1/h²;
- k_ν(−ξ) = k_ν(ξ);
- a reflection fixes exactly h_m support points;
- the direct deficits equal Theorem D.

For m = 11 the direct deficit (982299) equals the closed form; this is also Lean-checked in my file lean/AuditDerand23.lean.

### 2.2 Theorem N: correct, and stronger than stated
I re-derived (i)–(iii).
- (i) Q(i) and Q(ζ_h) are linearly disjoint, so a vanishing combination of fewer than h of the ζ_h^P must vanish identically.
- (iii) The real-part separation is 0.45 > 0.40, because each k has at most 2 hits. The multiset {±7x_j} determines {±x_j}, which gives ≤ 4m² partners.
- (ii) G1 and G2 are lines Tr(yx) = 0, since the trace form is nondegenerate for h ∤ 32. G2 forces π ∈ D_m.
- The final count 2N_m h·4m²/h² is right.

**New observation (should be added).** Hypotheses (a) and (b) hold automatically for every odd m with h = h_m prime and h > 18. Hence "admissible" can be deleted.
- (a) Suppose λ^d ≡ r ∈ F_h. Apply the nontrivial automorphism σ of O/h: Frobenius in the inert case, the swap of components in the split case. It sends λ to λ⁻¹, so r² ≡ λ^dλ^{−d} = 1 and λ^d ≡ ±1. Now ord_h(λ) = m is odd, so λ^d ≡ −1 is impossible. Hence λ^d ≡ 1 = k′/k, i.e. k ≡ k′, which is excluded by |k − k′| ≤ 18 < h.
  - ord_h(λ) = m holds because h | λ^d − 1 with d | m, d < m would force h_m² | D_d = 4h_d² < h_m².
- (b) Suppose u + v = 6 with u = λ^a, v = λ^b. Applying σ gives u⁻¹ + v⁻¹ = 6, so uv = 1. Then u and v are the two roots of t² − 6t + 1, i.e. {u, v} = {λ, λ⁻¹}, so {a, b} ≡ {1, −1}. If a = b, then u² = 1 and 2u = 6, so 9 ≡ 1, which is impossible.

My computation (t4_thmN.log) confirms (a) and (b) for all 11 m, consistent with this argument.

**Overstatements to fix.**
- "B_m → 2m for NSW-prime m" is a statement about a sequence. It is known only for the finitely many known NSW primes; infinitude is open, like Mersenne primes.
- The bound is nontrivial only for m ≥ 29: 10^{3.91} at m = 7 and 10^{1.08} = 12 at m = 19.
- The result concerns the η-**Bohr mean** B_m, not F_m(η) at fixed η.
- N_m ~ m³/2, so the error term is O(m⁵/h_m). "O(m⁶/h_m)" is a valid but loose upper bound.

### 2.3 ECPP certificates [Cert]: verified
logs/a1_ecpp_verify.log. For each m ∈ {59, 163, 257, 421, 937, 947, 1493} I checked:
- h_m recomputed directly as √(Tr S^m − 2)/2;
- the certificate's first N equals h_m;
- every step with my own pure-Python Atkin–Morain/Goldwasser–Kilian checker:
  - gcd(N, 6) = 1 and gcd(4a³ + 27b², N) = 1;
  - q = (N + 1 − t)/s with q > (N^{1/4} + 1)², tested by an exact integer inequality;
  - [s]P ≠ O computed affinely with honest unit checks, and [q][s]P = O;
  - the chain is consistent;
  - the last q (≤ 1.1·10¹⁹) is proved prime by deterministic Miller–Rabin (valid below 3.3·10²⁴).

All seven are VALID under my checker, under PARI `primecertisvalid`, and under gmpy2 BPSW. A certificate with one tampered coordinate is rejected. m ≤ 47 is deterministic (h₄₇ has 18 digits). So Theorem N is unconditional for all eleven listed m. The certificates are not Lean-checked, which is stated honestly.

### 2.4 C3 / C5 / Theorem G
- **C3 typo.** "c̃_k = (360,0) for k = ±7" → "c̃_{±7} = (−360, 0) (over 800)". The Lean `shifted_real_parts` already says −360.
- **C5.** "[N, exact]" → "[N, 40-digit mpmath; not a cyclotomic proof]". My independent 60-digit check (t8) confirms ND^(2) at m = 3 and 5.
- **Theorem G.**
  - The algebra M_2 = 2B² − Σw_o² is right; I reproduced 1.873843, 1.993972 and 1.999754.
  - Under ND the ν-average is irrelevant: |κ_o|² = |o|²/D_eff is ν-independent.
  - Convergence of *mixed* moments E Z^a Z̄^b (a ≠ b) to 0 needs ND for relations Σ_{i≤a} S(o_i) = Σ_{j≤b} S(o′_j) with a ≠ b as well. Add this to ND^(≤k).
  - "Unconditional for the k that are verified" only gives exact finite-m identities, not a CLT. Replace with: "the predicted moments are exact at m = 2, 3, 5, 7 (k = 2); the limit statement is conditional on ND^(≤k) for all large m."

### 2.5 D2 "Reduction [P]"
The claim "the Γ-diagonal equals 2m − Δ_m(η), reflections contribute ~κ^{(m−1)/2}" is stated without proof. It also uses a different diagonal than the ξ-side B^sym, which is exactly η-independent. Relabel it [S]/heuristic and point to phase-3 Theorem W, which replaces it.

### 2.6 Theorem U
The bound is right. From Theorem 1(c), ||Z^{(N)}|² − |Z(ν)|²| ≤ 2s0^m·πms2 s0^{m−1}/N. The incomplete-block term is ≤ (D/X)·max|Z|² ≤ (D/X)·min(s0^{2m}, D_eff). I reproduced s0 = 1.560, 2.104, 5.626, 16.96, 32.29 and c(η) = 0.377, 0.308, 0.192, 0.135, 0.115 (t5).

Fixes:
1. "odd N ≤ X" → "N ∈ (X, 2X] with gcd(N, D_m) = 1".
2. "c(η)·log λ ∈ (0.19, 0.66)" holds only for η ∈ [0.5, 100]. c(η) → 0 as η → ∞ (c·log λ = 0.174 at η = 400) and → 1/log λ as η → 0.
3. **Interpretation error.** Theorem U shows that the N-average equals F_m(η) uniformly in the window. It says nothing about F_m(η) being 2m. Phase 3 shows F_m(η) ≈ 2m(1 + χ_m(η)) + W^rest, so F ≈ 4m whenever m ≪ 5333/η². For η ≤ 5 that covers the whole window for any X ≤ 10^{1000}. Replace "So the derandomized ramp holds uniformly …" and "B_m/2m → 1 throughout it" with: "the N-average reproduces the ν-average F_m(η) uniformly for m ≤ (1−ε)c(η)log X. The value 2m is obtained only after the additional η-Bohr average (Theorems 4/5, N), or at fixed η for m ≫ m_*(η) under Conjecture R."
4. Optional improvement. Using min(s0^{2m}, D_eff), the window constant can be raised to min(1/(2log s0), max(c(η), 1/(2log λ))), e.g. 0.284 instead of 0.192 at η = 5.

## 3. Phase 3

### 3.1 Prop C: correct for all odd m (the proof gap closes)
Numerically, on the full group G with no CRT split and no Prop C, the ν-average of |Z|² equals my class computation to ≤ 1e-11 for m = 3–9. For m = 9 the kernel values on 400² random pairs are exactly μ(q)/φ(q) with q | 1393 = 7·199.

A proof valid for every odd m, including p² | h (replacing the "1-dimensional invariant forms mod p" step):
- V = V_2 ⊕ V_odd is 𝒬-orthogonal and ⟨·,·⟩-orthogonal, because cross terms have order dividing gcd(4, h) = 1. So k_ν(½𝟙 + x) = k^{(2)}_ν · k^{odd}_ν(x).
- k^{odd}_ν(x) = h⁻²Σ_{β∈V_odd} e(−ν𝒬(β) − ⟨β, x⟩) is a Gauss sum of a quadratic form that is *nondegenerate* on V_odd, since Rad = V[4]. Hence it equals (ε_ν/h)·e(ν̄𝒬^∨(x)), with 𝒬^∨ the dual (inverse) form mod h.
- So t = 𝒬^∨(ξ) − 𝒬^∨(ξ′). 𝒬^∨ is λ-invariant. Over Z/p^e the invariant binary forms form a free rank-1 module spanned by the norm form, because μ² − 1 is a unit (Nm(λ² − 1) = −32). Hence 𝒬^∨ = c·q/h with c a unit by nondegeneracy.

Change "checked only for m ≤ 13" to [P] for all odd m.

### 3.2 Self-duality remark (§1)
Σ_y e((A·Nm y + Tr y)/h) = h·e(−Ā/h) is confirmed with sign +1 at h = 41, 239, 1393.

The orthogonality Σ_r Kl_T(rs)·conj Kl_T(rs′) = h(h[s = s′] − 1) holds only for s, s′ ≠ 0 (and h prime). At s = 0 the left side is 0 or h|Kl(0)|², not the formula (t6). Add "s, s′ ∈ (Z/h)^×, h prime".

### 3.3 Lemma P and Theorem W
- The identity is right. In my code W^par is computed exactly from orbit data (stabilisers and the relation −ξ ∈ Γξ) on all h² points, and |E| = |W^par − 2mχ| respects 4m²/h for m = 3–11.
- Lemma P(iii), "≤ 2m·h bad points": for prime m this is exact. The union of m reflection lines and m anti-reflection lines, all through 0, has 2mh − (2m − 1) points; I observe 178597 at m = 11. For composite m, add the rotation-fixed points: ≤ 2mh + Σ_{d|m, d<m} φ(m/d)·h_d². The bound then reads |E| ≤ 4m²/h + 2m·Σ h_d²/h², a negligible change.
- Lemma P(ii): "λ^{2k} ≡ 1 so m | k" needs ord_h(λ) = m also for composite h. This is true (§2.2), but say so.
- **Mislabelled data.** In logs/W_decomp*.log and in the §4 table, "W^rest/2m" is computed as (F − B^sym − 2mχ)/2m = (W^rest + E)/2m, not W^rest/2m. With the true W^rest from exact W^par:

| η | m = 5 (theirs / true) | m = 7 | m = 9 | m = 11 |
|---|---|---|---|---|
| 5 | −0.39 / −0.21 | +0.16 / +0.20 | −0.07 / −0.06 | +0.15 / +0.15 |
| 10 | −0.07 / +0.10 | −0.11 / −0.07 | −0.02 / −0.01 | +0.016 / +0.018 |
| 25 | +0.02 / +0.16 | −0.09 / −0.06 | −0.04 / −0.03 | +0.005 / +0.006 |
| 50 | −0.01 / +0.11 | −0.04 / −0.007 | −0.03 / −0.025 | +0.009 / +0.010 |
| 400 | −0.36 / −0.26 | +0.02 / +0.05 | −0.05 / −0.04 | −0.018 / −0.016 |

  The fix is to define W̃^rest := F − B^sym − 2mχ_m (= W^rest + E) and state the decomposition as F = B^sym + 2mχ + W̃^rest. All tables then stay correct. Note that the m = 13 entry +0.0006 at η = 25 is below the resolution |E|/2m ≤ 5.4e-4.

### 3.4 Theorem T and the spectrum
- The derivation is correct. Poisson on the coset ½𝟙 + 4G, with annihilator HZ^m + Z𝟙 (index 4 over HZ^m), gives (−1)^{Σn} = (−1)^a for odd m and the nearest-neighbour transfer matrix.
- My own transfer code reproduces χ_m to ≤ 1e-6 for η ≤ 50 and m = 3–13. Their m = 13 values 0.78722, 0.25534 and 0.01781 match.
- The spectrum table is reproduced digit for digit: 0.999813, 0.999251, 0.995345, 0.98177, 0.90034, 0.73105, 0.61995, 0.5586; ρ₊ = 0.9998 … 1.25.

Fixes:
- Tail bound: "exact up to the tail Σ_{|n|>4K−3}|ŵ|" → "up to m·‖ŵ‖₁^{m−1}·Σ_{|n−a|>4K}|ŵ(n)|". The factor ‖ŵ‖₁^{m−1} ≥ 1 is missing.
- Validation claim: "agree to ≤ 7·10⁻⁵ for η ≤ 400" is false in their own log at η = 400. The transfer and direct values there are 0.33429 vs 0.34540 (m = 3), 0.01849 vs 0.02343 (m = 5) and 0.03875 vs 0.04256 (m = 7). Replace with "for η ≤ 200; at η = 400 the truncation K is insufficient (differences up to 1.1·10⁻²)".
- "Hence 2mχ_m = o(m), exponentially, at every fixed η ≠ 0" is [N]: the spectral radius of the *infinite* operator is not controlled.
  - Suggested upgrade (verification pending). M_a is the Fourier-side matrix of the twisted transfer operator of the linear Anosov map T with real-analytic weight e^{iηu}, restricted to the four characters of G/4G. By the Ruelle–Pollicott/dynamical-determinant theory for real-analytic hyperbolic maps (Rugh 1992; Fried; Faure–Roy, Nonlinearity 2006; Slipantschuk–Bandtlow–Just 2017), Tr M_a^m = Σ resonances^m. The leading resonance has modulus < 1 unless ηu is cohomologous to const + 2πZ-valued. That is excluded because the orbit sums of u have nondegenerate Gaussian fluctuations (σ² = 4‖f_odd‖² > 0).

### 3.5 Small-η law and crossover
- 800²‖f_odd‖² = Σ_k(800·Im c_k)² = 60 is confirmed (Lean `P2_odd_norm` and my own sum).
- −log μ(η)/η² = 1.8750e-4, 1.8746e-4, 1.8662e-4, 1.8403e-4, 1.680e-4, 1.253e-4 at η = 0.1, 1, 5, 10, 25, 50. So the law is excellent for η ≤ 10, 1% off at 25, and wrong for η ≥ 50 (0.626 vs 0.731).

Fixes:
1. "m_*(η) ≈ 5333/η²" → "for η ≲ 25; in general m_* = log 2/(−log μ(η)), e.g. 2.2 at η = 50".
2. "W_par/2m ≈ 0.85–0.99 for η ≤ 10 and m ≤ 11" → "χ_m ∈ [0.82, 0.995] for 2 ≤ η ≤ 10, m ≤ 11". The value at m = 11, η = 10 is 0.8167.
3. "far beyond the Ehrenfest-type windows of phase 2 for η ≲ 50" is wrong as stated: m_*(50) ≈ 2. The correct comparison is m_*(η) > c(η)·log X; for X = 10^{160} this holds for η ≲ 9.
4. **Attribution.** x ↦ −x is a *classical* symmetry (−I commutes with S and M_N is even), broken by f_odd. It is not a Keating–Mezzadri pseudo-symmetry, which is an arithmetical quantum symmetry with no classical limit. The 4m → 2m law with Gaussian damping exp(−½Var(ηΔS)) is the derandomized analogue of the semiclassical symmetry-breaking crossover of Bohigas–Giannoni–Ozorio de Almeida–Schmit, Nonlinearity 8 (1995) 203 (GOE–GUE; Pandey–Mehta 1983 for RMT). Replace "concrete instance of the Keating–Mezzadri pseudo-symmetry mechanism" with: "an exactly solvable instance of weak breaking of a classical (parity) symmetry, analogous to the semiclassical BGOS crossover; not a KM pseudo-symmetry".

### 3.6 Conjecture R and the "quadratic large sieve"
- The equivalence "W^rest = o(m) ⇔ ℓ²-collision statement for the pushforward of Ĝ under n ↦ 2nᵀH⁻¹n mod 1" is a restatement of Prop C (Parseval), not a reduction.
- Literature check. Known large sieves with quadratic structure are Baier–Zhao (square moduli, JNT 2008), the recent quadratic-polynomial moduli result (Acta Arith., doi 10.4064/aa240923-21-1) and Baier's quadratic amplitude. They sum over *many moduli* with one-variable amplitudes. Conjecture R has *one* modulus h, an m-variable form, m → ∞, and product weights. None of these results implies it.
- Neither is it ruled out: my true W^rest at η ≥ 10 trends to 0 (≤ 0.018·2m at m = 11).
- Structural caution. ord_h(λ) = m ≈ 2log h/log λ, so the h_m are exactly the *minimal-period* moduli. For those moduli Faure–Nonnenmacher–De Bièvre (2003) built scars, and Kurlberg–Rudnick (2001, needs ord > N^{1/2}) and Bourgain (2007, sum-product, needs ord > p^ε) do not apply. Bourgain–Glibichuk–Konyagin bounds need |⟨λ⟩| ≥ h^δ, so Bourgain-type methods are *structurally unavailable* here. Say so in §4.
- Formulation fixes:
  - (i) "admissible" is automatic (§2.2);
  - (ii) the NSW-prime version is a statement along a sequence not known to be infinite;
  - (iii) "after removing the classes with gcd(r, h) divisible by primes p ≤ 28m" must be made precise: which A_r are removed, and is the claim then about F or about a modified F?
  - Also state it for W̃^rest.

### 3.7 Fixed-η distribution
Reproduced exactly (t2_fixed_eta_9/11.log):

| m | η | M4 | M6 | \|EZ²\|/F | KS |
|---|---|---|---|---|---|
| 9 | 5 | 2.045 | 6.380 | 0.021 | 0.016 |
| 9 | 400 | 1.933 | 5.528 | 0.074 | 0.023 |
| 11 | 10–400 | 1.936–2.004 | 5.51–6.15 | ≤ 0.030 | 0.0062–0.0134 |
| 11 | 5 | 15.87 | — | — | — |
| 11 | 2 | 1556 | 3.8·10⁶ | 0.70 | 0.40 |

At m = 11, η = 2: F/2m = 5.5617.

Disclosure fix: at small η the law is far from Gaussian. M4 = 6.1 at (m, η) = (9, 2); M4 = 1556 and KS = 0.40 at (11, 2); KS = 0.040 > 0.0154 at (11, 0.5). Also, the "5% critical value" treats the φ(h) values of ν as i.i.d. samples, but they are a deterministic population, so it is only a yardstick. The remark "doubled variance … sectors independent in the limit" is heuristic; label it [H].

### 3.8 Lean
- I copied /workspace/bgs-build/formalization to /workspace/audit/derand23/build. `lake exe cache get` decompressed 8689 cached files; Mathlib was not built from source.
- `lake build Bgs.DerandChecks`, `Bgs.Phase2Checks` and `Bgs.Phase3Checks` all succeeded. The files are identical to the project copies.
- `#print axioms` over all 41 theorems (logs/lean_axioms.log) gives 33 with none, 7 with [propext] and 1 with [propext, Quot.sound]. There is no sorry, native_decide or ofReduceBool.
- The content is finite instances (P3_sum checks one vector per m; P5 is a 13×13 box, whereas the real statement is immediate from hyperbolicity). The labels say so.
- My additions (lean/AuditDerand23.lean): `audit_thmD_m11 : deficitNum 11 = 982299` and `audit_h11 : hm 11 = 8119 ∧ 8119 = 23*353`. Both are axiom-free.

## 4. Exact fix list (replacement wording)

1. REPORT.md §8: F1 above. §0 item 3: F2 above.
2. REPORT2 §C3: "c̃_k = (360,0) for k = ±7" → "c̃_{±7} = (−360, 0)".
3. REPORT2 §C4:
   - Delete "admissible". Add: "Lemma: for odd m with h_m prime and h_m > 18, (a) and (b) hold automatically (Frobenius/conjugation argument: λ^d ∈ F_h forces λ^d = ±1; λ^a + λ^b = λ + λ⁻¹ forces {λ^a, λ^b} = {λ, λ⁻¹})."
   - "B_m → 2m" → "for each NSW-prime m, |B_m − B^sym_m| ≤ 8m²N_m/h_m = O(m⁵/h_m). Nontrivial from m = 29. Whether infinitely many NSW primes exist is open."
4. REPORT2 §C5: "[N, exact]" → "[N, 40-digit floating point]".
5. REPORT2 §D1:
   - add to ND^(≤k): "including relations with unequal numbers of terms (needed for E Z^aZ̄^b → 0)";
   - "unconditional for the k that are verified" → "exact at the verified finite m; the limit is conditional".
6. REPORT2 §D2: "Reduction [P]" → "Reduction [S] (superseded by phase-3 Theorem W)".
7. REPORT2 §E (Theorem U):
   - "odd N ≤ X" → "N ∈ (X, 2X], gcd(N, D_m) = 1";
   - "(0.19, 0.66)" → "(0.20, 0.66) for η ∈ [0.5, 100]; → 0 as η → ∞";
   - replace "So the derandomized ramp holds uniformly …" and "B_m/2m → 1 throughout it …" with the sentence in §2.6(3).
8. REPORT3 §1 Prop C: replace the third proof bullet with the Gauss-sum argument of §3.1. Delete "checked only for m ≤ 13".
9. REPORT3 §1 self-duality: add "for s, s′ ∈ (Z/h)^×, h prime".
10. REPORT3 §2:
    - Lemma P(iii): "at most 2m·h" → "at most 2mh + Σ_{d|m,d<m} φ(m/d)h_d² (= 2mh − 2m + 1 for prime m)";
    - define W̃^rest := F − B^sym − 2mχ_m and say all tables report W̃^rest/2m;
    - optionally add the true W^rest column from §3.3.
11. REPORT3 §3:
    - the tail-bound wording of §3.4;
    - "≤ 7·10⁻⁵ for η ≤ 400" → "≤ 7·10⁻⁵ for η ≤ 200 (truncation insufficient at η = 400)";
    - "Hence 2mχ_m = o(m) … at every fixed η ≠ 0" → "numerically, for η ∈ [0.1, 400] (truncation K ≤ 20), |μ| < 1; a proof would follow from Ruelle–Pollicott theory for analytic Anosov maps (not written out)".
12. REPORT3 §3 corollary:
    - m_* scope and the Ehrenfest comparison (§3.5, items 1–3);
    - the Keating–Mezzadri sentence → the BGOS wording (§3.5, item 4).
13. REPORT3 §0 item 2: "W_par/2m ≈ 0.85–0.99 for η ≤ 10 and m ≤ 11" → "χ_m ∈ [0.82, 0.995] for 2 ≤ η ≤ 10, m ≤ 11".
14. REPORT3 §4(c) and Conjecture R:
    - "equivalent to a quadratic large-sieve statement" → "equivalent (by Parseval) to an ℓ²-collision bound for the pushforward measure; this is not covered by known large-sieve inequalities (Baier–Zhao and successors treat many moduli and one variable)";
    - add the minimal-period caution: h_m have ord λ = m ≈ 2 log h/log λ, the FNDB regime, where KR/Bourgain/BGK sum-product bounds do not apply;
    - make the torsion-removal clause precise.
15. REPORT3 §5: add the small-η outliers (m = 9, η = 2: M4 = 6.1; m = 11, η = 2: M4 = 1556; η = 0.5: KS above the yardstick). Mark the KS critical value as a heuristic yardstick and the doubled-variance remark as [H].
16. REPORT3 §9 literature: add BGOS 1995, Pandey–Mehta 1983, FNDB 2003, Kurlberg–Rudnick 2001, Bourgain 2007 (LNM 1910), BGK 2006, Faure–Roy 2006 and Rugh 1992. Keep Keating–Mezzadri only for the arithmetic-symmetry discussion.

## 5. Novelty assessment (honest)
- **Genuinely new and useful (for this model):**
  - Theorem N, with the strengthening that admissibility is automatic, plus the ECPP certificates. This gives a clean unconditional statement for the known NSW primes. The mechanism (prime-order vanishing sums plus symbol separation) is standard, but its combination with the q-sequence geometry is new.
  - Prop C (exact class formula) and the exact transfer-operator identity for χ_m (Theorem T) with the explicit rate 2‖f_odd‖² = 1.875·10⁻⁴.
- **Routine but correctly done:**
  - Prop K: the ν-average of quadratic Gauss-sum kernels gives Ramanujan sums.
  - Lemma S/Addendum and Lemma F/Theorem D: Möbius counting of palindromic orbits.
  - Theorem G: the standard moment method under a linear-independence hypothesis.
  - Theorem U: bookkeeping on Theorem 2.
- **Known physics, derandomized:** the parity crossover 4m → 2m with Gaussian damping exp(−m·2‖f_odd‖²η²) is the BGOS-type semiclassical symmetry-breaking law. The novelty is the exact, fixed-kick, non-random identity, not the phenomenon.
- **Not new / overstated:**
  - "quadratic large sieve" (a restatement);
  - "B_m → 2m" (a finite list);
  - "derandomized ramp uniformly in the window" (Theorem U gives F, not 2m);
  - the Keating–Mezzadri attribution.

## 6. What is integrable into the repo now

| Item | Suggested status |
|---|---|
| Prop K; Lemma S + Addendum; Lemma F; Theorem D (with Lean m ≤ 9 plus audit m = 11) | **proved** |
| p-splitting lemma C2; symbol facts C3 (sign fixed) | **proved** |
| Theorem N for m ∈ {7, 19, 29, 47, 59, 163, 257, 421, 937, 947, 1493}, with ECPP certificates (independently re-verified) | **proved** (state the bound; "nontrivial from m = 29") |
| "Admissibility is automatic" (§2.2) | **verification-pending** (short proof given here; authors should write it up) |
| Prop C for all odd m (Gauss-sum proof, §3.1) | **proved** for squarefree h as written; **verification-pending** for the general write-up |
| Theorem W identity (with W̃^rest relabelling and the Lemma P(iii) count fix); Theorem T identity | **proved** |
| μ(η) spectrum, small-η law, crossover m_*(η) | **numerical** (small-η law: proof-sketch) |
| Exponential decay of χ_m at fixed η | **open / verification-pending** (Ruelle–Pollicott route) |
| Theorem U (error estimate only, with the corrected interpretation) | **proved** |
| Theorem G | **conditional** (on ND^(≤k), including unequal-length relations) |
| ND^(2) at m = 2, 3, 5, 7 | **numerical** (high-precision float) |
| W̃^rest tables, fixed-η CLT numerics | **numerical** |
| Conjecture R; fixed-η CLT; ND for composite h / even m | **open** |

## 7. Reproduce
```
P=/workspace/audit/derand23/venv/bin/python; cd /workspace/audit/derand23
$P code/a1_ecpp_verify.py 59,163,257,421,937,947,1493     # ~40 s
$P code/t1_structure.py 3,5,7,9                           # m=9 ~25 min
$P code/t2_fixed_eta.py 3,5,7 2,5,10,25,50,100,400 full   # seconds
$P code/t2_fixed_eta.py 9 0.5,2,5,10,25,50,100,400 full   # ~30 s
$P code/t2_fixed_eta.py 11 0.5,2,5,10,25,50,100,200,400   # ~5 min, ~8 GB RAM
$P code/t3_transfer.py      # ~17 min
$P code/t4_thmN.py; $P code/t5_s0.py; $P code/t6_kloosterman.py; $P code/t7_thmG.py; $P code/t8_nd2.py
cd build && lake exe cache get && lake build Bgs.DerandChecks Bgs.Phase2Checks Bgs.Phase3Checks && lake env lean AuditAxioms.lean && lake env lean AuditDerand23.lean
```

---

## 8. Phase 4 audit (turn 2, 29 Oct 2026, Europe/Berlin)

Scope: /workspace/bgs-derand/phase4 (REPORT4.md, code, logs, lean/Phase4Checks.lean), plus the [ref23-fix] edits in REPORT.md, phase2/REPORT2.md and phase3/REPORT3.md. I read their files but did not modify them. All new numbers come from my own code: code/t9_cert.py, t10_lemmaV.py, t11_propL.py, t12_torsion.py; logs in logs/t9_*, t10_*, t11_*, t12_*.

### 8.1 Part 1: the 16 fixes

| # | Where | Applied? | Note |
|---|---|---|---|
| 1 | REPORT.md §8 (F1, δ_m distinctness), §0 item 3 (F2) | yes | lines 34 and 371 |
| 2 | REPORT2 C3 sign c̃_{±7} = (−360, 0) | yes | |
| 3 | REPORT2 C4: "admissible" deleted, automatic-admissibility Lemma, bound wording, "nontrivial from m = 29" | yes | minor: §H says "proved for the 11 listed m" while C4 says "every NSW-prime m". Suggested wording: "holds for every NSW-prime m with h > 28m; the 11 listed m are those with h_m certified prime" |
| 4 | REPORT2 C5 "[N, 40-digit floating point]" | yes | |
| 5 | REPORT2 D1: unequal-length relations; "conditional" limit | yes | |
| 6 | REPORT2 D2 → [S] | yes | |
| 7 | REPORT2 Theorem U: N ∈ (X, 2X], (0.20, 0.66), interpretation | yes | |
| 8 | REPORT3 Prop C Gauss-sum proof; "checked only for m ≤ 13" deleted | yes | line 49 |
| 9 | REPORT3 self-duality "s, s′ units, h prime" | yes | line 56 |
| 10 | REPORT3 Lemma P(iii) count; W̃^rest definition and relabelling | yes | optional true-W^rest column not added (it was optional) |
| 11 | REPORT3 §3 tail bound, η ≤ 200 validation, decay → [N] + R–P route | yes | lines 31, 83, 92, 108, 117 |
| 12 | REPORT3 m_* scope, Ehrenfest comparison, BGOS instead of KM | yes | lines 118, 120 |
| 13 | REPORT3 §0 χ_m ∈ [0.82, 0.995] | yes | |
| 14 | REPORT3 Parseval/ℓ² wording, minimal-period caution, torsion clause | yes | the clause is **dropped**, not made precise; justified by phase 4 §2.3 (confirmed in §8.6) |
| 15 | REPORT3 §5 small-η outliers, heuristic yardstick, [H] | yes | |
| 16 | REPORT3 literature | yes | |

**Verdict: 16/16 applied faithfully.** Two residual spots in REPORT3 §4(b) should also change:
- **R1.** Line 143 still asserts "This is the second-moment shadow of the phase-2 finding … For NSW-prime m it is absent" before the withdrawal note. Replace it with: "Phase 3 proposed this as the second-moment shadow of the phase-2 torsion obstruction; phase 4 withdraws that explanation (below)."
- **R2.** Line ~134, "Three mechanisms keep W̃^rest away from 0, each identified exactly", should read: "Two regimes are identified ((a) pre-mixing, (c) the generic part); a third mechanism (b) was proposed and is withdrawn."

The *descriptive* phase-3 fact is true. In my own computation (t12) the 12 largest |A_r| at (11, η = 2) all have r ≡ 0 mod 23 (|A_0| = 7615; the next are ≈ 2900–3700, rms 982). These classes carry only 13.7% of Σ|A_r|², against a point share of 8.5%. So the torsion classes are over-coherent, but they are not where the excess lives.

### 8.2 (a) Lemma V and Prop L: **correct, [P] justified**
- **Proof check.**
  - O/hO ≅ V^_odd via γ ↦ (Tr γλ^j); disc(1, λ) = 32 is prime to h, so the trace form is nondegenerate mod h.
  - n ∈ Λ ⇔ α_n ∈ h(2√2)⁻¹O ∩ O = hO, so h² | Nm α_n.
  - Nm(a + bλ^d) = a² + b² + abT_d ≠ 0, and |Nm| ≤ 324(2 + T_{(m−1)/2}) < h². The asymptotic check is λ^{(m+1)/2} > 1296, so m ≥ 9.
  - For m = 5, 7 the argument via the test sequence (0, 1) is valid (one test sequence gives a necessary condition).
  - The ‖n‖∞ ≤ 18 scope correctly covers the j = j′ terms.
  - All steps check.
- **Independent brute force (t10).** I tested membership in HZ^m + Z𝟙 directly by exact rational inversion of the circulant H (H⁻¹𝟙 = 𝟙/4), for all n = a e₀ + b e_d with |a|, |b| ≤ 18, for every odd m ≤ 61.
  - There are **0 lattice vectors for 5 ≤ m ≤ 61**. m = 3 fails (e.g. 7e₀).
  - The norm inequality holds for all odd 9 ≤ m ≤ 199 and fails exactly at m = 3, 5, 7, as the proof says.
- **Prop L (t11).** Direct sums over all h² q-sequences:
  - E X² / (mσ²) = 1.000000000000 for m = 5, 7, 9, 11, with E X = 0 to 1e-17.
  - χ ≥ 1 − ½mσ²η² holds at all tested η.
  - m = 3: E X² = 3.0·10⁻³ = 2.67·mσ², and the bound fails.
  - My m = 11 χ values (0.999485, 0.991790, 0.949974, 0.816736, 0.314637, 0.034858 at η = 0.5, 2, 5, 10, 25, 50) equal my turn-1 values from the independent CRT code.
- **Comment.** The bound is informative only for m ≲ 2/(σ²η²) ≈ 5333/η². It makes the pre-asymptotic "≈ 4m" regime rigorous; it says nothing at large m.
- **Lean (Phase4Checks)** checks only the numerical facts. `m3_obstruction : 7 ∣ 7·1` is content-free decoration and should either state the actual lattice relation (7e₀ ∈ HZ³ + Z𝟙) or be removed. The reduction steps are on paper.

### 8.3 (b) The certificate: **mathematically sound; rigorous modulo two small bookkeeping gaps; suggested status "verification-pending (computer-assisted)", not plain "proved"**

**Structure check.** The following steps are all correct:
- the cycle inequality γ₀ΣN ≤ cΣ|n − a| (L = |u| − |t|; constants γ₀ = 1 − 1/λ and c = 1/(2√2) in their normalisation, = 2 in mine);
- tilt products ≥ 1 on closed cycles, so |Tr M_a^m| ≤ Tr A_a^m;
- Collatz–Wielandt, with Tr A^m ≤ ρ^{m−1}Σ_s(Av)/v on all of Z²;
- the outside-box bound: for N(s) > K₂ and |δ| < x₂, the landing satisfies N(s′) > K_mid, and v(s′)/v(s) ≤ e^{κγ₀N(s) + κc|δ|};
- the lattice count #{N ≤ r} ≤ (2r + 1)(2λr + 1), which holds because p = u + t and q = λu + t/λ in their coordinates;
- coverage: 93 contiguous intervals, no gaps or overlaps, all 4·93 runs `valid`, max ρ = 0.999860.

**Rounding argument.** The a-priori bound is acceptable:
- every float sum has nonnegative terms and fewer than 500 summands (γ_n ≤ 1.2·10⁻¹³ ≪ SAFE − 1 = 10⁻⁹);
- arb uppers are rounded to nearest and then ×SAFE;
- there are no subnormals (smallest product ≈ 10⁻⁶², so relative-error analysis holds).

It does rely on libm `exp` being accurate to a few ulp (true for glibc, but not an IEEE guarantee). That is standard for computer-assisted proofs, but it should be stated as a hypothesis.

**Gaps found** (all ≪ 10⁻³⁰ in size, but unproved as written):
- **G1.** `rem = … + tl·1e40`: the J-truncation tail tl is an *unweighted* ℓ¹ bound. The factor 10⁴⁰ is called a "generous tilt factor", but there is no lemma that the tilted tail Σ|err(n)|e^{τ|n|} ≤ 10⁴⁰·tl. It is true numerically: my rigorous tilted bound is 2(y^{J+1}/(J+1)!)e^y per factor with y = X e^{τk}/2, giving ≤ 10⁻³⁰ even at J = 40. Fix: compute the tilted tail directly (one line).
- **G2.** `bounds()`: `np.convolve(term, D)[9:-9]` truncates the Taylor terms at the array edges. Spilled mass, and true coefficients beyond the stored n-range, are silently set to 0. Edge values are ≈ 10⁻³⁰⁰, so this is harmless, but it is not accounted for. Fix: keep the full convolution, or add the spilled mass to `drop`.
- **G3** (presentation). Theorem D_cert must say what it does *not* give. The bound is < 0.01 only for m ≥ m⁺, which is 1.4·10⁵ at η ∈ [1, 1.1], 6·10³ near η = 5 and 10²–10³ for η ≳ 15. Below that it is vacuous. It does not certify anything at the m where numerics or NSW primes live, for η ≲ 10.

**Independent re-certification (t9_cert.py, no phase-4 code).** My implementation differs in all the places that matter:
- my own eigen-normalisation;
- coefficient envelopes computed in arb with η as a **ball** on 24 sub-intervals (no Taylor/Gronwall), with a rigorous tilted truncation tail;
- **directed (outward) rounding**: `nextafter` after every float op; exponentials only from arb-computed monotone tables; N(s) enclosed ±10⁻⁹; matvec error bounded by (1 + (k+1)u)/(1 − (k+1)u);
- the outside region and the lattice tail evaluated in arb.

Results (ρ = max over a; C = Σ_a C_a):

| interval | phase-4 ρ_I | my certified ρ | my C | max\|μ\| (float, turn 1) |
|---|---|---|---|---|
| [1.0, 1.1] | 0.999860 | **0.999820** | 1.35e7 | 0.999813 (η = 1) |
| [2.6324, 3.3853] | 0.999789 | **0.998787** | 1.30e7 | |
| [10.2198, 11.0104] | 0.986106 | **0.982879** | 1.31e7 | 0.981765 (η = 10) |
| [30.0, 30.5] | 0.898361 | **0.900** (a = 0: 0.89231; a ≠ 0 floored at 0.9) | 8.8e6 | |
| [50.5, 51.2] | 0.862820 | **0.900** (a = 0: 0.84216) | 4.6e6 | 0.731 (η = 50) |
| [81.2445, 81.5741] | 0.999848 | **0.987552** | 6.7e6 | |

All six are valid with ρ < 1. So on these intervals the claim |χ_m(η)| ≤ Cρ^{m−1} holds with fully directed-rounding arithmetic.
- At η ≈ 1 my certified ρ is within 7·10⁻⁶ of the true leading |μ|. The majorant is tight there.
- At η ≈ 81 my ρ (0.988) is far below theirs (0.99985). Their ρ_I is inflated by the Gronwall envelope over a wide interval, so the coverage end at 81.574 is an artefact of their envelope, not of the method.
- My C is about 4× theirs, from the cruder lattice count. Their C_I ≈ 3·10⁶ is consistent.
- One implementation note for the authors: for a ≠ 0 at large η the float radii approach those of a = 0 (0.976–0.987 at η = 81). The `rfloor` = 0.95 logic is fine, but it is not "≈ 0.08–0.4" there. Correct that sentence of §1.3.

**Verdict.**
- **[Cert] is honest**, and the math is right.
- For repo status "proved" I would require: (i) G1 and G2 fixed in code and the grid rerun; (ii) a short written float-error lemma, including the libm hypothesis; (iii) independent re-certification of *all* 93 intervals. My t9_cert.py can do (iii) in about 6–8 h of box time. I did 6 now.
- Until then the status is **verification-pending (computer-assisted)**.

### 8.4 (c) Decay at every fixed η ≠ 0 via resonances plus Livšic: **sound sketch; keep [P-sketch]; suggest a simpler last step**
- **What checks out:**
  - |ν| ≤ 1: cleanest via the trace formula, |Tr^♭𝓛^m| ≤ #Fix(T^m)/|det(I − T^m)| = 1, so Σν^m z^m is analytic in |z| < 1.
  - The meaning of "ζ_a of order | 4": ζ_a = e(−aθ) is a genuine non-trivial character, but its class in Z²/(Tᵗ − I)Z² has order dividing det(T − I) = −4, so ζ_a⁴ is a character coboundary. The 4th-power step is therefore correct, though the wording should say "cohomology class of order dividing 4" rather than "order | 4".
  - The lift: degree k forced to 0 by invertibility of T − I. ∫u = 0 kills the constant, so u = (2π/4η)(φ∘T − φ) with φ continuous.
- **Simpler contradiction (recommended).** A continuous coboundary has vanishing sums over every periodic orbit. The support points ½𝟙 + x/h are T-periodic orbits of length m, and X(x) is exactly that orbit sum. So X ≡ 0 on 𝒮, contradicting Prop L: E X² = mσ² > 0 for any single odd m ≥ 5. This replaces the Green–Kubo correlation computation and reuses Lemma V.
- **Inputs still to verify:**
  1. trace class / nuclearity of the twisted analytic transfer operator on an anisotropic space, and the identity Tr M_a^m = Tr^♭𝓛_a^m (the Poisson step);
  2. the peripheral-spectrum lemma (|ν| = 1 ⇒ L^∞ eigenfunction: Cesàro projector of uniformly bounded functions);
  3. measurable → continuous Livšic for S¹-valued Hölder cocycles over Anosov automorphisms (Livšic 1972; Pollicott–Walkden 2001).

  All three are standard, but each needs a precise citation with hypotheses matched.
- **Limitation.** No constants. Uniformity on compact η-sets follows from upper semicontinuity of the spectral radius only if one anisotropic space works for the whole η-range. That is not stated, and it is not needed for "fixed η".
- **Status:** conditional on (1)–(3), i.e. **verification-pending**.

### 8.5 (d) Conjecture R: **precise and well-posed; one evidence number is wrong**
- The statement is good: max over η ∈ [η₀, η₁] of |W̃^rest_m(η)|/m → 0 through odd m, plus R_NSW.
- Since |E| ≤ 4m²/h → 0, the W̃ versus W distinction is immaterial in the limit. Together with Theorem D and §8.4, R is equivalent to F_m(η) = 2m(1 + χ_m(η)) + o(m) uniformly on compacts, i.e. the derandomized COE diagonal value at fixed η. It is the correct target.
- **Evidence fix.** "|W̃^rest|/2m ≤ 0.11, **0.04**, 0.018, 0.008 at m = 7, 9, 11, 13 for η ≥ 10" → "0.11, **0.05**, 0.018, 0.008 for η ∈ [10, 400]". REPORT3's table has −0.05 at (m, η) = (9, 400).
- The evidence is m ≤ 13 only, and it includes the unexplained (11, 2) spike of +3.57. Status **open [C]**. The literature section (no reduction to a named conjecture; DFI, KR, BGK and BG are all unavailable in the minimal-period regime) agrees with my turn-1 assessment.

### 8.6 (e) Torsion withdrawal: **reproduced exactly; withdrawal justified**
With independent code (t12: my own q-sequence enumeration, norm classes r = x₀² − 6x₀x₁ + x₁² mod h, and the Ramanujan kernel via the multiplicative c_h), at m = 11, h = 23·353:

| η | F/2m | p = 23: e_gen / e_tor / F_tor/2m | p = 353: e_gen / e_tor |
|---|---|---|---|
| 2 | 5.5617 | +3.2484 / +7.0287 / 0.7673 | +3.5277 / +11.00 |
| 5 | 2.0967 | +0.1270 / +0.3581 / 0.1963 | +0.1435 / +0.7043 |
| 10 | 1.8320 | +0.0195 / −0.0303 / 0.1520 | +0.0180 / −0.4608 |

- These match phase-4 §2.3 to 4 decimals. The share s_p = (2p − 1)/p² is confirmed.
- The excess at η = 2 survives in the generic classes, so withdrawing the torsion attribution is correct. The outlier is **open [N]**.
- As noted under R1–R2, the true part of phase 3 (top classes are r ≡ 0 mod 23) should be kept as a description.

### 8.7 (f) Lean
- I copied Phase4Checks.lean to build/Bgs/, ran `lake exe cache get` ("No files to download", 8690 files already present) and `lake env lean Bgs/Phase4Checks.lean`: **exit 0**, 50 s. Log: logs/lean_phase4_build.log.
- Axioms:
  - `m5_U`, `m7_U`: none (`decide`);
  - `U2_value`, `m7_prime`, `m9_norm`: propext, Classical.choice, Quot.sound (norm_num);
  - `m3_obstruction`: propext.
- No sorry and no native_decide.
- The `Umod` recursion is the correct U-sequence (U₀ = 1, U₁ = 6), and the ranges Fin 4 / Fin 6 match d = 1..m−1.
- As noted in §8.2, `m3_obstruction` is vacuous.

### 8.8 Phase-4 verdict table

| Claim | Label given | My verdict |
|---|---|---|
| Lemma V | [P] (+ L finite cases) | **correct**; brute-force confirmed for m ≤ 61 |
| Prop L (χ ≥ 1 − ½mσ²η², m ≥ 5) | [P] | **correct**; E X² = mσ² exact for m = 5–11; m = 3 fails as stated |
| §1.2 majorant, cycle inequality, Collatz–Wielandt | [P] | **correct** |
| §1.3–1.5 certificate on [1, 81.574] (Theorem D_cert) | [Cert] | **sound**; gaps G1 and G2 (tiny); 6 intervals independently re-certified with directed rounding; status verification-pending |
| §1.6 decay at every fixed η | [P-sketch] | **sound sketch**; three cited inputs; use the Prop L contradiction |
| Conjecture R | [C] | **precise**; fix m = 9 evidence 0.04 → 0.05 |
| §2.3 torsion split and withdrawal | [P identity; N] | **reproduced exactly**; withdrawal justified; outlier open |
| Phase4Checks.lean | [L] | **builds**; m3_obstruction vacuous |

### 8.9 Phase-4 fix list (replacement wording)
1. REPORT4 §1.3, end of step 1: add "The J-truncation tail is bounded in the tilted norm by 2Π_k(…) with y_k = |x_k|e^{τk}/2, giving ≤ 10⁻³⁰" (replacing the `tl·1e40` heuristic in code). Keep the full convolution in `bounds()` (G2). Rerun grid.py.
2. REPORT4 §1.3, "What is not interval arithmetic": add "The a-priori bound also assumes libm exp/log accurate to ≤ 4 ulp. An independent directed-rounding re-certification (referee, t9_cert.py) confirms 6 of the 93 intervals."
3. REPORT4 §1.3, last bullet: "These a have float radii ≈ 0.08–0.4" → "≈ 0.08–0.4 for η ≲ 11, increasing to ≈ 0.98 near η = 81".
4. REPORT4 §1.5 Theorem D_cert: add "The upper bound is < 1 only for m ≥ m⁺(η) (≈ 1.4·10⁵ at η = 1, ≈ 6·10³ at η = 5, 10²–10³ for η ≳ 15). It is a qualitative decay statement with explicit but large thresholds, and gives no information at m ≤ 13."
5. REPORT4 §1.6: "ζ_a a character cocycle of order | 4" → "ζ_a = e(−aθ), whose class in H¹ (characters modulo (Tᵗ − I)) has order dividing |det(T − I)| = 4". Replace the final Green–Kubo contradiction with: "A continuous coboundary has zero sum over every periodic orbit, so X ≡ 0 on 𝒮, contradicting Prop L (E X² = mσ² > 0)."
6. REPORT4 §2.2 evidence: "0.11, 0.04, 0.018, 0.008" → "0.11, 0.05, 0.018, 0.008 (η ∈ [10, 400])".
7. REPORT3 §4(b): R1 and R2 of §8.1.
8. REPORT2 §H: the Theorem N scope sentence (§8.1, item 3).
9. Phase4Checks.lean: replace `m3_obstruction` with a real statement, namely the explicit membership 7e₀ = H₃·(1,0,0) + 𝟙 = (6,−1,−1) + (1,1,1), checkable by `decide`. Otherwise delete it.

### 8.10 Final integrable package, phases 1–4

**Dependencies on existing repo claims** (main d6fa6e2a, record/claim_registry.md, read via the GitHub connector):
- **BGS-TRACE-131 (PROVED).** Line B's time-reversal statement (M_N symmetric for S = [[3,4],[2,3]], α ≡ δ = 3, so Uᵀ = K⁻¹UK for real position kicks) is exactly the α ≡ δ case of TRACE-131. Cite it; do not re-claim.
- **BGS-TRACE-127, 128, 132 (PROVED).** These are the *random-phase* (Haar diagonal D) short-time limits (fixed-m limit 2m; time-3 kernel 49 when 7 | N). Line B is the derandomized analogue, with a fixed 32-mode kick and an N/ν-average. The 2m of phase 1 is the same diagonal value. Cite as the comparison; there is no logical dependence. The 7 | N phenomenon parallels Line B's h₃ = 7 torsion and the failure of Lemma V at m = 3 (worth one sentence).
- **BGS-TRACE-143, 144 (PROVED).** 143 is the Haar ↔ DFT star-graph equivalence; 144 is the Gauss-sum/partition-lattice formula. Line B's Prop K/Prop C are the fixed-kick counterparts (Gauss sums → Ramanujan sums). They are independent proofs, so cite as related.
- **BGS-TRACE-145, 146 (PROVED), 147 (VERIFICATION-PENDING), 148 (OPEN).** These cover the random-phase off-diagonal (2-opt/swap/figure-eight) and τ², τ³ coefficients. Line B's W̃^rest / Conjecture R is the derandomized analogue of the *off-diagonal* problem. Line B proves nothing at τ = O(1), so it must not be presented as progress on TRACE-148.

**Items and suggested status:**

| Item | Status |
|---|---|
| Phase 1 Thm 3 / Prop R / 2m law for m ≤ 8 (with F1, F2) | proved (finite m); 2m law conditional on ND_m for general m |
| Prop K, Lemma S + Addendum, Lemma F, Theorem D (Lean m ≤ 9, audit m = 11) | **proved** |
| C2 p-splitting; C3 symbol facts (sign fixed) | **proved** |
| Automatic admissibility (Frobenius) | **verification-pending** (write-up exists in REPORT2; needs a second reader) |
| Theorem N for the 11 certified NSW-prime m, with ECPP certificates (7 re-verified) | **proved** (bound; nontrivial from m = 29) |
| Prop C for all odd m (Gauss-sum proof) | **verification-pending** (written; independently checked by me) |
| Theorem W identity (W̃^rest), Theorem T identity χ_m = Σ(−1)^a Tr M_a^m | **proved** |
| Lemma V, Prop L (lower bound, m ≥ 5) | **proved** |
| Majorant / cycle inequality / Collatz–Wielandt framework (§1.2) | **proved** |
| Theorem D_cert on η ∈ [1, 81.574] | **verification-pending** (computer-assisted; fix G1/G2, full independent rerun) |
| Decay of χ_m at every fixed η ≠ 0 | **conditional** on the three cited inputs of §8.4 |
| Theorem U (error estimate, corrected interpretation) | **proved** |
| Theorem G | **conditional** (ND^(≤k) incl. unequal-length relations) |
| ND^(2) at small m; μ(η) spectrum; m_* crossover; W̃^rest tables; fixed-η CLT numerics; torsion split numbers | **numerical-only** |
| Torsion-split identity F = F_gen + F_tor | proved (trivial identity); interpretation numerical |
| Conjecture R / R_NSW; fixed-η CLT; ND for composite h and even m; the (11, 2) outlier | **open** |

**Required non-claims** (to appear verbatim in the integrated text):
1. Nothing is proved at τ = m/N = O(1). All results are fixed-m (diagonal / below Ehrenfest). This is not progress on BGS-BGS-001 or BGS-TRACE-148.
2. "B_m → 2m" is not claimed. Theorem N covers a finite list of certified NSW primes, and the infinitude of NSW primes is open.
3. The parity crossover is the derandomized analogue of the known BGOS/Pandey–Mehta symmetry-breaking crossover. It is not a Keating–Mezzadri pseudo-symmetry, and the phenomenon is not new.
4. The certified decay bound is vacuous below m⁺(η) (10²–10⁵). It says nothing at the numerically accessible m.
5. Conjecture R is not reduced to any known conjecture or large-sieve inequality. The "quadratic large sieve" phrasing is withdrawn. KR/Bourgain/BGK do not apply (minimal period ord_h λ = m).
6. The fixed-η CLT is numerical only (m ≤ 11); the KS yardstick is heuristic.
7. The (m, η) = (11, 2) outlier is unexplained; the torsion attribution is withdrawn.
8. The Theorem D_cert arithmetic is IEEE float with an a-priori error bound (plus arb coefficients), not full interval arithmetic, until the full directed-rounding rerun.

**Remaining blockers before integration:**
- **B1.** Fix G1/G2 in certify.py, rerun grid.py, and get an independent directed-rounding re-certification of all 93 intervals. My t9_cert.py is ready, about 6–8 h.
- **B2.** Second reader for automatic admissibility and the Prop C general write-up.
- **B3.** For the fixed-η decay: precise citations with matched hypotheses for nuclearity / flat trace (twisted linear Anosov, analytic weight), the peripheral-spectrum lemma, and measurable Livšic for S¹ cocycles. Otherwise keep it as conditional.
- **B4.** Apply the wording fixes R1, R2 and §8.9, and assign claim IDs. The new IDs should cite TRACE-131 (time reversal) and TRACE-127/128/143/144 (random-phase comparison) as related, not as dependencies.

### 8.10a Second-reader addendum (2026-10-29, added by the independent second reader; the table above is the referee's and is left unchanged)

| Item | Referee status (8.10) | After second reading |
|---|---|---|
| Automatic admissibility (Frobenius), TRACE-167 | verification-pending | **proved** (statement confirmed; part (b) needed a one-line fix in the split case, norm-1 argument; fix applied) |
| Prop C for all odd m, TRACE-169 | verification-pending | **proved** (confirmed, incl. p² | h; no fix) |
| Theorem D_cert on η ∈ [1, 81.574], TRACE-173 | verification-pending | **proved (computer-assisted)** with the directed-rounding constants of t9_cert.py (unmodified): 93/93 valid, contiguous [1, 81.57406988332305], max ρ' = 0.99981969, max C' = 1.4296e7; not with the float constants (C_I ≤ 3.64e6) |

Blockers: B1 closed (all 93 intervals re-certified with directed rounding; G1/G2 were fixed by the authors). B2 closed. B3 unchanged (174 stays conditional). Report and logs: packet `computations/verification/lineB/second_reader/`.

### 8.11 Reproduce (phase 4 audit)
```
P=/workspace/audit/derand23/venv/bin/python; cd /workspace/audit/derand23/code
$P t10_lemmaV.py      # ~4 min, Lemma V brute force m<=61 + norm inequality
$P t11_propL.py       # ~2 min, E X^2 = m sigma^2 and chi >= LB, m=3..11
$P t12_torsion.py     # ~1 min, torsion split m=11
B=0.0176777; K=0.0088388   # beta=0.1/(4 sqrt2), kappa=beta/2 in my normalisation
$P t9_cert.py 1.0 1.1 $B $K 45.2548 25        # R1 = Kmid*4*sqrt2 ; x2
$P t9_cert.py 2.6324 3.3853 $B $K 50.9117 27
$P t9_cert.py 10.2198 11.0104 $B $K 62.2254 31
$P t9_cert.py 30.0 30.5 $B $K 90.5097 40
$P t9_cert.py 50.5 51.2 $B $K 113.137 50
$P t9_cert.py 81.2445 81.5741 $B $K 113.137 50   # ~5 min, ~6 GB
cd ../build && lake exe cache get && lake env lean Bgs/Phase4Checks.lean
```
