> **Packet copy (Line B, IDs BGS-TRACE-163 to 182).** On main at 502af245 the highest TRACE id is BGS-TRACE-162, so 163 is the next free id; the block was not renumbered. This is the detailed phase report cited by `../derandomized_fixed_kick.md`, copied unchanged below this box. Its status labels ([P], [P-sketch], [N], [C], [Cert], [L], [H]) are the working labels; the **integration status of every claim is the one in `../derandomized_fixed_kick.md` and `record/claims.json`**, which follow the referee's table (audit §8.10) with the second-reader upgrades of 167, 169 and 173 (`computations/verification/lineB/second_reader/SECOND_READER_REPORT.md`). Path map: `code/`, `logs/` → `computations/verification/lineB/phase1/`, `…/phase1/logs/`; `lean/DerandChecks.lean` → `formalization/Bgs/LineBDerand.lean` (namespace `Bgs.LineB.Derand`).

# BGS derandomization for the fixed-kick perturbed cat map

**Model.** U_N = exp(iτN·A_N)·M_N. S = [[3,4],[2,3]], N odd, A_N is the fixed 32-mode Weyl kick, τ = 1e-80.
**Status.** Executor report, 2026-10-29. Nothing was pushed to GitHub. The private repo was only read, via MCP.

Labels used throughout:
- **[P]** proved in this report, with a complete argument.
- **[P+L]** proved, with the finite instances also kernel-checked in Lean 4 using `decide`.
- **[N]** numerical evidence only, with deterministic logs.
- **[C]** conjecture.
- **[S]** sketch: the argument is outlined but not written out in full.

---------------------------------------------------------------------------------------------------

> **Referee revision (2026-10-29).** This version incorporates the independent referee's fix list (/workspace/audit/derand/REPORT.md §6). The changes are marked "[ref-fix]". The core mathematics is unchanged. Phase-2/3 results are in phase2/REPORT2.md and phase3/REPORT3.md.

## 0. Summary of results

The fixed system really does supply its own averaging. Three findings, with honest scope:

1. **Exact Pell–norm trace formula [P].** [ref-fix: Lean certifies only H_mX_m = D_mI and the tables, not the formula]
   - Scope: the diagonal (l = 0) part of the kick, i.e. any fixed real trigonometric f, with g = e^{iηf}.
   - Formula: for every odd N with gcd(N, D_m) = 1,
     Tr(K_η M)^m = Tr M^m · Σ_{n∈Z^m} Φ̂(n) · e(Q(n)/N) · e(−ν_N · y′_m · Nm(α_n)/g′_m),
     where ν_N = N⁻¹ mod g′_m and α_n = Σ n_j λ^j ∈ Z[λ], λ = 3+2√2.
   - Consequence: the large-N limit is an explicit function Z_m(ν_N; η) of the residue N⁻¹ mod g′_m, with an explicit O(1/N) error.

2. **Route (b), pointwise self-averaging in one N, is false [P].** |Tr U_N^m|² does not converge as N → ∞. Asymptotically it is a non-constant function of N⁻¹ mod g′_m. The correct derandomized statement is distributional.

3. **Routes (a) and (c) combined give the COE diagonal-approximation value for the fixed kick (conditional on ND_m; see [ref-fix] below).**
   - **Theorem 2 [P]:** the N-average equals avg over ν, i.e. F_m(η), a finite positive-definite trigonometric polynomial.
   - **Theorem 4 [P]:** its η-Bohr mean B_m satisfies 0 ≤ 2m − B_m ≤ 224 m² D_m^{−1/2} under the explicit, finitely checkable non-degeneracy condition ND_m. ND_m is verified for m ≤ 9 except m = 6 [N]. The referee confirms it exactly (cyclotomic equality test) for m ≤ 8; m = 9 rests on float clustering with gap/spread ≈ 8e4 [ref-fix]. At m = 6 two exact torsion coincidences of f occur and are identified exactly; B_9 = 17.9418 vs 2m = 18.
   - **Theorem 5 [P]:** for the physical coupling η = τN, the N-average over a window D_eff/(δ_m τ) ≪ X ≪ τ^{−1−1/(m+1)} performs the η-average automatically, and the result is B_m. With our crude error bounds and τ = 1e-80, this rigorous window is non-empty only for m ≤ 6 (§8).
   - [ref-fix] The value 2m is the COE *diagonal-approximation* value 2τ at τ = m/N → 0 for fixed m, below the Ehrenfest time; nothing is shown at τ = O(1). The 2m law is conditional on ND_m for every m (verified exactly for m ≤ 8 by the referee and by float clustering at m = 9, m ≠ 6; bounded unconditionally by phase-2 Theorem N for NSW-prime m; the bound 8m²N_m/h_m is < 1 only from m = 29 on; B_7 = B_7^sym holds by the exact ND check [ref23-fix]). Unconditionally rigorous: B_m^sym → 2m, and B_m = B_m^sym for the checked m. Time reversal holds for every real position kick (M_N is symmetric, so Uᵀ = K⁻¹UK). Non-parity only removes the extra unitary parity symmetry (the 4m = 2×COE case). Two related cases:
     - A parity-symmetric (real) kick gives 4m, i.e. 2×COE [N].
     - The full kick, with l = ±1 time-reversal breaking, is conjectured to give m (CUE) [C].

**Scaling.** η = τN is the effective coupling. τ = 1e-80 gives three regimes:

| Regime | Description |
|---|---|
| N ≪ 1e80 | Arithmetic; F ≈ 1 |
| 1e80 ≲ N ≲ 1e80·τ^{−1/(m+1)} (truth probably up to ~1e160) | Linear-response "Pell regime", where the theorems apply |
| N ≳ 1e160 | Nonlinear map; true BGS regime. Not reached. |

**Not achieved (open):**
- the fixed-η limit without the η-average;
- a proof of ND_m for all m;
- the full non-diagonal kick (CUE);
- Heisenberg-time scales, m ~ N. There is an Ehrenfest barrier m ≲ 2 log_λ N.

---------------------------------------------------------------------------------------------------

## 1. Conventions

**Map and quantization.**
- Position basis x ∈ Z_N, N odd, e_N(t) = e^{2πit/N}, e(t) = e^{2πit}, and 8̄ = 8⁻¹ mod N.
- M_N(x,y) = N^{−1/2} e_N(−8̄(3x² − 2xy + 3y²)). Possible global unimodular constants are irrelevant, because only |Tr M^m| = 1 enters.

**Diagonal kick.**
- The l = 0 Weyl modes of A_N act as multiplication by f(x/N), with f(q) = Σ_k c_k e(kq) real.
- The exact rational c_k come from the audit file audit46_core.py:
  - c_{±7} = 9/20;
  - c_{±1} = 1/20 ∓ i/200;
  - c_{±8}, c_{±6} = −1/40 ∓ (±)i/400;
  - plus terms of size 1/400 and 1/800;
  - 14 nonzero coefficients in total, |k| ≤ 9 (logs/exact_torsion.log).
