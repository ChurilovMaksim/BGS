> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round7_2026_10_21/root_original_intensity_at_prescribed_phase.md`. Embedded SHA256: `deea7755070222fdfca37d5c8f2721dc82b62afa34d56b18df614756308b5c63`.
> [Thematic guide](../../topics/algebra.md).

# Nonsingular eigenvector intensities at the prescribed original phase

Research continuation, 21 October 2026. This note proves a new
finite-dimensional statement for the **original** matrices, for every
odd $N\ge3$ with $7\nmid N$. The parameter in its application
is exactly $\tau=10^{-80}$. There is no averaging over phases or
dimensions and no replacement of the original matrices.

The conclusion strengthens the previous assertion about almost every
auxiliary coordinate phase: the intensity Jacobian is now proved
nonsingular at the original phase itself in these dimensions. It
does not prove the signed trace estimate required by
$H_{\rm diag}$, and it supplies no lower bound uniform in $N$
for the least singular value of the intensity matrix.

## 1. Statements

Set
$$
U_N(z)=e^{izNA_N}M_N,\qquad
Z=\operatorname{diag}(z_0,\ldots,z_{N-1}),
$$
where the coordinates are ordered along the Jacobi path
$x_j=(N+1)/2+j\pmod N$. Let $P$ map this ordering to the
original coordinate ordering and put $\mathscr Z=PZP^*$.
Define the coefficient Jacobian
$$
\mathcal J_N(z)=
\left[
 \left.\frac{\partial}{\partial z_v}
       e_k(U_N(z)\mathscr Z)\right|_{Z=I}
\right]_{1\le k\le N,\ 0\le v<N}.
\tag{1.1}
$$
Here $e_k$ is the elementary symmetric polynomial of the matrix
eigenvalues, equivalently the sum of its principal minors of size
$k$. The variables $z_v$ in $Z$ are independent complex
variables; the scalar $z$ in $U_N(z)$ is a different variable.

**Theorem 1.** For every nonzero algebraic complex $z$,
$$
\det\mathcal J_N(z)\ne0.
\tag{1.2}
$$

**Theorem 2.** If $z$ is nonzero, real and algebraic, let
$\psi_1,\ldots,\psi_N$ be an orthonormal eigenbasis of
$U_N(z)$. Its spectrum is simple, as established in the input
proof recalled below. Then
$$
\boxed{
\det\left[|\psi_j(x_v)|^2\right]_{1\le j\le N,\ 0\le v<N}\ne0.
}
\tag{1.3}
$$
In particular (1.3) holds for the original $z=10^{-80}$.

The eigenvectors can be reordered or multiplied by unit phases;
neither operation changes the asserted nonvanishing. Permuting back
to the original order of coordinates also preserves nonvanishing.

**Corollary 3.** For these original dimensions,
$$
\{X:U_NX=XU_N,\ \operatorname{diag}X=0\}=\{0\}.
\tag{1.4}
$$
Equivalently, the stationary eigenspace of
$U_N\otimes\overline{U_N}$ contains no nonzero vector orthogonal
to the coordinate diagonal. This asserts the stationary eigenspace
only; it is not a proof that all nonstationary dark modes are absent.

## 2. Exact inputs and why they apply

The underlying Jacobi and valuation proof is included in the same
cumulative document as
`research_round2_2026_10_20/arithmetic_padic_jacobi_simplicity.md`,
SHA256
`f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df`.
The needed estimates are reproduced here with their derivations,
including the ramified case $5\mid N$.

Put $\omega=(-3+4i)/5=(1+2i)/(1-2i)$, let $P$ be the path
permutation, and let $D=\operatorname{diag}(\omega^j)$. Directly
from the modular-half Weyl rule,
$$
L=200D^{-1}P^*A_NPD
\tag{2.1}
$$
is a real symmetric Jacobi path, with diagonal
$d_j=200V(x_j/N)$ and internal edges
$b_j=r((j+1)/N)>0$, $0\le j<N-1$. Its closing edge is zero.
Indeed $r(y/N)=0$ on an odd grid exactly when $N\mid7y$.
The condition $7\nmid N$ therefore makes the path connected.
An eigenvector is determined by its first entry by the three-term
recurrence; a zero first entry forces all entries to vanish. Each
eigenspace has dimension one, and real symmetry gives a simple
spectrum.

Choose a valuation $v$ on a number field containing the finite
set of algebraic quantities in the proof, extending the prime
$(1+2i)$ of $\mathbb Q(i)$, normalized by $v(5)=1$.
Then $v(\omega)=1$. The extension can be obtained by embedding
the algebraic numbers under consideration in an algebraic closure
of the completion at that prime. Set
$\mathfrak o=\{a:v(a)\ge0\}$ and
$\mathfrak m=\{a:v(a)>0\}$.

All roots of unity are valuation units. For a primitive root of
order $5^a$,
$$
v(1-\zeta_{5^a})=\frac1{4\cdot5^{a-1}}.
\tag{2.2}
$$
To verify this, the reduction of such a root is one, while
$(1-\zeta^j)/(1-\zeta)$ is a unit for $5\nmid j$.
The product of these $4\cdot5^{a-1}$ equal-valuation factors is
$\Phi_{5^a}(1)=5$. A root of unity of order prime to five
cannot reduce to one unless it equals one: the lowest-valuation
term of $(1+u)^d-1$, $5\nmid d$, would otherwise be
$du$. Separating prime-to-five and five-power parts proves
that $v(1-\eta)>0$ only when the order of $\eta$ is a
power of five.

The factorization
$$
r(y/N)=-\frac{(\eta^7-1)^2(\eta+1)^2}{4\eta^8},
\qquad \eta=e_N(y),
\tag{2.3}
$$
shows that every nonzero internal edge has
$0\le v(b_j)\le1/2$. An odd-order root cannot reduce to
$-1$, so $1+\eta$ is a unit. Also $v(d_j)\ge0$:
the expression
$200V=200\cos(14\pi q)+20r+2r\sin(2\pi q)-20$
has only unit denominators at this place. These assertions do not
require $5\nmid N$.

Let $\Phi$ be the matrix of real algebraic eigenvectors of
$L$, initially normalized at the first coordinate. The monic
recurrence gives
$$
\Phi_{j,i}=p_j(\mu_i)/\beta_j,\qquad
\beta_j=\prod_{a<j}b_a,
$$
$$
p_0=1,\quad p_1(X)=X-d_0,\quad
p_{j+1}(X)=(X-d_j)p_j(X)-b_{j-1}^2p_{j-1}(X).
\tag{2.4}
$$
The eigenvalues $\mu_i$ and all coefficients of the monic
$p_j$ are in $\mathfrak o$. Dividing an alternating
polynomial in the $\mu_i$'s by their Vandermonde preserves
integrality: it follows either from successive monic division or
from the integer Schur-polynomial expansion of a monomial alternant.
The consecutive initial minor has quotient one. Applying the same
argument from the opposite endpoint gives, for any $k$-element
eigenvalue set $E$,
$$
v\left(\frac{\det\Phi_{J,E}}
                  {\det\Phi_{J_k,E}}\right)
\ge-\frac12\left(\sum J-\sum J_k\right),
\qquad J_k=\{0,\ldots,k-1\},
\tag{2.5}
$$
$$
v\left(\frac{\det\Phi_{I,E}}
                  {\det\Phi_{I_k,E}}\right)
\ge-\frac12\left(\sum I_k-\sum I\right),
\qquad I_k=\{N-k,\ldots,N-1\}.
\tag{2.6}
$$
Both denominators are nonzero. Normalizing the eigenvectors in
Euclidean norm multiplies every minor on either side by common
nonzero algebraic factors, which cancel in these ratios.

For $M_0=P^*M_NP$, the explicit kernel is
$$
(M_0)_{ij}=N^{-1/2}u_i v_j\zeta_N^{\overline4\,ij},
\tag{2.7}
$$
with root-of-unity factors $u_i,v_j$ and primitive Fourier
multiplier $\overline4$ modulo $N$. Every Fourier minor
is a row Vandermonde times an integral Schur polynomial. Consecutive
columns make the latter a unit monomial. The row Vandermonde has
least valuation for consecutive rows. To check this last point
without an unramified assumption, write $N=5^e n$, $5\nmid n$.
If $e\ge1$, its valuation is exactly
$$
\frac{C_n(I)}{4\cdot5^{e-1}}
+\sum_{a=1}^{e-1}5^{a-e}C_{n5^a}(I),
\quad
C_d(I)=\sum_{r\bmod d}\binom{|I\cap(r+d\mathbb Z)|}{2}.
\tag{2.8}
$$
This follows by summing (2.2) over differences of row indices;
the weights in (2.8) are the successive increments of their
possible valuations. For each divisor $d$, the pair count
$C_d$ is minimized when its occupancies differ by at most one.
Consecutive sets have this property for every divisor at once.
If $e=0$, every distinct root difference is a unit. Hence in
all cases
$$
v\left(\frac{\det(M_0)_{I,J}}
                  {\det(M_0)_{I_k,J_k}}\right)\ge0.
\tag{2.9}
$$
The denominator is nonzero. The factor $N^{-k/2}$ cancels
in the ratio even when five divides $N$.

## 3. The dominant coordinate monomial

Let $Q=P D\widehat\Phi$ be the orthonormal eigenvector matrix
of $A_N$, ordered by strictly decreasing eigenvalues
$a_1>\cdots>a_N$. The normalization of $\widehat\Phi$
does not change (2.5)–(2.6). In this section $Z$ is written
in path order. For $E_k=\{1,\ldots,k\}$, set
$$
b_k(Z)=\det\bigl(Q_{E_k}^*M_N(PZP^*)Q_{E_k}\bigr).
\tag{3.1}
$$
The coordinate permutation is displayed explicitly here; equivalently
one can work throughout in path coordinates and omit both $P$'s.

Two applications of Cauchy–Binet give
$$
b_k(Z)=\sum_{|I|=|J|=k}c_{k,I,J}
                         \prod_{j\in J}z_j,
\tag{3.2}
$$
where, up to a common nonzero eigenvector-normalization factor,
$$
c_{k,I,J}=
\det\Phi_{I,E_k}\det(M_0)_{I,J}\det\Phi_{J,E_k}
                   \omega^{\sum J-\sum I}.
\tag{3.3}
$$
The factor in (3.2) is indexed by $J$, the **column** coordinates
of the Fourier minor. This is why the right phase multiplication
$M_NZ$ must be tracked explicitly.

The coefficient $c_{k,I_k,J_k}$ is nonzero. For any other
nonzero coefficient, put
$$
g=(\sum I_k-\sum I)+(\sum J-\sum J_k)>0.
$$
It is a positive integer. Equations (2.5), (2.6), (2.9) and
$v(\omega)=1$ imply
$$
v(c_{k,I,J}/c_{k,I_k,J_k})\ge g/2>0.
\tag{3.4}
$$
Therefore the polynomial $b_k(Z)/c_{k,I_k,J_k}$ has coefficients
in $\mathfrak o$, and its reduction modulo $\mathfrak m$
is the single monomial
$$
\frac{b_k(Z)}{c_{k,I_k,J_k}}
\equiv z_0z_1\cdots z_{k-1}\pmod{\mathfrak m}.
\tag{3.5}
$$
This also proves $b_k(I)\ne0$.

Differentiate before specializing to $Z=I$. Since each monomial
in (3.2) has exponents zero or one, differentiation preserves its
coefficient's positive valuation or kills it. Dividing by the unit
$b_k(I)/c_{k,I_k,J_k}$, (3.5) gives
$$
L_{kv}:=
\frac{\partial_{z_v}b_k(I)}{b_k(I)}
\equiv\mathbf1_{\{v<k\}}\pmod{\mathfrak m}.
\tag{3.6}
$$
The $N$-by-$N$ matrix on the right has ones on and below
its main diagonal and zeros above it (with row $k$ paired to
column $v=k-1$). Its determinant is one. Thus
$$
\det L\equiv1\pmod{\mathfrak m},\qquad
\det[\partial_{z_v}b_k(I)]
=\left(\prod_{k=1}^N b_k(I)\right)\det L\ne0.
\tag{3.7}
$$
This proves a nonzero determinant, without any Archimedean lower
bound and without selecting a generic coordinate phase.

## 4. Passing through large real time to a nonzero exponential polynomial

Temporarily set $W(s)=e^{sA_N}M_N$, with $s\in\mathbb C$.
In the $A_N$-basis, $e^{sA_N}$ is diagonal. The principal-minor
formula therefore gives the exact expansion
$$
e_k(W(s)\mathscr Z)=
\sum_{|E|=k}
e^{s\sum_{j\in E}a_j}
\det\bigl(Q_E^*M_N\mathscr Z Q_E\bigr),
\tag{4.1}
$$
where $\mathscr Z=PZP^*$ is the physical coordinate multiplier.
Because the $a_j$ are strictly decreasing, the exponent
has a unique largest real value
$A_k=a_1+\cdots+a_k$, attained at $E_k$.

Differentiating the finite sum in the coordinate phase and letting
real $s\to+\infty$,
$$
e^{-sA_k}
\left.\partial_{z_v}e_k(W(s)\mathscr Z)\right|_{Z=I}
\longrightarrow\partial_{z_v}b_k(I).
\tag{4.2}
$$
Taking the determinant of this fixed-size matrix gives
$$
e^{-s\sum_k A_k}
\det\left[\left.\partial_{z_v}e_k(W(s)\mathscr Z)\right|_{Z=I}\right]
\longrightarrow\det[\partial_{z_v}b_k(I)]\ne0.
\tag{4.3}
$$
In particular, the determinant on the left before normalization
is not identically zero as a function of $s$.

It is a finite exponential polynomial: $A_N,M_N,Q$ are
algebraic, (4.1) is finite, and determinants and derivatives use
only finite sums and products. After equal frequencies are
collected, it has the form
$$
F(s)=\sum_{\beta\in\mathcal F}d_\beta e^{s\beta},
\qquad d_\beta\in\overline{\mathbb Q}\setminus\{0\},
\quad \beta\in\overline{\mathbb Q},
\tag{4.4}
$$
with pairwise distinct frequencies and a nonempty finite set
$\mathcal F$. At every nonzero algebraic $s$, the numbers
$s\beta$ remain distinct and algebraic.

Apply the qualitative Lindemann–Weierstrass theorem in
Cheng-Chao Huang, *Explicit Bounds for Linear Forms in the
Exponentials of Algebraic Numbers*, ISSAC 2022, Theorem 1.1,
DOI <https://doi.org/10.1145/3476446.3536170>;
the author version is
<https://arxiv.org/pdf/2112.05004v2>, page 1, dated 16 May 2022.
The exact theorem was opened and its hypotheses checked on
21 October 2026. It asserts nonvanishing of an algebraic linear
combination of exponentials of distinct algebraic numbers, when
all coefficients are nonzero. These are precisely the conditions
in (4.4). Thus $F(iNz)\ne0$ for every nonzero algebraic $z$,
which is Theorem 1. This use of transcendence is qualitative only.

## 5. Identifying the Jacobian with the intensity matrix

For completeness, the same nonzero $b_k(I)$'s also verify the
previous simple-spectrum argument. The characteristic polynomial
of $e^{sA_N}M_N$, on the scale $X=e^{sa_k}Y$ as real
$s\to+\infty$, has only its $(k-1)$-st and $k$-th
coefficient terms at the maximal scale. Their nonzero root is
$Y=b_k(I)/b_{k-1}(I)$, $b_0=1$. On a sufficiently small
circle around this point the remaining finitely many terms
decay exponentially. Rouché's theorem yields one simple root
there for large $s$. The $N$ scales are disjoint because
the $a_k$'s differ. The discriminant is consequently a nonzero
finite algebraic exponential polynomial. Applying the same
Lindemann–Weierstrass theorem proves simple spectrum at every
nonzero algebraic $iNz$, including the real-unitary case.

Now suppose $z$ is real and algebraic and nonzero. Write
$U_N(z)\psi_j=\lambda_j\psi_j$, with an orthonormal basis.
Simple eigenvalues have differentiable local branches under
right coordinate phases. At $Z=I$, differentiating the
eigenvalue equation and multiplying by $\psi_j^*$ gives
$$
\partial_{z_v}\lambda_j(U_N(z)\mathscr Z)
=\psi_j^*U_N(z)E_v\psi_j
=\lambda_j|\psi_j(x_v)|^2.
\tag{5.1}
$$
Here normality ensures $\psi_j^*U_N(z)=\lambda_j\psi_j^*$,
and $E_v$ is the coordinate rank-one projection.

Set $B_{jv}=|\psi_j(x_v)|^2$ and
$E_{kj}=e_{k-1}(\lambda_1,\ldots,\widehat{\lambda_j},\ldots,
\lambda_N)$. The chain rule gives
$$
\mathcal J_N(z)=E\,\operatorname{diag}(\lambda_1,\ldots,\lambda_N)B.
\tag{5.2}
$$
The matrix $E$ is nonsingular when the $\lambda_j$'s are
distinct. Indeed its columns, with the alternating coefficient
signs restored, are the coefficient vectors of
$\prod_{i\ne j}(X-\lambda_i)$. A linear relation among
these polynomials, evaluated at $X=\lambda_j$, makes its
$j$-th coefficient zero. Each $\lambda_j$ is nonzero by
unitarity. Theorem 1 and (5.2) therefore imply $\det B\ne0$,
proving Theorem 2.

Using real phases $z_v=e^{i\phi_v}$ and eigenphases
$\lambda_j=e^{i\vartheta_j}$, the same calculation gives
$$
\left.\frac{\partial\vartheta_j}{\partial\phi_v}\right|_{\phi=0}
=B_{jv}.
\tag{5.3}
$$
Thus the real phase-to-eigenphase map is locally invertible at
the prescribed original matrix, up to the choice of local labels
and real lifts of the simple eigenangles.

## 6. What this proves about stationary observation

Every commuting matrix has the form
$X=\sum_j c_j\psi_j\psi_j^*$, since the spectrum is simple.
Its coordinate diagonal is $B^Tc$. Invertibility of $B$
proves (1.4). Equivalently, the dephasing map
$$
D\longmapsto\sum_j(\psi_j^*D\psi_j)\psi_j\psi_j^*
\tag{6.1}
$$
maps the $N$-dimensional space of coordinate diagonal matrices
isomorphically onto the $N$-dimensional commutant of $U_N$.
No bound on the inverse in (6.1) is obtained.

There is also a directly observable equivalent consequence:
$$
\det\left[(U_N^n)_{x_vx_v}\right]_{
                      0\le n<N,\ 0\le v<N}\ne0.
\tag{6.2}
$$
The matrix in (6.2) is the distinct-eigenvalue Vandermonde
$[\lambda_j^n]$ times $B$. Both factors are invertible.

## 7. Precise remaining limitations

The hypothesis $7\nmid N$ was used to obtain one connected
Jacobi path and a simple $A_N$. The proof does not cover the
seven-path case $7\mid N$.

The theorem rules out the stationary dark subspace. If distinct
ordered pairs have the same nontrivial ratio
$\lambda_j/\lambda_k$, their corresponding eigenoperators
can have linear combinations with zero coordinate diagonal.
Nothing in (1.3) alone excludes that possibility. A proof about
all of $U_N\otimes\overline{U_N}$ still needs control of these
ratio eigenspaces.

Most importantly, an exact nonzero determinant gives no
quantitative phase cancellation or integrability bound at times
of order $N$. The companion countermodel shows explicitly
that a nonsingular intensity matrix, even combined with several
other qualitative spectral properties, can coexist with a
divergent fixed pair statistic in a different family. The first
unproved original weighted trace estimate remains unchanged.
