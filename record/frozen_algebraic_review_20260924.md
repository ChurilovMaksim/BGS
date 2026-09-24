# Algebraic spectrum audit — `BGS-FM-008`

**Verdict:** project proof with exact external theorem input and
author-level review; no quantitative spectral-gap inference.
See [`frozen_algebraic_spectral_simplicity.md`](../mathematics/frozen_algebraic_spectral_simplicity.md)
for the exact statement and
[`submitted_article_review_20260924.md`](submitted_article_review_20260924.md)
for the submitted PDF's hash and original locators §§2.5, 3.1–3.5.

The key proof contract is $N$ odd with $7\nmid N$. The Jacobi generator
has one path and simple spectrum. At the Gaussian prime $1+2i$, check
$v(-3+4i)=2$, $v(-3-4i)=0$ and $0\le v(r_j)\le1/2$. The diagonal similarity
has strictly increasing valuation weights; the scaled Jacobi matrix
reduces to one nilpotent Jordan block. Generalized Fourier minors all
have valuation at least the consecutive-row-and-column minor via
balanced residue counts at each $5$-power quotient. This unique extremal
minor survives contraction with normalized left/right eigenvector
wedges. These are the all-order steps; enumeration of row subsets is
only a regression.

The external implication is exactly [Popescu (2023), arXiv:2306.14352v2,
Theorem 3.2](https://arxiv.org/pdf/2306.14352): distinct algebraic
exponents give linearly independent exponentials **over algebraic
coefficients**. It applies to $it a_j$ at nonzero algebraic $t$ after
collecting equal exponent sums. The large imaginary-time witness
$e^{sA_N}M_N$ is used solely to show that each discriminant/resultant
exponential polynomial is not identically zero. It is not an
analytic-continuation approximation at the physical $t=\tau N$.

The original `verify_v2.py` replay passed and matched the submitted JSON
byte for byte. The maintained adaptation
`computations/verification/frozen_total_minors.py` checks finite
5-adic Fourier valuations and balanced-weight combinatorics, with
result `evidence/20260924/frozen_total_minors.json`.
Numerical eigenbasis checks for $N=3,5,9,11,15$ are secondary and do
not establish nonvanishing for arbitrary $N$.

No assertion is made when $7\mid N$, including $N=7$ where $A_7$
is scalar. Nonzero minors, transcendental eigenvalue ratios and simple
powers do not rule out extremely close eigenphases or determine CUE.
