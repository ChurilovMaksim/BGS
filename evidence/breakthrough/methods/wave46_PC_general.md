# Wave 46, task 7 — PC in general: compatibility step

## Verdict

**Full-space PC at m = 24 is NOT proved, but the compatibility step is
now sharply isolated.** Pairwise compatibility is proved exhaustively
for every small-component pair (16,211,212 joint pairs, 0 failures),
and the non-dihedral core at (81, 512) is proved exhaustively
(3,781,916 joint pairs, 0 failures). What remains is exactly: (i)
triple intersections — pairwise-clean Π cosets can still fail
jointly, and (ii) pairs involving 1153² beyond the slice. No
counterexample to full PC was found anywhere. No Lean built,
repository untouched.

## 1. Setup

D_24 = 2^9·3^4·5^2·7^2·11^2·17^2·1153^2, t = gcd(24,4) = 4, π ∈ D_4
(class maps r ↦ r+b, r ↦ −r+b). For a pair (y, y′) with equal global
multiset, Π_q = {π : prof′_q[r] = prof_q[π(r)] ∀r}. PC is ∩_q Π_q ≠ ∅.
Slice = (289, 1153²) components (wave 44: 0 failures in 376,185,238
slice pairs). Other components: 25, 49, 81, 121, 512.

## 2. Slice reframing: slice fibers are dihedral orbits

Mod-p lemma (wave 12 §3a): equal multiset ⟹ dihedral image. Hence
every slice mate arises from (d, e) ∈ D_24² with t′ = t∘d, s′ = s∘e
and equal pair multiset. Enumerating all 48² (d, e) for 61 random
base points gives mates = 48 (24 with stabilizer) in every case,
**all dihedral images, 0 non-dihedral mates**. Consistent with wave
44's average fiber size 47.94 ≈ 48 = |D_24|. So slice PC is, modulo
§3a, the dihedral class-map statement — the slice does not constrain
a global σ beyond its class map. (An earlier random sampler was
abandoned: it found nothing in 3 min because the first base point's
fiber is purely dihedral.)

## 3. Per-component Π catalog (exact)

Kernel sizes and "full" fractions (all four class multisets equal):
25: 25, 13/25; 49: 49, 49/49; 81: 81, 1/81; 121: 121, 1/121; 289: 289,
1/289; 512: 512, 4/512. Π_q is never empty for any single-component
pair. Π-set shapes: 25: full, {f1,f3,s1,s3}, {f0,f2,s0,s2} (parity
cosets); 49: always full; 81, 121: exactly the 16 two-sets {f_b, s_c};
289: 8 singletons + 16 two-sets; 512: singletons, two-sets, one
4-set; 1153² (300k sample): singletons + two-sets, as at 289.
Mechanism: at non-constraining q, Bα^12 = B, so class multisets are
α⁴-cycle traces; orbit size d gives gcd(d,4) cycles (d odd ⟹ full).

## 4. Non-dihedral pairs live only at 81 and 512

Single-component pairs (y, y′) with equal multiset, tested for
y′ = y∘d, d ∈ D_24: 25: 60/60 dihedral; 49: 93/93; 121: 660/660; 289:
1648/1648; **81: 432/840 non-dihedral; 512: 896/2830 non-dihedral**.
So the only possible source of non-dihedral global σ's is (81, 512).

## 5. (81, 512) subsystem: exhaustive, 0 failures

Joint pairs = pairs of joint sequences with equal multiset of the 24
value-pairs (the common-σ condition). C++ exhaustive search:
10,827,420 mate combos (= Σf²(81)·Σf²(512) − diagonals, exact
identity), 3,781,916 joint pairs, of which 1,407,260 dihedral and
2,374,656 non-dihedral — **Π_81 ∩ Π_512 ≠ ∅ for all of them**.
Two C++ bugs were caught by cross-checks (kernel sizes vs Python):
C++ `%` on negatives in the recurrence and in reflection maps gave
false failures first; fixed, counts verified by the exact identity.

