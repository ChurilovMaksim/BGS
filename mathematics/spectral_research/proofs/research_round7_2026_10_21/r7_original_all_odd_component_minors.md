> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round7_2026_10_21/r7_original_all_odd_component_minors.md`. Embedded SHA256: `edf0e6b09942cf9b6c0877dd533be3f866b6273a4483358a4c5d1f9768dbb39b`.
> [Thematic guide](../../topics/algebra.md).

# Original minors with rows in one Jacobi component, in every odd dimension

Research continuation, 21 October 2026. This is an all-odd consequence
of the fixed-column Fourier-minor argument developed in this round.
It concerns the exact original matrix, at the prescribed algebraic
parameter. It does not prove the coefficient Jacobian nonsingular
in the seven-component case, or any spectral-statistics estimate.

## 1. Statement

For odd $N\ge3$, put
$$
g=\gcd(N,7)\in\{1,7\},\qquad n=N/g,\qquad h=(N+1)/2.
$$
The Jacobi components of $A_N$ have coordinate sets
$$
\mathcal P_s=\{h+sn+j\pmod N:0\le j<n\},
\qquad 0\le s<g.
\tag{1.1}
$$

**Theorem.** Let $z\ne0$ be algebraic and complex. For every
pair of physical coordinate sets $I,J$ of equal size
$1\le k\le n$, if $I\subset\mathcal P_s$ for one
component $s$, then
$$
\boxed{\det U_N(z)[I,J]\ne0,
\qquad U_N(z)=e^{izNA_N}M_N.}
\tag{1.2}
$$
The column set $J$ is arbitrary; its entries may lie in any
of the components. This includes the original $z=10^{-80}$.
When $7\nmid N$, there is one component and (1.2) gives every
minor. When $7\mid N$, (1.2) is a statement about all minors
whose rows lie in one of the seven paths. No global simplicity of
$A_N$ or $U_N$ is assumed in this latter case.

**Corollary.** If $v\ne0$ has $m\le n$ nonzero
physical coordinates, then each component $\mathcal P_s$
contains at least $n-m+1$ nonzero coordinates of $U_N(z)v$.
Thus
$$
|\operatorname{supp}(U_N(z)v)|\ge N-g(m-1).
\tag{1.3}
$$
The conclusion is about exact zeros. It provides no lower bound
on the magnitudes of the nonzero entries.

## 2. Exact Jacobi input

The modular-half definition in the question gives
$$
(A_N)_{x,x+1}=\omega^{-1}r((x+h)/N)/200,
\qquad \omega=(-3+4i)/5.
\tag{2.1}
$$
The diagonal is $V(x/N)$, with $V$ as in the problem.
On an odd grid $r(y/N)=0$ if and only if $N\mid7y$.
Therefore the zero hopping edges are exactly the ends of the
components (1.1), and there are no internal zero edges.

Let $P_s:\mathbb C^n\to\mathbb C^N$ embed the ordered
component (1.1), and let
$D=\operatorname{diag}(1,\omega,\ldots,\omega^{n-1})$.
Then
$$
L_s=200D^{-1}P_s^*A_NP_sD
\tag{2.2}
$$
is real symmetric Jacobi, with positive internal off-diagonal
entries. In particular each individual component has simple
spectrum, even if eigenvalues of different components coincide.
The empty-edge case $n=1$ is included.

At a place over $1+2i$, normalized by $v(5)=1$,
$v(\omega)=1$, the diagonal entries of $L_s$ are
integral, and its nonzero edges have valuations in $[0,1/2]$.
The proof is the exact factorization
$$
r(y/N)=-\frac{(\eta^7-1)^2(\eta+1)^2}{4\eta^8},
\qquad \eta=e_N(y),
$$
together with
$v(1-\zeta_{5^a})=1/(4\cdot5^{a-1})$ and the fact that
an odd-order root has $1+\eta$ a unit. These estimates,
including powers of five dividing $N$, are proved in
`research_round2_2026_10_20/arithmetic_padic_jacobi_simplicity.md`,
SHA-256
`f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df`,
and their application to all seven components is proved in
`arithmetic_seven_chain_discriminant_checkpoint.md`, SHA-256
`eee2b4caa27349a81e5cf3113d53ff1f88164e44b748c2eb99754f6e07fc6a8f`.

For a matrix $\Phi_s$ of real algebraic eigenvectors of
$L_s$, any eigenvector set $E$ of size $k$, and
$S_0=\{n-k,\ldots,n-1\}$, the endpoint-minor bound is
$$
v\left(\frac{\det\Phi_s[S,E]}{\det\Phi_s[S_0,E]}\right)
\ge-\frac12\left(\sum S_0-\sum S\right).
\tag{2.3}
$$
Its denominator is nonzero. The same sources prove (2.3) by
the endpoint monic Jacobi recurrence: division of a polynomial
alternant by its eigenvalue Vandermonde leaves an integral
polynomial, while the edge denominator costs at most one half
per step. No unit assumption on eigenvalue differences is used.

## 3. Arbitrary physical columns and one eigenvector component

Choose an orthonormal algebraic eigenbasis on each component.
For one component write it as $Q_s=P_sD\Phi_s R_s$, with
$R_s$ the nonzero diagonal normalization. For any eigenvector
index set $E$ of size $k$ in this component and any physical
column set $J$ of size $k$, the following is nonzero:
$$
\boxed{\det(Q_s^*M_N)[E,J]\ne0.}
\tag{3.1}
$$

To prove it, expand by Cauchy--Binet over component row coordinates:
$$
\det(Q_s^*M_N)[E,J]
=\left(\prod_{a\in E}(R_s)_{aa}\right)
\sum_{|S|=k}
\det\Phi_s[S,E]\,
\omega^{-\sum S}\,
\det(P_s^*M_N)[S,J].
\tag{3.2}
$$
The term $S=S_0$ has the unique smallest power of $\omega$.
We now verify the Fourier ratio with $J$ fixed.

Up to row and column roots of unity and $N^{-1/2}$, the
kernel $(P_s^*M_N)[u,y]$ is
$q^{uy}$, where $q=e_N(4^{-1})$ is primitive. The offset
of the component is absorbed into column factors. After
transposing its minor, the nodes $q^y$, $y\in J$, are
fixed distinct roots of unity and the exponent set is $S$.
Every such alternant is the ordinary Vandermonde in these nodes
times an integral Schur polynomial. For $S_0$, whose
exponents are consecutive, the Schur factor is a monomial in
the nodes and hence a unit. The common Vandermonde is nonzero
and cancels in the ratio, including when it has positive
valuation. Therefore
$$
v\left(\frac{\det(P_s^*M_N)[S,J]}
                 {\det(P_s^*M_N)[S_0,J]}\right)\ge0,
\tag{3.3}
$$
and the denominator is nonzero. This is a fixed-column argument;
no claim that a mixed-component endpoint Fourier minor is a unit
has entered the proof.

For $S\ne S_0$ put
$d_S=\sum S_0-\sum S\ge1$. The gauge factor contributes
$d_S$, (2.3) costs at most $d_S/2$, and (3.3) costs
nothing. Hence the ratio of each other nonzero summand in (3.2)
to its $S_0$-summand has valuation at least
$d_S/2>0$. The latter summand is nonzero and uniquely
dominates. This proves (3.1).

## 4. Top exterior vectors within a component

Let $E_s^{(k)}$ denote the $k$ largest eigenvalues in
component $s$. For every $k$-element component coordinate
set $I$,
$$
\det Q_s[I,E_s^{(k)}]\ne0.
\tag{4.1}
$$
Here the physical row notation means restriction to the component.
One direct proof uses the additive exterior compound of the real
Jacobi matrix $L_s$. In the increasing $k$-subset basis,
its off-diagonal entries move one index to an unoccupied neighbor.
They are positive, because no other index is crossed. This graph
is connected. A maximum of its Rayleigh quotient can be replaced
by the absolute values of its entries, and a zero entry of a
nonnegative maximizing eigenvector forces all neighboring entries
to vanish. Connectedness would then force the vector to be zero.
Thus its top eigenvector has every entry nonzero.

The eigenvalues of this compound are the sums of $k$ distinct
local Jacobi eigenvalues. Its unique largest eigenvalue is their
top $k$ sum, whose eigenvector is the wedge of those $k$
eigenvectors. Its coordinates are the minors in (4.1) before the
nonzero gauge and normalization factors. Those factors preserve
nonvanishing. This proves (4.1), also for $k=n$ and $n=1$.

## 5. Large real time and exact specialization

Let $V(t)=e^{tA_N}M_N$, with real $t\to+\infty$,
and use the orthonormal eigenbasis obtained by combining all
components. If $I$ lies in component $s$, expansion of
the minor gives
$$
\det V(t)[I,J]
=\sum_{\substack{E\text{ in component }s\\|E|=k}}
e^{t\sum_{a\in E}a}
\det Q_s[I,E]\,
\det(Q_s^*M_N)[E,J].
\tag{5.1}
$$
All terms with an eigenvector from another component have a zero
column in their restriction to $I$, which explains the stated
sum even if eigenvalues in different components coincide.

The strictly ordered local spectrum gives a unique largest
exponent in (5.1), at $E=E_s^{(k)}$. Both factors of its
coefficient are nonzero by (3.1) and (4.1). Thus (5.1) is a
nonzero finite exponential polynomial with algebraic coefficients
and algebraic frequencies. Equal frequencies in the remaining
terms can be collected without affecting this largest term.

At $t=iNz$, $z\ne0$ algebraic, the surviving exponents
are distinct algebraic numbers. The qualitative
Lindemann--Weierstrass theorem therefore proves (1.2).
The exact external statement used is Theorem 3.2 of S. A. Popescu,
*A Simple and Self-contained Proof for the Lindemann--Weierstrass
Theorem*, DOI `10.1007/978-3-031-51959-8_16`, author version
<https://arxiv.org/pdf/2306.14352>, page 14. It states linear
independence over the algebraic numbers of the exponentials of
distinct algebraic numbers. Its hypotheses have been verified
above; its text was reopened and checked in this research round.

Finally, to prove (1.3), let $J=\operatorname{supp}v$, with
$|J|=m\le n$. If $U_N(z)v$ had at least $m$ zero
coordinates in a component, choose $m$ of them as $I$.
Then $U_N(z)[I,J]v_J=0$, contradicting the invertible minor
(1.2) and $v_J\ne0$. Each component has at most $m-1$
zeros, which proves (1.3).

## 6. Boundary

The theorem treats every odd dimension, including every multiple
of seven. It does not make a claim about arbitrary mixed-component
row sets in those dimensions. It also does not assert the analogous
statement for higher positive powers in the seven-component case:
the intermediate exterior eigenspaces would then mix components.
The one-component higher-power theorem is established separately.

No inverse bound for any minor follows here. In particular these
nonvanishing statements do not supply the weighted signed quantum
trace estimate at times comparable with $N$, which remains
the first open asymptotic step toward $H_{\rm diag}$.
