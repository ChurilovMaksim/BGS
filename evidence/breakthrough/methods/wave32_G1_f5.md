# Wave 32, task 1 — G1 at f=5: case analysis by (k,s), k+s=5

**Verdict.** (3,2) and (4,1) are CLOSED (lifted singleton argument).
(1,4) is open modulo one named lemma M5 (level-5 collapsed shift),
confirmed by a full check at (324,3) with 0 bad pairs. (2,3) is open
modulo one named lemma Q5 (level-5 quadratic shift; only tier-2/3
orbits constrain), shape-checked at (30758,13). (5,0) is open modulo
one named lemma R50 (level-5 real case). (3,2), (4,1), (5,0) have no
known instance (k≥3: none below 2×10⁹). Repository untouched, no
Lean built (proof sketches + exact checks, not Lean).

## 0. Setup (as waves 26, 31)

p odd, P = p⁵, R = ℤ[√2], α = 3+2√2, γ = α^{L₀} = 1+pᵏu (u a unit
at p), s = v_p(m/L₀), k+s = 5, t = gcd(m,4). G1′: recurrence
sequences y_i = Tr(Aα^i) mod p⁵ with equal sorted multisets have
D_t-related per-class multisets. Cases: (1,4), (2,3), (3,2), (4,1),
(5,0). The f=4 base is now fully closed: (2,2) wave 26, (1,3) via
M4 (wave 27, proved), (3,1) via R30 (waves 28–31, proved), (4,0) via
R40 (wave 27, proved) + R30 for the divisible case. Linear regime
2k ≥ 5 ⟺ k ≥ 3; (1,4) and (2,3) are nonlinear. Key lemma (I1-type,
from N(γ) = 1: 2a + pᵏ(a²−2b²) = 0 forces a ≡ 0 mod pᵏ, so
u ≡ μ√2 mod p, μ ≠ 0, at every k): Tr(Cu) ≡ 0 mod p ⟺ C is real
mod p. Used in §3–§4 to make singletons real-residue.

## 1. Case (1,4): k=1 — open modulo M5, confirmed at (324,3)

Step 1: mod p⁴ this is (1,3), closed. Level-4 output:
A′ = A^ε·α^s·(1+pη), η = pη₁+p²η₂+p³η₃, Tr(η₁) = Tr(η₂) = 0
(levels 3, 4). Top-digit shift (expansion of
p·Tr(Cηγ^j) mod p⁵):
p⁴·[Tr(Cη₃) + j·Tr(Cη₂u) + C(j,2)·Tr(Cη₁u²)] — constant within
a mod-p⁴ fiber (depends only on j mod p), so the M4 fiber
argument has a level-5 analogue with
δ(a,C) = Tr(Cη₃) + a·Tr(Cη₂u) + C(a,2)·Tr(Cη₁u²), quadratic in a.
Ingredients lifting verbatim: t₂ = 4cμ² ≠ 0 for collapsed units,
I1, ≤ 2 collapsed γ-orbits (Aα^i real mod p ⟺ L₀ | 2(i−i₀)).
New work: (i) the level-5 vertex/block decomposition with
cubic/quartic terms (analogue of M4 §2), (ii) coefficient
vanishing across fibers (δ = 0 as a quadratic in a, for varying C).
Named lemma M5: under the level-4 output, the level-5 per-class
multisets match under π; in particular δ(a,C) = 0 for every
collapsed orbit.
Computation (exact, C++): full G1′ at (324,3) mod 243 — 59049 A,
127 groups, max group 26244, 0 D₄-bad pairs. So (1,4) holds at
the smallest case; M5 is the only proof gap.

## 2. Case (2,3): k=2 — open modulo Q5, shape-checked at (30758,13)

Step 1: mod p⁴ this is (2,2), closed outright. Level-4 output:
A″ = A(1+p²η), η = η₀+pη₁+p²η₂ ∈ R/p³ (η₀, η₁ constrained as in
wave 26 §4: Tr(η₀) ≡ 0 mod p in the collapsed case, S_C = 0 per
level-4 singleton), η₂ free. Top-digit shift:
p⁴·[j·Tr(Cη₀u) + Tr(Cη₂)] = p⁴·[j·s + r].
CORRECTION (caught by the check): the top digit within a mod-p⁴
fiber is NOT constant — the j·T₁ term contributes t·T₁
(t = j/p²) — so non-collapsed and tier-1 orbits
(v_p(Tr(Cu)) ≤ 1) have FULL F_p top-digit lines per fiber,
invariant under fiber-constant shifts, hence NO constraint. Only
tier-2/3 orbits (v_p(Tr(Cu)) ≥ 2, single fiber, quadratic top
digits) constrain, via one vertex equation each:
 tier-3: r = s(s−T₂)/(2T₂);
 tier-2: r = s(s+2T₁″−T₂)/(2T₂),
