# Wave 34, task 3 — RB1′′ is FALSE: joint split fibers at m = 60

## Verdict

RB1′′ (wave 33 §3) claims every contributing global fiber is one
split fiber at q\* × one supported 2-fiber × one companion fiber
(singleton, or twin when q\* = q₃) × singletons elsewhere. This is
false: at m = 60 there are 24 contributing joint fibers built from
two on-support split components, with a split companion. The
CRT-injectivity / pinning sketch behind the joint-nonzero exclusion
fails as a mechanism: joint-nonzero families do contribute, richly.
Repository untouched; no Lean built.

## Setup (exact)

- m = 60, D₆₀ = 8572001542975368419584080488440354732051920000,
  components {49, 81, 121, 128, 361, 625, 841, 1681, 3481, 72361,
  361201, 923521, 5202961}.
- Fiber = same sorted multiset; split = >1 dihedral Γ-orbit;
  support factorizes over CRT (wave 16). All other components are
  fixed to supported singletons (zero everywhere except q = 128,
  where zero is not supported and a supported singleton is used).
- A global fiber in this slice = pairs (a, b) ∈ F₈₁ × F₆₂₅ with
  the same joint multiset of pairs (aᵢ, bᵢ) (CRT is injective on
  pairs; reductions to other components force the fixed
  singletons). Diagonal Γ-orbits are computed on vᵢ = aᵢ·625 + bᵢ.
- Phases by the wave-32 S_q method (adjugate-free, correction mode
  tested: corr = True at both q, phase spreads ≤ 1.5×10⁻¹⁴).

## Data

- q = 81: one on-support split fiber, 36 points, 3 orbits of 12,
  phases 2.792527, −1.396263, 0.698132 (3rd roots, 120° apart).
- q = 625: two on-support split fibers, 150 points each, 5 orbits
  of 30, phases 5th roots (72° apart, e.g. 0.251327, −2.261947,
  2.764602, 1.507964, −1.005310 for the first).
- ord₆₂₅(β) = 375, divisible by 3: 625 is NOT twin-eligible (twin
  criterion: 3 ∤ ord). Twin fibers are single-orbit by census
  (m = 48: 27 and 10693 fibers, 0 split); a 5-orbit companion is
  not a twin fiber under any reading.

## Result: 24 contributing joint fibers

For each of the two 625 split fibers: 5400 pairs → 12 joint fibers,
ALL multi-orbit, ALL contributing. Each has exactly 5 diagonal
orbits: one fixed 81-orbit × all 5 625-orbits (verified orbit
pairs, e.g. (o₈₁, o₆₂₅) = (6,1), (6,6), (6,11), (6,9), (6,4)).
Phases are a constant plus 5th roots, so the coherent sum vanishes
and Δ_F = |F|² exactly: fibers of size 300 (orbits 60 each) have
Δ_F = 90000, fibers of size 600 (orbits 120 each) have
Δ_F = 360000. Total: 24 contributing joint fibers in this slice.

## Why no loophole saves RB1′′

- With q\* = 81: the companion at 625 is split (5 orbits), not a
  singleton and not a twin fiber (split, and 3 | ord₆₂₅(β)).
- With q\* = 625: the companion at 81 is split, and q\* ≠ q₃, so
  the twin exception does not apply either.
- The joint multiset locks the 81-orbit but lets the 625-orbit
  run free — the opposite of joint exclusion. The slice was built
  with freely chosen fixed singletons, so the "pinning of other
  components" sketch fails too.

## Consequences

- The wave-33 conditional theorem for Δ → 0 loses its premise
  RB1′′ and must be re-counted with a third mechanism (C: joint
  splits) plus a joint-census hypothesis (SC-joint: total joint
  contribution polynomial in m). Δ → 0 itself is NOT refuted:
  the joint fibers found here are polynomially small (size
  ≤ 600, Δ_F ≤ 360000 at m = 60).
- The wave-25 twin mechanism is untouched: it concerns a
  single-orbit companion identifying q₃-orbits, a different
  phenomenon from the joint splits exhibited here.

## Files

- Note: this file. Test: `wave34_RB1pp_test.py` (component census,
  S_q phases with correction test, joint grouping, diagonal
  orbits, Δ_F via the wave-19 formula).
