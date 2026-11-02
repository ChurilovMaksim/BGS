# Wave 27, task 3 — Lemma R40: the real case at level p⁴: PROVED

**Verdict: R40 is proved (units, |H| ≥ 3).** No counterexample.
This closes the unit case of G1 at f=4, case (4,0) (wave-26 §6);
the divisible case goes by the standard induction to level p³
(R30's territory). Repository untouched, no Lean built.

## 1. Precise statement

Let p be odd, R = Z[√2], H ⊆ R/p⁴ a cyclic norm-1 subgroup of
order n ≥ 3 with gcd(n, p) = 1 (Teichmüller: reduction H → H mod p
is an isomorphism). Let C, C′ be units mod p⁴ with the same
H-orbit multiset {Tr(Cζ) : ζ ∈ H} mod p⁴. Assume the **real case
mod p**: C̄ ≡ C·θ (mod p) for some θ ∈ H mod p, i.e. C̄/C ∈ H
mod p, equivalently Cⁿ ≡ C̄ⁿ (mod p) (norm-1 group mod p is cyclic,
so its unique order-n subgroup is H mod p).

**R40.** Then C′ ≡ C·ζ or C̄·ζ (mod p⁴) for some ζ ∈ H.

Remarks. The full-orbit form (H = G₀, n = L₀) is exactly what
wave-26 §6 needs for (4,0); the proof below is uniform in H.
|H| ≥ 3 is automatic in the (4,0) setting: |H| ≤ 2 forces
(L₀, t) ∈ {(4,4),(4,2),(8,4)} (wave-25 §4), but ord(α) = 4 forces
p = 3 and ord(α) = 8 forces p = 17, both with k = 1, never k = 4.

## 2. Proof

Write θ̃ ∈ H for the unique lift of θ. For ζ ∈ H, the
**partner** ζ′ = θ̃/ζ ∈ H satisfies Cζ′ ≡ C̄ζ̄ (mod p), since
Cθ̃ ≡ C̄ (mod p) by definition of θ̃, so Cζ′ = Cθ̃/ζ ≡ C̄/ζ = C̄ζ̄
(mod p). Traces mod p: Tr(Cζ) ≡ C(ζ + θ/ζ) (mod p), so the mod-p
fibre of ζ is {ζ, ζ′}: indeed ζ₁ + θ/ζ₁ = ζ₂ + θ/ζ₂ gives
(ζ₁−ζ₂)(1 − θ/(ζ₁ζ₂)) = 0, and for norm-1 elements both factors
are units-or-zero in both split and inert cases, so ζ₂ = ζ₁ or
ζ₁ζ₂ = θ. Fixed points (ζ′ = ζ, i.e. ζ² = θ̃) number ≤ 2, so
non-fixed ζ exist. Moreover Im(Cζ) ≡ 0 (mod p) ⟺ Cζ real mod p
⟺ ζ² ≡ θ̃, i.e. exactly at fixed points; non-fixed ζ have
y(ζ) := Im(Cζ) mod p ≠ 0.

**Step 1 (mod p²).** Wave-25 closed L6 at f = 2, s = 0, so
C′ ≡ C·ζ₁ or C̄·ζ₁ (mod p²). Replacing C by a H-translate or its
conjugate (preserving hypothesis and conclusion), assume
C′ ≡ C (mod p²): C′ = C(1 + p²η), η ∈ R/p².

**Step 2 (power sums).** Σ_ζ Tr(C′ζ)² = Σ_ζ Tr(Cζ)² gives
2p²·Σ_ζ Tr(Cζ)Tr(ηCζ) ≡ 0 (mod p⁴). Now
Tr(w)Tr(ηw) = ηw² + η̄w̄² + Tr(η)N(w), and Σζ² = Σζ̄² = 0
(β² ≠ 1 for a generator β, since n ≥ 3), so
Σ_ζ Tr(Cζ)Tr(ηCζ) = n·Tr(η)·N(C). Hence Tr(η) ≡ 0 (mod p²),
so η = b√2 with b ∈ Z/p²: C′ = C(1 + p²b√2).

**Step 3 (fibres and pairs).** Tr(Cζ′) − Tr(Cζ) = p·Δ(ζ) with
Δ(ζ) = E₁/ζ − (E₁/θ̃)ζ (mod p), E₁ := (Cθ̃ − C̄)/p ∈ R/p³.
Δ(ζ) ≡ 0 ⟺ E₁ ≡ 0 (mod p) or ζ fixed. Group the multiset
equality mod p⁴ by Tr mod p² (the twist is trivial mod p²).

- *Subcase E₁ ≢ 0 (mod p).* The mod-p² fibre of a non-fixed ζ
  is the singleton {ζ}. Its twisted value τ + p²·4b·Y (Y :=
  Im(Cζ) mod p², a unit since y(ζ) ≠ 0) must equal τ mod p⁴,
  so b ≡ 0 (mod p²) and C′ = C. Done.
- *Subcase E₁ ≡ 0 (mod p) (deep real: C̄ ≡ Cθ̃ mod p²).*
  Write E₁ = pE₂, E₂ ∈ R/p². Partners lie in the mod-p² fibre,
  with Tr(Cζ′) = Tr(Cζ) + p²D, D := E₂/ζ − (E₂/θ̃)ζ ∈ Z/p²,
  and Im(Cζ′) ≡ −Im(Cζ) (mod p²) since Cζ′ ≡ C̄ζ̄ (mod p²).
  The twisted pair {τ + p²·4bY, τ′ − p²·4bY} must equal
  {τ, τ′} mod p⁴, so per pair 4bY ≡ 0 or 4bY ≡ D (mod p²).
  If some pair gives 4bY ≡ 0, then b ≡ 0 (mod p²) as above.
  Else every pair swaps, and the key identity
  D·√2·Cθ̃ = −4Y·E₂ (mod p²) — from
  −4Y·E₂ = −√2E₂(Cζ − C̄/ζ) and C̄/ζ ≡ Cθ̃/ζ (mod p²) —
  gives, Y being a unit, b√2·Cθ̃ ≡ −E₂ (mod p²). Hence
  C′ = C + p²b√2·C = C − p²E₂/θ̃ = C̄·θ̃⁻¹ ∈ C̄·H. ∎

The mechanism is sharp: a swap-surviving twist is *exactly* the
conjugate branch, never a new symmetry. The divisible case
(p | C) reduces by induction to level p³ and is not claimed here.

## 3. Numerical confirmation (exact integers, p = 5, mod 625)

H₃ (order 3) and H₆ (order 6) Teichmüller subgroups built by
Newton-lifting x³−1, x⁶−1 from mod 5 (derivatives units mod 5).
Random scan: 9503 real-case units A, twists (1+25b√2) and
(1+125b′√2), b, b′ ∈ {1,2,3,4}: **0** multiset-preserving
non-D-related twists. Deep-subcase test (C̄ ≡ Cθ̃ mod 25):
60 H₃ + 60 H₆ cases; the pair-implied twist b̂ = D/(4Y) mod 25
preserved the multiset in all 120 cases and equalled the
conjugate branch C̄θ̃⁻¹ in all 120 (5 spot-checked exactly).
An earlier run reporting 582 "counterexamples" used a wrong H
of order 15 (α⁵ mod 625 has order 30, not 6) and is discarded;
the corrected run supersedes it.

## 4. What remains

- G1 at f = 4: only M4 (level-4 collapsed shift, (1,3)) and R30
  (f = 3, s = 0, (3,1)) remain, plus Lean formalisation.
  (2,2) is closed (wave-26), (4,0) is closed for units by R40.
- R40 itself: Lean formalisation untouched.

## Files

- This note: wave27_R40.md
- Scripts: wave27_R40_test.py (corrected scan), wave27_R40_deep.py
  (deep-subcase test)
- Prior: wave26_G1_f4.md §6 (R40 named), wave25_G1_f2s0_close.md
  (Step 1 input), wave13_G1_realCz_f2.md (f = 2 template)
