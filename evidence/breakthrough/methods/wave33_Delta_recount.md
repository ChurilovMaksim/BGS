# Wave 33, task 2 — Δ → 0 recount without 3-exclusivity

## Verdict

The repaired conditional theorem below replaces RB1′/RB2 with one
general split-census hypothesis (SC). No family is exhibited where
the new phase splits make ΣΔ_F fail to vanish: in all censused data
the new splits are polynomially small (150 at m = 30/60, ≤ 128 at
m = 64), and SC holds with ≥ 15× slack at c = 4. What wave 32 kills
is only the exclusivity: RB1′ (split component must be q₃), RB2
(only q₃ splits on support), and the wave-29 conclusion
Δ(m) = 0 unless 12 | m. The Δ → 0 route survives, re-counted.
Repository untouched; no Lean built.

## 1. What failed, exactly

- RB1′ (wave 25): every contributing fiber = one split 3-fiber ×
  one supported 2-fiber × one twin-qt fiber × singletons. False:
  wave 32 rigid fibers at m = 30 (split 5-fiber × singletons) and
  m = 32 (split 2-fiber × singletons) contribute with no split
  3-fiber and no twin companion.
- RB2 (wave 23): only q₃ splits on support. False: q = 625 at
  m = 30, 60 and q = 8192 at m = 32, 32768 at m = 64.
- Wave-29 lemma conclusion Δ(m) = 0 unless 12 | m: false, since
  Δ(30) ≥ 3.9×10⁻¹⁸ and Δ(32) ≥ 1.8×10⁻¹⁷ (wave 32, rigid lifts).
  Its proof was conditional on RB1′, so the conditional statement
  stands but its premise falls; Lemma 9-split itself (no splits at
  q₃ exponent e ≤ 2) is untouched and still used below.

## 2. Framework kept from waves 20/23/25

Δ(m) = Σ_F Δ_F/|supp|, Δ_F ≤ |F|² (wave-19 formula), and
Δ(m) ≤ 16·ΣΔ_F/D_m (D_m ≥ ρ^m − 2, ρ = 3+2√2; |V4| ≤ 16).
Two mechanisms produce a contributing (Δ_F > 0) global fiber:

- (A) Direct split: the fiber contains an on-support split fiber
  at some prime power q* (phases may cancel fully or partially;
  the upper bound Δ_F ≤ |F|² needs no phase hypothesis).
- (B) Twin identification: the fiber contains a split q₃-fiber
  whose orbits are identified by a twin companion fiber at qt
  (wave-25 β-order mechanism, 3 ∤ ord_qt(β)).

## 3. Repaired hypotheses (exact content)

- (H0) Only-split-contributes (wave-20 lemma, still a sketch via
  S_q Γ-invariance): every contributing fiber contains an
  on-support split component fiber.
- (RB1′′) Generalized rigidity (replaces RB1′): every contributing
  fiber is a product of (i) one on-support split fiber at some
  prime power q*, (ii) one supported 2-fiber (possibly a
  singleton), (iii) one companion fiber at a single component qt
  — a singleton, except when q* = q₃, where it may be a twin
  fiber via the generalized twin identification — with singletons
  elsewhere. The joint-nonzero exclusion and the pinning of other
  components remain the CRT-injectivity sketch, as in wave 25.
  If a future census finds a non-singleton companion at
  q* ≠ q₃, RB1′′ falls and the counting reopens.
- (SC-sup) Support is constant on component fibers (0 partial
  fibers in every census, waves 20/32).
- (SC) Split census: Σ_{q ‖ D_m} n_q·s_q² ≤ m^c for a fixed c,
  where n_q = number of on-support split fibers at q and s_q =
  their maximum size. This is the whole replacement for RB1′/RB2:
  it does not say which components split, only that split fibers
  are polynomially few and small in quadratic weight.
- (F2) max|f_qt| ≤ m^b over twin qt with exponent f ≥ 2 (b = 2
  is proved for square components qt = p², wave 32 task 4).

## 4. Repaired conditional theorem

**Theorem.** Assume H0, RB1′′, SC-sup, SC, F2. Then Δ(m) → 0.

*Proof.* Proved pieces used: RB3′ (wave 32) — #supported 2-fibers
Q₂ ≤ 8m² and max 2-fiber size S₂ ≤ 8m²; H12-poly exponential
(wave 31) — Σ_{twin qt} qt/D_m ≤ 18u³/α^{8u} at m = 12u;
Lemma 9-split (wave 29) — no split q₃-fiber unless 12 | m.

