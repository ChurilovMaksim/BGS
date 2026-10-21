> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/root_reconnection_permutation_computation_note.md`. Embedded SHA256: `b3569fd1fc3a81c7f9b9ebe2087ff45896958b7a9ca4c576e3be5afc94cac6ad`.
> [Thematic guide](../../topics/histories.md).

# Exact finite reconnection counts: computation and correction

Date: 2026-10-21. This is a finite calculation, not a spectral limit.

Let gamma=(1 2 ... r). For each r-cycle sigma satisfying sigma(i)!=gamma(i)
for every i, count the cycles of pi=sigma^{-1} gamma. The exact counts are:

| r | Cycle count c : number of permutations | Total |
|---|---|---|
| 3 | 1 : 1 | 1 |
| 4 | 2 : 1 | 1 |
| 5 | 1 : 8 | 8 |
| 6 | 2 : 36 | 36 |
| 7 | 1 : 180; 3 : 49 | 229 |
| 8 | 2 : 1604; 4 : 21 | 1625 |
| 9 | 1 : 8064; 3 : 5144 | 13208 |

The Wolfram Language code in the accompanying source was executed in a
Wolfram kernel. An independent Python enumeration reconstructs the
successor permutation and counts all its cycles by traversing them.
Both agree with the table and the inclusion-exclusion total below.

An initial Wolfram expression `Thread[s != g]` was rejected after it
produced impossible r=4 counts: list inequality had already evaluated
as a single comparison of entire lists. The executed corrected code
uses `MapThread[Unequal, {s, g}]`, which tests each port separately.
No result of the initial expression is used in a theorem.

For completeness the total count has the elementary exact formula

$$
 q_r=\sum_{j=0}^{r-1}(-1)^j\binom rj(r-j-1)!+(-1)^r.
$$

To prove it, apply inclusion-exclusion to the forbidden directed edges
i->gamma(i). Any chosen proper subset of j such edges consists of
directed paths in the original cycle. Contracting these edges leaves
r-j labelled blocks, whose cyclic order can be chosen in
(r-j-1)! ways. If all r edges are prescribed, exactly the original
cycle remains, giving the last term. This proves the total for every
r>=2 without extrapolating from the table.

The parity check r-c(pi) even follows because both gamma and sigma
have sign (-1)^(r-1), so their quotient is even. The table's refined
cycle counts are finite computations only; no general closed formula
for them is needed for the growing-order cancellation theorem.
