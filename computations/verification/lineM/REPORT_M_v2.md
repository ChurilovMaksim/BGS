# Line M report v2: fresh-eyes search for a different route to refuting frozen R′ (TRACE-206)

**v2.** 31 Oct 2026 (Asia/Yekaterinburg, UTC+5). This version applies the referee fixes M-F1 … M-F12 from
/workspace/audit/lineM/REPORT.md (verdict READY-after-fixes). REPORT_M.md (v1) is kept unchanged for provenance. The errata table is
§10 and the registry table is §11. Nothing was pushed.

**Labels.**
- [P] proved here
- [P-cite] proved from a cited claim or theorem
- [CA] computer-assisted
- [N] floating-point numerics
- [H] heuristic
- [assessment] opinion on strategy
- [constant arithmetic] evaluation of a closed-form expression (not evidence)

Inputs used as given: TRACE-206 (frozen definition), 198/199 (Line F, incl. F3), 212/213, 216, 221/222, 225/231/235/236 (D7, S⁺),
226 (L16), 228, 229, 230, 237 (K1), 238 (Prop K2), 241–246, and the Line L/L2/L3 reports.

## 0. Verdict

**No route to an unconditional refutation of frozen R′ was found.** Candidates (i)–(v) and four further ideas all fail, each for a
precise reason, and most of those reasons are proved below. Every route reduces to the same object as in Lines K and L: the
**signed open-level functional D_iso(q) − E_b(q)/q**, which has to be controlled one m at a time.

| # | Statement (v2 wording) | Label |
|---|---|---|
| M1 | gcd(h_m, h_n) = h_gcd(m,n) for odd m, n. Distinct m = 3p share only the conductor 7 | [P] (r(q) lemma: TRACE-230) |
| M2 | Positive-weight averaged H♮ ⇒ H♮ (δ/2) | [P]; the signed-weight remark is [assessment] |
| M3 | For m = 3p ≥ 495, ρ = (±2,8): d = h_p is included and open, and Prop K2's per-level floor there is ≥ c·1.13288^m ≫ the D7 demand. This is a no-go for positivity methods | [P] on Line F [CA] |
| M4a | The four P* families are disjoint for every odd m | [P] (Lean core) |
| M4b | (±2,8) inclusion rule = all d \| h, 1 < d ≤ √h, for odd m ≥ 15 | [P] on Line F F3 [CA]; [N] at m = 11, 13 |
| M4c | (±2,16) rule degenerates for m ≳ 85 | [N], open |
| M5 | Squares offset a cross deficit X at level d only if d ≳ \|Z_ρ\|²/X; sharp within the quadratic relaxation | [P] |
| M6 | ±ρ pairing law at all levels | [H] / conditional on C1–C4 |
| M7a | ord_c(λ) \| 3p for c \| h_{3p}; λ^p ≡ 1 mod 2h_p; p = 2 log_λ h_p + O(1) | [P] (Lean `lam_pow_eq`) |
| M7b | Relation to Kurlberg–Rudnick, Bourgain, BGK, FND | [P-cite + assessment] |

Precise obstruction [assessment]:
- Even the inherited level d = h_p, present for **every** m = 3p, is beyond reach of every positivity or Cauchy–Schwarz method,
  with margin (1.1124)^m (M3).
- So a refutation needs a signed equidistribution bound at h_p (and at the other open conductors below L_m), one m at a time.
- h_p is a minimal-period modulus (M7a), and the walk runs for m = 3p ≈ 6 log_λ h_p steps. That is beyond the Ehrenfest time, and
  no general principle applies there.

## 1. Exact bookkeeping [P-cite 206, 212, 213, J3]

W′_m = φ⁻¹[Σ_{ν non-res}(|Z(ν)|² − RMT) + Σ_{ρ, d incl}(cross_d(ρ) + sq_d(ρ))], with:
- sq_d ≥ 0;
- the bulk term ≥ −RMT;
- cross_q = 2Re(conj Z_ρ·(D_iso − E_b/q)) at a prime q ∥ h (K1).

