> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_endpoint_cyclicity.md`. Embedded SHA256: `387243de3e23f5df546c999ef2d650a640e6b7c4d4488ea775765e3ae5362868`.
> [Thematic guide](../../topics/algebra.md).

# Exact endpoint cyclicity and complete visibility of a local detector

20 October 2026. The matrices, modular half phases, and fixed parameter
tau=10^(-80) are exactly those in the question.

## 1. The result

Let

$$
U_N(z)=e^{izNA_N}M_N,
\qquad x_+=(N+1)/2,\quad x_-=(N-1)/2\pmod N.
$$

**Theorem.** If N>=3 is odd and 7 does not divide N, then, for
every nonzero algebraic complex z, each of the two coordinate
vectors e_(x_+), e_(x_-) is both observable and cyclic for U_N(z):

$$
\det\begin{pmatrix}
e_x^*\\ e_x^*U_N(z)\\ \vdots\\ e_x^*U_N(z)^{N-1}
\end{pmatrix}\ne0,
\qquad
\det[e_x,U_N(z)e_x,\ldots,U_N(z)^{N-1}e_x]\ne0.
\tag{1.1}
$$

In particular, every nonzero eigenvector of U_N(z) has nonzero
coordinates at both x_+ and x_-. For the actual real parameter tau,
any positive detector E whose range contains either coordinate
vector has full visible space under U_N(tau).

The theorem asserts these two coordinates. It does not assert
nonvanishing at every interior coordinate of the Jacobi path. It
also does not give a quantitative lower bound on the endpoint
coordinates or on the detector's escape rate.

## 2. Verified input and conventions

The input `arithmetic_padic_jacobi_simplicity.md`, SHA-256
`f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df`,
is used without modification. Its Sections 2--6 explicitly prove
the following facts, including dimensions divisible by powers of 5.

Write omega=(-3+4i)/5. Order the coordinates by
x_j=x_++j mod N, 0<=j<N, and put D=diag(omega^j). If P is this
coordinate permutation, then

$$
L=200D^*P^*A_NPD
$$

is a real symmetric Jacobi path with positive internal edges b_j.
Its eigenvalues are simple. Choose real eigenvectors phi_i and let
Phi be their coordinate matrix. Every eigenvector is nonzero at
both path endpoints.

At a valuation v_+ extending the prime (1+2i), normalized by
v_+(5)=1, one has v_+(omega)=1 and

$$
v_+(d_j)\ge0,\qquad 0\le v_+(b_j)\le1/2.
\tag{2.1}
$$

The same diagonal and edge bounds hold for a valuation v_-
extending (1-2i), with v_-(omega)=-1. Indeed the proof uses only
integrality of d_j and the factorization

$$
r(y/N)=-\frac{(\eta^7-1)^2(\eta+1)^2}{4\eta^8},
\qquad \eta=e^{2\pi iy/N},
$$

and the root-of-unity valuation
v(1-eta)=1/(4*5^(a-1)) when eta is primitive of order 5^a.
These statements hold at either of the two places.

For a coordinate subset I of size l, and any l-element eigenvalue
set F, the initial and final contiguous coordinate minors are
nonzero. At either valuation,

$$
v\!\left(\frac{\det\Phi_{I,F}}
 {\det\Phi_{\{0,\ldots,l-1\},F}}\right)
\ge-\frac12\left(\sum I-\frac{l(l-1)}2\right),
\tag{2.2}
$$

$$
v\!\left(\frac{\det\Phi_{I,F}}
 {\det\Phi_{\{N-l,\ldots,N-1\},F}}\right)
\ge-\frac12\left(\sum_{j=N-l}^{N-1}j-\sum I\right).
\tag{2.3}
$$

These follow from the monic Jacobi recurrence and integral
Vandermonde division; no endpoint coordinate is assumed to be a
valuation unit.

Set M_0=P^*M_NP. Its entries are

$$
(M_0)_{ij}=N^{-1/2}u_i v_j\zeta_N^{\bar4ij},
\tag{2.4}
$$

where u_i,v_j are roots of unity. If I_0,J_0 are any intervals of
l consecutive coordinate indices, then

$$
\det(M_0)_{I_0,J_0}\ne0,
\qquad
v\!\left(\frac{\det(M_0)_{I,J}}
                   {\det(M_0)_{I_0,J_0}}\right)\ge0
\tag{2.5}
$$

for all l-element I,J. To check that the stated input applies to
arbitrary consecutive J_0, subtract its first index from every
column exponent in (2.4). This multiplies each row by a root of
unity. The remaining determinant is a Vandermonde. The valuation
of that Vandermonde is minimized by consecutive row indices, by
the balanced-residue calculation in Section 5 of the input. Every
ordinary Fourier minor is that row Vandermonde times an integral
Schur polynomial. The factor N^(-l/2) cancels in (2.5).

The conventions det(empty)=1 and sum(empty)=0 cover l=0 below.

## 3. The additional bordered-minor theorem

Define the unnormalized overlap matrix

$$
C=\Phi^T D^{-1}M_0D\Phi.
$$

Let E,F be arbitrary eigenvalue subsets with |E|=k and |F|=k-1.
For either endpoint j_*=0 or j_*=N-1, consider the k-by-k matrix
whose first k-1 rows are C_(F,E) and whose last row is
omega^(j_*) Phi_(j_*,E). Its determinant will be denoted
H_(j_*;F,E). We prove

$$
\boxed{H_{j_*;F,E}\ne0.}
\tag{3.1}
$$

This is an additional mixed-minor assertion. It is not a formal
consequence of total nonsingularity of C.

First apply Cauchy--Binet to the product

$$
\begin{pmatrix}
\Phi_F^TD^{-1}M_0\\ e_{j_*}^T
\end{pmatrix}D\Phi_E.
$$

Only coordinate column sets containing j_* occur. Expanding the
last row and applying Cauchy--Binet once more gives

$$
H_{j_*;F,E}
=\epsilon_{j_*,k}\!
\sum_{\substack{|I|=|J|=k-1\\ j_*\notin J}}
\det\Phi_{I,F}\,\det(M_0)_{I,J}\,
\det\Phi_{J\cup\{j_*\},E}\,
\omega^{j_*+\sum J-\sum I}.
\tag{3.2}
$$

Every coordinate set is in increasing order. The sign is constant
over the sum because j_* is an endpoint: epsilon_(0,k)=(-1)^(k+1)
and epsilon_(N-1,k)=1. Its value has no bearing on nonvanishing.

### 3.1. The first endpoint

Use v_+. The unique least power of omega occurs at

$$
I_0=\{N-k+1,\ldots,N-1\},\qquad
J_0=\{1,\ldots,k-1\}.
\tag{3.3}
$$

Both sets have k-1 elements; J_0 union {0} is the first k
coordinates. Thus both Jacobi minors in this summand are nonzero
endpoint minors, and its Fourier minor is a nonzero consecutive
Vandermonde.

For any other pair define

$$
g=(\sum I_0-\sum I)+(\sum J-\sum J_0)>0.
$$

The ratio of its summand to the summand (3.3) has valuation at
least

$$
-\tfrac12(\sum I_0-\sum I)
-\tfrac12(\sum J-\sum J_0)+g=g/2>0,
\tag{3.4}
$$

by (2.2), (2.3), and (2.5). Hence after division by the nonzero
extreme summand, (3.2) is 1 plus terms of positive valuation. It
cannot vanish.

### 3.2. The last endpoint

Use v_-. Now the uniquely least valuation of the omega power
occurs at its largest exponent, namely

$$
I_0=\{0,\ldots,k-2\},\qquad
J_0=\{N-k,\ldots,N-2\}.
\tag{3.5}
$$

Here J_0 union {N-1} is the last k coordinates. Again every
factor of the extreme summand is nonzero. For any other pair put

$$
g=(\sum I-\sum I_0)+(\sum J_0-\sum J)>0.
$$

Because v_-(omega)=-1, the omega ratio contributes g to the
valuation. Equations (2.2)--(2.5) bound the loss in the other
factors by at most g/2. The same strict-dominance argument proves
(3.1) at the second endpoint.

The case k=1 is simply the nonzero endpoint coordinate of one
Jacobi eigenvector, and agrees with the empty-set conventions.

To express (3.1) in an orthonormal eigenbasis, write
Q=PD Phi diag(n_i^(-1)), where n_i=||phi_i||>0, and set
B=Q^*M_NQ. If c_x^*=e_x^*Q is the coordinate row of an endpoint,
then multiplication of the first k-1 rows by the corresponding
n_i and all k columns by their n_i transforms

$$
\begin{pmatrix}B_{F,E}\\ (c_x^*)_E\end{pmatrix}
$$

into precisely the matrix defining H_(j_*;F,E). All the factors
are nonzero. Therefore

$$
\boxed{\det\begin{pmatrix}B_{F,E}\\ (c_x^*)_E\end{pmatrix}\ne0}
\tag{3.6}
$$

for both physical endpoints and every E,F of the stated sizes.

## 4. Large-real-time eigenvectors

Order the distinct eigenvalues of A_N as a_1>...>a_N. Work in
the orthonormal eigenbasis just fixed, and put

$$
D_t=\operatorname{diag}(e^{ta_i}),\qquad C_t=D_tB,
\quad b_k=\det B_{[1:k],[1:k]},\quad b_0=1.
$$

All b_k are nonzero by the input's all-minor theorem. The
characteristic coefficient argument of its Section 7 proves that
for sufficiently large real t, C_t has N distinct eigenvalues
lambda_k(t), with

$$
\lambda_k(t)e^{-ta_k}\longrightarrow b_k/b_{k-1}\ne0.
\tag{4.1}
$$

For completeness, the unique largest exponential in the k-th
characteristic coefficient is b_k exp(t sum_(i<=k)a_i). On the
scale X=exp(ta_k)Y, the two terms of orders k-1 and k dominate
near Y=b_k/b_(k-1). Their normalized limit has one simple
nonzero root there. Rouché's theorem gives (4.1), and the distinct
exponential scales separate all N roots.

Fix k and normalize a right eigenvector r_k(t) by its k-th
coordinate equal to 1. We now justify that this normalization is
possible for large t and compute the limit. In the equations
(C_t-lambda_k I)r=0, divide row i<k by exp(ta_i), and divide row
i>k by -lambda_k. Delete row k and treat the k-th coordinate as
the specified inhomogeneous value 1. The coefficient matrix for
the remaining coordinates tends to

$$
\begin{pmatrix}
B_{I,I}&B_{I,L}\\ 0&I_L
\end{pmatrix},\qquad
I=\{1,\ldots,k-1\},\quad L=\{k+1,\ldots,N\}.
\tag{4.2}
$$

It is invertible since det B_(I,I)=b_(k-1). The solution of these
N-1 equations therefore exists uniquely and converges. The
deleted row is also satisfied, since lambda_k is an eigenvalue
and the retained rows have rank N-1. Thus

$$
r_k(t)\longrightarrow r_k^{(0)},\qquad
(r_k^{(0)})_L=0,\quad (r_k^{(0)})_k=1,
\quad (r_k^{(0)})_I=-B_{I,I}^{-1}B_{I,k}.
\tag{4.3}
$$

For either endpoint row c_x^*, the limiting coordinate is

$$
c_x^*r_k^{(0)}
=\frac{1}{b_{k-1}}
\det\begin{pmatrix}
B_{I,[1:k]}\\ (c_x^*)_{[1:k]}
\end{pmatrix}\ne0
\tag{4.4}
$$

by (3.6). Consequently c_x^*r_k(t) is nonzero for all sufficiently
large t, simultaneously for all finitely many k.

Let O_x(t) be the matrix with rows c_x^* C_t^m, 0<=m<N, and let
R_t be the matrix of these right eigenvectors. Then

$$
(O_x(t)R_t)_{m,k}=\lambda_k(t)^m\,c_x^*r_k(t).
$$

Its determinant is the nonzero Vandermonde of the distinct
lambda_k(t), multiplied by the nonzero product of the endpoint
coordinates. Since R_t is invertible, O_x(t) is invertible.
Changing back by Q proves endpoint observability for e^(tA_N)M_N
for sufficiently large positive real t.

## 5. Return to the exact algebraic parameter

For an endpoint x define the entire function

$$
\mathcal O_x(z)=
\det\begin{pmatrix}
e_x^*\\ e_x^*U_N(z)\\ \vdots\\ e_x^*U_N(z)^{N-1}
\end{pmatrix}.
$$

The preceding section shows that it is not identically zero,
by evaluating at z=-it/N for large positive t.

The matrix A_N is algebraic Hermitian with simple algebraic
eigenvalues. Its spectral projectors are algebraic. Expanding
the exponentials in every finite product U_N(z)^m shows that
mathcal O_x(z) is a finite sum

$$
\mathcal O_x(z)=\sum_\nu q_\nu e^{izN\beta_\nu},
\qquad q_\nu,\beta_\nu\in\overline{\mathbb Q}.
\tag{5.1}
$$

Collect equal frequencies. At least one resulting coefficient is
nonzero because the function is not identically zero. At any
nonzero algebraic z, the exponents izN beta_nu are distinct
algebraic numbers. The Lindemann--Weierstrass theorem says that
their exponentials are linearly independent over the algebraic
numbers. Thus mathcal O_x(z) cannot vanish.

The published statement used is Theorem 3.2 of S. A. Popescu,
*A Simple and Self-contained Proof for the Lindemann--Weierstrass
Theorem*, DOI 10.1007/978-3-031-51959-8_16; its precise hypotheses
and statement were checked in Section 7 of the frozen input.
There is no assumption that the frequencies beta_nu themselves
are rationally independent. Only their distinctness after
collection is used.

This proves observability in (1.1). If w is a nonzero eigenvector
and e_x^*w=0, then every row of the observable matrix annihilates
w, contradicting invertibility. Hence the endpoint coordinate of
every eigenvector is nonzero.

For cyclicity, use the exact identity, valid for all complex z,

$$
U_N(z)^*=U_N(\overline z)^{-1}.
\tag{5.2}
$$

Taking the adjoint of the observable matrix at bar z gives
independence of e_x,U_N(z)^(-1)e_x,...,U_N(z)^(-(N-1))e_x.
Multiplication by the invertible matrix U_N(z)^(N-1), followed
by reversal of the columns, gives the cyclic determinant in
(1.1). This proves the theorem for complex as well as real
nonzero algebraic z.

## 6. Consequence for exact soft quantum return

Let U=U_N(tau), let 0<=E<=I, and define

$$
D_E=\sqrt{I-E}\,U,\qquad
F_m=\sqrt E\,U D_E^{m-1}\sqrt E\quad(m\ge1).
$$

The visible subspace is the smallest U-invariant subspace
containing ran E. In finite dimension for unitary U this equals
span{U^j ran E:j in Z}; its orthogonal complement is the largest
U-invariant subspace contained in ker E. If ran E contains either
endpoint coordinate vector, cyclicity proves that the visible
subspace is C^N. Therefore the exact soft-return Kac identity
gives

$$
\boxed{\sum_{m\ge1}m\,\|F_m\|_{\rm HS}^2=N.}
\tag{6.1}
$$

Here is a direct finite-dimensional derivation for this full
visibility case, to specify exactly the identity used. Since D_E
is a contraction, an eigenvalue of modulus 1 would have an
eigenvector w with

    ||D_E w||=||w||,

forcing E U w=0. The relation D_Ew=lambda w then implies
Uw=lambda w and Ew=0, giving a dark eigenvector. Full visibility
excludes this. Thus the spectral radius of D_E is strictly less
than 1, and its powers tend to zero exponentially for this fixed N.

Put R=sqrt(I-E) and S=sqrt E. The unitary block matrix

$$
\begin{pmatrix}RU&S\\ SU&-R\end{pmatrix}
$$

gives D_E D_E^*+E=I and
U^*EU=I-D_E^*D_E. Since F_m=SU D_E^(m-1)S,

$$
\|F_m\|_{\rm HS}^2
=\operatorname{Tr}\bigl[E(D_E^*)^{m-1}
        (I-D_E^*D_E)D_E^{m-1}\bigr]
=a_{m-1}-a_m,
$$

where a_j=Tr[E(D_E^*)^j D_E^j]. Exponential decay justifies
telescoping with the weight m and summing cyclically:

$$
\sum_{m\ge1}m\|F_m\|_{\rm HS}^2
=\sum_{j\ge0}a_j
=\operatorname{Tr}\sum_{j\ge0}D_E^j E(D_E^*)^j
=\operatorname{Tr}I=N.
$$

The last identity follows by telescoping E=I-D_E D_E^*.
No N-uniform spectral gap or decay estimate is asserted.

For the discrete Fourier effect

$$
E_N=P_I\mathcal F_N^*P_J\mathcal F_NP_I,
$$

let I and J be consecutive cyclic intervals of lengths r,s,
respectively, with s>=r. Its restriction to P_I C^N is strictly
positive: the first r consecutive Fourier rows restricted to I
are a Vandermonde in r distinct N-th roots, with only nonzero
row factors if I wraps. Hence ran E_N=P_I C^N. Whenever I
contains x_+ or x_-, (6.1) applies exactly.

An interval centered at q=1/2 of length comparable to sqrt N
contains both endpoints for all sufficiently large odd N. The
corrected ordinary-Weyl classical symbol has vanishing gradient
on q=1/2, and S(1/2,0)=(1/2,0) modulo the lattice, so this is
also the fixed-point center used for the local marker. No change
of the prescribed perturbation parameter is involved.

## 7. What the theorem does and does not settle

This is an exact result for the original matrices at tau, for
every odd N not divisible by 7. It rules out a dark eigenvector
for the specified local coordinate detector and identifies its
mean return sum exactly with the full dimension.

The argument requires the new bordered-minor theorem. Mere total
nonsingularity of M_N in an A_N eigenbasis, or the earlier absence
of algebraic eigenlines, would not suffice to exclude a
transcendental eigenvector contained in a coordinate hyperplane.

The valuation and Lindemann--Weierstrass arguments are qualitative.
They do not bound how small an endpoint coordinate may be as N
grows. In particular, (6.1) supplies no control of individual
return phases or of the signed products of power traces at
times proportional to N. H_diag remains unproved.
