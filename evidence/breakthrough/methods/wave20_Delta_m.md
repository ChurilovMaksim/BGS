# Wave 20, task 3: cancellation deficit Δ(m) beyond m = 12

## Question

Wave 19 gave the corrected D1 formula R = Bsym_fiber − Δ, with Δ = 0 at
m = 8 and Δ = 4/21175 ≈ 1.88902×10⁻⁴ at m = 12. The hard item for the
limit reading (B2′) is control of Δ as m → ∞. Here Δ is estimated at
m = 16, 20, 24 by CRT component lifts (no full enumeration: |supp| ≥
1.1×10¹¹ at these m). Repository untouched; no Lean build.

## Lemma (sketch): only split component fibers contribute

S_q[j] = Σ_i exp(2πi·c_i·T_corr[i,j]/q) is Γ-invariant: reindexing the
kernel sum by γ ∈ D_m works because X = adj(H_m) commutes with dihedral
permutations (H_m is circulant) and Q, P are γ-equivariant. Hence S_q
is constant on every single-orbit component fiber. A global fiber F
whose component fibers are all single orbits therefore has φ̂ constant
on F, so its deficit is exactly 0. Support factorises over CRT exactly
(a congruence mod D splits mod q_j), so an on-support fiber's component
fibers are all supported. Consequence: Δ(m) gets contributions ONLY
from on-support global fibers containing an on-support split component
fiber. (This also explains retroactively why all 757 gluing fibers at
m = 12 had Δ_F = 0 exactly.)

## Results

| m | D | \|supp\| = D/16 | on-support split components | contributing global fibers | ΣΔ_F | Δ(m) |
|---|---|---|---|---|---|---|
| 8 | — | — | none | 0 | 0 | 0 |
| 12 | 1536796800 | 96049800 | q=81 (36 pts, 3 orbits) | 5 | 18144 | 1.88902×10⁻⁴ |
| 16 | 1773462177792 | 110841386112 | none (q=2048 splits all off-support) | 0 | 0 | 0 exactly |
| 20 | 2046573816377472 | 127910863523592 | none (no splits at all) | 0 | 0 | 0 exactly |
| 24 | 2361744410637427200 | 147609025664839200 | q=81 (36 pts, 3 orbits) | 18 | 77760 | 5.26797×10⁻¹³ |

Component analysis (exact, all prime powers ≤ 2×10⁶ enumerated):
m = 16: q=2048 has 10 split fibers, all with 0 supported points; all
other components split-free. m = 20: zero split fibers anywhere.
m = 24: q=81 has exactly 1 split fiber (36 points, 3 orbits, fully
supported); q=512 has 5 split fibers, all off-support; all other
components split-free. Support is constant on every component fiber
(0 partial fibers) at all three m.

## m = 24 in detail

The m = 12 pattern repeats exactly. Rigid global fibers: one per
supported 512-fiber (18 fibers: 4 of size 1, 14 of size 2; 32 supported
512-points), other components zero, 81-component = the split fiber.
Each rigid fiber has size 36×|512-fiber| (36 ×4, 72 ×14), 3 Γ-orbits,
and fully cancels: S_81 orbit phases are 120° apart (0.698132,
2.792527, −1.396263 rad; |S_81| = 9 = √81 on all orbits), coherent sums
~10⁻²⁷ ≈ 0, so deficit_F = |F|² (1296 / 5184). Total ΣΔ_F = 77760.

Completeness checks for m = 24:
- Rigidity sweep: for every small-odd-component point (484 points at
  q = 25, 49, 121, 289) × every supported 512-fiber (18), the
  (512-fiber × S_81 × {t} × zeros) combos do NOT share one multiset
  (0 extra rigid families). Same for 60 sampled q = 1329409 points.
  (Single-component sweeps suffice: a joint rigid σ must preserve
  each fixed component individually, by CRT injectivity.)
- Generic sampling: 20 random points with 81-component in the split
  fiber, other components random supported — exact (v₀,v₁) fiber
  enumeration gives every time a single Γ-orbit of size 48, spanning
  exactly 1 S_81-orbit, deficit 0. Generic fibers are unsplit, as at
  m = 12.
- Cross-checks: (v₀,v₁) enumeration of a rigid fiber reproduces size
  36; full φ̂ via CRT including S_1329409[zero] (|S| = 1153 = √q)
  gives |φ̂|² = 16/D to relative error 1.6×10⁻¹³ on a rigid point.
  Correction modes (u⁻² vs raw) decided per component by the wave-16
  test (300/300 pairs decisive at every component, all corrected at
  m = 24). Global arithmetic used Python ints; mod-q work used
  X = adj(H₂₄) reduced mod q (entries ~10¹⁸ would overflow int64).

## What this suggests for the limit

Δ does not grow — it collapses: 1.9×10⁻⁴ at m = 12 → 5.3×10⁻¹³ at
m = 24 (factor ~3.6×10⁸ down), and exactly 0 at m = 16, 20. Mechanism:
the numerator ΣΔ_F is ~(#supported 2-component fibers) × |S|², i.e.
O(10⁴), while the denominator |supp| = D/16 grows exponentially in m
(D_m ~ (3+2√2)^m). If this persists, Δ → 0 and R → Bsym_fiber in the
limit, so the corrected D1 limit reading survives with negligible
cancellation loss. This is a suggestion, NOT a proof: it needs
(i) on-support splits to stay confined to components whose rigid-fiber
count grows subexponentially, and (ii) no new on-support split
component at larger m (e.g. m divisible by 36, or a 2-component split
landing on support). Both are open; the next test is m = 36.

## Caveats (unproved steps, flagged)

- Γ-invariance of S_q is a sketch (reindexing + circulant argument),
  not a Lean proof; it is what makes Δ(16) = Δ(20) = 0 exact rather
  than sampled.
- m = 24 completeness: the q = 1329409 rigidity sweep is sampled
  (60/1329409 points), not exhaustive; a rigid-compatible large-q
  point would add rigid families (each contributing at most |F|² ≤
  5184-ish per family, so even dozens would keep Δ(24) ≲ 10⁻¹¹).
- The limit Δ → 0 is conjectural (see above).

## Files

- `wave20_m24_deficit.py`, `wave20_m24_deficit.log` (full output),
  `wave20_m24_deficit.json` (18 rigid fibers with orbits/phases),
  `wave20_comp_analysis.py`, `wave20_comp_analysis.json`.