Only cross parts can be negative of exponential size.

## 2. Candidate (i): averaged / Cesàro / Tauberian statements in m

**M1 [P] (M-F12).**
- *r(q) lemma (TRACE-230; J3 §4).* For odd m and an odd prime q: q | h_m ⇔ λ^m ≡ 1 (mod q) ⇔ r(q) | m. This uses ε^{2m} − 1 = 2h_m ε^m
  for odd m.
- *Valuations.* By lifting the exponent in O/q^k (hypotheses: q odd and unramified in Z[√2], i.e. q ≠ 2),
  v_q(h_m) = v_q(h_r) + v_q(m/r) for r = r(q) | m. Also 2 ∤ h_m. Hence gcd(h_m, h_n) = h_gcd(m,n).
- *Corollary.* On m = 3p every prime q ≠ 7 dividing h_m has r(q) ∈ {p, 3p}. So open conductors at distinct m = 3p are pairwise
  disjoint, and only 7 is shared.
  - Exception noted in TRACE-230: 49 | h_21 (p = 7, since ord_49(λ) = 21). For p ≠ 7, 49 ∤ h_{3p}.
- *Checks.*
  - [N]: 0 failures for odd m, n ≤ 301 (logs/m_checks_v2.log [1]).
  - Referee: m, n ≤ 601, plus LTE checks.
  - Lean: `strong_div_small` (odd m, n < 60), `nsw_three_mul` (general).

**M2 [P] (M-F8).**
- Setup:
  - Write D̃7_m := φ⁻¹·D7_m. By Theorem J3, D̃7_m ≥ 0.99·K_j·1.0184224^m > 0 on S⁺ for m ≥ M0(j).
  - Write Õ_m := φ⁻¹·O♮_m. Both use the same normalisation throughout.
  - Let c_m ≥ 0 on S⁺ with Σ_m c_m D̃7_m = ∞.
- Claim: if, for some δ ∈ (0,1), Σ_{m≤M} c_m(Õ_m + (1−δ)D̃7_m) ≥ 0 for infinitely many M, then Õ_m ≥ −(1−δ/2)D̃7_m for infinitely
  many m ∈ S⁺.
- Proof: otherwise, for all but finitely many m, Õ_m + (1−δ)D̃7_m < −(δ/2)D̃7_m. Then the partial sums are
  ≤ C − (δ/2)Σ_{m≤M} c_m D̃7_m → −∞, a contradiction. ∎
- So averaged H♮ implies H♮ with δ/2; an averaged hypothesis is never weaker.
- [assessment] With signed weights, R′ only gives Σ c_m W′_m = o(Σ|c_m| m). For c_m < 0 the bounds sq_d ≥ 0 and bulk ≥ −RMT cannot be
  dropped, so upper bounds on F_m-type sums would also be needed. I expect that to be harder, but it is not a theorem.
- [assessment] Any sequence satisfying R′ pointwise satisfies all averages of R′. This is a tautology about the **linear** consequences
  of R′. It does not show that a conspiracy is compatible with the nonlinear proven constraints (Theorem U Parseval, the sector law,
  M5).
- [assessment] Hence no Tauberian argument can refute R′ **from R′ and the linear D7 data alone**. By M1 the open data are disjoint
  across m, so there is no exact inter-m structure to exploit.

## 3. Candidate (ii): combining m with 3m, 9m, or residues mod 168 (M-F9)

- **m and 3m.** h_{3m} = h_m(4h_m² + 3) for every odd m (Lean `nsw_three_mul`).
  - (1+√2)^m mod 8 has period 8, and 3m ≢ m (mod 8) for odd m, so m and 3m fall in different operator cases (constants c_a).
  - These cases are unitarily intertwined (TRACE-216), so "different case" is not by itself an obstruction.
  - The real obstruction is L3 (S3): the phase of the larger index has a factor at level 4h_m² + 3, on which λ^m ≢ 1. So the Gauss
    side does not fold.
  - Numerically, |Ẑ^{(p)}|³ does not track |Ẑ^{(3p)}| (L3 S4).
