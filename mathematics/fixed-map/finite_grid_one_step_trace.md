# A finite-grid proof of the original one-step and inserted traces

**Supports BGS-TRACE-109.** Analytic proof and adversarial self-review,
21 October 2026, starting from main `2271f00`. No all-time sector formula,
pressure estimate, external referee or formal verification is used here.
All limits keep $\tau=10^{-80}$ fixed and run through all odd dimensions.

Final dependency and cross-surface self-review: 22 October 2026.

## 1. Exact conventions and the needed error scale

Use the original matrices and the ordinary-half symbol $a$ in
[TRACE-106](physical_kick_trace_decay.md), §§1--2. Put $h=(2\pi N)^{-1}$,
$t_*=\tau/(2\pi)$ and $C_N=e^{3\pi iN/4}$.
The four initial phases obey the exact Gauss identity

$$
M_N(x,y)=\frac{C_N}{2\sqrt N}\sum_{m=0}^3
e^{iF_0(x/N,y/N+m)/h},\qquad
F_0(Q,s)=-\frac{3Q^2-2Qs+3s^2}{8}.                 \tag{1}
$$

An amplitude retained only to leading order gives Hilbert--Schmidt error
$O(N^{-1/2})$, which would allow $O(1)$ trace error. We retain the next
transport amplitude. The resulting errors are

$$
\|U_N-V_N\|_{\rm HS}=O(N^{-3/2}),\quad
|\operatorname{Tr}(U_N-V_N)|+
|\operatorname{Tr}(A_N(U_N-V_N))|=O(N^{-1}).         \tag{2}
$$

Constants may depend on the fixed symbol and fixed time interval but not on
$N$. The second estimate follows from the first and $\|A_N\|\le59/50$.

## 2. Phase and the first correction

Solve $F_t=a(Q,F_Q)$, $F(0)=F_0$. The characteristic field is
$(-a_p,a_Q)$, so its graph is $\Psi=\phi_{-a}^{t_*}\circ L$,
$L=\left(\begin{smallmatrix}3&-4\\-2&3\end{smallmatrix}\right)$.
On the phase-space strip of width $.01$ the finite Fourier series gives
$|a|<4$, $|X|<300$, $|DX|<20000$. For $|t|\le10^{-12}$ the endpoint
characteristic equation is a contraction with derivative error less than
$2.1\cdot10^{-8}$. It gives $F=F_0+G$, holomorphic on a fixed smaller
strip, with $|G|_{.003}\le10|t|$. Thus all fixed spatial derivatives of
$G$ are bounded uniformly over the entire real plane.

For a Fourier mode $(k,l)$ write $c=2\pi l$ and

$$
\theta_h=2\pi k(Q+\pi hl)+\frac{F(Q+ch,s)-F(Q,s)}h,\quad
\theta_0=2\pi(kQ+lF_Q),
$$
$$
d_1=2\pi^2kl+\frac{c^2}{2}F_{QQ},\qquad
d_2=\frac{c^3}{6}F_{QQQ}.
$$

The affine real part causes no large remainder: exactly

$$
\theta_h=2\pi[(k-3l/4)Q+(l/4)s]
+h(2\pi^2kl-3\pi^2l^2/2)
+c\int_0^1G_Q(Q+uch,s)\,du.                       \tag{3}
$$

For an amplitude $f$ the exact conjugated evolution is

$$
L_hf=\frac ih\sum_{k,l}a_{kl}
\left(e^{i\theta_h}f(Q+ch,s)-e^{i\theta_0}f(Q,s)\right).
$$

Taylor's integral remainder, using (3), gives $L_h=L_0+hL_1+O(h^2)$
between fixed bounded derivative norms. Explicitly,

$$
L_0f=a_p f_Q+\tfrac12(a_{Qp}+a_{pp}F_{QQ})f,
$$
$$
L_1f=i\sum_{k,l}a_{kl}e^{i\theta_0}
\left[\frac{c^2}{2}f_{QQ}+icd_1f_Q+
\left(id_2-\frac{d_1^2}{2}\right)f\right].         \tag{4}
$$

All symbol derivatives here are evaluated at $(Q,F_Q)$.
Choose bounded smooth solutions

$$
\partial_tB_0=L_0B_0,\quad B_0(0)=1,\qquad
\partial_tB_1=L_0B_1+L_1B_0,\quad B_1(0)=0.       \tag{5}
$$

Their existence and bounded fixed spatial derivatives follow by integrating
the first-order characteristic equation and its inhomogeneous equation.
Differentiating $F_{Qs}$ proves $B_0=2\sqrt{F_{Qs}}$ on the positive branch.
Thus $B^{[1]}_h=B_0+hB_1$ has evolution residual $O(h^2)$ in every fixed
derivative norm needed below. No convergence of an infinite WKB series is
assumed.

## 3. Wrapped grid shifts and Hilbert--Schmidt control

The exact deck identities are

$$
F(Q,s+4)=F(Q,s)+Q-3s-6,\quad
F(Q+1,s)=F(Q,s-3)-2s+3.                            \tag{6}
$$

They hold initially and persist by uniqueness of the Hamilton--Jacobi
equation, because the induced momentum changes are integers. The exact
operator $L_h$ respects these identities: its extra exponential factors are
$e^{2\pi il}$ or $e^{2\pi ik}$, both one. Hence $L_0,L_1$ respect them,
and uniqueness in (5) gives the corresponding amplitude permutation laws.

