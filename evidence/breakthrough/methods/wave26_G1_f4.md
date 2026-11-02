# Wave 26, task 1 — G1 at f=4: case analysis by (k,s), k+s=4

**Verdict.** (2,2) is CLOSED. (1,3) is closed modulo one named level-4
lemma M4, and confirmed numerically by a full check at (108,3).
(3,1) is closed modulo R30 (the f=3, s=0 gap); (4,0) is closed modulo
R40 (real case at level p⁴). No counterexample anywhere. En route, a
correction: wave-12 Lemma 5 is FALSE as stated when 2k < f, which
forces a repair of the f=3 (1,2) proof (its conclusion stands).
Repository untouched, no Lean built.

## 0. Setup (as waves 12–15)

p odd, P = p⁴, R = Z[√2], α = 3+2√2, γ = α^{L₀} = 1+pᵏu (u a unit at
p), s = v_p(m/L₀), k+s = 4, t = gcd(m,4). G1′: arbitrary recurrence
sequences y_i = Tr(Aα^i) mod p⁴ with equal sorted multisets have
D_t-related per-class multisets. Cases: (1,3), (2,2), (3,1), (4,0).

## 1. CORRECTION: Lemma 5 fails exactly in the nonlinear regime

Wave-12 Lemma 5 claims F(C) = {Tr(Cγ^j) : j ∈ Z/p^s} is always a
coset of step p^{k+v} (v = v_p(Tr(Cu))). This is false when 2k < f:
the quadratic Taylor term C(j,2)p^{2k}Tr(Cu²) survives mod p^f, and
the proof sketch's "tracing against a unit" step confuses
φ-injectivity with trace-injectivity. Counterexample at (36,3):
C = 1+3√2 has Tr(Cu) = 18 (v = 2 = s), yet
F(C) = {2 (×6), 11 (×3)} mod 27 — not a singleton.

Measured (exact): at (36,3), 162/729 violations; at (108,3),
1620/6561. Refined statement, verified exactly: in the regime
2k < f, Lemma 5 fails exactly for C whose unit part (after dividing
out v_p(C)) is collapsed (Tr(Cu) ≡ 0 mod p), and failure propagates
under scaling by p — at (108,3), violations are all 1458
unit-collapsed C plus exactly the 162 div-by-3 C whose level-3 unit
part is collapsed; unit-noncollapsed (4374) and div-by-9 (81) pass.
In the linear regime 2k ≥ f, Lemma 5 holds (checked: 0/400
violations at p=13, k=2). Consequence: only the k=1 cases need the
polynomial (non-coset) analysis below; (2,2), (3,1), (4,0) are linear.

## 2. Repaired f=3 (1,2) — needed as Step 1 for (1,3)

Wave-15's S* proof used the false "v=2 singletons" plus a size
counting argument; both are wrong (a v=2 pair contributes a
2-value quadratic multiset {0 (×6), T₂ (×3)} at p=3, not one value,
so low-group sizes are already divisible by p). Repair: the uniform
shift property survives (F(C′) = F(C) + p²·c·Tr(η₁) for collapsed C),
and the dichotomy is saved by multiplicities, not sizes: a
collapsed pair's top-digit multiset has a distinguished value
(vertex, multiplicity p) versus the rest (multiplicity 2p), so a
nonzero uniform shift cannot preserve it. With the 0-or-2 lemma
(collapsed pairs number 0 or 2), every case (v=1 partner or v=2
partner) forces Tr(η₁) = 0. Conclusion stands: f=3 (1,2) is closed,
and its digit constraints (Tr(η₀) = 0, S* = 0 when Coll ≠ ∅) are
available for the level-4 step.

## 3. Case (1,3): k=1 — closed modulo M4, confirmed at (108,3)

Step 1: per-class equality mod 27 via repaired f=3 (1,2); write
A″ = A(1+3η), η = η₀+3η₁+9η₂, with Tr(η₀) = 0, S* = 0 when Coll ≠ ∅
(and no collapsed pairs at all otherwise, in which case only full
cosets occur and level 4 is automatic). Remaining freedom: η₂.
Level-4 cosets are polynomial, not cosets (§1): for collapsed C,
Φ_C(j) = Tr(C) + 9·(j·T₁′ + C(j,2)T₂) + 27·C(j,3)T₃ mod 81, and the
η₂-twist shifts collapsed values by 9·S_C with S_C varying with
C mod 9 (not uniform within a mod-9 class). Named lemma M4: the
pooled collapsed-part multiset in each mod-9 class, given the
level-3 constraints, is not invariant under any nonzero such
shift — i.e. the level-4 shift vanishes. M4 is open in general;
its conclusion is verified at (108,3) by the full check below.

