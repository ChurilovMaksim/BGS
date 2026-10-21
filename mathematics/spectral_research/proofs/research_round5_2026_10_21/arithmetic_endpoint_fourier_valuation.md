> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/arithmetic_endpoint_fourier_valuation.md`. Embedded SHA256: `457c14773d76cf29fb034d3a006ba5c5314e0a973193931431c3dd1b38356d2a`.
> [Thematic guide](../../topics/dephasing.md).

# Exact valuations of the seven-chain endpoint Fourier minors

Research continuation, 21 October 2026. Base checkpoint:
\`Spectral_research_round4_2026-10-21.md\`, SHA256
\`e74f697134ea0d7d0ad5776c118ac267cf4999ae029e5b1f0252de364596fa4a\`.

## 1. Scope and result

The earlier proof of simple spectrum for the specified
$U_N=\exp(i\tau N A_N)M_N$ covers every odd $N$ with $7\nmid N$.
When $N=7n$, the exact zeros of the Jacobi hopping coefficients split
$A_N$ into seven paths of length $n$. The difficulty in the
large-complex-time discriminant argument is a principal minor of
$M_N$ expressed in eigenvectors from several of these paths.

This note proves a uniform statement about the leading *coordinate*
Fourier minor in that expansion. It applies when $7\nmid n$, including
arbitrarily nonsquarefree $n$. It does not prove that the full
eigenvector-basis minor is nonzero at the prescribed gauge.

The proof is elementary and is given in full. Its confluent determinant
method is closely related to the arithmetic-principal-minor argument
in Caragea, Lee, Malikiosis and Pfander,
*Principal minors of Fourier matrices of square-free order*,
arXiv:2505.24326v3, Theorem 5.7 and the proof of Theorem 1.4 in Section 5:
<https://arxiv.org/pdf/2505.24326v3>. Their Theorem 5.7 is stated for
squarefree $N$. No extension of that theorem is being assumed here;
the proof below establishes the claimed special class and its exact
valuation without that restriction. No claim of historical novelty
is made.

### Theorem 1

Let $p$ be prime, $n\ge1$, $\gcd(p,n)=1$, $N=pn$. Choose
integers $0\le k_s\le n$, $s=0,\ldots,p-1$, and let

$$
\begin{split}
k&=\sum_{s=0}^{p-1}k_s,\\
I&=\bigcup_{s=0}^{p-1}
 \{sn+n-k_s,\ldots,sn+n-1\},\\
J&=\bigcup_{s=0}^{p-1}
 \{sn,\ldots,sn+k_s-1\},\\
m_a&=\#\{s:k_s>a\},\qquad 0\le a<n.
\end{split}                                                    \tag{1.1}
$$

Empty intervals are omitted. Let $\zeta$ be any primitive $N$-th
root of unity, and let $v$ be any extension to a field containing
$\zeta$ of the $p$-adic valuation normalized by $v(p)=1$. Then

$$
\boxed{\quad
v\!\left(\det(\zeta^{ij})_{i\in I,j\in J}\right)
 =\frac1{p-1}\sum_{a=0}^{n-1}\binom{m_a}{2}.
\quad}                                                         \tag{1.2}
$$

The determinant is therefore nonzero. The convention for $k=0$
is that the determinant is 1.

## 2. Reduction of the rows and roots of unity

Replace each row index $i$ by $i'=-i-1\pmod N$, and replace
$\zeta$ by $\eta=\zeta^{-1}$. The matrix entry transforms as

$$
\zeta^{ij}=\zeta^{-j}\eta^{i'j}.                                 \tag{2.1}
$$

The column factors in (2.1) are units. Up to row order, the new row
set is

$$
I'=\bigcup_{s=0}^{p-1}
 \{(p-1-s)n,\ldots,(p-1-s)n+k_s-1\}.                             \tag{2.2}
$$

Both $I'$ and $J$ have exactly $m_a$ elements in residue class
$a\pmod n$. The sequence $m_0,\ldots,m_{n-1}$ is nonincreasing,
and $0\le m_a\le p$.

Let the residue field of $v$ be $\kappa$, of characteristic $p$.
The image $\xi$ of $\eta$ has exact order $n$. Indeed,
$\eta^{pn}=1$ implies $\xi^n=1$. A root of unity of order
prime to $p$ retains its order upon reduction: if such a nonidentity
root $u$, of order $d$, reduced to 1, then
$1+\cdots+u^{d-1}=0$ would reduce to the nonzero element $d$
of $\kappa$. Since $\eta^p$ has order $n$, its image has
order $n$, and hence so does $\xi$.

For later use, if $\epsilon$ is a primitive $p$-th root, then

$$
v(1-\epsilon)=\frac1{p-1}.                                     \tag{2.3}
$$

To see this, use
$\prod_{j=1}^{p-1}(1-\epsilon^j)=p$. Each quotient
$(1-\epsilon^j)/(1-\epsilon)=1+\cdots+\epsilon^{j-1}$
reduces to the nonzero element $j$, so all $p-1$ factors have
the same valuation.

## 3. An integral alternant quotient

Enumerate $J$ as distinct integers $c_1,\ldots,c_k$, and put

$$
D(X_1,\ldots,X_k)=\det(X_i^{c_j})_{1\le i,j\le k},
\qquad
V(X)=\prod_{1\le i<j\le k}(X_j-X_i).
$$

Because $D$ is alternating, every $X_j-X_i$ divides it. These
are pairwise nonassociate prime elements of
$\mathbb Z[X_1,\ldots,X_k]$. Thus

$$
D(X)=V(X)P(X),\qquad P\in\mathbb Z[X_1,\ldots,X_k].              \tag{3.1}
$$

We shall prove that $P$ evaluated at the nodes
$(\eta^i)_{i\in I'}$ is a valuation unit. These nodes reduce to
$\xi^a$, each repeated $m_a$ times.

Label the variables in group $a$ by $X_{a,r}$,
$0\le r<m_a$, in that order. Apply
$\prod_a\prod_{r=0}^{m_a-1}\partial_{X_{a,r}}^r$
to (3.1), and set $X_{a,r}=\xi^a$ in $\kappa$.
The within-group Vandermonde has total degree
$\binom{m_a}{2}$, which equals the total derivative order in that
group. Every Leibniz term leaving a positive-order vanishing factor
from that Vandermonde is zero. The resulting identity is

$$
\det\!\left((c_j)_r\,\xi^{a(c_j-r)}\right)_{(a,r),j}
 =
 P\!\left(\bigl((\xi^a)^{[m_a]}\bigr)_{a=0}^{n-1}\right)
 \left(\prod_a\prod_{r=0}^{m_a-1}r!\right)
 \left(\prod_{a<b}(\xi^b-\xi^a)^{m_am_b}\right),                \tag{3.2}
$$

up to an overall sign if a different initial ordering is used.
Here $(c)_r=c(c-1)\cdots(c-r+1)$, with $(c)_0=1$;
the notation $(\xi^a)^{[m_a]}$ means $m_a$ repeated arguments.
The identity can also be checked directly by expanding each
within-group Vandermonde as $\det(X_{a,r}^{\,q})_{r,q}$:
the prescribed derivatives pick its identity-permutation monomial
and contribute $\prod_{r=0}^{m_a-1}r!$.

All explicit factors on the right of (3.2) are nonzero: $m_a\le p$
ensures $r<p$, and $\xi^a\ne\xi^b$ for $a\ne b$.
It remains to prove that the determinant on the left is nonzero.

## 4. The confluent matrix has a triangular decomposition

Remove the row unit $\xi^{-ar}$ from row $(a,r)$.
Within each row group, replace the falling powers $(c)_r$ by
the ordinary powers $c^r$. The change of basis is triangular
with diagonal 1, since both polynomial families are monic in degree
$r$. Thus it suffices to prove invertibility of

$$
C_{(a,r),j}=\xi^{ac_j}c_j^r,\qquad 0\le r<m_a.                 \tag{4.1}
$$

Group the column exponents by their residue $b\pmod n$. The
group contains exactly $m_b$ exponents

$$
c_{b,j}=b+n s_{b,j},\qquad 1\le j\le m_b,
$$

where the $s_{b,j}$'s are distinct elements of
$\{0,\ldots,p-1\}$. Since $p\nmid n$, these $m_b$ exponents
are distinct modulo $p$. The square matrix

$$
V_b=(c_{b,j}^{\,r})_{0\le r<m_b,\ 1\le j\le m_b}
$$

is therefore an invertible Vandermonde over $\kappa$.
For each $b$, multiply its column block in (4.1) on the right
by $V_b^{-1}$, and index the new columns by $(b,q)$,
$0\le q<m_b$. Because
$\xi^{ac_{b,j}}=\xi^{ab}$, the resulting entry equals
$\xi^{ab}\delta_{rq}$ whenever $r<m_b$.

Order all rows and columns by increasing derivative degree.
An entry with row degree $r<q$ is zero, since then $r<m_b$.
Consequently the transformed matrix is block lower triangular.
Its diagonal block of degree $r$, for $0\le r<p$, is

$$
\bigl(\xi^{ab}\bigr)_{a,b\in A_r},\qquad
A_r=\{a:m_a>r\}.                                               \tag{4.2}
$$

The set $A_r$ is an initial interval
$\{0,\ldots,t_r-1\}$, because the $m_a$'s are nonincreasing.
The matrix in (4.2) is the ordinary Vandermonde with nodes
$1,\xi,\ldots,\xi^{t_r-1}$, so it is invertible.
Empty diagonal blocks contribute determinant 1.
Every diagonal block is invertible, hence so is (4.1).

Equation (3.2) now shows

$$
P\!\left(\bigl((\xi^a)^{[m_a]}\bigr)_{a=0}^{n-1}\right)\ne0.
$$

By integrality of $P$, this proves
$v(P((\eta^i)_{i\in I'}))=0$.

## 5. Exact valuation and an archimedean bound

Only the Vandermonde in (3.1) contributes to the valuation.
Two row nodes in different residue classes modulo $n$ have
different reductions, hence their difference is a unit.
Two distinct indices in the same residue class differ by
$nq$, with $q\not\equiv0\pmod p$. The ratio of their nodes
is a primitive $p$-th root, so their difference has valuation
$1/(p-1)$ by (2.3). There are
$\sum_a\binom{m_a}{2}$ such pairs. This proves (1.2).

For completeness this also gives a crude, unconditional complex
lower bound. Write
$D_{I,J}=\det(\zeta^{ij})_{i\in I,j\in J}$.
It is a nonzero algebraic integer in $\mathbb Q(\zeta_N)$.
Its field norm is a nonzero rational integer. Every conjugate is
a $k$-by-$k$ root-of-unity matrix determinant and has modulus
at most $k^{k/2}$ by the Gram determinant/Hadamard inequality.
For $k\ge1$, therefore,

$$
|D_{I,J}|\ge
k^{-k(\varphi(N)-1)/2}.                                       \tag{5.1}
$$

No bound of this size yields the local spectral-statistics limit;
(5.1) concerns only the displayed coordinate determinant.

## 6. Application to the original seven paths

Let $N=7n$, $7\nmid n$, with $N$ odd. In the original path
coordinates

$$
x_{s,j}=h+sn+j\pmod N,\qquad h=(N+1)/2,
$$

the entries of $M_N$ factor as

$$
M_N(h+i,h+j)
 =N^{-1/2}u_i v_j\zeta_N^{cij},
\qquad c=\overline4\pmod N,                                   \tag{6.1}
$$

where $u_i,v_j$ are roots of unity. This follows directly by
expanding the specified quadratic form:
its cross term is $2\overline8\,ij=\overline4\,ij$;
every remaining term depends only on $i$, only on $j$, or is
constant. Since $c$ is invertible modulo $N$,
$\zeta_N^c$ is primitive and Theorem 1 applies.

For any prescribed count $k_s$ of selected Jacobi eigenvectors
in path $s$, take the last $k_s$ row coordinates and the first
$k_s$ column coordinates of that path. Let $M_N[I,J]$ denote
this submatrix in the path coordinates. At every extension of
the $7$-adic valuation, normalized by $v_7(7)=1$,

$$
\boxed{
v_7\det M_N[I,J]
=\frac16\sum_{a=0}^{n-1}\binom{m_a}{2}-\frac{k}{2}.
}                                                            \tag{6.2}
$$

In particular all these leading coordinate minors are nonzero.
This treats every odd $N$ with $7\Vert N$, with no restriction
on the other prime factors or their exponents.
The same factorization and (5.1) give

$$
|\det M_N[I,J]|
\ge N^{-k/2}k^{-k(\varphi(N)-1)/2}.                             \tag{6.3}
$$

## 7. First remaining leaf in the discriminant route

The frozen seven-chain checkpoint
\`research_round2_2026_10_20/arithmetic_seven_chain_discriminant_checkpoint.md\`,
SHA256
\`eee2b4caa27349a81e5cf3113d53ff1f88164e44b748c2eb99754f6e07fc6a8f\`,
expresses the relevant eigenvector-basis minor as a double
Cauchy--Binet sum. The auxiliary gauge
$\omega=(-3+4i)/5$ contributes
$\omega^{\sum j-\sum i}$, with sums of local path coordinates.
The term whose coordinate determinant is (6.2) has the unique
smallest exponent of $\omega$.

The old dominance argument, however, works at a prime above $5$,
where $v_5(\omega)=1$; at a prime above $7$, $\omega$ is a
unit. Thus nonvanishing and the valuation (6.2) do not prove
that this term dominates the sum at the prescribed $\omega$.
There is no valid operation transferring its $7$-adic valuation
to that $5$-adic place.

Indeed the separate exact calculation
\`arithmetic_endpoint_mod5_probe.py\` finds, already at $N=63$,
a four-by-four endpoint minor which reduces to zero at one
prime above $5$. This shows that a blanket assertion of
$5$-adic unit leading coefficients is false, even when
$7\Vert N$. It does not show that the exact complex minor
is zero; Theorem 1 proves the opposite.

The first unresolved assertion for this route remains:
for each required mixed set of actual Jacobi eigenvectors,
does its full overlap principal minor survive the sum over
coordinate subsets at the fixed $\omega$? It would suffice
to establish the appropriate noncancellation estimate at the
$5$-adic place, or a different argument proving nonidentity
of the actual exponential discriminant. Neither is proved here.
Consequently this note does not assert simple spectrum in the
remaining dimensions and does not establish or refute
$H_{\rm diag}$.
