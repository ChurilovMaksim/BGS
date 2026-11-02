# Wave 37, task 5 — The 18,000 non-affine pairs at m=30: characterized

Setup (wave 36): slice ker(625) × ker(841) at m=30, 525,625 points,
9,061 fibers by sorted multiset, 15,420,460 pairs. A pair has an
exactly-affine matching iff its points lie in one affine orbit
(σ(i) = ui + c, gcd(u,30) = 1; 240 maps). Wave 36 found 18,000 pairs
without one, all in fibers of size 150. Here is exactly which pairs
they are, and the single mechanism producing them.

## Proved criterion (verified exactly on all 15,420,460 pairs)

A pair lacks an exactly-affine matching **iff** it lies in one of
the two exceptional fibers (ids 45, 186) **and** its two rows lie
in different dihedral orbits (rotation classes) of that fiber.
All other 9,059 fibers are single affine orbits. Count check:
per exceptional fiber, C(150,2) − 5·C(30,2) = 11,175 − 2,175 =
9,000 cross-orbit pairs; 2 × 9,000 = 18,000. Base-other check:
2 × (150 − 30) = 240, matching wave 36's (b).

## The two exceptional fibers (every fact verified exactly)

- Size 150 each — the only size-150 fibers in the slice (next
  sizes: 120, 60, 30, 20, 10). Each is exactly 5 affine orbits
  of size 30.
- 841-component: the zero row (i2 = 0 for all 150 members).
- 625-component: every row divisible by 25. Value sets (÷25):
  fiber 45 = residues mod 25 with mod-5 reduction in {0,1,4};
  fiber 186 = {0,2,3}. Each value occurs exactly twice
  (15 values × 2 = 30 positions).
- Every member is reflection-symmetric: stabilizer exactly
  {id, one reflection} (size 2, verified for all 300 members).
  For the orbit representatives the valid affine maps are
  exactly the 60 dihedral maps (u ∈ {1, 29}); hence each affine
  orbit is exactly the rotation class of its representative
  (30 rotations, verified via the global orbit partition).
- Within each fiber, the 5 orbits are distinguished by their
  unordered cyclic adjacent-pair multisets (all 5 distinct
  in each fiber).

## The single mechanism: residue scaling ("scaling splitting")

Let U_S = {u mod 25 : u mod 5 ∈ {1,4}} (10 units). Scaling a row
by u ∈ U_S preserves the value set (u preserves the residue
set), hence preserves each fiber — but scaling is not a
position permutation, so it moves a row to a different
dihedral orbit. Verified action tables:

- U_S acts transitively on the 5 orbits of each fiber, and
  factors through U_S/{±1} ≅ C5: u and −u act identically
  (negation of a row is a rotation of it, verified).
- The two fibers are exchanged by scaling by 2: ×2 maps
  fiber 45's K1 row set exactly onto fiber 186's, and ×2⁻¹
  back (mod-5 classes {0,1,4} ↔ {0,2,3}).
- Example (wave 36's counterexample): base pt 841 (i1=1,i2=0)
  and other pt 3364 (i1=4,i2=0) lie in fiber 45 in orbits 841
  and 3364; rep 3364's K1 row is exactly 4 × rep 841's K1
  row mod 625.

So one scaling class = 2 fibers × 5 dihedral orbits: the
multiset does not determine the dihedral class, because
residue scaling rearranges values while preserving the
multiset. That is the whole content of the 18,000: they are
the cross-orbit pairs of this one scaling class, nothing else.

## Why it happens (structural explanation)

Kernel rows are closed under shifts and reversal (dihedral),
but a multiplier u ∉ {±1} generally sends a kernel row
outside the kernel — so for these rows the only valid affine
maps are dihedral, and reflection symmetry cuts dihedral
orbits from 60 to 30. The value set S (residues with mod-5
in {0,1,4}) is stable under U_S, so scaling produces new
rows with the same multiset but a different cyclic
arrangement (different adjacent-pair multiset) — hence a
different dihedral orbit. At m=18 no such scaling-stable
value set occurs, so every fiber was a single affine orbit;
at m=30 the 25-divisible 625-component supplies one.

## Answers to wave 36's open questions

- Failures concentrate in large fibers only: YES — only in
  the two size-150 fibers (the maximum size).
- Fibers are unions of whole affine orbits: YES, trivially
  (orbits partition fibers); the refined fact is that
  9,059/9,061 fibers are single orbits.

## Limits

- Slice only (ker(625) × ker(841), other components zero);
  full Fix_30 is not enumerated. The criterion is exact
  within the slice; whether scaling splitting accounts for
  all non-affine pairs in the full space is open, but the
  mechanism is structural (dihedral-closed kernel, scaling-
  stable value sets), so it should generalize.
- The adjacent-pair multiset separates the 5 orbits in each
  exceptional fiber but is not claimed as a global orbit
  invariant (affine maps with u ∉ {±1} change distance-1
  pairs).

## Files

- `wave37_nonaffine.py` (reproduction + orbit partition;
  18,000 verified), `wave37_nonaffine2.py` (fiber
  dissection), `wave37_nonaffine3.py` (value sets, adj-pair
  multisets, scaling between reps), `wave37_nonaffine4.py`
  (stabilizers, scaling action table). Repository untouched,
  no Lean built.
