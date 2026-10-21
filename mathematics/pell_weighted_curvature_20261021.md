# Full weighted gradient, Pell curvature and the forced early inflection

**Claim:** BGS-TRACE-111. **Status:** analytic author proof, reconstructed
and self-reviewed on 21 October 2026. All time sums below include the full
support of the fixed test. This is a theorem at the initial parameter
$t=0$ and on a shrinking interval; it does not evaluate the fixed positive
parameter $\tau=10^{-80}$.

## Fixed test and statements

Use the exact matrices of [TRACE-106](physical_kick_trace_decay.md), with
$U_N(t)=e^{itNA_N}M_N$. Define

$$
\phi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},\quad I=\int\phi,
\quad b_* =\frac{|\mathcal F^{-1}\phi|^2}{2I^2},\quad
w=|\widehat b_*|^2=\frac{(\phi*\phi)^2}{4I^4},
$$
$$
p_m(t)=\operatorname{Tr}U_N(t)^m,\quad
S_N(t)=\frac1{N^2}\sum_{1\le m<2N}w(m/N)|p_m(t)|^2.
                                                               \tag{1}
$$

Let $N=N_r=(\lambda^r-\lambda^{-r})/(4\sqrt2)$ for odd $r\ge3$,
$\lambda=3+2\sqrt2$, and $d=2r=O(\log N)$. Write
$I_w=\int_0^2 w$, $J_2=\int_0^2 x^2w(x)\,dx>0$ and
$c=289J_2/80000$. Then

$$
S_N(0)=\frac Nd I_w+O(1),\quad
|S_N'(0)|=O_L(N^{-L})\ (\text{each fixed }L),\quad
S_N''(0)\le-c\frac{N^5}{d^2}                       \tag{2}
$$

for sufficiently large $N$ on this sequence. Moreover there is
$t_N=O(d^3/N^2)$ with

$$
S_N''(t_N)\ge\frac{c^4}{512 C_3^2 I_w}\frac{N^5}{d^7}>0,
\qquad C_3=32(59/50)^3\|w\|_\infty.               \tag{3}
$$

Thus the full sum changes curvature before any fixed positive parameter
for large Pell dimensions. This does not establish the sign of $S_N'$
throughout that interval or the value of $S_N(\tau)$.

## Full gradient and exact return algebra

For all real $t$, define the Hermitian traceless commuting gradient

$$
G_N(t)=\sum_{m\ge1}m w(m/N)
\operatorname{Im}\bigl(\overline{p_m(t)}U_N(t)^m\bigr),
\quad Q_N(t)=\mathcal E_{U_N(t)}(A_N).
$$

Cyclicity and $p_m'=iNm\operatorname{Tr}(A_NU_N^m)$ give

$$
S_N'=-\frac2N\operatorname{Tr}(A_NG_N)
=-\frac2N\operatorname{Tr}(Q_NG_N),
$$
$$
2\|G_N\|_{\rm HS}^2
=\sum_{m,n\ge1}mnw_mw_n\Re\left(
\overline{p_m}p_n p_{m-n}-\overline{p_m}\,\overline{p_n}p_{m+n}
\right).                                                     \tag{4}
$$

There is no absolute value inside the double sum. On the Pell sequence
$M_N^d$ is scalar. The matrix sequence
$X_m=\operatorname{Im}(\overline{\operatorname{Tr}M_N^m}M_N^m)$
is $d$-periodic, odd and has zero average. Apply Poisson summation to
the smooth odd function $\chi(x)=xw(x)$. The finite Fourier mode
$j$ and Poisson index $\ell$ combine bijectively as $d\ell-j$;
there is no extra multiplicity $d$. Repeated integration by parts gives

$$
\|G_N(0)\|_{\rm op}\le C_{R,\chi}N^3(d/N)^R.        \tag{5}
$$

Exact covariance and Weyl orthogonality yield, for $1\le s<d$,

$$
|\operatorname{Tr}(T(v)M_N^s)|^2
\le\#\ker(S^s-I\bmod N)\le7N.                    \tag{6}
$$

The bound includes composite $N$: the modular kernel injects into the
integral cokernel of $S^s-I$, bounding it by the absolute determinant;
the Pell identities then give the stated bound. Multiples of $d$ in
(1) contribute $(N/d)I_w+o(1)$, and (6) bounds the other terms by
$O(1)$. Equations (4)--(6) prove the first two assertions in (2).

## Hessian without differentiating eigenvalue branches

Diagonalize $A_N$ only within each eigenspace of the fixed matrix $M_N$.
Let $\lambda_a=e^{2\pi i\theta_a}$, $q_a=Q_{aa}$, and

