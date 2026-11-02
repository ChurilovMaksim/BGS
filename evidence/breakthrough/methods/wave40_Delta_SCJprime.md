# Wave 40, task 3 — Δ → 0 recount v3: SCJ′ replaces polynomial SCJ

## Verdict

The wave-35 theorem v2 survives with exactly one slot replaced:
polynomial SCJ (ΣΔ_F(C) ≤ m^{c_J}) is out — wave 39 showed
realization is full at m = 180 (one section alone ≥ 2.96×10²⁶,
killing c_J ≤ 11) and conditionally refutes it along m = 9t —
and SCJ′ (ΣΔ_F(C) ≤ D_m^γ for a uniform γ < 1) is in. No
mechanism fails under SCJ′: A and B never used SCJ, and C
needs only ΣΔ_F(C) = o(D_m), which SCJ′ gives directly.
Δ → 0 is now conditional on exactly: H0 (proved), SC-sup,
SCL, SCJ′, F2-poly (f ≥ 3 only), plus proved SIZE, RB3′,
H12-poly, Lemma 9-split. Repository untouched; no Lean built.

## 1. What wave 39 changed, and what it did not

- Polynomial SCJ is dead as a theorem shape: along m = 9t,
  B(m) ~ D_{3t} = D_m^{1/3} (superpolynomial) is realized
  with Δ_F ≥ c > 0 per fiber, modulo F1–F4 (§3). No fixed
  c_J can work there. The m = 60 evidence (≤ 8.64×10⁶
  vs D₆₀ ≈ 8.57×10³⁹) is now just a small-m data point,
  not evidence for polynomiality.
- Δ → 0 is NOT threatened by this: it needs only
  ΣΔ_F = o(D_m), and D_m^{1/3} = o(D_m). The wave-35 slot
  was stronger than necessary. SCJ′ is the exact
  weakening that the m = 180 evidence supports:
  γ = 1/3 along m = 9t, and the m = 180 section total
  (2.96×10²⁶) is vastly below D_180 (138 digits).
- Falsification criterion for SCJ′ (hence for Δ → 0 via
  C): a family with ΣΔ_F(C) ≥ D_m^γ for every γ < 1,
  i.e. joint contribution comparable to D_m itself.
  Nothing observed comes close: the largest realized
  section is ~D_m^{1/3} along 9t.

## 2. Framework (unchanged from v2)

Δ(m) = Σ_F Δ_F/|supp|, Δ_F ≤ |F|²,
Δ(m) ≤ 16·ΣΔ_F/D_m (wave-19 formula;
D_m ≥ ρ^m − 2, ρ = 3+2√2). By H0 every contributing
fiber has ≥ 1 on-support split component; S(F) is its
set of split components. Trichotomy (exhaustive;
overlap harmless for an upper bound):

- (A) Direct split: |S| = 1, no twin identification.
- (B) Twin identification: |S| = 1, a split q₃-fiber
  whose orbits are identified by a twin companion
  (3 ∤ ord_qt(β)); a split twin companion would put
  the fiber in C instead.
- (C) Joint splits: |S| ≥ 2 (m = 60 prototype:
  diagonal orbits = locked orbit × all free orbits;
  m = 180 prototype: locked 625 × top-digit 729 pair
  × blind components, all realized).

## 3. Hypotheses (exact content)

- (H0) Only-split-contributes: PROVED. Lemma F's
  exponent identity was proved in wave 35 (exact lift
  relation + u_q² scaling + CRT character identity;
  16,000 exact samples at m = 8, 12, 0 failures), so
  φ̂ = (1/D)·Π_q S_q and S_q is constant on orbits;
  fibers with all components single orbits have
  Δ_F = 0. The v2 "modulo Lemma F" caveat is closed.
- (SC-sup) Support constant on component fibers
  (open; 0 partial fibers in every census).
- (SCL) Split-Count Lemma (open): n_q ≤ 10 for every
  component q (max observed: 10 at m = 64, 5 odd p).
- (SIZE) s_q ≤ m² for every component fiber
  (proved, wave 34 pair argument).
  SCL + SIZE give (SC5): Σ_q n_q s_q² < 26m⁵.
