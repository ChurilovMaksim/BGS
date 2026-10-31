# Line M report: fresh-eyes search for a different route to refuting frozen R′ (TRACE-206)

31 Oct 2026 (Asia/Yekaterinburg, UTC+5). Work directory /workspace/bgs-lineM. Nothing was pushed.
Labels: [P] proved here (paper), [P-cite] proved from a cited claim, [N] numerics, [H] heuristic, [assessment] opinion on strategy.
Inputs used as given: TRACE-206 (frozen definition), 212/213 (reduction), 221/222 (sector law, antiunitary RK), 225/231/235/236
(D7, S⁺), 237 (K1), 238 (Prop K2), 241–246 (Weil range), the Line L/L2/L3 reports.

## 0. Verdict

**I found no route to an unconditional refutation.** Candidates (i)–(v) and four of my own ideas all fail. Each fails for a reason
that can be stated precisely, and most of those reasons are proved below. Every route I tried comes back to the same object as
Lines K and L: the **signed linear functional D_iso(q) − E_b(q)/q at open levels**. No averaging over m, combination of different
m, sign identity or positivity argument changes it.

New results. They are structural and do not refute R′.

| # | Statement | Label | Kills |
|---|---|---|---|
| M1 | Strong divisibility: gcd(h_m, h_n) = h_gcd(m,n) for odd m, n. Open conductors of h_{3p} and h_{3p′} (p ≠ p′) are disjoint, except 7 | [P] + [N] check | (i), (ii) as an exact link |
| M2 | Averaging is never easier. With positive weights, averaged H♮ ⇒ H♮. With signed weights, the positivity of the square and bulk terms is lost | [P] | (i) |
| M3 | Inherited-level capacity: for every m = 3p, the level h_p is included and open. Its positivity floor is ≥ c·1.13288^m, against a D7 demand of ≍ 1.0184^m | [P] + Line F input | (iii), (iv), every per-level positivity argument |
| M4 | For large m the frozen inclusion rule is just {d \| h : 1 < d ≤ √h} for (±2,8), and the four families never share a member | [P] (3 ∤ h_m) + Line F input | (iii) |
| M5 | Fiber minimisation: square parts can offset a cross deficit X at a prime level q only if q ≳ \|Z\|²/X. That is exactly the base of L_m, so the positivity threshold is sharp | [P] | (iv) |
| M6 | ρ ↔ −ρ: at every conductor, the cross terms in twisted sectors 2 and 6 cancel exactly between ±ρ; sectors 0 and 4 double | [P-sketch from TRACE-222; not checked numerically at open levels] | hope that O♮ vanishes identically |
| M7 | Every open conductor has ord(λ) ≤ 3p. The conductor h_p has ord = p = 2 log_λ h_p + O(1), the FND minimal-period regime. Density-one theorems (Kurlberg–Rudnick, Bourgain) never reach these conductors, for any m | [P] | (v) |

Precise obstruction [assessment, sharpened by M3 and M7]:
- Even the single inherited level d = h_p could absorb D7 by itself, with an exponential margin of (1.1124)^m.
- So any refutation must prove a **signed** equidistribution statement for the TRACE-206 measure at the inherited modulus h_p, or at
  its prime factors. This holds for all large p in S⁺, and must be done one m at a time.
- h_p is a minimal-period (Faure–Nonnenmacher–De Bièvre) modulus for λ, and the walk has length m = 3p ≈ 6 log_λ h_p.
- That is beyond the Ehrenfest time, and no general principle is available there. I agree with the author's assessment and make it
  sharper: the obstruction is present for **every** m in the D7 family, not just generically.

## 1. Exact bookkeeping used throughout [P-cite 206, 212, 213, J3]

W′_m = φ⁻¹[Σ_{ν non-res}(|Z(ν)|² − RMT) + Σ_{ρ, d incl} (cross_d(ρ) + sq_d(ρ))], with:
- sq_d ≥ 0;
- the bulk term ≥ −RMT;
- cross_q = 2Re(conj Z_ρ·(D_iso − E_b/q)) at prime q ∥ h (K1).

The only negative terms of exponential size are cross parts. Every route below has to say something about them.

## 2. Candidate (i): averaged / Cesàro / Tauberian statements in m

**M1 (strong divisibility) [P].**
- For odd m, ε = 1+√2 and q an odd prime: q | h_m ⇔ λ^m ≡ 1 (mod q) ⇔ r(q) | m (J3 §4 lemma).
- Valuations follow from lifting the exponent in O/q^k, so gcd(h_m, h_n) = h_gcd(m,n).
- Check [N]: 0 failures for all odd m, n ≤ 301 (logs/m_checks.log). The identity h_{3p} = h_p(4h_p² + 3) also checks for p < 130.
- Corollary [P]: on m = 3p, every prime q ≠ 7 dividing h_m has r(q) ∈ {p, 3p}. So the open conductors at different m = 3p are
  **pairwise disjoint**. The only conductor common to the whole D7 family is 7.

