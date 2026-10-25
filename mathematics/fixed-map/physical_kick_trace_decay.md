# Uniform trace decay of the physical kick

**Claim:** BGS-TRACE-106. **Status:** analytic author proof, reconstructed and
author-checked on 21 October 2026; not externally refereed or Lean-formalized.
The imported manuscript proves the exponent $1/25$. The positive-square
localization below strengthens it to $1/9$. No priority claim is made.

## 1. Exact family and conclusions

For odd $N\ge3$, put $e_N(t)=\exp(2\pi it/N)$ and

$$
(T_N(a,b)\psi)(x)=e_N\bigl(b(x+\overline2a)\bigr)\psi(x+a),
\qquad x,a,b\in\mathbb Z/N\mathbb Z,
$$

where $\overline2$ denotes the modular inverse. Let $q,p\in\mathbb R/\mathbb Z$,
$e^{i\alpha_0}=(-3+4i)/5$, and

$$
\begin{aligned}
r(q)&=(1-\cos14\pi q)(1+\cos2\pi q),\\
f(q,p)&=\cos14\pi q+\frac{r(q)}{10}
 +\frac{r(q)\sin2\pi q}{100}
 +\frac{r(q)\cos(2\pi p-\alpha_0)}{100}.
\end{aligned}
$$

If $f-1/10=\sum c_{kl}e^{2\pi i(kq+lp)}$, define
$A_N=\sum c_{kl}T_N(l,k)$ and $E_N(t)=e^{itNA_N}$.
This is the original modular quantization; $A_N=A_N^*$.
Write $\operatorname{tr}_N=N^{-1}\operatorname{Tr}$.

**Theorem 1.** There is a finite constant $C$, independent of $N,t$, such that

$$
\left|\operatorname{tr}_N E_N(t)\right|
 \le C(N|t|)^{-1/9},\qquad
0<|t|\le10^{-20},\quad N|t|\ge1.                 \tag{1}
$$

The prefactor is not evaluated numerically. In particular (1) applies to
the unchanged physical coupling $t=\tau=10^{-80}$.

**Theorem 2.** For every finite $T>0$, there are $C_T,c_T>0$ such that

$$
|\operatorname{tr}_N E_N(t)|\le C_T(N|t|)^{-c_T},\qquad
0<|t|\le T,\quad N|t|\ge1.                     \tag{2}
$$

If $0<|t_N|\le T$ and $N|t_N|\to\infty$, the empirical eigenvalue
measure of $E_N(t_N)$ converges to Haar measure on the circle. Moreover,

$$
\inf_{|z|=1}N^{-1/2}\|E_N(t_N)-zI\|_{\rm HS}\to\sqrt2,
\qquad \inf_{|z|=1}\|E_N(t_N)-zI\|_{\rm op}\to2.       \tag{3}
$$

For the original unitary

$$
(M_N)_{xy}=N^{-1/2}e_N\bigl(-\overline8(3x^2-2xy+3y^2)\bigr),
\qquad U_N=E_N(\tau)M_N,
$$

this gives $\inf_{|z|=1}\|U_N-zM_N\|_{\rm op}\to2$.
This is a distance between matrices, not a distance between spectra modulo
arbitrary unitary conjugation. None of these statements proves the local
spectral law of $U_N$ or estimates its full Heisenberg-time trace sum.

## 2. Ordinary-half conversion and elementary calculus

For integer labels $v=(k,l)$ set

$$
\mathsf W_N(k,l)=(-1)^{kl}T_N(l,k),\qquad
Q_N(b)=\sum_v\widehat b(v)\mathsf W_N(v).
$$

These integer-labelled matrices have the exact product

$$
\mathsf W_N(v)\mathsf W_N(w)
 =e^{\pi i\Omega(v,w)/N}\mathsf W_N(v+w),\qquad
\Omega(v,w)=lk'-kl'.                              \tag{4}
$$

They must not be reduced modulo $N$ while discarding the resulting signs.
The actual ordinary-half symbol of $A_N$ is

$$
a(q,p)=\cos14\pi q+\frac{r(q)}{10}
 +\frac{r(q)\sin2\pi q}{100}-\frac1{10}
 +\frac{r(q+1/2)\cos(2\pi p-\alpha_0)}{100}.         \tag{5}
$$

Indeed multiplication by $(-1)^{kl}$ translates the $l=\pm1$ coefficient
by half a $q$-period. Thus $A_N=Q_N(a)$ for every odd modulus, including
small moduli with Fourier aliases.

Let $|b|_s=\sum_v(1+|v|)^s|\widehat b(v)|$. Equation (4) gives

