# Γ-orbits per fiber — working note (not a proof for general m, not a Lean theorem)

Conventions (as in the wave-3 O* test): `Fix_m = ker(H_m mod D_m)`,
`H_m = 6I − C − Cᵀ`, `D_m = det H_m`. A fiber is a `sorted(y)` class.
Γ is the dihedral group `j ↦ ±j + k mod m`, acting by `(γ·y)_j = y_{γ(j)}`
(so Γ-orbits always lie inside fibers). Aff is `j ↦ a·j + b`,
`a ∈ (ℤ/m)ˣ`. All enumeration below is exact integer arithmetic;
it is a verifier artefact, not a Lean theorem.

Question: is the number of Γ-orbits inside one fiber bounded by a small
constant (e.g. 2) for all m, or can it grow?

## Answer

**No universal bound exists at all. The number of Γ-orbits per fiber is
unbounded in m:**

- No bound ≤ 2: at m = 12 there is a fiber with exactly 3 Γ-orbits
  (§m=12).
- Growth: at m = 16, 32, 64 there are fibers with exactly 4, 8, 16
  Γ-orbits (§2^k family). The mechanism is the coset index
  `[Aff : Γ] = φ(m)/2`: a fiber that is one full affine orbit of a
  distinct-entry vector splits into exactly `φ(m)/2` dihedral orbits.
  Along `m = 2^k` this is `2^{k-2}` → ∞.
- By contrast, m = 9, 10, 11, 13 have exactly 1 Γ-orbit per fiber, and
  m = 8 has max 2. So the orbit count is 1 for many m, then jumps:
  2 (m=8) → 3 (m=12) → 4 (m=16) → 8 (m=32) → 16 (m=64).

## Table (Γ-orbits per fiber, by m)

| m | fibers | Γ-orbits | max orbits/fiber | status |
|---|---|---|---|---|
| 8 | 85106 | 85145 | 2 (39 fibers × 2) | global enumeration (M08 / wave-3 O*) |
| 9 | 108505 per mod-4 slice (×4 slices) | = fibers | 1 | NEW global C++ check (§m=9) |
| 10 | — | = fibers | 1 | Tag A/B dihedral arguments + NEW dihedral-criterion C++ remainder search (§m=10) |
| 11 | — | = fibers | 1 | dihedral argument, all cases (§m=11) |
| 12 | — | ≥ fibers + 2 | ≥ 3 (one fiber: exactly 3) | explicit lift (§m=12) |
| 13 | — | = fibers | 1 | dihedral argument, all cases (§m=13) |
| 16 | — | — | ≥ 4 (one fiber: exactly 4 among lifts) | full-permutation fiber, coset mechanism (§2^k) |
| 21 | — | — | ≥ 7 (exactly 7 among lifts) | mod-49 fiber, verified globally (§m=21/24) |
| 24 | — | — | ≥ 6 (exactly 6 among lifts) | mod-72 fiber, verified globally (§m=21/24) |
| 30 | — | — | ≥ 5 (divisor fiber) | mod-25 fiber (§scan) |
| 32 | — | — | ≥ 8 (exactly 8 among lifts) | same, verified globally (§2^k) |
| 64 | — | — | ≥ 16 (exactly 16 among lifts) | same, via canon transfer (§2^k) |

## m=12 — the candidate fiber (exactly 3 Γ-orbits)

Mod 81, `Fix_12 mod 81` has 81 vectors in 7 fibers; exactly one fiber
splits: sorted class `(9, 9, 18, 18, 36, 36, 45, 45, 63, 63, 72, 72)`,
36 vectors, split into 3 dihedral canons of 12 and 3 affine canons of
12 (dihedral and affine coincide on this fiber). All values are
multiples of 9: a torsion lift of a mod-9 kernel vector.