- **m and 9m.** The shared conductors c | h_m are inherited.
  - At 9m their sums are Tr[R·Π_β⁹]; at the full period they are Tr[R·Π_β] (L3 S4 form). For non-normal, infinite-rank Π_β these do not
    determine each other.
  - m = 9p also brings in the fixed conductor 199 (rank 9), whose twisted radius 1.470 [N, J3 §4] exceeds the D7 rate.
  - [assessment] There is no contradictory constraint.
- **Residues mod 168 / p₀ mod 56.** These only select B_j. The open data stay disjoint (M1).

## 4. Candidate (iii): the frozen inclusion rule

**M4a (family disjointness) [P] (M-F3).**
- If a unit ν lies in families ρ = (a,b) at level d and ρ′ = (a′,b′) at level d′ (d, d′ ≤ √h, primaries d = 1 included), the
  congruences 4ν ≡ ±1 and 8ν ≡ ±1 mod h/d (resp. h/d′) force gcd(h/d, h/d′) | 3.
- 3 ∤ h_m for odd m: 3 | h would give 2y² ≡ 1 mod 3, which is impossible (Lean `three_not_dvd_nsw`). Hence gcd = 1.
- Then (h/d)(h/d′) | h (Lean `coprime_core`), i.e. dd′ ≥ h. With d, d′ ≤ √h this forces d = d′ = √h. Then h/d is coprime to itself,
  so h/d = 1 and h = 1, which is impossible.
- So no unit lies in two families, and each family has exactly one primary.
- *Check [N, exact enumeration]* (logs/m_checks_v2.log [4]):
  - Every unit ν mod 2h was tested against all four families, with exact level d_ρ(ν) = 2h/gcd(bν − a, 2h), for odd m = 5…17.
  - 0 units lie in ≥ 2 families with levels ≤ √h (primaries included), and each family has exactly one primary.
  - This replaces the v1 §4 loop, which only re-tested the gcd arithmetic.
  - The referee's ref_m.py [9] (m = 5…19) agrees.

**M4b ((±2,8) degeneration) (M-F1).**
- Line F F3 (TRACE-198/199) gives |Z_ρ| ≥ ½(1 − λ^{−m})(μ_lo^m − 3012.4), with μ_lo = 1.9154712.
- With this certified bound, |Z_ρ|² ≥ 4m·h_m holds for every odd m in [15, 20001] (code/m_incl_v2.py, logs/m_incl_v2.log;
  mpmath 60 digits). Beyond that it is monotone, since the ratio grows like (μ_lo/λ^{1/4})^m/√m = 1.2328^m/√m.
- So for odd m ≥ 15, every d | h with 1 < d ≤ √h satisfies |Z_ρ|²/d² ≥ 4m [P on Line F [CA]].
- At m = 11, 13 the certified bound is insufficient. Float values (Line G growth_law, ratios 1.13 and 2.22) give the same conclusion
  there [N]. At m = 9 it fails.
- So for (±2,8) and odd m ≥ 15 no level is borderline.

**M4c ((±2,16)) [N] (M-F2).**
- The (±2,16) rule is **not** degenerate at small or moderate m. The float |Z_16|² < 4mh for every m ≤ 29 (a gap of ×24 at m = 29),
  and the crossover extrapolated from the float rate 1.615 is m ≈ 85.
- No certified lower bound on |Z_16| exists (TRACE-238 has only an upper bound). So "no borderline level" is restricted to (±2,8).
- For (±2,16) the cut-off d* = |Z_16|/(2√m) < √h is genuine at moderate m. It does not help a refutation, because levels above d* go
  to the bulk, which is ≥ −RMT.