$$
\begin{aligned}
\|Q_N(b)\|&\le |b|_0,\\
\|Q_N(b)Q_N(c)-Q_N(bc)\|&\le C N^{-1}|b|_1|c|_1,\\
\|[Q_N(b),Q_N(c)]\|&\le C N^{-1}|b|_1|c|_1.
\end{aligned}                                                   \tag{6}
$$

For real $\eta$, symmetrize the double Fourier sum in (4). Its sine part
cancels exactly. Since $|\cos x-1|\le x^2/2$,

$$
\|Q_N(\eta)^2-Q_N(\eta^2)\|
 \le C N^{-2}|\eta|_2^2.                           \tag{7}
$$

Also $Q_N(\eta)=Q_N(\eta)^*$, so its square is positive. Orthogonality
of Weyl labels gives

$$
\operatorname{tr}_N Q_N(\eta)^2
 \le \|\eta\|_{L^2}^2+C N^{-2}|\eta|_2^2.            \tag{8}
$$

To check the aliases in (8), expand $Q_N(\eta)^*Q_N(\eta)$.
Diagonal labels give $\sum|\widehat\eta(v)|^2$ exactly. Other nonzero
traces require $v-w\in N\mathbb Z^2\setminus\{0\}$; then at least one
label has length at least $N/2$. The absolute sum is bounded by
$2|\eta|_0\sum_{|v|\ge N/2}|\widehat\eta(v)|\le C N^{-2}|\eta|_2^2$.
Possible alias phases have modulus one and do not affect this bound.

Fourier Cauchy--Schwarz and Parseval in dimension two give the sharper
derivative budgets

$$
|b|_1\le C\|b\|_{H^3}\le C\|b\|_{C^3},\qquad
|b|_2\le C\|b\|_{H^4}\le C\|b\|_{C^4}.              \tag{9}
$$

For example the first inequality factors each summand into
$(1+|v|)^{-2}$ times $(1+|v|)^3|\widehat b(v)|$ and uses
$\sum_{v\in\mathbb Z^2}(1+|v|)^{-4}<\infty$.

## 3. Uniform Egorov estimate with its small-time factor

Use $\{a,b\}=a_qb_p-a_pb_q$ and the flow $\kappa_t$ of
$X=(a_p,-a_q)/(2\pi)$. From (4) and $|\sin x-x|\le |x|^3/6$,

$$
\left\|iN[A_N,Q_N(b)]+\frac1{2\pi}Q_N(\{a,b\})\right\|
 \le C_a N^{-2}|b|_3.                              \tag{10}
$$

The sign follows from $\{e_v,e_w\}=4\pi^2\Omega(v,w)e_{v+w}$.
For fixed $b$, all required derivatives of $b\circ\kappa_t$ are bounded
on $|t|\le T$. Differentiating, then integrating the discrepancy by
unitary Duhamel, yields

$$
E_N(t)Q_N(b)E_N(t)^*
 =Q_N(b\circ\kappa_t)+O_{b,T}(|t|N^{-2}).             \tag{11}
$$

Only the two fixed characters $b_1=e^{2\pi iq}$ and $b_2=e^{2\pi ip}$
are inserted in (11). No $N$-dependent cutoff is inserted in Egorov.
Define, with the smooth value at $t=0$,

$$
d_j(t,z)=\frac{b_j(z)-b_j(\kappa_tz)}t,
\quad d_j(0,z)=-Xb_j(z),\quad v_t=|d_1|^2+|d_2|^2.    \tag{12}
$$

All their fixed spatial derivatives are uniformly bounded on $|t|\le T$:
$d_j=-\int_0^1(Xb_j)\circ\kappa_{ut}\,du$.
For $F=E_N(t)$ and $\mu(u)=\operatorname{tr}_N(Q_N(u)F)$, cyclicity,
(6) and (11) imply

$$
|\mu(ud_j)|\le C_T(N|t|)^{-1}|u|_1.                 \tag{13}
$$

Explicitly, putting $B=Q_N(b_j)$, $C_j=Q_N(b_j\circ\kappa_t)$ and
$R=FBF^*-C_j$ gives
$\operatorname{tr}_N[Q_N(u)(B-C_j)F]
=\operatorname{tr}_N([Q_N(u),B]F)+\operatorname{tr}_N(Q_N(u)RF)$.
Replace the product by its symbol using (6), then divide by $t$.
The $O(|t|N^{-2})$ term becomes $O(N^{-2})$ and is bounded by
$C_T(N|t|)^{-1}$. This proves (13) even for varying $u$.

## 4. Positive-square localization: the strengthening

Suppose uniformly on a bounded time interval

