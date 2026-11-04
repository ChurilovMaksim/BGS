# Wave 18, task 2 — P_w census on support at m=12: P_w FAILS on support

## Verdict

**P_w does not hold on support at m=12.** Of the 762 split fibers meeting
support, 152 contain two Γ-orbits with the same sorted(w), so their
(fiber,w)-class strictly contains more than one Γ-orbit. This closes the
gluing-split census gap left open by wave 17 — and the answer is negative.
Repository untouched; no Lean build; all comparisons are exact integers
(no floating point in the verdict).

## Method (exact census, no full enumeration of Fix_12)

- Global point = CRT tuple of component points (q = 128, 81, 25, 49, 121).
  Γ = dihedral action on positions (24 perms).
- Every Γ-orbit has a representative with 121-component equal to a fixed
  base point of its 121-fiber (121-fibers are single orbits), so
  enumerating, per super-combo of component fibers (128-fibers supported
  only; odd components fully supported), all tuples (b_128, b_81, b_25,
  b_49) with 121-component fixed covers one representative of EVERY
  orbit of EVERY fiber meeting support. Total: 8,731,800 representatives
  (exactly the predicted 8·81·25·49·11).
- Fiber = sorted global values; orbit = dihedral canon (lex-min over the
  24 perms). Grouping representatives by (sorted values, canon) is exact:
  distinct canons per sorted-value group = number of Γ-orbits in that
  fiber. Split fibers are groups with ≥ 2 canons; sorted(w) per orbit
  (w = Hy/D, exact integers, Γ-equivariant so constant on orbits)
  decides P_w.
- Support: global supp = AND of component supports (wave 16, exact
  factorization), constant on component fibers (verified: no mixed
  fiber) and hence on global fibers. Census scope is exactly the
  4,010,394 fibers fully meeting support (average size ≈ 23.95,
  consistent with |supp| = 96,049,800).

## Numbers

- Split fibers on support: 762 (sizes: 48×729, 24×28, 72×3, 36×2).
- P_w-failing split fibers: 152 (sizes: 48×146, 24×6). Split but
  correctly separated by sorted(w): 610.
- All 5 lifts of the q=81 component split separate correctly, including
  the two 36-point fibers (3 orbits of 12, the wave-16 lift type).
  **All 152 failures are gluing splits** (81-component unsplit).

## Exhibit (first failing fiber, combo [1, 6, 0, 1, 0])

Two valid Fix points, both in support, same fiber, distinct Γ-orbits
(canons differ; brute force over all 24 perms confirms no γ maps one to
the other), identical sorted(w) = (-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5):

- y1 = [1024531200, 475675200, 292723200, 1280664000, 1244073600,
  36590400, 512265600, 1500206400, 804988800, 256132800, 731808000,
  1061121600]
- y2 = [1244073600, 256132800, 292723200, 1500206400, 1024531200,
  36590400, 731808000, 1280664000, 804988800, 475675200, 512265600,
  1061121600]

A second failing fiber (combo [1, 6, 1, 2, 0]) was verified the same way.

## Consequence for 152, route (b)

Only split fibers contribute to Bsym_w − Bsym_Γ, so the difference is
exact from the census: Σ over split fibers of (Σ_class |C|² −
Σ_orbit |O|²) = 169920, hence

- Bsym_w(supp) = 383795287/16008300 ≈ 23.974769,
- Bsym_Γ(supp) = 383766967/16008300 ≈ 23.972999 (wave 17),
- difference ≈ 0.001769 > 0.

So the (B1) value equality Bsym_w = Bsym_Γ, which held at m=8
(318335/20808), **fails at m=12**. Combined with wave 17 ((B2) fails via
D1a/D1b cancellation, and O′ is false at m=12), route (b) for 152 fails
at m=12 in both readings. P_w as a general separator on support is dead;
152's separation step needs something beyond (fiber,w)-classes, or a
different restatement. (For completeness: P_w at m=8 on support still
stands; the failure is specific to m=12 gluing splits.)

## Scope limits (honest)

- Census covers fibers meeting support at m=12 under the s=1 torsion
  criterion only; off-support fibers were not censused (irrelevant for
  Bsym on support, but P_w off support is a separate question).
- The 610 split-but-separated fibers were checked only for sorted(w)
  distinctness across orbits, not for any finer invariant.

## Files

- Script: [wave18_Pw_m12_census.py](wave18_Pw_m12_census.py)
- Full data (all 762 split fibers, orbits, sorted(w)): `wave18_Pw_m12_census.json` (not in repository)
