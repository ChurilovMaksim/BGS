# Wave 39, task 2 — Lemma U, scaling-degeneracy mechanism: PROVED under H2'

## Verdict

The scaling mechanism is **proved under a stated saturation hypothesis
H2'**, and the unconditional version is **false**: (m, p, f) = (42, 13, 2)
is the exact dividing line. There β⁷ ≡ 1 mod 169 (the order does not
grow on lifting), the B-sequence takes only 7 values, and scaling by
λ ≡ ±1 mod 13 with λ ≢ ±1 mod 169 genuinely changes block0. So where
H2' fails, scaling does not even create ℘-collisions (except the
trivial sign): the mechanism is conditional, not universal. Mechanism
(ii) (partial conjugations, wave 38) and (iii) (this note) are now
both proved in their natural generality; the "only three mechanisms"
classification and dihedral moves (i, definitional) remain.

## Setup (waves 36–38)

m = 2u, u odd, q = p^{2f} constraining (α^u ≡ −1 mod p^f, p odd),
β = α², so β^u ≡ 1 mod p^f. Parameters C^a, C^b ∈ R/p^f (R = Z[√2]).
block0 = {(Tr(C^a β^k), Tr(C^b β^k)) : k ∈ Z/u}, block1 = −block0.

## Lemmas

**Lemma 1 (trace form).** For pure-√2 C = c√2, writing
β^k = A_k + B_k√2, Tr(C β^k) = 4cB_k: indeed
C β^k = 2cB_k + cA_k√2 and Tr(x + y√2) = 2x.

**Lemma 2 (negation).** B_{−k} = −B_k, since β̄ = β^{−1} (N(β) = 1):
B_{−k} = (β^{−k} − β^k)/(2√2) = −B_k. As k ↦ −k permutes Z/u,
the multiset {B_k} is negation-invariant; hence any fiber
multiplicity satisfies μ(−r) = μ(r).

**Hypothesis H2' (saturation).** The multiset {B_k : k ∈ Z/u} is a
union of full mod-p fibers, each internally uniform: there is
S ⊆ Z/p and multiplicities μ(r) with μ(−r) = μ(r) (automatic by
Lemma 2) such that every x ∈ Z/p^f with x mod p ∈ S occurs exactly
μ(x mod p) times, and no other value occurs. (f = 1 always satisfies
H2' trivially: each fiber has a single lift.)

## Theorem (scaling invariance under H2')

Assume H2'. Let C^a, C^b both be pure-√2 (0 allowed). Then scaling
both by any unit λ ∈ (Z/p^f)× with λ ≡ ε mod p, ε ∈ {+1, −1},
preserves block0 and block1 individually, hence the unordered block
pair and ℘.

**Proof.** By Lemma 1, block0 is the image of the multiset {B_k}
under the fixed Z-linear map φ(x) = (4c_a x, 4c_b x). Scaling the
parameters by λ sends block0 to λ·block0 (componentwise, by
Z-linearity of Tr), and λ·φ(x) = φ(λx). So it suffices that
{B_k} is λ-invariant. Now λ is a bijection of Z/p^f mapping the
fiber over r bijectively onto the fiber over εr (λx mod p = εr iff
x mod p = r), and H2' gives equal multiplicities μ(εr) = μ(r).
Thus {λB_k} = {B_k}, so λ·block0 = block0, and block1 = −block0
is preserved since λ commutes with negation. ∎

**Corollary (collapse).** For units c₁, c₂ with c₁ ≡ ±c₂ mod p,
(c₁√2, 0) and (c₂√2, 0) have identical block pairs: scaling by
λ = c₁/c₂ ≡ ±1 mod p sends one parameter to the other and
preserves blocks by the Theorem. More sharply, the scaling group is
exactly the stabilizer of S in (Z/p)× lifted to ±1 mod p: any λ
with λ ≢ ±1 mod p moves S and breaks block0 (λ = 2 at m = 30
verified to fail).

**Remark (trivial sign).** c ↦ −c always preserves block0, with no
hypothesis: block0(−c) = −block0(c) = block0(c) by Lemma 2. This is
the reflection part of the dihedral action, not a scaling degeneracy.

## Verification (exact integer arithmetic)

**m = 30, component 25 (the wave-37 scaling group).** B_k mod 25 =
[0,12,8,10,7,3,20,2,23,5,22,18,15,17,13]: saturated, S = {0,2,3},
μ = 1 (all 5 lifts of each class, once). All 10 units c ≡ ±1 mod 5
give the identical block pair (block0 = block1, 15 distinct first
coordinates); the 10 values pair into 5 G-orbits (c, −c) of size
30 (rotation orbit 15 × conjugation), recovering exactly the 150
wave-37 points. λ = 4 scales block0(c=1) to block0(c=4); λ = 2 fails.

**Sweep.** All constraining (m, p, f) with m ≤ 60, p ≤ 200 odd,
p^f ≤ 10⁵: 24 components, **23 pass H2'**, one fails:
m=12: 3, 3², 11; m=18: 5, 197; m=24: 17; m=30: 5, 5², 29;
m=36: 3, 3², 3³, 11, 73, 179; m=42: 5, 13 (13² FAILS); m=48: 97;
m=60: 3, 3², 11, 19, 59 (exponents are f; f = 1 cases trivial).

**The dividing line (42, 13, 2).** β has order 7 mod 13 and already
β⁷ ≡ 1 mod 169, so the order does not grow on lifting: B_k takes
only 7 values, each 3 times (u = 21), one lift per mod-13 class
instead of 13. Direct check: block0(c=12) ≠ block0(c=1) although
12 ≡ −1 mod 13, and block0(c=14) ≠ block0(c=1) although
14 ≡ 1 mod 13; only c ≡ ±1 mod 169 coincide. Since block0(c) is
negation-invariant, ℘(c) = 2·block0(c), so distinct c-classes do
not even collide here — the scaling mechanism is absent, not
block-breaking. This refutes the unconditional scaling claim and
shows H2' is the operative condition.

## What remains

Prove H2' in general, i.e. an LTE-type lift-sweeping lemma: when the
order of β grows by p on lifting (β^d ≡ 1 mod p but ≢ 1 mod p² in
the appropriate sense), the B-sequence fills each mod-p fiber
uniformly; when it does not grow (as at (42, 13, 2)), saturation
fails and there is no scaling degeneracy to prove. The full
"collisions arise only from (i)–(iii)" classification is still open.

## Files

- wave39_LemmaU_scaling_check.py (all checks above; sweep + m=30 group)
- No Lean work was done (per brief); repository untouched.
