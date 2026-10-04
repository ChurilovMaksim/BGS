# Polynomial coboundary comparison from bounded-trace initial spectra

**Claim ID: BGS-FLOW-012.** Project derivation, 4 October 2026.
Base: `4982f8fc3d6303cc2cf7840e608f07d41ba2783e`.
This extends the initial-state comparison, not the Dyson relaxation theorem.
The actual fixed map remains the target; its coupling is not changed.

## 1. Objects and statement

Fix $K<\infty$. Let $N\ge N_K$ be odd and let $A_N$ be any unitary with
$|p_1(A_N)|+|p_2(A_N)|\le K$, $p_j(A)=\operatorname{Tr}A^j$.
Start the **original uncentered** chain at $U_0^\varepsilon=A_N$:

$$
U_{j+1}^\varepsilon=
e^{i\varepsilon(G_j-U_j^\varepsilon G_jU_j^{\varepsilon *})}
U_j^\varepsilon,
\qquad \mathbb E(G_j)_{ab}(G_j)_{cd}=N^{-1}\delta_{ad}\delta_{bc}.
\tag{G1}
$$

The $G_j$ are independent normalized GUE. Define $Y_0=\Pi(A_N)$ using
the unique small Möbius centering of FLOW-009. Let $D_t[Y_0]$ be
normalized traceless unitary Brownian motion from **this stated initial
matrix**. Common rotation is removed by the independent uniform observation
origin. For the unfolded averaged Laplace functional $\Phi_{N,f}$,
$0\le f\in C_c^\infty(\mathbb R)$, $h=\varepsilon^4/2$,
$n=\lfloor t/h\rfloor$, $1/N\le t\le1/12$, and sufficiently small
absolute $\varepsilon>0$,

$$
\left|\mathbb E\Phi_{N,f}(U_n^\varepsilon)
-\mathbb E\Phi_{N,f}(D_t[Y_0])\right|
\le C_{f,K}\left[
\sqrt t+N^{-1}+N^4\varepsilon+N^9\varepsilon^2
+tN^9\varepsilon+tN^{10}\varepsilon^2\right].
\tag{G2}
$$

The centering is part of the **reference initial condition**; it is not
inserted into the random algorithm. No comparison to Dyson motion from
the uncentered $A_N$, or to Sine$_2$, is silently substituted.

At $t=N^{-2/3}$, $\varepsilon=N^{-26/3}$ and exactly $n=2N^{34}$,
(G2) is $O_{f,K}(N^{-1/3})$. In particular it applies eventually to the
unchanged frozen map at $\tau=10^{-80}$: FM-013 gives $|p_1|<4$,
$|p_2|<9$, hence $K=20$. Its dimension threshold remains ineffective.
Its stochastic-chain local limit is Sine$_2$ **if and only if** the
corresponding centered-start Dyson law has that limit at these times.
Neither limit is proved for this initial family here.

## 2. Initial chart and the fast boundary layer

Put $x_0=m_1(A_N)$ and $\rho=\varepsilon/N+\varepsilon^4$.
FLOW-009 (3) gives $|w(A_N)|\le8K/N$. Expanding $p_2(M_wA_N)$ gives

$$
p_2(Y_0)=p_2(A_N)-2wp_1(A_N)+2\bar w p_3(A_N)+O(N|w|^2),
\qquad |p_2(Y_0)|\le C_K.
\tag{G3}
$$

Use the same stops as FLOW-010: centered $|m_2|=2/5$, or
$|m_1|=a=1/1024$, with the larger chart and large-jump control retained.
Take $N_K$ sufficiently large that the initial point is strictly inside.
The contraction inequality FLOW-010 (5), which is uniform in every
pre-exit initial matrix, now yields

$$
\mathbb E[|x_j|^{2p};j<\sigma]
\le e^{-c_p\varepsilon^2j}|x_0|^{2p}+C_p\rho^{2p}.
\tag{G4}
$$

Its $p=1$ square root and geometric summation imply

$$
h\sum_{j<n}\mathbb E[|x_j|;j<\sigma]
\le C\varepsilon^2|x_0|+Ct\rho.
\tag{G5}
$$

The first term is the fast initial boundary layer. Omitting it would
incorrectly apply the clock-start estimate to a noncentered initial matrix.

There is no $\varepsilon^{-2}|x_0|^{2p}$ exit loss. Apply the same
one-step Lyapunov inequality to the **frozen stopped** variable and drop
its negative drift. For $p=3$,

$$
\mathbb E|x_{n\wedge\sigma}|^6
\le |x_0|^6+C n\varepsilon^2\rho^6
\le |x_0|^6+C(t+1)(\varepsilon^4/N^6+\varepsilon^{22}).
\tag{G6}
$$