$$
\operatorname{vol}\{v_t\le\delta\}\le C_T\delta^\beta,
\qquad 0<\delta<\delta_T.                            \tag{14}
$$

Choose a real smooth $\rho$ with $0\le\rho\le1$, equal to one on
$[0,1]$ and zero on $[2,\infty)$. Set

$$
\eta=\rho(v_t/\delta),\quad \chi=\eta^2,
\qquad u_j=(1-\chi)\overline{d_j}/v_t,
$$

extending $u_j$ by zero near $v_t=0$. The derivatives in (12) are
uniformly bounded, and the derivatives of $(1-\rho(s/\delta)^2)/s$
of order $j\le3$ are $O(\delta^{-j-1})$. Thus

$$
|u_j|_1\le C_T\delta^{-4},\qquad
|\eta|_2\le C_T\delta^{-4}.                         \tag{15}
$$

The identity $\sum_j u_jd_j=1-\chi$ and (13) bound the exterior by
$C_T(N|t|)^{-1}\delta^{-4}$.
For the interior use (7), then positivity of $Q_N(\eta)^2$:

$$
\begin{aligned}
|\mu(\chi)|
&\le |\operatorname{tr}_N(Q_N(\eta)^2F)|
       +C N^{-2}|\eta|_2^2\\
&\le \operatorname{tr}_N Q_N(\eta)^2+C N^{-2}|\eta|_2^2\\
&\le C_T\delta^\beta+C_TN^{-2}\delta^{-8}.
\end{aligned}                                                   \tag{16}
$$

The middle inequality holds for every positive matrix $P$ and unitary
$F$: $|\operatorname{Tr}(PF)|\le\operatorname{Tr}P$ by diagonalizing $P$.
No positivity of Weyl quantization itself is assumed.
Writing $R=N|t|$ and using $N^{-2}\le T^2R^{-2}$ gives

$$
|\operatorname{tr}_N E_N(t)|\le C_T
 \left(\delta^\beta+R^{-1}\delta^{-4}+R^{-2}\delta^{-8}\right).
                                                               \tag{17}
$$

Choose $\delta=R^{-1/(4+\beta)}$. The first two terms are
$R^{-\beta/(4+\beta)}$, and the third is their square. For sufficiently
large $R$ the sublevel cutoff condition holds; enlarge the constant for
the remaining bounded interval $R\ge1$. Therefore (14) implies exponent
$c=\beta/(4+\beta)$, instead of the imported $\beta/(12+\beta)$.

## 5. Explicit sublevel exponent for the actual symbol

Put $\theta=2\pi q$, $\varphi=2\pi p-\alpha_0$,
$c=\cos\theta$, $s=\sin\theta$, $z=\cos\varphi$. Formula (5) is

$$
a=A\cos7\theta+B,
\quad A=1-(1+c)(1/10+s/100)+(1-c)z/100,
\quad B=c/10+(1+c)s/100+(1-c)z/100.
$$

Direct differentiation and the triangle inequality give

$$
19/25\le A\le51/50,\qquad
|A_\theta|,|B_\theta|\le7/50,\qquad
|A_{\theta\theta}|,|B_{\theta\theta}|\le4/25.
$$

If $|\sin7\theta|\ge1/4$, then $|a_\theta|\ge21/20$.
On the fourteen complementary arcs, $|\cos7\theta|>19/20$ and

$$
|a_{\theta\theta}|>
49(19/25)(19/20)-14(7/50)(1/4)-8/25
=4321/125>34.
$$

For each fixed $p$, $a_\theta$ is monotone on each such arc.
Consequently, in normalized torus volume,

$$
\operatorname{vol}\{|a_\theta|\le u\}\le7u/(17\pi),
\qquad0<u\le1.                                      \tag{18}
$$

Indeed each arc contributes length at most $2u/34$ in $\theta$.
The symbol has frequencies $|k|+|l|\le9$ and Fourier norm below two.
Hence $\|X\|_\infty\le18$ and $\|DX\|_\infty\le324\pi<2000$ in
the induced maximum norm. For the lifted displacement $\Delta_t$,

$$
\|\Delta_t\|_\infty\le18|t|,\qquad
\|\Delta_t-tX(z)\|_\infty
 \le |t|\|X(z)\|_\infty\frac{2000|t|}{1-2000|t|}.     \tag{19}
$$

To obtain the relative bound, integrate
$\|X(\kappa_s z)-X(z)\|\le(e^{2000|s|}-1)\|X(z)\|$,
which follows from Gronwall along the positive or negative trajectory.
For $|t|\le10^{-20}$, (19) gives
$\|\Delta_t\|_\infty\ge|t|\|X(z)\|_\infty/2$, and its components
have modulus below $1/2$. Since $|e^{2\pi ix}-1|\ge4|x|$ there,