Define

$$
V_N(t)_{xy}=\frac{C_N}{2\sqrt N}\sum_{m=0}^3
B^{[1]}_h(t,x/N,y/N+m)e^{iF(t,x/N,y/N+m)/h}.        \tag{7}
$$

On $Q=x/N,s=y/N$, affine increments in (6), multiplied by $N$, are
integers. Thus (7) is exactly periodic on the grid. The ordinary Weyl
shift is exactly the finite matrix action, including wraps, rather than an
approximation on an unwrapped interval.
Equations (4)--(5) give entrywise residual $O(h^2/\sqrt N)$ in
$\partial_tV_N-(i/h)A_NV_N$. Its Hilbert--Schmidt norm is
$O(\sqrt N h^2)$. Equation (1) gives $V_N(0)=M_N$. Unitary Duhamel over
the fixed interval proves (2).

## 4. Discrete stationary phase with all aliases

Write $f_m(q)=F(t_*,q,q+m)$. On every lifted bounded coordinate interval,
$f_m''=-1+O(\tau)$, so it is strictly negative. Use finitely many smooth
coordinate cutoffs on the circle, with compactly supported lifts whose
integer translates form a partition of unity. Grid periodicity proved above
identifies their sums with the finite trace, without a sharp endpoint cutoff.
For each localized amplitude $b_h$, Poisson summation gives

$$
\sum_{x\in\mathbb Z}b_h(x/N)e^{2\pi iN f_m(x/N)}
=N\sum_{n\in\mathbb Z}\int b_h(q)
e^{2\pi iN(f_m(q)-nq)}\,dq.                       \tag{8}
$$

For large $|n|$, integration by parts $K$ times bounds the integral by
$C_K N^{-K}(1+|n|)^{-K}$. The remaining nonstationary terms have the
same $N^{-K}$ bound. These estimates are summable over every alias.
At a stationary point the one-dimensional Morse coordinate and the Gaussian
integral give the leading value with integral error $O(N^{-3/2})$.
The amplitudes $B_0+hB_1$ have uniformly bounded required derivatives;
their $hB_1$ correction contributes only $O(N^{-1})$ after stationary phase.
The outside factor in (7) turns the summed stationary error into $O(N^{-1})$.

The stationary equations are $P-p=n$, $Q-s=-m$, precisely the fixed-point
condition on the torus. There are four inequivalent stationary points:

| $q$ | Sheet $m$ | Alias $n$ | Torus momentum | $(F_0-nq)\bmod1$ | $a$ |
|---:|---:|---:|---:|---:|---:|
| $0$ | $0$ | $0$ | $0$ | $0$ | $9/10$ |
| $0$ | $2$ | $-1$ | $1/2$ | $1/2$ | $9/10$ |
| $1/2$ | $1$ | $-1$ | $0$ | $3/4$ | $-11/10$ |
| $1/2$ | $3$ | $-2$ | $1/2$ | $3/4$ | $-11/10$ |

Each is an exact equilibrium of the kick. Hence its phase increment is
exactly $t_*a$, with no remainder in $\tau$. Strict concavity and
$f_m'=-q-m/2+O(\tau)$ exclude any other stationary classes.
Overlapping lifts do not duplicate a contribution: (6) permutes sheets and
aliases, preserves the amplitude, and changes the critical phase by an
integer. The cutoff weights on the lifts sum to one.

If $J=F_{Qs}>0$, differentiation of the canonical equations gives

$$
f_m''=J(2-\operatorname{Tr}D\Psi).
$$

The prefactors in (7)--(8) therefore combine to
$\zeta_N(\operatorname{Tr}D\Psi-2)^{-1/2}$, where
$\zeta_N=C_Ne^{-i\pi/4}=e^{2\pi i(3N-1)/8}$.
At the four stationary points,

$$
a_{qq}=\frac{\pi^2}{125}(-19606,-19594,24306,24894),
\quad a_{pp}=a_{qp}=0,
$$
$$
D\Psi=\begin{pmatrix}1&0\\t_*a_{qq}&1\end{pmatrix}L.
$$

This gives exactly the four $T_{ij}$ and constants $\mathsf A,\mathsf B$
defined in [TRACE-109](inserted_trace_coboundary.md), and proves
its one-step trace formula (1).

## 5. Insertion and consequences

Apply the exact finite Weyl sum to (7). After removal of the same phase,
its amplitude is

$$
\sum_{k,l}a_{kl}e^{i\theta_h}
B_h^{[1]}(Q+2\pi hl,s)
=a(Q,F_Q)B_0(Q,s)+O(h)                            \tag{9}
$$

in the same fixed spatial derivative norms. Apply (8) directly to (9), and
use the inserted error in (2). The four values of $a$ in the table prove
the inserted-trace formula (2) of TRACE-109 with $O(N^{-1})$ remainder.
No remainder is differentiated.

The projection and two-copy identities in that note now give their stated
unconditional lower constants for this original family. Also
$\liminf(|\operatorname{Tr}U_N|^2-\sum_x|U_N(x,x)|^2)\ge200\tau$
follows by combining its one-step lower bound with TRACE-108.
This discrepancy vanishes after multiplication by $N^{-2}$; neither it nor
the coboundary obstruction determines the full microscopic pair defect.