**M2 (averaging is no easier) [P].** Let c_m ≥ 0 on S⁺ with Σ c_m D7_m/φ → ∞.
- Suppose, for some δ, Σ_{m≤M} c_m(O♮_m + (1−δ)D7_m) ≥ 0 for infinitely many M.
- Suppose also that only finitely many m had O♮_m ≥ −(1−δ/2)D7_m. Then the partial sums would be ≤ C − (δ/2)Σ c_m D7_m → −∞, a
  contradiction.
- So averaged H♮ ⇒ H♮ (with δ/2). An averaged hypothesis is at least as strong as the pointwise one.
- With signed weights (c_m = cos(arg B_j + m arg ξ), Fejér kernels, Dirichlet-series weights), R′ only gives
  Σ c_m W′_m = o(Σ|c_m| m). For c_m < 0 the terms sq_d ≥ 0 and bulk ≥ −RMT can no longer be dropped. So one additionally needs
  **upper** bounds on F_m-type quantities to relative precision 1.0184^m/1.52^m. That is strictly harder.

**Why no orthogonality in m can appear [assessment, on M1].**
- Orthogonality would need O♮_m to have exploitable m-structure, for example an exponential-polynomial profile as at fixed
  conductors (G2).
- By M1, O♮_m is built from conductors that occur at that m only.
- The pointwise "conspiracy model" O♮_m := −D7_m − (squares) satisfies every linear relation among the W′_m that R′ implies.
- So no Tauberian argument can produce a contradiction from R′ plus D7 alone. Some per-m input on O♮ is unavoidable.

## 3. Candidate (ii): combining m with 3m, 9m, or different residues mod 168

- **m and 3m.** h_{3m} = h_m(4h_m² + 3).
  - The m = 3m′ phase has a factor at level K = 4h_m² + 3, on which λ^m ≢ 1. So the Gauss side does not fold (L3 S3).
  - The automaton constants depend on (h, y′) mod 8, i.e. on m mod 4 (TRACE-216, period 8 in m). For odd m, 3m ≢ m (mod 4), so
    m and 3m are always in **different operator cases** [P]. That is the L3 failure.
- **m and 9m** (same case mod 8, both ≡ 3 mod 6).
  - The shared conductors c | h_m are inherited.
  - At 9m their twisted sums are Tr[R·Π_β⁹], and at m (full period) they are Tr[R·Π_β] [L3 S4 form].
  - For a non-normal infinite-rank Π_β, Tr Π and Tr Π⁹ do not determine each other. R′(m) and R′(9m) constrain different D7 phases
    and different open data.
  - Moreover, m = 9p introduces the fixed conductor 199 (rank 9). Its twisted radius, 1.470 [N, J3 §4], is above the D7 rate, so
    the D7 lever is replaced rather than reinforced.
- **Residues mod 168 / p₀ mod 56.** These only choose which B_j enters. The open data are still disjoint (M1).
- **Conclusion:** combinations of m give no contradictory constraints [P for the structural facts, assessment for "no route"].

## 4. Candidate (iii): the frozen inclusion rule

**M4 [P + Line F input].**
- With |Z_ρ| ≥ (½ − o(1))μ*^m (Line F, (±2,8)), |Z_ρ|²/d² ≥ 4m holds for **every** d ≤ √h as soon as |Z_ρ|² ≥ 4mh. That is true
  for all odd m ≥ 11 (code/m_incl.py; asymptotically (μ*²/λ^{1/2})^m = 1.52^m).
- So for (±2,8) the rule is just "all d | h, 1 < d ≤ √h". No level is borderline, and there is no discontinuity to exploit.
- For (±2,16) the same holds if the float rate 1.615 is right, since 1.615² > √λ [N].
- No overlaps [P]:
  - A member shared by two families forces gcd(h/d, h/d′) | 3 (the congruences 4ν ≡ ±1 and 8ν ≡ ±1 differ by 2, 3 or 1).
  - 3 ∤ h_m for odd m, because λ ≡ −√2 has order 4 in F₉.
  - So gcd = 1, which forces dd′ ≥ h. With d, d′ ≤ √h this means d = d′ = 1.
  - Exhaustive check, m = 9…39: 0 cases.
- So the frozen rule has exactly one artifact: the member main term |Z_ρ|²/d² leaves out the cross term. At d = 7 that is
  Theorem J; at every other level it is O♮.

## 5. Candidate (iv): positivity / sum-of-squares structure of F_m

