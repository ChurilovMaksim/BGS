# Möbius reduction of repeated Gaussian coboundary steps

**Claim ID: BGS-FLOW-009.** Project proof and author check,
29 September 2026. No independent review, formal certificate or priority
claim. The Möbius geometry of first-harmonic mean-field motion is
established prior work; the local facts needed here are proved below.

**30 September continuation:** [FLOW-010](coboundary_joint_limit.md)
adds a quantitative joint regime at epsilon_N=exp(-N), using stronger
uniform estimates. The iterated statement and proof below retain their
original scope; the extension does not supply deterministic noise removal.

## 1. Exact scope and order of limits

Let $G_n$ be independent normalized GUE matrices and set

$$
U_{n+1}^{\varepsilon}
=\exp\{i\varepsilon(G_n-U_n^{\varepsilon}G_nU_n^{\varepsilon*})\}
 U_n^{\varepsilon}. \tag{1}
$$

No centering term or covariance whitening is inserted in (1).
For odd $N\ge3$ start at the clock
$U_0^{\varepsilon}=C_N=\operatorname{diag}(e^{2\pi ij/N})_{j=0}^{N-1}$.
Let $\Phi_{N,f}$ be the uniform-origin unfolded Laplace functional of
[FLOW-004](quadratic_noise_coupling.md), for $0\le f\in C_c^1(\mathbb R)$.
If $t_N\to0$ and $Nt_N\to\infty$, then

$$
\lim_{N\to\infty,\ N\ \mathrm{odd}}\limsup_{\varepsilon\downarrow0}
\left|\mathbb E\Phi_{N,f}
 (U_{\lfloor2t_N/\varepsilon^4\rfloor}^{\varepsilon})
-\Phi_{\rm Sine}(f)\right|=0. \tag{2}
$$

The inner small-step limit first fixes $N$. No explicit joint rate
$\varepsilon_N$, fixed-step theorem, or universality of the deterministic
initial spectrum is claimed. In particular (2) changes the clock's
local law. It is a theorem about repeated external random perturbations.

The proof has three parts: local Möbius centering, a fixed-$N$ fast/slow
limit of the spectral quotient, and a uniform small-time comparison
of the resulting projected diffusion with Dyson motion.

## 2. Centering and preservation of averaged local laws

For $|w|<1$ define

$$
M_w(U)=(U-wI)(I-\bar wU)^{-1}.
$$

If $|m_2(U)|\le3/4$ and $|m_1(U)|\le1/1024$, there is a unique small
solution $w=w(U)$ of $N^{-1}\operatorname{Tr}M_w(U)=0$, with
$|w|\le8|m_1|$. It depends smoothly on $U$; put $\Pi(U)=M_{w(U)}(U)$.
For the local existence statement, expand

$$
N^{-1}\operatorname{Tr}M_w(U)=m_1-w+\bar w m_2+R(w),
$$
$$
|R(w)|\le\frac{2|w|^2}{1-|w|},\qquad
\operatorname{Lip}_{|w|\le r}R\le\frac{2r(2-r)}{(1-r)^2}. \tag{3}
$$

The map $w\mapsto m_1+\bar w m_2+R(w)$ is a contraction of the disk
$|w|\le8|m_1|\le1/128$ into itself. The derivative bound is strictly
less than one, also giving smooth dependence and local uniqueness.
At $m_1=0$, the center is $w=0$. The map need not preserve the
determinant; the spectral quotient also removes common rotation.

Two centered representatives of the same nearby disk-Möbius orbit
differ only by rotation: decompose their connecting automorphism as
a rotation followed by $M_a$, and apply the same uniqueness at a
centered configuration. Thus, for any rotation-invariant spectral
function $f$ on the centered slice, $\widetilde f=f\circ\Pi$ is locally
Möbius invariant. In particular $D_J\widetilde f=0$ for the faster field
$J$ in [FLOW-008](coboundary_fourth_order_drift.md).

Here is a uniform local-statistics estimate that does not require bounded
occupancy. If an orientation-preserving circle map $\psi$ has a lift with
$\|\psi'-1\|_\infty=\delta\le1/2$, then, for $\operatorname{supp}f\subset[-R,R]$,

