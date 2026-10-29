# Referee audit of BGS Line D (`/workspace/bgs-lineD/REPORT.md`): band-limited random kicks on the quantized cat map

Everything in this audit lives in `/workspace/audit/lineD/`: `code/` (fresh code that shares nothing with `bgs-lineD/code`), `logs/`, `lean_build/` (isolated Lean copy). Backups go to `/home/box/audit_lineD_backup/` every 15 min. `/workspace/bgs-lineD` was only read. Nothing was pushed.
Context I also read: Line B (`/workspace/bgs-derand/REPORT.md`: Thm 1, Prop R, Thm 4, ND_m), the Line C registry text, and registry entries BGS-TRACE-126/129/133/143–148 (PR-54 snapshot `audit/pr54/h2`).

## 0. Verdicts at a glance

| Item | Verdict | Recommended registry state | One-line reason |
|---|---|---|---|
| D1 exact bridge | **confirmed, needs fix** (wording) | proved | The algebra is right. Pathwise brute force matches to ≤1e-12 at 28 (m,p,kick) cases. But "real-analytic" is not proved (only C^∞), the evenness argument is mis-stated, and the identity is Line B Thm 1 applied for each θ. |
| D2 1/p expansion | **confirmed, needs fix** (scope) | proved (scope as fixed below) | The Taylor step is right. The period-g' reduction has a one-line proof, so it is [P], not [N]. The O(p⁻²) constant is **not uniform in η or K**: at p = 101 the two-term expansion already fails at η = 4 and gets the sign wrong at η = 16. |
| D3 orbit-pair formula | **confirmed, needs fix** | proved | Poisson plus the Kluyver average is right. The orbit formula matches the n-sum to 1e-10. The support facts are provable (Line B Prop R, or the 3-line argument below), so the "[N]" and "[P-sketch]" tags can be upgraded. Fix the "Fix_m = period-m orbits of S" wording. |
| D4 strong-kick limit | **confirmed as an implication; downgrade the corollary "=2m for no finite m and no fixed K"** | implication: proved. Instances m ≤ 7: verification-pending. B^sym < 2m for all m: proved for odd m (argument below), open for even m > 9 | Values reproduced exactly: 235/49, 61/12, 15801/1681, 27417/2450, 788019/57121. The corollary is false as worded: at finite η, Ψ_m(t*) crosses 2m by continuity. |
| D5 separation / collisions | **needs fix** | (a) multiset part proved; Γ part for m ≤ 7 verification-pending. (b) proved. (c) verification-pending | Newton separates **multisets**, not Γ-classes. The table row overclaims this. "p-dependence survives exactly when 𝒦 fails to separate" is **wrong**: at m = 4, K = 1 the limit is non-separating but s-independent. |
| D6 1/p coefficient | (a) **confirmed**. (b) **needs fix**. The §5 sentence "c₁ → 0 (separating)" is **wrong for the J0 ensemble** | (a) proved. (b) conditional (G ensemble, Γ-separation). J0 large-η behaviour: open | The tilted factor b is O(η⁴), not O(η²). For uniform phases, c₁ **grows** (m = 3, K = 1 separating: max\|c₁\| = 13, 129, 683, 7182, 85063 at η = 1, 4, 16, 64, 256). |
| D7 full band = Line C | **confirmed** (minor fixes) | proved (conditional only on BGS-TRACE-146, which is proved) | Re-derived. Exact enumeration at p = 5, 7, 11, 13 (m = 3, 4) confirms both bounds. Line C values 235/49, 631/121, 901/169, 1829/343 are reproduced. The "literally i.i.d." remark is wrong (zero-sum constraint) but harmless. |
| D8 R-scaling, K_* ∝ p^{2/3} | **downgrade wording** | open (conjecture) + numerical | Two primes collapse (p = 101 does not). R is defined from the G-ensemble weight but tested on J0 data. K_* ∝ p^{2/3} is just "R fixed" restated, and R_* depends on the sample size. |
| D9 "χ² ≈ 967 explained" | **downgrade to "consistent with"** | numerical | K_eff = 1.04 and R = 0.39 are confirmed. The χ² runs over m = 3..202, where D1–D6 (fixed m, p → ∞) say nothing. |
| Lean `Bgs.LineDCerts` | **confirmed; wording fix** | proved (finite certificates only) | Builds in my own copy (49 s). Kernel `decide` only, no imports. Axioms are ∅ or {propext}. No sorry or native_decide. `coll4/coll6` do **not** certify completeness, the support, or Γ-distinctness. I checked those outside Lean. |
| Novelty (§1 of their report) | **overstated** | — | The mechanism of D1/D3 is Boasman–Keating 1995 §5, already disclaimed in Line B. The J0 average is recorded as standard in BGS-TRACE-133. D4 is the ensemble analogue of Line B Thm 4 with the same B^sym. Degli Esposti–Winn 2005 is uncited. Keating 1991 is mis-cited. |

