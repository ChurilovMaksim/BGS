# Line I: averaging across residues for Conjecture R′ — exact dilation laws, a reduction, and certified twisted spectra

Status: paper proofs (elementary finite Fourier analysis), Lean cores (`Bgs.LineI`, `Bgs.LineIArith`), computer-assisted certificates
(arb ball arithmetic plus float BLAS with a-priori rounding bounds, as in Line H), and floating-point numerics, each labelled below.
Independent referee audit: `computations/verification/lineI/referee/REPORT.md` (first round: ACCEPT AFTER FIXES, fixes B1–B9 and
recommendations R1–R7 applied; delta review of Session 4: ACCEPT AFTER FIXES, fixes DF1–DF7 applied, see §10).

Registered claims (`record/claims.json`): §2 is **BGS-TRACE-211**, §3 is **BGS-TRACE-212**, §4 is **BGS-TRACE-213**, §5 is
**BGS-TRACE-214**, §6 is **BGS-TRACE-215**, §7 is **BGS-TRACE-216**, §8 is **BGS-TRACE-217**, §9.1 is **BGS-TRACE-218**, §9.2 is
**BGS-TRACE-219**, and Conjecture R′_A (§9.3) is **BGS-TRACE-220** (open). The derivation of the Line G G3 form in §3 proves
**BGS-TRACE-204** (owner decision, audit of PR #60). **BGS-TRACE-206 (Conjecture R′) stays open.** The packet
is `computations/verification/lineI/`; the integration record is `evidence/executions/20261031/lineI/INTEGRATION.md`.

**Later work (Line J, 31 October 2026).** [lineJ_d7_twisted_coefficient.md](lineJ_d7_twisted_coefficient.md) (BGS-TRACE-221 to BGS-TRACE-233) decides c(β) ≠ 0 exactly
(BGS-TRACE-221): class 1:3 cancels exactly between ρ = (±2,8), and 2:1 survives. It proves Theorem J (BGS-TRACE-225): the frozen d = 7
term oscillates with growth ≥ 1.0184224^m along subsequences. The heuristic statement at the end of §8 about the d = 7 cross term is
superseded by these. Frozen R′ is refuted along m = 3p only conditionally (BGS-TRACE-231, under the open BGS-TRACE-232 and 233), and it
stays open.

**Scope.** Everything here is about the single-cosine **k1** kick 0.9 cos 2πq at η = 2 (ĝ(n) = iⁿJ_n(1.8)), the map S = [[3,4],[2,3]],
λ = 3 + 2√2, odd m, h = h_m = Re(1+√2)^m, y′ = Im(1+√2)^m (h² + 1 = 2y′²), φ = φ(2h). Nothing here is a statement about the Line B kick,
about Conjecture R (BGS-TRACE-179) or R_NSW (BGS-TRACE-210), or about BGS (BGS-BGS-001); there is no progress on BGS-TRACE-148.
The goal of Line I was a proof of Conjecture R′ (BGS-TRACE-206). **It was not obtained.** What was obtained: exact identities for the
dilation members, an exact reduction of R′ to three sub-statements, certified bounds on the d = 7 square term (ρ = (±2,8) only), a certified lower bound
on the d = 7 twisted spectral radius that rules out the operator-radius route to the d = 7 cross term, and two arithmetic lemmas.
Withdrawn during review and NOT registered: the statement that the diagonal is "invisible" in Lemma I5 (§5), the "p ~ h^c" size claim (§9.2),
and the claim that resonance terms are "exactly" the large-e Möbius terms (§9.1).

**Labels.** [P] paper proof here; [L] Lean-checked core; [CA] computer-assisted certificate; [N] floating-point numerics; [H] heuristic;
[assessment] an argument that a specific route fails (not an impossibility proof).

## 1. Notation (frozen definition of BGS-TRACE-206)
Z_m(ν) = Σ_{n∈ℤ^m} Φ̂(n) e(−νP(n)/2h), Φ̂(n) = Π_j ĝ(n_j), P(n) = Σ_{i,j<m} ψ(|i−j|) n_i n_j, ψ(d) = y′x_d − 2h y_d with
λ^d = x_d + 2y_d√2 (BGS-TRACE-183). F_m = φ⁻¹ Σ_{ν unit mod 2h} |Z_ν|², RMT_m = 4m − m²/h. Resonant primaries 𝓟* = {(2,8), (−2,8), (2,16),
(−2,16)}, ν_ρ the unit with bν_ρ ≡ a (mod 2h), Z_ρ = Z_m(ν_ρ); levels d | h, 1 < d ≤ √h, members M_d(ρ) = {ν unit: bν ≡ a mod 2h/d, not
mod 2h/d′ for d′ | d, d′ < d}, n_d = |M_d(ρ)|; a level is included iff |Z_ρ|²/d² ≥ 4m; Res_m and W′_m = F_m − RMT_m − Res_m as in
BGS-TRACE-206. Dev_d(ρ) = Σ_{ν∈M_d(ρ)} (|Z_ν|² − |Z_ρ|²/d²). α_n = Σ_i n_i λ^i ∈ ℤ[√2], Nm and Tr the norm and trace of ℚ(√2).

## 2. Prop I1 (relative phase split) — BGS-TRACE-211 [P, elementary; N]
For any unit ν₀ with Z_m(ν₀) ≠ 0 let σ be the complex measure on ℤ/2h with σ(p) = Z_m(ν₀)⁻¹ Σ_{P(n)≡p} Φ̂(n) e(−ν₀P(n)/2h)
(total mass 1) and σ̂(δ) = Σ_p σ(p) e(−δp/2h). Then for every integer δ,  Z_m(ν₀ + δ) = Z_m(ν₀) σ̂(δ).
*Proof.* Substitute the definition; the sum is absolutely convergent (Σ|Φ̂| < ∞). ∎
This is a definitional rewriting (low novelty; it is the "relative" form of the phase split G1 of Line G, BGS-TRACE-203). With ν₀ = ν_ρ,
the dilation members of level d are σ̂ at δ ∈ (2h/d)ℤ (§3). The reading of the "resonance halo" (residues near small-denominator
rationals) as small rational δ is a heuristic description [H], not part of the claim; the halo is NOT a generalised 1/d² dilation law
(numerically the normalised excess grows with d′). Check: `integration_checks/lineI_identity_checks.py` (C2, random weights, m = 5, 7, 9,
rel. err ≤ 4e−13).

## 3. Prop I2 / I2′ (dilation-coset L² law) — BGS-TRACE-212 [P; L core; N]
Fix a unit ν₀, put w(n) = Φ̂(n) e(−ν₀P(n)/2h), Z₀ = Σ_n w(n) = Z_m(ν₀). For odd d | h put W(γ) = Σ_{α_n ≡ γ (mod d)} w(n) (γ ∈ ℤ[√2]/d)
and Ẑ(β) = Σ_n w(n) e(Tr(βα_n)/d) (the twisted sums: the kick at site i translated by Tr(βλ^i)/d).
**Congruence [P].** P(n) ≡ y′·Nm(α_n) (mod 2h): Nm(α_n) = Σ_{i,j} n_i n_j x_{|i−j|} (λλ̄ = 1) and ψ(d) ≡ y′x_d (mod 2h).
**(I2′) per member, any odd d | h, prime or composite.** For j with t = j y′ a unit mod d,
  Z_m(ν₀ + 2hj/d) = Σ_γ W(γ) e(−t·Nm γ/d) = d⁻² Σ_{β mod d} Ẑ(β) G_t(β),   G_t(β) = Σ_γ e(−(t·Nm γ + Tr βγ)/d),
and |G_t(β)| = d for all β (the form factorises into two one-variable Gauss sums with unit leading coefficients, d odd). Hence
Z_t = ω_t Z₀/d + Δ_t with |ω_t| = 1 and |Δ_t| ≤ d⁻¹ Σ_{β≢0}|Ẑ(β)|.
*Proof.* e(−jP(n)/d) = e(−t·Nm(α_n)/d) by the congruence (d | h), group the words by α_n mod d, and invert the finite Fourier transform
on (ℤ/d)² with the trace pairing (non-degenerate for odd d). ∎
**(I2) coset law, prime d ∥ h.** With ε = (2/d), W_u = Σ_{Nm γ ≡ u} W(γ) and Z_t = Σ_u W_u e(−tu/d):
 (a) Σ_{t mod d} |Z_t|² = d Σ_u |W_u|²;  (b) N(u) = #{γ: Nm γ ≡ u} = d − ε (u ≠ 0), N(0) = d + (d−1)ε;
 (c) with δ_u = W_u − Z₀N(u)/d² (so Σ δ_u = 0): Σ_u N(u)δ_u = εdδ₀ and Σ_u N(u)² = d³ + d² − d;
 (d) Σ_{t≠0} |Z_t|² = |Z₀|²(1/d − 1/d²) + 2ε Re(Z̄₀δ₀) + d Σ_u |δ_u|².
For odd m, ε = +1 for every prime d | h_m (2 is a square mod d because (2y′)² − 2 = 2h², Lean `Bgs.LineIArith.two_isSq_mod`), so the
inert branch of (b) is vacuous here. 7 | h_m ⟺ m ≡ 3 (mod 6) (Lean `seven_dvd_nsw_iff`).
* **Lean** (`formalization/Bgs/LineI.lean`, namespace `Bgs.LineI`): `cross_term`, `sum_N_sq`, `coset_decomp` (the algebra (c)–(d) for any
  ε with ε² = 1), `norm_count_7` (full norm counts over ℤ/7), `norm_count_23_zero` (zero count over ℤ/23 only); and
  `Bgs.LineIArith.two_isSq_mod`, `seven_dvd_nsw_iff`. **Not formalised:** the Fourier step (a), the congruence, I2′, the identification
  of Z_t with Z_m(ν₀ + 2hj/d).
* **Numerics.** Author `code/verify_coset.py` (m = 5 d = 41, m = 9 d = 7, m = 11 d = 23, m = 7 d = 239; max err 1.5e−12). Integration
  re-implementation: `integration_checks/lineI_identity_checks.py` (C1 congruence: 0 failures; C3 (a)–(d), C4 I2′ for d = 41 (m = 5) and
  d = 7 (m = 9): ≤ 6.6e−13) and `lineI_composite_d_check.py` (I2′ and |G_t| = d for composite d = 287 = 7·41 at m = 15 and d = 49 at
  m = 21, prime d = 7, 41: ≤ 3.9e−15). Twisted-trace closure: m = 9, ρ = (2,8), the members predicted from the 49 twisted traces agree with
  the class sums to 2.6e−8 (`code/dilpred.py`, `logs/dilpred_d7.log`).
* **The Line G G3 form; proof of BGS-TRACE-204 [P; N].** Let t be a unit mod d, t̄ = t⁻¹ mod d, and let γ ↦ γ̄ be the conjugation
  x + y√2 ↦ x − y√2 on ℤ[√2]/d. Then, in ℤ/d, t·Nm(γ + t̄β̄) = t(γ + t̄β̄)(γ̄ + t̄β) = t·Nm γ + (γβ + γ̄β̄) + t̄·Nm β, and γβ + γ̄β̄ = Tr(βγ), so
    t·Nm γ + Tr(βγ) = t·Nm(γ′) − t̄·Nm β,   γ′ = γ + t̄β̄.
  The map γ ↦ γ′ is a bijection of ℤ[√2]/d. Hence G_t(β) = e(t̄·Nm β/d)·G_d(t), where G_d(t) = G_t(0) = Σ_γ e(−t·Nm γ/d) and |G_d(t)| = d.
  Substituting this into I2′ gives
    Z_m(ν₀ + 2hj/d) = (G_d(t)/d²) Σ_{β mod d} e(t̄·Nm β/d) Ẑ(β),
  which is exactly the G3 formula of BGS-TRACE-204, with Z^{(β)}_{ν₀} = Ẑ(β) and the same sign conventions as Line G's
  `check_dilution.py`. Two remarks on conventions:
  * The right side is invariant under β ↦ −β (Nm(−β) = Nm β), so the direction of the kick translation does not matter.
  * The step uses only the congruence and Fourier inversion. So it holds for every odd d | h, prime or composite, and every j with
    t = jy′ a unit.

  **Check [N]:** `integration_checks/lineI_G3_form_check.py` compares the formula against brute force directly from P(n). It uses random
  site-dependent weights and a random unit ν₀, and also checks the completed square G_t(β) = e(t̄Nmβ/d)G_d(t) for every β. Cases:
  * d = 41 (m = 5) and 239 (m = 7);
  * d = 7, 199, 1393 = h (m = 9);
  * d = 23, 353 (m = 11) and 79, 599 (m = 13);
  * d = 7, 31, 41, 217, 287, 961 = 31², 1271 (m = 15);
  * d = 7, 49, 1673 (m = 21).

  The worst relative error is ≤ 8.4e−15. The negative control t̄ ↦ −t̄ is run and logged by the same script and fails in every case, with error ≥ 1.19. On this basis BGS-TRACE-204 is registered
  as **proved**, with a dependency on this claim (owner decision). Its non-claim is unchanged: the main-term approximation
  |Z|² ≈ |Z_ρ|²/d² has no rigorous error bound.
* **Heuristic corollary [H].** The frozen dilation term is o(1) relative to the main term iff the twisted radii satisfy r_tw < √λ/μ₀
  (cross part) and r_tw < λ^{1/4} (square part); μ₀ is the growth rate of |Z_ρ| (§8).

## 4. Theorem I4 (exact reduction of R′) — BGS-TRACE-213 [P, elementary; N]
For m ≥ 5 the sets {ν_ρ} (ρ ∈ 𝓟*) and M_d(ρ) (ρ ∈ 𝓟*, any set of included levels) are pairwise disjoint (a common member of two
levels d ≠ d′ of one ρ satisfies the congruence modulo 2h/gcd(d,d′) and is excluded from the larger level; two different ρ would force
M ≤ 6 for the modulus M = 2h/max(d,d′) ≥ 2√h; ν_ρ is the d′ = 1 case). Let 𝓡_m be their union. Then, exactly,
  W′_m = φ⁻¹ Σ_{ν unit, ν ∉ 𝓡_m} (|Z_ν|² − RMT_m) + φ⁻¹ Σ_{ρ, d included} Dev_d(ρ).
Split the first sum by the height y(Λ_ν) of the reduced representative of z_ν = (ν + i)/2h in SL₂(ℤ)\ℍ: fix ONE function Y(m) → ∞ and
let (E″) be the part with y ≤ Y(m) (the growing compacta K_m = {y ≤ Y(m)}, uniformly — not merely each fixed compact) and (T″) the part
with y > Y(m), both after removing 𝓡_m, and (D) the dilation remainder φ⁻¹ Σ Dev. **If (E″), (T″) and (D) are each o(m), then R′ holds.**
**Alternative sufficient hypothesis** (sufficient, not equivalent; DF1): (T″) for EVERY Y(m) → ∞ and (E″) for each fixed Y, with a diagonal
choice of Y(m) growing slowly enough. Normalisation: all sums over units, divided by φ(2h).
*Proof.* Insert Res_m and use disjointness; the diagonal argument is standard. ∎  None of (E″), (T″), (D) is proved. For d = 7 the square
part of (D) is controlled only for ρ = (±2,8) (BGS-TRACE-215); the (±2,16) level-7 members are not controlled; the cross part is not
controlled, and BGS-TRACE-217 shows that the operator-radius route to it fails.
Numerical check of the bookkeeping (frozen definition, all levels included, random weights): `integration_checks` C7, ≤ 4.4e−16.

## 5. Lemma I5′ (Fourier expansion of weighted horocycle sums) — BGS-TRACE-214 [P; N]
Let f(x + iy) = Σ_{k∈ℤ} c_k(y) e(kx) with Σ_k |c_k(1/2h)| < ∞ (e.g. f smooth on SL₂(ℤ)\ℍ; only 1-periodicity in x is used), z_ν = (ν + i)/2h,
C(k) = Σ_{n,n′} Φ̂(n) conj Φ̂(n′) 1[P(n) − P(n′) ≡ k (mod 2h)] and c_q the Ramanujan sum. Then
 (a) Σ_{ν mod 2h} |Z_ν|² f(z_ν) = 2h Σ_k c_k(1/2h) C(k)   (C(k), not C(−k));
 (b) Σ_{ν unit} |Z_ν|² f(z_ν) = Σ_k c_k(1/2h) Σ_{n,n′} Φ̂(n) conj Φ̂(n′) c_{2h}(k − P(n) + P(n′)).
*Proof.* Expand |Z|² and f and sum over ν (orthogonality mod 2h, resp. the definition of c_{2h}). ∎
**Diagonal.** Pairs with P(n) ≡ P(n′) (mod 2h) contribute C(0) × the UNWEIGHTED sum of f over the 2h horocycle points (a), resp. over the
φ(2h) primitive ones (b); in (a) the diagonal meets every c_{2hj}, not only c₀. So it is **not** invisible for cusp forms (the earlier
"diagonal invisible" statement is withdrawn and not registered). Using (b) for R′ needs an equidistribution input for primitive rational
points on the horocycle of height 1/2h with an explicit rate, and C(0) = O(m) (numerically O(m), not proved) — both are open inputs,
not part of this claim. Check: `integration_checks` C6 (random c_k, |k| ≤ 40), ≤ 1.7e−13.

## 6. Theorem I6 v2 (d = 7 square term) — BGS-TRACE-215 [CA]
**Statement.** k1 kick, η = 2, ρ ∈ {(2,8), (−2,8)}, every m ≡ 3 (mod 6) (so 7 | h_m), m ≥ 9, d = 7, every β ≢ 0 (mod 7):
  |Ẑ(β)| ≤ 6.769·10⁶ · 1.45^m + 6.859·10⁴   (outward rounded; exact CV = 6 768 179.601…, CE = 68 586.18…),
and the square term of level 7 satisfies
  7 Σ_u |δ_u|² / φ(2h_m) ≤ (13/7)·48·(6.769·10⁶·1.45^m + 6.859·10⁴)² · (e^γ lnln h + 2.50637/lnln h)/h,
which is ≤ 0.01 for every such m ≥ 321 (0.004574 at m = 321 with the exact constants CV, CE; 0.004575 with the rounded constants
displayed; m = 315 gives 0.01046) and decays like (1.45²/√λ)^m ≤ 0.87089^m
(rigorous tail for m ≥ 1425, ≤ 4.7·10⁻⁶⁹ at m = 1425).
**Proof chain.** (1) Certified spectra [CA] of the lifted twisted operators (G2 automaton factor on the 16 reachable states ⊗ 3-cycle twist
⊗ the vertex/edge Hardy lattices of BGS-TRACE-197; K0 = 2, ρ = 0.85, β = 3.5, full alphabet |n| ≤ 150 explicit + analytic tail) for all 8
classes of β mod ±λ in the case m ≡ 9 (mod 24), ρ = (2,8): V in |z| < 1.45 (F ≤ 0.357 < 1 at R = 1.45), E in |z| < 1.0 (F = 0.0138);
rig_spec v4 of Line H unchanged (sha f346e22c…). (2) ‖L^n‖ ≤ R^{n+1}G/(1−F), |Tr(BL^m)| ≤ 4‖L‖₁R^mG/(1−F). (3) The lifted partial-trace
identity Ẑ = c_m(Tr BV^m − Tr BE^m), c_m = 1 − λ^{−m}, from BGS-TRACE-197 with a finite monomial state factor and rank-one B, termwise per
word (as in BGS-TRACE-207); referee brute force over all 5⁹ words at |n| ≤ 2 (agreement 1e−12…5e−14) and full alphabet at m = 9 (1.1e−8).
(4) Class invariance Ẑ(λβ) = Ẑ(β) (λ^m ≡ 1 mod 2h, cyclic quadratic form), Ẑ(−β) = Ẑ(β). (5) Parseval and N(u) ≤ 2d − 1. (6) Rosser–Schoenfeld
Theorem 15 (Illinois J. Math. 6 (1962), pp. 71–72, (3.42); registered as EXT-RS-1962) lower bound for φ, applied with n = h_m. (7) All other operator cases and ρ = (−2,8) by the exact intertwiners of BGS-TRACE-216. Arithmetic in arb
(`cert_v2/bounds_sq_v2.py`; DF2 path-fixed rerun `cert_v3/bounds_sq_v3.py`, log byte-identical; v3 supersedes v2, which is kept as provenance).
**Scope.** Only the SQUARE part of the d = 7 remainder, only ρ = (±2,8) (the (±2,16) level-7 members are not controlled), only m ≡ 3 (mod 6); < 0.01 only from m = 321. The cross term
2Re(Z̄_ρδ₀) is NOT controlled. Trusted components: arb/python-flint 0.9.0, IEEE binary64, OpenBLAS zgemm without Strassen, Line F F1.
Galerkin matrices are not stored in the repository; they regenerate deterministically (commands in the packet README; the referee
regenerated V_1_3/E_1_3 byte-identically).

## 7. Exact monomial intertwiners — BGS-TRACE-216 [P, exact integer witnesses; N]
The finite (automaton) factor of the (±2,8) G2 operators depends on m only through (h, y′) mod 8, i.e. on (1+√2)^m mod 8 (period 8 in m),
and the twist on β and m mod 3; for m ≡ 3 (mod 6) this gives the 8 cases (m mod 24 ∈ {9, 15, 21, 3}) × (a = ±2). For every case there is a
monomial unitary X on the 16 reachable states (permutation × 8th roots of unity) with
  a = +2:  X A_n^{(9,2)} X⁻¹ = A_n^{(m,2)}  for all n mod 8;     a = −2:  X (−1)ⁿ conj(A_n^{(9,2)}) X⁻¹ = A_n^{(m,−2)};
and a monomial Y with Y A_{−n} Y⁻¹ = A_n. Consequently, for the TRUE lifted twisted operators V and E:
  L^{(m,2)}_β = U L^{(9,2)}_β U⁻¹ (U = I ⊗ X ⊗ I₃),  L^{(m,−2)}_β = J L^{(9,2)}_{−β} J⁻¹ (J = K ⊗ X ⊗ I₃ antiunitary, K complex conjugation
  on the disc lattice; uses conj ĝ(n) = (−1)ⁿĝ(n) and K M_C K = M_{−C}),  L_{−β} = (R ⊗ Y ⊗ I₃) L_β (R ⊗ Y ⊗ I₃)⁻¹ (R: s ↦ −s, c ↦ −c).
Spectra (for J: conjugated, moduli and multiplicities preserved), sup_{|z|=R}‖(z − L)⁻¹‖, trace norms and ‖B‖ are invariant, and β ↦ −β
permutes the classes; hence every certificate of BGS-TRACE-215 and BGS-TRACE-217 transfers to all m ≡ 3 (mod 6), ρ = (±2,8).
Witnesses: `sym/monomial_intertw.py` (integer arithmetic mod 8; `sym/monomial_intertw.json`; DF2 path-fixed rerun `sym_v3/`, identical JSON
except the code hash; v3 supersedes v1, which is kept as provenance). Referee: symbolic check, own Galerkin check to ≤ 1.2e−16 with negative controls (1.16 / 1.13), and a DIRECT
certificate of the transferred case m = 15, a = −2, class 1:3 (`cert2/`): F(V, 1.45) = 0.356981, F(E, 1.0) = 0.013833, equal to the m = 9
values. Not formalised: the intertwiner witnesses are checked by exact integer code, not in Lean (the auxiliary fact 7 | h_m ⟺ m ≡ 3 mod 6 is
the Lean lemma `seven_dvd_nsw_iff`, registered under BGS-TRACE-212).

## 8. Theorem I9 (certified lower bound for the top twisted spectral radius) — BGS-TRACE-217 [CA + P]
**Statement.** For the lifted twisted V operator (K0 = 2, ρ = 0.85, β = 3.5) with β in class 1:3 or 2:1 (the two classes with the largest
float radii), in every operator case m ≡ 3 (mod 6), ρ = (±2,8):
  σ(V_β) ∩ {|z| > 1.22} = {μ, ωμ, ω²μ} (ω = e^{2πi/3}), each eigenvalue algebraically simple, with the CERTIFIED range 1.262 < |μ| < 1.45;
the rest of σ(V_β) lies in |z| < 1.22. Hence r_tw(β) = |μ_β| > 1.262 > 1.260376 ≥ √λ/μ₀.
**μ₀ (DF3; wording per owner audit R5).** Define μ₀ := lim |Z_m(ν_ρ)|^{1/m} over odd m (the quantity in the cross term). The limit
exists by BGS-TRACE-198 and BGS-TRACE-199. The bound rests directly on BGS-TRACE-199's lower bound for the sequence itself:
* **ρ = (−2,8).** 8ν ≡ −2 (mod 2h) means 4ν ≡ −1 (mod h), and the unit condition picks the odd lift. So ν_{(−2,8)} = ν* of
  BGS-TRACE-183, and BGS-TRACE-199 gives |Z_m(ν*)| ≥ ½(1 − λ^{−m})(1.9154712^m − 3012.30) for every odd m ≥ 13, hence μ₀ ≥ 1.9154712.
  BGS-TRACE-198 (|μ*| ∈ [1.9154712, 1.9154753], `computations/verification/lineF/logs/certV_eta2_a4_tight.json`) supplies the upper end.
  Line F uses the same kick convention, w = iⁿJ_n(0.9η) with η = 2.
* **ρ = (2,8)** (ν = −ν*). Use conj ĝ(n) = (−1)ⁿĝ(n) and the TRACE-183 phase at −ν*:
  conj Z_m(−ν*) = Σ_n Φ̂(n) e(q/2 + κ(Σn)²/8 + (Σn)/2). The factor e(4s/8) shifts the TRACE-184 sector coefficients (c_a ↦ c_{a−4}, still of
  modulus ½ for even a), so the same lower bound holds.

Hence √λ/μ₀ ≤ (1+√2)/1.9154712 = 1.2603758… ≤ 1.260376 (arb). (Float growth rates of both ρ: 1.9154732, Line G.)
**Certificate [CA].** `dom/rig_dom3b.py` generalises Line H rig_spec v4 to a k-dimensional (k = 3) Householder deflation with an
a-posteriori residual; T₀ = [[Λ, b₁₂], [0, Y]]; the three eigenvalues of Λ are isolated in arb (all |·| > R), σ(Y) ⊂ {|z| < R} by Neumann
validity; sup_{|z|=R}‖(z − T₀)⁻¹‖ by a pointwise bound on 4096 grid points plus covering by the resolvent identity; homotopy F < 1 ⇒ the
count 3 is the count for V_β. Operator: D = 8064 (K = 36/30), δ₁ = 3.13e−4, δ₂ = 3.1e−8, Δ = 6.25e−4, pertT = 9.375e−4. Certified at
R = 1.22, 1.24, 1.25 and 1.262 for both classes. **DF4:** the v2 code took gmax with an arb comparison that is False on overlapping balls;
v3 (`dom_v3/rig_dom3b.py`) compares exact upper ends. Rerun on the unchanged matrices (sha256 = v2 provenance): all certified; F(1.262) =
0.6842758739 (1:3) and 0.6489779088 (2:1) (v2: 0.6842758739 / 0.6488989; referee rerun of 2:1: 0.6489779088). The upper bound |μ| < 1.45
is the BGS-TRACE-215 rest certificate on the same true operator. Orbit structure [P]: S V_β S⁻¹ = ωV_β (S = ω^i on cycle component i), so
the 3-element multiset is one free orbit of z ↦ ωz, hence three distinct simple eigenvalues.
**Diagnostics only (DF5).** The Λ-block moduli 1.2837143 (1:3) and 1.2835951 (2:1) and the float radius 1.28371 are NOT enclosures of |μ|.
**Consequence [P, given the certificate].** For m ≡ 0 (mod 3), Ẑ(β) = c_m·c(β)·μ^m + O_β(1.22^m), c(β) = Σ_i Tr(BP_i). EITHER c(β) = 0, OR
limsup |Ẑ(β)|^{1/m} = |μ| > 1.262 > √λ/μ₀; in the second case no proof of (D) at d = 7 can go through r_tw < √λ/μ₀.
**Not certified / not implied.** c(β) ≠ 0 (float ≈ 0.5); the sign and size of the frozen d = 7 term in W′ (needs the Z₀ coefficients, the
8 classes in δ₀ and both ρ); frozen R′ is NOT disproved (bulk, (±2,16) members and other levels uncontrolled). The statement that the
frozen d = 7 term contributes ≍ 1.0185^m/m to W′/m along a subsequence (so that frozen R′ would fail around m ≈ 300–400) is a heuristic [H].

## 9. Arithmetic and structural statements
### 9.1 Aliasing (Möbius) identity — BGS-TRACE-218 [P; N]
With Z_m(θ) = Σ_n Φ̂(n) e(−θP(n)) and C_Z(k) = Σ_{n,n′} Φ̂(n) conj Φ̂(n′) 1[P(n) − P(n′) = k] (in ℤ), for every q | 2h
  (1/q) Σ_{ν′ mod q} |Z_m(ν′/q)|² = Σ_{j∈ℤ} C_Z(jq),   and   F_m = φ(2h)⁻¹ Σ_{e | 2h} μ(e) (2h/e) Σ_j C_Z(j·2h/e).
*Proof.* Expand, use orthogonality mod q (absolute convergence from Σ|Φ̂| < ∞), and Σ_{e | gcd(ν,2h)} μ(e) = 1[ν unit]. ∎
**Interpretation [H / assessment], not part of the claim (DF6).** The e > 2 Möbius terms are sums at EXACT rationals of denominator dividing
2h/e (non-unit residues, subtracted out), whereas the TRACE-206 resonant residues are units near (not at) small-denominator rationals;
they are related through the G2 law, not identical. Reading the bulk as the e ∈ {1,2}, j ≠ 0 aliasing sum is heuristic; Hecke-equivariance
and L²-in-m averaging reduce to the same aliasing sum and give no cancellation [assessment]. Check: `integration_checks` C5, ≤ 2.4e−12.

### 9.2 Unbounded prime support of h_m — BGS-TRACE-219 [P modulo a cited theorem; L]
h_m = V_m/2 for the Lucas pair α, β = 1 ± √2 ((P,Q) = (2,−1)), and U_{2m} = U_m V_m = 2h_m U_m. By Bilu–Hanrot–Voutier (J. reine angew.
Math. 539 (2001) 75–122, Theorem 1.4: for n > 30 every n-th Lucas number has a primitive divisor; Carmichael 1913 already covers real Lucas
pairs) U_{2m} has, for every m ≥ 16, a prime p dividing it and not (α − β)²U₁⋯U_{2m−1}. Then p is odd, p | h_m, and p ∤ h_{m′} for 0 < m′ < m.
Hence every m ≥ 16 contributes a NEW odd prime of h_m, and every finite set S of primes misses a prime factor of h_m for all sufficiently
large m. **Lean** (`Bgs.LineIArith`): `pell`, `lucasU_two_mul`, `nsw_dvd_lucasU_two_mul`, `primitive_dvd_nsw` and `finite_set_fails` — the
deduction is kernel-checked with the primitive-divisor theorem as an explicit hypothesis. BHV itself is not formalised; it is registered as
the external dependency EXT-BHV-2001, and Carmichael 1913 as EXT-CARMICHAEL-1913 (corroborating). No size statement on these primes is claimed (the earlier "p ~ h^c" is withdrawn). Check
(`integration_checks` C8): every m = 2..60 has a new prime of h_m; for 16 ≤ m ≤ 60 every primitive prime of U_{2m} divides h_m and no earlier h.
**[assessment], not part of the claim.** A transfer operator on a FIXED S-arithmetic space only sees residues with S-smooth reduced
denominator; once h_m has a prime outside S, every unit residue has reduced denominator 2h_m, so all are invisible to it. The full-adelic
version is non-nuclear and its "trace" is the Parseval sum of §9.1.

### 9.3 Conjecture R′_A (amended mean law) — BGS-TRACE-220 [C, open]
Keep 𝓟*, Z_ρ, the levels, the inclusion rule, M_d(ρ) and RMT_m frozen as in BGS-TRACE-206, but use the ACTUAL member values:
  Res^A_m = φ⁻¹ Σ_ρ [ (|Z_ρ|² − RMT_m) + Σ_{d incl.} Σ_{ν∈M_d(ρ)} (|Z_ν|² − RMT_m) ],   W′^A_m = F_m − RMT_m − Res^A_m.
**Conjecture R′_A:** W′^A_m = o(m). By §4, W′^A_m is exactly the non-resonant sum (E″-part + T″-part, for any Y(m)) and
W′_m − W′^A_m = φ⁻¹ Σ Dev_d(ρ); so (E″) + (T″) imply R′_A (not conversely: R′_A only bounds their sum), and R′_A + (D) imply R′; by I2′ each member value is explicit through d² − 1 twisted traces per level. With this definition Line I reproduces the W′_act values of Line G (`code/base.py`) [N].
**Evidence (heuristic / numerical only, NOT a proof):** on the "rest" set (85 % of residues, away from the resonant couplings) the mean of
|Z|²/RMT is 0.722, 0.865, 0.948, 1.019, 0.999 for m = 9…17 [N]; the halo near θ = ±½ contributes O(1) in F units for m = 11…17 [N]; W′_act/m
for m = 7…17: −1.226, −0.819, −0.314, −0.041, +0.229, +0.092 [N]. Rigorous routes tried (Deshouillers–Iwaniec large sieve, Kuznetsov/Weil,
Bowen–Margulis) fail for the stated inequality chains [assessment]. Proposed in the packet as an amendment of BGS-TRACE-206; it does not
replace it (206 stays open with its frozen definition).

## 10. Review record
First referee round (B1–B9, R1–R7) and delta review of Session 4 (DF1–DF7), all applied; the delta fixes are listed in
`computations/verification/lineI/AUTHOR_REPORT_session4.md` §S4.7 and in the integration record. Pre-fix copies of the four edited author
files are kept in `computations/verification/lineI/pre_delta/`.

## 11. Dependencies
BGS-TRACE-183, 184 (phase collapse and sector law), 197 (lifted trace identity), 198, 199 (certified μ*), 203 (G2 law), 206 (frozen
definition). BGS-TRACE-204 now depends on BGS-TRACE-212 (§3). External, registered in `literature/external_dependencies.json`
(review: `literature/lineI_sources_20261031.md`):
* EXT-BHV-2001 (Bilu–Hanrot–Voutier 2001, Theorem 1.4) for BGS-TRACE-219;
* EXT-CARMICHAEL-1913 for BGS-TRACE-219, corroborating;
* EXT-RS-1962 (Rosser–Schoenfeld 1962, Theorem 15) for BGS-TRACE-215.

The Ruelle / Bandtlow–Jenkinson trace formula enters through BGS-TRACE-197. That gap predates Line I and is out of scope here.