Lift to a global fiber: `D = 1536796800`, `M = D/81 = 18972800`,
`φ(t) = t·M·inv(M mod 81) mod D`. The 36 lifts are all in `Fix_12`
(verified: `H·y ≡ 0 mod D`), all share one sorted multiset, and have
exactly 3 global dihedral canons of 12. The reported wave-4 pair
`y, y′` is among the lifts. The global fiber is exactly these 36
vectors: any vector in it is a permutation of `y`'s entries, hence its
entries are multiples of `M`, hence its other prime-power components
are 0, hence it is the lift of its mod-81 reduction, which lies in the
mod-81 fiber. So this global fiber has exactly 3 Γ-orbits of size 12.
In particular no bound "≤ 2 orbits per fiber for all m" holds.

Why the lift preserves orbit counts (general lemma, used in §scan):
for any divisor `d | D_m`, the map `z ↦ (D_m/d)·z` sends `ker(H_m mod d)`
injectively into `Fix_m`, commutes with position permutations, and
sends equal sorted multisets to equal sorted multisets; hence the
number of Γ-orbits in the lifted fiber equals the number in the
mod-`d` fiber, and the global fiber containing the lifts has at least
that many Γ-orbits (adding vectors cannot merge orbits).

## m=9 — global check (NEW)

Global vectors are CRT triples `(c, v49, v39601)` with `c` constant
mod 4. The C++ check (`gamma_m9.cpp`, 0.8 s) loops over all
`49 × 39601 = 1,940,449` pairs at fixed `c = 0` — the other `c`-slices
are isomorphic (adding a constant to all packed keys preserves sorted
order and lex-min canons) — with packed key `v49 + 49·v39601` per
position, and counts distinct dihedral canons per sorted key.
Result: 108,505 fibers, max 1 dihedral canon per fiber. So every
m=9 fiber is a single Γ-orbit. This is stronger than the wave-4 result
(affine-canon search + argument): the repeated-value case, whose
earlier search used an affine-canon hit criterion, is now covered by
the dihedral criterion directly.

## m=10 — Tag arguments + dihedral-criterion remainder search (NEW)

Tag A (q841 distinct) and Tag B (q32 non-constant + q1681 pattern
distinct) conclude with a global *dihedral* permutation
(`σ = d_841`, resp. `σ = p` with `a = 1` or `9`), so those fibers are
single Γ-orbits. The remainder (q841 non-distinct AND (q32 constant OR
pattern non-distinct), 3,470,912 vectors) was previously searched only
with an affine-canon hit criterion, which does not exclude
Γ-splitting inside one affine orbit. Rerunning the same search with a
dihedral-canon hit criterion (`ostar_m10_remaining_gamma.cpp`):
17,609,232 combinations over 184,590 dihedral-orbit representatives,
**0 hits**. Hence every remainder fiber is also a single Γ-orbit.
Combined: m=10 has exactly 1 Γ-orbit per fiber. (Fibers do not cross
the Tag/remainder boundary: component distinctness profiles are
preserved by dihedral permutations, and Step 2 of the wave-5 note gives
that every fiber-mate's components are dihedral images of the base's.)

## m=11 and m=13 — dihedral arguments (from the wave-5/6 notes)

- m=11: the wave-5 argument concludes in every case with a global
  dihedral permutation (distinct component ⇒ `σ = d_i`; one
  non-constant component ⇒ its dihedral perm; both non-constant
  reflection components ⇒ a rotation `rot^k` or a reflection
  `p(j) = c − j`; all constant ⇒ singleton). Hence 1 Γ-orbit/fiber.
- m=13: the wave-6 argument is the same shape (distinct component ⇒
  `σ = d_i`; reflection-only ⇒ rotation or reflection by the
  intersection argument, cross-equalities holding for exactly one `j`
  since 2 is invertible mod 13). Hence 1 Γ-orbit/fiber.

## m=8 — reference values