$$
|\Phi_{N,f}(\psi(\theta))-\Phi_{N,f}(\theta)|
\le\delta(1+6R^2\|f'\|_\infty). \tag{4}
$$

Change the observation angle from $\alpha$ to $\psi(\beta)$; its density
differs from uniform by at most $\delta$. For each lifted angular difference,
the unfolded displacement changes by at most $\delta|x|$. A term can
contribute only for $|x|\le2R$. Integrating the sum over uniform $\beta$
gives exactly unit intensity, and
$\int_{-2R}^{2R}|x|\,dx=4R^2$. The exponential is 1-Lipschitz on
nonnegative arguments; the Jacobian is at most $3/2$. This proves (4).

The boundary derivative of $M_w$ is
$(1-|w|^2)/|1-\bar wz|^2$, so its derivative error is at most
$2|w|/(1-|w|)$. Consequently

$$
|\Phi_{N,f}(\Pi U)-\Phi_{N,f}(U)|\le C_f|m_1(U)| \tag{5}
$$

on this neighborhood, with $C_f$ independent of $N$. In particular,
bounded $p_1$ makes this centering invisible to averaged local weak laws
as $N\to\infty$. This does not make the stochastic evolution invisible.

## 3. Fixed-dimension spectral quotient limit

Consider the slice $\mathcal M=\{U:\operatorname{Tr}U=0,\ |m_2|<1/2\}$.
Locally it is a smooth real codimension-two manifold: the two trace
gradients are independent when $|m_2|<1$.
For smooth rotation-invariant class functions on it, define

$$
\overline L f(U)=L_X(f\circ\Pi)(U),\qquad U\in\mathcal M. \tag{6}
$$

This is the generator of a smooth projected matrix diffusion on the
slice, stopped before the indicated boundary; its explicit coefficients
are given in Section 4. Its spectral law modulo common rotation is unique.

Fix $N$, start with $m_1=0$, and choose a threshold
$q_0\in(2/5,1/2)$ such that $q_0^2$ is a regular value of $|m_2|^2$
on the slice modulo rotation. Sard's theorem allows such a choice;
an empty level causes no exit. The spectra of $\Pi U_n^{\varepsilon}$,
modulo common rotation and with time step $h=\varepsilon^4/2$, converge
locally up to this exit to the spectral law of (6).

The needed estimates are as follows. Stop also if $|m_1|$ reaches
$a=1/1024$. Before either exit, $|m_2(U_n)|<3/4$: the difference from
the centered second trace is at most $2\|U_n-\Pi U_n\|_{\rm op}$,
and (3) bounds it by less than $1/4$.
For each fixed positive integer $p$, the Gaussian Taylor expansion and
(5) of FLOW-008 give

$$
\mathbb E(|m_1(U_{n+1})|^{2p}\mid U_n)
\le(1-c_p\varepsilon^2)|m_1(U_n)|^{2p}
   +C_{N,p}\varepsilon^{2p+2}. \tag{7}
$$

To verify the remainder structure rather than assume it, write
$\Delta m_1=\varepsilon^2 r(U,G)+O_G(\varepsilon^3)$, with all
$k$th absolute moments bounded by $C_{N,k}\varepsilon^{2k}$.
Its conditional mean is $\varepsilon^2D_Jm_1+O_N(\varepsilon^4)$;
odd terms vanish. The leading derivative of $|m_1|^{2p}$ is at most
$-p\varepsilon^2|m_1|^{2p}/4$. Each remaining polynomial term is
absorbed by half of this negative term plus
$C_{N,p}\varepsilon^{2p+2}$, using Young's inequality with
$|m_1|/\varepsilon$. This proves (7).

Apply (7) to the process killed at the two exits. Since $m_1(U_0)=0$,
its pre-exit $2p$th moment is $O_{N,p}(\varepsilon^{2p})$ uniformly in
the step number. A union bound over $O(T\varepsilon^{-4})$ steps gives
probability $O_{N,T}(\varepsilon^2)$ for an $a$-exit before the $q_0$-exit,
by taking $p=3$. Also
$\mathbb E[|m_1(U_n)|;n<\sigma]=O_N(\varepsilon)$.

For $\widetilde f=f\circ\Pi$, the first expected term
$\varepsilon^2D_J\widetilde f$ vanishes identically. FLOW-008 gives

$$
\mathbb E[\widetilde f(U_{n+1})-\widetilde f(U_n)\mid U_n]
=h\{\overline Lf(\Pi U_n)+O_{N,f}(|m_1(U_n)|)\}
 +O_{N,f}(\varepsilon^6). \tag{8}
$$

At $m_1=0$, both the mean quadratic field and the expected fourth
logarithm vanish; the remaining quadratic variation is precisely
$L_X$. Away from the slice, the coefficient error in (8) follows by
smoothness. Summing its expectation to time $T$ gives $O_{N,T,f}(\varepsilon)$.
Conditional second moments of the increments are $O_{N,f}(h)$, and
Gaussian tails make the maximum jump tend to zero. These estimates
give tightness and the martingale problem (6) for the projected spectral
coordinates. Smooth invariant functions separate unordered spectra
modulo rotation on compact subsets. Uniqueness follows from the smooth
projected matrix SDE: its invariant backward semigroup determines all
invariant martingale-problem expectations, after smooth localization.

At a nonempty regular exit level, the covariance is positive in its
nonconstant normal direction, so the exit functional is almost surely
continuous under this local convergence. Common rotation is the only
irrelevant scalar direction; FLOW-003 is positive on the traceless
Hermitian space. This justifies the regular stopping convention.

This argument concerns spectra, not convergence of the rapidly changing
eigenvectors of (1). The conjugated step $W_\varepsilon U$ has the same
spectral transition kernel as (1) because fresh GUE is conjugation invariant.

## 4. Projected diffusion and dimension-uniform bounds

At $Y\in\mathcal M$ put $q=m_2$, $r=m_3$, $d=1-|q|^2$ and take the
square-root factors $K_a=\mathcal C_Y^{1/2}E_a$ from FLOW-004. Set

$$
f_a=\frac iN\operatorname{Tr}(K_aY),\qquad
w_a=\frac{f_a+q\bar f_a}{d},\qquad
J_a=i(w_aY^*-\bar w_aY),\qquad L_a=K_a+J_a. \tag{9}
$$

This is the derivative of $\Pi$; in particular
$\operatorname{Tr}(L_aY)=0$. In left Hermitian coordinates at the slice,
it is the orthogonal projection onto the kernel of the first-trace
derivative: its correction lies in the span of the two trace gradients
$\operatorname{Re}Y,\operatorname{Im}Y$. Positivity of $\mathcal C_Y$
therefore gives positivity on the traceless tangent subspace. Define

$$
v=\sum_a|w_a|^2,\quad \zeta=\sum_aw_a^2,\quad
T=\sum_a\bar w_aK_a=\frac{i}{Nd}\mathcal C_Y(\bar qY-Y^*),
$$
$$
\kappa=\sum_a\bar w_a\frac{2i}{N}\operatorname{Tr}(K_aY^2),\quad
h_0=\kappa+r\bar\zeta,\quad b=(h_0+q\bar h_0)/d.
$$

The covariance is complex-linearly extended in the formula for $T$.
The projected SDE is

$$
dY=i\sum_aL_aY\,dW_a-\tfrac12\sum_aL_a^2Y\,dt+iA_\Pi Y\,dt,
$$
$$
A_\Pi=ibY^*-i\bar bY+TY+T^*Y^*
             +\tfrac i2\zeta Y^{*2}-\tfrac i2\bar\zeta Y^2. \tag{10}
$$

For verification of this Itô correction, expand
$\Pi(V)=V-wI+\bar wV^2-|w|^2V+\bar w^2V^3+O(|w|^3)$.
At the slice the raw first-trace drift is zero. The constraint
$\operatorname{Tr}\Pi(V)=0$ yields drift equation
$b-q\bar b=\kappa+r\bar\zeta$. Its matrix drift is
$-Y/2-bI+\bar bY^2+2iTY^2-vY+\bar\zeta Y^3$.
Subtracting $-\sum_aL_a^2Y/2$ gives (10). All matrices formed by
applying $\mathcal C_Y$ to powers of $Y$ commute with $Y$.

For $|q|\le1/2$, the following deliberately coarse bounds are uniform:

$$
v\le5/N^2,\quad |\zeta|\le5/N^2,\quad
\|T\|_{\rm op}\le4/N^2,\quad |b|\le26/N^2,
\qquad \|A_\Pi\|_{\rm op}\le80/N^2. \tag{11}
$$

Indeed, with $s=m_4$,
$\sum f_a^2=-(q-\bar qs)/(2N^2)$ and
$\sum|f_a|^2=(1-|q|^2+|r|^2/2)/N^2$.
Substitution into (9) gives $v<5/N^2$.
The explicit covariance gives $\|\mathcal C_Y(Y)\|_{\rm op},
\|\mathcal C_Y(Y^*)\|_{\rm op}\le2/N$.
Cauchy--Schwarz and $\Gamma(m_2,\bar m_2)\le12/N^2$ give
$|\kappa|<8/N^2$, whence (11).

The projected second trace also satisfies

$$
\overline Lp_2=-\tfrac12(1-|q|^2)p_2+e,
\quad |e|\le150/N,\qquad
\overline\Gamma(p_2,\bar p_2)\le64. \tag{12}
$$

To check the first bound, the second-order expansion of $p_2(\Pi V)$ is
$p_2(V)-2wp_1(V)+2\bar wp_3(V)+Nw^2-4|w|^2p_2(V)+3\bar w^2p_4(V)$.
Use (11), $|p_j|\le N$, and the raw bracket bounds $\Gamma(p_j,\bar p_j)\le3j^2$
on its drift. Their sum is less than $150/N$. Its martingale coefficient
is the raw $dp_2$ coefficient plus $2\bar w_ap_3$; hence its bracket is
at most $(\sqrt{12}+2\sqrt5)^2<64$.
Gronwall and the martingale maximal inequality imply, for $t\le1$,

$$
\mathbb E\sup_{s\le t\wedge\sigma}|p_2(Y_s)|^2
\le C(|p_2(Y_0)|^2+t+t^2/N^2). \tag{13}
$$

For a clock start, exit through $|p_2|=Nq_0$, $q_0>2/5$, thus has
probability at most $C(t+t^2/N^2)/N^2$.

## 5. Comparison to Dyson motion

Couple (10) to traceless unitary Brownian motion from the same $Y_0$
using $B_a=E_a/\sqrt N$. Write $R_a=L_a-B_a$.
The cancellation $\sum_a[B_a,R_a]=0$ still holds: it holds for
$K_a-B_a$ by FLOW-004, and $\sum_aw_aB_a$ commutes with $Y$, since
the covariance square root preserves its commuting Hermitian subspace.
Furthermore $\sum J_a^2\le4vI$. FLOW-004 and (11) imply

$$
\left\|\sum_aR_a^2\right\|_{\rm op}
\le4|m_2|^2+44/N^2,\qquad
\operatorname{Tr}\sum_aR_a^2\le4N|m_2|^2+44/N. \tag{14}
$$

For the relative matrix $Z=V^*Y$, stopped at $\sigma$, the Itô drift is
$-V^*(\sum R_a^2)VZ/2+iV^*A_\Pi VZ$.
The Hilbert--Schmidt energy estimate from FLOW-004 now has the additional
term bounded by $160(\mathbb E\|Z-I\|_{\rm HS}^2)^{1/2}/N^{3/2}$.
Use (13)--(14), integrate, and absorb this square-root term to obtain

$$
N\mathbb E\|Y_{t\wedge\sigma}-V_{t\wedge\sigma}\|_{\rm HS}^2
\le Ct(1+|p_2(Y_0)|^2)+Ct^2/N^2,\qquad t\le1. \tag{15}
$$

Thus for the clock start, the averaged Laplace discrepancy is
$O_f(\sqrt t)$, with the exit probability adding $O(t/N^2)$.
The odd-clock Dyson kernel estimate in
[FLOW-007](quadratic_noise_clock_limit.md) gives

$$
\left|\mathbb E\Phi_{N,f}(Y_t)-\Phi_{\rm Sine}(f)\right|
\le C_f[\sqrt t+(Nt)^{-1}+N^{-2}],\quad Nt\ge1,\ t\le1/12, \tag{16}
$$

where any continuation after exit affects the estimate only by its
probability. By Section 3, the pre-exit centered spectra of (1) have
this diffusion limit at fixed $N$. Equation (7) and (5) remove the
centering in the averaged Laplace functional with an $O_{N,f}(\varepsilon)$
error before exit. Regular-exit convergence and (13) bound the discarded
paths by $O(t/N^2)$. Taking the inner limsup in (16), followed by
$N\to\infty$ at the times specified in Section 1, proves (2) for smooth
$f$. Nonnegative smooth approximation extends it to $C_c^1$: unit mean
intensity after origin averaging bounds the Laplace error by
$\|f-g\|_1$, uniformly in every spectrum and $N$.

## 6. What this closes, and what it leaves open

The full covariance alone was insufficient to identify the fourth-order
limit of finite coboundary kicks. The missing faster motion is a
Möbius mean-field motion; its quotient removes that motion, and the
fourth-degree logarithmic mean vanishes on the centered slice. This
gives a precise spectral diffusion mechanism for the uncentered steps.
It is not convergence of their uncentered matrix paths, nor a uniform
simultaneous small-step/large-dimension theorem.

The clock starts with rigid local spacing, yet (2) produces Sine$_2$.
Therefore this theorem still cannot transfer noisy universality back
to the deterministic initial spectrum. The model-specific deterministic
noise-removal or Heisenberg joint-trace estimate remains open. No
quantization of all chaotic systems is covered by (2).