$$
\sqrt{v_t}\ge4\|\Delta_t\|_\infty/|t|
 \ge2\|X(z)\|_\infty\ge2|a_\theta|.
$$

The same conclusion holds at zero by continuity. Inserting
$u=\sqrt\delta/2$ in (18) proves

$$
\sup_{|t|\le10^{-20}}\operatorname{vol}\{v_t\le\delta\}
 \le \frac7{34\pi}\sqrt\delta,\qquad0<\delta\le1.     \tag{20}
$$

Thus $\beta=1/2$ in (17), giving $c=1/9$ and proving Theorem 1.

## 6. Every bounded time interval and spectral consequences

On the entire circle $q=0$, (5) gives

$$
a=9/10,\quad da=0,\quad a_{pp}=a_{pq}=0,\quad
a_{qq}=-\frac{2\pi^2}{25}(1960-\cos(2\pi p-\alpha_0))<0.
$$

Every point there is stationary. Its flow derivative is
$D\kappa_t=I+tL$ with
$L=\left(\begin{smallmatrix}0&0\\-a_{qq}/(2\pi)&0\end{smallmatrix}\right)$,
$L\ne0$ and $L^2=0$. Therefore $\kappa_t\ne\mathrm{Id}$ for every
$t\ne0$. The functions $v_t$ in (12) are jointly real analytic and
none is identically zero, including at $t=0$.

Here is the uniform finite-type argument needed for (14). At every
zero $(t,z)$, a finite-order spatial derivative of $v_t$ is nonzero:
otherwise its convergent spatial Taylor series and analytic continuation
on the connected torus would give $v_t\equiv0$. A nonzero homogeneous
differential has a nonzero value in a real spatial direction. Its modulus
is bounded below on a product of a small time interval and a rotated
spatial rectangle. Finitely many such products cover the compact zero
set in $[-T,T]\times\mathbb T^2$. Outside the union, $v$ has a positive
minimum. On each rectangle, apply the one-dimensional estimate
$|\{|g|\le\delta\}|\le C_j(\delta/c)^{1/j}$ when
$|g^{(j)}|\ge c$, then integrate the transverse variable.
For completeness, that estimate follows by selecting $j+1$ sublevel
points separated by a constant times the sublevel measure, and applying
the divided-difference mean-value formula. The divided difference is at
most $C_j\delta/L^j$ and at least $c/j!$, where $L$ is that measure.
This proves (14) with some $\beta_T>0$, uniformly in $t$.
Equation (17) proves Theorem 2 with $c_T=\beta_T/(4+\beta_T)$.

For every fixed nonzero integer $m$, apply (2) at $mt_N$ on the interval
$|t|\le |m|T$. Then $\operatorname{tr}_N E_N(t_N)^m\to0$.
Density of trigonometric polynomials proves convergence to circle Haar
measure. The exact Hilbert--Schmidt identity is

$$
\inf_{|z|=1}N^{-1}\|E_N-zI\|_{\rm HS}^2
 =2-2|\operatorname{tr}_N E_N|.
$$

For the operator norm, weak convergence implies eventual occupation of
each arc in any fixed finite covering of the circle. Hence, uniformly in
$z$, there is an eigenvalue arbitrarily close to $-z$. This yields the
lower bound $2\cos(\varepsilon/2)$; the upper bound is two. First take
$N\to\infty$, then $\varepsilon\to0$. Multiplication by $M_N^*$ proves
the asserted distance for $U_N$.

## 7. Provenance and exact remaining obligation

The imported Round 12 physical-kick proof supplies (5), (10)--(14), (18)--(20)
and the stationary-circle argument. Its $1/25$ proof is valid; it is
superseded here only quantitatively. Equations (7)--(9) and the use of a
positive square in (16) are the strengthening reconstructed in this review.
All estimates are derived here, with no new external theorem dependency.

[Review and source hashes](../../record/spectral_research/spectral_master_audit.md) record
the exact imported version, finite checks and the unreviewed historical scope.
The [finite verifier](../../computations/verification/physical_kick_trace_checks.py)
checks coefficients, alias-sensitive Weyl identities and exponent arithmetic;
it does not certify the analytic limits.

The original mixed Heisenberg-scale trace hierarchy remains open. A bound
for $E_N(t)$ is not a bound for $(E_N(\tau)M_N)^m$: its ordered interaction
picture contains different conjugated generators, with $m$ growing like $N$.