$$
\Gamma_a=\sum_{\lambda_b\ne\lambda_a}|A_{ab}|^2
\frac{\lambda_a+\lambda_b}{\lambda_a-\lambda_b}=i\beta_a,
\qquad |\beta_a|\le\frac d2\|A_N\|^2,
$$
$$
H_N(\theta)=\sum_{m\ge1}m^2w(m/N)\cos(2\pi m\theta).
$$

Differentiate finite matrix powers twice, using
$p_m''(0)=-N^2m\sum_{j=0}^{m-1}\operatorname{Tr}(AM^jAM^{m-j})$.
Summing the resulting finite geometric progression gives exactly

$$
S_N''(0)=-\sum_{a,b}(q_a-q_b)^2H_N(\theta_a-\theta_b)
+2\sum_a\beta_a G_N(0)_{aa}.                     \tag{7}
$$

For different $d$-clock eigenvalues the angular separation is at least
$1/d$. Poisson summation of $x^2w(x)$ bounds their total contribution
by $O_R(N^5(d/N)^R)$. Within a block the cosine equals one. Therefore

$$
S_N''(0)=-2H_N(0)\mathcal V_N+O_R(N^5(d/N)^R),\quad
\mathcal V_N=\sum_j\left[n_j\operatorname{Tr}Q_j^2
-(\operatorname{Tr}Q_j)^2\right].                  \tag{8}
$$

For the concrete Fourier coefficients $\|A_N\|\le L_A=59/50$.
The $(0,7)$ coefficient has modulus $9/20$, while all remaining
coefficients together have norm at most $.28$. Projecting its finite
Weyl orbit gives

$$
\|Q\|_{\rm HS}^2\ge\frac{289N}{10000d},\quad
n_j\ge N/d-\sqrt{7N},\quad
\sum_j(\operatorname{Tr}Q_j)^2\le7L_A^2N.
$$

Consequently $\mathcal V_N\ge289N^2/(40000d^2)$ for sufficiently
large $N$ (the explicit sufficient comparison is $N\ge1350d^2$).
Since $H_N(0)=N^3J_2+o(N^3)$, (8) proves the curvature bound in (2).
All orbit labels, projection norms, composite-modulus estimates and
geometric-sum algebra are worked out in the
[complete gradient/Hessian proof](spectral_research/proofs/research_round14_2026_10_21/signed_sum/r14_full_weighted_gradient_and_hessian_attempt.md),
§§2--7. A separate finite verifier compares the direct matrix Hessian to
(7); it does not prove its asymptotic lower bound.

## Positivity forces an inflection

Finite differentiation and unitarity give $|S_N'''(t)|\le C_3N^7$.
Use the elementary following fact: if $F\ge0$, $F(0)\le M$,
$F''(0)\le-B$, $|F'''|\le C$, and $|F'(0)|$ is sufficiently
small, then at $\delta=B/(2C)$,
$F'(\delta)\le-B^2/(8C)$. Also $F(\delta)\le2M$.
If $H=\max_{[\delta,\delta+32CM/B^2]}F''$, Taylor's integral formula
and positivity give $H\ge B^4/(256C^2M)$.

Take $M=2I_wN/d$, $B=cN^5/d^2$, $C=C_3N^7$.
The small-gradient conditions follow from (5). The resulting point
of positive curvature satisfies (3), with

$$
t_N\le\frac{c}{2C_3N^2d^2}
+\frac{64C_3I_w}{c^2}\frac{d^3}{N^2}.             \tag{9}
$$

## Entire continuation, with the correct inverse powers

For complex $z$ set

$$
\mathcal S_N(z)=N^{-2}\sum_m w(m/N)
\operatorname{Tr}U_N(z)^m\operatorname{Tr}U_N(z)^{-m}.
$$

The second factor is an inverse power, not an adjoint at complex $z$.
Both factors are entire and agree with (1) on the real line. Direct
operator bounds give

$$
|\mathcal S_N(x+iy)|\le2\|w\|_\infty N e^{4L_AN^2|y|}.
$$

If $|(d/N)\mathcal S_N|\le M_0$ on a disk of radius $R_N$, (2)
and Cauchy's inequality force

$$
R_N\le\sqrt{2M_0/c}\frac{\sqrt d}{N^2}.            \tag{10}
$$

Each Taylor series has infinite radius of convergence. Equation (10)
restricts a uniformly bounded analytic family, not that radius.
The [full continuation proof](spectral_research/proofs/research_round14_2026_10_21/obstruction/r14_pell_curvature_inflection_and_analytic_window.md)
also proves a finite exponential-sum closure, fixed-$N$ recurrence and
the consequent failure of monotone decay on the entire positive half-line.
None of those recurrence times is placed before the fixed $\tau$.

The unresolved observable is $S_N(\tau)-N^{-2}\sum_mw(m/N)\min(m,N)$.
Initial curvature, a forced inflection and analyticity do not evaluate it.