**Conclusion.** For (±2,8) the frozen rule's only artifact is that the member main term |Z_ρ|²/d² omits the cross term: Theorem J at
d = 7, and O♮ everywhere else.

## 5. Candidate (iv): positivity / sum-of-squares structure of F_m

**M5 [P].** At any included level d (prime or composite), put X_ν := Z(ν) − Z_ρ/d for the members and S := Σ_{ν∈M_d} X_ν.
- Then Dev_d = 2Re(conj Z_ρ·S)/d + Σ|X_ν|². This is pure algebra, since the G3 main term is exactly Z_ρ/d. G3/K1 is needed only to
  name S as D_iso − E_b/q.
- Cauchy–Schwarz gives Σ|X_ν|² ≥ |S|²/n_d.
- For a cross value −X one needs |S| ≥ dX/(2|Z_ρ|), so sq_d ≥ d²X²/(4|Z_ρ|² n_d) ≈ dX²/(4|Z_ρ|²).
- This offsets X only if d ≳ 4|Z_ρ|²/X. With X ≍ φ·1.0184^m this is the base μ*²/ξ_lo = 1.4923 of L_m.
- Minimising over S gives exactly −n_d|Z_ρ|²/d², which is Prop K2's per-level bound (TRACE-238).
- "Sharp" means sharp within this quadratic relaxation (equality when all X_ν are equal).
- Any Cauchy–Schwarz lower bound with a test vector reduces, to first order, to the same linear functional S.
- The referee checked the decomposition on random data, with max relative error 4e−14.

**M3 (inherited-level no-go for positivity methods) [P on Line F [CA]] (M-F1, M-F5).**

*Scope.* m = 3p ≥ 495, ρ = (±2,8).
- (a) **Inclusion.** h_p | h_{3p} (M1), and h_p ≤ √h_{3p}. By M4b (m ≥ 15), level h_p is included.
- (b) **Openness** (TRACE-246 definition). h_p is composite or prime with h_p ≫ c_W p², it is not in {1, 7} ∪ {q, 7q : q ≤ c_W p²},
  and its conductor-h_p part is not absorbed for m below the K2 crossover. In general, openness of the conductor-h_p part is all that
  is used.
  - v1's "h_p < L_m < √h" is dropped (M-F5d): the second inequality needs η_m < 0.1009, i.e. p ≳ 2.2e8, and it is not needed.
- (c) **The floor.** Dev_{h_p} ≥ −n_{h_p}|Z_ρ|²/h_p² is Prop K2's per-level bound, i.e. the magnitude of the frozen main term at that
  level.
  - n_{h_p}/h_p → 1: n_q = q − 2 for q ∥ h (TRACE-228); every q | h_p has q ≡ 1 mod 2p (J3 §4 corollary); ω(h_p) ≤ log h_p/log(2p+1).
    Hence n_{h_p}/h_p ≥ 1 − 2ω(h_p)/(2p+1) → 1.
  - [N] check for p ≤ 61 (logs/m_checks_v2.log [6]): all h_p are squarefree, q ≡ 1 mod 2p, n/h_p ∈ [0.908, 1], and the bound holds.
  - With |Z_ρ| ≥ ½(1−λ^{−m})(μ_lo^m − 3012.4) and φ ≤ h, the floor in units of φ is ≥ c·(μ_lo²/λ^{2/3})^m = c·1.13288^m. That exceeds the
    D7 demand 0.99·K_j·1.0184224^m by (1.11239)^m [constant arithmetic].
- (d) **Meaning.** No positivity or Cauchy–Schwarz bound at d = h_p can force the cross part there above the D7 demand. This is a
  no-go for the method. It does **not** show that a conspiracy is realisable.