85106 fibers, 85145 Γ-orbits: 39 fibers split into exactly 2 orbits
each (33 fibers of size 32 as 16+16, 6 fibers of size 16 as 8+8),
all other fibers single orbits. Max = 2. Note the scanner result at
`d = 24`: `ker(H_8 mod 24)` has 576 vectors, 66 fibers, max 2 dihedral
canons but max 1 affine canon (9 dihedral-bad fibers) — i.e. the
m=8 Γ-splitting is already visible at the torsion level `d = 24`,
while affine separation holds there. Affine-clean does not imply
Γ-clean.

## Mechanism for growth (§mechanism) and its obstruction

Where does splitting come from? Two distinct mechanisms are now
established:

1. **Torsion lifts** (m=8, m=12): a vector that is a lift from a
   smaller modulus (`y = (D/d)·z`, `z ∈ ker mod d`) has extra position
   symmetries. At m=8 the splitting is a `d = 24` torsion phenomenon
   (9 dihedral-bad fibers mod 24, affine-clean there); at m=12 it is
   a mod-9 fiber (values all multiples of 9, already splitting into 3
   mod 9, hence mod 81 and globally) lifting to 3 orbits.
2. **Coset index** (m=2^k): a distinct-entry vector whose full affine
   orbit lies in the kernel splits into `[Aff:Γ] = φ(m)/2` dihedral
   orbits (§2^k). This is the unbounded mechanism: 4, 8, 16, ….

A third conceivable route — (b) two independent torsion mechanisms in
one m whose lifts combine with aligned value multisets — has a genuine
obstruction: CRT-combining two bad component fibers requires the
combined value multisets to match, which is the same gluing problem
that kills most naive combinations (cf. the m=9 gluing analysis:
per-component bad fibers are not sufficient — at m=8 the prime-power
components are affine-clean and the splitting comes from
cross-component gluing at the composite torsion level). Route (b) is
not needed for unboundedness, since route 2 already gives it.

## The 2^k family — unbounded growth (§2^k)

For `m = 2^k`, `ker(H_m mod m)` contains the full-permutation fiber
(sorted = `0..m−1`), generated by the `(0,1)`-seeded recurrence
`v_{i+1} = 6v_i − v_{i-1}` (e.g. m=16: `(0,1,6,3,12,5,2,7,8,9,14,11,4,13,10,15)`).
Why it splits into exactly `φ(m)/2` orbits:

- All entries distinct ⇒ dihedral stabiliser trivial ⇒ each dihedral
  orbit has size `|Γ| = 2m`.
- All entries distinct ⇒ affine stabiliser trivial ⇒ the affine orbit
  has size `|Aff| = m·φ(m)`, and the whole affine orbit lies in the
  kernel (verified: fiber = affine orbit at m=16, 32, 64).
- Hence the fiber splits into `|Aff|/|Γ| = φ(m)/2 = 2^{k-2}` dihedral
  orbits: 4 (m=16, orbits of 32), 8 (m=32, orbits of 64), 16 (m=64,
  orbits of 128).

Lift to global fibers: `m | D_m` for m = 16, 32, 64 (verified), and the
multiplication lift `z ↦ (D_m/m)·z` is injective on `ℤ/m`, commutes
with position permutations, and (for these lifts, `z < m` so the lift
is exact, `M·z`, with `M > 0`) preserves lex order, hence preserves
dihedral-canon counts exactly. Verified globally: m=16 lifts all in
`Fix_16`, one sorted multiset, 4 global canons of 32; m=32 lifts all
in `Fix_32`, 8 global canons of 64; m=64 lifts all in `Fix_64`, canon
transfer checked on 20 vectors, count 16. So global fibers at
m = 2^k contain at least `2^{k-2}` Γ-orbits: the count is unbounded
in m. (Prime moduli do not give this: `ker(H_p mod p)` is trivial
for p = 17, 19, 23, 29, 31 — only the zero vector — so the prime route
to `φ(p)/2` fails at `d = p`; the 2-power route is the one that works.)

## Divisor scan (§scan) — COMPLETE

