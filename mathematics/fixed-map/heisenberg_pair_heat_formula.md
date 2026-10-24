# Exact heat compensation of a Heisenberg pair test

**Claim ID: BGS-FLOW-021. Status: project proof with independent internal review of the new implications.**
5 October 2026. The operator, unfolding and full deterministic BGS target
are unchanged. This note resolves the stable pair vector into explicit
heat modes and expresses its pointwise evolution through determinant
ratios. It does not estimate that vector at the actual frozen operator.
Hook symmetric functions and unitary cut-and-join are classical; priority
is not claimed. The new derivation below needs no unverified character
formula. Its analytic inputs are FLOW-020 G6 and G15, ultimately the
checked stable Haar moments and the normalized generator D5. The sole
stable case below $N=3$, namely $N=2,m=1$, follows directly from
$G_N(|p_1|^2-1)=-(|p_1|^2-1)$ and the stable second/fourth moments;
it does not require G15 outside its recorded dimension range.

## 1. Exact conventions and statement

Let $A$ be any unitary $N\times N$ matrix. Write $p_j=\operatorname{Tr}A^j$ and let $P_t$ be
normalized unitary Brownian heat, with $\mathbb E B_t=e^{-t/2}I$. For an integer
$m\ge1$ suppose $2m\le N$. Put $Q_m=|p_m|^2-m$. On the formal trace variables
define the finite Wick operation

$$
\mathfrak W F=\exp\left[-\sum_{j\ge1}j\partial_{p_j}
 \partial_{p_{-j}}\right]F.                                      \tag{H1}
$$

Every application below is to a polynomial, so the exponential terminates.
The variables with negative indices are conjugates only on evaluation;
they are independent in this formal operation. Define

$$
R_A(x,y)=\frac{\det(I-yxA)}{\det(I-xA)}
=\exp\left[\sum_{j\ge1}\frac{1-y^j}{j}p_jx^j\right],\qquad
H_m(A;y)=\frac{[x^m]R_A(x,y)}{1-y}.                              \tag{H2}
$$

Coefficient extraction is at $x=0$. $H_m$ is a polynomial in $y$ of degree
at most $m-1$: the numerator coefficient vanishes at $y=1$ and has degree
at most $m$. Its value at $y=1$ is the removable limit $H_m(A;1)=p_m$.
No choice of determinant logarithm on the unit circle is involved.
Set $H_0=0$; $R_A$ has constant coefficient $1$, rather than $(1-y)H_0$.

For real $y$ put

$$
K_m(A;y)=|H_m(A;y)|^2-my^{m-1}
 -(1-y)^2\sum_{k=1}^{m-1}(m-k)y^{m-k-1}|H_k(A;y)|^2.             \tag{H3}
$$

**Theorem.** For every such $A,m,N$ and all $t\ge0$, with $y=e^{mt/N}$,

$$
P_tQ_m(A)=e^{-t[m+m(m-1)/N]}K_m(A;y).                           \tag{H4}
$$

This is an identity of smooth class functions, including repeated
eigenvalues and $t=0$. In particular H4 is valid with $A$ equal to the
unchanged $U_N$ whenever $m\le N/2$. It is not a substitution of a randomized
initial matrix for $U_N$.

## 2. Elementary construction of the hook modes

Write $H_m(y)=\sum_{r=0}^{m-1}y^r f_{m,r}$. These coefficients are the
usual signed hook Schur functions, but their two required properties
will be proved directly. Use independent complex Gaussian variables
$Z_j$ with variance $j$, which represent exactly the stable Haar Gram
products. For independent formal x,u,y,v, Gaussian pairing gives

$$
\mathbb E R_Z(x,y)\overline{R_Z(u,v)}
=\frac{(1-yxu)(1-vxu)}{(1-xu)(1-yvxu)}
=1+\frac{(1-y)(1-v)xu}{(1-xu)(1-yvxu)}.                        \tag{H5}
$$

Here the bar means conjugation of the coefficients $Z$, not the formal
parameters. Extract $x^mu^n$. All nonconstant terms depend only on $xu$,
so for $m,n\ge1$

