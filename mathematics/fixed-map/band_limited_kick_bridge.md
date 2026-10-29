<!-- Canonical note for Line D (band-limited random kicks). Registered claim IDs BGS-TRACE-149..162.
The packet marked this block provisional because a Line B packet also starts at 149. On main d6fa6e2a the
highest registered TRACE id was BGS-TRACE-148 (historical gaps 138 and 139 left unused, as in the Line C
numbering), and Line B had not merged, so 149 was the next free id and no renumbering was done.
Path mapping: `code/`, `logs/` below are
`computations/verification/lineD/code|logs`; `referee_replay/` is `computations/verification/lineD/referee_replay`;
`lean/LineDCerts.lean` is `formalization/Bgs/LineDCerts.lean`. -->

# Line D — band-limited random kicks on the quantized cat map (v2, after independent referee audit)

Repository context: `ChurilovMaksim/BGS`, main `d6fa6e2a` (read-only; nothing pushed).
Working tree of the research run: `/workspace/bgs-lineD/` (v1 of this report kept there as `REPORT_v1.md`).
Referee audit: `/workspace/audit/lineD/REPORT.md` (read-only; replay scripts copied into the packet).
Every required fix of audit §4 is applied; the change list is §10.

Labels: **[P]** proved here, **[P-sketch]** outline with a step not written out, **[N]** numerical (exact
arithmetic, quadrature or Monte Carlo, with a log), **[CA]** computer-assisted exact check, **[C]** conjecture /
heuristic. Registry states (BGS conventions) are given in §9.

---------------------------------------------------------------------------------------------------------------------

## 0. Summary

Ensemble. S = [[3,4],[2,3]] (λ = 3+2√2); M_N(x,y) = N^{-1/2} e_N(−8̄(3x²−2xy+3y²)) (the matrix of Lines B/C);
U = exp(iηV_θ)M_N, V_θ(x) = Σ_{k∈𝒦} a_k cos(2πkx/N + θ_k) with a fixed finite mode set 𝒦 (default {1..K}),
a_k ≠ 0, and θ_k i.i.d. uniform ("J0 ensemble") or c_k = a_k e^{iθ_k} replaced by circular complex Gaussians
with E|c_k|² = a_k² ("G ensemble"). H_m = 6I − C − Cᵀ (C the cyclic shift), D_m = det H_m = Tr S^m − 2,
X_m = D_m H_m^{-1} ∈ Z^{m×m}. Γ = dihedral group of order 2m acting on index positions.