- (e) **Prime factors of h_p** (M-F5c). The same capacity statement holds for each prime factor q | h_p (its floor ≍ 1.52^m/q is even
  larger). But such factors need not be open: small factors occur (23 | h_11, 47 | h_23, 79 | h_13), and those lie in the Weil range
  for large p.
- The v1 "numerics, stable to 5 digits" was a closed-form evaluation and is relabelled [constant arithmetic] (M-F4).

**Fixed-conductor squares.**
- Example: conductor 239 (rank 7), radius 1.566 > λ^{1/4} [N, J3], square rate 1.566²/√λ ≈ 1.0158 per step.
- These are positive and growing, but far below the same capacity [assessment].

## 6. Candidate (v): equivalence theorem and known equidistribution results (M-F7)

**Equivalence.** Only "frozen R′ ⇒ conspiracy" is available (K3, K2′, M3). The converse needs the bulk asymptotics, which is R′'s own
content and is open. So there is no "⇔" theorem.

**M7a (arithmetic) [P].**
- For c | h_{3p}: λ^{3p} ≡ 1 mod c, so ord_c(λ) | 3p (r(q) lemma).
- λ^p = 1 + 2h_p ε^p for odd p (Lean `lam_pow_eq`, a ring identity). So λ^p ≡ 1 mod 2h_p, and the referee checked λ^p ≢ 1 mod 4h_p
  for p ≤ 61.
- p = 2 log_λ h_p + 2 log_λ 2 + o(1).
- Every open prime conductor q | h_{3p} has ord_q(λ) ≤ 3p < q.

**M7b (literature) [P-cite + assessment].** All results below concern eigenfunctions of the **unkicked** quantized cat map. They are
not about the kicked R′ functional. Only their arithmetic input (exponential sums over the orbit subgroup) is relevant here.
- **Kurlberg–Rudnick**, "On quantum ergodicity for linear maps of the torus", Comm. Math. Phys. (2001).
  - Volume: the referee gives 221; my recollection is 222, pp. 201–227. To be checked against the publisher before registration.
  - Their condition is ord(A,N)/(N^{1/2}(log N)^7) → ∞ (plus genericity). Density one comes from ord ≫ N^{1/2}·exp((log N)^δ) for
    almost all N.
  - Open conductors have ord ≤ 3p, while q > c_W p². So KR's condition fails as soon as q ≥ C p² (log q)^{14}, i.e. on essentially the
    whole open range. It also fails for the composite modulus h_p, where ord = p ≈ 2 log_λ h_p.
- **Bourgain**, "A remark on quantum ergodicity for CAT maps", GAFA Seminar, LNM 1910 (2007), and **Bourgain–Glibichuk–Konyagin**,
  J. London Math. Soc. (2) 73 (2006).
  - What they give: for a prime modulus q with ord(λ, q) > q^ε, a power saving for exponential sums over the orbit subgroup (via
    Bourgain, "Mordell's exponential sum estimate revisited", JAMS 18 (2005), and BGK).
  - Here |H| = r(q) ∈ {p, 3p} and q ≤ p^C give ord ≥ q^{1/C}. So for **prime** conductors c_W p² < q ≤ p^C the arithmetic input is
    available, ineffectively, as Lines K/L state: a Theorem-W-type o(r) bound. This partially covers the bottom of the open range.
  - What they do not give: anything for q > p^C for every fixed C. In particular nothing for q up to L_m = e^{Θ(p)}, where
    |H| ≈ log q.
  - Nothing is claimed here about composite moduli such as h_p.
  - Since h_p is present for every m = 3p (M3), no density-one set of m avoids the uncovered regime.
- **Faure–Nonnenmacher–De Bièvre**, "Scarred eigenstates for quantum cat maps of minimal periods", Comm. Math. Phys. 239 (2003)
  449–492.
  - h_p is a minimal-period modulus in their sense (M7a), where half-scarred eigenstates exist for the unkicked map.
  - This is an analogy for the kicked functional, not an implication [assessment].