**M5 (fiber minimisation) [P].** At a prime level q ∥ h, put X_ν := Z(ν) − Z_ρ/q for each member, and S := Σ_{ν∈M_q} X_ν.
- The G3 main term is exactly Z_ρ/q, because |G_q| = q and the phase is trivial for q ≡ ±1 mod 8.
- Then cross_q = 2Re(conj Z_ρ·S)/q and sq_q = Σ|X_ν|² ≥ |S|²/n_q (Cauchy–Schwarz).
- For a cross value −X one needs |S| ≥ qX/(2|Z_ρ|), so sq_q ≥ q²X²/(4|Z_ρ|²n_q) ≈ qX²/(4|Z_ρ|²).
- This offsets X only if q ≳ |Z_ρ|²/X. With X ≍ φ·1.0184^m that is q ≳ (μ*²/ξ)^m, exactly the base of L_m.
- So positivity reproduces Prop K2 and nothing below it.
- Any Cauchy–Schwarz lower bound Σ_{ν∈M}|Z|² ≥ |Σ c̄_ν Z(ν)|²/‖c‖² reduces, to first order, to the same linear functional S.
  (The full-fiber "deficit identity" of REPORT_L_v2 §5d is not needed and stays [H].)

**M3 (inherited-level capacity) [P + Line F input].**
- For m = 3p, the level d = h_p divides h_m (M1). It satisfies 2p+1 ≤ h_p ≈ λ^{m/6} = 1.342^m < L_m ≈ 1.4923^{m(1+η)} < √h. So it is
  included and open for every large p (Weil range: h_p ≫ c_W p²).
- Its positivity floor is n_{h_p}|Z_ρ|²/(h_p² φ) ≥ (1−o(1))·|Z_ρ|²/(h_p h) ≈ (μ*²/λ^{2/3})^m = 1.13288^m, computed in
  logs/m_checks.log (stable to 5 digits for p = 11…101).
- That exceeds the D7 demand K·1.0184^m by (1.1124)^m, and the same holds for every prime factor of h_p.
- Smaller open primes give even larger floors, ≍ 1.52^m/q.
- The point of M3: this happens for **every** p, with an explicit, always-present level whose structure is known (λ^p ≡ 1 mod 2h_p).
  So no choice of a subsequence inside {3p} can avoid it. So positivity can never
  remove the inherited level, for any p, and no sign or positivity identity of F_m can close the argument.
- Fixed-conductor squares give growing positive terms, e.g. conductor 239 (rank 7) with radius 1.566 > λ^{1/4} [N, J3], square
  rate 1.566²/√λ = 1.0158 per step. They are absorbed by the same capacity.

## 6. Candidate (v): equivalence theorem and known equidistribution theorems

- **Equivalence.** Only "frozen R′ ⇒ conspiracy" is provable: Theorem K3, K2′ and M3. The converse needs the bulk asymptotics
  (1/φ)Σ_{non-res}(|Z|² − RMT) = o(m), which is R′'s own content and is open. So no "⇔" theorem is available [P: the converse
  direction carries R′'s bulk statement].
- **M7 [P].**
  - Every open prime conductor q | h_{3p} has |⟨λ mod q⟩| = r(q) ≤ 3p, while q > c_W p². So q is outside the Kurlberg–Rudnick
    density-one set (which needs ord ≥ q^{1/2+ε}) as soon as q > (3p)^{2+ε}. Above p^C it is outside the Bourgain / BGK range.
  - The composite conductor h_p has ord = p with λ^p ≡ 1 (mod 2h_p) and p = 2 log_λ h_p + O(1). This is exactly the FND
    minimal-period regime, where half-scarred eigenstates exist for the unkicked map.
  - Such a conductor is present for **every** m = 3p (M3). So there is no density-one set of m on which density-one-in-q theorems
    could apply.
  - Prime conductors with ord ≤ C(log q)^A form a set of primes of density 0 (they divide Π_{r≤R}(λ^r − 1)). The relevant moduli
    are precisely the exceptional set of those theorems.

## 7. My own additional candidates