Thus a first-trace exit has probability at most the right side times
$a^{-6}$. A union bound on the decaying initial term in (G4) would be
needlessly nonuniform for very small $\varepsilon$; (G6) avoids it.

## 3. Localization and weak comparison

Use FLOW-010's nonnegative extension $F_2=|p_2|^2$,
$\|F_2\|_6\le CN^2$, and $\overline L F_2\le C$.
Its local weak expansion (8) remains unchanged. Starting with (G3) and
using (G5) gives

$$
\mathbb E F_2(\Pi U_{n\wedge\sigma})
\le C_K+Ct+C N^6\{
\varepsilon^2|x_0|+t(\rho+\varepsilon^2)\}.
\tag{G7}
$$

Divide by $N^2(2/5)^2$ on a second-trace exit without a large jump.
Together with (G6) and the inherited Gaussian large-jump estimate this
implies the deliberately coarse, dimension-uniform bound

$$
\mathbb P(\sigma\le n)
\le C_K[N^{-2}+(t+1)N^4\varepsilon].
\tag{G8}
$$

The $N^{-2}$ includes the nonzero initial second trace. It cannot be
replaced by the clock's $t/N^2$ without another argument.

FLOW-011 proves dimension-uniform coefficient derivative bounds on the
whole localized centered chart and hence
$\|S_sF\|_6\le Ce^{Cs}\|F\|_6$. These estimates do not depend on a clock
initial matrix. Telescope its backward semigroup using FLOW-010 (8),
(G5), and (G8). For $0\le F\le1$ the resulting error is bounded by

$$
C_K[N^{-2}+N^4\varepsilon]
+C N^4\|F\|_6\{
\varepsilon^2|x_0|+t(\varepsilon/N+\varepsilon^2)\}.
\tag{G9}
$$

The time-increment and final-rounding budgets are the same as in
FLOW-011 (P14), absorbed in $tN^4\|F\|_6\varepsilon^2$ for $t\ge1/N$.
No derivative of a killed boundary semigroup is required.

For the nonnegative microscopic test, FLOW-011 (P18) gives
$\|\Phi_{N,f}\|_6\le C_fN^6$. Since $|x_0|\le K/N$, the extra
boundary-layer term in (G9) is at most $C_{f,K}N^9\varepsilon^2$.
Terminal centering costs at most
$C_f\mathbb E[|x_n|;n<\sigma]\le C_{f,K}/N+C_f\rho$ by FLOW-009 (5)
and (G4). Discarded paths cost their exit probability.

For the projected diffusion from $Y_0$, FLOW-009 (13) gives an exit
probability $C_K/N^2$ on $t\le1$. Equations (14)--(15) there couple it
to $D_t[Y_0]$ with
$N\mathbb E\|Y_{t\wedge\sigma}-D_{t\wedge\sigma}\|_{\rm HS}^2
\le C_Kt$. FLOW-004's spectral matching and origin-averaged estimate
therefore give a Laplace error $C_{f,K}\sqrt t+C_K/N^2$.
Combining these bounds proves (G2).

## 4. Consequences and the missing input

At the displayed $2N^{34}$ steps the new boundary-layer term is
$N^9\varepsilon^2=N^{-25/3}$; the leading errors are $\sqrt t$ and
$tN^9\varepsilon=N^{-1/3}$. The original starting matrix is retained.
Smooth $L^1$ approximation extends convergence comparisons to
nonnegative $C_c^1$ tests, without asserting the rate at that regularity.

More generally $\varepsilon=N^{-10}$ makes (G2) vanish for any
$t_N\to0$ with $Nt_N\ge1$, using at most $2t_NN^{40}$ steps.
This does **not** select a relaxation time or make the noise invisible.

The [cluster obstruction](dyson_relaxation_obstruction.md) shows that
bounded fixed traces, global equidistribution, simplicity and nonzero
power traces cannot imply Sine$_2$ at an arbitrarily prescribed vanishing
time. The [FM-007 Poisson corollary](frozen_mesoscopic_regularity.md)
supplies initial regularity down to a logarithmic scale, including for
the exact centered spectrum. The separate [FLOW-014 proof](circular_dyson_actual_start.md)
closes circular relaxation at $t_N=8g_N$, with $g_N=4\log J_N/J_N$;
the logarithmic input does not select the faster $N^{-2/3}$ time.
This comparison claim alone does not identify its reference law.
Deterministic noise removal and BGS-TRACE-005 remain
separate open obligations. This is a scoped stochastic comparison proof,
not deterministic BGS or a priority claim.