$$
\langle H_m(y),H_n(v)\rangle
=\mathbf1_{m=n}\sum_{r=0}^{m-1}(yv)^r.                         \tag{H6}
$$

Thus the $f_{m,r}$ have unit norm and are mutually orthogonal at fixed $m$.
For holomorphic polynomials their Gaussian inner product is the
diagonal power-sum inner product with norm
$z_\lambda=\prod_j j^{a_j}a_j!$, for multiplicities $a_j$.

Let the positive cut-and-join operator be

$$
\mathcal C=\frac12\sum_{a,b\ge1}\left[
 (a+b)p_ap_b\partial_{p_{a+b}}
 +ab p_{a+b}\partial_{p_a}\partial_{p_b}\right].                \tag{H7}
$$

This is the actual permutation operator of FLOW-020 G15, including
the ordered-split and repeated-factor multiplicities. Put $D=x\partial_x$
and $S=(R-1)/(1-y)=\sum_{m\ge1}x^mH_m(y)$. Direct differentiation gives

$$
\mathcal C S=\left[\frac12(D^2-D)-D y\partial_y\right]S.        \tag{H8}
$$

For completeness, the bilinear term after dividing $\mathcal C R$ by $R$ is
$\tfrac12\sum_{a,b}p_ap_b(1-y^{a+b})x^{a+b}$. Its linear coefficient
at $p_nx^n$ is $\tfrac12\sum_{a=1}^{n-1}(1-y^a)(1-y^{n-a})$.
Differentiating the right side of H8 gives the same bilinear term;
its linear coefficient is

$$
\frac{(n-1)(1-y^n)}2+ny^n-\frac{y(1-y^n)}{1-y}
=\frac12\sum_{a=1}^{n-1}(1-y^a)(1-y^{n-a}).                   \tag{H9}
$$

This identity is polynomial after removing the displayed denominator.
The derivative of $1/(1-y)$ is retained in H9. Consequently

$$
\mathcal C f_{m,r}=\frac{m(m-1-2r)}2f_{m,r}.                   \tag{H10}
$$

At $y=1$, H2 says $p_m=\sum_r f_{m,r}$. No representation-theoretic
eigenvalue theorem has been imported in H5--H10.

## 3. Full signed point formula, including contractions

By FLOW-020's stable Wick isometry the functions
$E_{m,r,s}=\mathfrak W(f_{m,r}\overline{f_{m,s}})$, $0\le r,s<m$, are orthonormal
in $\mathcal V_{m,N}$. The reducing-space formula G15 and H10 give their exact
heat rates

$$
\lambda_{m,r,s}=m+\frac{m(m-1-r-s)}N.                         \tag{H11}
$$

Their sum is $Q_m$. Thus for all $t\ge0$

$$
P_tQ_m=e^{-t[m+m(m-1)/N]}
 \mathfrak W\left(H_m(e^{mt/N})\overline{H_m(e^{mt/N})}\right).
                                                                    \tag{H12}
$$

The Wick product in H12 must not be replaced by the raw squared
modulus. To evaluate it exactly, use H1 on two formal exponentials:

$$
\begin{split}
\mathfrak W\bigl(R_A(x,y)R_{A^{-1}}(u,y)\bigr)
&=\frac{(1-xu)(1-y^2xu)}{(1-yxu)^2}
 R_A(x,y)R_{A^{-1}}(u,y),\\
\frac{(1-xu)(1-y^2xu)}{(1-yxu)^2}
&=1-\frac{(1-y)^2xu}{(1-yxu)^2}.                              \tag{H13}
\end{split}
$$

These are formal coefficient identities: at each coefficient only
finitely many trace derivatives contribute. Extract x^m u^m and
divide by (1-y)^2. The constant coefficient of each $R$ contributes
$-my^{m-1}$; the other contractions contribute the sum in H3.
The identity extends to $y=1$ by polynomial continuity. This proves
$\mathfrak W(|H_m(y)|^2)=K_m(y)$, hence H4. The full stable signed hierarchy has
collapsed for this observable to $m$ determinant coefficients and
their explicit compensating weights, not to its first heat jet.

