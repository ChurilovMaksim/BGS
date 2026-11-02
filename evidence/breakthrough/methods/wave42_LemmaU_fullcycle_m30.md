# Wave 42, task 2 (retry) — Lemma U at m=30: full-cycle rigidity, proved

Verdict: every ℘-collision at m=30 is dihedral, partial conjugation, or
scaling degeneracy. The proof uses the full cycle (periods + fibers), not
one-step branching: one-step induction failed because H4 is empty (wave 41);
the full cycle at m=30 has only 15 steps and a rigid period structure.

## 1. Period rigidity (exact)

β = 17+12√2 (Tr β = 34), α = 3+2√2, α¹⁵ ≡ −1 mod 25 and mod 29 (checked),
so block1 = −block0 and ℘ = block0 ∪ (−block0).
Mod 25: β¹⁵ = 1; β−1 has norm −32 ≡ 18, a unit; β³−1 = 10√2;
β⁵−1 = 11+3√2 has norm 3, a unit. Hence for C^a ∈ R/25: period 1 ⟺ C^a = 0;
period | 3 ⟺ C^a ∈ 5R/25 (10a ≡ 20b ≡ 0 mod 25 ⟺ 5 | a, b); period 5 is
impossible unless C^a = 0. So T_a ∈ {1,3,15}.
Mod 29: β⁵ = 1; β³−1 has norm 8, β−1 has norm −32 ≡ 26, both units. Hence
T_b ∈ {1,5}: T_b = 1 ⟺ C^b = 0, else T_b = 5.
Cases: (15,5), (3,5), (1,5), (15,1), (3,1), (1,1).

## 2. Three full-cycle lemmas (exact, whole parameter spaces)

L1 (29-side): for every C^b ∈ R/29, any β-cycle with values in {±s}
(s = trace cycle of C^b) is dihedral to C^b or −C^b. Checked over all 841
parameters: 0 exceptions. In particular no mixed b-cycle exists.
L2 (25-side fibers): for generic C^a (nonzero, ∉ 5R), write
T_j = {t_j, t_{j+5}, t_{j+10}} (j mod 5). If a cycle x has fiber multisets
{F_j(x)} = {T_j}, then x is dihedral to C^a. Checked over all generic C^a:
0 exceptions. (Point: (Tr, Tr∘β⁵, Tr∘β¹⁰) determines C^a, since the forms
2a and 24a+12b are independent mod 25.)
L3 (25-side single): no genuine single-component recombination at 25: if
M(x) ∪ M(y) = M(t) ∪ M(−t) for β-cycles x, y, then
{M(x), M(y)} = {M(t), M(−t)}. Checked over all 625 parameters: 0 genuine
recombinations. (Reorderings, e.g. C^a = √2 vs 1+2√2 with identical value
multisets, give identical blocks, not conflicts.)

## 3. Assembly

(1,5): ℘ has a-coordinates all 0; recombinants are (0, X_b) with
M(X_b) ∪ M(Y_b) = {s} ∪ {−s}; by L1, X = block0 or block1. (1,1) trivial.
(15,1), (3,1): symmetric by L3; scaling parameters (C^b = 0, C^a = c√2)
preserve the block multiset itself (coefficient-multiset invariance,
waves 39–40), so they are not conflicts.
(3,5): C^a ∈ 5R, so t has period 3; since 5 ≡ 2 mod 3, t_{j+5ℓ}
(ℓ = 0,1,2) runs over all residues mod 3, so block0 =
⊔_j {s_j} × {t_0,t_1,t_2} is a Cartesian product. By the wave-38 product
theorem, conjugating either component preserves blocks: these are exactly
the (ii) groups. L1 + L3 exclude any other recombination.
(15,5) generic: X, Y partition ℘. By L1, M(X_b), M(Y_b) are M(s), M(−s) in
some order; say X_b is a rotation/reflection of s. X's pairs with second
coordinate s_j are a fiber triple of x, and lie in ℘, whose pairs with
second coordinate s_j are T_j (generic: s negation-free, fibers distinct).
Hence {F_j(x)} = {T_j}, so by L2 x is dihedral to t. Alignment:
X_k = (ε t_{σk+r}, s_{τk+c}); the pair condition forces σ = τ, r ≡ c
mod 5, matching signs (generic distinctness); the residual 5-shift permutes
within fibers, so X's pair multiset = block0's (resp. block1's). Hence
X ∈ {block0, block1}.
Degenerate locus in (15,5) (value coincidences, negation coincidences
s_j = −s_{j′}, fiber collisions): the generic alignment weakens, but the
locus is exactly where parameters have extra symmetry (real / pure-√2 /
torsion) or product structure; there the proved product theorem (wave 38)
and scaling theorem (waves 39–40) apply, and the exact m=30 census
(wave 37, reproduced wave 41: 9,061 groups — 8,975 dihedral-only, 84
partial-conjugation, 2 scaling, 0 conflicts) confirms no further type.

## 4. Conclusion

Lemma U holds at m=30: ℘ determines the unordered block pair. The remaining
gap for general m is a full-cycle rigidity argument without the rigid period
structure (T | 15, β⁵ = 1 mod 29) used here. No Lean built, repo untouched.
Scripts: wave42_fullcycle_checks.py, wave42_fullcycle_check3c.py.
