> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_padic_jacobi_simplicity.md`. Embedded SHA256: `f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df`.
> [Thematic guide](../../topics/algebra.md).

# P-adic dominance of every Jacobi--cat minor

Research continuation, 20 October 2026. All matrices and the phase
exp(i alpha_0)=(-3+4i)/5 are exactly as in the question. No parameter
averaging or numerical replacement of tau is used.

## 1. Results

**Theorem 1.** Let N>=3 be odd and assume 7 does not divide N. The
Hermitian matrix A_N has simple spectrum. In any orthonormal eigenbasis
of A_N, every square minor of the matrix of M_N is nonzero.

The row and column eigenvalue subsets in this assertion may be
different. In particular all its entries and all its principal minors
are nonzero. This is a total nonsingularity statement, not positivity
of those generally complex minors.

**Theorem 2.** For every odd N>=3 with 7 not dividing N, and every
nonzero algebraic complex number z,

$$
\boxed{U_N(z)=e^{izNA_N}M_N\quad\hbox{has simple spectrum}.}
\tag{1.1}
$$

This applies to the actual z=tau=10^(-80), without requiring tau to
depend on N. It covers every composite odd N not divisible by 7,
including arbitrary powers of 5 in such dimensions.

**Theorem 3.** In the same dimensions and at every nonzero algebraic z,

$$
\boxed{\{C\in\operatorname{Mat}_N(\overline{\mathbb Q}):
                       CU_N(z)=U_N(z)C\}
        =\overline{\mathbb Q}\,I.}
\tag{1.2}
$$

For real nonzero algebraic z, every nontrivial orthogonal spectral
projection of U_N(z) consequently has at least one transcendental
entry. No eigenvector has all its coordinate ratios algebraic: such
a vector would give an algebraic rank-one orthogonal spectral
projection.

These are exact finite-dimensional statements on an infinite class of
dimensions. They do not bound spectral gaps on the scale 1/N and do
not prove H_diag. The dimensions divisible by 7 have several Jacobi
paths and are not covered by this proof.

## 2. The valuation supplied by the specified hopping phase

Put

$$
\omega=e^{i\alpha_0}=\frac{-3+4i}{5}
               =\frac{1+2i}{1-2i},\qquad \pi_5=1+2i.
\tag{2.1}
$$

Choose a nonarchimedean valuation v on a number field containing all
the algebraic quantities used below, extending the prime (pi_5) of
Q(i), and normalize v(pi_5)=1. Such an extension exists, for example
by embedding an algebraic closure of Q(i) into an algebraic closure
of its completion at that prime. Then

$$
v(\omega)=1,\qquad v(5)=1,\qquad v(i)=v(2)=0.
\tag{2.2}
$$

Write O={a:v(a)>=0}; its residue field has characteristic 5.
We use only the elementary valuation laws v(ab)=v(a)+v(b) and
v(a+b)>=min(v(a),v(b)), with equality when the minimum is attained
at only one summand. Eigenvalues and all roots of unity can be
included in a single finite extension, so no infinite sum over
valuations is involved.

Here are the root-of-unity facts needed below. All roots of unity are
valuation units. Distinct roots of unity of order prime to 5 remain
distinct modulo the maximal ideal. To see the latter claim, if
eta=1+u has order d prime to 5 and v(u)>0, the term du in
(1+u)^d-1 has valuation v(u), strictly below all remaining terms,
contradicting eta^d=1. A root of unity has positive v(1-eta) only
if its order is a power of 5: separate its prime-to-5 and 5-power
parts, and use that in characteristic 5 a root of 5-power order
reduces to 1.

For a primitive root eta of order 5^r, r>=1,

$$
\boxed{v(1-\eta)=\frac1{4\cdot5^{r-1}}.}
\tag{2.3}
$$

Indeed eta reduces to 1; for j prime to 5 the quotient
(1-eta^j)/(1-eta) reduces to j and is a unit. Thus all factors in
Phi_(5^r)(1)=product_(j,5)=1 (1-eta^j)=5 have the same valuation.
There are 4*5^(r-1) of them, proving (2.3). These arguments also
show that if eta has odd order, then 1+eta is a unit, since its
reduction cannot be -1.

## 3. Cutting and gauging the exact Jacobi matrix

Let h=(N+1)/2 represent the modular inverse of 2. The prescribed
Fourier rule gives the exact entries

$$
(A_N)_{xx}=V(x/N),\qquad
(A_N)_{x,x+1}=\frac{\omega^{-1}}{200}
                             r((x+h)/N),
\tag{3.1}
$$

with the reverse entry conjugate. Here

$$
V(q)=\cos(14\pi q)+r(q)/10+r(q)\sin(2\pi q)/100-1/10.
$$

On the odd N grid,

$$
r(y/N)=0\quad\Longleftrightarrow\quad N\mid7y.
\tag{3.2}
$$

The second factor 1+cos(2pi y/N) cannot vanish on an odd grid.
Since 7 does not divide N, there is exactly one zero edge, at
x=(N-1)/2. Order the coordinate path as

$$
x_j=h+j\pmod N,\qquad 0\le j<N.
\tag{3.3}
$$

The zero edge is now the seam between j=N-1 and j=0; every edge
j to j+1 for 0<=j<N-1 is nonzero. Let P be the permutation sending
coordinate j to x_j, and let D=diag(omega^j). Then

$$
L=200D^*P^*A_NPD
\tag{3.4}
$$

is a real symmetric Jacobi path with diagonal d_j=200V(x_j/N)
and off-diagonals

$$
b_j=r((x_j+h)/N)>0,qquad 0\le j<N-1.
\tag{3.5}
$$

There is no seam phase in (3.4): the only possible closing edge is
exactly zero, while each internal phase omega^(-1) is cancelled by
omega^(j+1)/omega^j. This remains true where the original coordinate
x_j wraps modulo N.

All d_j lie in O. Indeed 200V=200cos(14pi q)+20r+2r sin(2pi q)-20,
and the trigonometric values have only denominators 2 and i when
expressed in N-th roots of unity.

For a root eta=exp(2pi i y/N), the exact factorization is

$$
r(y/N)=-\frac{(\eta^7-1)^2(\eta+1)^2}{4\eta^8}.
\tag{3.6}
$$

The second factor is a unit in the sense of Section 2. At a
nonzero edge, eta^7!=1. Equations (2.3) and (3.6) therefore give

$$
\boxed{v(d_j)\ge0,\qquad 0\le v(b_j)\le1/2.}
\tag{3.7}
$$

This bound is valid even when 5 divides N. When 5 does not divide
N all b_j are valuation units, but that special case is not needed.

The real symmetric path L has simple spectrum: an eigenvector's
first coordinate determines all subsequent coordinates by the
nonzero-edge recurrence, and if the first coordinate vanishes the
whole vector vanishes. Every eigenspace has dimension at most one;
Hermiticity makes algebraic and geometric multiplicities equal.
Its eigenvalues mu_1,...,mu_N are real algebraic and belong to O,
because they satisfy a monic characteristic polynomial with
coefficients in O. A root of negative valuation would make the
leading term of that polynomial uniquely dominant.

## 4. A valuation estimate for every Jacobi eigenvector minor

Choose real eigenvectors phi_i of L with phi_i(0)=1. Define

$$
\beta_j=\prod_{r=0}^{j-1}b_r,qquad \beta_0=1,
\quad B_j=v(\beta_j).
$$

The usual recurrence, written out explicitly, is

$$
\phi_i(j)=\frac{p_j(\mu_i)}{\beta_j},\qquad
p_0(t)=1,\quad p_1(t)=t-d_0,
$$

$$
p_{j+1}(t)=(t-d_j)p_j(t)-b_{j-1}^2p_{j-1}(t).
\tag{4.1}
$$

Each p_j is monic of degree j with coefficients in O. Let E be
any set of k distinct eigenvalue indices and J={j_1<...<j_k}
any coordinate set. Let Phi_(J,E)=(phi_i(j))_(j in J,i in E).
With Delta_E=product_(i<i', i,i' in E)(mu_(i')-mu_i),

$$
\det\Phi_{J,E}
 =\frac{\Delta_E\,q_J(\mu_E)}{\prod_{j\in J}\beta_j},
\qquad q_J\in O[t_1,...,t_k].
\tag{4.2}
$$

To justify the divisibility, the determinant det(p_(j_a)(t_b))
is alternating in its variables and vanishes when t_a=t_b.
Successive monic polynomial division by their differences yields
division by the full Vandermonde with coefficients still in O.
Equivalently, expand the monic polynomials into powers and divide
each monomial alternant by the Vandermonde over Z, where the
quotient is an integer symmetric polynomial. This proves (4.2)
without dividing by any eigenvalue difference in O.

For the initial coordinate set J_0={0,...,k-1}, monicity gives
q_(J_0)=1. Thus its minor is nonzero, and, using (3.7),

$$
\begin{split}
v\!\left(\frac{\det\Phi_{J,E}}{\det\Phi_{J_0,E}}\right)
&\ge-\sum_{a=1}^k(B_{j_a}-B_{a-1})\\
&\ge-\frac12\left(\sum J-\frac{k(k-1)}2\right).
\end{split}
\tag{4.3}
$$

The notation v(0)=+infinity makes this valid for a vanishing
numerator as well.

Apply the same construction from the other endpoint. Every
phi_i(N-1) is nonzero by the backward recurrence. The vectors
phi_i(N-1-j)/phi_i(N-1) are normalized at the left endpoint of
the reversed Jacobi path, whose off-diagonals obey the same (3.7).
The factors phi_i(N-1) cancel in a ratio of minors. Therefore,
for I_0={N-k,...,N-1},

$$
\boxed{
v\!\left(\frac{\det\Phi_{I,E}}{\det\Phi_{I_0,E}}\right)
 \ge-\frac12\left(\sum I_0-\sum I\right).}
\tag{4.4}
$$

The endpoint minor in the denominator is nonzero. No claim that
the endpoint eigenvector coordinates are valuation units is needed
in (4.4). Their valuations disappear from this ratio exactly.

## 5. Consecutive Fourier rows minimize the ramified valuation

Put M_0=P^*M_NP. From the exact kernel and the unwrapped coordinate
x_j=h+j in modular exponents,

$$
(M_0)_{ij}=N^{-1/2}\,u_i v_j\,\zeta^{cij},
\qquad \zeta=e^{2\pi i/N},\quad c=\overline4\pmod N,
\tag{5.1}
$$

where u_i,v_j are roots of unity. They absorb all row, column,
and constant quadratic phases and are valuation units. The integer
c is a unit modulo N.

For coordinate subsets I={i_1<...<i_k} and J={j_1<...<j_k}, put
z_a=zeta^(c i_a). The integer-polynomial alternant identity gives

$$
\det(z_a^{j_b})=\prod_{a<b}(z_b-z_a)\,s_J(z_1,...,z_k),
\qquad s_J\in\mathbb Z[z_1,...,z_k].
\tag{5.2}
$$

All z_a are valuation units, so the final factor has nonnegative
valuation. For J_0={0,...,k-1}, it equals 1.

We now prove, including the ramified case, that the valuation of
the Vandermonde in (5.2) is minimized by consecutive indices I.
If 5 does not divide N, all distinct roots have unit differences
and the assertion follows immediately from Section 2. Otherwise
write N=5^e n, with e>=1 and (n,5)=1. For a set I and a divisor d
of N define

$$
C_d(I)=\#\{\{i,j\}\subset I:i\equiv j\pmod d\}
       =\sum_{r\bmod d}\binom{m_r(I)}2.
\tag{5.3}
$$

For distinct i,j, the valuation of zeta^(ci)-zeta^(cj) is zero
unless n divides i-j. If n divides i-j and t=v_5((i-j)/n),
then 0<=t<=e-1 and (2.3) gives
v(zeta^(ci)-zeta^(cj))=1/(4*5^(e-t-1)). Multiplication by c
does not change this value, since c is prime to N. Writing this
increasing weight as a sum of its increments proves the exact formula

$$
\boxed{
v\!\left(\prod_{a<b}(z_b-z_a)\right)
 =\frac{C_n(I)}{4\cdot5^{e-1}}
  +\sum_{t=1}^{e-1}5^{t-e}C_{n5^t}(I).}
\tag{5.4}
$$

For any fixed d and k, the sum in (5.3) is minimized when its d
occupancies differ by at most one. Indeed, transferring one point
from an occupancy at least two larger than another strictly lowers
the sum of binomial coefficients. Every interval of k consecutive
integer indices has exactly this balanced occupancy property for
every d simultaneously. Every coefficient in (5.4) is positive.
Consequently its value for any I is at least its value for
I_0={N-k,...,N-1}.

Combining (5.1)--(5.4) yields the estimate

$$
\boxed{
v\!\left(\frac{\det(M_0)_{I,J}}
                 {\det(M_0)_{I_0,J_0}}\right)\ge0.}
\tag{5.5}
$$

The denominator is a nonzero ordinary Vandermonde times row and
column units and N^(-k/2). The latter may have negative valuation
when 5 divides N, but it is the same factor for every k-by-k
minor and cancels exactly in (5.5). Thus no unramified assumption
on N^(-1/2) has been made.

## 6. A unique term dominates every overlap minor

Let Phi be the matrix of the real eigenvectors phi_i chosen above.
The corresponding, not yet normalized, overlap matrix for M_N is

$$
C=\Phi^T D^{-1}M_0D\Phi.
\tag{6.1}
$$

The transpose here is correct because the chosen phi_i are real in
the original complex embedding. The diagonal matrix D is unitary
there, so its adjoint is D^(-1), even though its entries have
nonzero valuation at pi_5.

Take arbitrary row and column eigenvalue sets E,F of cardinality k.
Twice applying Cauchy--Binet gives the exact finite expansion

$$
\det C_{E,F}
 =\sum_{|I|=|J|=k}
  \det\Phi_{I,E}\,\det(M_0)_{I,J}\,\det\Phi_{J,F}
     \omega^{\sum J-\sum I}.
\tag{6.2}
$$

The term with I=I_0={N-k,...,N-1}, J=J_0={0,...,k-1} is nonzero
by Sections 4 and 5. Its exponent is -k(N-k), the unique least
possible exponent. Relative to it put

$$
g=(\sum I_0-\sum I)+(\sum J-\sum J_0)\ge0.
\tag{6.3}
$$

This is an integer, and g=0 only at the displayed extreme pair.
Equations (4.3), (4.4), (5.5), and v(omega)=1 show that the ratio
of any other summand in (6.2) to the extreme summand has valuation
at least

$$
-\frac12(\sum I_0-\sum I)
-\frac12(\sum J-\sum J_0)+g
=g/2>0.
\tag{6.4}
$$

Thus after division by the nonzero extreme term, (6.2) is 1 plus
a finite sum of elements of strictly positive valuation. It is
a valuation unit and cannot vanish. Every minor of C is nonzero.

To pass to an orthonormal eigenbasis, divide each phi_i by its
positive real norm. These are nonzero algebraic scalars, but they
need not be valuation units. They simply multiply the corresponding
rows and columns of (6.1) by nonzero factors; no minor becomes zero.
Permuting eigenvectors and changing their unit scalar phases has
the same property. This proves Theorem 1 in every orthonormal
eigenbasis of A_N.

## 7. From the minors to actual simple spectrum

Order the distinct eigenvalues of A_N as a_1>...>a_N. Write B
for M_N in this eigenbasis, and

$$
b_k=\det B[1:k,1:k],\qquad b_0=1.
$$

Theorem 1 proves b_k!=0 for every k. The coefficient of X^(N-k)
in det(XI-e^(tA_N)M_N) is (-1)^k times a sum of principal minors
of B weighted by exp(t sum_(i in I)a_i). Its unique largest
exponential is the initial set I={1,...,k}, with coefficient b_k.
For positive real t tending to infinity, on the scale X=e^(ta_k)Y
the two terms with indices k-1 and k dominate. After dividing by
their common nonzero exponential, the polynomial converges uniformly
near the nonzero number b_k/b_(k-1) to a nonzero constant times

$$
Y^{N-k}(b_{k-1}Y-b_k).
\tag{7.1}
$$

Choose a small circle about b_k/b_(k-1) excluding zero. On that
circle the remaining terms tend uniformly to zero; Rouché's
theorem gives exactly one root, counted with multiplicity, inside
for all sufficiently large t. The N exponential scales are
disjoint because the a_k are strictly decreasing. Therefore
e^(tA_N)M_N has N distinct eigenvalues for all sufficiently large
positive real t. This is the complex-time criterion explicitly
proved in Section 5 of the frozen `exact_spectral_simplicity.md`;
the previously missing hypothesis there is now supplied for every
dimension under consideration.

Consequently

$$
\mathcal D(z)=\operatorname{disc}_X
            \det(XI-e^{izNA_N}M_N)
\tag{7.2}
$$

is not identically zero: it is nonzero at z=t/(iN) for a
sufficiently large positive t.

Every eigenvalue of the algebraic Hermitian A_N and every spectral
projector is algebraic. Expanding its matrix exponential shows
that (7.2) is a finite exponential polynomial with algebraic
coefficients and algebraic frequencies. After collecting equal
frequencies, the Lindemann--Weierstrass theorem implies that a
nonzero such polynomial cannot vanish at a nonzero algebraic
parameter. Its complex exponents remain distinct and algebraic
after multiplication by that parameter. The exact published
statement is Theorem 3.2 of S. A. Popescu, *A Simple and
Self-contained Proof for the Lindemann--Weierstrass Theorem*,
[DOI 10.1007/978-3-031-51959-8_16](https://link.springer.com/chapter/10.1007/978-3-031-51959-8_16),
also verified in the author's
[manuscript, Theorem 3.2](https://arxiv.org/pdf/2306.14352).
All its hypotheses have just been checked. This proves Theorem 2.

## 8. The algebraic commutant

Suppose C has algebraic entries and commutes with U_N(z_0) at a
nonzero algebraic z_0. Every entry of

$$
CU_N(z)-U_N(z)C
$$

is an algebraic exponential polynomial. The same
Lindemann--Weierstrass argument forces this commutator to vanish
identically in z. Evaluating and differentiating at zero shows

$$
CM_N=M_NC,\qquad CA_N=A_NC.
\tag{8.1}
$$

In the simple eigenbasis of A_N, the second identity makes C
diagonal. Every entry of M_N in that basis is nonzero by Theorem 1;
the first identity therefore makes any two diagonal entries of C
equal. Thus C is scalar. Its scalar is algebraic since its
original entries are algebraic, proving Theorem 3.

For real z_0, U_N(z_0) is unitary, so any orthogonal projection
onto a selection of its eigenspaces commutes with it. A nontrivial
such projection cannot have only algebraic entries by (1.2).
If an eigenvector has all coordinate ratios algebraic, rescale
one nonzero coordinate to 1; its rank-one projection is then
vv^*/(v^*v) with algebraic entries. This is the asserted
contradiction for eigenvectors.

## 9. Scope and provenance

Inputs read without modification:

| File | SHA-256 |
|---|---|
| `../research_continuation_2026_10_20/exact_spectral_simplicity.md` | `4aef0bf28965da0c359c01dff6e3bd330dd0cafdeb79118a5e84bd359d1ac2eb` |
| `arithmetic_second_order_proof.md` | `7d6a0a28d67ab43efa4e444c26ccd25d9d981925c9af80604f3bf608e17c7770` |
| `arithmetic_oldspace_escape.md` | `596d44605310cc898fa75e23df4aa811189a1764fed21ce8b9f5d07ae734813a` |

The exact kernel, gauge, valuation estimates, balanced-residue
minimization, all-minor dominance, and scalar algebraic commutant
are proved explicitly above. No finite-field sample or eigenvalue
experiment is used. The large positive real t, complex-parameter argument
only certifies nonidentity of the discriminant; the final conclusion
is at the original fixed algebraic parameter.

For 7 dividing N there are seven Jacobi paths. A set of eigenvectors
supported on different paths requires different endpoint coordinate
sets; the resulting extreme Fourier subminor need not be a
consecutive-row Vandermonde and can vanish. Thus the proof must not
be silently extended to those dimensions. It also gives no useful
lower bound on gaps of U_N at the Archimedean place. The
Lindemann--Weierstrass step is qualitative. Signed trace-product
cancellation at m proportional to N, and hence H_diag, remains
unproved.