## 4. Exact spectral measure and microscopic time

Orthonormality and H11 give, for every $t\ge0$,

$$
\|P_tQ_m\|_2^2
=e^{-2mt}\left[\frac{\sinh(m^2t/N)}{\sinh(mt/N)}\right]^2,
\qquad
\langle Q_m,P_tQ_m\rangle
=e^{-mt}\left[\frac{\sinh(m^2t/(2N))}{\sinh(mt/(2N))}\right]^2.
                                                                    \tag{H14}
$$

At $t=0$ the ratios mean $m$, so both values are $m^2$. These are
Haar-$L^2$ and Haar autocorrelation identities, not pointwise bounds.

Let $0<a<b<1/2$, let $w$ be a real smooth compactly supported function
in $(a,b)$, and put $J_{N,w}=N^{-2}\sum_mw(m/N)Q_m$. Distinct $m$ give
orthogonal reducing spaces. If $L_N=-G_N/N$, the spectral measure
of $\sqrt N J_{N,w}$ for $L_N$ is exactly

$$
\nu_N=N^{-3}\sum_m w(m/N)^2\sum_{r,s=0}^{m-1}
\delta_{\lambda_{m,r,s}/N}.                                   \tag{H15}
$$

It converges weakly to the finite positive measure

$$
\nu_w(d\ell)=\left[\int_a^b w(\xi)^2
 \left(1-\frac{|\ell-\xi|}{\xi^2}\right)_+d\xi\right]d\ell.
                                                                    \tag{H16}
$$

To prove this, set $\xi=m/N$, $u=r/m$, $v=s/m$. Then $\lambda/N$ converges
uniformly to $\xi+\xi^2(1-u-v)$. The two uniform coordinates have the
triangular sum density. The $m^2$ modes and the outer $N^{-3}$ give
$\xi^2d\xi$; this cancels the $\xi^{-2}$ in that triangular density.
Ordinary Riemann sums prove H16, including endpoint multiplicities.
All measures have uniformly bounded mass and compact support.

For each fixed $s\ge0$, H14 or H16 yields

$$
\lim_{N\to\infty}N\|P_{s/N}J_{N,w}\|_2^2
=\int_a^b w(\xi)^2 e^{-2s\xi}
 \left[\frac{\sinh(s\xi^2)}{s\xi}\right]^2d\xi.                \tag{H17}
$$

The bracket at $s=0$ means $\xi$. This supplies the entire particular-test
Haar-$L^2$ profile at microscopic noise time. It refines G16's interval
bound but supplies no actual-map expectation. Any linear operator whose
domain contains $P_tJ_{N,w}$ and whose image of that vector is $J_{N,w}$,
provided $J_{N,w}\ne0$,
has Haar-$L^2$ operator norm at least
$\|J_{N,w}\|_2/\|P_tJ_{N,w}\|_2$, with the denominator given exactly
by the weighted sum of H14. This refines the coarse G16 lower bound.

## 5. Clock calibration and a pointwise determinant discriminator

For the $N$-clock $C_N$, $R_{C_N}(x,y)=(1-(yx)^N)/(1-x^N)$. Every
$H_k(C_N;y)=0$ at $1\le k<N$. H4 gives the exact stable-band identity

$$
P_tQ_m(C_N)=-me^{-mt},\qquad
\mathbb E|p_m(B_tC_N)|^2=m(1-e^{-mt}).                         \tag{H18}
$$

This agrees with the prior clock relaxation mechanism; it is not a
formula for $U_N$. The negative clock mean and the small Haar-$L^2$ norm
of the local band concern different evaluations. In fact, for each
$m\ge2$ and $t>0$, H14's $L^2$ norm decays more slowly than $m e^{-mt}$.
Point evaluation is not Haar-$L^2$ contraction.

When $A$ has simple eigenvalues $z_i$, partial fractions give for $m\ge1$

$$
H_m(A;y)=\sum_{i=1}^N z_i^m
 \prod_{j\ne i}\frac{1-yz_j/z_i}{1-z_j/z_i}.                  \tag{H19}
