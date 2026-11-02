# Wave 23, task 3: Δ(m) → 0 — proof strategy

Turns the exact sequence Δ(12) ≈ 1.9×10⁻⁴, Δ(24) ≈ 5.3×10⁻¹³,
Δ(36) ≈ 6.5×10⁻²¹, Δ = 0 at m = 16, 20 (waves 20, 22) into a conditional
proof. Repository untouched; no Lean build.

## 1. Exact target

Δ(m) = Σ_F Δ_F / |supp|, |supp| = D_m/16 (exact at m = 12, 24, 36),
Δ_F = |F|² − |Σ_j |O_j| e^{iθ_j}|² ≤ |F|² (wave-19 formula: deficit
is incoherent minus coherent sum over the Γ-orbits O_j in fiber F).
So Δ(m) → 0 ⟺ Σ_F Δ_F(m) = o(D_m).

## 2. Master inequality

By the wave-20 lemma (sketch: S_q Γ-invariant, so φ̂ is constant on
any global fiber whose component fibers are all single orbits), only
global fibers containing an on-support split component fiber
contribute. Let N(m) = number of such rigid global fibers,
M(m) = max |F| over them. Then

  Σ_F Δ_F ≤ N(m) · M(m)².

## 3. Conditional theorem (proved)

Theorem. If N(m) ≤ m^a and M(m) ≤ m^b for m ≥ m₀, then Δ(m) → 0.
Proof. Δ(m) = 16·ΣΔ_F/D_m ≤ 16·m^{a+2b}/D_m. And D_m = ρ^m + ρ̄^m − 2
≥ ρ^m − 2 with ρ = 3+2√2 > 5.8 (from D_m = 2(X_m − 1) and the Pell
closed form X_m = (ρ^m + ρ̄^m)/2, i.e. the recurrence
X_{n+1} = 6X_n − X_{n−1}); a polynomial over ρ^m tends to 0. ∎

## 4. The named lemma: RB (rigidity + polynomial bounds)

RB has three parts; each reproduces the observed data exactly.

(RB1) Rigidity. Every contributing global fiber is the full product
of one split 3-component fiber, one supported 2-component fiber, and
singletons elsewhere. Observed: m = 12: 5 = 5×1; m = 24: 18 = 18×1;
m = 36: 10 = 5×2 (only the 5 built on split fiber 14 have Δ_F > 0).

(RB2) 3-part. The only on-support split component is the full 3-part
q₃ = 3^{2v₃(m)+2} when 4 | m, and none otherwise (m = 4, 8, 20 have
3-part 9 and no splits — splitting needs exponent ≥ 4). Split fibers
there: sizes 4·9^{e/2−1} ≤ 4m², orbit counts 3^{e/2−1} ≤ m.
Observed: e = 4: 1 fiber, 36 pts, 3 orbits; e = 6: 2 fibers,
324 pts / 9 orbits and 36 pts / 3 orbits.

(RB3) 2-part. #supported 2-fibers ≤ q₂ = 2^{2v₂(m)+3} ≤ 8m²
(observed 5 at q₂ = 128, 18 at q₂ = 512), each of size ≤ 2
(observed sizes 1–2; the trivial single-orbit bound 2m also suffices).

Under RB1–RB3: N(m) ≤ 8m² × 2 = 16m², M(m) ≤ 4m² × 2 = 8m²
(global size = split size × 2-fiber size, exact at m = 12, 24, 36),
so ΣΔ_F ≤ 1024·m⁶ and Δ(m) ≤ 16·1024·m⁶/(ρ^m − 2) → 0.

## 5. New lemma 3-LTE (PROVED in wave 24, see wave24_LTE3.md; was verified to m = 60, proof open)

v₃(D_m) = 0 if 4 ∤ m; = 2v₃(m)+2 if 4 | m. Verified exactly via the
Pell recurrence for m ≤ 60 (D_m cross-checked against 11 known
values); the v₂-LTE (wave 11) re-verified on the same range.
Consequence: q₃ ≤ 9m² — the split modulus grows only polynomially.
Mechanism identified, proof open: binomial expansion of (1+t)^k with
t = 576+408√2 at the base step k = m/4, where the first two terms
share v₃ and their sum gains one (k = 3: 1728+1994112 = 2⁶·3⁴·5·7·11);
the full proof needs this cancellation at all orders.

CORRECTION to the wave-22 note: at m = 48 the components are
2¹¹ = 2048 and 3⁴ = 81, not 512/6561 (computed exactly). Predicted
m = 48 test: split at q = 81 (36 pts, 3 orbits, if the pattern holds),
Δ(48) ~ 10⁻³²–10⁻³⁰ for N ∈ [5, 100] (D₄₈/16 ≈ 3.49×10³⁵).

## 6. Why naive bounds fail (explicit)

Permutation bound. Fibers are equal-sorted-multiset classes, so
|F| ≤ m!. This works at m = 12 (m!/D_m = 0.31) but m!/D_m = 11.8 at
m = 16, 1189 at m = 20, 1.0×10¹⁴ at m = 36. Any argument using only
|F| ≤ m! is vacuous for m ≥ 16.

CRT product bound. A single-orbit component fiber has ≤ 2m points,
so naively |F| ≤ (2m)^{#components}. At m = 36 (9 components) this
gives 72⁹ ≈ 5.2×10¹⁶ against the actual max fiber 648 — an overcount
of 8×10¹³ — and a naive Δ bound of ≈ 1.2×10⁸ with N = 10, vacuous.
The gap IS the rigidity content: in rigid fibers the non-split
components contribute 1 (singletons) or ≤ 2, not 2m each.

## 7. What remains for Δ → 0

- Prove RB1 (joint-nonzero rigid families excluded; now sweep +
  CRT-injectivity sketch).
- Prove RB2's orbit-count/size classification at 3^e (needs the
  3-adic analysis of split fibers + a proof of 3-LTE).
- Prove RB3's support thinness at the 2-part (2-adic analysis).
- Promote Γ-invariance of S_q from sketch to proof (underlies §2).
Then §3 gives Δ → 0, and with R = Bsym_fiber − Δ the corrected limit
reading R → Bsym_fiber holds with Δ as the (vanishing) error.
