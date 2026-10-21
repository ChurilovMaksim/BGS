> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/arithmetic_endpoint_good_place_obstruction.md`. Embedded SHA256: `8ceb2b4830ecf578ec81269d7e11db8486739461bd73cb7be663c06e971aa932`.
> [Thematic guide](../../topics/dephasing.md).

# A precise bad place, and the narrower good-place question

Research continuation, 21 October 2026. This note concerns endpoint
coordinate minors of the original matrix $M_N$, not spectral
correlations or eigenvector-basis overlap minors.

## 1. An exact four-by-four calculation at $N=63$

Take seven path counts
$$
(k_0,\ldots,k_6)=(2,0,2,0,0,0,0).
$$
With path length $n=9$, the endpoint row and column sets are
$$
I=\{7,8,25,26\},\qquad J=\{0,1,18,19\}.
$$
Thus $I=J+7$. For a primitive 63rd root $\zeta$,
$$
\det(\zeta^{ij})_{i\in I,j\in J}
=\zeta^{7\sum J}\det(\zeta^{ij})_{i,j\in J}.
\tag{1.1}
$$
The first factor is a unit at every finite place.

Expanding the determinant on the right over its 24 permutations,
and reducing the exponents modulo 63, gives $D(\zeta)$, where
$$
\begin{split}
D(X)={}&4X-X^{10}-X^{19}+4X^{28}
 +X^{36}-2X^{37}+X^{38}\\
&-2X^{45}-2X^{46}-2X^{47}
 +X^{54}-2X^{55}+X^{56}.
\end{split}                                                     \tag{1.2}
$$

Define
$$
P(X)=X^6+3X^5+3X^4+3X^3+3X^2+3X+1\in\mathbb F_5[X].
\tag{1.3}
$$
The following polynomial identities and Euclidean-algorithm results
are exact in $\mathbb F_5[X]$:
$$
\begin{gathered}
X^{5^6}\equiv X\pmod P,\\
\gcd(P,X^{5^2}-X)=\gcd(P,X^{5^3}-X)=1,\\
X^{63}\equiv1\pmod P,\\
X^9\equiv2+X^2+X^3+4X^4+4X^5\pmod P,\\
X^{21}\equiv2X+2X^2+3X^3+2X^5\pmod P.
\end{gathered}                                                   \tag{1.4}
$$
The first two lines prove that $P$ is irreducible of degree 6:
the first forces its squarefree irreducible factors to have degrees
dividing 6, and the gcd conditions exclude degrees 1, 2 and 3.
The remaining lines prove that the image of $X$ in
$\mathbb F_5[X]/P$ has order exactly 63.

The cyclotomic polynomial is
$$
\begin{split}
\Phi_{63}(X)
&=\frac{X^{42}+X^{21}+1}{X^6+X^3+1}\\
&=X^{36}-X^{33}+X^{27}-X^{24}+X^{18}
  -X^{12}+X^9-X^3+1.
\end{split}
\tag{1.5}
$$
Direct reduction gives the stronger exact identity
$$
\boxed{\gcd(\overline{\Phi_{63}},\overline D)=P
\quad\hbox{in }\mathbb F_5[X].}
\tag{1.6}
$$
Consequently the endpoint determinant reduces to zero for precisely
the six primitive roots belonging to the irreducible factor $P$.

There are 36 primitive 63rd roots and
$\operatorname{ord}_{63}(5)=6$, so $\Phi_{63}$ has six
irreducible factors of degree 6 in characteristic 5. At the other
five factors, (1.6) says that this same determinant is a unit.
Thus this example refutes the blanket claim that every endpoint
minor is a unit at every place above 5. It does not refute the
claim that each endpoint minor has at least one good place.

## 2. Exact norm and comparison with the new 7-adic formula

The exact resultant calculation yields
$$
\boxed{
\left|\operatorname{Norm}_{\mathbb Q(\zeta_{63})/\mathbb Q}
 D(\zeta_{63})\right|
 =5^6\,7^{12}\,127^2\,881^2
 =2707420823861071212015625.
}
\tag{2.1}
$$
It is obtained by reducing $D$ modulo the monic polynomial
$\Phi_{63}$, forming their Sylvester matrix, and evaluating its
determinant by integer fraction-free elimination. Every division
in the supplied program is asserted exact.

All identities (1.2)--(1.6) and (2.1) have a small, independent,
integer-arithmetic checker:
\`arithmetic_endpoint_mod5_certificate.py\`, SHA256
\`df90a06eab14b1bb97b9416fa6d2f1e3cd0543170ed77f0dc17a03888bdbb700\`.
It has no external dependencies and does not inspect numerically
computed eigenvalues.

Theorem 1 of
\`arithmetic_endpoint_fourier_valuation.md\`, SHA256
\`457c14773d76cf29fb034d3a006ba5c5314e0a973193931431c3dd1b38356d2a\`,
gives $m_0=m_1=2$, with all other $m_a=0$. Its exact
7-adic valuation is therefore $2/6=1/3$. Since
$\varphi(63)=36$, this predicts the factor $7^{12}$ in
(2.1), in agreement with the independent resultant calculation.
The determinant is nonzero over $\mathbb C$; its zero reduction
at a prime above 5 is a different assertion.

## 3. The narrower remaining arithmetic question

For $N=7n$, $\gcd(n,35)=1$, and a prescribed seven-tuple of
endpoint counts, let $D_{I,J}(\zeta_N)$ be the unnormalized
coordinate determinant. A potentially sufficient replacement for
the failed all-places unit claim is
$$
D_{I,J}(\zeta_N)\notin5\mathbb Z[\zeta_N].
\tag{3.1}
$$
Because $5\nmid N$, reduction of $X^N-1$ is separable.
Thus (3.1) is equivalent to the existence of at least one
primitive-root factor of $\Phi_N$ in characteristic 5 at which
the determinant is nonzero.

Such a place may be chosen separately for each required minor.
It is compatible with the old Jacobi-gauge argument: choose
the Gaussian prime $1+2i$, so
$v(\omega)=1$ for $\omega=(1+2i)/(1-2i)$, and extend
the corresponding valuation and the selected cyclotomic place
to a common algebraic field. They are compatible because
$N$ is odd and the 4th and $N$-th root choices may be made
independently. Each internal Jacobi hopping coefficient is then
a unit: its cyclotomic factors are differences of distinct
prime-to-5 roots, and the exact zero edges have already been
removed. The diagonals are integral after multiplying the
Jacobi matrix by 200, as in the frozen proof.

The old endpoint recurrence consequently gives integral
eigenvector-minor ratios relative to their path endpoints.
If (3.1) supplies a unit Fourier endpoint minor, the other
coordinate terms have a strictly larger integral power of
$\omega$, and the unique endpoint term dominates. This
conditional paragraph only explains the mathematical relevance
of (3.1); it does not assert (3.1).

The exact bounded discriminator
\`arithmetic_endpoint_global_content_probe.py\`
computes the determinant polynomial by integer permutation sums
and tests its remainder modulo $\Phi_N$ in characteristic 5.
Finite non-discovery in this test is not a proof of (3.1).
No uniform proof or counterexample to (3.1) has been obtained
in this note. Dimensions divisible by 49, and the ramified
case $5\mid n$, require additional arguments regardless.

Even a proof of (3.1) and of the resulting simple-spectrum
statement would not establish the required limiting
factorial-moment cancellations in $H_{\rm diag}$.