Method: for m = 1..30, every divisor `d | D_m` with `2 ≤ d ≤ 20000`
(2,431 pairs), enumerate `ker(H_m mod d)` with the C++ scanner
(`scan_divisor.cpp`: `(A^m − I)` congruence method, no `d²` scan),
group by sorted multiset, count distinct dihedral and affine canons
per fiber. All 2,431 pairs are now processed. Max dihedral canons per
m (divisor fibers; each lifts to a global fiber with at least that
many Γ-orbits, by the lemma in §m=12):

| max | m |
|---|---|
| 1 | 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 14, 17, 18, 19, 22, 23, 25, 26, 27, 29 |
| 2 | 8, 15, 20, 28 |
| 3 | 12 |
| 4 | 16 |
| 5 | 30 |
| 6 | 24 |
| 7 | 21 |

Standout rows (all verified as global lifts, not just mod-`d`):
- m=21, d=49: fiber 294 = 7 orbits × 42 (`|Γ_21|`), values the 21 units
  listed in §m=21/24 below; affine canons also 7.
- m=24, d=72: fiber 288 = 6 orbits × 48, affine canons 3 (each affine
  orbit = 2 dihedral orbits).
- m=30, d=25: fiber 150 = 5 orbits × 60, affine canons 5.
- m=15, d=287: 740 dihedral-bad fibers, max 2, affine-clean — so
  global m=15 also has split fibers (via lift), a case not covered by
  the earlier global arguments.

Limitation: 449/2,431 rows were skipped (446 for `|ker| > 3,000,000`
vectors, 3 for timeout) — large composite `d` with huge kernels.
Skipped rows are concentrated at m=12 (42), m=24 (151), m=30 (82),
m=20 (49), m=28 (47). The unboundedness verdict does not depend on
them (§2^k), and no skipped row can lower any maximum reported here.
One operational note: `/tmp` was wiped mid-scan, deleting the scanner
binary and the pair list; both were rebuilt under `workspace/` and
the 22 affected pairs rerun from there — all 2,431 pairs now have a
row.

## m=21 and m=24 — global lifts verified (§m=21/24)

- m=21, d=49, sorted `(1,2,4,8,9,11,15,16,18,22,23,25,29,30,32,36,37,39,43,44,46)`:
  mod fiber 294 vectors; lifts by `D_21/49` all in `Fix_21`, one
  sorted multiset, exactly 7 global dihedral canons of 42.
- m=24, d=72, sorted `(5,7,8,10,17,19,20,22,29,31,32,34,41,43,44,46,53,55,56,58,65,67,68,70)`:
  mod fiber 288 vectors; lifts by `D_24/72` all in `Fix_24`, one
  sorted multiset, exactly 6 global dihedral canons of 48.

## Files

- [This note](sandbox://workspace/bgs-breakthrough/methods/gamma_orbits_per_fiber_note.md)
- [m=9 global Γ check](sandbox://workspace/bgs-breakthrough/methods/gamma_m9.cpp)
- [m=10 remainder Γ check (dihedral criterion)](sandbox://workspace/bgs-breakthrough/methods/ostar_m10_remaining_gamma.cpp)
- [Divisor scanner](sandbox://workspace/bgs-breakthrough/methods/scan_divisor.cpp)
- [Divisor scan results (complete: all 2,431 pairs)](sandbox://workspace/bgs-breakthrough/methods/scan_divisors_results.jsonl)
- [m=21/m=24 global candidates](sandbox://workspace/bgs-breakthrough/methods/gamma_m21_m24_candidates.json)
- [m=9 component vectors](sandbox://workspace/bgs-breakthrough/methods/m9_q49.txt) (m9_q39601.txt likewise)
- [m=16 global candidate](sandbox://workspace/bgs-breakthrough/methods/gamma_m16_candidate.json)
- [m=32 global candidate](sandbox://workspace/bgs-breakthrough/methods/gamma_m32_candidate.json)
- [m=64 candidate summary](sandbox://workspace/bgs-breakthrough/methods/gamma_m64_candidate.json)