| # | statement (scope) | label | registry state (referee) |
|---|---|---|---|
| D1 | For every odd N with gcd(N, D_m) = 1 and every θ: Tr U^m = Tr M_N^m·Σ_n Ĝ_θ(n) e(t_N·2nᵀX_m n), t_N = (D_m^{-1} mod N)/N, \|Tr M_N^m\| = 1; hence E_θ\|Tr U^m\|² = Ψ_m(t_N) with Ψ_m C^∞, even, 1-periodic and independent of N. This is Line B Thm 1 applied for each θ (Boasman–Keating mechanism). | [P] | proved |
| D2 | t_N = t* + 1/(ND_m), t* = −N̄/D_m; E = Ψ_m(t*) + c₁/N + O_{m,𝒦,a,η}(N^{-2}), c₁ = Ψ'_m(t*)/D_m. Ψ_m(t*) depends only on ±N mod g'_m, g'_m = D_m/gcd(D_m, 2X_ii, 4X_ij) (an upper bound on the period). The O(N^{-2}) constant is **not uniform in η or K**. | [P] | proved |
| D3 | Orbit-pair formula over Fix_m = {ξ ∈ (R/Z)^m : H_mξ ∈ Z^m} (period-m solutions of q_{j+1}+q_{j−1} = 6q_j mod 1): Ψ_m(s/D) = Σ_{ξ,ξ'} φ̂_s(ξ) conj φ̂_s(ξ') Π_k ω_k(η(S_k(ξ)−S_k(ξ'))). \|φ̂_s\|² ∈ {0, \|V[4]\|/D_m} with s-independent support. | [P] | proved |
| D4 | If P_𝒦 separates Γ-classes on the support, lim_{η→∞}Ψ_m(t*) = B_m^sym for every residue. B_m^sym < 2m for every odd m [P]; for even m only by enumeration (m ≤ 9). Values m = 3..7 exact rationals. | implication [P]; instances [CA] | proved / verification-pending; even m open |
| D5 | (a) 𝒦 ⊇ {1..m} separates point multisets [P]; multiset ⇒ Γ-class checked exactly for m ≤ 7 [CA]. (b) half-turn invariant orbits collide for odd 𝒦 at even m [P]. (c) K = 1 separates on the support for m = 3, 5, 7 (gaps 0.753, 1.936e-3, 3.685e-5); collisions at m = 4, 6; {1,2} separates for m ≤ 7 [CA]. | [P]/[CA] | proved / verification-pending |
| D6 | (a) The Γ-diagonal part of c₁ vanishes [P]. (b) G ensemble, Γ-separating 𝒦: \|c₁\| ≤ C_m η⁴ e^{−a_min²η²δ²/4} → 0 [P, conditional on separation]. J0 ensemble: c₁ grows numerically (≈ η^{1.5} at m = 3, K = 1) [N]. c₁ is odd under N ↦ −N (mod g'_m), so it is not −2m² uniformly in N [P]. | [P]/[N] | (a) proved; (b) conditional; J0 open |
| D7 | Full band K = (N−1)/2, a_k ≡ a, prime p > 4^m: \|E − E_LineC(p,m)\| ≤ p^m e^{−η²a²p/4} (G), ≤ p^m e^{−βη²a²p} (J0); with BGS-TRACE-146: E = 2m − 2m²/p + O_m(p^{-3/2}) for m ≥ 5. | [P] | proved (transfer from TRACE-146) |
| D7' | K = κN, 0 < κ < ½ | [P-sketch] | open |
| D8 | R-scaling of E − E_LineC and the threshold R_* ≈ 1.6 (K_* ≈ 12, 20, 31 at p = 101, 211, 401 for ηa = 2), J0 data | [C] + [N] | open (conjecture) |
| D9 | Line C's χ²/dof ≈ 967 for its 7-mode kick is **consistent with** an effectively single-mode (K_eff = 1.04, R = 0.39) regime | [N] | numerical record, not a claim |
| Lean | `Bgs.LineDCerts`: H_mX_m = D_mI (m = 3..8), orbit counts (m = 3, 4), \|ker(H_m mod 4)\| (m = 3..6), listed collision sequences are half-turn-invariant orbits; controls | [P] finite | proved (finite certificates only) |

### Non-claims (verbatim, referee audit §5)
* "This does not prove BGS-TRACE-005 or BGS-BGS-001, and it says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m."
* "The exact trace identity (D1) and its orbit form (D3) are the Boasman–Keating mechanism and Line B Theorem 1 applied for each kick realisation; they are not claimed as new."
* "All regime-I statements are iterated limits, p → ∞ first at fixed (m, 𝒦, a, η), then η → ∞; the O(p^{-2}) remainder is not uniform in η or K."
* "The strong-kick value B_m^sym is reached only under P_𝒦-separation of dihedral classes, which is verified by computer for m ≤ 7, not proved for general m."
* "At finite η the leading term Ψ_m(t*) depends on p mod g'_m and is not 2m; the COE value 2m is not obtained at any fixed m in this model."
* "The decay c₁ → 0 is proved only for the Gaussian ensemble with separating 𝒦; for uniform phases c₁ is not shown to vanish and numerically grows with η."
* "The full-band result D7 is only a transfer of Line C (BGS-TRACE-146), not a new COE theorem."
* "The R-scaling, the K_* ∝ p^{2/3} law and the threshold R_* are numerical/heuristic (two to three primes, Monte Carlo) and depend on the Monte Carlo precision."
* "The account of Line C's χ²/dof ≈ 967 is qualitative and numerical; it is not derived from D1–D6, which concern fixed m."
* "Lean certifies only finite arithmetic facts (H_mX_m = D_mI, orbit counts, |ker(H_m mod 4)|, and that listed sequences are half-turn-invariant orbits); no analytic statement of Line D is formalised."
* "Intermediate band K = κp is a sketch only."

Reading note on the fifth non-claim: "is not 2m" means *not 2m in general / not identically*; by continuity in η,
Ψ_m(t*) passes through 2m at isolated (η, residue) values (D4 below), which is not a COE statement.

---------------------------------------------------------------------------------------------------------------------

## 1. Literature placement and novelty

* **Boasman & Keating, Proc. R. Soc. A 449 (1995) 629**, §5: exact, absolutely convergent expansion of tr Uⁿ for
  perturbed cat maps over the fixed points of the *unperturbed* map, via Fourier expansion of the kick. **This is
  the mechanism of D1/D3**, which we do not claim. Line B (Thm 1, Prop R, Thm 4) already states the same prior art.
* **Line B** (`/workspace/bgs-derand/REPORT.md`; Line B packet, provisional IDs from BGS-TRACE-149): Thm 1 is D1 for a
  fixed kick (D1 = Line B Thm 1 applied for each θ), Prop R gives the support structure of D3, Thm 4 gives
  B_m = B_m^sym under ND_m with the same B^sym values. D4 is the quenched-ensemble analogue of Thm 4.
* **BGS-TRACE-133 / 129** record the phase-averaged Kluyver (J0) orbit-pair average as standard; D3's J0 weight is that
  average. **BGS-TRACE-126** is the 16-mode phase-averaged form factor; **BGS-TRACE-143–148** are Line C.
* **Keating, "The cat maps: quantum mechanics and classical motion", Nonlinearity 4 (1991) 309–341** and the companion
  **"Asymptotic properties of the periodic orbits of the cat maps", Nonlinearity 4 (1991) 277–307**
  (doi:10.1088/0951-7715/4/2/005; page range verified on IOPscience and the Bristol repository). Keating's exact
  Gauss-sum trace formulas are the source of the arithmetic N-dependence.
* **Degli Esposti & Winn, "The quantum perturbed cat map and symmetry", J. Phys. A 38 (2005) 5895–5912**
  (doi:10.1088/0305-4470/38/26/005): N-dependent quantum symmetries of *perturbed* cat maps that change the
  statistics on a positive-density set of N. With **Keating & Mezzadri, Nonlinearity 13 (2000) 747**
  (pseudo-symmetries), the closest prior statements that arithmetic N-dependence survives perturbation.
* **Kurlberg–Rudnick (Duke 2000; CMP 2001)**: Hecke symmetries — background only. The p mod g' dependence here comes
  from the Pell-form Gauss sum, and the B^sym deficit from Γ-stabilisers (symmetric/repeated orbits); neither is a
  Hecke statement (v1's attribution removed).
* **Nonnenmacher, Nonlinearity 16 (2003) 1685** (noisy cat maps): annealed noise at each step (a quantum channel);
  here the kick is quenched across the m steps — related, not the same.
* **Kottos–Smilansky, Tanner 2001, Gnutzmann–Seif 2004 (PRE 69, 056219/056220), Berkolaiko–Keating 1999,
  Gnutzmann–Altland 2005, Pluhař–Weidenmüller 2014**: the maximal (site-diagonal) ensemble = Line C; they bear only
  on D7, which adds only the exponentially small band-limited correction.
* **Aleiner–Larkin 1996; Brouwer–Rahav–Tian, PRE 74 (2006) 066208**: off-diagonal correction only after 2τ_E
  (heuristic background for regime II). **Bogomolny–Keating 1996; Bogomolny et al., Phys. Rep. 1997**: background.
* **Demanet–Nguyen 2015; Li–Liao 2021** (super-resolution): the tool needed for D7'.

**Novelty (referee's wording, adopted).** New are the explicit residue-indexed function Ψ_m for quenched few-mode random
kicks; its strong-kick limit B^sym at every residue under P_𝒦-separation (D4); the vanishing of the Γ-diagonal
part of c₁ and its decay for the Gaussian ensemble (D6); the full-band transfer lemma (D7). The exact trace identity
(D1), its orbit form (D3) and the J0 average are not new. No paper found computes E_θ|Tr U^m|² exactly for a fixed
finite random mode set on a cat map (web search; not exhaustive).

---------------------------------------------------------------------------------------------------------------------

## 2. D1 — exact bridge [P]

**Theorem D1.** Let N be odd with gcd(N, D_m) = 1 (no primality is used; D_m is even, so N odd is automatic for
primes p ∤ D_m). For every θ,
Tr U^m = Tr M_N^m · Σ_{n∈Z^m} Ĝ_θ(n) e(t_N A_m(n)), A_m(n) = 2nᵀX_m n, t_N = (D_m^{-1} mod N)/N, |Tr M_N^m| = 1.

*Proof.* Tr U^m = N^{-m/2} Σ_{x∈(Z/N)^m} G^{⊗m}(x) e_N(c xᵀH_m x), c = −8̄ (2 invertible since N odd); the cycle form is
Σ_j(3x_j² − 2x_jx_{j+1} + 3x_{j+1}²) = xᵀH_m x. Expand G^{⊗m}(x) = Σ_n Ĝ(n) e_N(n·x) (absolutely convergent:
Ĝ decays like exp(−c|n| log|n|)). H_m is invertible mod N (gcd(N, D_m) = 1); with u = −4H^{-1}n,
c xᵀHx + n·x = c(x−u)ᵀH(x−u) + 2nᵀH^{-1}n and 2nᵀH^{-1}n ≡ 2D̄ nᵀX_m n. The remaining non-degenerate Gauss sum is
Tr M_N^m, of modulus 1. ∎ This is Line B Thm 1 applied for each θ. When N | D_m the normalisation fails
(referee: |Tr M_7³| = 7, |Tr M_3⁴| = 3).

**Regularity and symmetry.** Ψ_m(t) := E_θ|Σ_n Ĝ_θ(n)e(tA(n))|² = Σ_{n,n'} E[Ĝ(n)conj Ĝ(n')] e(t(A(n)−A(n'))) is
1-periodic (A integer valued) and **C^∞**: all derivatives are absolutely convergent series. (Real-analyticity is
*not* claimed: Ĝ decays only like exp(−c|n|log|n|) while the frequencies are quadratic in n.) **Evenness:**
conj Ĝ_θ(n) is the coefficient of e^{−iηV_θ} at −n; −V_θ = V_{θ+π} (G ensemble: c ↦ −c) and both ensembles are
invariant under this map; A(−n) = A(n). Hence Ψ(−t) = E|conj Σ|² = Ψ(t). Gauss-sum signs/Jacobi symbols enter only
through |Tr M^m|² = 1, so no p mod 4 dependence survives.

*Checks [N].* `logs/verify_exact.log`: pathwise agreement ≤ 4e-14 (m = 3; p = 13, 101, 103, 211), ≤ 7e-8 (m = 4,
truncation). Referee (fresh code, literal matrices): ≤ 1e-12 at 28 (m, p, kick) cases; E_θ = Ψ(t_p) to ≤ 1e-11 at
17 (m, p) pairs (`referee_replay/d1_check.py`, `psi_check.py`).

---------------------------------------------------------------------------------------------------------------------

## 3. D2 — expansion in 1/N and the period g' [P]

**Corollary D2.** Write D_mD̄ = 1 + Nj; then t_N = 1/(ND_m) + j/D_m with j ≡ −N̄ (mod D_m), so t_N ≡ t* + 1/(ND_m),
t* = −N̄/D_m. Taylor: E = Ψ_m(t*) + Ψ'_m(t*)/(ND_m) + R, |R| ≤ sup|Ψ''_m|/(2D_m²N²).
**Period [P].** Let g'_m := D_m / gcd(D_m, 2X_ii, 4X_ij). Every value A(n) = 2nᵀXn = Σ 2X_ii n_i² + Σ_{i<j}4X_ij n_in_j
is a multiple of D_m/g'_m, so e(sA(n)/D_m) depends only on s mod g'_m; hence Ψ_m(t*) depends only on N̄ mod g'_m, and
by evenness only on ±N mod g'_m. g'_m = 14, 48, 82, 280, 478, 1632, 2786 (m = 3..9). **g'_m is an upper bound on the
period**: e.g. for m = 4, K = 1, a = η = 1 the value 4.0578090022 is shared by N ≡ 5, 17, 29 (mod 48).

**Non-uniformity (required caveat).** The remainder constant sup|Ψ''| depends on (m, 𝒦, a, η) and grows with η and K
(the effective frequencies |A(n)| scale like (ηaK)²). **The expansion is not uniform in η or K, and the limits N → ∞
and η → ∞ do not commute.** Counterexample (referee, `referee_replay/extra.py`; m = 3, K = 1, J0, p = 101, residue
s = 163):

| η | exact E | Ψ(t*) | p(E − Ψ(t*)) | c₁ at that residue |
|---|---|---|---|---|
| 1 | 2.9298 | 2.7990 | 13.2 | 13.3 |
| 4 | 3.3477 | 3.4911 | −14.5 | −6.5 |
| 16 | 4.1962 | 3.7953 | +40.5 | −201 |
| 64 | 4.7821 | 4.3689 | +41.7 | −7182 |

At η = 16 the two-term expansion has the wrong sign. The often-quoted regime condition η²(Σk²a_k²)m ≪ N is a
heuristic [C].

*Checks [N].* `logs/regime1_k1_a1.0_eta1.0.log` (J0, K = 1, a = η = 1; exact θ-quadrature at p = 101, 197, 401,
797, 1601): p(E − Ψ(t*)) = 7.137, 7.180, 7.199, 7.208, 7.212 → c₁ = 7.2156 (m = 4), p²(E − Ψ − c₁/p) bounded; m = 5
leading values 5.080, 2.411, 10.856, 3.492, 22.646 vary with p mod 82. Reproduced by the referee.

---------------------------------------------------------------------------------------------------------------------

## 4. D3 — orbit-pair formula and the support of the Gauss weights [P]

**Proposition D3.** Since A(n + H_mk) ≡ A(n) (mod D_m), e(sA(n)/D_m) lives on V = Z^m/H_mZ^m, whose dual is
H_m^{-1}Z^m/Z^m ≅ Fix_m := {ξ ∈ (R/Z)^m : H_mξ ∈ Z^m}. **Fix_m is the set of period-m solutions of the q-recurrence
q_{j+1} + q_{j−1} = 6q_j (mod 1)**, i.e. of T = [[0,1],[−1,6]]; it has D_m elements, the same count as Fix(S^m), but
no bijection with Fix(S^m) is claimed. Poisson summation gives
Σ_n Ĝ(n)e(sA(n)/D) = Σ_{ξ∈Fix_m} φ̂_s(ξ)G^{⊗m}(ξ), φ̂_s(ξ) = D^{-1}Σ_{n∈V} e(2s nᵀH^{-1}n − n·ξ),
and averaging |·|² uses E_θ[G^{⊗m}(ξ) conj G^{⊗m}(ξ')] = Π_k ω_k(η(S_k(ξ) − S_k(ξ'))), S_k(ξ) = Σ_j e(kξ_j), with
ω = J0(a|z|) (uniform θ: the standard Kluyver average, as recorded in BGS-TRACE-133) or exp(−a²|z|²/4) (G). ∎
Σ_ξ φ̂_s(ξ) = 1; φ̂_s is invariant under Γ and parity (phase included).

**Support structure [P]** (Line B Prop R; referee's three-line argument). Put Q(β) = βᵀH^{-1}β, β = β' + γ. Then
|φ̂_s(ξ)|² = D^{-1}Σ_{γ∈V[4]} e(2sQ(γ) − γ·ξ), because Σ_{β'} e(4sγᵀH^{-1}β') = D·1[4H^{-1}γ ∈ Z^m] for s a unit.
On V[4], 2Q(γ) ∈ ½Z, so e(2sQ(γ)) = ±1 depends only on s mod 2 (s is odd); and γ ↦ e(2sQ(γ) − γ·ξ) is a character of
V[4]. Hence |φ̂_s|² ∈ {0, |V[4]|/D} and the support (a coset of the annihilator) does not depend on s. ∎
D_eff = D/|V[4]| = 49, 72, 1681, 4900, 57121 and |Rad| = |V[4]| = |ker(H_m mod 4)| = 4, 16, 4, 8, 4 for m = 3..7
(and 16, 4 for m = 8, 9 [N]); Lean certifies |ker(H_m mod 4)| for m = 3..6.
*Checks [N].* Orbit formula = n-sum to 1e-10–1e-12 (`logs/verify_exact.log` V2; referee `psi_check.log`,
`c1_validate.log`); support facts vs direct φ̂ to 5e-17 (referee `structure_m*.log`).

---------------------------------------------------------------------------------------------------------------------

## 5. D4–D5 — leading term: strong-kick limit, separation, collisions

**Theorem D4 [P] (implication).** Assume a_k ≠ 0 for k ∈ 𝒦 and let P_𝒦(ξ) = (S_k(ξ))_{k∈𝒦}. As η → ∞ every pair
with P_𝒦(ξ) ≠ P_𝒦(ξ') has weight → 0 and every pair with equal P_𝒦 has weight 1, so
lim_{η→∞}Ψ_m(s/D) = Σ_{P_𝒦-classes C}|Σ_{ξ∈C}φ̂_s(ξ)|². If P_𝒦 separates Γ-classes on the support,
lim_{η→∞}Ψ_m = B_m^sym := D_eff^{-1}Σ_{ξ∈supp}|Γξ|, the same for every residue s. ∎

**Values [CA, exact rationals for m ≤ 7]:** B_3^sym = 235/49 = 4.795918, B_4^sym = 61/12 = 5.083333,
B_5^sym = 15801/1681 = 9.399762, B_6^sym = 27417/2450 = 11.190612, B_7^sym = 788019/57121 = 13.795609
(floats: B_8^sym = 15.298683, B_9^sym = 17.941811 [N]); identical to Line B's table.

**Proposition (B^sym < 2m for odd m) [P]** (referee's argument). For odd m, D_eff = a_m² with a_m odd
(ρ^m + (1−√2)^m = 2a_m; D_eff = 49 = 7², 1681 = 41², 57121 = 239²), so the support (Γ-invariant) has odd size. The
reversal acts on it as an involution, so it has a fixed point ξ₀; its stabiliser contains the reversal, so
|Γξ₀| ≤ m. Hence 2m − B_m^sym ≥ m/D_eff > 0. The same counting works whenever 2m ∤ D_eff (true at m = 6). For even m
with 2m | D_eff (m = 4, 8) the inequality rests on enumeration (m ≤ 9); **for general even m it is open.**
(Line B proves 0 ≤ 2m − B_m^sym ≤ 224m²D_m^{-1/2} under ND_m.)

**Correct statement of the corollary (v1's "equals 2m for no finite m and no fixed 𝒦" was false and is withdrawn).**
lim_{η→∞}Ψ_m = B_m^sym < 2m (strict for odd m; verified for m ≤ 9). At finite η, Ψ_m(t*) is residue-dependent and
can take any value in a range containing 2m: Ψ_m is continuous in η, equals 1 at η = 0, and reaches 44.76 > 10 at
m = 5, K = 1, G, η = 2 for some residue — so it equals 2m at some finite η. No parity doubling occurs in the limit.

**Lemma D5.** (a) [P] If 𝒦 ⊇ {1..m}, P_𝒦 gives the power sums of {e(ξ_j)}, hence (Newton) the **multiset**.
Multiset ⇒ Γ-class is a separate fact: checked exactly (integer arithmetic) for m = 3..7, on the support and on all
of Fix_m, by the referee, and in floating point by us (`logs/structure.log`) [CA]. So 𝒦 ⊇ {1..m} separates
Γ-classes for m ≤ 7; for general m this is not proved.
(b) [P] For even m and 𝒦 ⊂ odd integers, a multiset invariant under q ↦ q + ½ has S_k = 0 for odd k
(e(kξ)(1 + (−1)^k) = 0), so all such orbits collide.
(c) [CA] With 𝒦 = {1}: m = 3, 5, 7 separate on the support with minimal gaps **0.753**, 1.936e-3, 3.685e-5
(v1's "0.247" for m = 3 is the gap over **all of Fix_3**, not the support); m = 4 and 6 have one collision group
each (2 and 26 Γ-classes, all half-turn-invariant with S₁ = 0, exactly the Lean lists; 60-digit check,
`logs/collisions.log`). 𝒦 = {1,2} separates for m ≤ 7.
**Residue dependence of the limit.** Non-separation is **necessary, not sufficient**, for residue dependence of
lim_{η→∞}Ψ_m: m = 6, K = 1 gives Ψ_∞ ∈ {10.705923, 11.165914} (residue dependent), while m = 4, K = 1 is
non-separating yet Ψ_∞ = 4.861111 at all 16 residues (< B_4^sym). (v1's "exactly when 𝒦 fails to separate" is withdrawn.)

**Approach to the limit [N]** (`logs/regime1_tables_m{3..7}.log`, `logs/eta_threshold.log`; a_k = 1, grid
η ∈ {¼,…,64} (m = 7: {½,…,32})): smallest grid η with max_s|Ψ_m − B_m^sym| ≤ 1%·2m (all larger grid η also OK):

| m | K=1 G | K=2 G | K=3 G | K=4 G | K=6 G | K=8 G | K=2 J0 | K=4 J0 | K=8 J0 |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 8 | 2 | 2 | 2 | 1 | 1 | 32 | 2 | 1 |
| 4 | never (Ψ_∞ = 4.8611) | 4 | 1 | 1 | 1 | 1 | 64 | 2 | 1 |
| 5 | >64 (gap 1.9e-3) | 16 | 8 | 4 | 2 | 2 | 64 | 4 | 1 |
| 6 | never (collision) | 8 | 8 | 2 | 2 | 1 | >64 | 8 | 2 |
| 7 | >32 (gap 3.7e-5) | >32 | 16 | 8 | 4 | 2 | >32 | 8 | 2 |

Referee reproduced m = 3 (K = 1, G): 8; m = 4 (K = 2): 4; m = 5 (K = 2): 16; m = 5 (K = 4): 4. These are N → ∞
values at fixed η; by D2's non-uniformity they say nothing about a fixed N once η is large. m = 8 tables were
started but not completed and are not reported.

---------------------------------------------------------------------------------------------------------------------

## 6. D6 — the 1/N coefficient

**Formula [P]** (re-derived independently by the referee). c₁ = Ψ'_m(t*)/D_m =
(2/π) Im Σ_{ξ,ξ'} φ̂(ξ) conj φ̂(ξ') E_θ[G^{⊗m}(ξ) conj G^{⊗m}(ξ') β(ξ)],
β(ξ) = iηh₀Σ_i v''(ξ_i) − η² v'(ξ)ᵀH_m^{-1}v'(ξ) (v = V_θ on the circle, h₀ = (H_m^{-1})_ii).
For the G ensemble the expectation is f·b with f = Π_k exp(−a_k²η²|ΔS_k|²/4) and **b real and a polynomial of degree
4 in η** (the tilted mean of c shifts by iσ²ζ with ζ ∝ η, so η²·v'ᵀH^{-1}v' contributes η²·σ⁴η²|ΔS|²; v1 said
"quadratic", which was wrong). Referee measures max|b|/η⁴ → 57, 178, 972 for (m,K) = (3,1), (4,1), (4,2).
Checks [N]: J0 θ-quadrature vs finite-p exact (c₁ = 7.2156 at m = 4); G closed form vs Monte Carlo (m = 5, K = 2,
η = 2: −54.96 vs −55.2 ± 5.5) and vs numerical d/dt of Ψ_G (referee: 1e-5 at η ≤ 1, 6e-3 at η = 2).

**Proposition D6.** (a) [P] The Γ-diagonal part of c₁ vanishes identically: φ̂ is constant on Γ-classes, so
φ̂(ξ)conj φ̂(ξ') = |φ̂(ξ)|² for ξ' ∈ Γξ; G^{⊗m}(ξ') = G^{⊗m}(ξ) and |G| = 1 for both ensembles (V real), so the
expectation is E[β(ξ)], which is real (E v'' = 0, v'ᵀH^{-1}v' real). (Referee: ≤ 1e-12 in every run.)
(b) [P, conditional on Γ-separation] **G ensemble only.** If P_𝒦 separates Γ-classes on the support with gap
δ_𝒦 > 0, every remaining pair has f ≤ exp(−a_min²η²δ_𝒦²/4) and |b| = O(η⁴), so |c₁| ≤ C_m η⁴ e^{−a_min²η²δ_𝒦²/4} → 0.
For 𝒦 ⊇ {1..m} the separation hypothesis holds for m ≤ 7 by the computer check of D5(a) only.
(c) [N] **J0 ensemble (uniform phases): c₁ does not tend to 0.** The tilted moments are Bessel functions decaying
like (η|Δ|)^{-1/2} while β carries η². Referee (`referee_replay/c1_j0.py`, m = 3, K = 1, separating, gap 0.753):
max_s|c₁| = 13.3, 128.7, 682.7, 7182, 85063, 453908 at η = 1, 4, 16, 64, 256, 1024 (roughly η^{1.5}), against
≤ 3e-10 for the G ensemble at η ≥ 16. The J0 large-η behaviour is **open**. This matters for D8, whose data are J0.
(d) [N] Non-separating 𝒦 (G ensemble): collision pairs have f = 1 and b ∝ η², so c₁ grows: m = 4, K = 1:
c₁ = ±0.302η² (η = 16, 32, 64; reproduced by the referee).
(e) [P] **What is proved about −2m².** Ψ' is odd, so c₁(−N mod g'_m) = −c₁(N mod g'_m): c₁ averages to 0 over
residues (checked to 1e-11) and **cannot equal −2m² uniformly in N**. For individual residues and some η, c₁ = −2m²
is not excluded (c₁ varies continuously in η through values like ±246).

Table: max over residues of |c₁| (G ensemble, a_k = 1; `logs/c1_tables.out`, `logs/c1_summary.md`) [N]:

| m | K | η=1 | η=2 | η=4 | η=8 | η=16 | η=32 | η=64 | −2m² |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 1 | 8.7 | 13.3 | 19.1 | 0.506 | 0 | 0 | 0 | -18 |
| 3 | 2 | 27.9 | 12 | 0.0002 | 0 | 0 | 0 | 0 | -18 |
| 3 | 3 | 23.7 | 0.0115 | 0 | 0 | 0 | 0 | 0 | -18 |
| 3 | 4 | 5.05 | 0.0003 | 0 | 0 | 0 | 0 | 0 | -18 |
| 3 | 6 | 0.618 | 0 | 0 | 0 | 0 | 0 | 0 | -18 |
| 4 | 1 | 10.1 | 6.18 | 9.4 | 19.3 | 77.4 | 310 | 1.24e+03 | -32 |
| 4 | 2 | 9.26 | 6.38 | 0.0217 | 0 | 0 | 0 | 0 | -32 |
| 4 | 3 | 1.92 | 0.0001 | 0 | 0 | 0 | 0 | 0 | -32 |
| 4 | 4 | 0.252 | 0 | 0 | 0 | 0 | 0 | 0 | -32 |
| 4 | 6 | 0.0744 | 0 | 0 | 0 | 0 | 0 | 0 | -32 |
| 5 | 1 | 41 | 246 | 180 | 251 | 155 | 206 | 1.16e+03 | -50 |
| 5 | 2 | 170 | 186 | 71.1 | 5.36 | 8.98 | 0.0346 | 0 | -50 |
| 5 | 3 | 131 | 77.4 | 31.3 | 2.09 | 0 | 0 | 0 | -50 |
| 5 | 4 | 97.3 | 45.4 | 4.94 | 0.0002 | 0 | 0 | 0 | -50 |
| 5 | 6 | 101 | 11 | 0.165 | 0 | 0 | 0 | 0 | -50 |
| 6 | 1 | 77 | 107 | 154 | 182 | 373 | 1.37e+03 | 5.65e+03 | -72 |
| 6 | 2 | 139 | 107 | 51.5 | 43.9 | 1 | 0 | 0 | -72 |
| 6 | 3 | 66.5 | 59.5 | 52.5 | 46.6 | 1.14 | 0 | 0 | -72 |
| 6 | 4 | 130 | 36.3 | 2.87 | 0 | 0 | 0 | 0 | -72 |
| 6 | 6 | 109 | 21.2 | 0.0164 | 0 | 0 | 0 | 0 | -72 |

---------------------------------------------------------------------------------------------------------------------

## 7. COE regime: full band (D7), K = κN (D7'), crossover numerics (D8), Line C's 967 (D9)

### 7.1 Regimes (orientation, not claims)
Regime I: fixed 𝒦, N → ∞ (D1–D6). Regime II: smooth chaotic kick below Ehrenfest; by Aleiner–Larkin /
Brouwer–Rahav–Tian no τ² term is expected [C]. Regime III: the kick resolves individual sites (D7, D7', D8).
Resolution parameter, defined from the **G-ensemble** pair weight: a site pair displaced by d sites has weight
exp(−(η²/4)Σ_k a_k²|e(kd/N) − 1|²) ≈ exp(−R²d²), R := πη(Σ_k k²a_k²)^{1/2}/N.

### 7.2 D7 — full band = Line C [P]
**Theorem D7.** Let p > 4^m be prime (the hypothesis of Line C's Theorem 6, BGS-TRACE-146; the bound below holds for
every odd prime), 𝒦 = {1,…,(p−1)/2}, a_k ≡ a. For x, y ∈ (Z/p)^m with occupation vectors N_x, N_y,
E_θ[e^{iη(ΣV(x_j) − ΣV(y_j))}] = Π_k ω(ηa|ΔS_k|), ΔS_k = Σ_z(N_x − N_y)(z)e(kz/p). If N_x = N_y the weight is 1 and these
pairs give exactly E_LineC(p,m). Otherwise Σ_{k=1}^{(p−1)/2}|ΔS_k|² = (p/2)‖N_x − N_y‖² ≥ p (Parseval; zero sum;
‖Δ‖² ≥ 2; symmetric spectrum). G: weight ≤ e^{−η²a²p/4}. J0: arguments ≤ X = 2mηa and |J0(x)| ≤ e^{−βx²} on [0, X],
β = min(0.2, 0.2676/X²), so weight ≤ e^{−βη²a²p}. With Σ_{x,y}|K(x)K(y)| = p^m:
|E − E_LineC| ≤ p^m e^{−η²a²p/4} (G), ≤ p^m e^{−βη²a²p} (J0). With BGS-TRACE-146,
E = 2m − 2m²/p + O_m(p^{-3/2}) for m ≥ 5, p > 4^m. ∎
Remarks. (i) For the G full band the site field is Gaussian with the k = 0 mode missing (a zero-sum constraint): the sites are i.i.d. **up to a global phase that cancels in
|Tr U^m|²** (v1's "literally i.i.d." was wrong; the zero-sum constraint). (ii) For J0 with ηa ≳ 1 the exponent
βη²a²p ≈ 0.067p/m² does not improve with η; the error is exponentially small only for p ≫ m³ log p (vacuous at p = 101).
(iii) This is a transfer of Line C, not a new COE theorem. Checks: referee exact enumeration at p = 5, 7, 11, 13
(m = 3, 4), all 24 cases within both bounds; Line C values 235/49, 631/121, 901/169, 1829/343 reproduced
(`referee_replay/d7_check.py`). (Referee aside, not a claim: B_3^sym = 235/49 = E_LineC(7,3) and 7 | D_3.)

### 7.3 D7' — K = κN, 0 < κ < ½ [P-sketch, open]
The proof of D7 works if min over admissible Δ ≠ 0 (‖Δ‖₁ ≤ 2m, ΣΔ = 0) of Σ_{k≤K}|Δ̂(k)|² grows like a power of N.
This is a smallest-singular-value bound for partial Fourier matrices on the N-th roots of unity; super-resolution
bounds (Demanet–Nguyen; Li–Liao) suggest ≳ κ^{4m−1}N, but adapting them (discrete torus, multiplicities) is not done.

### 7.4 D8 — crossover numerics and a conjecture [C] + [N] (state: open)
Flat ensembles, **J0 (uniform θ)**, a_k = 1, η = 2: exact eigenvalues at p = 101 (S = 20 000, `code/mc_band.py`),
FFT traces at p = 211 (S = 60 000) and p = 401 (S = 100 000) (`code/mc_fast.py`). Deviation from Line C's exact value
E_LineC(p,m), 100·(E − E_LC) ± 100·se, and χ²/dof vs finite-N COE over m = 3..8 (`code/rc_table.py`,
`logs/rc_table.md`, `logs/rcollapse.log`):

| p | K | R | χ²/dof vs COE (m=3..8) | 100(E−E_LC) m=3 | m=4 | m=5 | m=6 | m=7 |
|---|---|---|---|---|---|---|---|---|
| 101 | 1 | 0.06 | 16854.6 | +371±3 | -368±3 | +71±7 | +4598±21 | -94±7 |
| 101 | 2 | 0.14 | 2478.9 | -111±3 | -308±3 | -219±5 | -84±7 | +489±14 |
| 101 | 3 | 0.23 | 501.3 | -170±3 | +17±7 | -136±6 | -35±8 | +45±10 |
| 101 | 4 | 0.34 | 96.6 | +55±6 | +138±8 | +52±7 | +29±9 | +56±10 |
| 211 | 7 | 0.35 | 93.8 | +19±3 | +55±4 | -53±4 | +43±5 | +6±6 |
| 401 | 11 | 0.35 | 111.1 | +9±2 | +53±3 | -33±3 | +44±4 | -1±4 |
| 211 | 10 | 0.58 | 16.4 | -9±3 | +26±3 | -7±4 | +19±5 | -1±6 |
| 101 | 6 | 0.59 | 27.3 | -53±4 | +23±6 | +22±7 | +12±8 | -6±9 |
| 401 | 16 | 0.61 | 21.9 | -9±2 | +26±3 | -2±3 | +2±4 | +5±4 |
| 211 | 13 | 0.85 | 6.0 | -16±2 | +7±3 | -0±4 | -1±5 | -3±6 |
| 101 | 8 | 0.89 | 2.4 | -23±4 | -1±6 | -4±7 | +6±8 | -3±9 |
| 401 | 21 | 0.90 | 4.6 | -6±2 | +10±3 | -2±3 | +3±4 | +1±4 |
| 101 | 10 | 1.22 | 1.1 | -16±4 | -4±6 | -2±7 | +5±8 | -4±9 |
| 401 | 26 | 1.23 | 1.8 | -8±2 | -2±3 | +3±3 | -1±4 | -1±4 |
| 211 | 17 | 1.26 | 3.6 | -13±2 | -1±3 | -3±4 | -9±5 | +3±6 |
| 101 | 12 | 1.59 | 0.9 | +0±4 | -4±6 | +5±7 | +5±8 | -4±9 |
| 211 | 20 | 1.60 | 1.3 | -2±2 | -7±3 | +2±4 | -8±5 | -3±6 |
| 401 | 31 | 1.60 | 0.3 | -3±2 | -1±3 | -3±3 | +0±4 | +1±4 |
| 211 | 26 | 2.34 | 1.6 | -1±2 | -0±3 | +1±4 | +9±5 | +10±6 |
| 101 | 16 | 2.41 | 3.6 | +2±4 | +4±6 | -12±7 | +18±8 | -18±9 |
| 401 | 41 | 2.42 | 0.8 | -1±2 | -2±3 | +2±3 | +1±4 | -4±4 |
| 101 | 20 | 3.33 | 3.5 | +6±4 | +7±6 | +2±7 | -3±8 | +12±9 |
| 101 | 24 | 4.35 | 0.5 | -3±4 | -4±6 | +2±7 | +0±8 | -7±9 |
| 211 | 40 | 4.43 | 1.5 | -4±2 | +5±3 | +3±4 | +4±5 | -0±6 |
| 101 | 32 | 6.65 | 2.3 | -4±4 | +2±6 | -5±7 | -19±8 | +19±10 |
| 101 | 50 | 12.89 | 2.3 | +1±4 | +6±6 | +2±7 | -4±8 | -13±9 |

**Independent spot check (referee, `referee_replay/d8_spot.py`, exact θ-quadrature with literal matrices, p = 101,
J0, a = 1, η = 2):** K = 1 (Q = 128): 100(E − E_LC) = +370.5, −369.1, +68.1, +4616.8, −95.1 (m = 3..7) vs our MC
+371 ± 3, −368 ± 3, +71 ± 7, +4598 ± 21, −94 ± 7; K = 2 (Q = 64²): −115.9, −308.4, −222.1, −84.2, +498.7 vs
−111 ± 3, −308 ± 3, −219 ± 5, −84 ± 7, +489 ± 14. The referee's K = 2 convergence run at Q = 96² finished and equals the Q = 64² values to the printed digits (`referee_replay/logs/d8_spot.log`). Our MC agrees within 1.6σ in every entry.

Observations [N]. At matched R the deviations at **p = 211 and p = 401** agree within MC error (m = 4: 0.55/0.53 at
R ≈ 0.35, 0.26/0.26 at R ≈ 0.6; m = 6: 0.43/0.44 at R ≈ 0.35); **p = 101 does not collapse** onto them (larger, more
arithmetic deviations). At fixed R the deviation is O(1), not O(1/p). Deviations fall below the MC error for
R ≳ 1.6 at all three primes (p = 401, K = 31, R = 1.60: all m = 3..7 within 1.5σ; K = 41, R = 2.42: within 1σ); at
R ≈ 1.2 an m = 3 deviation ≈ −0.08…−0.16 (3–4σ) persists.

**Conjecture D8 [C].** For fixed m, η, a, along K = K(p) with R fixed, lim_{p→∞}E_θ|Tr U^m|² = 2m + F_m(R) exists,
with F_m(R) → 0 as R → ∞; recovering Line C's −2m²/p term needs F_m(R(p)) = o(1/p), i.e. R → ∞.
**Caveats (referee):** (1) the collapse rests on **two primes (211, 401)**; p = 101 does not collapse. (2) R is derived
from the **G-ensemble** pair weight but tested on **J0** data (and D6(c) shows the two ensembles differ at large η).
(3) "K_* ∝ p^{2/3}" is merely a restatement of "the threshold sits at fixed R" (R ∝ K^{3/2}/p); any log factor is
untested. (4) R_* ≈ 1.6 is the point where deviations drop below the Monte Carlo error at S ≤ 10⁵; it depends on S.
With these caveats: K_* ≈ 12, 20, 31 at p = 101, 211, 401 for ηa = 2.

### 7.5 D9 — Line C's χ²/dof ≈ 967 (numerical record; "consistent with", not "explained")
Line C's control kick has 7 modes with one dominant (a_7 = 0.9, others ≤ 0.1): participation K_eff = 1.0377 and
R(η = 2, p = 101) = 0.3932 (both confirmed by the referee). Our reproduction (`logs/mc/diag7_*`, `logs/mc/k7only_*`,
seed 3, S = 20 000): χ²/dof = 1029 over m = 3..202 (Line C: 967), m = 4 value 1.55 (Line C: 1.59); dominant mode
alone 2071; flat K = 1: 1309; flat K = 8: 1.01. The large χ² is **consistent with** an effectively single-mode,
small-R regime in which the fixed-m leading term is arithmetic. It is **not derived** from D1–D6: the χ² runs over
m = 3..202 and is dominated by large m, where the fixed-m results say nothing.

---------------------------------------------------------------------------------------------------------------------

## 8. Lean certificates (`Bgs.LineDCerts`)
Isolated build (`lean_v2_build.sh`): fresh copy of `/workspace/bgs-build/formalization` → `lean_build_v2/`,
`lake exe cache get` first (`logs/lean_v2_cache_get.log`: "Decompressed 8689 already-cached file(s)", exit 0; Mathlib
not built from source), then `lake build Bgs.LineDCerts` (`logs/lean_v2_build.log`): **"Built Bgs.LineDCerts (46s)", "Build completed
successfully", exit 0** (47.7 s wall); the built file is byte-identical to `lean/LineDCerts.lean`
(sha256 aa5178c2…). A file containing
`import Bgs.LineDCerts` compiles with `lake env lean` (exit 0, `logs/lean_v2_import_test.log`).
Kernel `decide` only; Lean core, no imports; grep for sorry / native_decide / admit / implemented_by / extern /
unsafe / opaque / axiom / import is empty (`logs/lean_v2_grep.log`). The referee built the v1 file independently
(49 s, same axioms). Lake warns "mathlib: repository … has local changes" (copied package tree); irrelevant, the
module imports nothing.

| theorem | what it certifies | axioms |
|---|---|---|
| `hx_ok` | H_mX_m = D·I with D := 2(x_m − 1), m = 3..8 (enough for H^{-1} ≡ D̄X mod N; det H_m = D_m is the classical product formula, not certified) | none |
| `D_values` | D_3..D_6 = 196, 1152, 6724, 39200 | none |
| `fix_count` | #T-periodic points in (Z/d₂)² = D_m for (m, d₂) = (3, 28), (4, 96); with \|Fix(T^m)\| = D_m, all of Fix_m lies in d₂-torsion | none |
| `rad_count` | \|ker(H_m mod 4)\| = 4, 16, 4, 8 (m = 3..6); identification with D_m/D_eff is Prop. D3 / Line B Prop R | propext |
| `coll4_ok`, `coll6_ok` | **only** that each listed sequence is a period-m orbit mod d₂ with half-turn-invariant multiset, and the m = 6 list has length 26 | propext |
| `hx_control`, `fix_control`, `rad_control`, `coll_control` | the checkers reject wrong data | none / propext |

**Not certified by Lean** (checked in Python instead): that the listed sequences lie on the support, are pairwise
Γ-inequivalent, and form the complete K = 1 collision set (`code/collisions.py` → `logs/collisions.log`; referee
`referee_replay/lean_semantics.py` → `lean_semantics.log`: on support, 2/2 and 26/26 distinct Γ-classes, equal to
the set of support Γ-classes with S₁ = 0).

---------------------------------------------------------------------------------------------------------------------

## 9. Claims and registry states (IDs confirmed on main d6fa6e2a; follow the referee's table, audit §6)
**Registered IDs BGS-TRACE-149 … 162.** The packet marked this block provisional because Line B's packet also
uses IDs from BGS-TRACE-149. On main d6fa6e2a the highest registered TRACE id was BGS-TRACE-148, so 149 was the
next free id. Line B had not merged, and no renumbering was done. Line B's theorem numbers are cited as prior
art; they are not registered dependency ids.

| ID | content | state |
|---|---|---|
| TRACE-149 | D1 (odd N, gcd(N,D_m) = 1; Ψ_m C^∞, even, periodic) — Line B Thm 1 per θ | proved |
| TRACE-150 | D2 expansion and period bound g'_m (fixed (m,𝒦,a,η); non-uniform in η, K) | proved |
| TRACE-151 | D3 orbit-pair formula and support structure | proved |
| TRACE-152 | D4 implication: Γ-separation ⇒ lim_{η→∞}Ψ_m = B_m^sym at every residue | proved |
| TRACE-153 | D4 instances m = 3..7 (exact B^sym values; separation for {1,2}, {1..m}); D5(a) Γ-part for m ≤ 7; D5(c) | verification-pending (computer-assisted) |
| TRACE-154 | B_m^sym < 2m for every odd m | proved |
| TRACE-155 | B_m^sym < 2m for even m beyond the computed range (m ≤ 9 enumerated) | open |
| TRACE-156 | D5(a) multiset separation (Newton); D5(b) half-turn collisions | proved |
| TRACE-157 | D6(a) Γ-diagonal part of c₁ vanishes; D6(e) oddness of c₁ under N ↦ −N | proved |
| TRACE-158 | D6(b) G ensemble: \|c₁\| ≤ C_mη⁴e^{−a²η²δ²/4} → 0 | conditional (on Γ-separation; unconditional for m ≤ 7 once TRACE-153 is promoted) |
| TRACE-159 | D6(c) J0 ensemble at large η (numerically c₁ grows) | open |
| TRACE-160 | D7 full band = Line C up to p^m e^{−cp} | proved (transfer from BGS-TRACE-146) |
| TRACE-161 | D7' K = κN | open (sketch) |
| TRACE-162 | D8 R-scaling / threshold conjecture, with numerics | open (conjecture) |
| — | D9 (Line C's 967) | numerical record only, not a claim |
| — | Lean `Bgs.LineDCerts` | finite certificates, attached as formalization evidence to TRACE-149/151/153/156 |

---------------------------------------------------------------------------------------------------------------------

## 10. Changes from v1 (referee audit §4, all applied)
1. **D1:** primality dropped; hypothesis "odd N, gcd(N, D_m) = 1" explicit; "real-analytic" → C^∞; evenness via V → −V
   (θ_k → θ_k + π / c → −c); D1 = Line B Thm 1 per θ; Boasman–Keating §5 and BGS-TRACE-133 cited as prior art.
2. **D2:** period reduction g'_m now [P] with the one-line proof; g'_m stated as an upper bound on the period;
   non-uniformity in η and K stated, with the m = 3, p = 101 counterexample (wrong sign at η = 16); regime condition
   labelled [C].
3. **D3:** support facts upgraded to [P] (Line B Prop R / referee argument); Fix_m described as period-m solutions of
   the q-recurrence (same count as Fix S^m, no bijection claimed); Kluyver average credited to TRACE-133.
4. **D4:** hypothesis a_k ≠ 0 added; false corollary "equals 2m for no finite m and no fixed 𝒦" withdrawn and replaced;
   proof of B^sym < 2m for odd m added (even m enumeration-only / open); exact rationals given.
5. **D5:** Newton gives multisets [P]; multiset ⇒ Γ only for m ≤ 7 [CA]; "exactly when 𝒦 fails to separate" replaced
   by "necessary, not sufficient" with the m = 4, K = 1 counterexample; gap 0.753 (support) vs 0.247 (all of Fix_3).
6. **D6:** b has degree 4 in η (bound C_mη⁴e^{…}); decay restricted to the G ensemble; J0 growth reported (referee
   data); "never −2m²" replaced by the oddness statement; separation hypothesis flagged as m ≤ 7 computer check.
7. **D7:** "literally i.i.d." → "i.i.d. up to a global phase that cancels"; hypothesis p > 4^m (BGS-TRACE-146) carried;
   J0 exponent caveat.
8. **D8:** downgraded to conjecture with the four caveats (two primes; G-derived R on J0 data; p^{2/3} = fixed R; R_*
   precision-dependent); referee's exact spot check incorporated (d8_spot finished; Q = 96 equals Q = 64).
9. **D9:** "explained" → "consistent with"; fixed-m results do not cover the χ² range.
10. **Lean:** coll4/coll6 certify only the listed sequences; Python checks cited; docstring updated; rebuilt in an
    isolated copy.
11. **Literature:** Keating 1991 citation fixed (309–341) and companion paper 277–307 verified by web search;
    Degli Esposti–Winn 2005 added; Kurlberg–Rudnick Hecke attribution removed; Boasman–Keating §5 credited; Nonnenmacher
    2003 added; novelty stated in the referee's words. All 11 non-claims included verbatim (§0).

---------------------------------------------------------------------------------------------------------------------

## 11. Reproduce
`venv/bin/python` (numpy 2.5, scipy 1.18, mpmath, sympy); from `code/`: `verify_exact.py` (D1, D3) · `structure.py`
(supports, Γ-classes, B^sym, separation) · `collisions.py 4|6` · `regime1_check.py` (D2) · `regime1_tables.py`,
`eta_threshold.py` (D4) · `c1_tables.py`, `c1_summary.py`, `c1_scan.py` (D6) · `linec_exact.py` (reads Line C engine) ·
`mc_band.py`, `mc_fast.py`, `run_scan.sh`, `run_fast.sh`, `analyze_scan.py`, `analyze_fast.py`, `rc_table.py` (D8, D9).
Referee replay (copied unchanged into the packet under `referee_replay/`): `core.py`, `structure.py`, `d1_check.py`,
`psi_check.py`, `run_d4.py`, `m6_k1.py`, `extra.py`, `d4_d6.py`, `c1_validate.py`, `run_c1.py`, `c1_j0.py`,
`d7_check.py`, `d8_spot.py`, `lean_semantics.py`. Lean: `./lean_v2_build.sh`.

---------------------------------------------------------------------------------------------------------------------

## Claim index (registered IDs BGS-TRACE-149..162; anchors used by the claims fragment)

<a id="claim-149"></a>
**BGS-TRACE-149 — Band-limited random kick: exact trace bridge E|Tr U^m|^2 = Psi_m(t_N)** (state: `proved`; ANALYTIC PROOF + NUMERICAL CHECK (pathwise <= 4e-14) + INDEPENDENT REFEREE AUDIT (fresh code, <= 1e-12 at 28 cases)). U = exp(i eta V_theta) M_N, M_N the S=[[3,4],[2,3]] cat-map matrix of Lines B/C, V_theta(x) = sum_{k in K} a_k cos(2 pi k x/N + theta_k), a fixed finite mode set K with a_k != 0; J0 ensemble: theta_k iid uniform; G ensemble: circular complex Gaussian coefficients with E|c_k|^2 = a_k^2. H_m = 6I - C - C^T, D_m = det H_m = Tr S^m - 2, X_m = D_m H_m^{-1}. For every odd N with gcd(N, D_m) = 1 (primality not used) and every theta: Tr U^m = Tr M_N^m sum_n Ghat_theta(n) e(t_N 2 n^T X_m n), t_N = (D_m^{-1} mod N)/N, |Tr M_N^m| = 1; hence E_theta|Tr U^m|^2 = Psi_m(t_N), Psi_m C^infinity (not claimed real-analytic), even (V -> -V symmetry), 1-periodic, independent of N. This is Line B Theorem 1 (Line B packet) applied for each theta; the mechanism is Boasman-Keating 1995 section 5 and is not claimed as new. When N | D_m the normalisation fails. Does not prove BGS-TRACE-005 or BGS-BGS-001; says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.

<a id="claim-150"></a>
**BGS-TRACE-150 — Band-limited random kick: 1/N expansion and residue period g'_m** (state: `proved`; ANALYTIC PROOF + EXACT QUADRATURE CHECKS (p <= 1601) + INDEPENDENT REFEREE AUDIT). t_N = t* + 1/(N D_m), t* = -N^{-1}/D_m (mod 1); E = Psi_m(t*) + c_1/N + O(N^-2), c_1 = Psi_m'(t*)/D_m, for fixed (m, K, a, eta). Psi_m(t*) depends only on +-N mod g'_m, g'_m = D_m/gcd(D_m, 2X_ii, 4X_ij) = 14, 48, 82, 280, 478, 1632, 2786 (m=3..9), an upper bound on the period. The O(N^-2) constant is NOT uniform in eta or K; the limits N -> infinity and eta -> infinity do not commute (m=3, K=1, J0, p=101: p(E-Psi(t*)) = 40.5 vs c_1 = -201 at eta=16). The condition eta^2 (sum k^2 a_k^2) m << N is heuristic. Does not prove BGS-TRACE-005 or BGS-BGS-001; says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.

<a id="claim-151"></a>
**BGS-TRACE-151 — Band-limited random kick: orbit-pair formula and Gauss-weight support** (state: `proved`; ANALYTIC PROOF + NUMERICAL CHECK (1e-10) + LEAN FINITE INSTANCES (|ker(H_m mod 4)|, m=3..6) + INDEPENDENT REFEREE AUDIT). Psi_m(s/D) = sum over xi, xi' in Fix_m = {xi : H_m xi in Z^m} (period-m solutions of q_{j+1}+q_{j-1} = 6 q_j mod 1; same count D_m as Fix S^m, no bijection claimed) of phihat_s(xi) conj phihat_s(xi') prod_k omega_k(eta(S_k(xi)-S_k(xi'))), omega = J0(a|z|) (standard Kluyver average, as in BGS-TRACE-133) or exp(-a^2|z|^2/4). |phihat_s|^2 in {0, |V[4]|/D_m}, support independent of s (Line B Prop R). D_eff = 49, 72, 1681, 4900, 57121 (m=3..7). Orbit form not claimed as new (Boasman-Keating). Does not prove BGS-TRACE-005 or BGS-BGS-001; says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.

<a id="claim-152"></a>
**BGS-TRACE-152 — Band-limited random kick: strong-kick limit B_m^sym at every residue under P_K-separation** (state: `proved`; ANALYTIC PROOF + INDEPENDENT REFEREE AUDIT). If a_k != 0 for k in K and P_K(xi) = (S_k(xi))_{k in K} separates dihedral (Gamma) classes on the support, then lim_{eta->inf} Psi_m(t*) = B_m^sym = D_eff^{-1} sum_{supp}|Gamma xi| for every residue. Iterated limit (N -> infinity first). Quenched-ensemble analogue of Line B Theorem 4. At finite eta Psi_m(t*) is residue dependent and takes values in a range containing 2m; the COE value 2m is not obtained at any fixed m. Does not prove BGS-TRACE-005 or BGS-BGS-001; says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.

<a id="claim-153"></a>
**BGS-TRACE-153 — Band-limited random kick: computer-assisted instances m=3..7 (B^sym values, Gamma-separation, K=1 collisions)** (state: `verification-pending`; COMPUTER-ASSISTED (exact integer and 60-digit checks) + INDEPENDENT REFEREE REPLAY; pending: deposit of a second independent exact replay as verifier of record). B_m^sym = 235/49, 61/12, 15801/1681, 27417/2450, 788019/57121 (m=3..7). Multiset => Gamma-class on Fix_m checked exactly for m <= 7, so K = {1..m} and K = {1,2} separate Gamma-classes for m <= 7. K = {1}: separates on the support for m = 3, 5, 7 (gaps 0.753, 1.936e-3, 3.685e-5); m = 4 and 6 have one collision group each (2 and 26 Gamma-classes, half-turn invariant; listed sequences Lean-certified as orbits, support/distinctness/completeness checked in Python). Non-separation is necessary, not sufficient, for residue dependence of the limit (m=4, K=1: 4.861111 at all residues; m=6, K=1: {10.705923, 11.165914}). eta-threshold tables are N -> infinity values only. Does not prove BGS-TRACE-005 or BGS-BGS-001; says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.

<a id="claim-154"></a>
**BGS-TRACE-154 — B_m^sym < 2m for every odd m** (state: `proved`; ANALYTIC PROOF (referee argument) + EXACT VALUES m <= 9). For odd m, D_eff = a_m^2 with a_m odd, so the Gamma-invariant support has odd size; the reversal involution has a fixed point xi_0 with |Gamma xi_0| <= m, hence 2m - B_m^sym >= m/D_eff > 0. Same argument whenever 2m does not divide D_eff (e.g. m = 6). Does not prove BGS-TRACE-005 or BGS-BGS-001; says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.

<a id="claim-155"></a>
**BGS-TRACE-155 — B_m^sym < 2m for even m beyond the computed range** (state: `open`; OPEN). Verified by enumeration for m <= 9 (B_4^sym = 61/12, B_6^sym = 27417/2450, B_8^sym = 15.298683). For even m with 2m | D_eff (m = 4, 8, ...) no general proof. Closure: a proof of a Gamma-stabiliser point on the support for every even m, or of Line B's ND_m bound in this form. Does not prove BGS-TRACE-005 or BGS-BGS-001; says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.

<a id="claim-156"></a>
**BGS-TRACE-156 — P_K separates point multisets for K containing {1..m}; half-turn collisions for odd K at even m** (state: `proved`; ANALYTIC PROOF + LEAN FINITE INSTANCES (listed m=4, m=6 sequences are half-turn invariant orbits)). (a) Newton identities: S_1..S_m determine the multiset {e(xi_j)} (multisets only; multiset => Gamma-class is BGS-TRACE-153, m <= 7). (b) For even m and K inside the odd integers, any orbit whose point multiset is invariant under q -> q + 1/2 has S_k = 0 for all odd k, so all such orbits collide. Does not prove BGS-TRACE-005 or BGS-BGS-001; says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.

<a id="claim-157"></a>
**BGS-TRACE-157 — 1/N coefficient: Gamma-diagonal part vanishes; oddness in the residue** (state: `proved`; ANALYTIC PROOF + NUMERICAL CHECK (Gamma-diagonal part <= 1e-12; residue sum 0 to 1e-11) + INDEPENDENT REFEREE RE-DERIVATION). c_1 = (2/pi) Im sum phihat(xi) conj phihat(xi') E[G(xi) conj G(xi') beta(xi)], beta = i eta h_0 sum v''(xi_i) - eta^2 v'^T H^{-1} v'. (a) The pairs xi' in Gamma xi contribute zero (both ensembles). (e) c_1(-N mod g'_m) = -c_1(N mod g'_m), so c_1 averages to 0 over residues and cannot equal -2m^2 uniformly in N; for single residues and some eta, c_1 = -2m^2 is not excluded. Does not prove BGS-TRACE-005 or BGS-BGS-001; says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.

<a id="claim-158"></a>
**BGS-TRACE-158 — 1/N coefficient, Gaussian ensemble: c_1 -> 0 as eta -> infinity under Gamma-separation** (state: `conditional`; CONDITIONAL on P_K-separation of Gamma-classes (unconditional for m <= 7 once BGS-TRACE-153 is promoted); ANALYTIC PROOF + EXACT TABLES m=3..6). G ensemble only. Tilted expectation f*b with f = prod exp(-a_k^2 eta^2 |Delta S_k|^2/4) and b real, polynomial of degree 4 in eta; if P_K separates Gamma-classes with gap delta, |c_1| <= C_m eta^4 exp(-a_min^2 eta^2 delta^2/4) -> 0. Separation holds for K containing {1..m} or {1,2} only for m <= 7 (computer check, BGS-TRACE-153). Non-separating K: c_1 grows (m=4, K=1: c_1 = +-0.302 eta^2). Does not prove BGS-TRACE-005 or BGS-BGS-001; says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.

<a id="claim-159"></a>
**BGS-TRACE-159 — 1/N coefficient for uniform phases (J0) at large eta** (state: `open`; OPEN (numerics by independent referee)). Open. Numerically c_1 does not tend to 0 for the J0 ensemble: m=3, K=1 (separating): max_s|c_1| = 13.3, 128.7, 682.7, 7182, 85063, 453908 at eta = 1, 4, 16, 64, 256, 1024 (about eta^1.5). Closure: an asymptotic for the Bessel-tilted moments. Does not prove BGS-TRACE-005 or BGS-BGS-001; says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.

<a id="claim-160"></a>
**BGS-TRACE-160 — Full-band random kick equals the maximal random-phase ensemble up to p^m exp(-c p)** (state: `proved`; ANALYTIC PROOF + EXACT ENUMERATION (p = 5..13) + INDEPENDENT REFEREE AUDIT). K = {1..(p-1)/2}, a_k = a, odd prime p: |E - E_LineC(p,m)| <= p^m exp(-eta^2 a^2 p/4) (G) and <= p^m exp(-beta eta^2 a^2 p), beta = min(0.2, 0.2676/(2 m eta a)^2) (J0). With BGS-TRACE-146 (prime p > 4^m): E = 2m - 2m^2/p + O_m(p^{-3/2}) for m >= 5. Only a transfer of Line C, not a new COE theorem. G full band: sites iid up to a global phase that cancels. J0 bound useful only for p >> m^3 log p. Does not prove BGS-TRACE-005 or BGS-BGS-001; says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.

<a id="claim-161"></a>
**BGS-TRACE-161 — Intermediate band K = kappa N** (state: `open`; OPEN (SKETCH)). Sketch only: needs a lower bound min_{Delta} sum_{k<=K}|Delta_hat(k)|^2 >= c N^gamma over admissible Delta (super-resolution / partial-Fourier smallest singular value on the N-th roots of unity with multiplicities). Does not prove BGS-TRACE-005 or BGS-BGS-001; says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.

<a id="claim-162"></a>
**BGS-TRACE-162 — Crossover conjecture: R-scaling of the band-limited deviation and the mode threshold** (state: `open`; OPEN / CONJECTURE (NUMERICAL DIAGNOSTICS ONLY)). Conjecture: with R = pi eta (sum k^2 a_k^2)^{1/2}/p fixed, lim_p E = 2m + F_m(R), F_m(R) -> 0 as R -> infinity; Line C's -2m^2/p needs R -> infinity. Numerics (J0, eta a = 2, Monte Carlo, p = 101, 211, 401): collapse at p = 211 and 401 only; deviations below MC error for R >~ 1.6 (K ~ 12, 20, 31). Caveats: two primes; R derived from the G weight but tested on J0 data; K_* ~ p^{2/3} only restates fixed R; R_* depends on the MC precision. Line C's chi^2/dof ~ 967 for its 7-mode kick is consistent with an effectively single-mode regime (K_eff = 1.04, R = 0.39); numerical record, not derived from fixed-m results. Does not prove BGS-TRACE-005 or BGS-BGS-001; says nothing about eigenvalue statistics beyond the second moment of Tr U^m at fixed m.
