> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round7_2026_10_21/root_original_every_power_minors.md`. Embedded SHA256: `9d3503703b5a5b0df580bb1a2a42e58a0617c7de94c3b340ac26d9ec93d54a48`.
> [Thematic guide](../../topics/algebra.md).

# Every physical minor of every nonzero power at the exact algebraic parameter

21 October 2026. This is a finite-dimensional theorem for the
original family in every odd dimension $N\ge3$ with $7\nmid N$.
It strengthens the previously proved leading-principal-minor
statements to all physical row and column sets and all nonzero
integer powers. The argument was independently reconstructed
by the researcher responsible for the Jacobi proof.

It provides exact nonvanishing and a support uncertainty inequality.
It does not provide lower bounds for the nonzero minors or the
signed trace estimates of $H_{\rm diag}$.

## 1. The theorem

Let
$$
U_N(z)=e^{izNA_N}M_N,
$$
with precisely the matrices in the question. If $z\ne0$ is an
algebraic complex number and $r\in\mathbb Z\setminus\{0\}$, then
$$
\boxed{\quad
\det\bigl(U_N(z)^r[I,J]\bigr)\ne0
\quad\text{for every }I,J\subset\mathbb Z/N\mathbb Z,\quad
1\le |I|=|J|\le N.
\quad}
\tag{1.1}
$$
In particular, this holds for the original $z=\tau=10^{-80}$.
The row and column sets are physical coordinate sets, not sets
of $A_N$-eigenvectors.

Consequently, for every nonzero $v\in\mathbb C^N$,
$$
\boxed{\quad
|\operatorname{supp}v|
+|\operatorname{supp}(U_N(z)^r v)|\ge N+1.
\quad}
\tag{1.2}
$$
The inequality is sharp as a statement about supports: for any
two prescribed sets of sizes summing to $N+1$, there is a
vector attaining precisely those input and output supports.

## 2. The exact Jacobi inputs

Let $h=(N+1)/2$, $x_j=h+j\pmod N$,
$\omega=(-3+4i)/5$, $P e_j=e_{x_j}$, and
$D=\operatorname{diag}(\omega^j)$. The direct modular-half
calculation gives the real symmetric Jacobi path
$$
L=200D^{-1}P^*A_NPD.
$$
Its internal edges are $b_j=r((j+1)/N)>0$, $0\le j<N-1$.
Here $7\nmid N$ is essential to connectedness.

Choose real algebraic eigenvectors $\Phi$ of $L$, and a
positive algebraic diagonal normalization $R_0$, so that
$$
Q=PD\Phi R_0
$$
is unitary and diagonalizes $A_N$. Order its eigenvalues as
$a_1>\cdots>a_N$. At a valuation over $1+2i$, normalized
by $v(5)=1$, one has $v(\omega)=1$, and for every
$k$-element eigenvector set $E$,
$$
\det\Phi_{S_0,E}\ne0,\qquad
v\!\left(\frac{\det\Phi_{S,E}}
                 {\det\Phi_{S_0,E}}\right)
\ge-\frac12\left(\sum S_0-\sum S\right),
\quad S_0=\{N-k,\ldots,N-1\}.
\tag{2.1}
$$

These statements, including arbitrary powers of 5 in $N$,
are proved in the included round-2 source
arithmetic_padic_jacobi_simplicity.md, SHA256
f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df.
Their derivation is reproduced in the current
root_original_intensity_at_prescribed_phase.md, Section 2:
the endpoint-normalized eigenvector entries are monic Jacobi
polynomials divided by products of edges with valuation in
$[0,1/2]$; their alternants divided by the eigenvalue
Vandermonde are integral; using the recurrence from the other
endpoint yields (2.1).

The same round-2 proof also gives
$$
b_k^0:=\det(Q^*M_NQ)_{E_k,E_k}\ne0,
\qquad E_k=\{1,\ldots,k\}.
\tag{2.2}
$$
Its double Cauchy--Binet expansion has a unique smallest
valuation term with the last $k$ coordinate rows and first
$k$ coordinate columns. The relative valuation of every
other nonzero term is at least half its positive integer
index-sum defect. This is the precise input for (2.2),
not a generic-minor assertion.

## 3. A one-sided Fourier--Jacobi matrix has every minor nonzero

Set $C=Q^*M_N$, and fix an arbitrary eigenvector index set
$E$ and an arbitrary physical coordinate set $J$, both
of size $k$. Expanding only over the path coordinates gives
$$
\det C_{E,J}
=\left(\prod_{e\in E}(R_0)_{ee}\right)
\sum_{|S|=k}
\det\Phi_{S,E}\,\omega^{-\sum S}
\det(P^*M_N)_{S,J}.
\tag{3.1}
$$
The normalization factor is common and nonzero.

The distinction from a general double expansion is that the
physical columns $J$ stay fixed. After root-of-unity row
and column factors are removed, the Fourier part of this
minor, transposed, is
$$
\det(z_j^{\,s})_{j\in J,\ s\in S},
\qquad z_j=e_N(\overline4\,j),
\tag{3.2}
$$
up to a common root-of-unity factor caused by the path
translation. All the $z_j$ are distinct valuation units.
The factor $N^{-k/2}$ is also common.

Divide (3.2) by its Vandermonde in the fixed nodes $z_j$.
For any increasing nonnegative exponents $S$, the quotient
is an integral Schur polynomial. This elementary alternant
identity can be obtained by successive monic division, or by
expanding monomial alternants in the integer Schur basis.
For the consecutive exponents $S_0=\{N-k,\ldots,N-1\}$,
the quotient is exactly a monomial in the $z_j$, hence a
valuation unit. Therefore
$$
\det(P^*M_N)_{S_0,J}\ne0,\qquad
v\!\left(
\frac{\det(P^*M_N)_{S,J}}
     {\det(P^*M_N)_{S_0,J}}
\right)\ge0.
\tag{3.3}
$$
This argument does not compare Vandermondes at different
node sets. In particular, arbitrary composite $N$ and
arbitrary physical $J$ cause no additional assumption.

For $S\ne S_0$, let $g=\sum S_0-\sum S>0$.
The relative valuation of its nonzero summand in (3.1)
is at least
$$
g-\frac g2+0=\frac g2>0
$$
by (2.1), (3.3), and $v(\omega)=1$.
The $S_0$ term is nonzero and uniquely dominates.
Thus
$$
\boxed{\det C_{E,J}\ne0\quad\text{for every }E,J.}
\tag{3.4}
$$

## 4. All coordinate minors of the top eigenspace

For completeness, positivity supplies the other one-sided
factor needed below. On the ordered coordinate basis of
$\bigwedge^k\mathbb R^N$, consider the additive compound
$$
L^{[k]}(v_1\wedge\cdots\wedge v_k)
=\sum_{j=1}^k
v_1\wedge\cdots\wedge Lv_j\wedge\cdots\wedge v_k.
$$
Every nonzero off-diagonal entry moves one index by one
step into an adjacent empty site. No index is crossed, so
the sign is positive and the coefficient is a positive
Jacobi edge. The graph of $k$-subsets joined by these
moves is connected.

A largest-Rayleigh-quotient vector of this real symmetric
matrix may be replaced by the absolute values of its
coordinates without decreasing the quotient. If a
nonnegative maximizing eigenvector had a zero entry,
its eigenvalue equation would force every neighboring
entry to be zero; connectedness would force it to vanish.
It is therefore strictly positive.

The largest eigenvalue of the compound is the unique sum
of the $k$ largest eigenvalues of $L$. Its eigenvector
is their wedge, whose coordinate entries are
$\det\Phi_{I,E_k}$. All are consequently nonzero.
The diagonal gauge and normalization preserve this, so
$$
\boxed{\det Q_{I,E_k}\ne0
\quad\text{for every physical }I,\ |I|=k.}
\tag{4.1}
$$
This statement concerns the top eigenspace; no assertion
about all coordinate minors of every arbitrary eigenspace
is substituted for it.

## 5. The unique largest exponential in a power minor

Write $W(s)=e^{sA_N}M_N$ and $B=Q^*M_NQ$.
In the $A_N$-basis, $W(s)$ is
$\operatorname{diag}(e^{sa_j})B$.
Exterior powers commute with multiplication. For a fixed
positive integer $r$, the physical minor
$\det W(s)^r[I,J]$ is therefore a finite sum over
successive $k$-element eigenvector sets:
$$
\begin{aligned}
\det W(s)^r[I,J]
=\sum_{E_1,\ldots,E_r}
&\det Q_{I,E_1}\,
e^{s\sum_{t=1}^r A_{E_t}}\\
&{}\times
\left(\prod_{t=1}^{r-1}\det B_{E_t,E_{t+1}}\right)
\det C_{E_r,J},
\end{aligned}
\tag{5.1}
$$
where $A_E=\sum_{j\in E}a_j$; the empty product at $r=1$
equals one. Equation (5.1) is just matrix multiplication
on $\bigwedge^k\mathbb C^N$, with no omitted paths.

The maximum of $A_E$ is unique, at $E_k$, because
the $a_j$'s are strictly ordered. Hence the largest
real exponential frequency in (5.1) is $rA_{E_k}$,
and only the constant sequence $E_t=E_k$ attains it.
Its coefficient is
$$
\det Q_{I,E_k}\,(b_k^0)^{r-1}\,\det C_{E_k,J}\ne0
\tag{5.2}
$$
by (4.1), (2.2), and (3.4). This proves that the minor
is a nonzero finite exponential polynomial in $s$.

All coefficients and all frequencies are algebraic.
After equal frequencies are collected, the qualitative
Lindemann--Weierstrass theorem applies at
$s=iNz\ne0$ algebraic: the exponents remain distinct
algebraic numbers and the retained coefficients are
nonzero algebraic numbers. The precise verified source
is Huang, ISSAC 2022, Theorem 1.1, author version
https://arxiv.org/pdf/2112.05004v2, page 1.
It follows that (1.1) holds for every positive $r$.

There is no assertion of a uniform lower bound as $r$
or $N$ varies. Each nonvanishing statement is exact,
and the argument holds for every integer $r>0$.

## 6. Negative powers

For every invertible matrix $T$, the complementary-minor
identity is
$$
\det T^{-1}[I,J]
=(-1)^{\sum I+\sum J}
\frac{\det T[J^c,I^c]}{\det T}.
\tag{6.1}
$$
To verify it, first assume the complementary block is
invertible, permute it to the upper-left corner, and
use the block inverse: the relevant inverse block is
the inverse Schur complement, while the determinant
of $T$ is the product of the complementary-block
determinant and the Schur-complement determinant.
The two permutation signs give the displayed sign.
Clearing the determinant denominators gives a polynomial
identity, so the result extends to every invertible
$T$ by density. The empty complementary determinant
is one.

Take $T=U_N(z)^{|r|}$. Its determinant is nonzero,
and every nonempty complementary minor is nonzero
by the positive-power result. Equation (6.1) proves
(1.1) for negative $r$ as well. This reasoning also
covers nonreal algebraic $z$.

## 7. Support uncertainty and its sharpness

Let $T=U_N(z)^r$, $S=\operatorname{supp}v$, and
$Y=\operatorname{supp}(Tv)$. If
$|S|+|Y|\le N$, at least $|S|$ rows lie outside
$Y$. Choose that many of them. The equations on
these rows give a square submatrix of $T$, with
columns $S$, annihilating the nonzero vector $v_S$.
This contradicts (1.1). Hence (1.2) holds.

Conversely fix $S,Y$ with $|S|=s$ and
$|Y|=N-s+1$. The $(s-1)$-by-$s$ matrix
$T[Y^c,S]$ has full row rank and a one-dimensional
nullspace. Every nonzero null vector has all $s$
coordinates nonzero: deleting a column leaves an
invertible $(s-1)$-square minor. Extend this vector
by zero off $S$. Its image vanishes on $Y^c$.
If it also vanished on any row in $Y$, the resulting
$s$-square submatrix would be singular, again
contradicting (1.1). Thus its image has exactly support
$Y$. The case $s=1$ uses the empty row matrix and
the already proved nonzero entries.

This is a statement about exact zeros. It does not
say how much mass remains on any specified support.
The auxiliary countermodel in this round also has
every-power nonzero minors while failing the pair
statistic. The all-power theorem therefore cannot
replace the unresolved microscopic cancellation.
