> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_endpoint_fourier_valuation.md`. Embedded SHA256: `315d5ec9660f2249549542fa9a2c5b12ff1d8851f233c1b08a963cf019cbba8d`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Independent audit: endpoint Fourier-minor valuations

Round 5, 21 October 2026. Auditor: /root/audit_uniform_word_r4.

## 1. Target, verification scope, and verdict

The entire frozen target arithmetic_endpoint_fourier_valuation.md was read.
Its independently checked SHA-256 is

457c14773d76cf29fb034d3a006ba5c5314e0a973193931431c3dd1b38356d2a.

**Verdict.** Theorem 1 and the coordinate-minor application (6.2) are proved
as stated. The proof works for every prime $p$, every $n$ coprime to $p$,
and every allowed endpoint count vector, without a squarefreeness assumption
on $n$. The argument does not prove nonvanishing of the full mixed
eigenvector-basis overlap minor. In particular it does not establish simple
spectrum of the original $U_N$ in the remaining dimensions, or establish
or refute $H_{\rm diag}$.

No target file was changed. The $k=0$ determinant is handled separately as
one; the archimedean formulas involving a power of $k$ inherit the explicit
$k\ge1$ condition of (5.1).

## 2. Row reflection, valuation field, and residue multiplicities

For $i=sn+n-k_s,\ldots,sn+n-1$, the reflected index
$i'=-i-1\pmod{pn}$ runs over

$$
(p-1-s)n,\ldots,(p-1-s)n+k_s-1.
$$

With $\eta=\zeta^{-1}$, the entry identity is

$$
\zeta^{ij}=\zeta^{-j}\eta^{i'j}.
$$

The resulting column factors and any row permutation have valuation zero.
Both the reflected row set and the column set have exactly

$$
m_a=\#\{s:k_s>a\}
$$

elements in residue class $a\bmod n$. These multiplicities are
nonincreasing in $a$, and no multiplicity exceeds $p$. This equality
does not require the two sets to coincide, or their block counts in the
original order to agree after reflection.

All roots of unity are valuation units. In a residue field of characteristic
$p$, the image of a primitive $p$-th root is one. The image $\xi$ of
$\eta$ has exact order $n$: a root of unity of order prime to $p$
cannot lose order under reduction, because a nonidentity such root reducing
to one would turn its vanishing geometric sum into a nonzero integer modulo
$p$. Apply this to $\eta^p$, whose order is $n$; also
$(\xi^n-1)^p=\xi^{pn}-1=0$.

For a primitive $p$-th root $\epsilon$, each

$$
\frac{1-\epsilon^j}{1-\epsilon}=1+\cdots+\epsilon^{j-1},
\qquad 1\le j<p,
$$

is a unit, since its residue is $j$. Taking valuations in
$\prod_{j=1}^{p-1}(1-\epsilon^j)=p$ therefore gives
$v(1-\epsilon)=1/(p-1)$. This includes $p=2$.

## 3. The alternant quotient has no hidden denominators

For distinct nonnegative column exponents $c_j$, the polynomial
$$
D(X)=\det(X_i^{c_j})
$$
is alternating. Each $X_j-X_i$ is prime in the integral polynomial ring,
as its quotient ring is a polynomial ring over $\mathbb Z$. Distinct such
factors are nonassociate, so their product $V(X)$ divides $D(X)$ in that
same ring:
$$
D(X)=V(X)P(X),\qquad P\in\mathbb Z[X_1,\ldots,X_k].
$$
In particular this division introduces neither rational nor $p$-adic
denominators.

Group the variables by their row residue $a$, with variables
$X_{a,r}$, $0\le r<m_a$. Apply exactly $r$ derivatives to the variable
$X_{a,r}$, then set all variables in this group equal to $\xi^a$.

The within-group Vandermonde has vanishing order
$\binom{m_a}{2}$ on that diagonal, equal to the total available derivative
order in the group. A nonzero Leibniz term therefore has to put every such
derivative on that within-group factor. The derivative of the within-group
Vandermonde is exactly
$$
\prod_{r=0}^{m_a-1}r!.
$$
This follows by expanding its determinant: only the monomial with exponent
$r$ in variable $X_{a,r}$ can survive all prescribed derivatives, since
all other monomials have the same total degree.

Consequently the confluent identity (3.2) is exact, up to a harmless ordering
sign. All its explicit right-hand factors are nonzero in the residue field:
the cross-group differences have distinct nodes, and $r<m_a\le p$ implies
$r!\ne0$ in characteristic $p$. In particular the edge case $m_a=p$
uses only $0!,\ldots,(p-1)!$, not $p!$.

## 4. Complete reconstruction of the block triangular step

Multiplying row $(a,r)$ by $\xi^{ar}$ removes its root-of-unity factor.
Within each row group the change from falling powers $(c)_r$ to ordinary
powers $c^r$ is triangular with diagonal one, over the integers and hence
over the residue field. We need the invertibility of

$$
C_{(a,r),j}=\xi^{ac_j}c_j^r.
$$

In column residue group $b$, the exponents are $c_{b,j}=b+ns_{b,j}$.
The $s_{b,j}$ are distinct members of $\{0,\ldots,p-1\}$, so the $c_{b,j}$
are distinct modulo $p$ because $n$ is a unit there. Thus the matrix

$$
V_b=(c_{b,j}^{\,r})_{0\le r<m_b,\,1\le j\le m_b}
$$

is an invertible Vandermonde. The inverses used at this step exist in the
residue field; lifting them to characteristic zero is unnecessary.

Since $\xi^n=1$, one has $\xi^{ac_{b,j}}=\xi^{ab}$. Multiplication of
column group $b$ by $V_b^{-1}$ makes the entry in row degree $r$, new
column degree $q$, exactly $\xi^{ab}\delta_{rq}$ whenever $r<m_b$.
If $r<q$, then $q<m_b$, so this entry is indeed zero. Sorting both rows
and columns by degree therefore gives a block lower triangular matrix.

The block of equal row and column degree $r$ is square: its row and column
index sets are both
$$
A_r=\{a:m_a>r\}.
$$
Monotonicity of $m_a$ makes this set the initial interval
$\{0,\ldots,t_r-1\}$. The diagonal block is
$$
(\xi^{ab})_{0\le a,b<t_r},
$$
an ordinary Vandermonde in the distinct nodes
$1,\xi,\ldots,\xi^{t_r-1}$. Its determinant is nonzero even if $n$
has repeated prime factors. Empty blocks contribute one.

It follows that the confluent determinant is nonzero. Returning to the
integral identity proves that $P$ evaluated at the original row nodes has
nonzero reduction and hence valuation zero. No cancellation of a putative
lowest coefficient has been assumed in this step; its nonvanishing has
been established by the displayed invertible diagonal blocks.

## 5. Exact valuation and the original cat-matrix factor

Only the ordinary Vandermonde contributes to the valuation. Distinct
row residues modulo $n$ give distinct reductions, so their node differences
are units. Two rows in the same residue class have indices differing by
$nq$, where $q\not\equiv0\pmod p$; their node ratio is a primitive
$p$-th root. Each such pair contributes $1/(p-1)$. Counting them gives

$$
v(D_{I,J})=\frac1{p-1}\sum_{a=0}^{n-1}\binom{m_a}{2}.
$$

As a check on edge cases, $n=1$ yields the prime-order valuation
$\binom{k}{2}/(p-1)$. For the full determinant $k=pn$, every $m_a=p$
and the formula gives $pn/2$, agreeing with the valuation of the full
unnormalized Fourier determinant.

The archimedean lower bound follows from the nonzero integer field norm and
Hadamard's bound $k^{k/2}$ for each conjugate. The target does not claim that
this very small bound supplies a useful spectral estimate.

For $N=7n$, $7\nmid n$, the actual path starts are
$h+sn$, $h=(N+1)/2$. Expansion of the prescribed modular quadratic
kernel gives row and column roots of unity times

$$
N^{-1/2}\zeta_N^{\overline4\,ij}.
$$

The exponent coefficient $\overline4$ is invertible for odd $N$, so
$\zeta_N^{\overline4}$ is primitive. Every normalized square root of $N$
has valuation $v_7(\sqrt N)=1/2$, since $7\Vert N$. Taking the determinant
therefore adds exactly $-k/2$, and gives

$$
v_7\det M_N[I,J]
=\frac16\sum_a\binom{m_a}{2}-\frac{k}{2}.
$$

Root-of-unity chirps and coordinate reorderings contribute no valuation.
This checks the normalization as well as the endpoint sets.

## 6. Independent finite check of the stated 5-adic warning

I read and ran the author's exact finite-field probe at $N=63$, obtaining
seven zero reductions among the 210 size-four endpoint count vectors. To
avoid relying solely on that program, I wrote the independent certificate
audit_endpoint_mod5_certificate.py, SHA-256

b194a9ec337043d1db5910d815098eaa7728fd00de2d7f04df3d40b2dca1e471.

It verifies the particular counts $(0,0,0,0,2,0,2)$, whose coordinate sets
are
$$
I=(43,44,61,62),\qquad J=(36,37,54,55).
$$
In the field $\mathbb F_5[W]/(W^6+W+2)$, put
$$
z=2+2W+4W^2+W^3+2W^4+4W^5.
$$
The certificate checks irreducibility using
$W^{5^6}=W$ modulo the degree-six polynomial and coprimality with
$W^{5^3}-W$ and $W^{5^2}-W$. These tests are sufficient: the first
identity leaves only irreducible-factor degrees dividing six, and the latter
two exclude every proper divisor of six.

It then checks $z^{63}=1$, $z^{21}\ne1$, and $z^9\ne1$, so $z$
has order exactly 63. The 24-term determinant expansion, reduced modulo
$X^{63}-1$, is

$$
\begin{split}
D(X)={}&-X^6-X^{15}+4X^{24}+X^{32}-2X^{33}+X^{34}\\
&-2X^{41}-2X^{42}-2X^{43}
+X^{50}-2X^{51}+X^{52}+4X^{60}.
\end{split}
$$

Exact polynomial arithmetic gives $D(z)=0$. The certificate separately
checks $\Phi_{63}(z)=0$ and $\Phi_{63}'(z)\ne0$, where
$$
\Phi_{63}(X)=X^{36}-X^{33}+X^{27}-X^{24}+X^{18}-X^{12}+X^9-X^3+1.
$$
Thus this is a zero reduction at a prime above five of the cyclotomic
integer determinant. It is not a zero determinant in characteristic zero;
the theorem just proved rules the latter out. This finite check supports
only the specific failure of a blanket five-adic unit assertion.

## 7. First remaining implication and literature boundary

For a fixed mixed selection of path eigenvectors, the endpoint term in the
double Cauchy--Binet sum has the unique minimum exponent of the gauge
$\omega$: each row set must use its largest $k_s$ local coordinates and
each column set its smallest $k_s$ local coordinates. The minimum is
$$
-\sum_s k_s(n-k_s).
$$
Coordinate-minor nonvanishing makes this an actual nonzero coefficient in
the auxiliary Laurent polynomial. It does not rule out a zero at one
prescribed nonzero algebraic value of its variable.

Here $\omega=(-3+4i)/5=(1+2i)/(1-2i)$. At the selected prime above five,
its valuation is one, whereas at every prime above seven it is a unit.
Consequently the valuation computed in Theorem 1 cannot be substituted into
the five-adic dominance argument. The exact unresolved assertion is
noncancellation of the full mixed overlap minor at this prescribed
$\omega$, including every other coordinate term.

I also checked the cited primary source's HTML version:

https://arxiv.org/html/2505.24326v3

Caragea, Lee, Malikiosis and Pfander's Theorem 5.7 is explicitly stated for
squarefree $N$; Section 5 contains the related confluent argument.
The audited target's nonsquarefree-$n$ statement is justified by its own
proof above, not by dropping a hypothesis from that theorem. No historical
priority claim has been audited or inferred.
