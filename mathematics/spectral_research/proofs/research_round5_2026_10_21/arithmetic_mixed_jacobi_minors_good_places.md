> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/arithmetic_mixed_jacobi_minors_good_places.md`. Embedded SHA256: `0eb94e2984dbdbc475b25897194404808255ba6b2da9703d2aef7f395db1bf55`.
> [Thematic guide](../../topics/algebra.md).

# Mixed Jacobi overlap minors: a uniform good-place theorem

Research continuation, 21 October 2026. Base checkpoint
Spectral_research_round4_2026-10-21.md, SHA256
e74f697134ea0d7d0ad5776c118ac267cf4999ae029e5b1f0252de364596fa4a.

This note proves uniform noncancellation for certain actual minors of
$M_N$ in the path eigenbasis of the specified $A_N$. It includes
the entire Cauchy--Binet sum at the original gauge $(-3+4i)/5$.
It does not prove simple spectrum of $U_N$ in the remaining
dimensions and does not establish $H_{\rm diag}$.

## 1. Statement

Let $N=7n$, where $n$ is odd and $\gcd(n,35)=1$. Put
$$
h=(N+1)/2,\qquad x_{s,j}=h+sn+j\pmod N,
\qquad 0\le s<7,\quad 0\le j<n.                                 \tag{1.1}
$$
These are the seven exact Jacobi paths of $A_N$. In path $s$
choose a set $E_s$ of $k_s$ distinct eigenvectors of its Jacobi
block, with $0\le k_s\le n$. Normalize them to be orthonormal in
the ordinary complex inner product, and extend by zero off that
path. Put $\mathcal E=\bigcup_s E_s$, $k=\sum_s k_s$, and
$$
B_{\mathcal E}=(\langle v,M_Nw\rangle)_{v,w\in\mathcal E}.        \tag{1.2}
$$
Form the nondecreasing list $u_1,\ldots,u_k$ which contains, for
each path $s$, the integers $0,\ldots,k_s-1$. Define
$$
L=\sum_j u_j^2
 =\sum_s\frac{k_s(k_s-1)(2k_s-1)}6,\qquad
W=L-\sum_j u_j u_{k+1-j}.                                      \tag{1.3}
$$
For $k=0$, set $L=W=0$.

**Theorem 1.** If
$$
\boxed{W<\varphi(n),}                                          \tag{1.4}
$$
then $\det B_{\mathcal E}\ne0$ for every choice of the $E_s$'s
with these counts. In particular $L<\varphi(n)$ is sufficient.

There is a single cyclotomic place above 5 for each admissible
count vector, compatible with $i\equiv2\pmod5$, at which the
endpoint coordinate term $T_0$ of every such minor dominates
all other terms. With $v(5)=1$, the precise conclusion is
$$
\boxed{v\!\left(\det B_{\mathcal E}/T_0-1\right)\ge1.}           \tag{1.5}
$$
The place depends on the counts and need not depend on which
Jacobi eigenvalues are selected. Eigenvalues belonging to
different paths may coincide. The statement concerns the
basis assembled from path eigenvectors; it does not assert
invariance under arbitrary rotations inside a repeated global
eigenspace of $A_N$.

## 2. The finite-field Fourier input

**Lemma 2.** For a primitive seventh root $z$ in an algebraically
closed field of characteristic 5, all square minors of
$F=(z^{ab})_{0\le a,b<7}$ are nonzero.

Here is a direct proof. Summing a geometric series gives
$F^{-1}=7^{-1}(z^{-ab})$. The complementary-minor identity
therefore reduces the claim to sizes at most 3. Explicitly,
a minor of an inverse matrix on complementary indices is the
corresponding original minor divided by the determinant of
the matrix, up to the row/column signs; this follows by
expanding exterior powers of the identity $F^{-1}F=I$.

Size 1 is immediate. For size 2 extract units to leave
$1-z^{(a-a')(b-b')}$, which is nonzero. At size 3, if either
index set is an arithmetic progression modulo 7, the minor
is a Vandermonde in distinct powers of $z$, times units.
Otherwise apply separate affine transformations to the two
index sets. Each may first be put in the form $\{0,1,t\}$.
The cases $t=2,4,6$ are arithmetic progressions; multiplication
by 5 sends $\{0,1,3\}$ to $\{0,1,5\}$. Thus it suffices
to consider both index sets equal to $\{0,1,3\}$, at another
primitive seventh root. Separate affine transformations merely
supply row/column units and change $z$ to a primitive power.

For this last minor direct expansion gives
$$
\det(z^{ab})_{a,b\in\{0,1,3\}}
=z^3(3-z^3-z^5-z^6).
$$
Set $\eta=z+z^2+z^4$, $\rho=z^3+z^5+z^6$. The geometric
sum and direct multiplication give $\eta+\rho=-1$ and
$\eta\rho=2$. Hence
$$
(3-\eta)(3-\rho)=14,
$$
which is nonzero in characteristic 5. This proves the lemma.

For attribution, the stronger all-characteristics result is
Proposition 4.5 of Caragea, Lee, Malikiosis and Pfander,
*Principal minors of Fourier matrices of square-free order*,
arXiv:2505.24326v3, Section 4:
<https://arxiv.org/pdf/2505.24326v3>. The needed argument was
proved above; no general finite-field Chebotarev statement
is being assumed.

## 3. A bounded-degree endpoint polynomial

For the fixed count vector use the endpoint index sets
$$
I=\{sn+n-1-u:0\le u<k_s\},\qquad
J=\{tn+b:0\le b<k_t\}.                                         \tag{3.1}
$$
Let $q$ have order $7n$ in characteristic 5 and put $z=q^n$.
Direct multiplication gives
$$
q^{(sn+n-1-u)(tn+b)}
=q^{(n-1)b}z^{t(n-1)}
 z^{nst+sb-tu}q^{-ub}.                                         \tag{3.2}
$$
The first two factors depend only on the column. Treating $q$
temporarily as an independent variable $Q$, define
$$
\mathcal P_z(Q)
=Q^L\det\bigl(z^{nst+sb-tu}Q^{-ub}\bigr)_{(s,u),(t,b)}.         \tag{3.3}
$$
Every determinant monomial has exponent
$L-\sum_j u_j u_{\pi(j)}$. Rearrangement gives
$$
\sum_j u_j u_{k+1-j}
 \le\sum_j u_j u_{\pi(j)}\le L.                                \tag{3.4}
$$
To check it directly, swapping an inverted pair changes the
scalar product of two sorted lists by
$(a'-a)(b'-b)\ge0$; repeated swaps give both extrema.
Thus (3.3) is a polynomial of degree at most $W$.

Its constant coefficient is nonzero. Indeed
$$
L-\sum_j u_j u_{\pi(j)}
=\frac12\sum_j(u_j-u_{\pi(j)})^2,                              \tag{3.5}
$$
so a maximizing permutation must match equal local levels
$u=b$. Set $S_u=\{s:k_s>u\}$. On ordering rows and columns
by level, the constant coefficient of (3.3), up to one
overall ordering sign, is
$$
\prod_u\det(z^{nst+u(s-t)})_{s,t\in S_u}
=\prod_u\det(z^{nst})_{s,t\in S_u}.                            \tag{3.6}
$$
The row/column factors cancel because their index sets agree.
Since $7\nmid n$, $z^n$ is primitive of order 7. Lemma 2
makes every factor nonzero. Consequently $\mathcal P_z\ne0$
and $\deg\mathcal P_z\le W$.

## 4. Selecting a good place

For fixed primitive $z$ of order 7 in characteristic 5,
there are exactly $\varphi(n)$ primitive roots $q$ of
order $7n$ with $q^n=z$. This follows by writing them as
powers of one primitive $7n$-th root and applying the
Chinese remainder bijection to units modulo 7 and $n$.
Here $7\nmid n$; the roots remain distinct since $5\nmid n$.
A nonzero polynomial of degree $W$ cannot vanish at more
than $W$ of them. If (1.4) holds, there is therefore a
primitive $q$ for which the endpoint determinant is nonzero.
Among all $6\varphi(n)$ primitive $7n$-th roots, at most
$6W$ are bad. This is a count of actual algebraic reductions,
not a random replacement of the matrix family.

In the original path coordinates, expansion of the prescribed
quadratic kernel gives
$$
M_N(h+i,h+j)=N^{-1/2}a_i b_j\zeta_N^{cij},
\qquad c=\overline4\pmod N,                                   \tag{4.1}
$$
with root-of-unity factors $a_i,b_j$. The cross term is
$2\overline8\,ij=\overline4\,ij$; everything else separates
into row and column factors. Since $c$ is invertible,
every primitive $q$ above is realized as the reduction of
$\zeta_N^c$ at a cyclotomic prime above 5. At a good prime
the endpoint determinant of $M_N$ is a unit: its Fourier
determinant is nonzero on reduction, the chirps are units,
and $N^{-1/2}$ is a unit since $5\nmid N$.

Choose this reduction together with $i\equiv2\pmod5$.
They are compatible: as $N$ is odd, the chosen fourth and
$N$-th roots specify a primitive $4N$-th root by the
Chinese remainder identity. Extend that valuation to a
field containing all needed eigenvectors. Then
$$
v(\omega)=1,\qquad
\omega=\frac{1+2i}{1-2i}=\frac{-3+4i}{5},\qquad v(5)=1.         \tag{4.2}
$$
Indeed $1-2i$ reduces to $2\ne0$ and the product of
$1+2i$ and $1-2i$ is 5.

## 5. Integral Jacobi recurrence at the same place

Write
$$
V(q)=\cos(14\pi q)+r(q)/10
+r(q)\sin(2\pi q)/100-1/10.
$$
In each path put $D_n=\operatorname{diag}(\omega^j)_{j=0}^{n-1}$.
The exact gauged path matrix is
$$
L_s=200D_n^*A_{N,s}D_n,                                       \tag{5.1}
$$
with diagonal $d_{s,j}=200V(x_{s,j}/N)$ and internal
off-diagonal
$$
b_{s,j}=r((sn+j+1)/N),\qquad 0\le j<n-1.                      \tag{5.2}
$$
To verify the midpoint in (5.2), the $l=1$ symbol coefficient
is $\omega^{-1}r/200$; the matrix entry from $x$ to $x+1$
samples $r$ at $x+\overline2$. With $x=h+sn+j$ and
$\overline2=h$, this is $sn+j+1\pmod N$. The last edge
vanishes, and every internal edge is positive in the real
embedding. The first coordinate recursively determines
an eigenvector of a real symmetric Jacobi matrix. It cannot
vanish for a nonzero eigenvector. Since the matrix is
diagonalizable, this proves simplicity of each individual
path spectrum.

At the chosen place above 5, all $d_{s,j}$ are integral,
because
$$
200V=200\cos(14\pi q)+20r+2r\sin(2\pi q)-20
$$
has only powers of 2 and the unit $i$ in its remaining
denominators. Each internal $b_{s,j}$ is a unit. In fact
with $w=\zeta_N^{sn+j+1}$,
$$
r(w)=-\frac{(w^7-1)^2(w+1)^2}{4w^8}.                          \tag{5.3}
$$
The internal-edge condition gives $w^7\ne1$, and $w\ne-1$
because $w$ has odd order. Prime-to-5 roots retain their
exact orders on reduction, so both differences remain
nonzero. This verifies all coefficient valuations in the
same selected place, not in a different embedding.

The eigenvalues $\mu$ of $L_s$ are integral, being roots
of its monic integral characteristic polynomial. Normalize
the corresponding real eigenvectors by $\phi_\mu(0)=1$.
Then
$$
\phi_\mu(j)=
 \frac{p_j(\mu)}{b_{s,0}\cdots b_{s,j-1}},                      \tag{5.4}
$$
where the monic integral polynomials satisfy
$$
p_0=1,\quad p_1=X-d_{s,0},\quad
p_{j+1}=(X-d_{s,j})p_j-b_{s,j-1}^2p_{j-1}.
$$
All displayed denominators are units.

For any $k_s$ distinct eigenvalues, the determinant on
the first $k_s$ coordinates equals their Vandermonde
determinant times units and nonzero normalizing scalars,
so it is nonzero. Every other coordinate determinant
divided by it is integral: the alternant
$\det(p_{i_a}(\mu_b))$ is divisible by
$\prod_{a<b}(\mu_b-\mu_a)$ with integral polynomial quotient,
whereas the first-coordinate alternant is exactly that
Vandermonde. Divisibility follows by alternation in the
variables, since the distinct linear factors are prime in
the integral polynomial ring. The reversed recurrence proves
the same statement relative to the last $k_s$ coordinates.
The conclusion is valid even if some distinct eigenvalues
have equal residues. Changing to orthonormal eigenvectors
only changes column scalars, which cancel in these ratios.

## 6. The full Cauchy--Binet sum

Let $\Phi_{\mathcal E}$ contain the selected real orthonormal
eigenvectors of the $L_s$'s, extended by zero between paths.
Let $D=\bigoplus_sD_n$, and let $M_N^{\rm path}$ be the
original $M_N$ in path order. Since the actual $A_N$
eigenvectors are the gauged path vectors, exactly
$$
B_{\mathcal E}=
\Phi_{\mathcal E}^{\,T}D^{-1}M_N^{\rm path}D\Phi_{\mathcal E}.
                                                                    \tag{6.1}
$$
The transpose is appropriate because $\Phi_{\mathcal E}$
is real, and $D^*=D^{-1}$ in the complex embedding.

Double Cauchy--Binet gives
$$
\det B_{\mathcal E}
=\sum_{I',J'}
 \det(\Phi_{\mathcal E}^{\,T}[:,I'])
 \det(M_N^{\rm path}[I',J'])
 \det(\Phi_{\mathcal E}[J',:])
 \omega^{\,\sum_{J'}j-\sum_{I'}i}.                              \tag{6.2}
$$
Here the sums in the exponent are local coordinates within
paths. A term is zero unless $I'$ and $J'$ each contain
exactly $k_s$ indices from path $s$.
The unique smallest exponent comes from last row coordinates
and first column coordinates, namely the sets $I,J$ of
(3.1). It equals
$$
\chi_0=-\sum_s k_s(n-k_s).                                     \tag{6.3}
$$
Every other nonzero term has exponent $\chi_0+g$, where
$$
g=\sum_s\left(\sum I_s-\sum I'_s
              +\sum J'_s-\sum J_s\right)\ge1.                  \tag{6.4}
$$
All summands here are nonnegative integers; equality is
possible only for the two endpoint sets.

The endpoint term $T_0$ is nonzero by Sections 4 and 5.
Divide another term by $T_0$. The two eigenvector-minor
ratios are integral by Section 5. The matrix-minor ratio
is integral as well: entries of $M_N$ are integral here
and its endpoint determinant is a unit. The gauge quotient
has valuation $g$ by (4.2). Every term ratio therefore
has valuation at least 1. The ultrametric inequality for
this finite sum proves (1.5), hence Theorem 1.

## 7. Uniform range and the precise limits

The local-level list has increments 0 or 1, so
$|u_{k+1-j}-u_j|\le|k+1-2j|$. Therefore
$$
W=\frac12\sum_j(u_j-u_{k+1-j})^2
 \le \frac{k(k^2-1)}6.                                        \tag{7.1}
$$
A count-independent sufficient condition is thus
$$
\boxed{\frac{k(k^2-1)}6<\varphi(n).}                           \tag{7.2}
$$
All selected principal minors of these sizes are nonzero
in every dimension satisfying the stated coprimalities.
The place can vary between count vectors.

For every fixed count vector the condition holds for all
sufficiently large $n$ in this class. No analytic estimate
for the totient is required: for odd primes $p$,
$$
\frac{\varphi(p^a)^2}{p^a}=p^{a-2}(p-1)^2\ge1.
$$
Multiplication gives $\varphi(n)\ge\sqrt n$, which diverges.
The stronger exact range is (7.2).

The exclusions are essential to the proof. If $7\mid n$,
the Fourier blocks in (3.6) collapse, consistently with
the existing $49\mid N$ endpoint obstruction. If $5\mid n$,
the finite-field roots cease to be distinct and some hopping
coefficients cease to be units.

This theorem does not separate eigenvalues from different
Jacobi paths and does not cover all principal-minor sizes.
Those are the explicit missing inputs for completing the
large-complex-time discriminant route. No implication to
simple spectrum of $U_N$ or to $H_{\rm diag}$ has been
inserted as an assumption.

