> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_padic_jacobi_audit.md`. Embedded SHA256: `ef2621947874f3bb4bbce1a3ef27d1f80b91a58d7fea1c5daa476668087f5194`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/algebra.md).

# Independent audit: p-adic Jacobi minors and actual spectral nonresonance

Research continuation, 20 October 2026. This audit checks the finite
algebraic arguments directly. It does not infer a spectral-statistical
limit from algebraic nonvanishing.

## 1. Inputs and verdict

| Frozen input | SHA-256 |
|---|---|
| arithmetic_padic_jacobi_simplicity.md | f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df |
| arithmetic_transcendental_eigenvalue_ratios.md | 334b97d4659d2f29ed22c7615252cdb88e7d2d4c99e1a896083cea993475e0a5 |

**Verdict: PASS.** For every odd $N\geq3$ with $7\nmid N$, the
proof establishes that $A_N$ is simple, every square minor of $M_N$
in an $A_N$-eigenbasis is nonzero, and $U_N(z)$ is simple at every
nonzero algebraic complex $z$. Its algebraic commutant is scalar.
The resultant extension also proves that every ratio of two distinct
eigenvalues is transcendental and that every nonzero integer power
has simple spectrum.

The audit includes arbitrary and different row and column eigenvalue
subsets, dimensions divisible by arbitrarily large powers of $5$,
the original modular half, and the normalization of the eigenvectors.
No numerical eigenvalue computation is used.

The sole wording correction during review was to replace a reference
to a positive imaginary parameter by a large positive real $t$
argument. The parameter actually used is
$z=t/(iN)=-it/N$. The formulas and conclusions were already correct.

## 2. Why the specified phase supplies strict dominance

Write
$$
\omega=\frac{-3+4i}{5}
       =\frac{1+2i}{1-2i}.
$$
Extend the valuation at the Gaussian prime $1+2i$ to a number field
containing all the finitely many algebraic quantities for the chosen
$N$, and normalize $v(1+2i)=1$. The conjugate prime is a unit, so
$$
v(\omega)=v(5)=1,\qquad v(2)=v(i)=0.
$$
In particular this is not a valuation in which the hopping phase is
a unit.

The root-of-unity computations used in the proof are valid in this
extension. Every root of unity is a unit. A root of unity of order
prime to $5$ cannot reduce to $1$, unless it is $1$: in
$(1+u)^d-1$, with $5\nmid d$ and $v(u)>0$, the linear term has
strictly smaller valuation than every higher term. For primitive
$5^r$-th roots,
$$
v(1-\eta)=\frac{1}{4\,5^{r-1}}.
$$
Indeed all primitive differences have the same valuation, because
$(1-\eta^j)/(1-\eta)$ reduces to the nonzero residue of $j$, and
their product is $\Phi_{5^r}(1)=5$.

For a root of odd order, $1+\eta$ is a unit. Its reduction cannot
have order $2$, since its order divides the original odd order.
Consequently the exact identity
$$
r(y/N)=-\frac{(\eta^7-1)^2(\eta+1)^2}{4\eta^8},
\qquad \eta=e^{2\pi iy/N},
$$
gives, at every nonzero hopping edge,
$$
0\leq v(r(y/N))\leq\frac12.
\tag{2.1}
$$
This upper bound is the margin needed later: the gain $1$ per
gauge-exponent step is strictly larger than the maximal loss $1/2$
from the Jacobi recurrence.

## 3. Exact modular gauge and Jacobi eigenvector minors

Let $h=(N+1)/2$, the specified inverse of $2$ modulo $N$.
The original quantization gives
$$
(A_N)_{x,x+1}
   =\frac{\omega^{-1}}{200}r((x+h)/N).
$$
On an odd grid the second factor of $r$ never vanishes, and hence
$$
r(y/N)=0\iff N\mid7y.
$$
When $7\nmid N$, this is a single zero edge. In the order
$x_j=h+j\bmod N$, it is exactly the seam between $N-1$ and $0$.
Since $x_j+h\equiv j+1\pmod N$, all internal edges are nonzero.
The diagonal gauge $D_{jj}=\omega^j$ cancels every internal phase
exactly, including the edge where the original coordinate order wraps.

Thus $L=200D^*P^*A_NPD$ is a real symmetric irreducible Jacobi path.
Its diagonal $d_j$ is valuation-integral: after multiplication by
$200$, its trigonometric expression has only denominators involving
$2$ and $i$. Its positive real off-diagonals $b_j$ satisfy (2.1).
The first-coordinate recurrence proves one-dimensional eigenspaces;
Hermiticity then proves simple spectrum. Its eigenvalues $\mu_i$
are valuation-integral because they solve a monic integral
characteristic polynomial.

Normalize each real eigenvector by $\phi_i(0)=1$, and put
$$
\beta_j=b_0\cdots b_{j-1},\qquad
\phi_i(j)=p_j(\mu_i)/\beta_j.
$$
The recurrence
$$
p_{j+1}(X)=(X-d_j)p_j(X)-b_{j-1}^2p_{j-1}(X)
$$
has monic integral polynomials $p_j$ of degree $j$.
For any eigenvalue subset $E$ of cardinality $k$ and coordinate
subset $J$, alternation gives
$$
\det\Phi_{J,E}
 =\frac{\Delta_E q_J(\mu_E)}{\prod_{j\in J}\beta_j},
\qquad q_J\in\mathcal O[X_1,\ldots,X_k].
\tag{3.1}
$$
There is no illegal division by small eigenvalue differences here.
The Vandermonde divisibility is a polynomial identity over the
valuation ring. One can expand the $p_j$ into monomials and use the
integer Schur-polynomial quotient of each monomial alternant.

For $J_0=\{0,\ldots,k-1\}$, monicity gives $q_{J_0}=1$.
Using $v(b_j)\leq1/2$, (3.1) gives
$$
v\left(\frac{\det\Phi_{J,E}}{\det\Phi_{J_0,E}}\right)
\geq-\frac12\left(\sum J-\sum J_0\right).
\tag{3.2}
$$
The denominator is nonzero. A zero numerator is harmless, with
$v(0)=+\infty$.

Apply the same proof after reversing the Jacobi path. Every last
coordinate is nonzero by the backward recurrence. Dividing each
reversed eigenvector by its last coordinate changes numerator and
denominator minors by exactly the same column factors. Those factors
cancel, regardless of their valuations. For
$I_0=\{N-k,\ldots,N-1\}$,
$$
v\left(\frac{\det\Phi_{I,E}}{\det\Phi_{I_0,E}}\right)
\geq-\frac12\left(\sum I_0-\sum I\right).
\tag{3.3}
$$
Both (3.2) and (3.3) hold for every eigenvalue subset independently.

## 4. The ramified Fourier-minor comparison

In the reordered coordinates,
$$
(P^*M_NP)_{ij}=N^{-1/2}u_i v_j\zeta^{cij},
\qquad \zeta=e^{2\pi i/N},\quad c=\overline4\bmod N,
$$
where $u_i,v_j$ are roots of unity. Unwrapped coordinates $h+j$
can be used inside the original modular exponents. All resulting
extra phases are row or column factors of valuation zero.

For fixed rows $I$, the minor with arbitrary columns $J$ is its
ordinary Vandermonde times an integer Schur polynomial evaluated at
roots of unity. This last factor has nonnegative valuation. With
the first $k$ columns $J_0$, it is exactly $1$.

It remains to minimize the Vandermonde valuation over row sets.
If $5\nmid N$, all distinct differences are units. If
$N=5^e n$, $5\nmid n$, define
$$
C_d(I)=\sum_{r\bmod d}\binom{\#(I\cap(r+d\mathbb Z))}{2}.
$$
For an index difference with $n\mid i-j$ and
$t=v_5((i-j)/n)<e$, the valuation is
$1/(4\,5^{e-t-1})$. For other differences it is zero. Summing
the positive increments of these weights gives exactly
$$
v\!\left(\operatorname{Vdm}(\zeta^{cI})\right)
 =\frac{C_n(I)}{4\,5^{e-1}}
   +\sum_{t=1}^{e-1}5^{t-e}C_{n5^t}(I).
\tag{4.1}
$$
The coefficient of the increment at $t\geq1$ is indeed $5^{t-e}$;
this accounts for all ramification rather than just the first level.

Each collision count is minimized by balanced residue occupancies,
since moving one point between occupancies differing by at least two
decreases the sum of binomial coefficients. A consecutive interval
of $k$ integers has balanced occupancies modulo every divisor
simultaneously. In particular $I_0$ minimizes every term in (4.1).
Therefore
$$
v\left(
\frac{\det(P^*M_NP)_{I,J}}
     {\det(P^*M_NP)_{I_0,J_0}}
\right)\geq0.
\tag{4.2}
$$
The common factor $N^{-k/2}$, which need not be a valuation unit,
cancels in this ratio. The denominator is a nonzero Vandermonde.

## 5. Unique least-valuation term for arbitrary overlap minors

In the unnormalized eigenbasis the overlap matrix is
$$
\Phi^T D^{-1}(P^*M_NP)D\Phi.
$$
The real transpose of $\Phi$ is correct. In the original complex
embedding $D$ is unitary, so its adjoint is $D^{-1}$; this is
compatible with its nonzero valuation at the chosen prime.

For arbitrary eigenvalue subsets $E,F$, double Cauchy--Binet gives
the finite sum
$$
\sum_{|I|=|J|=k}
\det\Phi_{I,E}\,
\det(P^*M_NP)_{I,J}\,
\det\Phi_{J,F}\,
\omega^{\sum J-\sum I}.
\tag{5.1}
$$
The term $I=I_0,J=J_0$ is nonzero. For any other term let
$$
g=(\sum I_0-\sum I)+(\sum J-\sum J_0)>0.
$$
This is a positive integer. Equations (3.2), (3.3), and (4.2) show
that its ratio to the extreme term has valuation at least
$$
g-\frac12(\sum I_0-\sum I)
  -\frac12(\sum J-\sum J_0)=\frac g2>0.
$$
After division by the extreme term, (5.1) is $1$ plus a finite
sum in the maximal ideal, and hence is nonzero. This proves total
nonsingularity, not merely nonzero principal minors.

Dividing real eigenvectors by their nonzero algebraic norms only
rescales rows and columns. The normalizing factors need not be
valuation units. Arbitrary phase choices and permutations of an
orthonormal eigenbasis also preserve all these nonzero statements.

## 6. Complex-time certification and Lindemann--Weierstrass

Let $a_1>\cdots>a_N$ be the eigenvalues of $A_N$, and $b_k$
the leading principal minors of $M_N$ in that eigenbasis.
All $b_k$ are nonzero. In the characteristic polynomial of
$e^{tA_N}M_N$, the coefficient at order $k$ has leading term
$(-1)^k b_k e^{t(a_1+\cdots+a_k)}$.

At $X=e^{ta_k}Y$, the exponents of the coefficient terms are
$$
E_j=\sum_{i\leq j}a_i+(N-j)a_k.
$$
Their consecutive differences are $E_j-E_{j-1}=a_j-a_k$.
Thus exactly $j=k-1,k$ maximize them. The normalized limiting
polynomial is a nonzero constant times
$$
Y^{N-k}(b_{k-1}Y-b_k).
$$
Rouché's theorem on a small circle around the nonzero root gives
one root counted with multiplicity. The scales for different $k$
are disjoint for large $t$, so all roots are simple. Shrinking
the circles also yields the asymptotic
$$
\lambda_k(e^{tA_N}M_N)
 =e^{ta_k}(b_k/b_{k-1}+o(1)).
\tag{6.1}
$$

This proves that the discriminant of the original entire family
is not identically zero, by evaluating at $z=t/(iN)$.
It is a finite exponential polynomial with algebraic coefficients
and algebraic frequencies, because $A_N$ and its spectral
projectors are algebraic. Equal frequencies must first be collected.
For any nonzero algebraic $z$, the remaining exponents remain
distinct and algebraic. The Lindemann--Weierstrass theorem on
linear independence of exponentials of distinct algebraic numbers
then prohibits a zero value.

The input identifies the published theorem precisely as Popescu,
Theorem 3.2, DOI 10.1007/978-3-031-51959-8_16, with author manuscript
arXiv:2306.14352. The application only uses this stated linear
independence theorem; it assumes no rational independence among
the eigenvalues of $A_N$.

For an algebraic matrix $C$ commuting with $U_N(z_0)$ at a
nonzero algebraic parameter, the same entrywise argument makes its
commutator vanish identically in the parameter. Evaluation and
differentiation at zero imply $[C,M_N]=[C,A_N]=0$.
In the simple $A_N$-eigenbasis $C$ is diagonal; the nonzero
entries of $M_N$ force every diagonal entry equal. This proves
the asserted algebraic commutant and, for real $z_0$, the stated
consequences for orthogonal spectral projections and eigenvectors.

## 7. Independent check of the resultant extension

Fix any algebraic $c\ne0,1$, and put
$$
R_c(z)=\operatorname{Res}_X
\big(P_z(X),c^NP_z(X/c)\big).
$$
Both polynomials are monic. The roots of the second are $c$
times those of the first. Since $U_N(z)$ is invertible, the
resultant vanishes precisely when two eigenvalues have ratio $c$;
the identical-index case cannot occur for $c\ne1$.

The resultant is an algebraic exponential polynomial. It is not
identically zero: by (6.1), every distinct-index ratio has modulus
tending to either zero or infinity along large positive $t$.
There are only finitely many pairs for the fixed $N$, so none can
equal the fixed nonzero $c$ for all sufficiently large $t$.
Lindemann--Weierstrass now excludes a zero at every nonzero
algebraic parameter.

Applying this separately to every algebraic $c\ne0,1$, and using
the already established simple spectrum for $c=1$, proves that
all distinct-eigenvalue ratios are transcendental. Any collision
in a nonzero integer power would make such a ratio a root of unity,
which is algebraic. Hence all these powers are simple.

## 8. Exact boundary at multiples of seven

The restriction $7\nmid N$ is a real boundary of this proof.
When $7\mid N$, the zero edges split the Jacobi matrix into
seven paths. Endpoint sets needed for eigenvectors on different
paths are no longer consecutive Fourier rows and columns.

For example, at $N=49$ the seven blocks have length $7$.
The first and last endpoint sets, in the reordered coordinates,
are
$$
J=\{7b:0\leq b<7\},\qquad
I=\{6+7a:0\leq a<7\}.
$$
Their Fourier core is
$$
\zeta_{49}^{c(6+7a)(7b)}
 =\zeta_{49}^{42cb},
$$
independent of $a$. It has rank one, so its $7$-by-$7$
determinant is zero. This is not a counterexample to simplicity
of the original $U_{49}$; it is a concrete failure of the
extreme-term argument if extended without a new idea.

Finally none of the valuation or transcendence conclusions supplies
an Archimedean lower bound on an eigenangle gap or a near-rational
ratio. They remove exact degeneracy and exact algebraic resonances
on the stated dimensions, but they do not establish the weighted
order-$N$ trace sums required by $H_{\rm diag}$.