$$

The constant polynomial quotient of $R$ has no positive coefficients;
the residue of its pole at $1/z_i$ includes the factor $1-y$, which
cancels H2's denominator. At $y=1$ all weights are one. Formula H19
is only used on the simple-spectrum locus; H2--H4 are the definitions
and hold at confluence. For $y>0$,

$$
\left|\prod_{j\ne i}\frac{1-yz_j/z_i}{1-z_j/z_i}\right|
=y^{(N-1)/2}\prod_{j\ne i}
 \left[1+\frac{(y-1)^2}{4y\sin^2((\theta_j-\theta_i)/2)}\right]^{1/2}.
                                                                    \tag{H20}
$$

Thus estimating individual residues introduces microscopic gaps.
Keeping the determinant coefficient and signed contraction formula
can avoid that particular division, but it still needs quantitative
information about the actual coefficients through m of order N.

## 6. Actual target and the first still missing estimate

For the unchanged $U_N=e^{i10^{-80}NA_N}M_N$ the complete pair defect
in this stable band is now explicitly

$$
P_tJ_{N,w}(U_N)-J_{N,w}(U_N)
=N^{-2}\sum_m w(m/N)
 \left[e^{-t[m+m(m-1)/N]}K_m(U_N;e^{mt/N})-Q_m(U_N)\right].    \tag{H21}
$$

No absolute values may be inserted term by term when asserting the
desired signed cancellation. The determinant representation is an
exact alternative to the integrated cubic hierarchy, with all
contractions retained. Neither H14--H17 nor the noisy limiting law
estimates H21 at $U_N$. The logarithmic trace estimate of FLOW-020
controls only a vanishing fraction of the coefficients needed in H2.
The remaining task is a model-specific signed estimate for H21 (or
directly $J_{N,w}(U_N)$); other Fourier bands and all higher factorial
orders remain separate required obligations. **TRACE-005 and the full
deterministic BGS objective remain OPEN.**

## 7. Exact short-trace matching does not control the determinant band

The next attempted input-only estimate is false even for simple spectra.
This uses the familiar clustered-clock mechanism, rather than a chaotic
counterexample or a new spectral distribution. The statement is stronger
than orthogonality to a linear projection: arbitrary functions of the
listed trace data cannot distinguish the two configurations.

**Proposition.** For any integer sequence $Q_N=o(N)$ and any $\alpha>0$,
there is an odd-dimensional subsequence $N=rL$ with $r,L\to\infty$
and two simple unitary spectra $A_N,D_N$ such that

$$
\begin{gathered}
p_j(A_N)=p_j(D_N)=e^{ij/N^4}-1\ne0
 \quad(1\le j\le Q_N),\\
|p_j(A_N)|+|p_j(D_N)|\le4e^{\alpha j}\quad(j\ge1),
                                                                    \tag{H22}
\end{gathered}
$$

$$
J_{N,w}(A_N)\longrightarrow-\int_a^b\xi w(\xi)d\xi,
\qquad
\frac{J_{N,w}(D_N)}L\longrightarrow\int_a^b w(\xi)d\xi>0.       \tag{H23}
$$

Here $w$ is fixed, smooth, compactly supported in $(a,b)$ and nonzero
nonnegative. Both normalized empirical spectral measures tend to
uniform measure. The displayed exponential bounds hold after discarding
finitely many members of the subsequence. The unchanged $U_N$ is
neither constructed nor refuted by this proposition.

**Construction.** Take any odd $L\to\infty$. For each $L$, choose an odd
$r$ sufficiently large that $Q_{rL}<r$, $r\ge\log(rL)/\alpha$ and
$r\to\infty$. This is possible: at fixed $L$, $Q_N/N\to0$ along
$N=rL$, and $r/\log(rL)\to\infty$. Set $N=rL$ and
$\varepsilon=N^{-4}$. Let $A_N$ be the $N$-clock with its eigenvalue
$1$ replaced by $e^{i\varepsilon}$. Before the same replacement, let
$D_N$ have eigenvalues

