> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/root_all_odd_no_algebraic_eigenvectors.md`. Embedded SHA256: `6634de7f0ccaf56270467f03401aadd66732ba704567e4b0b47ebdd6a74677e2`.
> [Thematic guide](../../topics/algebra.md).

# No projectively algebraic eigenvectors in every odd dimension except 7

Research continuation, 20 October 2026. This theorem concerns exactly the
matrices in the question, with no change to the Fourier rule, hopping phase,
or fixed parameter. It does not prove spectral statistics.

## 1. The statement

For every odd integer N >= 3, N != 7, and every nonzero algebraic complex
number z, the matrix

$$
U_N(z)=e^{izNA_N}M_N
$$

has **no projectively algebraic eigenvector**. This means that no nonzero
eigenvector can be rescaled to have all coordinates in the field of
algebraic numbers. Its eigenvalue is not assumed algebraic.

We prove the stronger auxiliary assertion

$$
E_\lambda(A_N)\cap M_N^{-1}E_\lambda(A_N)=\{0\}
\tag{1.1}
$$

for every eigenvalue lambda in every stated dimension N. For N=7n with
odd n>=9 this allows eigenspaces of dimension up to seven. In the other
dimensions A_N is simple, so absence of a common eigenvector proves
the same assertion. No quantitative bound on the angle in
(1.1), on spectral spacings, or on moments of local point counts follows.

The exception N=7 is real: A_7=(9/10)I and M_7 has an algebraic eigenbasis,
which is also an eigenbasis of U_7(z).

## 2. Inputs, gauge, and valuation

The complete preceding proof
'arithmetic_padic_jacobi_simplicity.md', SHA-256

f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df,

establishes the needed one-path estimates. Its elementary ingredients
apply to each path separately, even when 7 divides N; we give the
application in detail.

Write h=(N+1)/2, x_j=h+j modulo N, and let P send coordinate j to x_j.
Put

$$
\omega=\frac{-3+4i}{5}=\frac{1+2i}{1-2i},\qquad
D=\operatorname{diag}(\omega^j),\qquad
L=200D^*P^*A_NPD.
\tag{2.1}
$$

As an ordinary complex matrix, D is unitary. The matrix L is real symmetric,
with diagonal d_j=200V(x_j/N), and off-diagonal b_j=r((j+1)/N). The closing
edge b_(N-1) is zero. The identity x_j+h=j+1 modulo N proves the displayed
off-diagonal formula directly, including the wrap of x_j.

If N=7n, its additional zero edges are j=n-1,2n-1,...,6n-1.
Thus L is the direct sum of seven Jacobi paths, on

$$
C_s=\{sn,\ldots,(s+1)n-1\},\qquad 0\le s\le6.
\tag{2.2}
$$

Every internal edge is nonzero. The usual nonzero-edge recurrence shows
that each path has simple real spectrum and that each of its eigenvectors
has nonzero values at both endpoints. Consequently, for every eigenvalue
mu of L,

$$
d_\mu:=\dim E_\mu(L)\le7,
\tag{2.3}
$$

and E_mu has a real algebraic basis with one vector on each of its active
paths. Orthogonality of eigenvectors with distinct eigenvalues is in the
ordinary real inner product.

Choose an extension of the valuation at (1+2i), normalized by
v(1+2i)=1, to a number field containing all eigenvalues, eigenvectors,
roots of unity, and square roots used in this proof. Then v(omega)=1.
The elementary root-of-unity calculation in the preceding proof yields

$$
v(d_j)\ge0,\qquad 0\le v(b_j)\le\frac12
\tag{2.4}
$$

at every nonzero edge, also when 5 divides N. Indeed, for
eta=exp(2pi i(j+1)/N),

$$
b_j=-\frac{(\eta^7-1)^2(\eta+1)^2}{4\eta^8};
$$

eta+1 is a valuation unit because eta has odd order. If eta^7!=1,
the valuation of eta^7-1 is zero or
1/(4*5^(r-1)) for a primitive 5^r root. This proves (2.4).

The eigenvalues of every scaled path L are integral at v: their monic
characteristic polynomials have integral coefficients, and a root of
negative valuation would make the leading term uniquely dominant.

Finally, M_0=P^*M_NP has entries

$$
(M_0)_{uv}=N^{-1/2}\alpha_u\beta_v\zeta_N^{cuv},
\qquad c=\overline4\pmod N,
\tag{2.5}
$$

with alpha_u,beta_v roots of unity. They absorb the quadratic chirps.
Every k-by-k minor is N^(-k/2) times a valuation-integral number.

## 3. Endpoint bounds within a path

Here are the precise local estimates used below. On any path of length n,
normalize a real eigenvector at its first endpoint to 1. If its scaled
eigenvalue is mu, then at local position j

$$
\phi_\mu(j)=\frac{p_j(\mu)}{b_0\cdots b_{j-1}},
$$

where p_0=1, p_1=t-d_0, and

$$
p_{j+1}(t)=(t-d_j)p_j(t)-b_{j-1}^2p_{j-1}(t).
\tag{3.1}
$$

These are monic polynomials with valuation-integral coefficients.
Thus

$$
v(\phi_\mu(j)/\phi_\mu(0))\ge-j/2.
\tag{3.2}
$$

For k distinct eigenvalues in one path, the determinant of their values
at k positions is an eigenvalue Vandermonde times an integral polynomial,
divided by the product of the corresponding edge products. Alternating
polynomial division proves this identity over the valuation ring;
no division by eigenvalue differences in that ring is presumed.

At the first k consecutive positions the integral polynomial is 1.
The same recurrence run from the other endpoint therefore proves that,
if I_* is the set of the last k positions in this path and I is any
other k-position subset, then its eigenvector matrix X satisfies

$$
\det X_{I_*,E}\ne0,\qquad
v\left(\frac{\det X_{I,E}}{\det X_{I_*,E}}\right)
 \ge-\frac12\left(\sum I_*-\sum I\right).
\tag{3.3}
$$

The sums can be in global or local coordinates; their difference is the
same. Endpoint eigenvector factors cancel from the ratio. They need not
be valuation units.

## 4. A mixed minor for all N=7n, n>=9

Fix an eigenvalue mu of L and put k=d_mu. Choose its supported real
eigenvectors as columns Y_1,...,Y_k, one on each active path with distinct
indices s_1,...,s_k. Fix any one row path C_r. It contains n distinct
eigenvalues, at most one of which is mu. Since n>=9 and k<=7, choose
k real eigenvectors X_1,...,X_k in this row path, all with eigenvalues
different from mu. They are orthogonal to E_mu(L).

Consider the k-by-k matrix

$$
B=X^T D^{-1}M_0D Y.
\tag{4.1}
$$

All columns and rows are in the original transformed Hilbert space;
normalizing the real eigenvectors changes its determinant by nonzero
algebraic row and column factors only.

Twice applying Cauchy--Binet gives

$$
\det B=\sum_{I,J}
 \det X_{I,E}\,\det(M_0)_{I,J}\,\det Y_{J,F}
             \omega^{\sum J-\sum I}.
\tag{4.2}
$$

A nonzero term has I contained in the fixed row path C_r and J with
exactly one coordinate in each active column path. Define

$$
I_*=\{\text{last k positions of }C_r\},\qquad
J_*=\{s_1n,\ldots,s_kn\}.
\tag{4.3}
$$

The two eigenvector minors at these positions are nonzero.
For the Fourier minor in (2.5), the consecutive row indices I_* turn
its determinant, after unit factors, into the Vandermonde of the k roots

$$
\zeta_N^{c s_1n},\ldots,\zeta_N^{c s_kn}.
$$

Their pairwise quotients are distinct seventh roots of unity. Their
differences are valuation units at the prime over 5. Thus

$$
v\big(\det(M_0)_{I_*,J_*}\big)=-\frac{k}{2}v(N).
\tag{4.4}
$$

This remains true if 5 divides n or 7 divides n: the roots used here
are zeta_N^(cn), which have exact order 7, not zeta_N^(cn^2).
For any other Fourier minor of this size, integrality after the common
factor N^(-k/2) gives

$$
v\left(\frac{\det(M_0)_{I,J}}
               {\det(M_0)_{I_*,J_*}}\right)\ge0.
\tag{4.5}
$$

Let

$$
g_R=\sum I_*-\sum I\ge0,\qquad
g_C=\sum J-\sum J_*\ge0.
$$

The row eigenvector ratio in (4.2) has valuation at least -g_R/2,
by (3.3). The column minor is a signed product of one eigenvector
coordinate per active path, so (3.2) gives valuation at least
-g_C/2 for its ratio to the endpoint column minor. The phase ratio
has valuation g_R+g_C. The full term ratio therefore has valuation
at least

$$
(g_R+g_C)/2.
\tag{4.6}
$$

This is strictly positive except at the unique pair (I_*,J_*).
That pair is nonzero by (3.3) and (4.4). Hence it uniquely dominates
the nonarchimedean sum (4.2), which cannot vanish.

Since the chosen X rows lie in E_mu(L)^\perp, the nonzero determinant
means that D^(-1)M_0D maps E_mu injectively into those selected
orthogonal coordinates. It follows that

$$
E_\mu(L)\cap(D^{-1}M_0D)^{-1}E_\mu(L)=\{0\}.
$$

Undoing the unitary gauge and scaling proves (1.1).

## 5. The three remaining multiple-of-seven dimensions

For odd N=7n<63 other than N=7, the possibilities are N=21,35,49.
The exact finite certificates in 'root_jacobi_small_certificates.json'
show that A_N has simple spectrum in these three cases.

This check is entirely algebraic. The source
'root_jacobi_small_certificates.py' constructs the scaled seven-path
matrix from (2.1), computes each path characteristic polynomial by
(3.1), and multiplies the seven polynomials. It does so over the
following explicitly specified prime fields:

| N | p | image of zeta_N | image of i |
|---|---|---|---|
| 21 | 337 | 13 | 148 |
| 35 | 281 | 98 | 228 |
| 49 | 197 | 16 | 183 |

The program verifies primality by integer trial division, the exact
order N of the displayed root, and i^2=-1 modulo p. Since N is odd,
these choices define a homomorphism from Z[i,zeta_N,1/200] to F_p:
one can equivalently combine them into a primitive 4N-th root, because
the conductors 4 and N are coprime.

For each resulting monic characteristic polynomial P, the certificate
provides the full coefficient arrays of two polynomials U,V and verifies

$$
UP+VP'=1\quad\hbox{in }\mathbb F_p[X].
\tag{5.1}
$$

The certificate therefore proves that the reduced characteristic
polynomial has no repeated roots. Its discriminant is nonzero modulo p
and hence is not zero in characteristic zero. This proves simplicity
of the actual A_N; it is not inference from numerical eigenvalues.
The certificate also records all seven path polynomials and the full
characteristic polynomial, with ascending coefficient convention.

The checked source and data hashes are

| File | SHA-256 |
|---|---|
| root_jacobi_small_certificates.py | 4735755e1debe91ca6ab4ceaaf19d75d82ea75057d91fc3023f2ebfdaabc868b |
| root_jacobi_small_certificates.json | a61eec699954c72eee1e5ee3f786b7cb2e3f172ed07d5bf69bd0ef67d401215e |

To finish these three cases, a simple eigenvector of the direct sum L
is supported on just one of its length-n paths. If M_N also preserved
its line, then D^(-1)M_0D would map that vector into the same path.
By (2.5), its values as a function of the output coordinate u, after
removing nonzero chirp and monomial factors, are values of a nonzero
polynomial Q(zeta_N^(cu)) of degree at most n-1. Vanishing at all
6n coordinates outside that path gives 6n distinct zeros, impossible
for this polynomial. Thus there is no common A_N,M_N eigenvector.

## 6. Dimensions not divisible by seven

In these dimensions, the frozen p-adic theorem proves that A_N is simple
and every entry of M_N in its eigenbasis is nonzero. A common eigenvector
would be an A_N basis vector whose M_N image has all other coordinates
zero. Since N>=3, this contradicts the nonzero off-diagonal entries.
Thus again no common eigenvector exists.

## 7. Projective Lindemann--Weierstrass completion

Suppose that an eigenline of U_N(z_0) has an algebraic representative
v != 0, where z_0 is nonzero and algebraic. For all coordinate pairs
i,j the function

$$
F_{ij}(z)=v_i(U_N(z)v)_j-v_j(U_N(z)v)_i
\tag{7.1}
$$

vanishes at z=z_0. The matrix A_N is algebraic and Hermitian. Its distinct
eigenvalues and spectral projections are algebraic, so its exponential
is a finite sum of these projections times exponentials with algebraic
frequencies. Hence each F_ij is a finite algebraic exponential polynomial.

Collect equal frequencies. The Lindemann--Weierstrass theorem says that
exponentials of distinct algebraic numbers are linearly independent
over the algebraic numbers. The frequencies multiplied by z_0 remain
distinct algebraic numbers. Therefore every collected coefficient is
zero, and F_ij vanishes identically. The eigenvalue of U_N(z_0) never
entered this argument and is not assumed algebraic.

It follows that U_N(z)v belongs to Cv for every complex z. At z=0,
M_N v belongs to Cv and is nonzero because M_N is invertible.
Differentiating at zero gives iN A_N M_N v in Cv; thus A_N v also
belongs to Cv. This is a common eigenvector, contradicted in Sections
4--6. The theorem follows for all the stated odd dimensions.

The precise published Lindemann--Weierstrass statement is Theorem 3.2
of S. A. Popescu, A Simple and Self-contained Proof for the
Lindemann--Weierstrass Theorem, DOI 10.1007/978-3-031-51959-8_16;
the author's version is https://arxiv.org/pdf/2306.14352.
Its hypotheses are explicitly checked above.

## 8. Boundary of the result

The proof does not establish simple spectrum of U_N in every dimension
divisible by seven. The absence of a common eigenvector, by itself,
is insufficient for that stronger claim. In particular a multiple
eigenspace of U_N need not have any algebraic vector. No inference
of simplicity or of a lower bound on gaps is made from the theorem.

The conclusion covers all odd N except the genuine finite exception 7.
It supplies exact arithmetic rigidity of the eigenlines of the original
family. The required signed trace sums at times proportional to N,
already the fixed-test k=2 estimate in H_diag, remain unproved.

