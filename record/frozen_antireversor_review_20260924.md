# Common antiunitary obstruction audit — `BGS-FM-009`

**Verdict:** exact certificate-backed project proof, internally checked;
no formal proof kernel or independent referee. The statement is
[`frozen_common_antireversor_certificate.md`](../mathematics/frozen_common_antireversor_certificate.md),
and the original PDF identity is pinned in
[`submitted_article_review_20260924.md`](submitted_article_review_20260924.md).

The necessary condition is derived from $M=M^{\mathsf T}$,
$\overline M=M^{-1}$, $A^*=A$, and similarity of $[A,M]$ to
$-[A,M]^{\mathsf T}$ under a common reversor; its odd trace must vanish.
The Weyl mixed-trace formulas used for the converse obstruction were
recomputed numerically from the **raw** $A_N,M_N$ for
$N=3,5,7,9,15,21,25,35$; the maximum discrepancy with the
Laurent-polynomial formula was below $5\cdot10^{-16}$.

`computations/verification/frozen_antireversor.py` derives the two
integer Laurent polynomials from 32 symbol modes, bounds **all** relevant
odd cyclotomic orders by totients, screens 2415+57 eligible orders over
$\mathbb F_2$, then performs the exact integer remainder check for
order 3. The regenerated
`evidence/20260924/antireversor/{certificate_polynomial.csv,
certificate_polynomial_7.csv,certificate_result.json}` matched the PDF's
three attachments byte for byte before the checker header was updated.
The mathematical explanation of completeness, not the count of tested
orders alone, is in the maintained proof.

**Exception and domain:** $N=7$ is explicit; for other odd $N$, no
antiunitary whatsoever reverses the pair $(A_N,M_N)$ in the stated
common sense. The corollary concerning the *single* $U_N$ assumes
algebraic matrix entries and uses the source-checked
Lindemann–Weierstrass theorem. All finite-dimensional unitary matrices
have some eigenbasis antiunitary reversor; do not strengthen the
corollary. None of these nonvanishing claims bounds near-resonances.
