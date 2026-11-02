# Wave 41, task 5 — F2-poly status reconciled: v3's "open" label is a shape mismatch, not a real gap

## Verdict

The wave-35 F2-poly theorem is sound, and its §4 counting already
closes mechanism B for f ≥ 3. The wave-40 recount v3 lists
"F2-poly (f ≥ 3) open" only because v3 states F2-poly in the pure
form max|f_qt| ≤ m^b, which wave 35 does not prove — but mechanism B
does not need that form. Restated v3 hypothesis list: H0 (proved),
SC-sup (open), SCL (open), SCJ′ (open). F2-poly drops out entirely
(f = 2 already sufficed via the wave-34 bound |f_qt| ≤ 2m·p²).

## 1. What wave 35 actually proves

For every qt = p^{2f} ‖ D_m (p odd, p ≠ 3, twin or not):

    |f_qt| ≤ 5m³·p^{e/2} ≤ 5m³·qt^{1/4},   e = v_𝔭(α^d − 1).

This is NOT of the form m^b: qt can be as large as ~D_m
(exponential in m), so the qt^{1/4} factor cannot be absorbed.
The pure-m^b bound, as v3 states it, is genuinely unproved —
and no refutation of it was found either (at (182,13) the max
fiber 4732 is far below 182²). It is simply unneeded for Δ → 0.

## 2. Proof audit (§1–§3, modulo prior-wave setup)

Assumed as given from waves 32/34 (not re-derived here): SNF
(p^f, p^f) for M^m − I, rows ↔ C ∈ R_{p^f} via w_j = Tr(Cα^j),
f = v_𝔭(α^m − 1) = e + v_p(m/d), d | p ∓ 1, d ≥ 3, p ∤ d.

- §1 (level-e determination): sound. The reduced multiset is m/d
  copies of the d-cycle of C_e; dividing multiplicities recovers
  the cycle, and its power sums give p_2 = 2dN and
  p_d = d·Tr(C^d) (+ binom(d,d/2)N^{d/2} if d even), hence (N, S)
  mod p^e since 2d is a unit mod p.
- §2 (root count): conclusion sound, one intermediate claim
  overstated (repaired below). Given (N, S), X = C_1^d satisfies
  X² − SX + N^d = 0; with Z = X − S/2, Z² = Δ/4, Z̄ = −Z.
  If v(Δ/4) = 2t < e′, the note claims "≤ 2 roots" for W — this
  is wrong as stated: Hensel roots mod p^{e′−2t} lift to p^t
  values of W mod p^{e′−t}, all satisfying W² ≡ u
  (mod p^{e′−2t}), so the count is ≤ 2p^t, not ≤ 2.
  Repair: 2t < e′ gives 2p^t ≤ 2p^{⌊e′/2⌋}, so the claimed
  per-case bound ≤ 2p^{⌊e′/2⌋} valid X still holds, and the
  v(Δ/4) ≥ e′ case independently gives p^{⌊e′/2⌋}.
  Given X, C_1 is a d-th root: ≤ d options (unit coordinate
  in the cyclic group (ℤ/p^{e′})^× with gcd(d, φ) = d, the
  other coordinate forced by Norm = N; inert case via μ_d
  of order d, reduction mod 𝔭 injective). Summing over
  levels k < e gives ≤ 5d·p^{e/2} (constant 5 verified for
  p ≥ 5; p = 3 is excluded from the theorem).
- §3 (theorem): sound. Reductions of a fiber share (N, S) by §1,
  hence lie among ≤ 5d·p^{e/2} classes C_e; each lifts to
  p^{2(f−e)} classes in R_{p^f}; d ≤ m and p^{f−e} ≤ m give
  |F| ≤ 5m³·p^{e/2}, and e ≤ f gives p^{e/2} ≤ qt^{1/4}.

## 3. Mechanism B is closed for f ≥ 3 (wave 35 §4)

v3's skeleton uses M_B ≤ s₃·S₂·m^b and hence needs pure m^b.
Replace it with wave 35 §4's qt-dependent counting (wave-33 §4
with SC(c), c = 5, and RB3′): N_qt ≤ 2m^{c+2}·qt fibers
containing qt, M_qt ≤ 40m^{c/2+5}·qt^{1/4}, so
ΣΔ_F(B) ≤ 3200m^{2c+12}·Σ_qt qt^{3/2}
≤ 3200m^{2c+12}·(Σ_qt qt)^{3/2} (Hölder), and H12-poly
(Σ twin qt ≤ D_m·18u³/α^{8u}) gives
ΣΔ_F(B)/D_m ≤ 3200m^{2c+13}·(18u³)^{3/2}·α^{−6u} → 0.
Inputs: SC(c)/SCL (already carried open by v3), RB3′ (proved),
H12-poly (proved). No new hypothesis is introduced.

## 4. Independent reproduction

Recompiled and reran wave35_F2poly_182.cpp (18 s): over all
13⁶ = 4,826,809 classes C mod 13³ at m = 182, max hash group
4732, exact re-verification by sorting sequences gives max
fiber exactly 4732 = 13·364, far below the theorem's
5m³·13 ≈ 3.9×10⁸. The headline verification reproduces exactly.

## 5. Corrected v3 statement

**Theorem (v3 restated).** Assume H0, SC-sup, SCL, SCJ′.
Then Δ(m) → 0. (SIZE, RB3′, H12-poly, Lemma 9-split, and
F2-poly in the wave-35 qt^{1/4} form are proved inputs.)
The pure-m^b bound over twin qt at f ≥ 3 remains open as a
standalone statement but is not a hypothesis of Δ → 0.

Limits: the audit covers wave-35 §1–§4 given the prior-wave
setup; Lean formalisation is open; repository untouched.
