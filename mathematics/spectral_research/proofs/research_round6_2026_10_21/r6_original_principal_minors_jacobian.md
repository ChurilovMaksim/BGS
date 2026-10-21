> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round6_2026_10_21/r6_original_principal_minors_jacobian.md`. Embedded SHA256: `73ebb8fb57c706a6eedf2ca1c40dd65c1ceb35890d49e7027cd987d3b5dd01ec`.
> [Thematic guide](../../topics/algebra.md).

# Nonzero prefix minors and the exact leading coefficient of the phase Jacobian

21 October 2026. Independent algebraic verification by
`r6_original_obstruction`.

**Result.** Every leading principal minor of the prescribed $U_N$
is nonzero for every odd $N\ge3$. The Jacobian of its unsigned
characteristic-coefficient functions under independent diagonal
variables is a nonzero polynomial. Its leading coefficient is exactly
the product of those leading principal minors. For the signed
coefficients of $\det(\lambda I-\operatorname{diag}(z)U_N)$,
the extra overall sign is $(-1)^{N(N+1)/2}$.

## 1. Algebraic nonvanishing transfer through an exponential

We first prove a finite-dimensional lemma. Let $A$ be a Hermitian
matrix with algebraic entries, let $B$ have algebraic entries, and
let $\kappa\ne0$ be algebraic. For equal-size ordered index sets
$I,J$,
$$
\det B[I,J]\ne0
\quad\Longrightarrow\quad
\det(e^{\kappa A}B)[I,J]\ne0.
\tag{1.1}
$$

Fix their size $k$. On $\bigwedge^k\mathbb C^N$, let
$$
A^{[k]}(v_1\wedge\cdots\wedge v_k)
=\sum_{j=1}^k
v_1\wedge\cdots\wedge Av_j\wedge\cdots\wedge v_k.
$$
It is Hermitian with algebraic entries in the standard exterior basis.
Differentiation of the exterior product gives
$$
\bigwedge^k e^{sA}=e^{sA^{[k]}},
$$
because both entire matrix functions satisfy the same constant
coefficient differential equation and have initial value $I$.
Consequently
$$
\bigwedge^k(e^{\kappa A}B)
=e^{\kappa A^{[k]}}\bigwedge^k B.
\tag{1.2}
$$

Let $\Sigma$ be the set of **distinct** eigenvalues of
$A^{[k]}$. Its members are real algebraic numbers. Its spectral
projectors are the algebraic matrices
$$
\Pi_s=\prod_{u\in\Sigma\setminus\{s\}}
\frac{A^{[k]}-uI}{s-u}.
$$
Writing $e_I,e_J$ for standard exterior basis vectors, (1.2)
therefore gives
$$
\det(e^{\kappa A}B)[I,J]
=\sum_{s\in\Sigma}\beta_s e^{\kappa s},
\qquad
\beta_s=e_I^*\Pi_s(\bigwedge^k B)e_J
\in\overline{\mathbb Q}.
\tag{1.3}
$$
Equal sums of eigenvalues of $A$ have already been grouped into
the single eigenspace labelled by $s$; no independence assumption
about these sums is made. Since $\sum_s\Pi_s=I$,
$$
\sum_{s\in\Sigma}\beta_s=\det B[I,J]\ne0.
$$
Thus at least one coefficient survives. After zero coefficients are
removed, all remaining exponents $\kappa s$ are distinct
algebraic numbers, because $\kappa\ne0$.

The exact external theorem used here is the qualitative
Lindemann--Weierstrass statement in Cheng-Chao Huang, *Explicit Bounds
for Linear Forms in the Exponentials of Algebraic Numbers*, ISSAC 2022,
Theorem 1.1, DOI
[10.1145/3476446.3536170](https://doi.org/10.1145/3476446.3536170).
The [author PDF](https://arxiv.org/pdf/2112.05004), version 2,
page 1, was independently opened on 21 October 2026 and contains both
the publication metadata and the precise theorem. It asserts
nonvanishing of an algebraic linear combination of exponentials
when its exponents are distinct algebraic numbers and every retained
coefficient is nonzero algebraic. All these hypotheses have just
been checked for (1.3). This proves (1.1).

For the prescribed family, $A_N$ and $M_N$ have algebraic
entries: their Fourier coefficients use rational numbers, $i$,
and $(-3+4i)/5$; Weyl and Gaussian phases are roots of unity;
and $\sqrt N$ is algebraic. The matrix $A_N$ is Hermitian.
The exponent parameter is precisely the nonzero algebraic number
$\kappa=iN\tau=iN10^{-80}$. Thus (1.1) applies to the exact
$U_N=e^{iN\tau A_N}M_N$, without taking a small-parameter limit.

## 2. Prefix minors of the Gaussian matrix

Let $v=8^{-1}\pmod N$, and put
$$
d_x=e_N(-3v x^2),\qquad \xi=e_N(4^{-1}).
$$
The defining kernel factors exactly as
$$
(M_N)_{xy}=N^{-1/2}d_xd_y\xi^{xy}.
$$
For $I_k=\{0,1,\ldots,k-1\}$, $1\le k\le N$,
the Vandermonde determinant is
$$
\det M_N[I_k,I_k]
=N^{-k/2}\left(\prod_{x=0}^{k-1}d_x\right)^2
\prod_{0\le u<v<k}(\xi^v-\xi^u).
\tag{2.1}
$$
Here $\xi$ is a primitive $N$-th root of unity, since
$4$ is invertible modulo every odd $N$. Its first $k$
powers are distinct, so every factor in (2.1) is nonzero.
This argument does not assume that $N$ is prime.

Applying (1.1) to (2.1) gives
$$
\boxed{\quad
d_k:=\det U_N[I_k,I_k]\ne0
\quad(1\le k\le N),\quad
\text{for every odd }N\ge3.
\quad}
\tag{2.2}
$$
No claim that every principal minor of $M_N$ is nonzero is
needed. Prefix sets are the ones for which the displayed ordinary
Vandermonde formula applies.

## 3. Exact leading monomial of the coefficient Jacobian

The following is an elementary polynomial statement for any complex
matrix $U$, without unitarity. Write
$$
\det(\lambda I-\operatorname{diag}(z_0,\ldots,z_{N-1})U)
=\lambda^N+\sum_{k=1}^N(-1)^k\sigma_k(z)\lambda^{N-k},
$$
where determinant expansion gives
$$
\sigma_k(z)=\sum_{\substack{I\subset\{0,\ldots,N-1\}\\|I|=k}}
\det U[I,I]\prod_{j\in I}z_j.
\tag{3.1}
$$
Assume $d_k=\det U[I_k,I_k]\ne0$ for all $k$, and use
lexicographic monomial order $z_0>z_1>\cdots>z_{N-1}$.
Then the largest monomial of $\sigma_k$ is
$$
m_k=z_0z_1\cdots z_{k-1},
\qquad [m_k]\sigma_k=d_k.
$$

Let
$$
\mathcal J(z)=\det[\partial_{z_j}\sigma_k(z)]_
{1\le k\le N,\ 0\le j<N}.
$$
Consider instead the logarithmic derivative matrix
$L_{kj}=z_j\partial_{z_j}\sigma_k$. Every monomial in row
$k$ is at most $m_k$ in the stated order. Its coefficient
at $m_k$ in column $j$ is
$$
d_k\mathbf1_{\{j<k\}}.
$$
Multiplicativity of the monomial order shows that every determinant
term of $\det L$ is at most
$M=\prod_{k=1}^N m_k$. A term can attain $M$ only if the
chosen monomial in **every** row is $m_k$: replacing any one
row monomial by a smaller one, with the other rows still no larger
than their respective maxima, strictly decreases the product.

It follows that the coefficient of $M$ is exactly
$$
[M]\det L
=\left(\prod_{k=1}^N d_k\right)
\det[\mathbf1_{\{j<k\}}]_
{1\le k\le N,\ 0\le j<N}
=\prod_{k=1}^N d_k.
\tag{3.2}
$$
The last matrix is lower triangular with diagonal entries one.
Equivalently, its only allowed permutation is $j=k-1$ for
every row. Thus no cancellation of the leading term is possible.

Each column of $L$ has the factor $z_j$, so
$\det L=(\prod_jz_j)\mathcal J(z)$. Since
$M=z_0^Nz_1^{N-1}\cdots z_{N-1}$, (3.2) proves
$$
\boxed{\quad
\operatorname{LT}_{\rm lex}\mathcal J(z)
=\left(\prod_{k=1}^N d_k\right)
z_0^{N-1}z_1^{N-2}\cdots z_{N-2},
\qquad\mathcal J\not\equiv0.
\quad}
\tag{3.3}
$$
The empty monomial is understood when $N=1$.

If the coordinate functions are instead the actual coefficients
$c_k=(-1)^k\sigma_k$ of the characteristic polynomial, their
Jacobian is
$$
\det[\partial_{z_j}c_k]
=(-1)^{1+2+\cdots+N}\mathcal J(z)
=(-1)^{N(N+1)/2}\mathcal J(z).
\tag{3.4}
$$
This is the only sign adjustment for the displayed row order and
column order. Reversing either order would of course introduce its
own permutation sign.

Applying (3.3)--(3.4) with (2.2) establishes the requested nonzero
Jacobian for every member of the prescribed family. These are exact
algebraic nondegeneracy results. They supply no quantitative lower
bound uniform in $N$, no original-phase simplicity assertion,
and no estimate of the unresolved spectral correlation functional.