## 7. Further candidates

- **(a) ±ρ pairing (M6) [H; conditional on C1–C4] (M-F6).**
  - Assume TRACE-222's antiunitary RK maps the + family to the − family at every conductor, with sector shift a ↦ a+4 and the same β,
    and that c⁻_{a+4} = s_a·conj c⁺_a (s = −1 on sectors {0,4}, +1 on {2,6}).
  - Then cross₊ + cross₋ = 2Re Σ_{a,b} conj(c_a z_a)·c_b y_b·(1 + s_a s_b).
  - Pairs (primary sector a, twisted sector b) with s_a ≠ s_b cancel; pairs with s_a = s_b double. This includes {2,6}×{2,6}, which v1's
    table had wrong.
  - The d = 7 "sectors 2,6 cancel" statement refers to pairs with the primary's top sector (s = −1). The primary sectors with s = +1
    have spectrum inside |z| < 1 (TRACE-198), so they are subdominant but not zero.
  - The dominant {0,4}×{0,4} part survives, so O♮ does not vanish identically.
  - The sign algebra was checked by the referee (error 3e−15).
  - Closure conditions:
    - **C1.** RK conjugation extended to the non-autonomous products L_{τ_{m−1}}⋯L_{τ_0} at conductor c, factor by factor.
    - **C2.** The sector law and c⁻_{a+4} = s_a conj c⁺_a are level-independent (TRACE-221(i) is scoped to d = 7).
    - **C3.** W_{c,β}(−ρ) = conj W_{c,β}(ρ) at every included level. At prime q ∥ h this follows from TRACE-229 if t_b(−ρ) = −t_b(ρ);
      composite levels then follow via TRACE-228.
    - **C4.** Scope is (±2,8) only (the (±2,16) read-out differs, TRACE-226).
  - Not registered as proved.
- **(b) Other fixed conductors** (41, 199, 239 on m ≡ 0 mod 5, 9, 7).
  - Their twisted radii are 1.47–1.57 [N, J3 §4], above the D7 rate.
  - Same structure as D7, and far below the open capacity. On m = 15p the floor at h_p is ≍ (μ*²/λ^{1/2+1/30})^m = 1.43^m
    [constant arithmetic] [assessment].
- **(c) Kick-parameter averaging** (over η or a shift θ). This changes the conjecture and is not a refutation of TRACE-206
  [assessment].
- **(d) Quantum dictionary [framing / H] (M-F10).**
  - Theorem U has the form of operator Parseval for a unitary on C^h. Read as Ẑ_β = Tr(U^m T_β), the quantity D_𝔮 becomes
    Tr(ΠU^mΠ) − Tr(U^m)/q for a rank-h/q projector Π.
  - No such unitary was constructed. The completing-the-square recentring Ẑ_β = e(c·Nm x₀/2h)·Σ_n Φ̂(n)χ(α_n − x₀), with
    x₀ ∈ (2h/q)O^∨, is a [P-sketch]: a one-line completion of the square, not written out in full and not P-checked.
- **(e) Norm-one correlation form [P-sketch / framing] (M-F10).**
  - [P] Σ_{ν mod 2h}|Z(ν)|² = 2h·Σ_{Nm x ≡ Nm x′ (2h)} B(x)conj B(x′), using P(n) ≡ y′Nm(α_n) (mod 2h) (L3 S1).
  - [P] B∘λ = B, from the cyclic shift and λ^m ≡ 1 mod 2h.
  - On unit pairs x′ = γx with Nm γ = 1, giving Σ_γ C(γ), C(γ) = ⟨B, B∘γ⟩ restricted to units.
  - The **reversal** x ↦ x̄ is not multiplication by a fixed γ. Its pairs are already among the γ-pairs (γ = x̄/x depends on x), so v1's
    statement "⟨λ⟩ and the reversal give exactly 2mΣ|B|²" double-counts and is withdrawn.
  - The non-unit part (x not invertible mod 2h) is not treated.
  - Sums of C over congruence subgroups are ≥ 0, which is the γ-side of M5.
  - Framing only; no estimate.

