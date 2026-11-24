# Effective separation of noncoincident eigenvalues

**Registry:** BGS-TRACE-361.

**Scope.** These results concern the original fixed-kick propagator at
every odd dimension. The constants are effective but do not give
microscopic control; exact coincidences are explicitly allowed.

Write the distinct eigenvalues as $\lambda_j$, with multiplicities
$d_j$. For $R=N^3\log(10N)$ and $B_N=\exp(\exp(20R))$ the
[original proof](BGS_Effective_Gaps.tex), §§1–4, gives
$$
|\lambda_i-\lambda_j|\ge e^{-B_N}\quad (i\ne j).
$$
The input is a nonzero moment determinant of size equal to the number
of distinct eigenvalues. Its factorization is
$\det H=(\prod_jd_j)(\prod_{i<j}(\lambda_i-\lambda_j)^2)$.
Expand the kick using the algebraic spectral projectors of $4000A_N$,
clear denominators, and use the integral trace pairing to express the
exponents in a rationally independent basis. Then apply Sert's effective
Lindemann–Weierstrass bound in
[Huang, Theorem 5.1](https://arxiv.org/pdf/2112.05004). Bounds on field
degree, coefficient height and discriminant are given in the source;
the remaining chordal distances are at most 2. This is an analytic
number-theory argument, not a statement covered by finite interval tests.

In particular, for any integer window start $a$ and length $T\ge1$,
$$
\left|\frac1{TN}\sum_{m=a+1}^{a+T}|\operatorname{Tr}U_N^m|^2
       -\frac1N\sum_jd_j^2\right|
   \le 2N e^{B_N}/T .
$$
This extends the time-first [multiplicity bound](../exact_splitting/README.md)
to joint limits with $T_N/(Ne^{B_N})\to\infty$, uniformly in the window
start. It is not a bound usable in windows of length comparable to $N$.

## Finite certificate at N = 49

For six explicit doublets whose first-order compression is scalar,
§§5–6 compute enclosures for the second-order coefficient and bound the
remainder of the Schur complement in norm. Thus the stated intervals
contain the gaps of the **full** unitaries, not just the compression.
For example, for the node `(ell,h) = (4,0)` the angular gap in radians
is in $t_0^2[0.00170645,0.00170648]$, where $t_0=49\cdot10^{-80}$.
The directed rational interval checker,
`python effective_gaps/check_intervals.py --verify` from the central
checker directory, was rerun and reproduced the six enclosures.

[Original source](BGS_Effective_Gaps.tex) ·
[central checker](../../../../computations/verification/bgs_f_november/).
