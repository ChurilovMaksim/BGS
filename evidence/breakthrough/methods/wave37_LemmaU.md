# Wave 37, task 3 — lemma U: verified exactly at m=18, m=30, not proved in general

## Verdict

Lemma U (wave 36, §4: the pair multiset ℘ determines the unordered
block pair {T_pair(C^a,C^b), T_pair(α^u C^a, α^u C^b)}) is **not proved
in general**, but **no counterexample exists** at every exactly tested
case, and at m=30 the collisions are completely classified — all three
collision mechanisms preserve blocks. A background exact test at
m=30, (625, 72361) is running (15M/45.2M points, 0 conflicts at last
check); it is not needed for the verdict below.

## 1. Setup used for the tests

m = 2u, u odd, q = p^{2f} constraining (q | Tr(α^u)+2), p odd.
Kernel vectors at q are y_i = p^f·Tr(C α^i mod p^f), C ∈ R/p^f R
(R = Z[√2]), by Lemma P below; working with reduced traces is
equivalent (all kernel values divisible by p^f, blocks preserved).
Block0 = {(Tr(C^a β^k), Tr(C^b β^k))}, block1 = same with
(α^u C^a, α^u C^b), k ∈ Z/u, β = α²; ℘ = block0 ∪ block1.
Points are all (C^a, C^b); grouping is by ℘ (big-int base-B encoding,
B = p_a^{f_a}·p_b^{f_b}); a conflict is a ℘-group with two distinct
unordered block pairs.

## 2. Proved lemmas

**Lemma P (kernel parametrisation).** For constraining q = p^{2f},
v_p(α^u+1) = f: α^m−1 = (α^u−1)(α^u+1) with v_p(α^u−1) = 0 (else
p | 2), so ker(α^m−1) = p^f·R/qR (size p^{2f} = q); and
C ↦ (Tr C, Tr(αC)) = (2a, 6a+16b) is a bijection R/p^f → (Z/p^f)²
for odd p (2, 16 units). Hence the enumeration is bijective onto
kernel vectors. Verified numerically in all test components
(α^m ≡ 1 mod p^f, signature injective).

**Lemma T (τ fixed-point-free).** τ(C) = α^u C satisfies
α^u ≡ −1 mod p^f (constraining), so α^u−1 ≡ −2 is a unit (p odd);
τ(C) = C ⟹ C = 0. So block0 = block1 can only happen via a
β-orbit coincidence, never via a τ-fixed parameter.

**Lemma C (β-cycle ↔ β-orbit, p ≠ 3).** A cyclic sequence
s_{j+1} = 34 s_j − s_{j−1} of pairs comes from a unique β-orbit
(D^a, D^b): (Tr D, Tr(βD)) = (2a, 2(17a+24b)) determines (a, b)
since 48 is a unit mod p^f for p ≠ 2, 3. (For p = 3 use the
α-cycle version via (Tr, Tr∘α), which is valid for all odd p.)

**Reformulation.** Lemma U ⟺ ℘ admits no partition into two
β-cycle multisets other than {block0, block1} (blocks are exactly
β-cycle multisets by Lemma C). This is the precise obstruction:
abstract multisets recombine ({1,2}∪{2,3} = {1,3}∪{2,2}, wave 36),
so a proof must use trace structure, not combinatorics alone.

## 3. Exact verification

| case | points | ℘-groups | conflicts | max fiber |
|---|---|---|---|---|
| m=18, (25, 38809) | 970,225 | 27,445 | 0 | 36 |
| m=30, (625, 841) | 525,625 | 9,061 | 0 | 150 |
| m=30, (625, 72361) | 45,225,625 | ~757,117 | 0 so far (running) | — |

Group counts match wave-35/36 fiber counts exactly (27,445; 9,061),
validating the setup. Size histograms: m=30: {1:1, 6:4, 10:28,
20:28, 30:626, 60:8316, 120:56, 150:2}; m=18: {1:1, 6:4, 18:980,
36:26460}. At m=18 no fiber exceeds the dihedral maximum 2m = 36,
so that case is consistent with dihedral invariance alone and adds
no evidence beyond it. The genuine test is m=30: **58 groups exceed
60** (56 of size 120, 2 of size 150; 7,020 points), i.e. fibers
strictly larger than any dihedral orbit, and block pairs are
constant on all of them. Also: 327 m=30 groups have block0 = block1
(degenerate case, trivially fine); 4,945 groups have a repeated pair
in ℘ (non-distinct case covered).

## 4. Collision classification at m=30 (625, 841)

- **Bulk:** fibers of size ≤ 60, consistent with single dihedral
  orbits (8,316 of size exactly 60 = 2m).
- **Partial conjugations (56 groups):** each oversized group of size
  120 is a single orbit under G = ⟨rotations, partial conjugations
  J_a, J_b⟩. Concrete instance: C^a = (0,5) ∈ R/25,
  C^b = (1,2) vs (1,27) = (1,−2) ∈ R/29 — two points in distinct
  60-point dihedral orbits sharing ℘ and the identical block0
  ((0,10,15) × (2,7,10,14,25), a full Cartesian product; the
  product structure plus first-coordinate negation symmetry is the
  mechanism: a-traces are odd under k ↦ −k for pure-√2 C^a, and
  {0,10,15} is negation-invariant mod 25).
- **Scaling degeneracies (2 groups, size 150):** five G-orbits of
  size 30 each; representatives C^b = (0,0), C^a = (0,c),
  c ∈ {1,4,6,9,11}. Here C^b = 0 and C^a is pure-√2 torsion, so
  blocks are (4c·d_k, 0)-type multisets and the coefficient
  multiset {d_k} is invariant under scaling by the c-ratios
  (block0 first coordinates {0,2,3,5,7,8,10,12,13,15,17,18,20,22,23}
  are closed under ×4 mod 25); all 150 points share one block pair.

In every mechanism, blocks are preserved. No other collision type
occurs at m=30.

## 5. What remains for a full proof

Prove in general that ℘-collisions arise only from (i) dihedral
moves, (ii) partial conjugations at degenerate (torsion/product)
parameters, (iii) scaling degeneracies — and that blocks are
preserved in cases (ii)–(iii). Equivalently, rule out recombinant
β-cycle partitions (§2) using trace structure plus a torsion
analysis of the parameters. Until then, Lemma U stands as:
verified exactly at m=18 and m=30 (625, 841), with the m=30
collision classification complete; PAIR's remaining gap is exactly
this lemma. No Lean work was done (per brief); repository untouched.

## Files

- wave37_LemmaU_test.py (exact test; m30, m18, m30b cases)
- wave37_LemmaU_stats.py (fiber-size statistics)
- wave37_LemmaU_m30b.log (background (625, 72361) test, running)
