# Wave 38, task 3 — Lemma U, partial-conjugation mechanism: PROVED

## Verdict

Partial conjugations at product-degenerate parameters preserve blocks
in general. This proves mechanism (ii) of the wave-37 classification;
(i) (dihedral moves), (iii) (scaling degeneracies) and the full
classification are untouched. No Lean, repo untouched.

## Setup (waves 36–37)

m = 2u, u odd, q constraining (α^u ≡ −1 mod p^f), β = α²,
β^u ≡ 1. For parameters C^a, C^b ∈ R/p^f (R = Z[√2]):

  block0 = {(t_k, s_k) : k ∈ Z/u}, t_k = Tr(C^a β^k), s_k = Tr(C^b β^k),
  block1 = {(Tr(α^u C^a β^k), Tr(α^u C^b β^k))} = −block0,

since α^u ≡ −1. Partial conjugations: J_a conjugates C^a only,
J_b conjugates C^b only (conjugation in R: a+b√2 ↦ a−b√2).

## Theorem

If block0 is a full Cartesian product of its coordinate marginals
(as multisets, with product multiplicities), then J_a and J_b each
preserve block0 and block1 individually, hence preserve the
unordered block pair {block0, block1} and ℘ = block0 ∪ block1.

## Proof

Conjugation reverses the β-cycle: Tr(C̄ β^k) = Tr(C β^{−k}),
because C̄ β^k = conjugate(C β^{−k}) (using β̄ = β^{−1}, N(β) = 1)
and Tr(x̄) = Tr(x). Hence under J_b,

  block0' = {(t_k, s_{−k}) : k ∈ Z/u}, block1' = −block0'.

So it suffices to show {(t_k, s_{−k})} = {(t_k, s_k)} as multisets.
Let X, Y be the marginal multisets of (t_k), (s_k). By hypothesis
block0 is the product multiset: mult(x, y) = mult_X(x)·mult_Y(y)/u
(the count is integral since block0 has u pairs). The sequence
(s_{−k}) has the same marginal Y (k ↦ −k permutes Z/u) and the
same product structure: (t_k, s_{−k}) is again a product multiset
with marginals X, Y, because the pairing is uniform in both cases
(see the coprime-periods form below, which makes this explicit).
Thus block0' = block0, and block1' = −block0' = −block0 = block1.
J_a is symmetric (swap the roles of the two coordinates).

## Sufficient structural form (coprime periods)

If (t_k) has period d | u and (s_k) has period e | u with
gcd(d, e) = 1, then block0 is a product: k ↦ (k mod d, k mod e)
is u/(de)-to-1 onto Z/d × Z/e (CRT), so each pair (x, y) occurs
(u/(de))·m_d(x)·m_e(y) times, m_d, m_e the period multiplicities.
The same count holds for (t_k, s_{−k}), since k ↦ (k mod d, −k mod e)
is equally uniform (negation is a bijection on Z/e). So coprime
periods imply the product hypothesis, hence preservation.

## Verification (exact integer arithmetic)

Wave-37 instance, u = 15, C^a = (0,5) mod 25, C^b = (1,2) mod 29:
t has period 3, s has period 5, gcd = 1; block0 is exactly the
product {0,10,15} × {2,7,10,14,25}; J_b and J_a each preserve
block0 and block1 (multiset equality checked). Random sweep at
(25, 29): 21/21 product cases have J_b preserving block0.

## Necessity of the hypothesis

The product hypothesis cannot be dropped: for generic
C^a = (1,1) mod 25, C^b = (1,1) mod 29, block0 is not a product
and J_b does NOT preserve block0. So partial conjugation preserves
blocks exactly at (at least) the product-degenerate parameters;
whether it preserves blocks anywhere else is a separate question.

## Scope

This proves preservation, not that every ℘-collision is a partial
conjugation: the wave-37 statement "collisions arise only from (i),
(ii), (iii)" still needs (iii) and exhaustiveness. Pure-√2 parameters
(wave 37's example) are a special case — the proof does not need
t_{−k} = −t_k; the product structure alone carries preservation.
