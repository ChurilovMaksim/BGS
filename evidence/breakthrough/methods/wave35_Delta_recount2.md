# Wave 35, task 1 — Δ → 0 recount v2: joint splits as mechanism C

## Verdict

The wave-33 conditional theorem loses its premise RB1′′ (wave 34:
24 contributing joint fibers F₈₁ × F₆₂₅ at m = 60), but Δ → 0
survives a second recount. The repair adds mechanism C (joint
splits) with one joint-census hypothesis (SCJ) and replaces the
wave-33 split census by its proved/lemmatized form (SCL + SIZE).
No family is exhibited where joint splits break vanishing: the
only censused joint contribution (m = 60) is ≤ 8.64×10⁶ against
D₆₀ ≈ 8.57×10³⁹. Repository untouched; no Lean built.

## 1. What wave 34 changed

- RB1′′ is FALSE: at m = 60, joint fibers built from two
  on-support split components (81: 36 points, 3 orbits; 625:
  150 points, 5 orbits) contribute with a split companion that
  is neither a singleton nor a twin fiber (3 | ord₆₂₅(β), so
  625 is not twin-eligible). The CRT-injectivity / pinning
  sketch fails as a mechanism: the joint multiset locks the
  81-orbit but lets the 625-orbit run free — the opposite of
  joint exclusion. Per 625 fiber: 5400 pairs → 12 joint fibers,
  all multi-orbit, all contributing; each has exactly 5
  diagonal orbits (one fixed 81-orbit × all 5 625-orbits),
  phases a constant plus 5th roots, so Δ_F = |F|² exactly
  (90000 for size-300 fibers, 360000 for size-600 fibers).
- SC with c = 4 is FALSE (m = 21, q = 2401: Σ = 432180 >
  21⁴); SC with c = 5 holds on all data (tightest slack 9.4×
  at m = 21; ~1700× at m = 108, ~2700× at m = 150).
- The single-fiber danger case is DEAD unconditionally: every
  component fiber has size ≤ m² (wave 34, pair argument: a
  kernel point is fixed by (y₀, y₁), both in its own multiset
  of ≤ m distinct values). So s_q = o(D_m^δ) for any δ.

## 2. Framework and mechanisms

Δ(m) = Σ_F Δ_F/|supp|, Δ_F ≤ |F|², Δ(m) ≤ 16·ΣΔ_F/D_m
(wave-19 formula; D_m ≥ ρ^m − 2, ρ = 3+2√2). By H0 every
contributing fiber has ≥ 1 on-support split component; let
S(F) be its set of split components. The trichotomy is
exhaustive (overlap is harmless for an upper bound):

- (A) Direct split: |S| = 1, no twin identification.
- (B) Twin identification: |S| = 1, a split q₃-fiber whose
  orbits are identified by a twin companion (wave-25
  β-order mechanism, 3 ∤ ord_qt(β)). A split twin
  companion would put the fiber in C instead.
- (C) Joint splits: |S| ≥ 2. The m = 60 fibers are the
  prototype: diagonal orbits = {locked orbit at q ∈ S\T}
  × {all orbits at q ∈ T} for a nonempty free set T ⊆ S.

## 3. Hypotheses (exact content)

- (H0) Only-split-contributes, modulo Lemma F (wave 34:
  dihedral symmetry of the adjugate makes S_q constant on
  orbits; φ̂ = (1/D)·Π_q S_q constant on fibers whose
  components are all single orbits, so Δ_F = 0 there).
  Lemma F's exponent identity is validated exactly (m = 8:
  all 1331712 points; m = 12/24: 300/300 correction tests)
  but not yet proved in writing.
- (SC-sup) Support constant on component fibers (0 partial
  fibers in every census).
- (SCL) Split-Count Lemma (open): n_q ≤ 10 for every
  component q (max observed: 10 at m = 64, 5 for odd p).
- (SIZE) s_q ≤ m² for every component fiber (proved,
  wave 34 §1). With ω(D_m) < 2.54m, SCL + SIZE give
  (SC5): Σ_q n_q s_q² ≤ 10 · 2.54m · m⁴ < 26m⁵.
