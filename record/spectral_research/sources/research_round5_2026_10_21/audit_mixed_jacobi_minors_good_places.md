> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_mixed_jacobi_minors_good_places.md`. Embedded SHA256: `8f437fc323ccb897eb19888a191f99e0c6ece08d6f2c92fc24c51917be8d4c20`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/algebra.md).

# Independent audit: actual mixed Jacobi overlap minors

Date: 21 October 2026. Auditor: /root/audit_uniform_word_r4.

Frozen target: arithmetic_mixed_jacobi_minors_good_places.md.

Target SHA256:
0eb94e2984dbdbc475b25897194404808255ba6b2da9703d2aef7f395db1bf55.

The target hash was independently recomputed. The entire argument in
Sections 1--7 was reconstructed; earlier audit statuses were not used as
proof. The frozen target was not changed.

## Verdict and one representative qualification

The stated nonvanishing and valuation theorem is proved for the stated
class $N=7n$, $n$ odd, $\gcd(n,35)=1$, and $W<\varphi(n)$.
The place can indeed be chosen from the count vector alone, and the
whole Cauchy--Binet sum, rather than an isolated coordinate determinant,
is controlled.

There is a harmless qualification to the literal matrix identity (6.1).
Section 1 permits arbitrary complex phases on normalized path
eigenvectors; (6.1) is literal after choosing the real-gauged
representatives. If the original selected vectors have phases in a
diagonal unitary $S$, their matrix is $S^*B_{\mathrm{real}}S$.
Consequently its determinant is unchanged. Each individual
Cauchy--Binet term is also unchanged: the two selected-column phase
products are $\overline{\det S}$ and $\det S$, whose product is one.
Thus both $\det B_{\mathcal E}$ and $T_0$ are phase invariant, even
when the initially chosen phases are not algebraic. The valuation
statement concerns the algebraic scalar computed using real-gauged
representatives. No restriction on the selected phases is needed.

No other gap was found in the theorem. The detailed reconstruction
below supplies the relevant normalization, divisibility, and residue
field checks.

## 1. The characteristic-5 Fourier lemma

Let $z$ be primitive of order seven in an algebraic closure of
$\mathbb F_5$, and $F_{ab}=z^{ab}$. The geometric-sum identity
gives
$$
F^{-1}=7^{-1}(z^{-ab}).
$$
Since $7$ is invertible, complementary minors reduce all sizes to
sizes at most three, for both $z$ and the primitive root $z^{-1}$.
The empty and full minors are included.

A two-by-two minor is a nonzero root-of-unity factor times
$1-z^{(a-a')(b-b')}$. At size three, if one index set is an
arithmetic progression, extracting row or column factors leaves a
Vandermonde on three distinct roots.

Every nonarithmetic triple is affinely equivalent to
$\{0,1,3\}$: in the normalized triple $\{0,1,t\}$, the
arithmetic cases are $t=2,4,6$, and multiplication by five interchanges
the remaining types $t=3,5$. Independent affine changes of row and
column indices only introduce nonzero row/column factors and replace
$z$ by another primitive power. In the remaining case,
$$
\det(z^{ab})_{a,b\in\{0,1,3\}}
=3z^3-z^6-z^2-z
=z^3(3-z^3-z^5-z^6).
$$
Writing
$\eta=z+z^2+z^4$, $\rho=z^3+z^5+z^6$, direct multiplication
gives $\eta+\rho=-1$, $\eta\rho=2$. Therefore
$$
(3-\eta)(3-\rho)=14\ne0\quad\text{in characteristic five}.
$$
This proves the precise finite-field input internally. The target's
literature attribution is not needed as a theorem input.

## 2. The endpoint polynomial and its nonzero constant term

For row label $i=sn+n-1-u$ and column label $j=tn+b$, direct
integer expansion gives
$$
q^{ij}
=q^{(n-1)b}z^{t(n-1)}
  z^{nst+sb-tu}q^{-ub},\qquad z=q^n.
$$
The first two factors depend only on the column. The multisets of
levels $u$ and $b$ agree. Thus in
$$
\mathcal P_z(Q)
=Q^L\det(z^{nst+sb-tu}Q^{-ub})
$$
each determinant monomial has exponent
$$
L-\sum_{j=1}^k u_j u_{\pi(j)}
\in[0,W].
$$
The two endpoints of this interval follow from the usual interchange
proof of rearrangement. In particular, no negative exponents remain.

More precisely,
$$
L-\sum_j u_j u_{\pi(j)}
=\frac12\sum_j(u_j-u_{\pi(j)})^2.
$$
An exponent-zero monomial must therefore match equal levels exactly.
Ordering rows and columns by level, the constant coefficient is, up
to one overall sign,
$$
\prod_u
\det(z^{nst+u(s-t)})_{s,t\in S_u}
=\prod_u\det((z^n)^{st})_{s,t\in S_u},
\qquad S_u=\{s:k_s>u\}.
$$
The factors $z^{us}$ and $z^{-ut}$ cancel because the row and
column index sets of each block are identical. Since $7\nmid n$,
$z^n$ is again primitive of order seven, so Section 1 makes every
factor nonzero. Hence
$$
\mathcal P_z\ne0,\qquad \deg\mathcal P_z\le W.
$$
Descending versus increasing order within the endpoint row blocks
only changes the overall sign; it has no bearing on nonvanishing or
valuation.

## 3. Root counting and compatibility of the place

Fix a primitive seventh root $z$ in characteristic five. There are
exactly $\varphi(n)$ primitive $7n$-th roots $q$ with $q^n=z$.
Indeed, writing $q=q_0^a$, the condition fixes one nonzero class of
$a$ modulo seven, while $a$ can be any unit modulo $n$.
The Chinese remainder bijection applies because $\gcd(7,n)=1$.
All these roots are distinct because $5\nmid 7n$.

Since $\deg\mathcal P_z\le W<\varphi(n)$, at least one such root
has $\mathcal P_z(q)\ne0$. The same argument bounds the number of
bad primitive roots, over all six choices of $z$, by $6W$.
This is an existence argument for a valuation of the original
algebraic entries; no matrix, gauge, or spectral parameter is changed.

For completeness, a primitive $N$-th root in characteristic five
is a root of the reduction of $\Phi_N$: the factorization
$X^N-1=\prod_{d\mid N}\Phi_d(X)$ remains squarefree when
$5\nmid N$, and its primitive roots cannot occur in factors with
proper divisor $d$. Evaluating the cyclotomic integer ring at the
chosen root therefore gives a prime over five.

The exact kernel in path coordinates has the form
$$
M_N(h+i,h+j)
=N^{-1/2}a_i b_j\zeta_N^{cij},
\qquad c=\overline4\bmod N,
$$
where $a_i,b_j$ are roots of unity. This follows by expanding the
quadratic form; its mixed coefficient is $2\overline8=\overline4$.
Since $c$ is a unit modulo $N$, the chosen $q$ can be realized
as the reduction of $\zeta_N^c$. The endpoint Fourier determinant
then has nonzero reduction. The chirps and $N^{-1/2}$ have
valuation zero, so the endpoint minor of $M_N$ is a unit.

The reduction $i\mapsto2$ is compatible with this choice. The
orders four and $N$ are coprime, and the map from primitive
$4N$-th roots to prescribed primitive roots of orders four and
$N$ is bijective by the Chinese remainder theorem. Hence both
reductions extend to a single cyclotomic place. At that place,
$$
\omega=\frac{1+2i}{1-2i},\qquad v(5)=1,\qquad v(\omega)=1.
$$
Indeed $1-2i\equiv2\ne0\pmod5$, whereas
$(1+2i)(1-2i)=5$. The place may subsequently be extended to one
finite field containing all path eigenvalues and real normalized
eigenvectors; no later choice of selected eigenvalues alters the
cyclotomic place.

## 4. The original Jacobi blocks and integral endpoint ratios

The $l=1$ Fourier coefficient of the $p$-dependent term is
$\omega^{-1}r/200$. The entry from $x$ to $x+1$ samples $r$
at $x+\overline2$. With $h=(N+1)/2$ and
$x=h+sn+j$, one has
$$
x+h\equiv sn+j+1\pmod N.
$$
Conjugating by $D_n=\operatorname{diag}(\omega^j)$ removes the
constant edge phase, because
$\omega^{-j}\omega^{-1}\omega^{j+1}=1$. Thus the target's
$$
L_s=200D_n^*A_{N,s}D_n
$$
is the real symmetric Jacobi matrix with the stated diagonal and
offdiagonal coefficients.

For $w=\zeta_N^{sn+j+1}$,
$$
r(w)=-\frac{(w^7-1)^2(w+1)^2}{4w^8}.
$$
For an internal edge $1\le j+1\le n-1$, $w^7\ne1$, since
$N\mid7(sn+j+1)$ would imply $n\mid j+1$. Also $w\ne-1$,
since its order is odd. Roots of unity with order prime to five
retain their exact order after reduction. Therefore every internal
hopping coefficient is a unit at the same selected place.
The diagonal is integral because
$$
200V=200\cos(14\pi q)+20r+2r\sin(2\pi q)-20
$$
has only powers of two and the unit $i$ in its remaining
denominators.

Each real Jacobi path has simple spectrum: a first coordinate
determines the eigenvector by recursion, cannot vanish in a
nonzero eigenvector, and real symmetry supplies diagonalizability.
All its eigenvalues $\mu$ are integral, because they satisfy its
monic integral characteristic polynomial. Equivalently, a root of
negative valuation would make the leading monomial the unique term
of minimal valuation, which is impossible.

With first coordinate normalized to one,
$$
\phi_\mu(j)
=\frac{p_j(\mu)}{b_0\cdots b_{j-1}},
$$
where the $p_j$ are monic integral polynomials of degree $j$.
For $k_s$ distinct eigenvalues, the determinant of the first
$k_s$ coordinates is a nonzero Vandermonde times units and common
column normalizers. For any other coordinate set, its numerator
alternant is divisible by this Vandermonde over the integral
coefficient ring. One does not need that ring to be a unique
factorization domain: each difference $X_b-X_a$ is a prime
element in the polynomial ring, because its quotient is a domain;
these monic linear factors are pairwise nonassociate, so their
product divides the alternant. Evaluation at integral eigenvalues
then shows the coordinate-minor ratio is integral.

This division is exact in characteristic zero. Distinct
eigenvalues may have identical residues without invalidating it.
Reversing the Jacobi recurrence proves the corresponding ratio
statement relative to the last $k_s$ coordinates.
Orthonormalizing the selected eigenvectors introduces common
nonzero column factors, which cancel in every ratio. They are not
being asserted to be units. The arbitrary complex-phase issue is
handled by the determinant invariance stated at the start.

## 5. The full determinant and strict valuation dominance

Use real-gauged representatives as justified above. The exact
double Cauchy--Binet expansion is
$$
\det B_{\mathcal E}
=\sum_{I',J'}
\det(\Phi^T[:,I'])\det(M_N^{\rm path}[I',J'])
\det(\Phi[J',:])
\omega^{\sum_{J'}j-\sum_{I'}i}.
$$
The sums in the exponent use local path coordinates. The block
supports of the selected eigenvectors imply that a nonzero term
must contain exactly $k_s$ row and $k_s$ column coordinates in
each path. This remains true even when eigenvalues from different
paths coincide.

Within each path the row-coordinate sum is uniquely maximized by
the last $k_s$ coordinates and the column-coordinate sum uniquely
minimized by the first $k_s$ coordinates. Their exponent is
$$
\chi_0=-\sum_s k_s(n-k_s).
$$
Every other term has exponent $\chi_0+g$, for an integer
$$
g=\sum_s
\left(\sum I_s-\sum I'_s+\sum J'_s-\sum J_s\right)\ge1.
$$
The endpoint row and column eigenvector determinants are nonzero
by the recurrence argument; the endpoint $M_N$ determinant is a unit by the
good-place construction. Thus the endpoint term $T_0$ is nonzero.

Divide each other term by $T_0$. Both eigenvector-minor ratios
are integral. The matrix-minor ratio is integral, since every
entry of $M_N$ is integral and its endpoint determinant is a
unit. Finally $\omega^g$ has valuation $g\ge1$. Hence the
finite sum of all nonendpoint ratios has valuation at least one:
$$
v\!\left(\frac{\det B_{\mathcal E}}{T_0}-1\right)\ge1.
$$
In particular $\det B_{\mathcal E}/T_0$ is a unit and cannot
vanish. There is no estimate of individual terms followed by an
unjustified archimedean cancellation claim: the dominance is in a
specified nonarchimedean valuation and applies to the complete
finite determinant sum.

## 6. Range, edge cases, and exact unresolved implication

The sorted list $u_j$ has increments zero or one, so
$$
W=\frac12\sum_j(u_j-u_{k+1-j})^2
\le\frac12\sum_j(k+1-2j)^2
=\frac{k(k^2-1)}6.
$$
This verifies the count-independent sufficient range in the
target. Also $0\le W\le L$, so $L<\varphi(n)$ suffices.
For odd $n$, multiplicativity and
$$
\frac{\varphi(p^a)^2}{p^a}=p^{a-2}(p-1)^2\ge1
$$
give $\varphi(n)\ge\sqrt n$. Thus every fixed count vector is
eventually included in the allowed coprime dimension class.

For $k=0$, the determinant and endpoint term are one, the
residual is zero, and its valuation is $+\infty$. For $n=1$
there are no internal Jacobi edges; the recurrence statements are
vacuous, $W=0<\varphi(1)=1$, and the result reduces to the
nonvanishing characteristic-five Fourier minors of order seven.
Selecting all coordinates of an individual path causes no
additional difficulty. The exclusions $7\mid n$ and $5\mid n$
are used exactly where stated: respectively in the primitive
order-seven constant blocks and in distinct prime-to-five
reductions and unit hopping coefficients.

This is a theorem about actual principal overlap minors in the
basis assembled from the individual path eigenvectors. It is not
a theorem about arbitrary rotations inside repeated global
eigenspaces of $A_N$. It neither separates the spectra of
different paths nor supplies all principal-minor sizes, and it
does not cover all odd dimensions. These are explicit missing
inputs for the proposed discriminant route; simplicity of the
full $U_N$, let alone $H_{\rm diag}$, is not a consequence of
the result audited here.