- K_η = diag(g(x/N)) with g = e^{iηf}, and U^diag_N = K_η M_N with η = τN.
- ĝ(n) are the continuum Fourier coefficients of g: g(q) = Σ ĝ(n) e(nq), absolutely convergent.
- s0 = Σ|ĝ|, s2 = Σ n²|ĝ|. Φ̂(n) = Π_j ĝ(n_j).

**Trace kernel.** Σ_j (3x_j² − 2x_j x_{j+1} + 3x_{j+1}²) = xᵀHx, where H = H_m = 6I − C − Cᵀ is circulant (C the cyclic shift). This gives H₁ = [4] and H₂ = [[6,−2],[−2,6]]. The eigenvalues 6 − 2cos(2πk/m) lie in [4, 8].

**Pell data.**
- S^d = [[x_d, 4y_d], [2y_d, x_d]], with x_{d+1} = 3x_d + 8y_d and y_{d+1} = x_d + 3y_d.
- λ^d = x_d + 2√2 y_d, and x² − 8y² = 1.
- D_m := det H_m = Tr S^m − 2 = 2(x_m − 1) = |det(S^m − I)|.
- y_m/(x_m − 1) = y′_m/g′_m in lowest terms.
- O = Z[λ] = Z[2√2], with Nm(a + bλ) = a² + 6ab + b².
- V_m = O/(λ^m − 1)O ≅ Z/d₁ × Z/d₂, with d₁d₂ = D_m, and d₁ = content(λ^m − 1) = gcd of the entries of L^m − I, where L = [[0,−1],[1,6]].

| m | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| D_m | 4 | 32 | 196 | 1152 | 6724 | 39200 | 228484 | 1331712 | 7761796 | 45239072 |
| g′_m | 2 | 8 | 14 | 48 | 82 | 280 | 478 | 1632 | 2786 | 9512 |
| y′_m | 1 | 3 | 5 | 17 | 29 | 99 | 169 | 577 | 985 | 3363 |
| d₁ | 1 | 2 | 7 | 12 | 41 | 70 | 239 | 408 | 1393 | 2378 |

