# Wave 38, task 5 — Non-affine pairs beyond the slice: generalized

## Verdict

1. **The two exceptional fibers at m=30 ARE full Fix_30 fibers, exactly.**
   The 18,000 non-affine pairs persist in full Fix_30, and scaling
   splitting accounts for at least 72,000 pairs there (constant-padding
   family). Wave 37's 10-unit U_S is only representatives: the full
   fiber-preserving unit group is all 250 units ≡ ±1 mod 5.
2. **Analogous scaling-split fibers exist at m = 12, 24, 36, 42, 48, 60**
   — dozens to hundreds per slice, all scaling-explained wherever the
   mechanism was tested. No new mechanism appeared anywhere.
3. **No scaling-split fibers in the tested slices at m = 6, 18**
   (m=18's ker(32)×ker(38809) slice was not computed: 38809² pairs
   infeasible by brute force; full Fix_18 is not enumerated).

## 1. Full Fix_30: fibers 45/186 generalize exactly

D_30 = 2^5·5^4·7^2·29^2·31^4·41^2·269^2, slice modulus 625·841
= 525625. Slice reproduced independently: 525,625 points, 9,061
fibers, exactly two of size 150, with 841-component zero,
625-component divisible by 25, (÷25) value sets with mod-5
reductions {0,1,4} and {0,2,3}, 5 affine orbits of 30 each.

**Proof the slice fibers are full fibers.** A global row is
determined position-wise by its component tuple (CRT injectivity),
so two global rows share a sorted global multiset iff they share
the multiset of component tuples. The slice rows have tuple
multiset {(a_i, 0, 0, …)} (zeros at 32, 49, 923521, 1681, 72361);
any global row with that tuple multiset has zeros elsewhere and
625-component in the slice fiber. Hence each exceptional fiber
has exactly 150 rows in full Fix_30, in 5 affine orbits of 30,
i.e. 9,000 cross-orbit pairs each — the 18,000 persist verbatim.
Verified: lifted reps satisfy the recurrence mod D_30, true
affine orbit size 30 (kernel-restricted; a naive multiset-only
count gives 120 by counting non-kernel reindexings), U_S scaling
reaches all 5 orbits with u-groups {±1},{±4},{±6},{±9},{±11}.

**Constant-padding family (new).** At odd components the only
constant kernel row is 0 (4c ≡ 0 mod q forces c = 0); mod 32 the
constants are {0, 8, 16, 24}. Padding either exceptional fiber
with a constant 32-component gives, by the same tuple argument,
a full fiber of 150 rows in 5 affine orbits. Verified: all six
padded reps satisfy the recurrence mod D_30 with true affine
orbit size 30. Total: 4 paddings × 2 fibers × 9,000 = **72,000
non-affine pairs** in full Fix_30 explained by scaling splitting.

**Full unit group at m=30 (correction to wave 37).** All 250 units
u mod 625 with u mod 5 ∈ {1,4} preserve fiber 151, 50 per orbit.
So the fiber-preserving group is the preimage of {±1} mod 5,
acting through C_5 with kernel the 50 units ≡ ±1 mod 25 — the
same numbers as at m=60 below. Wave 37's 10 units were representatives.

**Open at m=30.** Whether non-constant paddings (other components
non-constant but stratified U_S-invariant) give further split
fibers in full Fix_30; the stratified condition is: within each
level set of the other components, the 625-multiset must be
U_S-invariant.

## 2. Other m: scaling splitting is the universal mechanism

Slice = ker(q1)×ker(q2) with other components zero (fiber-closed:
mates preserve component multisets). Fibers by sorted multiset;
orbits under affine maps σ(i) = ui + c. Multi-orbit fibers and
their mechanism (scaling of one component transitive on orbits,
scaling of the other stabilizes orbit 0):

