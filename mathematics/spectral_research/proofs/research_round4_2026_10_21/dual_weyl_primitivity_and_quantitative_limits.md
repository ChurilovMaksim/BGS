> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/dual_weyl_primitivity_and_quantitative_limits.md`. Embedded SHA256: `90cb06de5c56441dfdb17f6fa32a35484b00c7919bbddd899fb8954f950043c1`.
> [Thematic guide](../../topics/dephasing.md).

# Exact Weyl adjoint dynamics: primitivity, an explicit mixing bound, and its limit

Research continuation, 21 October 2026.

Base checkpoint: `Spectral_research_2026-10-21.md`, SHA-256
`388b7c16c198a67d8a7f06358f1c1b8b0ae6e44724e91d91ef679848909bc394`.

## 1. Status and exact result

The original all-odd-dimensional spectral-statistics problem is not solved here.
This note proves a structural and quantitative theorem for the **exact**
adjoint matrix of the prescribed family, without changing its kick or averaging
over a parameter. Its stochastic matrix is an auxiliary observable of that
matrix; no replacement of coherent evolution by stochastic evolution is made.

Let
$$
U_N(z)=e^{izNA_N}M_N,\qquad
W_N(k,l)=T_N(l,k),\qquad
\mathcal C_N(z)X=U_N(z)XU_N(z)^{-1}.
$$
Write its matrix in the Weyl basis, orthonormal for
$\langle X,Y\rangle=N^{-1}\operatorname{Tr}(X^*Y)$, as
$$
C_N(z)_{u,v}=\frac1N\operatorname{Tr}
 \bigl(W_N(u)^*U_N(z)W_N(v)U_N(z)^{-1}\bigr).
$$
For real $z$, this matrix is unitary. The zero label is a separate one-dimensional
identity block. Put $\Lambda_N=(\mathbb Z/N\mathbb Z)^2\setminus\{0\}$ and
$$
P_N(z)_{u,v}=|C_N(z)_{u,v}|^2,
\qquad u,v\in\Lambda_N.
\tag{1.1}
$$

**Theorem A.** For every odd $N\ge3$, $N\ne7$, and every nonzero real
algebraic $z$, $P_N(z)$ is a primitive doubly stochastic matrix. In fact,
$$
P_N(z)^{6N^2}>0\quad\hbox{entrywise}.
\tag{1.2}
$$
Consequently the only coordinate subspaces in the Weyl basis invariant under
$\mathcal C_N(z)$ are $0$, the scalar line, the traceless space, and the
whole matrix space. A diagonal matrix in this Weyl coordinate system commuting
with $C_N(z)$ is constant on all nonzero labels.

At $N=7$, $A_7=9I/10$, so the adjoint is the unperturbed label permutation;
the exception is real.

**Theorem B.** For the exact $\tau=10^{-80}$, the self-loop at the fixed
integer label $v_*=(1,-2)$ satisfies, for all odd $N\ge3$, $N\ne7$,
$$
|C_N(\tau)_{v_*,v_*}|\ge\tau/50,
\qquad P_N(\tau)_{v_*,v_*}\ge\tau^2/2500.
\tag{1.3}
$$
This bound is uniform in $N$, and its proof does not require $\tau N$ to
be small.

**Theorem C.** A completely explicit positive bound for the spectral gap in
modulus of $P_N(\tau)$ is given in Section 7. It deteriorates much faster
than any inverse power of $N$; in particular, it does not imply mixing on
times of order $N$. The theorem separates genuine effective positivity
from an unproved useful rate.

## 2. Exact adjoint generator, with modular-half signs

For integer frequency labels define
$$
\omega(\kappa,v)=\kappa_l v_k-\kappa_k v_l.
$$
Direct substitution into the Weyl definition gives
$$
W_N(\kappa)W_N(v)
=e_N(\overline2\,\omega(\kappa,v))W_N(\kappa+v),
\tag{2.1}
$$
where $\overline2$ denotes the inverse of $2$ modulo $N$.
Let $F$ be the 32 original nonzero Fourier indices of $f-1/10$, before
aliasing, and write its coefficients as $c_\kappa$. Then
$$
A_N=\sum_{\kappa\in F}c_\kappa W_N(\kappa),\qquad
G_N=iN\operatorname{ad}_{A_N}.
$$
In the Weyl basis,
$$
G_N e_v=
iN\sum_{\kappa\in F}c_\kappa
\left[e_N(\overline2\omega(\kappa,v))-
e_N(-\overline2\omega(\kappa,v))\right]e_{v+\kappa}.
\tag{2.2}
$$
Terms with the same residue are summed. For integer lifts this coefficient is
$$
-2N c_\kappa(-1)^{\omega(\kappa,v)}
\sin\frac{\pi\omega(\kappa,v)}N.
\tag{2.3}
$$
The factor $(-1)^\omega$ cannot be dropped: it is exactly the modular-half
convention. Formula (2.3) is invariant under changing a label lift by a multiple
of $N$, since both its sign and sine then change by the same sign.

The exact quadratic-kernel covariance is
$$
M_NW_N(v)M_N^{-1}=W_N(Sv),\qquad
S=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
\tag{2.4}
$$
It follows that
$$
\boxed{C_N(z)=e^{zG_N}\mathsf P_S,}
\tag{2.5}
$$
where $\mathsf P_Se_v=e_{Sv}$.
The generator $G_N$ is skew Hermitian. Its zero row and column vanish,
so both factors preserve the scalar line and its orthogonal complement.

## 3. Algebraic evaluation and the exact nonzero transition graph

We use the Lindemann--Weierstrass theorem in its distinct-exponent form:
exponentials of distinct algebraic numbers are linearly independent over
the algebraic numbers. A published source covering this precise statement
is Cheng-Chao Huang, *Explicit Bounds for Linear Forms in the Exponentials
of Algebraic Numbers*, ISSAC 2022, Theorem 1.1,
DOI [10.1145/3476446.3536170](https://doi.org/10.1145/3476446.3536170),
[author's version](https://arxiv.org/pdf/2112.05004), page 1.

It follows that, for a finite exponential polynomial
$F(z)=\sum_j b_je^{\lambda_jz}$ with algebraic coefficients and slopes,
$$
F(z_0)=0\quad\Longleftrightarrow\quad F\equiv0
\tag{3.1}
$$
at every nonzero algebraic $z_0$, after equal slopes have been combined.

Every entry in (2.5) is of this form. Indeed all entries of $A_N$ are
algebraic, its distinct eigenvalues $\lambda$ are real algebraic, and
$$
\Pi_\lambda=
\prod_{\mu\ne\lambda}\frac{A_N-\mu I}{\lambda-\mu}
$$
are algebraic spectral projectors, whether or not the spectrum is simple.
Thus
$$
C_N(z)_{u,v}=
\sum_{\lambda,\mu}
\beta^{u,v}_{\lambda,\mu}e^{iNz(\lambda-\mu)},
\qquad
\beta^{u,v}_{\lambda,\mu}
=\frac1N\operatorname{Tr}
 \bigl(W_N(u)^*\Pi_\lambda W_N(Sv)\Pi_\mu\bigr).
\tag{3.2}
$$
This verifies all hypotheses of (3.1). No claim of a quantitative lower bound
is inferred from (3.1) alone.

### 3.1 Required Fourier coefficients, including every small alias

The pure-q coefficients at positive frequencies are
$$
\begin{array}{c|rrrrrrr}
k&1&2&5&6&7&8&9\\\hline
c_{(k,0)}&1/20-i/200&-i/400&-i/800&-1/40-i/400&9/20&-1/40+i/400&i/800.
\end{array}
\tag{3.3}
$$
The negative ones are their complex conjugates. The mixed coefficients are
$$
c_{(k,1)}=\gamma r_k,\quad
c_{(k,-1)}=\bar\gamma r_k,\quad
\gamma=(-3-4i)/1000,
$$
$$
r_0=1,\quad r_{\pm1}=1/2,\quad r_{\pm7}=-1/2,
\quad r_{\pm6}=r_{\pm8}=-1/4.
\tag{3.4}
$$
These follow by multiplying the finite polynomials in the question; for
example the pure-q sine coefficient is
$-i(r_{k-1}-r_{k+1})/200$.

Let $c_N(v)=\sum_{\kappa\equiv v\bmod N}c_\kappa$, and put
$u_N=c_N(1,0)$, $\gamma_N=c_N(0,1)$, $b_N=c_N(2,0)$.
The full exceptional alias table is

| N | u_N | gamma_N | b_N |
|---|---|---|---|
| 3 | $19/40-3i/800$ | $\gamma/2$ | $19/40+3i/800$ |
| 5 | $1/40-7i/800$ | $\gamma$ | $17/40-i/200$ |
| 7 | $0$ | $0$ | $0$ |
| 9 | $1/40-3i/400$ | $\gamma$ | $9/20-i/400$ |
| 11 | $1/20-i/200$ | $\gamma$ | $-3i/800$ |
| odd N at least 13 | $1/20-i/200$ | $\gamma$ | $-i/400$ |

For instance, only the frequency $-9$ aliases into $2$ when $N=11$.
For $N\ge13$, no original pure-q frequency other than $2$ can alias
there; the largest original absolute frequency is $9$. The two other
marked coefficients are already unaliased for $N\ge11$.
At $N=7$, summing the entire table, not only the three marked coefficients,
leaves exactly $A_7=9I/10$.

### 3.2 Edges that must survive at the frozen algebraic kick

Use the directed convention v to u when $C_N(z)_{u,v}\ne0$.
For every v the permutation edge
$$
v\longrightarrow Sv
\tag{3.5}
$$
survives, since the corresponding analytic entry equals one at zero.
For each generator edge $w\longrightarrow w+\kappa$ for which
$c_N(\kappa)\ne0$ and $\omega(\kappa,w)\not\equiv0\pmod N$,
the first derivative of
$C_N(z)_{w+\kappa,S^{-1}w}$ is nonzero. It therefore survives at
every nonzero algebraic z by (3.1).

The alias table proves that the support contains the edges needed to simulate
$$
(k,l)\longrightarrow(k\pm1,l)\quad(l\ne0),
\qquad
(k,l)\longrightarrow(k,l\pm1)\quad(k\ne0).
\tag{3.6}
$$
The sine in (2.2) vanishes exactly when $\omega=0\pmod N$.
This is a nonzero-residue condition, not a unit-residue condition; it is valid
unchanged for composite N.

## 4. Connectedness, aperiodicity, and a quadratic primitivity exponent

Let $h_N$ be the order of S modulo N. Each step in (3.6) is implemented
in the support of C by $h_N-1$ forward permutation steps, followed by
one surviving adjusted edge. Thus it uses exactly $h_N$ steps.

The elementary graph (3.6) is connected on all nonzero residues. Here is an
explicit construction avoiding zero and valid over composite rings.
Use the anchor $v_*=(1,-2)$. If $l\ne0$, first change k to 1 by at most
$N-1$ positive horizontal steps, then change l to -2 by at most $N-1$
positive vertical steps. If $l=0$, then k is nonzero: first change l to -2
vertically, then change k to 1 horizontally. Every step meets its nonvanishing
condition, and the entire path has at most $2N-2$ steps. Reversing the
construction gives an equally short path from the anchor to any target.

There is also a self-loop at the anchor. Indeed,
$$
Sv_*=(-1,-2),\qquad (I-S)v_*=(2,0),\qquad
\omega((2,0),Sv_*)=4.
$$
For odd $N\ge3$, $N\ne7$, the alias table gives $b_N\ne0$, and
$N\nmid4$. Thus $C_N(z)_{v_*,v_*}$ has nonzero first derivative and
is nonzero at every specified algebraic kick.

The elementary number-theoretic bound
$$
\boxed{h_N\le4N/3}
\tag{4.1}
$$
has a uniform composite-modulus proof. At an odd prime p the discriminant
of S is 32, so S has distinct eigenvalues $3\pm2\sqrt2$ in
$\mathbb F_{p^2}$. Their product is one. Frobenius either fixes both or
exchanges them, giving
$S^{p-(2/p)}=I\pmod p$. The binomial expansion of $(I+p^aB)^p$
then yields
$$
\operatorname{ord}_{p^a}S\mid p^{a-1}(p-(2/p)).
$$
If the distinct prime divisors of N are $p_1,\ldots,p_r$, all these upper
multiples are even. Their least common multiple is at most their product
divided by $2^{r-1}$. Consequently
$$
h_N\le2N\prod_{p\mid N}\frac{p-(2/p)}{2p}
\le2N\prod_{p\mid N}\frac{p+1}{2p}\le4N/3.
$$
No p=2 case is needed.

The path from any v to the anchor and from the anchor to any u therefore
uses at most $(4N-4)h_N<6N^2$ edges in the support of C. Insert as many
one-step anchor loops as needed to obtain exactly $6N^2$ edges. All their
squared moduli are positive. This proves (1.2), and hence Theorem A.

For the coordinate-subspace assertion, an invariant coordinate subset cannot
have a surviving edge leading to its complement. Strong connectedness rules
this out on $\Lambda_N$. For a diagonal commuting matrix with entries d_v,
commutation requires $(d_u-d_v)C_{u,v}=0$; connectedness forces constant d_v
on $\Lambda_N$. This argument makes no algebraicity assumption on d_v.

## 5. Uniform quantitative self-loop from a local exact series

The original finite Fourier sum has
$\sum_{\kappa\in F}|c_\kappa|<2$ and
$\max_{\kappa\in F}|\kappa|_1\le9$.
For any integer lift w, (2.3) gives
$$
\sum_{\kappa\in F}|G_{w+\kappa,w}^{(\kappa)}|
\le 2\pi\sum_\kappa |c_\kappa||\kappa|_1|w|_1
\le36\pi |w|_1.
$$
Expanding powers by their original, unaliased increments is legitimate even
when endpoints alias; taking the sum of their absolute values only increases
the bound. Thus
$$
\|G_N^je_w\|_1
\le(36\pi)^j\prod_{q=0}^{j-1}(|w|_1+9q).
\tag{5.1}
$$
For $w=Sv_*=(-1,-2)$, this is at most $1200^j j!$. Therefore
$$
\left|C_N(\tau)_{v_*,v_*}
-\tau(G_N)_{v_*,Sv_*}\right|
\le\frac{(1200\tau)^2}{1-1200\tau}.
\tag{5.2}
$$
The constant term is zero because $v_*\ne Sv_*\pmod N$.

For $N\ge11$, the alias table gives $|b_N|\ge1/400$, and
$0<4\pi/N<\pi/2$. By $\sin x\ge2x/\pi$,
$$
|(G_N)_{v_*,Sv_*}|
=2N|b_N|\sin(4\pi/N)\ge1/25.
\tag{5.3}
$$
The same lower bound follows for N=3,5,9 from the displayed alias table:
use respectively $|\sin(4\pi/3)|\ge1/2$,
$\sin(4\pi/5)=\sin(\pi/5)\ge2/5$, and
$9\sin(4\pi/9)\ge8$.
At $\tau=10^{-80}$, the right side of (5.2) is smaller than $\tau/50$.
Equations (5.2)--(5.3) prove (1.3).

The exact scope of this local estimate matters. For a general lift w,
the majorant of the complete column series is
$$
\sum_{j\ge0}\frac{|z|^j}{j!}\|G_N^je_w\|_1
\le (1-324\pi|z|)^{-|w|_1/9},
\qquad 324\pi|z|<1.
\tag{5.4}
$$
At labels of size comparable to N this grows exponentially in $|z|N$.
Consequently first-derivative positivity does not yield a uniform lower bound
for the high-frequency transitions from this series. No assumption
$\tau N\ll1$ is inserted to bridge that failure.

## 6. Explicit degree and height bounds for every nonzero transition

This section uses absolute logarithmic heights. For a matrix B over a number
field, let h_mat(B) denote the projective height of the vector consisting of 1
and all its entries. Directly from the placewise triangle inequality and
ultrametric inequality,
$$
\begin{split}
h_{\rm mat}(BC)&\le h_{\rm mat}(B)+h_{\rm mat}(C)+\log N,\\
h_{\rm mat}(B+C)&\le h_{\rm mat}(B)+h_{\rm mat}(C)+\log2,\\
h_{\rm mat}(aB)&\le h(a)+h_{\rm mat}(B),\\
h(\operatorname{Tr}B)&\le h_{\rm mat}(B)+\log N.
\end{split}
\tag{6.1}
$$
The factors N or 2 occur only at archimedean places, whose normalized weights
sum to one. Each individual entry height is bounded by h_mat.

All entries of A belong to $K_0=\mathbb Q(i,\zeta_N)$, whose degree is at
most $2N$. The matrix $4000A$ has algebraic-integer entries. Under every
embedding of $K_0$, every Weyl summand remains unitary and the coefficients
have their original absolute values, so the image matrix has norm less than 2.
It follows that
$$
h_{\rm mat}(A)\le\log8000<9.
\tag{6.2}
$$
To verify this height bound directly, at finite places the denominator 4000
contributes at most $\log4000$ in total; at archimedean places the maximum
entry contributes at most $\log2$.

Every $4000\lambda$, for an eigenvalue $\lambda$ of A, is integral over
the ring of algebraic integers, hence is an algebraic integer. Every conjugate
of $\lambda$ is an eigenvalue of an embedded matrix A and has modulus at
most 2. The same denominator and archimedean estimates yield
$$
h(\lambda)\le\log8000<9.
\tag{6.3}
$$

Take the splitting field K of the characteristic polynomial over $K_0$.
Its extension degree is at most N!, since its Galois group embeds in the
permutation group on its distinct roots. Thus
$$
[K:\mathbb Q]\le D_N:=2N\,N!.
\tag{6.4}
$$
Every exponent and coefficient in (3.2), including any grouping of equal
exponents, lies in this same field.

For each factor in a spectral projector, (6.1)--(6.3) give
$$
h_{\rm mat}\!\left(\frac{A-\nu I}{\lambda-\nu}\right)<38.
$$
There are at most N-1 factors. Therefore
$$
h_{\rm mat}(\Pi_\lambda)
\le(N-1)(38+\log N).
\tag{6.5}
$$
Weyl matrices have matrix height zero. Applied to (3.2), this gives
$$
h(\beta^{u,v}_{\lambda,\mu})
\le2(N-1)(38+\log N)+5\log N.
\tag{6.6}
$$
Equal-exponent grouping sums at most N^2 terms. Repeated scalar addition
adds at most their total heights plus $(N^2-1)\log2$.
For the frozen kick, the exponent
$\alpha=iN\tau(\lambda-\mu)$ has height at most
$$
80\log10+\log N+18+\log2.
$$
Consequently a uniform safe bound for the heights of all exponents and all
grouped coefficients, for every odd N at least 3, is
$$
\boxed{H_N=100N^3(1+\log N)+80\log10.}
\tag{6.7}
$$
There are at most N^2 grouped nonzero terms. None of these bounds assumes
that A or U has a simple spectrum.

## 7. An effective spectral-gap bound, and why it is too weak

We now apply the published Theorem 1.2 of Huang, cited in Section 3, to the
distinct grouped exponents in (3.2) evaluated at the exact kick. The original
theorem is stated for arbitrary distinct algebraic exponents and nonzero
algebraic coefficients, with bounds on their degrees and absolute logarithmic
heights. Sections 3 and 6 check precisely those hypotheses.

For specificity, define the positive expression $\mathfrak L(m,d,h)$ from
that theorem as follows:
$$
\delta=d^{2m},\qquad \mu=md^{6m}(2h/d+3),
$$
$$
r=82(9/2)^\delta\delta^{3\delta+2},\qquad
r''=16(1+6\delta^2)(9/2)^\delta\delta^{3\delta},
$$
$$
\begin{split}
r'={}&12(9/2)^\delta\delta^{3\delta+2}
+16(1+6\delta^2)(9/2)^\delta\delta^{3\delta}\log(9\delta^3)\\
&+80(9/2)^\delta\delta^{3\delta+4}(1+6\delta)\mu,
\end{split}
$$
$$
R=r'm^\delta e^{6\delta^2\mu}
+r''m^\delta e^{6\delta^2\mu}(\log m+6\delta\mu)
+72e^{2\delta\mu},
$$
$$
\mathfrak L(m,d,h)
=e^{8\delta\mu}
+rm^\delta e^{6\delta^2\mu}
\left(mh+\frac{39}{164}\mu+e^R\right).
\tag{7.1}
$$
The conclusion is $\log|\sum\beta_j e^{\alpha_j}|\ge-\mathfrak L(m,d,h)$.
The formula was checked in the typeset primary PDF, page 2, including the
powers $m^\delta$. All its terms are nondecreasing for integers
$m,d\ge1$, $h\ge0$; in particular
$\mu=2mh d^{6m-1}+3md^{6m}$ is increasing in d.

Set
$$
F_N=\mathfrak L(N^2,D_N,H_N),\qquad
\varepsilon_N=e^{-2F_N},\qquad L_N=6N^2,
$$
$$
a_N=(N^2-1)e^{-2L_NF_N}.
\tag{7.2}
$$
Every nonzero transition entry C has modulus at least $e^{-F_N}$, hence
every selected stochastic edge has probability at least $\varepsilon_N$.
The exact-length paths constructed in Section 4 yield
$$
(P_N(\tau)^{L_N})_{u,v}\ge\varepsilon_N^{L_N}.
\tag{7.3}
$$
Let $\Pi$ be the $(N^2-1)$-dimensional matrix all of whose entries equal
$1/(N^2-1)$. It follows that
$$
P_N(\tau)^{L_N}=a_N\Pi+(1-a_N)Q_N,
\tag{7.4}
$$
for a doubly stochastic matrix Q_N. Here $0<a_N<1$; this is also immediate
from the displayed enormous positive expression F_N.

On zero-sum column vectors, (7.4) contracts the $\ell^1$ norm by at most
$1-a_N$. It follows without any diagonalizability assumption that the
uniform stationary law is unique and
$$
\|P_N(\tau)^t-\Pi\|_{1\to1}
\le2(1-a_N)^{\lfloor t/L_N\rfloor},
\tag{7.5}
$$
$$
\boxed{
1-\max_{\lambda\ne1}|\lambda(P_N(\tau))|
\ge\frac{a_N}{L_N}
=\frac{N^2-1}{6N^2}e^{-12N^2F_N}.
}
\tag{7.6}
$$
For the eigenvalue inequality use
$|\lambda|^{L_N}\le1-a_N$ and
$(1-a_N)^{1/L_N}\le1-a_N/L_N$.

This is an actual explicit function of N for the original frozen family,
not an unspecified minimum over matrix entries. However, substituting
$t\asymp N$ into (7.5) gives no decay at all; even its block length is
quadratic, and a_N is extraordinarily small. The effective theorem therefore
resolves computability of a gap, not the spectral-statistics bottleneck.

## 8. The coherent obstruction is still present

The stochastic matrix (1.1) squares amplitudes **before** summing paths.
The original target instead depends on
$$
\operatorname{Tr}\mathcal C_N(\tau)^n
=|\operatorname{Tr}U_N^n|^2.
$$
Powers of (1.1) are not entrywise squares of powers of C. If
$Z_n=|C^n|^{\circ2}$ denotes entrywise squared modulus, then exactly
$$
Z_{n+1}=PZ_n+\mathcal E_n,
$$
$$
\mathcal E_n(u,v)=
\sum_{w\ne w'}C_{u,w}\overline{C_{u,w'}}
(C^n)_{w,v}\overline{(C^n)_{w',v}}.
\tag{8.1}
$$
Both row and column sums of $\mathcal E_n$ are zero, by unitarity.
This does not make its norm small. The exact recurrence retains a new
coherence term at every step; the stochastic bound above supplies no estimate
for those terms on the required time scale.

In particular, the following first fixed-test estimate remains unproved:
$$
\frac1{N^2}\sum_{1\le n<2N}|\widehat b_*(n/N)|^2
\bigl(|\operatorname{Tr}U_N^n|^2-\min(n,N)\bigr)=o(1),
$$
where b_* is the explicit nonnegative band-limited Schwartz test in the base
checkpoint. No fixed-test infinite countersequence has been obtained either.

Theorem A rules out every exact decomposition into nonzero Weyl coordinate
sectors, Theorem B supplies a uniform genuine transition probability, and
Theorem C supplies an effective global rate with its actual size exposed.
None of these statements is promoted to independence of phases or to
$H_{\rm diag}$.

## 9. Provenance and continuation condition

The new generator, alias table, support graph, composite order bound, local
series, and algebraic height bounds were derived directly here. The only
external theorem is Lindemann--Weierstrass and its explicit quantitative
version, in the published Huang source identified above. A finite exact
coefficient script accompanies this note; it checks the alias arithmetic and
the small combinatorial instances, not the infinite-dimensional assertion.

The next substantial continuation would require either a useful quantitative
global transition estimate beyond Section 5, or an estimate of the full
coherent contributions in (8.1) with an error that remains small through
times of order N. The present proof has not supplied either estimate.