## 8. What a positive route would have to do [assessment] (M-F11)

1. It must work one m at a time (M2) and with signs (M5).
2. It must give, at the inherited modulus h_p and at every other open conductor below L_m, the bound
   |D_iso − E_b/q| ≤ ((1−δ)·1.28359)^m, averaged over conductors. In L3 form this is a mean of Tr[R·Π_β³] over isotropic β at rank-p
   levels.
3. The bottom of the prime open range (q ≤ p^C) has Bourgain/BGK input (ineffective, M7b). The top does not.
4. Numerics (L2, m ≤ 51 only): isotropic |D|^{1/m} = 0.94–1.12 at inherited levels, and the full K1 functional's worst case is
   1.178 at (21,239). Both are below 1.28. So "R′ is very likely false" is an [assessment] on m ≤ 51 data.
5. The input needed is a scarring-regime equidistribution statement specific to the kick e^{1.8i cos}.

## 9. Files

All in /workspace/bgs-lineM.
- `code/m_checks.py` and `logs/m_checks.log`: v1, pinned and unchanged. Its log ends in the p = 199 KeyError.
- `code/m_checks_v2.py` → `logs/m_checks_v2.log` (M-F4, M-F3, M-F5b):
  - h_m by fast powering in Z[√2], cross-checked against the v1 recurrence;
  - strong divisibility, 3 ∤ h, the h_{3p} identity for p < 433;
  - membership enumeration for m = 5…17;
  - capacity bases [constant arithmetic] for p up to 199;
  - n_{h_p}/h_p for p ≤ 61.
- `code/m_incl.py` and `logs/m_incl.log`: v1, unchanged. `code/m_incl_v2.py` → `logs/m_incl_v2.log`: the certified m ≥ 15 threshold
  (M-F1).
- `lean/LineMArith.lean`: the referee's file, byte-identical copy.
  - Compiled with `lake env lean` in /workspace/lineL-integ/integ/formalization. That tree's Bgs/LineIArith.lean, Bgs/LineG.lean,
    lean-toolchain and lake-manifest.json are byte-identical to the repo clone.
  - Exit 0. No sorry, no native_decide. Axioms listed in `logs/lean_LineMArith.log`.
- `REPORT_M.md` (v1, unchanged), `REPORT_M_v2.md` (this file), `NOTES_M.md`, `claims_extract.txt`, `SHA256_M.txt`.

## 10. Errata (v1 → v2)