## 6. All small-component pairs: exhaustive, 0 failures

Joint pairs (ordered, excl. diagonal), C++ exhaustive:

| pair | joint | pair | joint |
| (81,512) | 3,781,916 | (81,25) | 41,928 |
| (81,121) | 212,280 | (512,25) | 679,676 |
| (512,121) | 2,979,740 | (81,49) | 83,274 |
| (81,289) | 1,896,816 | (512,49) | 1,425,332 |
| (512,289) | 2,143,772 | (25,121) | 61,920 |
| (25,289) | 402,008 | (49,121) | 125,346 |
| (49,289) | 828,314 | (121,289) | 1,536,776 |
| (25,49) | 12,114 | total | 16,211,212 |

**0 failures in all 15 pairs.** Patterns: (25,121), (49,121),
(121,289), (25,49) joint pairs are all dihedral; (512,49) and
(49,289) have mate combos = joint pairs (every fiber-mate combo is
jointly compatible — the 3-periodic 49-vectors are transparent).

## 7. Confinement of non-dihedral σ's, and harmless leaks

For every non-dihedral pair at 81 (432) and 512 (896), 3 sampled σ's
each: V_q(σ) = {y ∈ ker_q : y∘σ ∈ ker_q} and dim_1153(σ) (exact
2-dim linear algebra over F_1153). 81-σ's: 0 leaks. 512-σ's: 4 leaks
(4/896 pairs, one σ each), all with |V| = {25:5, 49:7, 81:9, 121:1,
289:1, 512:512}, dim_1153 = 0 — leaks only to the loose components
25/49, never to 121/289/1153. Triple analysis on all 4 leaks:
Π_25(nonzero) = {f0,f2,s0,s2} (parity-preserving coset), every Π_81
2-set contains an anchor in it (f2, f0, s0, s2 per leak), and
**triple-empty combinations: 0**. Mechanism: σ imprints one anchor
class map respected at 25, 81, 512 at once. V-sets are deep layers
(9-divisible at 81, 64-divisible at 512) — σ moves only vectors
insensitive to its fine structure.

## 8. What remains (exact gaps)

1. **Triple intersections.** Pairwise-clean does not imply total:
   three Π cosets can meet pairwise but not jointly (wave 12 §2
   pattern, at prime-power level). Closing this needs
   pair-contingency at prime-power level for ≥3 components — the
   same kind of gap as wave 12 §3b, now localized to all-dihedral
   pairs (non-dihedral pairs are confined to (81,512) and clean).
2. **Pairs involving 1153² beyond slice.** (289,1153²) is wave 44;
   (q,1153²) for q ∈ {25,49,81,121,512} is not exhaustively run
   (1.33M kernel). Evidence: dim_1153(σ) = 0 for all sampled
   non-dihedral σ's, and 1153²-pairs are dihedral by §3a mod 1153.
3. **§3a dependence.** The slice-orbit claim (§2) and the
   completeness of the (d,e) enumeration rest on wave 12 §3a.

## Files

- This note: `methods/wave46_PC_general.md`
- `wave46_PC_kernels.py` (fractions, orbit sizes, Π emptiness),
  `wave46_PC_pisets.py` (Π-set catalogs, 1153² sample),
  `wave46_PC_de_mates.py`, `wave46_PC_scanbase.py` (slice mates),
  `wave46_PC_dihedral.py` (non-dihedral pairs),
  `wave46_PC_sigma.py`, `wave46_PC_Vsets.py`, `wave46_PC_Vdihedral.py`
  (σ realizability, V-sets), `wave46_PC_confinement.py`,
  `wave46_PC_leaks.py` (confinement + triple analysis),
  `wave46_PC_joint.cpp` (generic exhaustive joint search),
  `wave46_PC_joint81512.cpp` (superseded (81,512) version),
  `wave46_PC_slicemates.cpp` (abandoned sampler),
  `wave46_PC_joint81512.log` (final (81,512) run).
