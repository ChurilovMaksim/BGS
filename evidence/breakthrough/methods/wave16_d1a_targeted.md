# Wave 16, task 3 — targeted search for a split fiber meeting support at m ≥ 11

## Verdict: FOUND at m = 12 — a split fiber fully in support, with exact phase cancellation

No partial fiber was found anywhere in this search, but the first real
D1a phase test now exists: at m = 12 a split fiber (36 points, 3
Γ-orbits of 12) lies fully in support, and φ̂ takes three distinct
values on it — one per orbit, 120° apart — so the fiber coherent sum
vanishes exactly while the incoherent sum is full. "φ̂ constant on
fibers" (true at m = 8 only because split fibers there are off-support)
is FALSE at m = 12. Repository untouched, no Lean build.

## Method (no full enumeration)

D_m factored into prime powers q_j; component Fix points mod q_j
enumerated via the SNF kernel (size q_j); component fibers = sorted
multisets, component orbits = dihedral canon. A component split fiber
lifts (other components fixed to supported points) to a global split
fiber, since the CRT lift map is injective on values and a global
dihedral identification would reduce mod q_j. Support factorizes over
CRT exactly — validated on 300 random m = 12 lifts: global support
equals the AND of component supports. Component support uses
Q(z) mod q_j = ((D·(z·v))//4) mod q_j for torsion z = Hv/4
(validated against the adjugate at m = 8 and m = 12). Global support
uses the s = 1 torsion criterion, as in wave 15.

## Component-split results, m = 12..20

| m | component splits | lift result |
|---|---|---|
| 12 | q = 81 only: 1 fiber, 36 pts, 3 orbits | FULL: 36/36 in support, 3 global orbits of 12 |
| 13, 14, 15, 17*, 18, 19*, 20 | none in any enumerated component | — |
| 16 | q = 2048: 10 fibers (16–128 pts, 2–4 orbits) | EMPTY: 0 supported in every one |

\* m = 17 (q = 243578449) and m = 19 (q ≈ 8.8·10¹³) have one prime-power
component too large to enumerate; splits inside those components are
unsearched (small components show no splits). At m = 15 there are no
component splits, yet wave 7 reports split fibers there — those must
be gluing splits, which this lift method does not cover (see below).

Pattern: odd prime-power components are fully component-supported
(comp_supp = q in every case), while 2-power components are only
fractionally supported (1/4 at q = 4, 1/8 at q = 32, 1/16 at q = 128
and q = 2048). Meeting support therefore needs a split in an odd
component plus a supported 2-component — rare, but it happens at m = 12.

## The m = 12 fiber in detail (φ̂ by CRT factorisation, wave 14 method)

Correction mode per component decided by direct test against global
exponents from the 12×12 adjugate (300 random pairs): raw at q = 128,
81, 49; u⁻²-corrected at q = 25, 121. Modulus validation:
|φ̂|² = 16/D on all 36 points, max error 5.6·10⁻²³ (s = 1),
1.1·10⁻²² (s = 13, also coprime to D).

| Γ-orbit (size 12) | φ̂ mean, s = 1 | \|Σ_orbit φ̂\| |
|---|---|---|
| 0 | −4.312211·10⁻⁵ − 9.247567·10⁻⁵i | 1.224427·10⁻³ = 12·\|φ̂\| |
| 1 | −5.852522·10⁻⁵ + 8.358268·10⁻⁵i | 1.224427·10⁻³ = 12·\|φ̂\| |
| 2 | +1.016473·10⁻⁴ + 8.892989·10⁻⁶i | 1.224427·10⁻³ = 12·\|φ̂\| |

The three means have arguments ≈ −115°, 125°, 5° — exactly 120°
apart, each of modulus √(16/D) = 1.0204·10⁻⁴. φ̂ is constant within
each orbit (Γ-invariance) but not across the fiber: fiber spread
max |φ̂ − mean| = 1.020·10⁻⁴. Fiber coherent sum |Σ_F φ̂| = 3.3·10⁻¹⁸
(≈ 0; |Σ_F φ̂|² = 1.1·10⁻³⁵ vs |F|²·16/D = 1.349·10⁻⁵), while the
incoherent sum Σ_F |φ̂|² = 3.748·10⁻⁷ is full. At s = 13 the same
three values occur with orbits permuted. Consequence for D1a: the
fiber-average term |Σ_F φ̂|² gets ZERO from this fiber, so no
argument that treats fiber sums as orbit-size-weighted (incoherent)
sums, or that assumes φ̂ constant on fibers, can work at m = 12 —
the within-fiber phase cancellation is real and must be accounted for.

## Gluing check at m = 12 (bounded)

The known glued fiber (q = 128 period-4 × q = 25 period-6, other
components zero) reproduces exactly: 24 vectors, 2 orbits of 12,
0/24 in support. Recombining the same (128, 25) pairings with the
other components fixed to supported points still gives one fiber,
2 orbits — but still 0/24 in support: the bottleneck is the q = 128
component itself (only 8/128 points supported), not the other
components. So gluing adds no meeting-support fiber at m = 12.

## What remains

- Partial fibers (0 < #(fiber ∩ supp) < |fiber|): none found in this
  search; all lifts are FULL or EMPTY. A partial fiber would be an
  even sharper D1a test, but the m = 12 full fiber already settles
  the phase question qualitatively (cancellation, not conspiracy).
- Gluing splits at m = 15 (and generally): unsearched; the m = 15
  split fibers of wave 7 are the natural next target.
- Large-component splits at m = 17, 19: unsearched (see above).
- D1a at m = 12 in full (aggregate Σ_F |Σ_F φ̂|² vs Bsym): needs the
  fiber sum over all fibers, not just this one — this fiber's zero
  contribution is one term, not the total.

## Files

- Search: [wave16_d1a_targeted.py](sandbox://workspace/bgs-breakthrough/methods/wave16_d1a_targeted.py), log [wave16_targeted_13_20.log](sandbox://workspace/bgs-breakthrough/methods/wave16_targeted_13_20.log)
- m = 12 φ̂: [wave16_d1a_m12_phi.py](sandbox://workspace/bgs-breakthrough/methods/wave16_d1a_m12_phi.py), numbers [wave16_m12_phi.json](sandbox://workspace/bgs-breakthrough/methods/wave16_m12_phi.json)
