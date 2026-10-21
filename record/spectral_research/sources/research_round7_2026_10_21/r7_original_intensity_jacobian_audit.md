> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round7_2026_10_21/r7_original_intensity_jacobian_audit.md`. Embedded SHA256: `bfc2e7f0a36d0354bd7c859a364f4a21f9796fe5ba6f63659fcf2773f29a620c`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/algebra.md).

# Independent audit: original intensity determinant and signed return sums

21 October 2026. The coefficient-Jacobian argument below was proposed by
the root researcher in this round. This note checks its phase placement,
valuation, algebraic specialization, and precise return-theoretic
consequences. It concerns the exact original family for odd
$N\ge3$, $7\nmid N$, at the prescribed $\tau=10^{-80}$.

The conclusion is a finite-dimensional theorem for the original
matrices. No spectral-universality estimate is asserted.

This audit checks the written parent source
`root_original_intensity_at_prescribed_phase.md` at SHA-256
`deea7755070222fdfca37d5c8f2721dc82b62afa34d56b18df614756308b5c63`.
In particular, that version displays the path-to-physical
coordinate permutation in its phase multiplier.

## 1. Frozen algebraic inputs

Use the exact one-path construction and valuation estimates proved in

`research_round2_2026_10_20/arithmetic_padic_jacobi_simplicity.md`,

SHA-256

`f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df`.

In the path ordering $x_j=(N+1)/2+j\pmod N$, write
$Q=PD\Phi R$ for an orthonormal eigenbasis of $A_N$. Here
$D_{jj}=\omega^j$, $\omega=(-3+4i)/5$, $\Phi$ is real
algebraic and diagonalizes the positive-edge real Jacobi matrix, and
$R$ is the nonzero algebraic diagonal normalization. At the place
$v_+$ over $1+2i$, $v_+(\omega)=1$.

For a fixed $k$-element eigenvalue set $E$, Cauchy--Binet
expansion of $\det(Q_E^*M_NQ_E)$ has a unique term of smallest
valuation. Its coordinate row and column sets are

$$
I_k=\{N-k,\ldots,N-1\},\qquad
J_k=\{0,\ldots,k-1\}.
\tag{1.1}
$$

This term is nonzero. Dividing any different nonzero term by it
gives valuation at least

$$
\frac12\left(\sum I_k-\sum I+\sum J-\sum J_k\right)>0.
\tag{1.2}
$$

The normalization factors in $R$ are common to all these terms
and cancel in (1.2). The proof includes arbitrary powers of 5
dividing $N$. It is the full termwise valuation statement, not
just the nonvanishing of the resulting minor, that is needed below.

The same frozen source proves that $A_N$ is simple and that
$U_N(z)$ is simple for every nonzero algebraic $z$. These
inputs are used only in the dimensions $7\nmid N$, where they
were proved.

## 2. Right diagonal phases and the algebraic derivative matrix

Let $Z=\operatorname{diag}(z_0,\ldots,z_{N-1})$ in the path
coordinate ordering and put $\mathscr Z=PZP^*$, the same
multiplier in physical coordinates. Order the eigenvalues of $A_N$ decreasingly
as $a_1>\cdots>a_N$, and let $E_k$ be the first $k$ of these
eigenvectors. Define

$$
b_k(Z)=\det(Q_{E_k}^*M_N\mathscr ZQ_{E_k}),\qquad b_k=b_k(I).
\tag{2.1}
$$

The right placement of $Z$ matters. In the gauge basis the matrix
in (2.1) contains

$$
\Phi_{E_k}^T D^{-1}M_0ZD\Phi_{E_k},\qquad M_0=P^*M_NP.
$$

Thus, in its double Cauchy--Binet expansion, the term indexed by
$I,J$ is the old term multiplied by
$z_J=\prod_{j\in J}z_j$. No row-index factor $z_I$ appears.
Let $T_{I,J}$ denote the original term, including its sign, and
$T_k=T_{I_k,J_k}$. Then

$$
b_k=\sum_{I,J}T_{I,J}=T_k(1+\eta_k),\qquad v_+(\eta_k)>0,
\tag{2.2}
$$

and

$$
\frac{\partial_{z_v}b_k(Z)|_{Z=I}}{b_k}-\mathbf1_{v<k}
=\frac{\sum_{I,J}
(\mathbf1_{v\in J}-\mathbf1_{v\in J_k})T_{I,J}}{b_k}.
\tag{2.3}
$$

The extreme term has coefficient zero in the numerator. Every
remaining term, after division by $b_k$, has positive valuation
by (1.2) and (2.2). Therefore the algebraic matrix

$$
L_{k,v}=b_k^{-1}\partial_{z_v}b_k(Z)|_{Z=I},
\qquad 1\le k\le N,\quad0\le v<N,
\tag{2.4}
$$

reduces in the residue field to the matrix

$$
H_{k,v}=\mathbf1_{v<k}.
\tag{2.5}
$$

With the displayed orders of rows and columns, $H$ is lower
triangular with diagonal entries 1. Hence

$$
v_+(\det L)=0,\qquad
\det\big[\partial_{z_v}b_k(Z)|_{Z=I}\big]
=\Big(\prod_{k=1}^N b_k\Big)\det L\ne0.
\tag{2.6}
$$

The last row $k=N$ is consistent: it is exactly the row of ones
after division by $b_N=\det M_N$. This also checks that no
determinant/global-phase direction was accidentally removed.

## 3. Large real time and specialization to the fixed original parameter

For complex $s$, let

$$
c_k(s,Z)=e_k(e^{sA_N}M_N\mathscr Z),
\qquad
\mathcal J(s)=\det\big[\partial_{z_v}c_k(s,Z)|_{Z=I}\big].
\tag{3.1}
$$

In the $A_N$-basis, the exact exterior expansion gives

$$
c_k(s,Z)=\sum_{|E|=k}
e^{s\sum_{i\in E}a_i}\det(Q_E^*M_N\mathscr ZQ_E).
\tag{3.2}
$$

For positive real $s\to\infty$, the set $E_k$ uniquely maximizes
$\sum_{i\in E}a_i$, since the $a_i$ are distinct. Differentiating
(3.2) with respect to one $z_v$ does not change these exponents.
Consequently

$$
e^{-s\sum_{i=1}^k a_i}
\partial_{z_v}c_k(s,Z)|_{Z=I}
\longrightarrow\partial_{z_v}b_k(Z)|_{Z=I}.
\tag{3.3}
$$

After all rows are normalized as in (3.3), the determinant tends
to the nonzero number in (2.6). Therefore $\mathcal J$ is not
identically zero.

All spectral projections of the algebraic Hermitian matrix
$A_N$ are algebraic. Equations (3.1)--(3.2) show that
$\mathcal J(s)$ is a finite exponential polynomial with algebraic
coefficients and frequencies. Collect equal frequencies. There
remains a nonzero coefficient because $\mathcal J\not\equiv0$.
At

$$
s_0=iN\tau\ne0,
$$

all the distinct exponents are distinct algebraic numbers.
Lindemann--Weierstrass therefore gives

$$
\boxed{\mathcal J(iN\tau)\ne0.}
\tag{3.4}
$$

The exact theorem used is S. A. Popescu, Theorem 3.2,
*A Simple and Self-contained Proof for the Lindemann--Weierstrass
Theorem*, DOI `10.1007/978-3-031-51959-8_16`; its author version is
<https://arxiv.org/pdf/2306.14352>. The displayed theorem at PDF
page 14 states linear independence over the algebraic numbers of
exponentials of distinct algebraic numbers. This statement was
reopened and checked in the current audit. No rational independence
of the frequencies is required.

The same argument works with $\tau$ replaced by any nonzero real
algebraic parameter. In this note it is applied to the fixed
parameter in the question.

## 4. The original eigenvector intensity matrix is invertible

Let $\psi_1,\ldots,\psi_N$ be an orthonormal eigenbasis of the
original $U_N$, with distinct eigenvalues $\lambda_j$. Define
the real matrix, with coordinate rows and eigenvector columns,

$$
\mathsf A_{v,j}=|\psi_j(x_v)|^2.
\tag{4.1}
$$

The simple eigenvalues of $U_N\mathscr Z$ are analytic near $Z=I$.
At that point the left eigenvector is $\psi_j^*$, so

$$
\partial_{z_v}\lambda_j(Z)|_{Z=I}
=\psi_j^*U_NE_v\psi_j
=\lambda_j\mathsf A_{v,j}.
\tag{4.2}
$$

Here $E_v$ is the physical coordinate projection. This is a
derivative with respect to the complex multiplier $z_v$; a
derivative with respect to its argument would have one additional
factor $i$.

The Jacobian from eigenvalues to elementary symmetric functions
has entries

$$
\frac{\partial e_k}{\partial\lambda_j}
=e_{k-1}(\lambda_1,\ldots,\widehat{\lambda_j},\ldots,\lambda_N)
$$

and determinant $\prod_{i<j}(\lambda_i-\lambda_j)$. One can
verify this by regarding the determinant as an alternating
polynomial of the requisite total degree and checking the leading
Vandermonde coefficient. It is nonzero here. Taking determinants
in the chain rule for (4.2) gives

$$
\mathcal J(iN\tau)
=\left(\prod_{j=1}^N\lambda_j\right)
\left(\prod_{i<j}(\lambda_i-\lambda_j)\right)
\det\mathsf A.
\tag{4.3}
$$

All factors except the last are already nonzero, and (3.4) proves

$$
\boxed{\det\mathsf A\ne0.}
\tag{4.4}
$$

This does not say that each individual intensity is nonzero.
Invertibility of a matrix of intensities and full coordinate
support are distinct assertions.

## 5. Exactly what is removed from the doubled dark space

Use the unnormalized Hilbert--Schmidt inner product on matrices,
so that $E_v=|x_v\rangle\langle x_v|$ is an orthonormal basis
of the diagonal subspace. Let

$$
W(X)=U_N XU_N^*,\qquad P(X)=\operatorname{diag}X,\qquad O=I-P.
$$

Because $U_N$ is simple,
$\ker(W-I)$ has the orthonormal basis
$P_j=|\psi_j\rangle\langle\psi_j|$, $1\le j\le N$.
The matrix of the restriction $P|_{\ker(W-I)}$ in these bases is
precisely $\mathsf A$. Thus (4.4) proves that this restriction
is an isomorphism. In particular,

$$
\ker(W-I)\cap\ker P=\{0\}.
\tag{5.1}
$$

Write $S=OWO$ on $\operatorname{ran}O$. If $Sy=y$,
$\|Wy\|=\|y\|=\|OWy\|$ forces $PWy=0$, and hence
$Wy=y$. Then (5.1) implies $y=0$. Therefore

$$
\boxed{1\notin\operatorname{spec}S.}
\tag{5.2}
$$

This excludes the stationary doubled dark directions. It does not
exclude dark eigenvectors of $W$ with another unit-modulus
eigenvalue. Repeated nontrivial ratios of eigenvalues of $U_N$
are not excluded by (4.4).

## 6. Two exact signed sums of the original first-return amplitudes

In the decomposition $\operatorname{ran}P\oplus\operatorname{ran}O$,
write

$$
W=\begin{pmatrix}D&B\\ C&S\end{pmatrix},\qquad
R=(I-S)^{-1}.
\tag{6.1}
$$

The inverse exists by (5.2). Define the exact transfer function

$$
F(z)=zD+z^2B(I-zS)^{-1}C
=\sum_{r\ge1}z^rF_r,
\quad
F_1=D,\quad F_r=BS^{r-2}C\ (r\ge2).
\tag{6.2}
$$

For every $p\in\operatorname{ran}P$, the isomorphism in Section 5
gives a unique stationary extension $Xp\in\ker(W-I)$ with
$PXp=p$. The second block equation forces

$$
Xp=\begin{pmatrix}p\\RCp\end{pmatrix}.
\tag{6.3}
$$

The first block equation then gives

$$
\boxed{F(1)=D+BRC=I_N.}
\tag{6.4}
$$

Because $W$ is unitary, $WX=X$ also implies $W^*X=X$.
The second block of the latter equality yields

$$
B^*=(I-S^*)RC,\qquad B=C^*R^*(I-S).
\tag{6.5}
$$

Differentiate (6.2) at 1. Using (6.4),
$R+RSR=R^2$, and (6.5), one obtains

$$
F'(1)=D+2BRC+BRSRC
=I+BR^2C
=I+C^*R^*RC
=X^*X.
\tag{6.6}
$$

If $E:\mathbb C^N\to\ker(W-I)$ is the isometry with columns
$P_j$, then $PE=\mathsf A$ and $X=E\mathsf A^{-1}$.
Consequently

$$
\boxed{F'(1)=(\mathsf A\mathsf A^*)^{-1}.}
\tag{6.7}
$$

The series (6.2) and its first derivative converge absolutely at
$z=1$, even if $S$ has dark eigenvalues on the rest of the
unit circle. Here is a direct verification. If $Sv=\gamma v$
with $|\gamma|=1$, then $\|Sv\|=\|v\|$. Positivity of
$I-S^*S$ forces $S^*Sv=v$, and hence
$S^*v=\overline\gamma v$. Thus its eigenspace is reducing
for $S$. Remove all such eigenspaces; their orthogonal direct
sum is a reducing unitary subspace $\mathcal H_u$, and the
restriction $S_b$ to its orthogonal complement has all
eigenvalues strictly inside the unit circle. There are no
additional peripheral Jordan vectors: either reducing removes
them directly, or their polynomially growing powers would
contradict $\|S^m\|\le1$.

The block-unitarity identities
$B^*B+S^*S=I$ and $CC^*+SS^*=I$ imply
$B|_{\mathcal H_u}=0$ and
$\operatorname{ran}C\perp\mathcal H_u$. Thus every
$BS^mC$ uses only $S_b$. For any
$\rho(S_b)<q<1$, its Jordan form gives
$\|S_b^m\|\le C_q q^m$, with a finite constant depending
on the fixed matrix. Both the series and its first derivative
therefore converge absolutely at 1. Consequently (6.4) and
(6.7) are the actual signed identities

$$
\boxed{\sum_{r\ge1}F_r=I_N,\qquad
\sum_{r\ge1}rF_r=(\mathsf A\mathsf A^*)^{-1}.}
\tag{6.8}
$$

The convention for $F_r$ agrees with the round-6 exact first
return amplitudes. The absolute-convergence and derivative
calculation were also checked independently by the round-7
long-return researcher.

## 7. The first remaining gaps

The argument above uses the one-path valuation theorem. It does
not establish (4.4) in dimensions divisible by 7. In those
dimensions, separate simple Jacobi paths do not automatically
give the required mixed minors or the unique largest exterior
frequency used in (3.3).

Even in the dimensions covered, (6.8) gives no bound on
$\|\mathsf A^{-1}\|$, on approach to the boundary uniformly in
$N$, or on signed weighted coefficients at return times
comparable to $N$. The asymptotic pair sum in the main ledger
therefore remains unproved. These identities cannot be
substituted for that estimate.

Finally, generic phase nonresonance cannot be substituted for
original nonresonance. Full support, a nonsingular intensity
matrix, and transcendence of every individual eigenvalue ratio
still do not in general rule out equality of two such ratios or
dark linear combinations inside that common-ratio eigenspace.

