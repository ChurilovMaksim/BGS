# A sharp coefficient bound for balanced Laurent Jack polynomials

**Stable claim:** BGS-TRACE-067. **State:** PROVED.
**Boundary:** All alpha>0, nonzero balanced signatures and K>=1: ratio at most 1/(N+alpha K); unique sharp highest-root mode. External priority is not established.
**Integration and review:** [11 October disposition](../record/chat_integration_20261011.md).
**Original input:** [dated source](../evidence/executions/20261011/chat-research/original/jack_phase_2026_10_11/jack_coefficient_theorem.md).


## Statement and convention

Fix an integer \(N\ge2\) and a real \(\alpha>0\).
A signature is a weakly decreasing integer vector
\(\lambda=(\lambda_1,\ldots,\lambda_N)\).
Assume \(\lambda\ne0\) and \(\sum_i\lambda_i=0\).
Let \(P_\lambda^{(\alpha)}\) be the monic symmetric Laurent Jack polynomial,
triangular in symmetric monomials with respect to dominance. Here

\[
D_\alpha=\sum_i (z_i\partial_{z_i})^2+
\frac1\alpha\sum_{i<j}\frac{z_i+z_j}{z_i-z_j}
 (z_i\partial_{z_i}-z_j\partial_{z_j})
\]

and \(D_\alpha P_\lambda=E_\lambda P_\lambda\), where

\[
E_\lambda=\sum_i\lambda_i^2+
\frac1\alpha\sum_i(N+1-2i)\lambda_i.
\]

The ratio below is unchanged by the scalar normalization of \(P_\lambda\).
Set

\[
c_0=[z_1^0\cdots z_N^0]P_\lambda,\qquad
S=P_\lambda(1,\ldots,1),\qquad
K=\min(\lambda_1,-\lambda_N).
\]

Both endpoints are nonzero, and \(K\ge1\). Then

\[
\boxed{
0\le\frac{c_0}{S}
\le\frac{1}{1+\alpha E_\lambda/(2K)}
\le\frac{1}{N+\alpha K}
\le\frac{1}{N+\alpha}.
}
\tag{1}
\]

Equality in the final bound holds precisely for

\[
\lambda_*=(1,0,\ldots,0,-1).
\tag{2}
\]

The positivity and coefficient calculation below are direct. The standard
identification of this triangular eigenfunction with the Jack polynomial is
the only convention being used.

## 1. Nonnegative Laurent coefficients

Write \(D_i=z_i\partial_{z_i}\). For integers \(a>b\), put \(m=a-b\).
A finite geometric-series identity gives

\[
\frac{x+y}{x-y}(D_x-D_y)(x^ay^b+x^by^a)
=m\left(x^ay^b+x^by^a+
2\sum_{r=1}^{m-1}x^{a-r}y^{b+r}\right).
\tag{3}
\]

This identity remains valid for negative exponents. Each intermediate
exponent pair is dominated by \((a,b)\). After grouping monomials into
permutation orbits, (3) and the square-derivative term imply

\[
D_\alpha m_\mu
=E_\mu m_\mu+\sum_{\nu<\mu} b_{\mu\nu}m_\nu,
\qquad b_{\mu\nu}\ge0.
\tag{4}
\]

Here \(m_\mu\) is the sum of distinct monomials in the orbit of \(\mu\).
All signatures in (4) have the same total degree. Dominance confines their
coordinates to \([\mu_N,\mu_1]\), so this set is finite.

For \(\lambda>\nu\) at fixed total degree,
\(\sum_i\lambda_i^2>\sum_i\nu_i^2\): the square sum is strictly
Schur-convex on unequal sorted vectors. Also

\[
\sum_i(N+1-2i)(\lambda_i-\nu_i)
=2\sum_{j=1}^{N-1}\sum_{i=1}^j(\lambda_i-\nu_i)>0.
\]

The last strict inequality holds because all inner sums are nonnegative
and at least one is positive. Thus \(E_\lambda>E_\nu\).
If