$$
e^{2\pi i h/r+i c/N^{10}},\qquad
0\le h<r,\quad0\le c<L.                                      \tag{H24}
$$

The offsets are distinct and much smaller than $2\pi/r$.
The replacement offset $\varepsilon$ is larger than the whole small
offset interval and smaller than $2\pi/r$. Both spectra are simple.
For $r\nmid j$, complete $r$-clock sums vanish before replacement,
so $p_j(D_N)=e^{ij\varepsilon}-1$. The same is true for $A_N$ when
$N\nmid j$, hence for every $1\le j<r$. These small positive phases
are less than $1$, establishing the nonzero assertion in H22.
For $j<r$ each trace has modulus at most $2$; for $j\ge r$ unitarity
and $N\le e^{\alpha r}$ give the displayed sum bound. The uniform
macroscopic limit follows from the $r$-clock Riemann sum and the
vanishing offsets and one-point replacement.

For $j\le bN$ the original repeated clock trace is
$N\mathbf1_{r\mid j}$. The offsets and replacement change it by at
most $NjL/N^{10}+j/N^4=O_b(N^{-3})$. They therefore change
$J_{N,w}$ by $O_w(N^{-3})$, using $|p_j|\le N$, $O(N)$ terms and
the factor $N^{-2}$. Writing $D_N^{(0)}$ for the unperturbed repeated clock, its value is exactly

$$
J_{N,w}(D_N^{(0)})=\sum_{k\ge1}w(k/L)
 -N^{-2}\sum_{j\ge1}j w(j/N).                                 \tag{H25}
$$

The first term divided by $L$ tends to $\int w$ and the second tends
to $\int\xi w$. For the perturbed $N$-clock only the second remains,
up to the same negligible error. This proves H23.

Consequently no estimate using only the first $Q_N=o(N)$ traces and
these global exponential bounds can approximate $J_{N,w}$ with error
$o(1)$ uniformly on both families. H22 supplies identical data for
every nonlinear function of those traces, whereas H23 separates their
answers. Estimating H21 for the actual map requires an additional
model-specific input. This does not prohibit using its full matrix,
fixed quantization, signed orbit correlations or determinant structure.

## 8. A uniform stable-band heat estimate from the actual short traces

The determinant formula also permits a new quantitative point estimate
after heat smoothing. This supplies an actual-start consequence, with an
explicit error shape, rather than only another inverse-norm obstruction.
The auxiliary Brownian time below does not change the frozen quantum
coupling or imply removal of that Brownian smoothing.

Fix $0<a<b<1/2$, integers $1\le J<N$, and $d\ge0$, and suppose
$|p_j(A)|\le Nd$ for $1\le j\le J$. For $0<t\le1$ define

$$
\Delta_{J,d,a}(t)=d(1+\log J)
 +\frac{8e^{-aJt/4}}{aJt},\qquad \vartheta=a(1-b).             \tag{H26}
$$

**Uniform point estimate.** If $\Delta_{J,d,a}(t)\le\vartheta t/16$,
then for every integer $aN\le m\le bN$,

$$
|P_tQ_m(A)|\le\left[e^b(at)^{-2}+N^2/2+N\right]
 e^{-\vartheta Nt/4}.                                         \tag{H27}
$$

There is no minimum-gap assumption. All inequalities are for actual
unitary matrices, and H4 already incorporates every Wick contraction.

**Proof.** Write $D_A(z)=\det(I-zA)$. For $0<\rho<1$, the convergent
logarithm series and unitarity give, uniformly in the angle,

$$
\left|\log|D_A(\rho e^{i\phi})|\right|
\le N\left[d(1+\log J)
 +\frac{\rho^{J+1}}{(J+1)(1-\rho)}\right].                    \tag{H28}
$$

The first $J$ terms use the stated trace bound; the remaining ones use
$|p_j|\le N$ and $1/j\le1/(J+1)$. This also gives a strictly positive
lower bound for the modulus of the denominator on each interior circle.
Unitarity gives the exact reflection identity
$|D_A(z)|=|z|^N|D_A(1/\overline z)|$ for $|z|>1$.