- (SCJ′) Joint census, restated (open): there is a
  uniform γ < 1 with Σ_{F: |S(F)| ≥ 2} Δ_F ≤ D_m^γ
  for all m. Uniformity matters: a γ(m) → 1 would
  not suffice. Evidence: γ = 1/3 along m = 9t
  (modulo F1–F4); m = 60 and m = 180 sections are
  consistent (tiny against D_m).
- (F1–F4) The 9t-family justification of γ = 1/3:
  (F1) 729 splits with a top-digit colliding pair
  (verified only at m = 36, 180); (F2) enough
  components of D_{3t} are non-split and all-blind
  for the 729-move (top-digit-law conditions
  v₃(d_a) ≤ 1, v₃(period o) ≤ 1); (F3) the phase
  gap stays bounded away from 0 (2π/3 at m = 180);
  (F4) distinctness generalizes (distinct (a, b)
  pairs, proved at m = 180). F1–F4 are open beyond
  m = 180; without them, γ = 1/3 along 9t is
  conjectural, but SCJ′ as a bare statement stands
  or falls on its own.
- (F2-poly) max|f_qt| ≤ m^b over twin qt with
  exponent f ≥ 3 (open). For f = 2 the proved bound
  |f_qt| ≤ 2m·p² (wave 34) already suffices.
- (H12-poly) Σ_{twin qt} qt/D_m ≤ 18u³/α^{8u} at
  m = 12u (proved, wave 31).
- (RB3′) #supported 2-fibers Q₂ ≤ 8m² and max
  2-fiber size S₂ ≤ 8m² (proved, wave 32).
- (Lemma 9-split) No split q₃-fiber at exponent
  e ≤ 2 (proved, wave 29).

## 4. Conditional theorem v3

**Theorem.** Assume H0, SC-sup, SCL, SCJ′, F2-poly
(f ≥ 3 only). Then Δ(m) → 0. (SIZE, RB3′,
H12-poly, Lemma 9-split are proved inputs.)

*Proof.* Mechanism A (v2 skeleton, unchanged).
Split fibers have size ≥ 2, so Σ_q n_q ≤
(Σ n_q s_q²)/4 ≤ 26m⁵/4 = 6.5m⁵. Hence
N_A ≤ 6.5m⁵ · Q₂ = 52m⁷ contributing fibers,
M_A ≤ m² · S₂ = 8m⁴ max size, and
ΣΔ_F(A) ≤ N_A · M_A² = 3328·m¹⁵ = poly(m).

Mechanism B (unchanged). Vacuous unless 12 | m
(9-split). There, N_B ≤ n₃ · Q₂ · (Σ twin qt)
≤ 10 · 8m² · Σ twin qt (fibers partition qt
points, so #fibers ≤ qt), and
M_B ≤ s₃ · S₂ · m^b ≤ 8m^{4+b}. So
ΣΔ_F(B) ≤ 5120·m^{10+2b} · Σ twin qt. By
H12-poly, Σ twin qt ≤ D_m · 18u³/α^{8u} (for
m ≥ 1200(b+1)²; smaller m are finitely many),
which beats every polynomial prefactor:
ΣΔ_F(B)/D_m → 0.

Mechanism C (the replaced slot). By SCJ′
directly, ΣΔ_F(C) ≤ D_m^γ with γ < 1 uniform,
so ΣΔ_F(C)/D_m ≤ D_m^{γ−1} → 0. No counting
of joint fibers per split tuple, no B(m), no
locked/free product bound is needed — SCJ′
packages exactly the total, and the total is
all Δ → 0 ever needed from C.

Every contributing fiber is in A ∪ B ∪ C by H0
and the §2 trichotomy, so
ΣΔ_F ≤ 3328m¹⁵ + o(D_m) + D_m^γ = o(D_m)
(D_m grows exponentially, γ < 1), and
Δ(m) ≤ 16·ΣΔ_F/D_m → 0. ∎

## 5. What is NOT claimed

- SCJ′ is open, as SCJ was; the improvement is
  that SCJ′ is consistent with all data (including
  the m = 180 killing section), while polynomial
  SCJ is conditionally refuted along 9t. The
  9t value γ = 1/3 is itself conditional on F1–F4.
- SCL and F2-poly (f ≥ 3) remain open exactly as
  in v2; SC-sup remains open. H0's Lemma F gap is
  the one hypothesis v2 carried that v3 drops.
- No Lean formalisation is claimed; the counting
  above is analytic, not a Lean proof.