\[
P_\lambda=m_\lambda+\sum_{\nu<\lambda}u_\nu m_\nu,
\]

the eigenvalue equation, solved downwards, expresses \(u_\nu\) as a
nonnegative already-computed numerator divided by \(E_\lambda-E_\nu>0\).
Consequently every individual Laurent monomial coefficient of \(P_\lambda\)
is nonnegative. In particular \(S>0\).

## 2. The constant coefficient equation

By symmetry, let \(c_k\) denote the coefficient of each individual monomial
\(z_i^kz_j^{-k}\), for \(i\ne j\) and \(k\ge1\).
It is crucial that \(c_k\) is a coefficient of an individual monomial, not of
the sum over all ordered pairs.

The square-derivative term has zero constant coefficient. The interaction
on a pair \(i,j\) changes only its two exponents. It can reach the all-zero
monomial only when all other exponents already vanish, and the two remaining
ones are \(k,-k\). In (3) the constant appears at \(r=k\), with coefficient
\(4k\), because \(a-b=2k\). There are \(\binom N2\) unordered pairs.
Therefore

\[
E_\lambda c_0
=\frac{2N(N-1)}{\alpha}\sum_{k\ge1} k c_k.
\tag{5}
\]

The signature of a root monomial is \((k,0,\ldots,0,-k)\).
Dominance by \(\lambda\) at the first and the penultimate partial sum
requires \(k\le\lambda_1\) and \(k\le-\lambda_N\).
Hence \(c_k=0\) for \(k>K\).

All coefficients are nonnegative. Evaluation at \(1^N\) therefore gives

\[
\begin{aligned}
S&\ge c_0+N(N-1)\sum_{k=1}^K c_k\\
&\ge c_0+\frac{N(N-1)}K\sum_{k=1}^K k c_k\\
&=c_0\left(1+\frac{\alpha E_\lambda}{2K}\right).
\end{aligned}
\tag{6}
\]

This proves the first upper bound in (1), including the case \(c_0=0\).

## 3. An energy lower bound

Let \(S_j=\sum_{i=1}^j\lambda_i\), so \(S_0=S_N=0\).
The differences \(S_j-S_{j-1}=\lambda_j\) are nonincreasing.
Thus \(S_j\) is a discrete concave sequence. On the interior indices
\(1,\ldots,N-1\), its minimum occurs at an endpoint, giving

\[
S_j\ge\min(S_1,S_{N-1})=K.
\]

This also covers \(N=2\), where there is just one interior index.
Since \(\lambda_1\ge K\) and \(-\lambda_N\ge K\),

\[
\sum_i\lambda_i^2\ge2K^2,\qquad
\sum_i(N+1-2i)\lambda_i=2\sum_{j=1}^{N-1}S_j
\ge2(N-1)K.
\]

Consequently

\[
E_\lambda\ge2K^2+\frac{2(N-1)K}{\alpha},
\qquad
1+\frac{\alpha E_\lambda}{2K}\ge N+\alpha K.
\tag{7}
\]

This proves the remaining inequalities in (1).

## 4. Sharpness and its unique mode

For \(\lambda_*\), the only dominated balanced signatures are
\(\lambda_*\) and \(0\). Equation (3) gives

\[
E_{\lambda_*}=2+\frac{2(N-1)}\alpha,\qquad
P_{\lambda_*}
=\sum_{i\ne j}\frac{z_i}{z_j}
+\frac{N(N-1)}{N-1+\alpha}.
\tag{8}
\]

Its normalized constant coefficient is exactly \(1/(N+\alpha)\).
Conversely equality in the final bound requires \(K=1\) and equality in
(7). Equality in the square-sum bound forces the two endpoints to be \(1,-1\)
and every other component to be zero. This is precisely (2).

## Status

This is a finite-dimensional algebraic proof for every \(\alpha>0\),
not a numerical extrapolation. An independent proof audit checked (3)–(8),
the coefficient multiplicities, strict energy ordering, and equality case.
Finite exact checks are recorded separately. Novelty has not been established.