## 1. Line-by-line re-derivation

### D1
* **Cycle form.** Σ_j(3x_j² − 2x_jx_{j+1} + 3x_{j+1}²) = xᵀ(6I − C − Cᵀ)x. ✔ (also for m = 2).
* **Determinant.** det H_m = Π_j(6 − 2cos 2πj/m) = λ^m + λ^{−m} − 2 = Tr S^m − 2. ✔
* **Completing the square.** With c = −8̄, we need 2cHu = n, so u = (2c)⁻¹H⁻¹n = −4H⁻¹n. ✔ Then −c uᵀHu = 16·8̄ nᵀH⁻¹n = 2nᵀH⁻¹n = 2D̄ nᵀX n. ✔ The phase sign is +, which I checked pathwise.
* **Hypotheses actually used:**
  * 2 is invertible (N odd);
  * H is invertible mod N, i.e. gcd(N, D_m) = 1;
  * the m-dimensional Gauss sum is non-degenerate, so \|Tr M^m\| = 1.
  
  **Primality is not used.** D1 holds for every odd N with gcd(N, D_m) = 1, which is exactly Line B Thm 1's range. Since D_m is even, p ∤ D_m already excludes p = 2. When p \| D_m the normalization breaks: I find \|Tr M_7³\| = 7 and \|Tr M_3⁴\| = 3 (`logs/d1_pathwise.log`). Keep the hypothesis explicit.
* **Gauss-sum signs and Jacobi symbols.** Tr M_p^m = ε_p^m·(Legendre factor). It enters only through \|Tr M^m\|² = 1, so no Jacobi or Legendre symbol and no p mod 4 dependence survives in E\|Tr U^m\|². ✔ (Unlike Line C, there is no p^{−k−1/2} sign issue at this level.)
* **Evenness (fix).** The report argues "θ → −θ, i.e. Ĝ(−n) ↔ conj". That is not the right symmetry: θ → −θ maps Ĝ(n) → Ĝ(−n) with no conjugation. The correct argument:
  * conj Ĝ_θ(n) is the coefficient of e^{−iηV_θ} at −n;
  * −V_θ = V_{θ+π} (for the G ensemble, c → −c), and both ensembles are invariant under this;
  * A(−n) = A(n).
  
  Hence Ψ(t) = E\|conj Σ\|² = Ψ(−t). The conclusion is correct.