Put $\xi=m/N$, $y=e^{\xi t}$ and choose the coefficient circle
$\rho=e^{-3\xi t/4}$. Then $y\rho=e^{\xi t/4}>1$, whose reflected
radius is $\rho'=e^{-\xi t/4}$. Both interior radii have exponents
at least $at/4$. Since $0<t\le1$ and $a<1/2$,
$1-e^{-at/4}\ge at/8$. Consequently each bracket in H28 is at
most $\Delta_{J,d,a}(t)$. Reflection and Cauchy's coefficient bound
now give for $1\le k\le m$

$$
|H_k(A;y)|\le\frac1{y-1}
 \exp\left[\frac{Nt\xi}{4}+\frac{3kt\xi}{4}
                 +2N\Delta_{J,d,a}(t)\right].                \tag{H29}
$$

For the first squared modulus in H3, combine H29 with H4.
Its full exponent, excluding the $4N\Delta$ error, is exactly
$-Nt\xi(1-\xi)/2+t\xi$.
For a contracted term with $\eta=k/N$, multiplication by
$y^{m-k-1}$ cancels that correction and gives exactly
$-Nt\xi(1-\eta)/2$, again excluding $4N\Delta$.
These are at most $-\vartheta Nt/2$ except for the first term's
$t\xi$ correction. The latter is bounded by $1/2$.
The factor $e^b$ in H27 retains that finite-dimension correction.
The contraction factors $(1-y)^2$ cancel H29's denominator;
$\sum_{k=1}^{m-1}(m-k)\le N^2/2$. The scalar term is exactly
$me^{-mt}\le Ne^{-aNt}$. Finally $4N\Delta\le\vartheta Nt/4$.
This proves H27 with its displayed prefactor.

**Actual-start corollary.** FLOW-020 G8 supplies fixed $C_0,\alpha>0$
with $|p_j(U_N)|\le C_0e^{\alpha j}$ at every positive index and all
odd $N\ge3$. Choose

$$
J_N=\left\lfloor\frac{\log N}{2(\alpha+1)}\right\rfloor,
d_N=C_0N^{-1/2},\qquad
t_N=C_a\frac{\log J_N}{J_N},\quad C_a=\max\{32,8/a\}.        \tag{H30}
$$

All formulas below are for sufficiently large odd $N$, so $J_N>1$
and $0<t_N\le1$. The short-trace hypothesis follows since
$\alpha/[2(\alpha+1)]<1/2$. Furthermore
$d_N(1+\log J_N)/t_N\to0$; the other summand of H26 divided by
$t_N$ is $O_a(J_N^{-1}/(\log J_N)^2)$ because $aC_a/4\ge2$.
The hypothesis of H27 therefore holds eventually and uniformly for
$t_N\le t\le1$, as $\Delta(t)/t$ decreases. In particular

$$
\sup_{aN\le m\le bN}
\left|\mathbb E|p_m(B_{t_N}U_N)|^2-m\right|
\le\left[e^b(at_N)^{-2}+N^2/2+N\right]
 e^{-\vartheta Nt_N/4}=o(N^{-H})\quad\text{for every fixed }H>0.
                                                                    \tag{H31}
$$

The supremum is over integers in the band. Summing H31 also proves
$P_{t_N}J_{N,w}(U_N)=o(N^{-H})$ for every fixed $H>0$. No growing
Fourier bandwidth, effective startup dimension or unperturbed value
$J_{N,w}(U_N)$ follows. The time constant depends on the fixed lower
band endpoint $a$; it is not silently identified with FLOW-014's
particular time constant $32$.

The same argument applies to the two spectra in H22: eventually
$J_N<r$, so $d_N=2/N$ suffices on their common short-trace window.
At the same time schedule H30 both smoothed values vanish, whereas
H23 gives different unperturbed values. Their signed defects $P_tJ-J$
therefore have a positive clock limit and a negative limit after
division by $L$, respectively. Even this stronger pointwise heat
control does not remove noise using the short-trace data alone.
**The actual signed defect H21 and full deterministic BGS remain OPEN.**