- (SCJ) Joint census (open, the new hypothesis): the total
  joint contribution satisfies Σ_{F: |S(F)| ≥ 2} Δ_F ≤ m^{c_J}
  for a fixed constant c_J. This packages exactly the two
  things the pinning sketch used to smuggle in: the number
  of joint fibers per split tuple, and their total across
  all slices (singleton choices elsewhere). Evidence:
  m = 60 gives ≤ 24 · 360000 = 8.64×10⁶ < 60⁵ ≈ 7.78×10⁸
  (slack ~90× at c_J = 5). Falsification: any family with
  superpolynomial total joint contribution.
- (F2-poly) max|f_qt| ≤ m^b over twin qt with exponent
  f ≥ 2 (open). For f = 2 the proved bound |f_qt| ≤ 2m·p²
  (wave 34) already suffices; only f ≥ 3 needs F2-poly.
- (H12-poly) Σ_{twin qt} qt/D_m ≤ 18u³/α^{8u} at m = 12u
  (proved, wave 31; α = 3+2√2). Lemma 9-split (wave 29:
  no split q₃-fiber at exponent e ≤ 2) is used as before.
- (RB3′) #supported 2-fibers Q₂ ≤ 8m² and max 2-fiber
  size S₂ ≤ 8m² (proved, wave 32; the "≤ 2" size clause
  was refuted and is not used).

## 4. Conditional theorem v2

**Theorem.** Assume H0 (mod Lemma F), SC-sup, SCL, SIZE,
SCJ, F2-poly (f ≥ 3 only), H12-poly. Then Δ(m) → 0.

*Proof.* Mechanism A (wave-33 skeleton, updated constants).
Split fibers have size ≥ 2, so Σ_q n_q ≤ (Σ n_q s_q²)/4
≤ 26m⁵/4 = 6.5m⁵. Hence N_A ≤ 6.5m⁵ · Q₂ = 52m⁷
contributing fibers, M_A ≤ m² · S₂ = 8m⁴ max size, and
ΣΔ_F(A) ≤ N_A · M_A² = 3328·m¹⁵ = poly(m).

Mechanism B. Vacuous unless 12 | m (9-split). There,
N_B ≤ n₃ · Q₂ · (Σ twin qt) ≤ 10 · 8m² · Σ twin qt
(fibers partition qt points, so #fibers ≤ qt), and
M_B ≤ s₃ · S₂ · m^b ≤ 8m^{4+b}. So
ΣΔ_F(B) ≤ 5120·m^{10+2b} · Σ twin qt. By H12-poly,
Σ twin qt ≤ D_m · 18u³/α^{8u} (for m ≥ 1200(b+1)²;
smaller m are finitely many), which beats every
polynomial prefactor: ΣΔ_F(B)/D_m → 0.

Mechanism C. By SCJ directly, ΣΔ_F(C) ≤ m^{c_J}.

Every contributing fiber is in A ∪ B ∪ C by H0 and the
§2 trichotomy, so ΣΔ_F ≤ 3328m¹⁵ + o(D_m) + m^{c_J}
= o(D_m) (D_m grows exponentially), and
Δ(m) ≤ 16·ΣΔ_F/D_m → 0. ∎

## 5. What is NOT claimed

- H0 stands modulo Lemma F (exponent identity unproved in
  writing); SCL and SCJ are open census hypotheses; F2-poly
  is open for f ≥ 3. The theorem is conditional on exactly
  these, plus the proved SIZE, RB3′, H12-poly.
- The structural route toward SCJ: the locked/free
  decomposition (§2) plus SCL + SIZE bounds each joint
  fiber by m^{2|S|}; what remains is a bound on the
  number of joint fibers per split tuple and on |S|
  itself (observed max |S| = 2, at m = 60; a contributing
  fiber with |S| ≥ 3 would force SCJ's structural route
  to generalize, though not falsify its total form).
- The wave-33 theorem is superseded: its premise RB1′′ is
  false and its constant c = 4 is false; v2 replaces them
  with SCL + SIZE (giving c = 5) and SCJ. The wave-25 twin
  mechanism itself is untouched by the RB1′′ refutation.
- No Lean formalisation is claimed; the counting above is
  analytic, not a Lean proof.
