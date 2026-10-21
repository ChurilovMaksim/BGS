> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round6_2026_10_21/r6_dense_phasechaos_isolated_all_orders.md`. Embedded SHA256: `88bc04559c4961bb0441984b1f9df5fc1d0ab2f99349d603e171a67bac7bebbe`.
> [Thematic guide](../../topics/histories.md).

# All-order isolated substitutions from operator bounded differences

21 October 2026. This note proves a signed estimate for an exact,
unmarked class of path pairs of the prescribed matrix. Every number of
isolated literal substitutions is included, up to half the cycle length;
the minimum allowed gap is two. The estimate has an explicit restriction
on the upper time band. That restriction is not discarded on the ground
that the kick is very small.

The proof does not change the original matrix, average its target
spectrum, or control the unequal-occupation remainder. Auxiliary
coordinate phases extract exactly the stated finite class. The only
published theorem used is Tropp's matrix bounded-differences inequality,
whose hypotheses and constants are checked in §3.

## 1. Exact class and result

Let $U$ be an $N\times N$ unitary matrix, $N\ge2$, and put
$$
P_{ab}=|U_{ab}|^2,\qquad J_{ab}=1/N.
$$
Assume
$$
\max_{a,b}P_{ab}\le C/N,\qquad
q=\|P-J\|_{\rm op}\le1/4,\qquad C\ge1.                 \tag{1.1}
$$
For a rooted cyclic word $x=(x_0,\ldots,x_{n-1})$, write
$$
a(x)=\prod_{i\pmod n}U_{x_i x_{i+1}},\qquad
d_v(x)=\#\{i:x_i=v\}.
$$

Let $\mathcal I_n$ be the set of ordered rooted pairs $(x,y)$
such that:

- $d(x)=d(y)$;
- $x\ne y$;
- the literal difference set $S(x,y)=\{i:x_i\ne y_i\}$ has no
  two consecutive elements modulo $n$.

For $n=1$, the cyclic adjacency condition excludes its sole position,
so $\mathcal I_1$ is empty. For every $n$, set
$$
H_n^{\rm iso}(U)=
\sum_{(x,y)\in\mathcal I_n}a(x)\overline{a(y)}.           \tag{1.2}
$$
Each pair has weight one. There is no choice of marking or rotation
quotient; roots are part of the ordered words. Repeated physical
vertices and short unchanged pieces are allowed.

The main finite estimate is
$$
\boxed{
|H_n^{\rm iso}(U)|
\le 2N(7/8)^n+Nq^n
+4N^2\exp\!\left(qn-\frac{N}{512C^2}\right),
\qquad n\ge1.
}                                                       \tag{1.3}
$$
Thus, if $B>0$ satisfies
$$
Bq\le\frac1{1024C^2},                                  \tag{1.4}
$$
then
$$
\boxed{
\frac1{N^2}\sum_{1\le n\le BN}|H_n^{\rm iso}(U)|
\le\frac{43}{3N}
+4BN\exp\!\left(-\frac{N}{1024C^2}\right).
}                                                       \tag{1.5}
$$
In particular the signed weighted class tends to zero after the
pair-statistic normalization for any uniformly bounded weights
supported in that time band. The bound is on the modulus after each
complete signed sum in (1.2), not on the sum of its individual
amplitude moduli.

There is a stronger weighted estimate with a smaller explicit band:
if
$$
Bq\le\frac1{4096C^2},
$$
then
$$
\boxed{
\frac1{N^2}\sum_{1\le n\le BN}|H_n^{\rm iso}(U)|
\le\frac{32(2C-1)}{3N^2}
+6BN\exp\!\left(-\frac{N}{4096C^2}\right).
}                                                       \tag{1.6}
$$
This refinement uses Hilbert--Schmidt norms for two factors in each
complete cyclic word, and is proved in §5.1.

## 2. A small operator change from one inner phase

Let $z_1,\ldots,z_N$ be independent uniform unit complex numbers,
and define
$$
V(z)=U\operatorname{diag}(z)U,\quad
R(z)_{ab}=|V(z)_{ab}|^2,\quad
D(z)=R(z)-P^2.                                         \tag{2.1}
$$
Every $V(z)$ is unitary, so $R(z)$ is doubly stochastic.
Coordinate phase orthogonality gives $\mathbb ER=P^2$, hence
$\mathbb ED=0$.

Suppose only $z_v$ changes, by $\delta z$. Write $c=U_{:v}$
and $r=U_{v:}$, as column and row vectors, respectively. Then
$$
V'=V+\delta z\,cr.
$$
The exact scalar identity
$$
|V'|^{\circ2}-|V|^{\circ2}
=(V'-V)\circ\overline{V'}+V\circ(\overline{V'}-\overline V)
$$
gives the exact matrix identity
$$
R'-R
=\delta z\,\operatorname{diag}(c)\,\overline{V'}\,
                 \operatorname{diag}(r)
+\overline{\delta z}\,
 \operatorname{diag}(\overline c)\,V\,
                 \operatorname{diag}(\overline r).       \tag{2.2}
$$
Here a diagonal matrix formed from a row means the diagonal with
those same coordinate entries; no transpose or conjugation is
implicitly added.

Both middle matrices in (2.2) have norm one. Moreover
$$
\|\operatorname{diag}(c)\|,
\|\operatorname{diag}(r)\|\le\sqrt{C/N}.
$$
Since $|\delta z|\le2$, this proves the deterministic bound
$$
\boxed{\|R(z')-R(z)\|\le4C/N.}                          \tag{2.3}
$$
It holds for every pair of phase vectors differing in one coordinate.
No typical-phase or independence assumption enters this step.

## 3. Published concentration theorem and verified hypotheses

The external input is:

Joel A. Tropp, *User-Friendly Tail Bounds for Sums of Random Matrices*,
Foundations of Computational Mathematics **12** (2012), 389--434,
Corollary 7.5, printed page 428.
DOI: https://doi.org/10.1007/s10208-011-9099-z .
Published full text:
https://link.springer.com/content/pdf/10.1007/s10208-011-9099-z.pdf .

The corollary concerns a self-adjoint matrix-valued function of
independent variables. If changing coordinate $v$ changes its value
by a self-adjoint matrix whose square is bounded by a fixed $A_v^2$,
then its largest-eigenvalue deviation has upper bound
$$
d_{\rm mat}\exp[-s^2/(8\sigma^2)],\qquad
\sigma^2=\left\|\sum_v A_v^2\right\|.                   \tag{3.1}
$$
The published statement, normalization, and page number were checked
directly, including its allowance of arbitrary independent variables.

Apply it to the self-adjoint dilation
$$
\mathcal H(z)=
\begin{pmatrix}0&R(z)\\R(z)^*&0\end{pmatrix}.
$$
This is a bounded measurable function of the independent phases,
with dimension $d_{\rm mat}=2N$.
Its change under one coordinate replacement has norm at most $4C/N$
by (2.3), hence its square is bounded in the positive-semidefinite
order by $(4C/N)^2 I_{2N}$. The fixed matrices
$$
A_v=(4C/N)I_{2N}
$$
therefore satisfy every hypothesis of the corollary, with
$\sigma^2=16C^2/N$.
The centered dilation is the dilation of $D(z)$, and its largest
eigenvalue is exactly $\|D(z)\|$. Thus
$$
\boxed{
\mathbb P\{\|D(z)\|\ge s\}
\le2N\exp\!\left(-\frac{Ns^2}{128C^2}\right),
\qquad s\ge0.
}                                                       \tag{3.2}
$$
No second tail or additional dimension factor is needed.
The trivial upper bound 1 may of course be used when the displayed
right side exceeds 1.

This controls high operator moments through a genuine exponential
tail, rather than extrapolating a fourth-moment calculation.
For example, if $L_N=128C^2\log(2N)/N$, then integration of (3.2)
gives
$$
\mathbb E\|D\|^4
\le L_N^2+\frac{256C^2L_N}{N}
+2\left(\frac{128C^2}{N}\right)^2.                     \tag{3.3}
$$
The proof splits the integral of $2t\,\mathbb P\{\|D\|^2>t\}$
at $t=L_N$. Equation (3.3) is an auxiliary bound and is not the
mechanism used to control arbitrarily many substitutions below.

## 4. The exact rooted-pair transfer, without a tiling multiplicity

Work in the doubled space with basis indexed by $(a,b)$, and set
$$
Q=U\otimes\overline U,\qquad
Z^{(2)}(z)_{(a,b),(a,b)}=z_a\overline z_b.
$$
Let $M$ be the orthogonal projection onto the $N$-dimensional
subspace with $a=b$, and $O=I-M$. The matrix
$$
\mathcal A(z)
=Z^{(2)}Q-OZ^{(2)}QO                                  \tag{4.1}
$$
forbids exactly those transitions for which both the old and new
pair states are off the diagonal.

Expanding the trace of its $n$-th power therefore gives
$$
\operatorname{Tr}\mathcal A(z)^n
=\sum_{\substack{x,y\\S(x,y)\text{ has no cyclic neighbors}}}
a(x)\overline{a(y)}\,z^{d(x)-d(y)}.                     \tag{4.2}
$$
Every term is one ordered pair of rooted cyclic words, with its
original phase and multiplicity one. Integrating the phases keeps
exactly equal occupations. The terms with empty difference set
are $x=y$ and sum to $\operatorname{Tr}P^n$. Consequently
$$
H_n^{\rm iso}
=\mathbb E\operatorname{Tr}\mathcal A(z)^n
 -\operatorname{Tr}P^n.                               \tag{4.3}
$$

The large doubled matrix has an exact smaller trace representation.
Relative to $M\oplus O$, write
$$
\mathcal A(z)=
\begin{pmatrix}P&B\\C(z)&0\end{pmatrix}.
$$
The blocks are
$$
B_{a,(u,v)}=U_{au}\overline{U_{av}},\qquad
C(z)_{(u,v),b}
=z_u\overline z_v U_{ub}\overline{U_{vb}},
\qquad u\ne v.
$$
Therefore
$$
B C(z)=
\sum_{u\ne v}z_u\overline z_v
\bigl[U_{au}\overline{U_{av}}U_{ub}\overline{U_{vb}}\bigr]_{a,b}
=D(z).                                                \tag{4.4}
$$
The missing terms $u=v$ are exactly $P^2$.

Define the $2N\times2N$ companion
$$
\mathcal T(z)=\begin{pmatrix}P&D(z)\\I&0\end{pmatrix}.    \tag{4.5}
$$
Finite block elimination gives
$$
\det(I-s\mathcal A(z))
=\det(I-sP-s^2D(z))
=\det(I-s\mathcal T(z)).
$$
Logarithmic differentiation at $s=0$, as a formal power series,
proves
$$
\operatorname{Tr}\mathcal A(z)^n
=\operatorname{Tr}\mathcal T(z)^n,\qquad n\ge1.          \tag{4.6}
$$
One may verify the formal trace identity directly by factoring the
finite characteristic polynomial into its eigenvalue factors.
No asymptotic determinant approximation is being used.

Equations (4.2)--(4.6) include the dense alternating difference sets,
the small values of $n$, and all cyclic roots. In particular there
is no need to count marked gap compositions and then divide by a
presumed number of markings.

## 5. Exact spectral-radius bounds for the companion

Let $e=N^{-1/2}(1,\ldots,1)$. Both $P$ and $R(z)$ preserve
$\mathbb Ce$ and $e^\perp$. The matrix $D(z)$ annihilates $e$
on both sides. Thus the companion decomposes into the constant block
$$
\begin{pmatrix}1&0\\1&0\end{pmatrix}
$$
and a $2(N-1)$-dimensional block $\mathcal T_0(z)$.
The first block has trace of every positive power equal to 1.

Write $P_0=P|_{e^\perp}$, $D_0=D|_{e^\perp}$. If $\lambda\ne0$
is an eigenvalue of $\mathcal T_0$, its eigenvector equations give
$$
\lambda^2 y=\lambda P_0y+D_0y,\qquad y\ne0.
$$
Hence, putting $d=\|D(z)\|$,
$$
|\lambda|^2\le q|\lambda|+d.
$$
Zero eigenvalues cause no problem. With
$$
r(q,d)=\frac{q+\sqrt{q^2+4d}}2,
$$
all eigenvalues obey $|\lambda|\le r(q,d)$, and therefore
$$
|\operatorname{Tr}\mathcal T(z)^n-1|
\le2(N-1)r(q,d)^n.                                     \tag{5.1}
$$
This uses the sum of eigenvalue powers with algebraic multiplicity;
neither diagonalizability nor normality is required.

Every doubly stochastic matrix is an $\ell^2$ contraction:
Jensen applied row by row and then column stochasticity prove this
directly. On $e^\perp$,
$$
\|D(z)\|=\|R(z)-P^2\|\le1+q^2.
$$
For $0\le q\le1$,
$$
r(q,1+q^2)\le1+q,                                     \tag{5.2}
$$
since substituting $1+q$ into $r^2-qr-(1+q^2)$
gives $q-q^2\ge0$.
On the event $\|D(z)\|\le1/2$, assumption $q\le1/4$ gives
$$
r(q,\|D\|)\le7/8.                                     \tag{5.3}
$$
Indeed at $r=7/8$ the polynomial $r^2-qr-1/2$ is at
least $3/64>0$.

Combine (5.1)--(5.3) with (3.2) at $s=1/2$:
$$
\mathbb E|\operatorname{Tr}\mathcal T(z)^n-1|
\le2N(7/8)^n
+4N^2\exp\!\left(qn-\frac{N}{512C^2}\right).             \tag{5.4}
$$
Finally,
$$
|\operatorname{Tr}P^n-1|
=|\operatorname{Tr}P_0^n|\le(N-1)q^n.
$$
Equations (4.3), (4.6), and (5.4) prove (1.3).

Summing the first two terms of (1.3) over all positive $n$
costs at most
$$
2N\frac{7/8}{1-7/8}
+N\frac{q}{1-q}
\le14N+N/3=\frac{43}3N.
$$
Under (1.4), the last term summed through $BN$ is at most
$$
4BN^3e^{-N/(1024C^2)}.
$$
This proves (1.5).

### 5.1. Hilbert--Schmidt refinement after complete cyclic summation

Set $E=P-J$. Doubly stochasticity gives
$$
\|E\|_{\rm HS}^2=\sum_{a,b}P_{ab}^2-1\le C-1.
$$
For $u\ne v$, write $A_{uv}$ for the coefficient matrix of
$z_u\overline z_v$ in (4.4). It has rank one and
$$
\|A_{uv}\|_{\rm HS}^2
=\left(\sum_aP_{au}P_{av}\right)
 \left(\sum_bP_{ub}P_{vb}\right).
$$
The second parenthesis is at most $C/N$, while
$$
\sum_{u,v}\sum_aP_{au}P_{av}=N.
$$
All characters $z_u\overline z_v$, $u\ne v$, are distinct.
Exact phase orthogonality therefore proves
$$
\mathbb E\|D(z)\|_{\rm HS}^2
=\sum_{u\ne v}\|A_{uv}\|_{\rm HS}^2\le C.              \tag{5.5}
$$
In particular, for
$$
M(z)=\max\{\|E\|_{\rm HS}^2,\|D(z)\|_{\rm HS}^2\},
\qquad
\mathbb EM(z)\le2C-1.                                 \tag{5.6}
$$

Let
$$
G_n(z)=\operatorname{Tr}\mathcal T(z)^n
       -\operatorname{Tr}P^n.
$$
Its finite cyclic expansion is indexed by the nonempty independent
difference sets of the $n$-cycle. A set of size $r$ contributes
a cyclic matrix word with $n-2r$ factors $P$ and $r$ factors
$D(z)$. Since $D J=J D=0$, and $EJ=JE=0$, all factors $P$
in such a nonempty word may be replaced by $E$.
This replacement is exact. Expanding $P=E+J$, every term
containing $J$ vanishes when followed cyclically to its first
factor $E$ or $D$.

On the good event $\|D(z)\|\le1/4$, all these factors have
operator norm at most $1/4$. For $n\ge3$, the number
$f=n-r$ of factors is at least two. Choose any two factors in
Hilbert--Schmidt norm and the rest in operator norm. To justify
this directly, split the cyclic word into products $A,B$, each
beginning with one of the chosen factors. Trace Cauchy--Schwarz
gives $|\operatorname{Tr}AB|\le\|A\|_{\rm HS}\|B\|_{\rm HS}$;
bounding the remaining factors in each product in operator norm
then gives
$$
|\operatorname{Tr}(F_1\cdots F_f)|
\le M(z)(1/4)^{f-2}.                                  \tag{5.7}
$$
This argument makes no assumption about the normality or sign of
the factors.

For scalar nonnegative $a,b$, the sum of cyclic weights, assigning
$a$ to each single edge and $b$ to each two-edge jump, is
$$
F_n(a,b)=\operatorname{Tr}
\begin{pmatrix}a&b\\1&0\end{pmatrix}^{\!n}.
$$
The same exact trace expansion as (4.2)--(4.6), now with scalar
coefficients, includes each independent subset once. Its nonempty
part is $Z_n(a,b)=F_n(a,b)-a^n$. The generating function is
$$
\sum_{n\ge1}F_n(a,b)s^n
=\frac{as+2bs^2}{1-as-bs^2}.
$$
At $a=b=1/4$, it converges at $s=1$ and gives
$$
\sum_{n\ge3}Z_n(1/4,1/4)
=\frac{1/4+2(1/4)}{1-1/4-1/4}
 -\frac{1/4}{1-1/4}-2(1/4)
=\frac23.                                             \tag{5.8}
$$
Thus (5.7), followed by (5.6) and Tonelli for nonnegative bounds,
proves
$$
\sum_{n\ge3}
\left|\mathbb E\!\left[
 \mathbf1_{\{\|D\|\le1/4\}}G_n(z)\right]\right|
\le16(2C-1)\,\frac23.                                 \tag{5.9}
$$
This does not sum individual path-amplitude moduli: the factors
$D$ and the cyclic transfer have already performed their complete
signed physical sums.

On the complementary event, (5.1)--(5.2) and the bound for
$\operatorname{Tr}P^n-1$ give
$$
|G_n(z)|\le3N(1+q)^n.
$$
By (3.2) at $s=1/4$,
$$
\left|\mathbb E[
 \mathbf1_{\{\|D\|>1/4\}}G_n(z)]\right|
\le6N^2e^{qn-N/(2048C^2)}.                            \tag{5.10}
$$
The complete $H_1^{\rm iso}$ and $H_2^{\rm iso}$ vanish exactly.
For $n=1$ there is no allowed nonempty difference set. For $n=2$
such a set would contain one position, which cannot preserve the
occupation vector; equivalently $\mathbb ED=0$.
The same reason gives $H_3^{\rm iso}=0$, though that improvement
is not needed in (5.9).

Summing (5.10) through $BN$, using
$Bq\le1/(4096C^2)$, and combining with (5.9) proves (1.6).

## 6. Application to the exact original family and its finite band

The frozen kernel and oscillatory proofs give, for all sufficiently
large odd $N$,
$$
\max P_N\le9/N,\qquad
\|P_N-J_N\|\le40000t+o(1),\qquad
t=\frac{10^{-80}}{2\pi}.
$$
The source files and hashes are:

- research_round5_2026_10_21/dual_physical_four_branch_kernel.md,
  0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c;
- research_round5_2026_10_21/root_oscillatory_matrix_cancellation.md,
  ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d.

Crucially, the latter estimate has a fixed positive upper floor.
It does not assert $q_N\to0$.
Since $40000t=(2/\pi)10^{-76}<10^{-76}$, one may fix
$$
\overline q=10^{-76}
$$
and use $q_N\le\overline q$ for every sufficiently large odd $N$.
Consequently the present theorem applies, with the unchanged kick,
to every fixed band satisfying
$$
\boxed{B\le B_{\rm iso}:=\frac{10^{76}}{82944}.}         \tag{6.1}
$$
The stronger bound (1.6), with coefficient $544/3$ in front of
$N^{-2}$, applies whenever
$$
B\le\frac{10^{76}}{331776}.                            \tag{6.2}
$$
The threshold is finite. Its large numerical size does not meet the
quantifier over arbitrary fixed Fourier bands in $H_{\rm diag}$.
There is no quantitative onset dimension claimed for the eventual
original-family norm bound.

This is an all-order cancellation theorem for the exact isolated,
equal-occupation pair class, including the previously problematic
minimum gap two. It does not control adjacent substitutions,
general reconnections, or the remaining unequal-occupation
contribution $\Omega_n(U_N)$.

## 7. Why a universal polynomial cap cannot be presumed

The global companion estimate cannot be replaced by a polynomial
in time solely because the original $U$ is unitary. Here is an exact
two-dimensional illustration.
For $0<q\le1/4$, let
$$
U_q=
\begin{pmatrix}
\sqrt{(1+q)/2}&\sqrt{(1-q)/2}\\
\sqrt{(1-q)/2}&-\sqrt{(1+q)/2}
\end{pmatrix}.
$$
It is real orthogonal, with
$$
P=\begin{pmatrix}(1+q)/2&(1-q)/2\\
                 (1-q)/2&(1+q)/2\end{pmatrix}.
$$
Its nonconstant mode has eigenvalue $q$, and the corresponding
mode of $D(z)$ is
$$
d=(1-q^2)\cos\varphi,\qquad
\varphi=\arg z_1-\arg z_2.
$$
The mean-zero companion trace is the scalar polynomial
$$
F_n(q,d)=\operatorname{Tr}
\begin{pmatrix}q&d\\1&0\end{pmatrix}^{\!n}
=\sum_{r=0}^{\lfloor n/2\rfloor}
\frac{n}{n-r}\binom{n-r}{r}q^{n-2r}d^r,\quad n\ge1.    \tag{7.1}
$$
Its coefficients follow either by expanding the two eigenvalue
powers or by the recurrence $F_n=qF_{n-1}+dF_{n-2}$,
with $F_0=2$, $F_1=q$.

Odd powers of $\cos\varphi$ integrate to zero. For even $r$,
$$
\mathbb E\cos^r\varphi
=2^{-r}\binom{r}{r/2}\ge\frac1{r+1}\ge\frac1{n+1}.
$$
The first inequality holds because the central binomial coefficient
is the largest among the $r+1$ coefficients summing to $2^r$.
Thus, for even $n$,
$$
\mathbb EF_n(q,(1-q^2)\cos\varphi)
\ge\frac{F_n(q,1-q^2)+F_n(q,-(1-q^2))}{2(n+1)}
\ge\frac{\lambda_+(q)^n-2}{2(n+1)},                   \tag{7.2}
$$
where
$$
\lambda_+(q)=\frac{q+\sqrt{4-3q^2}}2>1.
$$
For the last step, the roots for the negative second argument
have modulus $\sqrt{1-q^2}<1$; the positive second argument
has positive root $\lambda_+>1$, and its other root contributes
nonnegatively at even $n$.
Therefore
$$
H_n^{\rm iso}(U_q)
\ge\frac{\lambda_+(q)^n-2}{2(n+1)}-q^n
\quad(n\text{ even}),                                \tag{7.3}
$$
which grows exponentially at fixed dimension.

This is not a counterexample to a growing-dimension theorem for
the original family, and does not prove that the band restriction
(6.1) is intrinsic there. It proves only that a blanket polynomial
cap in time does not follow from finite unitarity, even with
arbitrarily small positive $q$. A further original-family
argument would be needed to remove the rare-phase/time-growth
competition in (5.4).

## 8. Remaining obligations

No inference about the original full spectrum has been made from
the auxiliary phase law. The phase integral in (4.3) is an exact
coefficient extraction for one explicitly defined signed class.
In particular the general same-occupation time-band bound cannot
be used to bound an arbitrary signed subset such as (1.2).

The first unproved extension within this route is quantitative
control of
$$
\mathbb E\operatorname{Tr}\mathcal T_0(z)^n
$$
on every fixed band $n\le BN$, with no bound on $B$, or a
different identity that avoids the rare-phase growth estimate.
Even such an extension would leave adjacent literal differences
and the general unequal-occupation remainder.

No uniform Abel tail for $H_n^{\rm iso}$ is asserted: at fixed
$N$, the factor $e^{qn}$ in the available estimate eventually
dominates an Abel weight at scale $n/N$. The established Abel
tail for the full nonnegative occupation sector does not dominate
this signed subseries term by term.

## 9. Exact finite verification

The companion r6_dense_phasechaos_exact_checks.py uses integers,
rational numbers, and formal Laurent polynomials. In particular,
its coefficient extraction does not approximate a torus integral
by a finite phase grid.

For two rational orthogonal matrices, it compares direct rooted-pair
enumeration with the companion trace as a polynomial in all coordinate
phase characters and a further variable recording the number of
literal differences. Thus the verification checks every phase
coefficient and every substitution order separately:

| Matrix numerator / denominator | Cycle lengths | Rooted pairs checked | Nonempty equal-occupation pairs |
| --- | --- | ---: | ---: |
| $\begin{pmatrix}21&20\\20&-21\end{pmatrix}/29$ | 1 through 10 | 182,270 | 40,192 |
| $\begin{pmatrix}-4&7&-4\\1&-4&-8\\-8&-4&1\end{pmatrix}/9$ | 1 through 7 | 334,281 | 33,156 |

The checks include the maximum possible density of independent
differences, the cyclic boundary, the exceptional small lengths,
and coefficient signs. The actual matrices are verified orthogonal
by exact multiplication. The direct enumeration also verifies that
the generated selected set equals the literal difference set of
the resulting pair, so no presentation multiplicity is suppressed.

Additional exact checks comprise:

- 900 positive-semidefinite certificates for the one-coordinate
  operator bound $\|\Delta R\|\le4/N$, using $4\times4$ and
  $8\times8$ normalized Hadamard matrices and unit complex phases;
  the certificates use rational elimination, not floating eigenvalues;
- the Hilbert--Schmidt coefficient bounds for the two rational
  matrices;
- the scalar independent-set trace identity through length 14 and
  its exact summed value $2/3$;
- 49 cases of the scalar recurrence and the coefficientwise lower
  bound used in the fixed-dimension example.

All assertions passed. The companion output is stored in
r6_dense_phasechaos_exact_checks_result.md. The published
concentration theorem and the analytic arguments above, rather
than these finite computations, establish the dimension-dependent
bounds. No numerical spectrum at the fixed kick is used as
asymptotic evidence.