* **"Real-analytic" (fix: replace by C^∞).** Ψ(t) = Σ_{n,n'} E[Ĝ(n) conj Ĝ(n')] e(t(A(n) − A(n'))).
  * The frequencies A(n) − A(n') are quadratic in n.
  * Ĝ(n) decays only like exp(−c\|n\| log\|n\|) (Bessel/entire-function decay), not like exp(−r\|n\|²).
  * So the series converges with all derivatives (C^∞), but analytic continuation to Im t ≠ 0 would need Σ\|Ĝ\|e^{2π\|Im t\|\|A(n)\|} < ∞. That diverges.
  
  Real-analyticity is therefore unproved and probably false: this is a theta-type series on the boundary. Only C² is needed for D2.
* **Numerics (fresh code).** I compared literal matrices U = e^{iηV_θ}M_p against Tr M^m·Σ_n Ĝ(n)e(t_pA(n)), with Ĝ from an FFT of the kick.
  * m = 3: ≤ 4e−13 at p = 5, 11, 13, 29, 101.
  * m = 4: ≤ 1e−12 at p = 5, 7, 11, 13, 29.
  * m = 5: ≤ 4e−9 at p = 3, 7, 11, 13 for one mode. The two-mode errors of 1e−7 (m = 4) and 3e−4 (m = 5) are truncation in n at \|n_i\| ≤ 14 and 9.
  
  In expectation (exact single-phase average), brute-force E_θ equals Ψ(t_p) to ≤ 1e−11 at 17 (m,p) pairs (`logs/psi_check.log`).

### D2
* t_p = D̄/p and DD̄ = 1 + pj give j ≡ −p̄ (mod D), so t_p ≡ t* + 1/(pD). ✔ (Checked to 1e−12 for 18 (m,p) pairs.)
* **Period g' is [P], not [N].** Let g' := D/gcd(D, 2X_ii, 4X_ij).
  * Every value A(n) = 2nᵀXn is a multiple of D/g'.
  * So e(sA(n)/D) depends only on s mod g', and Ψ(t*) only on p mod g'. By evenness it depends only on ±p mod g'.
  * I compute g' = 14, 48, 82, 280, 478, 1632, 2786 for m = 3..9, matching the report.
  * This is an upper bound on the period. For m = 4, K = 1, a = η = 1 the value 4.0578 is shared by p ≡ 5, 17, 29 (mod 48), so the true period there is smaller.
* **Reproduced (J0, K = 1, a = η = 1).**
  * Ψ_4(t*) = 4.0578090022 at p = 101, 197, 401, 797, 1601.
  * p(Ψ(t_p) − Ψ(t*)) = 7.137, 7.180, 7.199, 7.208, 7.212, which is identical to theirs.
  * c₁ = Ψ'(t*)/D = 7.2153 by central difference. They give 7.2156; the difference is at the level of my h = 1e−6 differencing.
  * m = 5 values: 5.080, 2.411, 10.856, 3.492, 22.646.
* **Uniformity (fix required).** The remainder is ≤ sup\|Ψ''\|/(2D²p²), uniform in p for fixed (m,𝒦,a,η). That is fine. But sup\|Ψ''\| grows with η and K, since the effective frequencies are \|A(n)\| ~ (ηaK)². The expansion is therefore **not uniform in η or K**, and the limits p → ∞ and η → ∞ do not commute. Concretely, at p = 101, m = 3, K = 1, J0 (`logs/extra.log`, `logs/nonuniform_p101.log`):

  | η | p(E − Ψ(t*)) | c₁ at that residue |
  |---|---|---|
  | 1 | 13.2 | 13.3 |
  | 4 | −14.5 | −6.5 |
  | 16 | +40.5 | −201 |
  | 64 | +41.7 | −7182 |

  The O(p⁻²) statement must say "for fixed (m,𝒦,a,η); the constant grows at least polynomially in η and K". The "regime of validity η²(Σk²a_k²)m ≪ p" is a heuristic and should be labelled [C].

### D3
* **Poisson summation is correct.** A(n + Hk) = A(n) + 4D kᵀn + 2D kᵀHk ≡ A(n) (mod D), so e(sA/D) lives on V = Z^m/HZ^m. Its dual is H⁻¹Z^m/Z^m. ✔
* **The averages are correct.** E e^{i Re(a e^{iθ} z)} = J0(a\|z\|). E e^{i Re(cz)} = e^{−a²\|z\|²/4} for E\|c\|² = a². ✔ The J0 average is the "standard Kluyver average" already recorded, and not claimed as new, in BGS-TRACE-133. Cite it.
* **Numerics.** The orbit formula equals the n-sum Ψ(t*) to 1e−10 (m = 3, 4, 5, all tested residues) and to 1e−10 for the G ensemble (m = 3, `logs/c1_validate.log`).
* **Support facts can be upgraded to [P].** Put Q(β) = βᵀH⁻¹β and β = β' + γ. Then
  \|φ̂_s(ξ)\|² = D⁻¹ Σ_{γ∈V[4]} e(2sQ(γ) − γ·ξ),
  because Σ_{β'} e(4sγᵀH⁻¹β') = D·1[4H⁻¹γ ∈ Z^m] for s a unit.
  * On V[4], 2Q(γ) = ½γᵀ(4H⁻¹γ) ∈ ½Z, so e(2sQ(γ)) = ±1 depends only on s mod 2, and s is odd.
  * γ ↦ e(2sQ(γ) − γ·ξ) is a character of V[4] because 4H⁻¹γ' ∈ Z^m.
  * Hence \|φ̂_s\|² ∈ {0, \|V[4]\|/D}, and the support is independent of s.
  
  This is Line B Prop R. Checked against direct φ̂ (error ≤ 5e−17) for m = 3..6 at 6 residues each. D_eff = 49, 72, 1681, 4900, 57121 and \|Rad\| = 4, 16, 4, 8, 4 for m = 3..7. Γ- and parity-invariance of φ̂, phase included, hold to 1e−16 (`logs/structure_m*.log`).
* **Wording fix.** Fix_m = {ξ : Hξ ∈ Z^m} is the set of period-m points of the q-recurrence, i.e. of T = [[0,1],[−1,6]]. It has the same cardinality D_m as Fix(S^m), but the q-projection of Fix(S^m) is not shown to be a bijection. Line B's own ref-fix limits that identification. Say "period-m solutions of q_{j+1} + q_{j−1} = 6q_j (mod 1)".

### D4
* **The implication is correct.** Finitely many pairs; every pair with ΔP_𝒦 ≠ 0 has weight → 0 (J0(x) → 0 and e^{−x²} → 0); φ̂ is constant on Γ-classes. Add the hypothesis **a_k ≠ 0 for k ∈ 𝒦**.
* **Values (fresh, exact rationals).**

  | m | B_m^sym |
  |---|---|
  | 3 | 235/49 = 4.795918 |
  | 4 | 61/12 = 5.083333 |
  | 5 | 15801/1681 = 9.399762 |
  | 6 | 27417/2450 = 11.190612 |
  | 7 | 788019/57121 = 13.795609 |

  These agree with the report and with Line B's table.
* **Numerical limit.** With the G ensemble at η = 32–128, Ψ → B^sym at every residue mod g' (6, 16 and 40 residues for m = 3, 4, 5) for 𝒦 = {1,2} and {1..m}, and for 𝒦 = {1} at m = 3 and 5 (`logs/d4_limits.log`).
* **Thresholds.** I reproduced the "smallest η within 1%·2m" entries for m = 3 (K = 1, G): 8; m = 4 (K = 2): 4; m = 5 (K = 2): 16; m = 5 (K = 4): 4.
* **Downgrade: "the exact leading term equals 2m for no finite m and no fixed 𝒦".** As worded this is false. Ψ_m(t*) is continuous in η, equals 1 at η = 0, and reaches 44.76 > 10 at m = 5, K = 1, η = 2 for some residue. So it equals 2m at some finite η. Correct statement: "lim_{η→∞} Ψ_m ≠ 2m".
* **B^sym < 2m strictly.**
  * Numerically for m ≤ 9 (Line B table).
  * **Provable for every odd m.** D_eff = a_m² with a_m odd (ρ^m + (1−√2)^m = 2a_m), so the Γ-invariant support has odd size. The reversal is an involution on it, so it has a fixed point; that point has \|Γξ\| ≤ m < 2m. Hence 2m − B^sym ≥ m/D_eff > 0.
  * The same orbit-counting argument works whenever 2m ∤ D_eff (true at m = 6).
  * Even m with 2m \| D_eff (m = 4, 8) rests on enumeration. For general even m it is open.
* **Unguarded "(c)" sentence.** "B_m^sym → 2m as m → ∞ but never equals 2m" needs exactly this qualification.

### D5
* **(a)** Newton plus K ⊇ {1..m} gives the multiset of {e(ξ_j)} ✔ [P]. **Γ-separation needs multiset ⇒ Γ.** I checked this **exactly** (integer arithmetic on w ∈ (Z/D)^m) for m = 3..7, on the support and on all of Fix_m: no multiset contains two Γ-classes. The summary row "𝒦 ⊇ {1..m} always separates (Newton) [P]" must read "separates multisets [P]; separates Γ-classes for m ≤ 7 [computer-assisted, exact]".
* **(b)** ✔ [P]: e(kξ)(1 + (−1)^k) = 0 for odd k.
* **(c)** Reproduced (floats, tol 1e−9):
  * K = 1 separates at m = 3, 5, 7. The support gaps are 0.753, 1.936e−3, 3.685e−5.
  * The report's 0.247 for m = 3 is the gap over **all of Fix_3**, not the support. State which set.
  * m = 4 has 2 collision classes and m = 6 has 26. All are half-turn-invariant multisets with S₁ = 0, the same classes as the Lean lists.
  * 𝒦 = {1,2} separates for m ≤ 7.
  * Ψ_∞(m = 4, K = 1) = 4.861111 at all 16 residues. Ψ_∞(m = 6, K = 1) ∈ {10.705923, 11.165914}, which is s-dependent.
* **Wrong: "the arithmetic p-dependence survives the strong-kick limit exactly when 𝒦 fails to separate".** m = 4, K = 1 fails to separate, yet the limit is the same at all residues. Correct: "non-separation is necessary for residue dependence of the limit, not sufficient (m = 6, K = 1: dependent; m = 4, K = 1: not)".

### D6
* **The formula is re-derived independently.**
  * Use e(hA(n)) ↔ exp(−(ih/π)∂ᵀX∂) on the torus and apply Poisson to F = −(i/π)∂ᵀX∂G^{⊗m} = −(iD/π)βG^{⊗m}.
  * This gives c₁ = (2/π) Im Σ φ̂(ξ) conj φ̂(ξ') E[G(ξ) conj G(ξ') β(ξ)], with β as stated. ✔
  * My Gaussian closed form (own derivation) matches the numerical d/dt of the n-sum Ψ_G to 1e−5 (η ≤ 1) and 6e−3 (η = 2) at m = 3 (`logs/c1_validate.log`).
  * My θ-quadrature for J0 matches d/dt at η = 1, 4, 8 (`logs/c1_j0.log`).
* **(a)** ✔ [P]. The Γ-diagonal part is ≤ 1e−12 in every run. Note that \|G\| = 1 for **both** ensembles, since V is real, so the "f = 1" remark for G is the same fact.
* **Table spot-checks (G, max over residues).**

  | m | K | η | max\|c₁\| (mine) | report |
  |---|---|---|---|---|
  | 3 | 1 | 1, 2, 4, 8, 16 | 8.70, 13.26, 19.08, 0.506, 1e−11 | 8.7, 13.3, 19.1, 0.506, 0 |
  | 3 | 2 | 1, 2 | 27.86, 11.96 | 27.9, 12 |
  | 4 | 1 | 1, 16, 32, 64 | 10.13, 77.39, 309.6, 1238 | 10.1, 77.4, 310, 1.24e3 (so ±0.302η² ✔) |
  | 4 | 2 | 2, 4 | 6.376, 0.0217 | 6.38, 0.0217 |
  | 5 | 2 | 2 | 186.2 | 186 |
  | 5 | 4 | 4 | 4.941 | 4.94 |

  The sum over residues is 0 to 1e−11, so oddness ✔.
* **(b) needs a fix.** Under Gaussian tilting, the mean of c shifts by iσ²ζ with ζ ∝ η, so the v'ᵀH⁻¹v' term contributes η²·σ⁴η²\|ΔS\|². Hence **b is a degree-4 polynomial in η**, not "quadratic". Measured: max\|b\|/η⁴ → 57, 178, 972 for (m,K) = (3,1), (4,1), (4,2). The bound becomes \|c₁\| ≤ C_m η⁴ e^{−a_min²η²δ²/4}. The conclusion c₁ → 0 survives, for the **G ensemble** only.
* **(b) hypothesis.** "applies to 𝒦 ⊇ {1..m} unconditionally" needs multiset ⇒ Γ. That is computer-checked for m ≤ 7 only (D5a).
* **Wrong for J0 (§5 sentence "it tends to 0 (separating) … as η → ∞").** For uniform phases the tilted moments are Bessel functions decaying like (η\|Δ\|)^{−1/2}, while β carries η². Measured at m = 3, K = 1 (separating, gap 0.753): max_s\|c₁\| = 13.3, 128.7, 682.7, 7182, 85063, 453908 at η = 1, 4, 16, 64, 256, 1024. That is growth of roughly η^{1.5}, versus ~1e−11 for G (`logs/c1_j0.log`). This matters because the D8 tables use the J0 (uniform θ) ensemble.
* **What *is* proved about "never −2m²".** c₁(−p mod g') = −c₁(p mod g') (Ψ' is odd), so c₁ averages to 0 over residues and cannot equal −2m² for all p. For individual residues and some η, c₁ = −2m² is not excluded: c₁ takes values like ±246 continuously in η. Reword "never reproduces −2m²" to "is odd under p ↦ −p (mod g'_m), hence not −2m² uniformly in p".

### D7
* **Parseval step re-derived.** Σ_{k=1}^{(p−1)/2}\|Δ̂(k)\|² = p‖Δ‖²/2 ≥ p, because ΣΔ = 0, ‖Δ‖² ≥ 2 and the spectrum of real Δ is symmetric. ✔
* **J0 bound.** J0 ≤ e^{−0.2x²} on [0,1] and \|J0\| ≤ J0(1) = e^{−0.2676} for x ≥ 1, so the bound with β = min(0.2, 0.2676/X²) holds. ✔ Also Σ\|K(x)K(y)\| = p^m. ✔
* **Exact enumeration (`logs/d7_check.log`).**
  * Line C values reproduced: 235/49 (p = 7, m = 3), 631/121, 901/169 and 1829/343 to ≤ 4e−15.
  * \|E_band − E_LC\| ≤ the stated bound at all 24 (p,m,ηa) cases, G and J0. The two "violations" are 8.9e−16 roundoff against bounds below 1e−16.
  * The J0 deviation decays slowly: 2e−3 at p = 13, ηa = 4. The J0 bound is vacuous at these p, as the report admits.
  * A Monte Carlo with the **literal** kick (p = 7, m = 3, J0, ηa = 1, 40 000 samples) gives 3.390 ± 0.014 against the pair-weight formula 3.405.
* **Fixes.**
  * (i) For the G full band, V = W − W̄ with W i.i.d. N(0, a²p/4). The sites are i.i.d. **up to a global phase**, which cancels in \|Tr U^m\|². They are not "literally i.i.d."
  * (ii) The transfer inherits Line C's hypothesis (prime p > 4^m, BGS-TRACE-146). Say so.
  * (iii) For J0 with ηa ≳ 1 the exponent βη²a²p ≈ 0.067p/m² does not improve with η. The error is exponentially small only for p ≫ m³ log p.
* **Interesting aside (not a claim).** B_3^sym = 235/49 equals E_LineC(7,3) exactly, and 7 \| D_3. I have not investigated this.

### D8 / D9
* **Spot check of the flat-kick table at p = 101.** Exact θ-quadrature with literal matrices, J0, a = 1, η = 2 (`logs/d8_spot.log`):
  * K = 1: 100(E − E_LC) = +370.5, −369.1, +68.1, +4616.8, −95.1 (m = 3..7). The report's MC gives +371 ± 3, −368 ± 3, +71 ± 7, +4598 ± 21, −94 ± 7.
  * K = 2 (Q = 64²): −115.9, −308.4, −222.1, −84.2, +498.7, against −111 ± 3, −308 ± 3, −219 ± 5, −84 ± 7, +489 ± 14. A Q = 96² convergence run is in `logs/d8_spot.log` if it finished.
  * E_LC is taken from Line C's engine values (`linec_exact_values.json`). m = 3 is checked against 6 − 9/p + 4/p².
* **diag7.** K_eff = 1.0377 and R(η = 2, p = 101) = 0.3932 ✔, computed from Line C's mode list.
* **Wording.**
  * "R-collapse" rests on two primes, 211 and 401.
  * R is derived from the **G** pair weight but applied to **J0** data.
  * "K_* ∝ p^{2/3}" is equivalent to "the threshold sits at fixed R", by the definition of R.
  * R_* ≈ 1.2–1.6 is the point where deviations fall below MC error at S ≤ 10⁵, so it depends on S.
  * D9's χ² is over m = 3..202 and dominated by large m, where D1–D6 (fixed m) do not apply. "Explained" must become "consistent with".

## 2. Lean (`Bgs.LineDCerts`)
* **Isolated copy.** I copied `/workspace/bgs-build/formalization` (sources plus `.lake/packages`) to `lean_build/` and added `lean/LineDCerts.lean` (sha256 d8258815…, identical to `build/Bgs/LineDCerts.lean`).
* **Cache.** `lake exe cache get` completed ("Decompressed 8689 already-cached file(s)"). No Mathlib source build.
* **Build.** `lake build Bgs.LineDCerts` gave "Built Bgs.LineDCerts (49s)" and "Build completed successfully" (`logs/lean_build.log`).
* **Axioms.**
  * `hx_ok`, `fix_count`, `D_values`, `hx_control` and `fix_control`: none.
  * `rad_count`, `coll4_ok`, `coll6_ok`, `rad_control` and `coll_control`: {propext} (`logs/lean_build.log`, `logs/axioms_extra.log`).
* **Grep.** No `sorry`, `native_decide`, `admit`, `axiom`, `implemented_by`, `extern`, `unsafe` or `opaque`. No imports (Lean core).
  * The mathlib package shows "local changes" (deleted bench scripts in the copied package). This is irrelevant, because the module imports nothing.
* **What the statements mean.**
  * `hx_ok`: HX = D·I with D := 2(x_m − 1). That is enough for H⁻¹ ≡ D̄X (mod p). It does not show det H = D; that is the classical product formula.
  * `fix_count`: counts T-periodic points in (Z/d₂)². Together with the outside fact \|Fix(T^m)\| = D_m, this shows all of Fix lies in d₂-torsion.
  * `rad_count`: \|ker(H mod 4)\|. Its identification with D/D_eff is Line B Prop R.
  * `coll4_ok`/`coll6_ok`: only that each listed sequence is a genuine period-m orbit mod d₂ with a half-turn-invariant multiset, and that the list has length 26. They do **not** certify that these are on the support, pairwise Γ-inequivalent, or the complete K = 1 collision set.
  * I checked those three facts in Python (`logs/lean_semantics.log`): all are on the support, 2/2 and 26/26 are distinct Γ-classes, and they equal the set of support Γ-classes with S₁ = 0. The report's §8 table should say "listed sequences are orbits and half-turn invariant; completeness/Γ-distinctness [N]".

## 3. Literature and novelty
* **Boasman & Keating 1995** (Proc. R. Soc. A 449, 629): an exact, absolutely convergent expansion of tr Uⁿ over **unperturbed** cat-map fixed points via Fourier expansion of the kick. That is the D1/D3 mechanism. Line B already states "the mechanism … and the unperturbed-orbit form … are prior art. We do not claim them". Line D must say the same. D1 as stated is Line B Thm 1 applied at each θ.
* **BGS-TRACE-133/129** already record the phase-averaged Kluyver/J0 orbit-pair sum as standard and not new.
* **Line B Thm 4**: B_m = B_m^sym under ND_m, with the same B^sym values. D4 is its quenched-ensemble analogue. What is new is pointwise-in-residue convergence without a ν- or Bohr-average, and the separation condition is via P_𝒦 rather than ND_m.
* **Keating 1991.** "The cat maps: quantum mechanics and classical motion", Nonlinearity 4, **309–341** (verified). The report's "309/335" is a mis-citation. The companion paper is "Asymptotic properties of the periodic orbits of the cat maps", Nonlinearity 4, 277–307 (from memory; check). Keating's exact Gauss-sum trace formulas are the source of the arithmetic N-dependence.
* **Kurlberg–Rudnick** (Duke 2000; CMP 2001): Hecke symmetries. The report's claim that Hecke degeneracies "reappear as the p mod g' dependence … and as B^sym" is loose. The p mod g' dependence comes from the Pell-form Gauss sum, and the B^sym deficit comes from Γ-stabilisers (symmetric and repeated orbits). Neither is a Hecke statement. Reword or drop.
* **Keating–Mezzadri 2000** (pseudo-symmetries) and **Degli Esposti–Winn 2005** (J. Phys. A 38, 5895, "The quantum perturbed cat map and symmetry": N-dependent symmetries of *perturbed* cat maps that change the statistics along a positive-density set of N). These are the closest prior statements that arithmetic N-dependence survives perturbation. Degli Esposti–Winn is **not cited** and should be.
* **Nonnenmacher 2003** (Nonlinearity 16, 1685): noisy cat maps. That is annealed, independent noise at each step, i.e. a quantum channel. Here the kick is quenched across the m steps. The setting is related but not the same; worth a sentence.
* **Gnutzmann–Seif 2004** (PRE 69, 056219/056220), Tanner 2001, Berkolaiko–Keating 1999, Gnutzmann–Altland, Pluhař–Weidenmüller: all concern the maximal (site-diagonal) ensemble, i.e. Line C. They bear only on D7. D7 adds nothing beyond Line C except the exponentially small band-limited correction.
* **Bogomolny–Keating 1996** (PRL 77, 1472) and Bogomolny et al., "Arithmetical chaos" (Phys. Rep. 1997): background for off-diagonal and arithmetic degeneracies. No overlap with D4–D6.
* **Searches.** I found no paper computing E_θ\|Tr U^m\|² exactly for a fixed finite random mode set on a cat map, nor the D4/D6 statements.
* **Honest novelty statement:**
  * new are the explicit residue-indexed function Ψ_m for quenched few-mode random kicks;
  * its strong-kick limit B^sym at every residue under P_𝒦-separation (D4);
  * the vanishing of the Γ-diagonal part of c₁ and its decay for the Gaussian ensemble (D6);
  * the full-band transfer lemma (D7).
  
  The exact trace identity (D1), its orbit form (D3) and the J0 average are not new.

## 4. Exact fixes required (to be applied to their REPORT.md and any repo text)
1. **D1:** replace "real-analytic" with "C^∞ (in fact, all derivatives are given by absolutely convergent series)". Replace the evenness argument by the V → −V (θ_k → θ_k + π / c → −c) argument. Add "valid for every odd N with gcd(N, D_m) = 1 (Line B Thm 1 applied for each θ)". Cite Boasman–Keating §5 and BGS-TRACE-133 as prior art for the mechanism and the average.
2. **D2:** change "reduction of the period from D_m to g'_m [N]" to [P] with the one-line proof (all A(n) are multiples of D/g'). Add "g'_m is an upper bound on the period". Add "the O(p⁻²) constant depends on (m,𝒦,a,η) and is not uniform in η or K; the limits p → ∞ and η → ∞ do not commute". Label "η²(Σk²a_k²)m ≪ p" as [C].
3. **D3:** upgrade "support does not depend on s [N]" and "Rad … [P-sketch]" to [P], citing Line B Prop R or the argument in §1 above. Replace "these are the period-m orbits of S" with "period-m solutions of the q-recurrence (same count D_m as Fix S^m)".
4. **D4:** add "a_k ≠ 0 for k ∈ 𝒦". Replace "Hence the exact leading term equals 2m for no finite m and no fixed 𝒦" with "lim_{η→∞} Ψ_m = B_m^sym < 2m (strict inequality proved for odd m, verified for m ≤ 9); at finite η, Ψ_m(t*) is residue-dependent and can take any value in a range containing 2m". Label the values [N/exact rational, m ≤ 7].
5. **D5:** change the summary row to "multisets [P]; Γ-classes for m ≤ 7 [computer-assisted, exact integer check]". Replace "exactly when 𝒦 fails to separate" with "only if 𝒦 fails to separate (necessary, not sufficient: m = 4, K = 1 is non-separating but residue-independent)". State that the K = 1 gaps (0.247 …) are over all of Fix_m; on the support m = 3 gives 0.753.
6. **D6:** "b real and quadratic in η" becomes "b real, polynomial of degree 4 in η". "\|b\| = O(η²)" becomes "O(η⁴)". Restrict (b) and the §5 sentence "it tends to 0 (separating)" to the **G ensemble**, and add "for uniform phases (J0), c₁ does not tend to 0 (it grows roughly like η^{3/2} at m = 3, K = 1)". Replace "never reproduces −2m²" with "is odd under p ↦ −p (mod g'_m), so it cannot equal −2m² uniformly in p". Mark "𝒦 ⊇ {1..m} unconditionally" as needing the m ≤ 7 computer check.
7. **D7:** "literally i.i.d." becomes "i.i.d. up to a global phase that cancels in \|Tr U^m\|²". Add Line C's hypothesis (p > 4^m prime, BGS-TRACE-146) to the transfer statement.
8. **D8/D9:** state "two primes (211, 401) collapse; p = 101 does not". State "R is derived from the G weight; data are J0". State "K_* ∝ p^{2/3} is the definition of fixed R, and R_* is precision-dependent". D9: "consistent with", not "explained"; note that the χ² is dominated by m ≫ 1, outside D1–D6.
9. **Lean §8:** coll4/coll6 certify orbit plus half-turn invariance of the listed sequences only.
10. **Literature:** fix the Keating 1991 citation. Add Degli Esposti–Winn 2005, Line B Thm 1/Thm 4/Prop R and BGS-TRACE-126/129/133. Remove the Hecke attribution. Replace "D1–D6 appear new" with the honest statement in §3.

## 5. Non-claims that must appear verbatim in any repo text
* "This does not prove BGS-TRACE-005 or BGS-BGS-001, and it says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m."
* "The exact trace identity (D1) and its orbit form (D3) are the Boasman–Keating mechanism and Line B Theorem 1 applied for each kick realisation; they are not claimed as new."
* "All regime-I statements are iterated limits, p → ∞ first at fixed (m, 𝒦, a, η), then η → ∞; the O(p^{-2}) remainder is not uniform in η or K."
* "The strong-kick value B_m^sym is reached only under P_𝒦-separation of dihedral classes, which is verified by computer for m ≤ 7, not proved for general m."
* "At finite η the leading term Ψ_m(t*) depends on p mod g'_m and is not 2m; the COE value 2m is not obtained at any fixed m in this model."
* "The decay c₁ → 0 is proved only for the Gaussian ensemble with separating 𝒦; for uniform phases c₁ is not shown to vanish and numerically grows with η."
* "The full-band result D7 is only a transfer of Line C (BGS-TRACE-146), not a new COE theorem."
* "The R-scaling, the K_* ∝ p^{2/3} law and the threshold R_* are numerical/heuristic (two to three primes, Monte Carlo) and depend on the Monte Carlo precision."
* "The account of Line C's χ²/dof ≈ 967 is qualitative and numerical; it is not derived from D1–D6, which concern fixed m."
* "Lean certifies only finite arithmetic facts (H_mX_m = D_mI, orbit counts, \|ker(H_m mod 4)\|, and that listed sequences are half-turn-invariant orbits); no analytic statement of Line D is formalised."
* "Intermediate band K = κp is a sketch only."

## 6. Recommended registry states (BGS conventions)

| Claim | State |
|---|---|
| D1 (with fixes; corollary of Line B Thm 1) | **proved** |
| D2 expansion and period g' (fixed (m,𝒦,a,η)) | **proved** |
| D3 orbit-pair formula and support structure | **proved** |
| D4 implication "Γ-separation ⇒ lim = B^sym for every residue" | **proved** |
| D4 instances m = 3..7 (values, separation for 𝒦 ⊇ {1,2} / {1..m}) | **verification-pending** (computer-assisted) |
| B^sym < 2m for all m | proved for odd m (argument in §1) / **open** for even m beyond the computed range |
| D5(a) multiset separation; D5(b) | **proved** |
| D5(a) Γ-part (m ≤ 7), D5(c) | **verification-pending** |
| D6(a) | **proved** |
| D6(b) (G ensemble, separating 𝒦, b = O(η⁴)) | **conditional** (on Γ-separation; unconditional for m ≤ 7 once D5 is promoted) |
| D6 for the J0 ensemble at large η | **open** (numerically c₁ grows) |
| D7 | **proved** (transfer from BGS-TRACE-146) |
| K = κp | **open** (sketch) |
| D8 | **open** (conjecture), numerics recorded |
| D9 | numerical record only, not a claim |
| Lean `Bgs.LineDCerts` | proved, finite certificates as described |

## 7. Reproduce (from `code/`, with `../venv/bin/python`)
`core.py` (engine) · `structure.py m [1|0]` (support, B^sym, multiset/Γ, collisions) · `d1_check.py` (pathwise D1) · `psi_check.py` (E vs Ψ(t_p), orbit formula, c₁) · `run_d4.py`, `m6_k1.py`, `extra.py` (limits, thresholds, non-commuting limits) · `d4_d6.py`, `c1_validate.py`, `run_c1.py`, `c1_j0.py` (D6) · `d7_check.py` · `d8_spot.py` · `lean_semantics.py`. Lean: `cd lean_build && lake build Bgs.LineDCerts`.