| slice | multi-orbit fibers | largest fiber, orbits | scaling comp. | units/orbit |
|---|---|---|---|---|
| m=12, 128×81 | 68 | 72 = 3×24 | 81 | 9 (27 preserving) |
| m=12, 81×25 | 1 | 36 = 3×12 | 81 | 18 (54 = all units) |
| m=24, 512×81 | 150 | 288 = 3×96 | 81 | 9 (27 preserving) |
| m=24, 81×25 | 1 | 36 = 3×12 | (same fiber as m=12) | — |
| m=36, 128×729 | 136 | 648 = 9×72 | 729 | 27 (243 preserving) |
| m=36, 729×25 | 44 | 324 = 9×36 | 729 | 54 (486 = all units) |
| m=42, 2401×25 | 65 | 588 = 7×84 | 2401 | 98 (686 preserving) |
| m=48, 2048×81 | 296 | 1152 = 3×384 | 81 | 9 (27 preserving) |
| m=60, 625×81 | 49 | 600 = 5×120 | 625 | 50 (250 preserving) |
| m=60, 625×121 | 72 | 600 = 5×120 | 625 | 50 (250 preserving) |

Pattern: the scaling component is always an odd prime power
p^e, e ≥ 2; the number of orbits is p^k (3, 9, 5, 7); the
fiber-preserving units form a subgroup of (Z/q)^× (typically the
preimage of a small subgroup mod p, e.g. {±1} mod 5 at 625,
index 3 at 2401) acting transitively on orbits. The other
component's units always stabilize orbit 0 (sometimes all of
them, e.g. 25-scaling at m=12/36, 121-scaling at m=60).
No multi-orbit fiber anywhere failed the scaling explanation
where the mechanism was tested (largest fiber of every slice
above except m=24, 81×25, which is the m=12 fiber doubled).

**m=48 correction.** The wave-38 odd×odd slices (25×49, 289×25)
showed 0 multi-orbit fibers, but that was a slice artifact:
the 2-part slice 2048×81 has 296. Lesson: test 2-part slices.

## 3. The b-sequence screen does NOT predict splitting

For every prime 5 ≤ p ≤ 200, the b-sequence value set
S_p = {b_j mod p} is a proper subset of F_p, with stabilizer
exactly {±1} (from b_{-j} = −b_j). Counting reason: b_j depends
on α^j up to inversion, α of order d | p±1, so
|S_p| ≤ (d+2)/2 < p. Hence mod-p stability is generic and
predicts nothing. The operative condition is one level up:
the value set mod p^f must be the **saturated lift** of a
±1-stable mod-p set (at m=30: all residues mod 25 with mod-5
in S_5 = {0,1,4}), so that every unit ≡ ±1 mod p preserves it,
while the cyclic arrangement — hence the dihedral orbit —
changes. Reflection symmetry (orbit size = m, not 2m) is what
makes the split visible as multiple affine orbits rather than
one large orbit. This saturated-lift recipe is the structural
summary of all observed cases, not a proved classification.

## 4. Negative cases and honest limits

- m=6: slices 25×49, 32×25, 32×49 — 0 multi-orbit fibers.
- m=18: slices 25×38809 (wave 36: every fiber a single affine
  orbit), 32×25, 32×49 — 0 multi-orbit fibers. The slice
  32×38809 was not computed (brute-force kernel mod 38809
  needs 38809² pairs); odd-component scaling splitting at m=18
  is already ruled out by wave 36's full 25×38809 slice.
- m=42, slice 2401×169 was not computed (68.6M points, memory);
  the m=42 answer comes from 2401×25.
- Full Fix_m is enumerated nowhere except via the m=30 tuple
  argument; all other-m claims are slice-exact, not full-space.
- Scaling splitting is the only mechanism observed, but it is
  not proved to be the only possible one.

## Files

- `wave38_nonaffine_general.py` (m=30 slice reproduction),
  `wave38_nonaffine_lift.py` (buggy multiset-only orbit count —
  superseded), `wave38_nonaffine_lift2.py` (corrected lift +
  paddings), `wave38_nonaffine_other_m.py` (slice census +
  b-screen), `wave38_nonaffine_mechanism.py`,
  `wave38_nonaffine_mech2.py`, `wave38_nonaffine_refine.py`,
  `wave38_nonaffine_close.py` (mechanism tests). Repository
  untouched, no Lean built.