- **(a) ±ρ symmetry (M6) [P-sketch].**
  - The antiunitary RK maps V^{(+2)}_{β,a} to V^{(−2)}_{β,a+4} with the **same** β, for any twist, at any conductor.
  - W(−ρ) = conj W(ρ), and W depends on β only through N(β) at prime levels (J3 §3).
  - Hence, exactly, cross₊ + cross₋ = Σ_{a,b} conj(c_a)c_b(1 + s_a s_b)·(…), with s = −1 on sectors {0,4} and +1 on {2,6}.
  - Caveat: I checked the sign algebra (c⁻_{a+4} = s_a·conj c⁺_a ⇒ coefficient conj(c_a)c_b(1 + s_a s_b)). I did not check
    W(−ρ)_β = conj W(ρ)_{±β} at composite levels.
  - Mixed pairs cancel at every open level. This generalises the d = 7 "1:3" cancellation, but the {0,4}×{0,4} part (which contains
    the primary's top) survives. So O♮ does **not** vanish identically, and this route closes nothing.
- **(b) Other fixed conductors** (41, 199, 239 on m ≡ 0 mod 5, 9, 7).
  - These have larger twisted radii (1.47–1.57 [N]) than D7, but the same structure: certified positive or oscillating terms of size
    ≪ the open capacity. On m = 15p, for example, the capacity of h_p is (μ*²/λ^{1/2+1/30})^m = 1.43^m.
  - So they add levers without removing the open part.
- **(c) Kick-parameter averaging** (over η or a shift θ, g(t+θ)).
  - Orthogonality in θ projects onto Σn = Σn′ and could give mean-square control over θ.
  - But frozen R′ fixes θ = 0, η = 2. Averaged versions are different conjectures, so this is not a refutation of TRACE-206
    [assessment].
- **(d) Quantum dictionary [H, not verified].**
  - Theorem U (Σ_{β mod h}|Ẑ(β/h)|² = h²) has the form of operator Parseval for a unitary on C^h.
  - Read that way, Ẑ_β = Tr(U^m T_β), and D_𝔮 = Tr(Π U^m Π) − Tr(U^m)/q, with Π the rank-h/q projector of the isotropic
    translation subgroup ℓ(𝔮).
  - The trivial bound 4h/q is then the rank bound, and H_mean is quantum equidistribution of the q block traces of U^m at time
    m ≈ 2T_E (6 T_E for the inherited modulus).
  - Elementary part [P]: completing the square shows Ẑ_β = e(c·Nm x₀/2h)·Σ_nΦ̂(n)χ(α_n − x₀), with x₀ ∈ (2h/q)O^∨. So the twisted sums
    are TRACE-206 sums with the walk recentred at q-torsion points.
  - This is a framing only; it gives no estimate.

- **(e) Norm-one correlation (Gram) form [P, elementary].**
  - From P(n) ≡ y′Nm(α_n) (mod 2h) (L3 S1): Σ_{ν mod 2h}|Z(ν)|² = 2h·Σ_{x,x′∈O/2h, Nm x ≡ Nm x′} B(x)·conj B(x′), where B is the walk
    law mod 2h with |B̂| ≡ 1.
  - B∘λ = B and B(x̄) = B(x) (cyclic shift and reversal, using λ^m ≡ 1 mod 2h).
  - On units, x′ = γx with Nm γ = 1. So the all-ν mean is Σ_{γ∈N¹(O/2h)} C(γ) + (non-unit part), with C(γ) = ⟨B, B∘γ⟩ and |C| ≤ 1.
  - The terms γ ∈ ⟨λ⟩, and the reversal, give the exact diagonal 2m·Σ_{unit x}|B(x)|²: this is B^sym. Resonances and all open-level
    cross parts are off-diagonal correlations C(γ), γ ∉ ⟨λ⟩.
  - Sums of C over congruence subgroups Γ_d = {γ ≡ 1 mod 2h/d} are |Γ_d|·‖P_{Γ_d}B‖² ≥ 0. That is the γ-side of the fiber positivity
    in M5, and it gives nothing new.
  - The conspiracy is a statement about ⟨B, B∘γ⟩ for γ in norm-one subgroups of order ~ q at open q: again equidistribution of a
    unimodular orbit product beyond log_λ q.

## 8. What a positive route would have to do [assessment]

1. It must work one m at a time (M2) and with signs (M5).
2. It must give, at the inherited modulus h_p (always present, M3), a bound on the cross part |D_iso − E_b/q| ≤ ((1−δ)·1.28359)^m,
   averaged over the conductors of h_p. In the L3 spectral form, that is a mean over isotropic β of the cubic functions Tr[R·Π_β³]
   of the p-step twisted products.
3. It must do the same for the rank-3p primes of K_p below L_m.
4. Numerics (L2) put the inherited levels at |D|^{1/m} ≈ 0.94–1.12, below the 1.28 target. So R′ is very likely false, but the
   needed input is a scarring-regime equidistribution theorem specific to the kick e^{1.8i cos}.
5. A realistic intermediate target is a **certified** computation of the inherited-level mean for one infinite family. But the
   minimal-period structure gives no recursion in p (L3 S3 and S4, and §3 here).

## 9. Files
- code/m_checks.py → logs/m_checks.log: strong divisibility, 3 ∤ h, the h_{3p} identity, family overlaps, inherited capacity rate.
- code/m_incl.py → logs/m_incl.log: inclusion-rule degeneration threshold.
- NOTES_M.md: resumption notes. claims_extract.txt: claims 206 and 232–247, verbatim.