| Fix | Where | Change |
|---|---|---|
| M-F1 | M3, M4b, m_incl | "(½ − o(1))μ*^m … from m ≥ 11 [P]" → [P] for odd m ≥ 15 via Line F F3 ½(1−λ^{−m})(μ_lo^m − 3012.4) (m_incl_v2.py); [N] at m = 11, 13 (ratios 1.13, 2.22) |
| M-F2 | M4c | (±2,16) rule is not degenerate for m ≲ 85 (float \|Z_16\|² < 4mh for m ≤ 29; extrapolated crossover m ≈ 85); [N] only; "no borderline level" restricted to (±2,8) |
| M-F3 | M4a | Last step corrected (dd′ ≥ h ⇒ d = d′ = √h ⇒ h/d self-coprime ⇒ h = 1); primaries included; v1 loop replaced by direct membership enumeration (m_checks_v2 [4]) |
| M-F4 | m_checks | New m_checks_v2.py (h to m < 1300; p = 199 runs); capacity column relabelled [constant arithmetic]; "stable to 5 digits" dropped; v1 script and log kept pinned |
| M-F5 | M3 | (a) floor identified as Prop K2 per-level bound, M3 = no-go for positivity methods; (b) n_{h_p}/h_p → 1 argument added (+ [N] p ≤ 61); (c) "every prime factor" restricted to capacity (23 \| h_11 etc. are Weil-range); (d) "L_m < √h" dropped; (e) scope m = 3p ≥ 495, ρ = (±2,8) |
| M-F6 | M6, §7(a) | Table corrected: s_a ≠ s_b pairs cancel, s_a = s_b pairs double (incl. {2,6}×{2,6}); d = 7 statement refers to the primary-top pairs; relabelled [H] / conditional on C1–C4; not registered as proved |
| M-F7 | M7 | Split into M7a [P] and M7b [P-cite + assessment]; KR condition stated correctly; Bourgain LNM 1910 reaches prime q ≤ p^C (ineffective); "never reach" restricted to q > p^C ∀C and to composite h_p (no claim); BGK spelled out (JLMS 2006) and Bourgain JAMS 18 (2005) cited; unkicked-map caveat; FND cited in full |
| M-F8 | M2 | One normalisation (φ⁻¹) in hypothesis and divergence; D̃7_m > 0 on S⁺ stated; "strictly harder" and conspiracy-consistency → [assessment] (tautology about linear consequences); Tauberian remark qualified "from R′ and D7 linear data alone" |
| M-F9 | §3 | TRACE-216 intertwiners noted; "different operator case" is not by itself the obstruction; L3 S3 non-folding is |
| M-F10 | §7(d), (e) | Relabelled [P-sketch]/framing; reversal double counting withdrawn; non-unit part flagged as untreated |
| M-F11 | §8.4 | 1.178 (full K1, L2) quoted alongside 0.94–1.12 (isotropic); "very likely false" → [assessment] on m ≤ 51 data |
| M-F12 | M1 | TRACE-230 credited for the r(q) lemma; LTE hypotheses (q odd, unramified) stated; 49 \| h_21 and 49 ∤ h_{3p} (p ≠ 7) noted |

## 11. Claims table (matches the referee's registry recommendations)

| Proposed claim | State | Basis / closure |
|---|---|---|
| M1 strong divisibility (odd indices) + disjointness of conductors across m = 3p | **proved** | Paper (TRACE-230 + LTE). Lean finite range (`strong_div_small`) and 3 ∤ h |
| M2 averaging lemma (positive weights ⇒ H♮ with δ/2) | **proved** | Elementary. The signed-weight remark is not registered |
| M3 inherited-level no-go: m = 3p ≥ 495, ρ = (±2,8); d = h_p included and open; K2 per-level floor at h_p ≥ c·1.1328^m ≫ D7 demand | **proved** (structural no-go; not a refutation) | Inputs: Line F F3, TRACE-228/230/238/246 |
| M4a family disjointness for P* (all odd m) | **proved** | Lean core `three_not_dvd_nsw`, `coprime_core`; enumeration m = 5…17 |
| M4b (±2,8) rule = all d ≤ √h for odd m ≥ 15 | **proved** (on Line F [CA]) | m = 11, 13 [N] |
| M4c (±2,16) rule degenerates for m ≳ 85 | **open** (float evidence) | Closure: a certified \|Z_16\| ≥ c·r^m with r² > √λ |
| M5 Cauchy–Schwarz sharpness of positivity (d ≳ \|Z\|²/X) | **proved** | Register as a refinement/annotation of TRACE-238 |
| M6 ±ρ pairing law at all levels | **open** (conditional) | Closure: C1–C3 for (±2,8) at squarefree levels (C4 scope) |
| M7a arithmetic (ord \| 3p; λ^p ≡ 1 mod 2h_p; p = 2log_λ h_p + O(1)) | **proved** | Lean `lam_pow_eq`. The M7b literature sentence is an annotation, not a claim |
| "Every refutation needs a signed equidistribution theorem at h_p" | not a claim | [assessment], prose only |

TRACE-206 (frozen R′) stays **open**. Line M changes no existing registry state.
