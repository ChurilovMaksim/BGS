# Wave 36, task 5 — σ-structure at m=18 and m=30

## Verdict (three readings, three outcomes)

A matching for a pair (y, y′) is a permutation σ of Z/m with
y′_i = y_{σ(i)} (equivalently, equal sorted multisets). t = gcd(m,4)
= 2 at both m, so classes are even/odd positions, D_2 = {id, swap}.

- **σ exactly affine** means σ(i) = ui + c (mod m), gcd(u,m) = 1.
- **σ affine up to class permutation** means σ = a∘ρ for affine a
  and class-preserving ρ. This holds iff σ maps each class onto a
  single class O_{ur+c}, i.e. iff σ is class-preserving with
  π ∈ D_2 (affine class maps are exactly D_2 here). Existence of
  such a matching for a pair is equivalent to per-class multiset
  equality under id or swap, i.e. to JBL existence for the pair.

Results: the **literal** conjecture ("every matching σ is
class-affine") is **FALSE** at both m, but only through the trivial
mechanism of wave 34 §0: values repeated across parities let one
swap images and break class-affineness. The **existence** reading
(some class-affine matching) holds everywhere: **0 failures**.
The **strong** reading (some exactly-affine matching) holds for
**every** pair at m=18 but **fails** at m=30 (18,000 pairs).
Repository untouched, no Lean built.

## Slices (fiber-closed, hence exact within the slice)

Mates preserve component multisets, so fixing components to zero
(resp. constant) is fiber-closed. Global values are injective in
the varying pair values, so fibers = sorted-pair-multiset groups,
and matching is componentwise pair matching.

- m=18: mod-32 constant 0, mod-49 = 0, mod-39601 = 0; varying
  ker(25) × ker(38809) (wave-35 constructions) = 970,225 points.
- m=30: all components 0 except ker(625) × ker(841) (brute force,
  asserted size = q) = 525,625 points. This is a structured
  sample of Fix_30, not a random one: random global sampling
  gives no pairs at D_30 ≈ 9.3×10^22. Full Fix_18/Fix_30 are
  not enumerated (D_18 ≈ 6.0×10^13).

## m=18: 27,445 fibers, max size 36, 942,780 base-other pairs

- (a) Class-affine existence, all 16,819,800 pairs: **0 without**.
- (b) Exactly-affine existence: base-other 942,780/942,780;
  all pairs 16,819,800/16,819,800 (affine-orbit incidences;
  5 pairs verified directly). Every fiber is a single affine
  orbit; max fiber 36 = 2m suggests fibers are dihedral orbits.
- (c) Literal per-σ, base-other pairs: all matchings
  class-affine 934,440; some non-class-affine matching 8,340;
  no class-affine matching 0. Exact test: for value v, with
  x = #{i even : σ(i) even}, achievable x is the interval
  [Σ_v max(0, a_0+b_0−n_v), Σ_v min(a_0, b_0)]; all matchings
  class-affine iff it is exactly {0} or {9}.

Explicit non-class-affine σ (verified: matching, maps some even
position to even and another to odd, so neither id nor swap):
base pt 38809, other pt 155236 (slice indices),
σ = [3,5,4,0,2,1,6,11,10,9,8,7,12,17,16,15,14,13].
Mechanism: value 0 occurs at both parities; swapping images of
two same-value opposite-parity positions breaks class-affineness.

## m=30: 9,061 fibers, max size 150, 516,564 base-other pairs

- (a) Class-affine existence, all 15,420,460 pairs: **0 without**.
- (b) Exactly-affine existence: base-other 516,324/516,564
  (240 without); all pairs 15,402,460/15,420,460 (**18,000
  without**). Fibers reach size 150 > 2m = 60: they span
  several affine orbits, unlike m=18.
- (c) Literal per-σ, base-other pairs: all matchings
  class-affine 506,358; some non-class-affine 10,206; none 0.

Explicit (b) counterexample pair (verified directly: all 240
affine maps (u,c) tested, none sends base to other): base pt
841, other pt 3364 in the slice (ker625 index 1 / ker841 index
0, resp. 4 / 0). Explicit (c) non-class-affine σ (verified):
base pt 4205, other pt 16820,
σ = [3,5,4,0,2,1,6,11,10,9,8,7,12,17,16,15,14,13,18,23,22,21,
20,19,24,29,28,27,26,25].

## Correction to the first (a) computation (honest bug note)

The first (a) run undercounted (8,687,748 with at m=18) because
the signature encoding used base N while unified even/odd ids
range over [0, 2N), colliding signatures. The reported (a)
numbers come from brute-force per-fiber signature counting,
which agrees with base-vs-other failures = 0 at both m and
with transitivity (class-affine matchings compose). Tests
(b) and (c) use independent paths (PA/PB affine maps; exact
contingency intervals) and were verified directly on examples.

## What this means

- The σ-structure conjecture in its literal per-σ form is dead,
  trivially: cross-parity value repetition always manufactures
  non-class-affine matchings. It was never a structural claim.
- The class-level (JBL) form is untouched: 0 failures at both m.
- The new structural fact is the m=18/m=30 split: exactly-affine
  matchings are universal at m=18 but not at m=30. So "σ is
  affine" is a property of small fibers, not a general lemma;
  any σ-structure route to JBL must go through class-affine
  existence (which holds), not through exact affineness.
- Open: whether the m=30 (b) failures concentrate in large
  fibers only, and whether fibers are always unions of whole
  affine orbits (suggested by both slices).

## Files

- This note: `methods/wave36_sigma_structure.md`
- `methods/wave36_sigma_structure.py` (main run; log
  `wave36_sigma_structure.log`)
- `methods/wave36_sigma_structure_a_fix.py` (corrected (a) attempt
  — see bug note; definitive (a) numbers are from the debug
  scripts below)
- `methods/wave36_sigma_debug_a.py` (m=18 brute-force (a)),
  `methods/wave36_sigma_debug_a30.py` (m=30 brute-force (a))