Mechanism A. Split fibers have size ≥ 2 (≥ 2 orbits), so
Σ_q n_q ≤ m^c/4, and max s_q ≤ m^{c/2} (n_q ≥ 1 where splits
occur). Hence N_A ≤ (m^c/4)·Q₂ = 2m^{c+2} contributing fibers,
M_A ≤ m^{c/2}·S₂ = 8m^{c/2+2} max size, and
ΣΔ_F(A) ≤ N_A·M_A² = 128·m^{2c+6} = poly(m) = o(D_m).

Mechanism B. Vacuous unless 12 | m (9-split: no split q₃-fiber
at exponent e ≤ 2, and e ≥ 4 forces 4 | m and 3 | m). There,
N_B ≤ n₃·Q₂·(Σ_{twin} #fibers at qt) ≤ (m^c/4)(8m²)(Σ twin qt)
(fibers partition qt points, so #fibers ≤ qt), and
M_B ≤ s₃·S₂·m^b ≤ 8m^{c/2+2+b}. So
ΣΔ_F(B) ≤ 128·m^{2c+6+2b}·Σ twin qt. By H12-poly exponential,
Σ twin qt ≤ D_m·18u³/α^{8u} (for m ≥ 1200(b+1)²; smaller m are
finitely many), which beats every polynomial prefactor:
ΣΔ_F(B)/D_m ≤ 128·m^{2c+6+2b}·18u³/α^{8u} → 0.
Every contributing fiber is counted in A or B by RB1′′
(overlap is harmless for an upper bound), so
ΣΔ_F = o(D_m) and Δ(m) → 0. ∎

## 5. SC checked against all censused splits (on-support only)

Σ_q n_q s_q², exact from waves 20/32 censuses (2-part splits at
m ≤ 48 are off-support and excluded; twin fibers at m = 48 are
single orbits, 0 split, and do not enter SC):

| m | split fibers (q: sizes) | Σ n_q s_q² | m⁴ | slack |
| 12 | 81: 36 | 1296 | 20736 | 16× |
| 24 | 81: 36 | 1296 | 331776 | 256× |
| 30 | 625: 150, 150 | 45000 | 810000 | 18× |
| 32 | 8192: 32×3, 16×2 | 3584 | 1048576 | 293× |
| 36 | 729: 324, 36 | 106272 | 1679616 | 16× |
| 48 | 81: 36 | 1296 | 5308416 | 4096× |
| 60 | 81: 36; 625: 150, 150 | 46296 | 12960000 | 280× |
| 64 | 32768: 128×3, 64×2, 32×3, 16×2 | 60928 | 16777216 | 275× |

So c = 4 suffices everywhere censused. The systematic growth
seen (2-part sizes 32 → 128 from e = 13 to e = 15) matches the
RB3-size conjecture max size = 2^{2v₂(m)−5} ≤ m²/32, which
together with RB3′ would imply the 2-part SC contribution
≤ 8m²·(m²/32)² = m⁶/128 — polynomial, as SC requires. The
5-splits are stable at 150 across m = 30 and m = 60, not growing
with m. No censused split exceeds 4m² in size.

## 6. What is NOT claimed, and what would kill the repair

- H0 and RB1′′ are still sketches (S_q Γ-invariance; CRT
  injectivity + pinning). SC is a hypothesis, not a theorem: its
  danger case is a split fiber of size ~D_m^δ at some huge prime
  power, which no census hints at but no argument rules out.
- The old wave-31 corollary "Δ → 0 conditional only on RB1′,
  RB2, RB3, max|f_qt| ≤ m^b" is superseded by §4: its premises
  RB1′, RB2 are false, and the twin-sum input is now the
  exponential H12-poly, used only at 12 | m for mechanism B.
- RB3′ (count) and the f_qt bound b = 2 for squares are proved
  and load-bearing as stated; F2 (f ≥ 2 twin qt) is the only
  remaining twin-side gap, and it affects mechanism B only.
- The no-vanishing branch is not exhibited: to refute Δ → 0 one
  would need Σ n_q s_q² superpolynomial, i.e. split fibers
  growing faster than any polynomial in m — against all data.