Computation (exact): full G1′ at (108,3) mod 81 — all 6561 A,
sequences of length 108, grouped by global multiset: 45 groups,
largest 2916, **0 D₄-bad pairs**. So (1,3) holds at the smallest
f=4, k=1 case; M4 is the only proof gap.

## 4. Case (2,2): k=2 — CLOSED

Linear regime, so Lemma-5 cosets hold: v=0 full coset step 169
(size 169), v=1 coset step 2197 (size 13), v=2 singleton (checked
0/400 shape violations at p=13). Proof: Step 1, mod 169 this is
f=2 s=0 (closed), so after normalisation A″ = A(1+169η),
η = η₀+13η₁ ∈ R/169. Step 2, level-3 (2,1) (closed) gives
Tr(η₀) ≡ 0 mod 13 when collapsed pairs exist at level 3. Step 3:
v=0 cosets are shift-invariant; v=1 cosets are preserved because
Tr(ηC) ≡ 0 mod 13 for collapsed C; v=2 singletons shift by
2197·S_C, S_C = c·w₀ + Tr(η₀C₁) + c·Tr(η₁) mod 13 (w₀ = Tr(η₀)/13).
Pooled partial fractions (2197² ≡ 0 mod 28561) give R_t = 0 per
trace value t; for unit A there is at most one singleton per t
((r,z) ↦ C mod 169 bijects onto A·⟨α⟩ mod 169, and t fixes C mod
13), so S_C = 0 per singleton, hence per-class equality. Divisible
A goes by induction to level-3 (2,1). Checks at p=13: v=1
invariance 274/274, v=2 shift formula 26/26, unit-A per-t
uniqueness 0 violations (the one raw violation was a divisible A,
the induction case). A full check at (2366,13) is infeasible
(28561² values of A), so (2,2) rests on this proof plus mechanism
checks, not on enumeration.

## 5. Case (3,1): k=3 — closed modulo R30

Normalisation needs R30 := G1 at f=3, s=0 (pure-G₀ rigidity at
level p³; see wave-14 §4: the real case needs digit analysis at
two levels, since (y₁−x₁)(y₁−x₂) = 0 mod p³ admits mixed
solutions). Given R30, A″ = A(1+27η), η ∈ R/3; cosets are linear
(2k = 6 ≥ 4): v=0 coset step 27 (size 3), v≥1 singleton; singletons
(C ≡ c mod p) shift by 27·c·Tr(η); pooled partial fractions
(27² ≡ 0 mod 81) give Tr(η) = 0 if any singleton with c ≠ 0 exists.
So (3,1) is exactly R30 plus one digit argument.

## 6. Case (4,0): k=4 — closed modulo R40 (non-real part proved)

γ ≡ 1 mod p⁴, G = G₀. Lucas identity
∏_{z∈G₀}(X − Tr(Cz)) = V_{L₀}(X,N(C)) − Tr(C^{L₀}) holds mod p⁴,
so the global multiset determines N(A) and Tr(A^{L₀}). Non-real
case (A^{L₀} ≢ Ā^{L₀} mod p): the quadratic X² − S X + N has
discriminant a unit mod p, hence exactly 2 roots mod p⁴ by Hensel,
so A′^{L₀} ∈ {A^{L₀}, Ā^{L₀}}; L₀-torsion lifting (derivative
L₀T^{L₀−1} a unit mod p) gives A′ = Aζ or Āζ, ζ ∈ G. Real case:
named lemma R40, the level-4 analogue of the wave-25 second-digit
transfer (iterated digit killing at 3, 9, 27). R40 is open.

## 7. Occurrence, and what remains

k=1: all primes except Wieferich-type; k=2: exactly 13, 31,
1546463 below 2×10⁹ (wave 17); k≥3: none below 2×10⁹. Hence at
f=4: (1,3) occurs widely (smallest (108,3)); (2,2) first occurs at
(2366,13) (and (14415,31)); (3,1) and (4,0) have no known instance.
Remaining for G1 at f=4: M4 (level-4 collapsed shift), R30, R40,
and Lean formalisation. The f=4 frontier is thus: one closed case,
one numerically confirmed case with a named proof gap, and two
cases that are vacuous in range and closed modulo their named gaps.

## Files

- This note: wave26_G1_f4.md
- Scripts: wave26_G1_f4_checks.py ((36,3)/(108,3) Lemma-5 shapes,
  full (108,3) G1′ check), wave26_G1_f4_p13.py (p=13 mechanism checks)
- Prior: wave12_G1_lift.md §5 (Lemma 5, corrected here),
  wave13_G1_realCz_f2.md, wave14_G1_f3.md, wave15_G1_Sstar.md,
  wave25_G1_f2s0_close.md
