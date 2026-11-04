# Self-referee

Read against the proofs in this directory, not against the hope that H1 would fall.

## Caught and corrected before this text was frozen

The first draft of the Prop. F disjointness said that the whole neighbourhood U_n is a bad-set complement. That is wrong. The digit word trims leading and trailing zeros, and the edge a = 0 of U_n is a quiet tail with no letter on the right. The corrected statement restricts to the outer quarter U_n^†, where both coefficients are bounded below and the zero block on [2, 2n] is internal. The integral lower bound loses a factor 4 and remains a positive multiple of λ^{−n}. The i.i.d. comparison in Prop. F still outgrows that multiple.

## What was checked by a second implementation

- Integer floor of U + V√2 against mpmath at 80 decimals, 200 samples, including negative forms.
- Carries n_k against an independent mpmath red, 40 random lattice points, k from −12 to 15.
- The fundamental domain through shell 12 reproduces `a_enum.jsonl` exactly (5109 classes).
- Exact span and exact internal zero-run equal the stored `span` and `zr` on all 5109 classes.
- The bound span ≤ ⌊log_ε(|N|/2)⌋ + 3 holds on those classes and on the re-enumeration through shell 16 (40 845 classes at j = 16). Equality is attained.
- The published crossover inputs 3.4962×10^{-4} and 7.4115×10^{-6} reproduce the primes 3307 and 1409.

## Places the argument is thinner than the tag

1. **Background renormalisation.** The sharp S_0 is computed from the bare certified |w|. Prop. K and lineN22 require the model-renormalised activities. A factor 1.01 moves 3067 to 3109. The note records that and does not absorb it into the tag [P].

2. **The 1.02 iteration in N20.** The published weight a = 2.6925×10^{-3} sits above the fixed point of the Kotecký–Preiss map; the left-hand side at that weight is about 2.640×10^{-3}. Comparing 3067 with 3307 without splitting the solver from the span overstates the gain by the eight primes from 3299 to 3307. The note splits them.

3. **Stored words.** On 2182 of 5109 classes the integer `word` in `a_enum.jsonl` differs from the exact letter. The span and the zero-run, which are what the finite bad set uses, agree. Anyone who treats those stored integers as digits is reading a truncated float. This note does not reopen Thm A.

4. **Uniform-norm obstruction.** N_max^{2s(j)} above the shell budget shows that this estimate cannot prove H1. It is compatible with the certified sums through j = 14, which are small. Using it as evidence against H1 would be an inversion of an upper bound.

5. **Exit time in the disjointness proof.** The index 2n+11 is proved from ε^2 > 5 and δ > 1.6×10^{-3}. It is not claimed to be the first possible exit. The Prop. F constants δ, Lip_H, and N_H that feed |r| ≥ 0.502 are cited, not recomputed.

6. **Crossover arithmetic.** The prime column is float gas versus exact K_p, the v5 standard, with additive budgets set to zero. It is not an interval proof of B_p > 0. Shell 16 is the end of the span census; the span theorem for larger shells is the analytic argument, and the census does not extend it.

7. **H1-ali, H5, H6, H7*, H8.** Untouched. A span bound does not compare near-collisions, does not control composite h_p, and does not bound included levels below L_fl.

## What this note does not say

H1 is open. H3 is open. Frozen R′ is open. BGS-BGS-001 is open. The conditional theorem R♯-mod v5 is still conditional. The idealised prime 3067 is a consequence of H1 at C ≤ 0.082 together with the proved length, inside the same idealisation as 3307, and it is fragile.
