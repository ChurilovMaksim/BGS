> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_continuation_2026_10_20/quantitative_transcendence_limits.md`. Embedded SHA256: `35a8399e59a1ff390031cab2be39c654d08acf095326dcbc160dadca23f9eae4`.
> [Thematic guide](../../topics/algebra.md).

# Quantitative limits of the transcendence argument at the fixed parameter

Date: 20 October 2026.

## 1. Result and scope

This note supplies an unconditional, explicit lower bound for the distance between two **distinct** eigenvalues of the original matrix
$$
 U_N=e^{i\tau N A_N}M_N,\qquad \tau=10^{-80},
$$
for every odd $N\ge3$. Repeated eigenvalues are allowed. The argument does not assume simple spectrum or the nonvanishing of the ordinary discriminant.

The bound follows from the published explicit Lindemann–Weierstrass estimate of Cheng-Chao Huang, together with degree and height estimates proved here for this exact family. Its numerical scale is extremely small. In particular, the resulting lower bound is smaller than $N^{-K}$ for every fixed $K$, once $N$ is sufficiently large. Applying either the direct gap-product estimate or the elementary packing estimate gives no improvement on the trivial $O(N^2)$ bound for pairs at distance $a/N$.

This is a limitation of the specific effective estimate and its application worked out below. It is not a theorem excluding every quantitative transcendence method, and it is not evidence that the actual eigenvalue gaps are that small. There is no averaging over $\tau$.

The new device is to use a moment Gram determinant of size equal to the number of distinct eigenvalues. It stays positive even when the full characteristic discriminant vanishes.

## 2. Exact family and the algebraic field

Use the original plus-shift finite Weyl convention
$$
 (T_N(a,b)u)(x)=e_N[b(x+\overline2a)]u(x+a),\qquad
 e_N(s)=e^{2\pi i s/N},
$$
and
$$
 (M_N)_{xy}=N^{-1/2}e_N[-\overline8(3x^2-2xy+3y^2)].
$$
All modular fractions refer to inverses modulo odd $N$.

The Hamiltonian is the original Fourier quantization
$$
 A_N=\sum_{k,l}c_{kl}T_N(l,k),
$$
where
$$
 \sum_{k,l}c_{kl}e^{2\pi i(kq+lp)}
 =\cos14\pi q+\frac{r(q)}{10}
 +\frac{r(q)\sin2\pi q}{100}
 +\frac{r(q)\cos(2\pi p-\alpha_0)}{100}-\frac1{10},
$$
$$
 r(q)=(1-\cos14\pi q)(1+\cos2\pi q),\qquad
 e^{i\alpha_0}=(-3+4i)/5.
$$
Every $4000c_{kl}$ is a Gaussian integer. The original Fourier coefficient mass satisfies
$$
 \sum_{k,l}|c_{kl}|
 \le 1+\frac3{10}+\frac4{100}+\frac4{100}
 =\frac{69}{50}=:\Lambda.
 \tag{2.1}
$$
Indeed, the cosine of frequency seven has mass $1$; the mass of $r/10-1/10$ is $3/10$; and the last two terms have mass at most $4/100$ each.

Put
$$
 K_0=\mathbb Q(e^{2\pi i/N},i,\sqrt N).
$$
Then
$$
 [K_0:\mathbb Q]\le4\varphi(N)\le4N.
$$
Let $\rho_1,\ldots,\rho_s$, $s\le N$, be the distinct eigenvalues of $A_N$, and let
$$
 K=K_0(\rho_1,\ldots,\rho_s).
$$
This is contained in the splitting field over $K_0$ of the degree-$N$ characteristic polynomial. Its Galois group permutes at most $N$ distinct roots, so
$$
 [K:\mathbb Q]\le4\varphi(N)N!\le d_N,\qquad
 d_N:=4N N!.
 \tag{2.2}
$$
Repeated roots do not invalidate this splitting-field bound.

All spectral projectors of $A_N$, all entries of $M_N^{\pm1}$, and every coefficient and exponent used below belong to $K$. The rational parameter $\tau$ does not enlarge the field.

These are proved upper bounds, not claims that the actual field always has degree $d_N$.

## 3. Heights of eigenvalues and projectors

### 3.1. Height conventions and elementary inequalities

For a scalar, matrix, or finite tuple $X$ of elements of $K$, write
$$
 h(X)=\frac1{[K:\mathbb Q]}
       \sum_v n_v\log\max(1,\max_{x\in X}|x|_v).
 \tag{3.1}
$$
This is the absolute logarithmic height of the tuple, with $1$ included. For a matrix the tuple consists of its entries. It is unchanged upon enlarging $K$.

The product formula and the local triangle inequalities give
$$
 h(XY)\le h(X)+h(Y)+\log N
 \tag{3.2}
$$
for two $N$-by-$N$ matrices, and
$$
 h(X-aI)\le h(X)+h(a)+\log2.
 \tag{3.3}
$$
For scalars,
$$
 h(ab)\le h(a)+h(b),\quad
 h(a-b)\le h(a)+h(b)+\log2,\quad
 h(a^{-1})=h(a)\quad(a\ne0).
 \tag{3.4}
$$
For concatenated tuples, the height of the concatenation is at most the sum of their heights. These statements follow place by place: at a nonarchimedean place no factor $N$ or $2$ is needed, and at an archimedean place the ordinary triangle inequality supplies it.

### 3.2. The constant eigenvalue-height bound

Every entry of $4000A_N$ is an algebraic integer. Hence each $4000\rho_j$ is an algebraic integer.

For any embedding of $K_0$ into $\mathbb C$, every Weyl matrix appearing in the Fourier sum is still unitary: roots of unity are sent to roots of unity, and the shift is unchanged. Gaussian rational Fourier coefficients are either unchanged or conjugated. Thus (2.1) gives
$$
 \|\sigma(A_N)\|\le\Lambda
 \tag{3.5}
$$
for every embedding $\sigma$. Every conjugate of every $\rho_j$ is a root of one of these conjugate characteristic polynomials, so it has absolute value at most $\Lambda$.

The common denominator $4000$ controls all finite places, and (3.5) controls all infinite places. Consequently, with
$$
 h_0:=\log(4000\Lambda)=\log5520,
$$
one has the simultaneous bounds
$$
 h(A_N)\le h_0,\qquad
 h(\rho_1,\ldots,\rho_s)\le h_0.
 \tag{3.6}
$$
The second bound is for the entire eigenvalue tuple, not the sum of $s$ separate scalar bounds. This distinction saves a factor $N$ in the exponent-height calculation.

Also,
$$
 h(M_N)=h(M_N^{-1})=\frac12\log N.
 \tag{3.7}
$$
All entries in either matrix are a root of unity times $N^{-1/2}$; their local absolute values agree.

### 3.3. Projectors and the coefficient family

Since $A_N$ is Hermitian, its distinct-eigenvalue projectors are
$$
 P_j=\prod_{k\ne j}\frac{A_N-\rho_k I}{\rho_j-\rho_k}.
 \tag{3.8}
$$
This formula remains valid when some eigenspaces have dimension greater than one. If $s=1$, the empty product is $I$.

Applying (3.2)–(3.4) to the numerator and denominator gives
$$
 h(P_j)
 \le 2(s-1)(2h_0+\log2)+(s-2)_+\log N
 \le P_N,
$$
where
$$
 P_N:=N(4h_0+2\log2+\log N).
 \tag{3.9}
$$
There is no unproved lower bound on an eigenvalue difference hidden here. The identity $h(x^{-1})=h(x)$ controls the inverse differences in height; a small value at one embedding is accounted for at the other places.

Set
$$
 B_j=P_jM_N,\qquad C_j=M_N^{-1}P_j.
$$
Then
$$
 h(B_j),h(C_j)\le P_N+\frac32\log N.
$$
For the tuple of **all** entries of **all** $B_j,C_j$, a convenient bound is
$$
 h((B_j,C_j)_{j\le s})\le B_N,\qquad
 B_N:=2N\left(P_N+\frac32\log N\right).
 \tag{3.10}
$$
Thus $P_N=O(N\log N)$ and $B_N=O(N^2\log N)$, with the displayed constants fully specified.

## 4. A positive exponential polynomial without a simplicity hypothesis

Write
$$
 U(z)=e^{izNA_N}M_N.
$$
For every integer $k$, define the entire function
$$
 p_k(z)=\operatorname{Tr}U(z)^k,\qquad p_0(z)=N.
$$
Negative powers are entire because
$$
 U(z)^{-1}=M_N^{-1}e^{-izNA_N}.
$$

Introduce formal Laurent variables $X_1,\ldots,X_s$:
$$
 \mathcal U(X)=\sum_j B_jX_j,\qquad
 \mathcal V(X)=\sum_j C_jX_j^{-1}.
$$
The projector identities $P_jP_k=\delta_{jk}P_j$ and $\sum_jP_j=I$ imply
$$
 \mathcal U(X)\mathcal V(X)=\mathcal V(X)\mathcal U(X)=I.
$$
Specialization $X_j=e^{izN\rho_j}$ therefore represents both positive and negative powers of $U(z)$.

Let $q$ be the number of distinct eigenvalues of the fixed unitary matrix $U(\tau)$, and write these values as
$$
 \lambda_1,\ldots,\lambda_q,\qquad
 m_1,\ldots,m_q\ge1,\qquad\sum_a m_a=N.
$$
Define
$$
 G_q(z)=[p_{j-k}(z)]_{0\le j,k<q},\qquad
 D_q(z)=\det G_q(z).
 \tag{4.1}
$$
At real $z=\tau$, the matrix is a moment Gram matrix:
$$
 G_q(\tau)=V\,\operatorname{diag}(m_1,\ldots,m_q)\,V^*,
 \qquad V_{ja}=\lambda_a^j.
$$
The Vandermonde matrix $V$ is square and invertible. Hence
$$
 D_q(\tau)
 =\left(\prod_a m_a\right)
   \prod_{a<b}|\lambda_a-\lambda_b|^2
 >0.
 \tag{4.2}
$$

Equation (4.2) proves exactly the nonvanishing needed for the effective theorem, irrespective of repeated eigenvalues. It is not an assumption about the ordinary characteristic discriminant. The unknown integer $q$ is harmless because every following estimate is uniform for $1\le q\le N$.

An additional qualitative consequence is that the number of distinct eigenvalues at every nonzero real algebraic parameter equals the maximum attained by the family over real parameters. To see this, choose the largest attained Gram rank. Its corresponding determinant is a nonzero algebraic exponential polynomial, so qualitative Lindemann–Weierstrass makes it nonzero at every such algebraic parameter. This does not determine whether that maximum is $N$.

## 5. Explicit degree, term-count, and height bounds for the Gram determinant

Set
$$
 L_N:=N(N-1),\qquad t_N:=(2L_N+1)^N.
 \tag{5.1}
$$

### 5.1. Exponent support

A term in the determinant expansion of $D_q$ is a product
$$
 \prod_{j=0}^{q-1}p_{j-\sigma(j)}.
$$
Its total Laurent degree in the sense of the $\ell^1$-norm of exponent vectors is at most
$$
 \sum_{j=0}^{q-1}|j-\sigma(j)|
 \le q(q-1)\le L_N.
 \tag{5.2}
$$
Therefore $D_q(\tau)$ can be written, after combining equal exponents and deleting zero coefficients, as
$$
 D_q(\tau)=\sum_{\nu=1}^{t}\beta_\nu e^{\alpha_\nu},
 \quad
 \alpha_\nu=i\tau N\sum_{j=1}^{s}n_{\nu j}\rho_j,
 \quad
 \sum_j|n_{\nu j}|\le L_N.
 \tag{5.3}
$$
The exponents in this final expression are distinct and the coefficients are nonzero. Since each integer coordinate lies in $[-L_N,L_N]$,
$$
 1\le t\le (2L_N+1)^s\le t_N.
 \tag{5.4}
$$
All $\alpha_\nu,\beta_\nu$ lie in $K$, so their individual degrees are at most $d_N$.

### 5.2. Exponent heights

At a finite place an integer linear combination of the $\rho_j$ has absolute value at most their maximum local absolute value. At an infinite place the additional factor is at most $L_N$. Using the simultaneous tuple bound in (3.6),
$$
 h\left(\sum_j n_{\nu j}\rho_j\right)
 \le h_0+\log L_N.
$$
Because $h(\tau)=80\log10$, a valid bound is
$$
 h(\alpha_\nu)\le
 A_N^{\rm ht}:=h_0+\log(NL_N)+80\log10.
 \tag{5.5}
$$
Here $A_N^{\rm ht}$ is a scalar height bound, not the Hamiltonian matrix.

The tiny real value of $\tau$ does not produce a small logarithmic height: its exact denominator contributes $80\log10$.

### 5.3. Coefficient heights, including all rearrangements

For each place $v$, put
$$
 b_v=\max\bigl(1,\max_{j,x,y}|(B_j)_{xy}|_v,
                    \max_{j,x,y}|(C_j)_{xy}|_v\bigr).
$$
The global average of $\log b_v$ is at most $B_N$.

At an infinite place, use the sum of absolute values of all coefficients of a Laurent polynomial. The Laurent polynomial representing $p_k$ has coefficient mass at most
$$
 N^{2|k|+1}b_v^{|k|}.
 \tag{5.6}
$$
For $k\ne0$, one expands at most $s^{|k|}$ choices of projectors and at most $N^{|k|}$ matrix-index cycles. The extra factor $N$ makes (5.6) valid also for $p_0=N$.

At a finite place, use the maximum absolute value of the Laurent coefficients, the nonarchimedean Gauss norm. Its bound is simply $b_v^{|k|}$; integer multiplicities and signs have absolute value at most one.

Multiplication of Laurent polynomials is submultiplicative for these norms. Expanding the $q$-by-$q$ determinant, and using (5.2), gives an infinite-place coefficient-mass bound
$$
 q!\,N^{2L_N+q}b_v^{L_N}
 \le N!\,N^{2L_N+N}b_v^{L_N},
$$
and a finite-place Gauss-norm bound $b_v^{L_N}$.

Combining monomials whose exponential frequencies agree cannot increase the infinite-place coefficient mass or the finite-place maximum norm. Thus no missing factor for frequency collisions or coefficient rearrangement remains. The height of the entire resulting coefficient tuple obeys
$$
 h(\beta_1,\ldots,\beta_t)\le
 C_N^{\rm ht}:=
 L_NB_N+\log(N!)+(2L_N+N)\log N.
 \tag{5.7}
$$

Use the single convenient parameter
$$
 h_N:=1+A_N^{\rm ht}+C_N^{\rm ht}.
 \tag{5.8}
$$
It bounds every exponent and coefficient height and satisfies $h_N=O(N^4\log N)$.

## 6. The verified published estimate

The source is Cheng-Chao Huang, *Explicit Bounds for Linear Forms in the Exponentials of Algebraic Numbers*, ISSAC 2022, pp. 371–379, DOI
https://doi.org/10.1145/3476446.3536170 .
The checked author version is arXiv:2112.05004v2, 16 May 2022:
https://arxiv.org/pdf/2112.05004v2 .
The exact result is Theorem 1.2 on PDF page 2. The HTML rendering was checked against that PDF page.

For distinct algebraic exponents, nonzero algebraic coefficients, at most $t$ terms, and degree and absolute logarithmic height bounded by $d,h$, that theorem gives
$$
 \log\left|\sum_\nu\beta_\nu e^{\alpha_\nu}\right|
 \ge-\Phi(t,d,h).
 \tag{6.1}
$$
Here the following notation spells out the published expression:
$$
 \delta=d^{2t},\qquad \mu=td^{6t}(2h/d+3),
$$
$$
 r=82(9/2)^\delta\delta^{3\delta+2},
 \qquad r''=16(1+6\delta^2)(9/2)^\delta\delta^{3\delta},
$$
$$
 r'=12(9/2)^\delta\delta^{3\delta+2}
    +16(1+6\delta^2)(9/2)^\delta\delta^{3\delta}
      \log(9\delta^3)
    +80(9/2)^\delta\delta^{3\delta+4}(1+6\delta)\mu,
$$
$$
 R=r't^\delta e^{6\delta^2\mu}
   +r''t^\delta e^{6\delta^2\mu}(\log t+6\delta\mu)
   +72e^{2\delta\mu},
$$
$$
 \Phi(t,d,h)=e^{8\delta\mu}
       +rt^\delta e^{6\delta^2\mu}
        \left(th+\frac{39}{164}\mu+e^R\right).
 \tag{6.2}
$$
All quantities are nondecreasing when $t,d,h$ increase, already for $t\ge1,d\ge1,h\ge0$. This includes the edge cases of actual degree one or actual height below one. For the only slightly non-obvious factor, write
$$
 td^{6t}(2h/d+3)=t(2h\,d^{6t-1}+3d^{6t}).
$$
Thus substituting the upper bounds from Section 5 is legitimate even if the actual number of surviving terms or their degrees is smaller.

The theorem concerns general complex algebraic exponents and coefficients; it does not require rational linear independence of the exponents, only that equal exponents have been combined. Its height is logarithmic, as in (3.1). This is the precise source-to-project translation.

The source proof derives its estimate from Sert's effective theorem. The present note uses Huang's explicit theorem directly. It does not claim that its specialization is the strongest estimate obtainable by a different choice of a rational basis or by another effective-transcendence argument.

## 7. An unconditional explicit gap bound

Apply (6.1) to the positive determinant (4.2), using (5.4), (2.2), and (5.8):
$$
 D_q(\tau)\ge \exp[-F_N],\qquad
 F_N:=\Phi(t_N,d_N,h_N).
 \tag{7.1}
$$

If $q\ge2$, let
$$
 g_N:=\min_{a\ne b}|\lambda_a-\lambda_b|.
$$
In (4.2), every other chordal gap is at most $2$, while
$\prod_a m_a\le N^N$. Therefore
$$
 D_q(\tau)\le
 N^N\,g_N^2\,2^{N(N-1)-2}.
$$
Consequently every pair of distinct eigenvalues obeys
$$
 \boxed{\quad
 |\lambda_a-\lambda_b|\ge\varepsilon_N
 :=2^{1-N(N-1)/2}N^{-N/2}\exp[-F_N/2]
 \quad(a\ne b).\quad}
 \tag{7.2}
$$
If $q=1$, the assertion about pairs of distinct eigenvalues is vacuous. No simplicity claim is used in either case. In the present family the earlier no-scalar theorem supplies $q\ge2$ outside $N=7$, and the bare $N=7$ cat is also nonscalar.

The circular angular distance in radians is at least its chordal distance, so (7.2) is also a lower bound for the angular gap. If phases are normalized modulo $1$, divide the bound by $2\pi$.

This is an explicit finite-$N$ statement at the original exact rational $\tau$, including dimensions divisible by seven.

## 8. Why this particular bound cannot control pairs at scale $1/N$

The input parameters have the explicit growth
$$
 \log d_N=\Theta(N\log N),\qquad
 \log t_N=2N\log N+O(N),\qquad
 h_N=2N^4\log N+O(N^4).
 \tag{8.1}
$$
These describe the bounds actually substituted, not lower bounds on the true algebraic complexity.

There is no need to estimate every nested exponential in (6.2) to see the scale. Its first summand already gives
$$
 F_N\ge e^{8\delta\mu}
     \ge \exp\!\left(24t_Nd_N^{8t_N}\right).
 \tag{8.2}
$$
Therefore the **guarantee produced by this calculation** satisfies
$$
 \varepsilon_N
 \le \exp\!\left[-\frac12
        \exp\!\left(24t_Nd_N^{8t_N}\right)\right].
 \tag{8.3}
$$
The prefactor in (7.2) is at most one for $N\ge3$. Equation (8.3) makes $\varepsilon_N=o(N^{-K})$ for every fixed positive $K$.

This direction of comparison is essential: it says that the lower bound we can certify is very small. It does not say that $g_N$, the actual gap, is small.

One can first use the determinant lower bound directly, without reducing it to a minimum-gap bound. In the favorable case $q=N$, let $R_a$ count unordered pairs at angular distance at most $a/N$. Each such chordal gap is at most $a/N$; every other chordal gap is at most $2$. Hence
$$
 D_N(\tau)\le(a/N)^{2R_a}
                 2^{N(N-1)-2R_a},
$$
and (7.1) gives, when $2N>a$,
$$
 R_a\le
 \frac{F_N+N(N-1)\log2}{2\log(2N/a)}.
 \tag{8.4}
$$
Because $F_N$ is far larger than $N^2\log N$, this estimate exceeds the trivial $N(N-1)/2$. Thus even retaining the full gap product does not yield the desired pair bound from this numerical estimate.

Even if all $N$ eigenvalues were simple, writing $\phi_j$ for their phases in radians, an angular separation guarantee $\varepsilon_N$ would yield only the elementary packing bound
$$
 \#\{(j,k):j\ne k,\ d_{\mathbb S^1}(\phi_j,\phi_k)\le a/N\}
 \le
 \min\left(N(N-1),\
          2N\left(1+\frac{a}{N\varepsilon_N}\right)\right).
 \tag{8.5}
$$
For the explicit $\varepsilon_N$, the second expression exceeds the trivial bound for all sufficiently large $N$. Unknown multiplicities make separation of distinct values still less informative for a count with multiplicities.

The logical insufficiency of these numerical constraints can be demonstrated directly. For fixed $a>0$, and all sufficiently large $N$, place $N$ distinct phases at
$$
 \phi_j=\frac{ja}{2N^2},\qquad0\le j<N.
$$
Their minimum chordal gap is at least $a/(4N^2)$, which is larger than $\varepsilon_N$. Their total angular span is less than $a/N$. Their ordinary Gram determinant obeys
$$
 D_N\ge\left(\frac{a}{4N^2}\right)^{N(N-1)}
       =\exp[-O_a(N^2\log N)]\ge e^{-F_N}.
$$
Thus all $N(N-1)$ ordered distinct pairs are close, while both numerical guarantees (7.1) and (7.2) are respected. This is an example of configurations compatible with the derived bounds; it is not asserted to be the spectrum of the original $U_N$, nor to meet its other dynamical constraints.

The specific published estimate therefore gives a positive uniform-in-parameters finite-dimensional separation, but neither its direct gap-product use nor its minimum-gap packing consequence supplies an $O(N)$ pair-count estimate at the requested microscopic scale.

## 9. An elementary finite-range comparison at the fixed parameter

There is a stronger elementary estimate for power traces in a finite range where the kick remains a small perturbation. For real $\tau$,
$$
 \|U_N-M_N\|
 \le \tau N\|A_N\|\le\Lambda\tau N.
$$
The telescoping identity for powers of two unitaries gives
$$
 |p_m(\tau)-p_m(0)|
 \le N\|U_N^m-M_N^m\|
 \le\Lambda m\tau N^2.
 \tag{9.1}
$$
The exact finite Egorov calculation in the base packet gives
$$
 |p_m(0)|^2=\#\ker(S^m-I)\ge1,
 \qquad S=\begin{pmatrix}3&4\\2&3\end{pmatrix}.
$$
Consequently
$$
 |p_m(\tau)|\ge1-\Lambda m\tau N^2,
$$
and in particular
$$
 |p_m(\tau)|\ge\frac12
 \quad\text{if}\quad
 mN^2\le\frac{1}{2\Lambda\tau}.
 \tag{9.2}
$$
No parameter averaging occurs. For $m$ of order $N$, this controls only $N^3$ below an explicit constant of order $10^{80}$, hence a finite dimension range. It supplies neither an asymptotic gap estimate nor the pair cancellation required for Hdiag. The existence of a large finite range must not be confused with an $N\to\infty$ theorem.

## 10. Source audit, verification, and remaining scope

The exact source/version and theorem were authenticated using the arXiv abstract history, the versioned PDF and its page-2 theorem, the HTML mathematical formulas, and the author's institutional publication record. The publication is ISSAC 2022, DOI 10.1145/3476446.3536170. The precise implication from Huang's theorem to (7.1) is **verified** once the elementary field/height estimates in this note are checked.

Search scope: searches for explicit quantitative Lindemann–Weierstrass, Sert's effective theorem, Huang's title, and later references returned the directly applicable arbitrary-algebraic-linear-form theorem above. This was a bounded applicability check, not an exhaustive proof of optimality among all published bounds. Baker-type logarithm estimates were not substituted for exponential-linear-form estimates.

The proof requires no numerical diagonalization, no unproved simplicity theorem, no lower bound on a projector denominator at the chosen complex embedding, and no average over $\tau$. The number of terms may drop through exact algebraic relations between the $\rho_j$; the norms in Section 5 explicitly accommodate those collisions.

The conclusions proved here are:

* an explicit lower bound for every nonzero spectral gap of the original family at the original parameter;
* explicit degree, coefficient-height, exponent-height, and term-count bounds entering it;
* a rigorous comparison showing that this particular numerical guarantee is far below the $1/N$ scale and that its direct gap-product and packing consequences cannot force $O(N)$ close pairs;
* a separate elementary lower bound on power traces in an explicitly finite perturbative range.

Simple spectrum, microscopic pair counts, and Hdiag remain unresolved by this calculation.