where s = Tr(Cη₀u), r = Tr(Cη₂), T₂ = Tr(Cu²) mod p,
T₁″ = (Tr(Cu)/p²) mod p. (Tier-3 with T₂ ≡ 0 forces s = r = 0
directly; tier-2 with T₂ ≡ 0 is a full line, no constraint.)
Named lemma Q5: the vertex equations from all tier-2/3 orbits,
together with the level-4 constraints, force the level-5 twist to
vanish. Gap, precisely: one tier-2/3 orbit never forces vanishing
— its vertex curve passes through (0,0) but has other F_p-points
(e.g. tier-3: (s,r) = (T₂,0)) — so Q5 needs the full system
across orbits + level-4 constraints, unproved. Tier-2/3 orbits
are rare (expected ≈0.08 per 14-orbit class by uniformity
heuristic; most classes are automatic at level 5); a class with
ALL orbits tier-2/3 forces A divisible by p² (via (Tr B, Tr(Bα))
determining B mod p²), i.e. the induction case.
Computation (exact): shape check at (30758,13) mod 13⁵ — L₀ = 14,
k = 2, α^30758 = 1; 5 non-collapsed (169 fibers, full lines),
5 tier-1 (13 fibers, full lines), 5 tier-2 + 3 tier-3 (single
fiber, quadratic top distribution exact). A full G1′ check is
infeasible (371293² A values).

## 3. Case (3,2): k=3 — CLOSED (lifted singleton argument)

Step 1: mod p⁴ this is (3,1), closed (R30 proved). Linear regime:
γ-orbits are cosets (step p^{3+v}): v=0 coset step p³ (p²
values), v=1 coset step p⁴ (p values), v=2 singleton. Remaining
twist A″ = A(1+p³η), η ∈ R/p², η₀ constrained by (3,1), η₁ free;
top-digit shift p⁴·Tr(Cη₁), uniform per orbit (γ^j ≡ 1 mod p³).
Cosets are invariant (adding p⁴δ permutes a full coset layer);
singletons move by p⁴·Tr(Cη₁). Singletons have C real mod p
(§0 lemma), so the shift is p⁴·c·Tr(η₁); pooled partial
fractions ((p⁴)² ≡ 0 mod p⁵) give Tr(η₁) = 0 if any c≠0
singleton exists, else induction. Sketch at the pooled step, the
same standard as wave 26 §5; no genuine instance exists to check
against.

## 4. Case (4,1): k=4 — CLOSED (lifted singleton argument)

Step 1: mod p⁴ this is (4,0), closed (R40 for units, |H| ≥ 3
automatic as in wave 27 — the |H| ≤ 2 cases force p = 3/17,
k = 1, never k = 4 — plus R30 for the divisible case). Remaining
twist A′ = Aζ(1+p⁴η), η ∈ R/p. γ-orbits (size p):
Tr(C) + j·p⁴·Tr(Cu) — full p-lines (Tr(Cu) ≢ 0 mod p),
invariant under the uniform per-orbit shift p⁴·Tr(ηC), and
singletons (Tr(Cu) ≡ 0, hence C real mod p by §0), moving by
p⁴·c·Tr(η); pooled fractions give Tr(η) = 0 if any c≠0
singleton exists, else induction. Same sketch standard as §3;
no genuine instance.

## 5. Case (5,0): k=5 — open modulo R50

γ ≡ 1 mod p⁵, G = G₀. Lucas identity mod p⁵ + Hensel (non-real
case: discriminant a unit mod p → exactly 2 roots mod p⁵;
L₀-torsion lifting) as in wave 26 §6, one level up. Real case:
named lemma R50 — the level-5 analogue of R40: for
H ⊆ R/p⁵ cyclic norm-1, |H| ≥ 3, gcd(n,p) = 1, units C, C′ with
the same H-orbit multiset and C̄ ≡ C·θ mod p (θ ∈ H mod p),
C′ ≡ C·ζ or C̄·ζ mod p⁵ for some ζ ∈ H. Proof architecture
(lift of R40): mod-p² step (L6 at f = 2, s = 0), power sums r = 2
→ Tr(η) ≡ 0 mod p³ (C′ = C(1+p²η), η ∈ R/p³) → η = b√2, then
fiber/pair analysis at levels p³, p⁴, p⁵ (R40's E₁ subcases +
one deeper level for the deep-real subcase). Open. Divisible
case by induction to level p⁴ (R40's territory, closed).

## 6. Occurrence, and what remains

k is a property of p (v_p(α^{L₀}−1)), independent of f, so wave
26 §7 carries over: k = 1 widely (all primes except
Wieferich-type); k = 2 exactly 13, 31, 1546463 below 2×10⁹;
k ≥ 3 none below 2×10⁹. Hence: (1,4) smallest (324,3),
confirmed; (2,3) first (30758,13) and (446865,31), shape-checked
only; (3,2), (4,1), (5,0) vacuous in range, the first two closed
by argument, the last modulo R50. Remaining for G1 at f = 5:
M5, Q5, R50, and Lean formalisation.

## Files

- This note: wave32_G1_f5.md
- Scripts: wave32_G1_f5_fullcheck.cpp (full (324,3) check),
  wave32_G1_f5_shapes.py (shape check at (30758,13))
- Prior: wave26_G1_f4.md, wave27_M4.md, wave27_R40.md,
  wave31_JointLemma.md, wave30_R30_close.md