[ref-fix] Lean coverage (lean/DerandChecks.lean): D_m for m ≤ 8 (m ≤ 10 in the referee's audit file `AuditDerandExtra.D_table`); g′, y′, d₁ for m ≤ 10. Closed forms [P+L for m ≤ 20]: D_m = Q_m² for odd m and D_m = 8P_m² for even m, where P and Q are the Pell and companion Pell numbers.

---------------------------------------------------------------------------------------------------

## 2. Lemma Q (exact inverse of the trace kernel) [P+L]

**Lemma Q.** For every m ≥ 1, H_m X_m = D_m I, where
X_m[i][j] = y_m x_{|i−j|} − (D_m/2)·y_{|i−j|}·[i≠j]   (0 ≤ i, j < m).
Equivalently, for n ∈ Z^m:

  2 nᵀ H⁻¹ n = (y′_m/g′_m)·Nm(α_n) + β(n),  where α_n = Σ_j n_j λ^j and β(n) = −2 Σ_{i<j} n_i n_j y_{j−i} ∈ Z.

**Proof.**

*Step 1 (the entries of X depend only on cyclic distance).* Put φ(d) = y_d + y_{m−d}. Since λ^{m−d} = λ^m λ^{−d}, we have y_{m−d} = y_m x_d − x_m y_d. Hence φ(d) = y_m x_d − (x_m − 1) y_d. Since D/2 = x_m − 1, φ(d) is exactly X[i][j] for d = |i−j| ≥ 1. It is also exactly X[i][i] at d = 0, because φ(0) = y_m. Moreover φ(d) = φ(m−d), so X[i][j] depends only on the cyclic distance and X is circulant with symbol φ̃(r) = φ(r), r ∈ Z_m. This is consistent at r = m, since φ(m) = y_m = φ(0).

*Step 2 (H X = D I).* Since λ + λ⁻¹ = 6, every y_d (d ∈ Z, with y_{−d} = −y_d) satisfies 6y_d − y_{d−1} − y_{d+1} = 0, and so does φ. Thus (HX)_{ij} = 6φ̃(r) − φ̃(r−1) − φ̃(r+1), with r = j − i mod m.
- For 1 ≤ r ≤ m−1 this is 0.
- For r = 0 it is 6y_m − 2φ(1) = 6y_m − 2(1 + y_{m−1}). Using y_{m−1} = 3y_m − x_m, this equals 2x_m − 2 = D.
- m = 1, 2 are covered by the same circulant formula (C = I, respectively C = Cᵀ).

*Step 3 (the quadratic-form identity).* 2nᵀH⁻¹n = (2/D) Σ_{i,j} n_i n_j φ(|i−j|) = (2y_m/D) Σ n_i n_j x_{|i−j|} − Σ_{i≠j} n_i n_j y_{|i−j|}.
Now Nm(α_n) = α_n ᾱ_n = Σ_{i,j} n_i n_j λ^{i−j} = Σ n_i n_j x_{|i−j|}, because λ^d + λ^{−d} = 2x_d. Finally 2y_m/D = y′/g′. ∎

**Lean certificate.** `lemmaQ_m` checks H X = D I with integer matrices for m = 1, …, 10 and 12. A control with the sign of the β part flipped is checked to *fail*.
**Exact rational check.** code/verify_exact.py checks the identity for 200 random n for each m ≤ 12: 200/200 pass (logs/verify_exact.log).

**Green's function form.** H⁻¹ is circulant with entries h(d) = (λ^d + λ^{m−d}) / ((λ − λ⁻¹)(λ^m − 1)), and D·h(d) = φ(d).

---------------------------------------------------------------------------------------------------

## 3. Theorem 1: exact Pell–norm trace formula [P]

**Theorem 1.** Let f be real with Σ n²|ĝ(n)| < ∞, for example any real trigonometric polynomial. Let η ∈ R, m ≥ 1, and N odd with gcd(N, D_m) = 1. Put ν = N⁻¹ mod g′_m (well defined, because g′ | D). Then:

(a) Tr(K_η M_N)^m = Tr(M_N^m) · Z_m^{(N)}(η), with
  Z_m^{(N)}(η) = Σ_{n∈Z^m} Φ̂(n) · e(Q(n)/N) · e(−ν y′_m Nm(α_n)/g′_m),
  where Q(n) := 2nᵀH⁻¹n ∈ [0, ‖n‖²/2].

(b) |Tr M_N^m| = 1.

(c) |Z_m^{(N)}(η) − Z_m(ν; η)| ≤ π m s2 s0^{m−1} / N, where
  Z_m(ν; η) := Σ_{n∈Z^m} Φ̂(n) e(−ν y′ Nm(α_n)/g′).

**Proof.**

*Expand the trace.* Tr(KM)^m = Σ_{x∈Z_N^m} Π_j g(x_j/N) M(x_j, x_{j+1}). Insert g(x_j/N) = Σ_{n_j} ĝ(n_j) e_N(n_j x_j); this is absolutely convergent, so the sums may be swapped. This gives
  Tr = N^{−m/2} Σ_n Φ̂(n) G(n),  with G(n) = Σ_{x∈Z_N^m} e_N(a xᵀHx + n·x)  and a = −8̄.

*Gauss sum.* Since N is odd and gcd(det H, N) = 1, the matrix 2aH is invertible mod N. The substitution x ↦ x − (2aH)⁻¹n completes the square and gives
  G(n) = G(0) e_N(−(4a)⁻¹ nᵀH⁻¹n) = G(0) e_N(2 nᵀ H_N⁻¹ n),
because 4a = −4·8̄ = −2̄. Here H_N⁻¹ is the inverse mod N. The standard multidimensional Gauss sum gives |G(0)| = N^{m/2}: diagonalize the form over Z/p^kZ for each p^k ∥ N (p odd, p ∤ D = det H), then multiply over p^k by CRT [ref-fix]. This proves (b), with G(0)N^{−m/2} = Tr M^m (the n = 0 term).

*Reciprocity.* By Lemma Q, 2nᵀH⁻¹n = r(n)/D with r(n) = 2y_m Nm(α_n) + Dβ(n) ∈ Z. So the phase is e(r(n)·D̄_N/N), where D̄_N = D⁻¹ mod N. Reciprocity for coprime D and N gives D̄_N/N + N̄_D/D ≡ 1/(DN) (mod 1). Therefore
  e(r D̄_N/N) = e(r/(DN)) · e(−r N̄_D/D) = e(Q(n)/N) · e(−N̄_D (y′Nm(α_n)/g′ + β(n))).
The β term is an integer and drops out. Since g′ | D, N̄_D ≡ ν mod g′, and y′Nm/g′ only depends on ν mod g′. This proves (a).

*Bounds.* 0 ≤ Q ≤ ‖n‖²/2, because H ≥ 4I. Since |e(t) − 1| ≤ 2π|t|,
  |Z^{(N)} − Z| ≤ Σ_n |Φ̂(n)| π‖n‖²/N = (π/N) Σ_j Σ_n n_j² Π_i |ĝ(n_i)| = π m s2 s0^{m−1}/N. ∎

**Remarks.**
- The theorem is uniform: it holds for every admissible N, not on average.
- Prior art: the Fourier/Gauss-sum step and the expansion over unperturbed orbits are Boasman–Keating 1995, §5, eq. (5.4). What is new here is the closed Pell–norm form of the phase (Lemma Q) and the reduction, via reciprocity, to a single residue ν = N⁻¹ mod g′ with an explicit uniform error.

**Numerics [N].**
- *Exact finite-N formula vs exact quantum traces* (eigenvalues of the N×N matrix): agreement ≤ 1.51e-9 in all 99 cases. These cover m = 1, 2, 3, η ∈ {0.3, 1, 2.5}, and N ∈ {15, 21, 25, 33, 35, 45, 61, 77, 101, 143, 155, 201}, including composite N. See logs/verify_exact.log.
- *Limit Z_m(ν_N) vs quantum* for m ≤ 7, η ≤ 4, N ≤ 1601: logs/verify_thm1.log. At these N the difference is still O(1), because convergence needs N ≫ m·s2; the frequency-7 mode makes s2 large. That is why the rate is checked through the exact sum below.
- *Rate in (c)* (logs/large_N.log; the exact sum is used for N up to 1e7). N·|Z^{(N)} − Z(ν_N)| stays below the proven constant:

| η | m | N·|diff| at N = 1e3 … 1e7 | proven bound |
|---|---|---|---|
| 0.5 | 1 | 87 → 77.28 | 122 |
| 0.5 | 2 | 77 → 78.8 | 382 |
| 0.5 | 3 | 120–190 | 893 |
| 1 | 1 | 199 → 154.6 | 358 |
| 1 | 3 | 210–440 | 4750 |

The rate is exactly O(1/N), as proved.

---------------------------------------------------------------------------------------------------

## 4. Theorem 3: orbit (periodic-orbit) form and the arithmetic kernel [P]

**Well-definedness on V [P].**
- n ↦ α_n induces V ≅ Z^m/HZ^m. Under Z^m ≅ Z[t]/(t^m − 1), H is multiplication by 6 − t − t⁻¹, and Z[t]/(t^m − 1, t² − 6t + 1) = O/(λ^m − 1). The order is |V| = |Nm(λ^m − 1)| = D.
- 𝒬(β) := y′Nm(β)/g′ mod 1 is a well-defined Q/Z-valued quadratic form on V. By Lemma Q, 𝒬(n) ≡ 2nᵀH⁻¹n mod 1, and 2(n + Hk)ᵀH⁻¹(n + Hk) − 2nᵀH⁻¹n = 4kᵀn + 2kᵀHk ∈ Z.
- Its bilinear form is ℬ(n, k) = 4nᵀH⁻¹k mod 1.

**Theorem 3.** Z_m(ν; η) = Σ_{ξ∈G} k_ν(ξ) · e^{iη S(ξ)}, where G = {ξ : Hξ ∈ Z^m}/Z^m, and:
- ξ runs over the D_m periodic q-sequences: ξ ∈ (R/Z)^m with Hξ ∈ Z^m, i.e. ξ_{j+1} + ξ_{j−1} ≡ 6ξ_j. [ref-fix] ξ ↦ (ξ₀, ξ₁) identifies them with Fix(T^m), T = [[0,1],[−1,6]] (the q-sequences of S′ = [[3,1],[8,3]], isogenous to S). |Fix(T^m)| = |Fix(S^m)| = D, but Fix(S^m) ≅ Z/2d₁ × Z/(d₂/2) ≇ Z/d₁ × Z/d₂ ≅ G, and the position-sequence map Fix(S^m) → G is not injective (image 8 of 32 at m = 2). The referee observed for m ≤ 4 that the support 𝒮 lies inside the image of Fix(S^m); this is not proved for all m.
- S(ξ) = Σ_j f(ξ_j) is the Birkhoff sum of f along the orbit, i.e. the first-order action perturbation.
- k_ν(ξ) = D⁻¹ Σ_{β∈V} e(−ν𝒬(β) − ⟨β, ξ⟩).

*Proof.* Group n by its class β ∈ V = Z^m/HZ^m and apply Poisson summation on the coset n₀ + HZ^m. The dual group of V is H⁻¹Z^m/Z^m = {ξ : Hξ ∈ Z^m}, and Σ_{n∈n₀+HZ^m} Φ̂(n) = D⁻¹ Σ_ξ Φ(ξ) e(−⟨n₀, ξ⟩), with Φ(ξ) = Π g(ξ_j) = e^{iηS(ξ)}. This is valid by absolute summability. ∎

So the derandomized form factor is a sum over the periodic q-sequences of the unperturbed linear dynamics (Fix(T^m); on the support these are images of periodic orbits of S for m ≤ 4) [ref-fix], each weighted by its Birkhoff-sum phase, and an arithmetic kernel replaces the random phases.

**Proposition R (structure of the kernel) [P].** Let Rad = V[4] = {k ∈ V : 4k = 0}. Then for every unit ν mod g′:
- |k_ν(ξ)|² ∈ {0, 1/D_eff}, with D_eff = D/|Rad|;
- the support coset 𝒮 ⊂ G ≅ Fix(T^m), of size D_eff, is independent of ν;
- |Rad| = gcd(4, d₁)·gcd(4, d₂) ∈ {4, 8, 16}.

*Proof.*
1. |Σ_β ψ(β)e(−⟨β,ξ⟩)|² = Σ_γ ψ(γ)e(−⟨γ,ξ⟩) Σ_β e(−νℬ(β,γ)), with ψ = e(−ν𝒬). The inner sum is |V|·1[γ ∈ Rad_ν].
2. ℬ takes values in (1/g′)Z/Z and ν is a unit, so Rad_ν = {γ : ℬ(·,γ) ≡ 0} = {γ : 4H⁻¹γ ∈ Z^m} = {γ : 4γ ∈ HZ^m} = V[4].
3. On Rad, 𝒬 is additive and 2𝒬(γ) = ℬ(γ,γ) ≡ 0, so 𝒬|_Rad takes values in {0, ½}. Since g′ is even, ν is odd, so ν𝒬 = 𝒬 on Rad.
4. Hence γ ↦ ψ(γ)e(−⟨γ,ξ⟩) is a character of Rad, independent of ν, and the sum is |Rad| or 0.
5. Therefore |k|² = |V||Rad|/D² or 0. By Parseval, Σ_ξ|k_ν|² = 1, so the support has D_eff points.
6. V ≅ Z/d₁ × Z/d₂ gives |V[4]| = gcd(4,d₁)gcd(4,d₂) ≤ 16. ∎

*Two side facts, proofs supplied by the referee [ref-fix, P]:*
- (a) **g′ is even for all m.** For odd m, y_m is odd and x_m − 1 is even. For even m, x_m ≡ 1 mod 8, so v₂(x_m − 1) = 2 + 2v₂(y_m) > v₂(y_m), using (x−1)(x+1) = 8y².
- (b) **d₁ and d₂ explicitly.**
  - Odd m: λ^m − 1 = h_m·(2ρ^m) with ρ = 1+√2, and 2ρ^m = (2a − 3b) + bλ has content 1. So d₁ = h_m, d₂ = 4h_m, |V[4]| = 4.
  - Even m: λ^m − 1 = P_m·(2√2ρ^m) with content 1. So d₁ = P_m, d₂ = 8P_m, |V[4]| = 4·gcd(4, P_m).

*Checks.*
- [N] logs/t_rad.log: for m ≤ 7 and **all** units ν, the levels of D|k|² are exactly {0, |V[4]|} and the support is ν-independent (max deviation ≤ 5e-16).
- [P+L] `Deff_values`: D/|V[4]| = 1, 4, 49, 72, 1681, 4900, 57121, 83232 (m = 1..8). These are the values found numerically.

**Symmetry [P].** k_ν is invariant under the dihedral group Γ_m = ⟨shift, reversal⟩ of order 2m acting on G ≅ Fix(T^m):
- the shift ξ_j ↦ ξ_{j+1} corresponds to β ↦ λβ, and Nm(λβ) = Nm β;
- the reversal corresponds to Galois conjugation β ↦ β̄.

S(ξ) is also Γ-invariant. These are exactly the "orbit and time-reversed orbit" degeneracies of the semiclassical diagonal approximation. In this model reversal is a symmetry of the *unperturbed* orbits; whether it survives the kick is the question addressed in §7.

---------------------------------------------------------------------------------------------------

## 5. Theorem 2: N-averages (route a) [P]

**Theorem 2.** Fix m, η, and f as in Theorem 1. Let 𝒩_X = {N ∈ (X, 2X] : gcd(N, D_m) = 1}; every such N is odd, because D is even. For every Ψ : C → C that is Lipschitz on the disc |z| ≤ s0^m (which contains all Z^{(N)} and Z) [ref-fix], and with U_N meaning U_N^diag = K_η M_N at fixed η [ref-fix],

  (1/|𝒩_X|) Σ_{N∈𝒩_X} Ψ(Tr U_N^m / Tr M_N^m) = (1/φ(g′)) Σ_{ν∈(Z/g′)^×} Ψ(Z_m(ν; η)) + O(Lip_Ψ·π m s2 s0^{m−1}/X + (D/X)(|Ψ(0)| + Lip_Ψ·√D_eff)) [ref-fix: the D/X term made explicit].

The same holds with N restricted to primes, with error o(1) by the prime number theorem in arithmetic progressions to the fixed modulus D. In particular

  avg_N |Tr U_N^m|² → F_m(η) := avg_ν |Z_m(ν; η)|² = Σ_{ξ,ξ′} K(ξ,ξ′) e^{iη(S(ξ) − S(ξ′))},

with K(ξ,ξ′) = avg_ν k_ν(ξ) conj(k_ν(ξ′)). K is positive semidefinite, ΣK = F_m(0) = 1, K(ξ,ξ) = 1/D_eff on 𝒮, and K is Γ×Γ-invariant.

*Proof.*
- Use Theorem 1(c) for every N, then equidistribution of N mod D among the residues coprime to D: there are φ(D) per block of D consecutive integers.
- Reduction mod D → (Z/g′)^× followed by inversion is a surjective homomorphism with equal fibres.
- |Tr M^m| = 1 by Theorem 1(b). ∎

**Corollary (route b is false) [P, non-constancy by finite floating-point computation with O(1) margin].** [ref-fix] Scope: m ≥ 2 (m = 1 has g′ = 2 and a pointwise limit). The statement holds for all η outside a discrete set: |Z(ν)|² − |Z(ν′)|² is a finite exponential sum in η. It is not established for the physical η = τN. For fixed η, |Tr U_N^m|² − |Z_m(N⁻¹ mod g′; η)|² → 0. So |Tr U_N^m|² has a limit along N → ∞ only if ν ↦ |Z_m(ν)|² is constant on units. It is not: for every m ≥ 2 checked, the normalized fourth moment over ν is M4 = avg_ν|Z|⁴/F² ∈ [1.05, 20.7], mostly 1.3–2.3 (logs/analyze_F_actual.log, crossover.log). A constant |Z| would give M4 = 1 and Var_ν|Z|² = 0, so the spread of |Z_m(ν)|² across ν is of order F_m itself. There is no pointwise RMT law at fixed η; the form factor is not self-averaging in a single N. The right statement is the distribution of Z_m(ν) over ν. Its fourth moment M4 = avg|Z|⁴/(avg|Z|²)² is close to 2, the complex-Gaussian value, at large η for m ≥ 5: the median over η ∈ [100, 1000] is 1.91–1.97 (logs/eta_stats.log) [N]. For m = 3 it is erratic, e.g. 4.62 at η = 1024.

**Numerics for Theorem 2 [N].** logs/n_average_fast_eta*_N*.log compare exact quantum |Tr U_N^m|² for N in [1001,1201) and [3001,3201), m ≤ 5, with |Z_m(N⁻¹ mod g′)|² on the same N. The per-N RMS error falls like 1/N, and the averages match F_m(η) within the finite-sample spread. See §10.

---------------------------------------------------------------------------------------------------

## 6. Theorem 4: η-Bohr mean (route c) and the 2m law [P, conditional on ND_m]

F_m(η) is a finite trigonometric polynomial in η, with frequencies S(ξ) − S(ξ′). Its Bohr mean is

  B_m := lim_T (1/T)∫_0^T F_m = Σ_{ξ,ξ′ : S(ξ)=S(ξ′)} K(ξ,ξ′) = Σ_{S-level sets C} avg_ν |Σ_{ξ∈C} k_ν(ξ)|²  [P].

**Condition ND_m (non-degeneracy).** For ξ, ξ′ ∈ 𝒮: S(ξ) = S(ξ′) implies ξ′ ∈ Γ_m ξ. In words, Birkhoff sums of f separate the dihedral classes of the supported periodic orbits.

**Theorem 4.** (i) Under ND_m,
  B_m = B_m^sym := Σ_ξ |Γξ| K(ξ,ξ) = Σ_{ξ∈𝒮} |Γξ|/D_eff.
(ii) Unconditionally,
  0 ≤ 2m − B_m^sym ≤ 224 m² D_m^{−1/2} = O(m² λ^{−m/2}).
Hence under ND_m, B_m = 2m(1 − O(m λ^{−m/2})). This is the COE diagonal-approximation value 2τ (τ = m/N → 0 at fixed m) [ref-fix], not the RMT form factor at τ = O(1).

*Proof.*
(i) Under ND_m the level sets are Γ-orbits, and K(ξ, gξ) = K(ξ, ξ).

(ii) Write the deficit and bound the weight.
- Σ_ξ K(ξ,ξ) = 1 (Parseval) and |Γξ| ≤ 2m, so 2m − B^sym = Σ_ξ (2m − |Γξ|) K(ξ,ξ) ≤ 2m · #{ξ with nontrivial stabilizer}/D_eff, with D_eff ≥ D/16 by Prop. R.

Then count the points with nontrivial stabilizer:
- *Rotations* (m − 1 of them). The shift by k fixes exactly the D_{gcd(k,m)} orbits of period dividing gcd(k,m). D_d ≤ D_{⌊m/2⌋} ≤ √D_m, since λ^{m/2} + λ^{−m/2} − 2 ≤ λ^{m/2} − λ^{−m/2}.
- *Reflections* (m of them). In coordinates (ξ_c, ξ_{c+1}) ∈ G = A⁻¹Z²/Z², with A = T^m − I and T = [[0,1],[−1,6]], a reflection is fixed iff a single linear condition ℓ·(ξ_c, ξ_{c+1}) ≡ 0 holds:
  - ℓ = (−1, 1) when the reflection swaps c and c+1;
  - ℓ = (−6, 2) when it fixes c, since ξ_{c+1} = ξ_{c−1} = 6ξ_c − ξ_{c+1}.
  - G ⊇ (1/d₁)Z²/Z² because d₁ | A. On this subgroup ℓ· has image of order ≥ d₁/content(ℓ) ≥ d₁/2, so |Fix| ≤ 2|G|/d₁ = 2d₂.
- *Bounding d₂.* With ρ = 1 + √2:
  - for odd m, λ^m − 1 = ρ^m·Q_m and Q_m = 2h_m, so h_m | content(λ^m − 1) = d₁ and D = Q_m² = 4h_m², giving d₂ ≤ 4h_m = 2√D;
  - for even m, λ^m − 1 = ρ^m·2√2 P_m, so P_m | d₁ and D = 8P_m², giving d₂ ≤ 8P_m = √(8D).
  - These facts are Lean-checked as `D_closed` and `d1_divisible`. So |Fix| ≤ 2√8·√D for every reflection.
- *Total.* #{nontrivial stabilizer} ≤ (m − 1)√D + m·4√2√D ≤ 7m√D, so 2m − B^sym ≤ 2m · 7m√D · 16/D = 224 m² D^{−1/2}. ∎

**Status of ND_m.**
- **Verified numerically for m ≤ 9 except m = 6 [N].** For m ≤ 8 the check (logs/analyze_B_actual.log) clusters S over 𝒮 with tolerance 1e-9.
  - Within-cluster spread is ≤ 4.4e-15.
  - The minimal gap between clusters is ≥ 2.5e-8 for m = 8, and larger for smaller m. That is ≥ 10⁶ times the float error, so the cluster structure is certain.
  - Every cluster equals one Γ-orbit.
- **m = 6.** There are exactly 2 non-dihedral clusters, explained *exactly* by torsion aliasing of f (logs/exact_torsion.log; code/exact_torsion.py):
  - f ≡ 9/10 on (1/7)Z exactly (the aliased coefficients mod 7 are {0: 9/10});
  - f(1/4) = −f(3/4) = 1/100.
  - Orbits supported on 7-torsion or 4-/8-torsion points therefore collide. The effect is B_6 = 11.1184 vs B_6^sym = 11.1906, a correction of −0.072.
- **m = 9 [N]** (code/analyze_B9.py, logs/analyze_B_actual_m9_tol1e-12.log):
  - ND_9 holds: 108505 clusters, none non-dihedral, B_9 = B_9^sym = 17.941811, deficit 0.058.
  - Spreads: in-cluster ≤ 3.6e-15; minimal inter-cluster gap δ_9 = 2.84e-10, so gap/spread ≈ 8·10⁴.
  - Cautionary note: with the coarser tolerance 1e-9 (logs/analyze_B_actual_m9_tol1e-9.log), two genuinely distinct orbits at distance 2.8e-10 were merged into a spurious "non-dihedral" cluster. The exact B is unchanged by this (17.941811 either way), because the cross term averages to zero over ν.
  - The tolerance has to sit between the float error (~1e-14) and δ_m.
- The non-dihedral-cluster correction method (code/analyze_Bbad.py) was validated on m = 6: it reproduces B_6 = 11.118367 (logs/analyze_Bbad_m6_validation.log). It also confirms that the m = 6 coincidences sit on points of order 7 and 4/28.

**Conjecture ND′ [C].** For each fixed f, non-dihedral coincidences S(ξ) = S(ξ′) occur only for ξ in a bounded torsion subgroup: the points of order dividing a fixed T(f), here T | 2²·7·lcm(…). Their total K-weight is O(D^{−1/2+ε}), so B_m = 2m − O(m² D^{−1/2+ε}) for all m.
- Route to a proof: S(ξ) − S(ξ′) = 0 is a vanishing sum of roots of unity of order dividing the denominators of ξ. Mann's theorem bounds the minimal vanishing sums. The Galois action ξ ↦ aξ (a ∈ (Z/ord)^×) permutes G ≅ Fix(T^m) and multiplies the frequencies, which should force collisions into the torsion that f itself "sees".
- Not done.

**Table of B_m (exact cluster formula, all units ν; logs/analyze_B_actual.log).**

| m | D | D_eff | B_m | B_m^sym | 2m | 2m − B^sym | ND_m |
|---|---|---|---|---|---|---|---|
| 1 | 4 | 1 | 1.000 | 1.000 | 2 | 1.000 | ✓ |
| 2 | 32 | 4 | 1.500 | 1.500 | 4 | 2.500 | ✓ |
| 3 | 196 | 49 | 4.796 | 4.796 | 6 | 1.204 | ✓ |
| 4 | 1152 | 72 | 5.083 | 5.083 | 8 | 2.917 | ✓ |
| 5 | 6724 | 1681 | 9.400 | 9.400 | 10 | 0.600 | ✓ |
| 6 | 39200 | 4900 | 11.118 | 11.191 | 12 | 0.809 | ✗ (2 torsion clusters, explained) |
| 7 | 228484 | 57121 | 13.796 | 13.796 | 14 | 0.204 | ✓ |
| 8 | 1331712 | 83232 | 15.299 | 15.299 | 16 | 0.701 | ✓ |
| 9 | 7761796 | 1940449 | 17.942 | 17.942 | 18 | 0.058 | ✓ |

- The deficits come from short orbits (repetitions of period-d orbits, d | m) and from the self-retracing orbits fixed by reflections. These are the exact counterparts of the known non-generic orbit corrections.
- The proven bound 224m²D^{−1/2} is not sharp. It becomes < 2m only for **m ≥ 8** (12544 m² < D_m) [ref-fix]. The observed deficit is O(1) and decreasing on the odd and even subsequences separately.

**Fluctuations at fixed η [N]** (logs/eta_stats.log, η ∈ [100, 1000]):

| m | std(F)/B | median M4 |
|---|---|---|
| 5 | 0.126 | 1.92 |
| 6 | 0.173 | 1.91 |
| 7 | 0.063 | 1.97 |
| 8 | 0.088 | 1.97 |

F_m(η) concentrates around B_m and Z is close to complex-Gaussian. This is the numerical evidence for the open fixed-η statement.

---------------------------------------------------------------------------------------------------

## 7. Symmetry classification of the derandomized ramp

| kick (l = 0 part) | symmetry | B_m → | status |
|---|---|---|---|
| actual f: complex c_k, c_{−k} = conj(c_k), Im c_k ≠ 0 (f not even) | Γ-classes generic; time reversal of the *orbit sum* present (reversal is a symmetry of S) | 2m (COE) | Theorem 4 [P] given ND_m [N for m ≤ 9, m ≠ 6] |
| f even (real c_k): extra parity ξ ↦ −ξ commutes with everything | degeneracy Γ × {±1} | 4m (2×COE, i.e. two independent COE blocks) | [N]: B = 7.37, 6.89, 17.61, 19.43, 27.18 for m = 3..7 (logs/analyze_B_real.log); proof is the same as Theorem 4 with Γ replaced by Γ × {±1} [S] |
| full kick incl. l = ±1 modes with c(1,k) ≠ c(−1,k) | breaks time reversal | m (CUE) | [C]. A general-kick Theorem 1 (twisted Weyl symbol with a (−1)^{v₁v₂} cocycle; the twisted algebra is commutative on the relevant lattice) is sketched [S] but not completed |

**Crossover (the near-symmetries are why things are slow).**
- The dominant mode c_{±7} = 9/20 is real, and the parity-breaking parts are ~1/200.
- So for moderate η the effective symmetry is 2×COE, and the COE value appears only for η ≫ 1/(parity-breaking strength).
- logs/crossover.log, m = 7: F ≈ 25–38 for η ≈ 2–16, which is the 4m = 28 regime, and F ≈ 13.0–15.5 for η ≥ 64, the 2m = 14 regime. On Cesàro means over [E, 2E]: 25.1 at E = 8, 14.24 at E = 64, 13.89 at E = 512.
- This matches the random-phase project finding of COE at η ≤ 2 (bgs-p1b), and it explains why the time-reversal-breaking parameter 9/160000 is tiny.

---------------------------------------------------------------------------------------------------

## 8. Theorem 5: the physical coupling η = τN [P]

**Theorem 5.** Let η_N = τN and N ∈ 𝒩_X. Then

  |avg_{N∈𝒩_X} |Tr U^diag_N^m|² − B_m| ≤ E₁ + E₂ + E₃ + E₄,

with (C_f carries the factor (‖f′‖₂/(2√3))^{m−1} ≈ 8^{m−1} [ref-fix]):
- E₁ = C_f m (1 + 2τX)^{m+2}/X · (2√D_eff + 1). This is Theorem 1(c), using s0(η) ≤ 1 + η‖f′‖₂/(2√3) and s2(η) ≤ C_f(1 + η)³, by Cauchy–Schwarz against Σn⁻² applied to g′ and g‴, and |Z_m(ν)| ≤ Σ_ξ|k_ν(ξ)| = √D_eff by Prop. R.
- E₂ = 2τD_m·D_eff·m‖f‖_∞ (Riemann sum: η is frozen on blocks of D consecutive N). This uses |∂_η|Z|²| ≤ 2|Z|·m‖f‖∞Σ|k| ≤ 2m‖f‖∞D_eff, since Σ_ξ|k_ν(ξ)| = √D_eff.
- E₃ = 2D_m·D_eff/X (incomplete blocks).
- E₄ = 2D_eff/(τXδ_m) (Bohr error). Here δ_m is the smallest nonzero gap among {S(ξ) : ξ ∈ 𝒮}, and Σ|K| ≤ D_eff is used.

*Proof.*
- On each complete block of D consecutive admissible N, ν_N runs over every unit class equally often.
- So the block average of |Z(ν_N; η_block)|² is exactly F_m(η_block).
- Then sum the four errors above. ∎

**Consequence for τ = 1e-80 (honest).** For fixed m:
- E₁ → 0 needs X ≪ τ^{−(m+2)/(m+1)}, up to constants.
- E₄ → 0 needs X ≫ D_eff/(τδ_m).
- δ_m comes from the logs: 1.8, 8.2e-3, 1.8e-3, 8.6e-5, 4.2e-5, 2.0e-6, 2.5e-8, 2.8e-10 for m = 2..9. It shrinks roughly like the minimal spacing of ~D_eff/2m Poisson points.

| m | log₁₀ lower end D_eff/(τδ_m) | log₁₀ upper end τ^{−(m+2)/(m+1)} | rigorous window |
|---|---|---|---|
| 2 | 80.3 | 106.7 | yes |
| 3 | 83.8 | 100.0 | yes |
| 4 | 84.6 | 96.0 | yes |
| 5 | 87.3 | 93.3 | yes |
| 6 | 88.1 | 91.4 | yes |
| 7 | 90.5 | 90.0 | no |
| 8 | 92.5 | 88.9 | no |
| 9 | 95.8 | 88.0 | no |

[ref-fix] So for m ≤ 6 the N-average of the *actual fixed-τ* diagonal model provably equals B_m (m = 6: the torsion-corrected 11.118) with explicit finite errors. Taking the best X in the window, the error is ≤ 1e-3 for m ≤ 5 (≤ 9e-4) and **≤ 0.15 at m = 6**; "o(1)" is meaningless at fixed τ. The constant C_f hides an m-dependence (‖f′‖₂/2√3)^{m−1} ≈ 8^{m−1}, coming from s0(η) ≤ 1 + η‖f′‖₂/(2√3) raised to the power m − 1. The *distinctness* of the S-classes (δ_m > 0) is certified exactly for m ≤ 8 by the referee's cyclotomic class computation. The numerical value of δ_m is a float with error ~1e-14 ≪ δ_m [ref23-fix]. For m ≥ 7 the window closes **with our bounds**. Both ends are loose:
- the true upper end is about τ⁻² = 1e160, where η²m/N stops being small;
- E₄ uses the crude Σ|K| ≤ D_eff.

Under the heuristic upper end, the window is wide open for every m ≤ 9.
- E₁ is crude; the true constraint is roughly τ²X ≪ 1.
- The window only exists at fixed m. Uniformity in m fails once m ≳ 2 log_λ X; see §9.

---------------------------------------------------------------------------------------------------

## 9. Obstructions and open problems (honest)

1. **Fixed η (no η-average) [open].** One would need F_m(η) → 2m for each fixed large η, i.e. Σ_{ξ≠Γξ′} K(ξ,ξ′)e^{iη(S(ξ)−S(ξ′))} → 0. That is a decorrelation statement for Birkhoff sums of a fixed trigonometric f over the D_eff supported periodic orbits, weighted by the Ramanujan-type kernel K (K involves c_{g′}/φ(g′)). It is equivalent in spirit to equidistribution of (S(ξ))_ξ mod 2π/η, i.e. a CLT/Berry–Esseen statement for cat-map periodic orbits *with arithmetic weights*. Known orbit equidistribution (Bowen; Kurlberg–Rudnick for Hecke-type averages) is not quantitative enough. Numerics: std/B ≈ 0.06–0.17 at m ≤ 8.
2. **ND_m for all m [open].** See Conjecture ND′.
3. **Full kick → CUE [C].** It needs the twisted (l ≠ 0) version of Lemma Q and Theorem 1. The phase becomes a twisted norm form, and the kernel is K on G ≅ Fix(T^m) × (sign data).
4. **Heisenberg time [barrier].** All results are at fixed m with N → ∞, i.e. m/N_H → 0. The Pell structure lives on D_m ≈ λ^m orbits, and the orbit sums become uncontrolled when D_m ≳ N, i.e. m ≳ log_λ N (the Ehrenfest time). Reaching m ~ N, where the form factor shows its RMT shape beyond the ramp, would need off-diagonal (Sieber–Richter-type) orbit-pair correlations. In this arithmetic model those are exactly the non-dihedral coincidences that ND_m excludes. That is the real crux, and it is open.
5. **Composite or non-coprime N.** gcd(N, D_m) > 1 is excluded. Those N have density 1 − φ(D)/D and could be treated by the same Gauss-sum computation with degenerate H; not done.

---------------------------------------------------------------------------------------------------

## 10. Numerics index (all deterministic; python = /workspace/bgs-p1b/venv/bin/python)

| script | checks | log |
|---|---|---|
| code/verify_exact.py | Lemma Q, rational, m ≤ 12 (200/200); exact finite-N formula vs quantum (99 cases, m ≤ 3, N ≤ 201, ≤ 1.51e-9) | logs/verify_exact.log |
| code/verify_thm1.py | limit Z(ν) vs quantum, O(1/N) | logs/verify_thm1.log |
| code/large_N.py | rate N·\|diff\| bounded up to N = 1e7 | logs/large_N.log |
| code/t_kdiag.py, code/t_rad.py | Prop. R: \|k\|² levels, ν-independence, \|Rad\| = \|V[4]\| | logs/t_rad.log |
| code/analyze_F.py | F_m(η), spreads over ν | logs/analyze_F_{actual,real}.log |
| code/analyze_B.py, analyze_B9.py, analyze_Bbad.py | exact Bohr means, ND_m clusters (m ≤ 8; m = 9 with non-dihedral-cluster method; m = 6 validation) | logs/analyze_B_{actual,real}.log, analyze_B_actual_m9_tol1e-12.log, analyze_B_actual_m9_tol1e-9.log, analyze_Bbad_m6_validation.log |
| code/exact_torsion.py | exact rational aliasing of f mod n | logs/exact_torsion.log |
| code/crossover.py, eta_stats.py | 2×COE → COE crossover, fixed-η fluctuations | logs/crossover.log, eta_stats.log |
| code/n_average_fast.py | Theorem 2 with exact quantum traces (matrix products), N ∈ [1001,1201) and [3001,3201) | logs/n_average_fast_eta{0.25,1.0}_N{1000,3000}.log |
| lean/DerandChecks.lean | Lemma Q (m ≤ 10, 12) + failing control; D, g′, y′, d₁; det(L^m − I) = −D; D = Q² / 8P²; h_m, P_m \| d₁; D_eff values | logs/lean_check.log |

**Reproduce.**
- Lean (Lean 4 v4.33.1 project with the Mathlib v4.33.1 cache; the file imports nothing):
  - `cd /workspace/bgs-build/formalization && lake exe cache get && cp /workspace/bgs-derand/lean/DerandChecks.lean Bgs/ && lake build Bgs.DerandChecks`
  - Builds cleanly in about 12 s. Kernel `decide` only, no `native_decide`.
  - `#print axioms` reports "does not depend on any axioms" for every checked theorem (logs/lean_check.log).
- Python: `cd code && $python verify_exact.py` (and likewise for the other scripts).

### Theorem 2 with exact quantum traces (logs/n_average_fast_eta*_N*.log)

The test compares the per-N quantity |Tr U_N^m|² (exact, from N×N matrix products) with the Theorem 1 prediction |Z_m(N⁻¹ mod g′)|² on the *same* N. All odd N in each window with gcd(N, D_m) = 1 are used. ||Tr M^m| − 1| ≤ 4.2e-13 for every N and m (Theorem 1(b)).

| η | m | RMS per-N error, N ≈ 1.1e3 | RMS per-N error, N ≈ 3.1e3 | ratio | avg\|Tr U\|² (N ≈ 3.1e3) | same-sample avg\|Z(ν_N)\|² | F_m(η) |
|---|---|---|---|---|---|---|---|
| 0.25 | 1 | 0.0755 | 0.0256 | 2.95 | 1.0256 | 1.0000 | 1.0000 |
| 0.25 | 2 | 0.0557 | 0.0194 | 2.87 | 1.2315 | 1.2298 | 1.2298 |
| 0.25 | 3 | 0.1527 | 0.0510 | 2.99 | 1.0731 | 1.0235 | 1.0219 |
| 0.25 | 4 | 0.1490 | 0.0530 | 2.81 | 1.7683 | 1.7748 | 1.8319 |
| 0.25 | 5 | 0.1593 | 0.0570 | 2.79 | 2.1537 | 2.1527 | 2.1182 |
| 1.0 | 1 | 0.3855 | 0.1107 | 3.48 | 1.1107 | 1.0000 | 1.0000 |
| 1.0 | 2 | 0.2731 | 0.0938 | 2.91 | 1.8479 | 1.8268 | 1.8268 |
| 1.0 | 3 | 1.3040 | 0.3512 | 3.71 | 1.6410 | 1.3492 | 1.3425 |
| 1.0 | 4 | 0.9477 | 0.3201 | 2.96 | 10.2905 | 10.3482 | 10.5413 |
| 1.0 | 5 | 2.7341 | 1.0541 | 2.59 | 12.2545 | 12.1988 | 11.5209 |

How to read the table:
- The window ratio of N is about 2.8, and the RMS error shrinks by about 2.6–3.7. That is the O(1/N) of Theorem 1(c).
- The remaining gap between the sample average and F_m(η) is a finite-sample effect: there are only 67–100 values of N, so the residues ν_N do not cover each unit class mod g′ uniformly. Theorem 2 needs X ≫ D, and D_5 = 6724 exceeds the window length. The same-sample column shows that the theorem's *pointwise* content holds.
- The large finite-N bias at m = 1, η = 1 (0.11 at N ≈ 3100) is the slow convergence (N ≫ m·s2) caused by the frequency-7 mode.


---------------------------------------------------------------------------------------------------

## 11. Literature and novelty (honest)

**Closest prior work.**
- **Boasman & Keating 1995**, "Semiclassical asymptotics of perturbed cat maps", Proc. R. Soc. Lond. A 449, 629–653, doi:10.1098/rspa.1995.0063. Checked against the paper: its §5, eq. (5.4), is an exact, absolutely convergent expansion of tr Uⁿ over the fixed points of the *unperturbed* cat map. It Fourier-expands the kick (coefficients A(k), Bessel functions for a sine kick) and carries a phase exp(−iπ kᵀC⁻¹k/N) with the real inverse C⁻¹ of the trace kernel. They call it "anti-semiclassical" (§5, eq. (5.5)). **So the mechanism of Theorem 1(a), Fourier expansion plus Gaussian completion, and the unperturbed-orbit form of Theorem 3 are prior art.** We do not claim them. What we add is the arithmetic content:
  - the exact Pell–norm form of C⁻¹ (Lemma Q);
  - reciprocity, which collapses all N-dependence to the residue N⁻¹ mod g′_m plus an explicit O(1/N) term;
  - the resulting limit object Z_m(ν).
- **Keating & Mezzadri 2000** (Nonlinearity 13): pseudo-symmetries of perturbed cat maps (one shear gives COE statistics, two shears give CUE). This is the heuristic precursor of §7.
- **Keating 1991** ("The cat maps: quantum mechanics and classical motion"): exact periodic-orbit trace formula for unperturbed cat maps with Gauss sums.
- **Kurlberg–Rudnick 2000** (Hecke theory); **Kurlberg–Rosenzweig–Rudnick 2007** (N-averages of matrix elements and fluctuations for cat maps). N-averaging as a derandomizing device appears there for *matrix elements*, not for the form factor of a kicked map.
- **Berkolaiko–Schanz–Whitney 2002/03** and **Berkolaiko 2006**: rigorous diagonal/off-diagonal form-factor terms on quantum graphs, with averaging over incommensurate bond lengths. That averaging is the exact analogue of our η-Bohr mean (route c), so route (c) is *not* new as a method.
- **Haake** (*Quantum Signatures of Chaos*): the textbook form-factor/COE–CUE classification. **Faure–Nonnenmacher–De Bièvre 2003**: scarred eigenstates for cat maps; non-RMT behaviour at special N, which is consistent with our non-self-averaging corollary.

**Additional prior art [ref-fix].**
- **Percival–Vivaldi 1987** (Physica D 27, "A linear code for the sawtooth and cat maps") and **Cvitanović–Liang** (J. Phys. A 55 (2022); Chaos 2026, "temporal/spatiotemporal cat"): the q-sequence/Lagrangian coding, the Green's-function inverse of 6I − C − Cᵀ, the Hill determinant |Det H| = |det(1 − S^m)|, and the link to ideals in quadratic orders. The Green's-function form in Lemma Q is standard; only the Pell-norm/g′ packaging is new.
- **Gutkin–Osipov 2016**: coupled cat maps in the same coding.
- **Keppeler–Marklof–Mezzadri 2001** ("Quantum cat maps with spin ½"): the diagonal approximation for perturbed cat maps, assuming no systematic action degeneracies. ND_m is the rigorous version of that assumption.
- **Barra–Gaspard 2000** (J. Stat. Phys.): for a fixed quantum graph the k-flow on the torus is ergodic, so spectral average = phase average. This is the direct precedent for derandomization by an internal parameter (Theorem 5, route c).
- **Kottos–Smilansky 1997/99** and **Berkolaiko–Keating 1999** (star graphs): form factors with averaging over bond lengths.
- **Bogomolny–Keating 1996**: off-diagonal correlations via arithmetic correlations of actions.
- **Keating–Mezzadri 2000** (already cited above).
- Boasman–Keating (5.4), letting N → ∞, already implies the residue-class reduction. Only the explicit modulus g′, the N⁻¹ form and the uniform constant are new.

**What appears new** (not found in the above, nor in /workspace/bgs-lit/LIT_REPORT.md) [ref-fix: items 1–2 toned down]:
(The Fourier/Gauss expansion and the unperturbed-orbit form themselves are Boasman–Keating 1995 and are not claimed.)
1. The explicit Pell–norm *packaging* of the (standard, Percival–Vivaldi/Cvitanović–Liang) Green's-function inverse: 2nᵀH⁻¹n = (y′/g′)Nm(α_n) + β(n), with the dihedral/Galois structure.
2. The *explicit* form of the residue reduction (implicit in Boasman–Keating (5.4) as N → ∞): explicit modulus g′_m, the N⁻¹ dependence and the uniform constant (Theorem 1). Hence the proof that the fixed-kick form factor is *not* self-averaging in N, and its replacement by the distribution over ν.
3. The arithmetic kernel K with |k|² = |V[4]|/D on a ν-independent coset (Prop. R).
4. A rigorous, deterministic, fixed-kick derivation of the COE diagonal-approximation value 2m − O(m²λ^{−m/2}) (2τ at τ = m/N → 0, fixed m) [ref-fix], conditional on an explicit, finitely checkable condition ND_m, together with the physical-τ window (Theorem 5).

**Caveat.** This is a fixed-m (short-time) result. Rigorous diagonal approximations for *averaged* systems exist (graphs), and the deep problem remains the m ~ N regime. We did not duplicate the CUE random-ensemble work of the other group: our CUE item is only a conjecture for the fixed kick.

---------------------------------------------------------------------------------------------------

## 12. Assessment: route to a non-averaged result

- **Within reach.** Proving ND′, the torsion-only coincidences, via the Galois action plus vanishing sums of roots of unity, would make Theorem 4 unconditional for all m with this f. Extending Theorem 1 to the l = ±1 modes would give the CUE value m. Both are concrete algebra.
- **Hard but well posed.** Fixed-η decorrelation of arithmetically weighted Birkhoff sums over G ≅ Fix(T^m) [ref-fix]. (Phase 3 isolates its parity part exactly; see phase3/REPORT3.md.) This is the single missing ingredient for a law in which only N is averaged. A pointwise-in-N law is *false* (Corollary §5).
- **Beyond current methods.** Times of order the Heisenberg time. The Pell/norm structure makes the obstruction explicit: off-diagonal orbit-pair correlations are exactly the non-dihedral level coincidences of Birkhoff sums.
