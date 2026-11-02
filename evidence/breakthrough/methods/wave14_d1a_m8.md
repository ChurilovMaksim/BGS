# Wave 14, task 3 — D1a at m=8: HOLDS numerically, in the strongest form

**Verdict: D1a holds at m=8, and φ̂_s is constant on every fiber.**
No phase conspiracy is needed, because the dangerous case does not
occur: no split fiber meets the support, and φ̂_s vanishes identically
on all split fibers. This is a numerical result (exact-integer
enumeration + complex sums), not a Lean theorem; main untouched.

## What was computed

φ̂_s from main (`LineDOrbitPairFull`, HEAD d87dce0, via connector):
φ̂_s([w]) = (1/D)·Σ_{η∈Vquot} e((2s·Qnum(y) − pairNum(y,w))/D),
pairNum(y,w) = (Xy)·w, Qnum(y) = pairNum(y,y), X = adj(H_8),
and fixEquivQuot sends ξ ∈ Fix_8 to [w_ξ], w_ξ = (Hξ)/D.
With η-representatives w_{ξ′}, ξ′ ∈ Fix_8, the sum factorises over
CRT components q ∈ {9, 289, 512} (kernels of sizes 9, 289, 512):
e(t/D) = ∏ e(c_i·t_i/q_i), c_i = (D/q_i)⁻¹ mod q_i.
One subtlety found and fixed by direct test: component kernel
w-vectors satisfy [w_i] = (D/q_i)·[w] in Vquot, so component Q/P are
scaled by u², u = (D/q_i) mod q_i; for q=512 (u=41) the u⁻²
correction is mandatory (242/500 raw mismatches, 0/500 corrected),
for q=9,289 it acts trivially on the values occurring.

## Validation of the φ̂ computation (all 1,331,712 points, s=1 and s=5)

- Exponent factorisation: max phase error 1.8×10⁻¹⁵ over 3000 random pairs.
- Modulus dichotomy (Lean `phihatFix_modulus_values`): |φ̂|² = 16/D on
  support (max error 1.7×10⁻¹⁹) and 0 off support (max error 9×10⁻³⁶).
- Support from |φ̂|² agrees exactly with the torsion criterion;
  support size 83,232 = D/16, for both s=1 and s=5 (both odd, coprime
  to D; s=3 was deliberately not used — 3 | D, so the
  support-independence theorem does not apply to it).

## The D1a numbers (s=1; s=5 identical within 10⁻¹⁴)

- Fibers: 85,106; Γ-orbits: 85,145; split fibers: 39 (78 orbits).
- Support composition: 5,684 fibers fully in support, 79,422 empty,
  0 partial. **Split fibers meeting support: 0.**
- φ̂_s constancy: max |φ̂ − fiber mean| = 1.3×10⁻¹⁷ within fibers,
  same within Γ-orbits. So φ̂_s is constant on every fiber: on a
  support fiber (a single Γ-orbit) by Γ-invariance, on a split fiber
  because it is identically 0 there.
- Per-orbit coherent sums inside split fibers: all 78 orbits have
  |Σ_{ξ∈O} φ̂_s(ξ)| ≤ 2.3×10⁻¹⁷ (zero); per-fiber coherent
  |Σ_F φ̂|² ≤ 2.0×10⁻³³, incoherent Σ_F |φ̂|² ≤ 6.2×10⁻³⁵ (zero).
  Example split fiber: size 32 = two orbits of 16, all φ̂ = 0.
- Aggregate D1a identity: Σ_F |Σ_{ξ∈F} φ̂_s(ξ)|² / Σ_ξ |φ̂_s(ξ)|²
  = 15.298683199, vs Bsym = 318335/20808 = 15.298683199
  (difference 4×10⁻¹⁴, for s=1 and s=5).

## What this does NOT establish (honest limit)

m=8 cannot test the phase-coherence question D1a poses in general:
a split fiber meeting the support, with different Γ-orbit phases
that would have to conspire (or fail to), does not exist at m=8.
The first real test needs an m where a split fiber meets supp;
the m=12 glued fiber is also off-support (wave 10), so that test
is still open and is the natural follow-up. D1b at m=8 is already
supplied by the 0 split fibers meeting support; D1c is untouched.

## Files

- Script: [wave14_d1a_m8.py](sandbox://workspace/bgs-breakthrough/methods/wave14_d1a_m8.py)
- Numbers: [wave14_d1a_m8_result.json](sandbox://workspace/bgs-breakthrough/methods/wave14_d1a_m8_result.json)
