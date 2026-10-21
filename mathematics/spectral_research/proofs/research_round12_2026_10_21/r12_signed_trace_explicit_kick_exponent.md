> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round12_2026_10_21/r12_signed_trace_explicit_kick_exponent.md`. Embedded SHA256: `91399c420e0094634dce6803f915af44ee5de68ce966ddd1b509f9568fb64c7f`.
> [Thematic guide](../../topics/approximation.md).

# An explicit small-time exponent for the original physical kick

## 0. Statement and exact scope

Let $A_N$ be exactly the matrix in the question, with the original
modular Weyl convention. There exists a finite constant $C$,
independent of odd $N$ and of real $t$, such that

$$
 \boxed{
 \left|\frac1N\operatorname{Tr}e^{itNA_N}\right|
       \le C(N|t|)^{-1/25},\qquad
 0<|t|\le10^{-20},\quad N|t|\ge1.}
                                                               \tag{0.1}
$$

The exponent and the allowed physical-time interval are explicit.
The finite prefactor $C$ is not evaluated numerically. In particular,
the prescribed physical time is included and satisfies

$$
 \boxed{
 \left|\frac1N\operatorname{Tr}e^{i10^{-80}NA_N}\right|
       \le C(N10^{-80})^{-1/25},\qquad N10^{-80}\ge1.}
                                                               \tag{0.2}
$$

The input trace argument is the one independently audited in
`r12_signed_trace_kick_audit.md`. The new point of this note is the
constructive uniform sublevel exponent $\beta=1/2$ for the actual
symbol on the displayed time interval. It replaces the unspecified
finite analytic order in that argument by explicit bounds.

These are estimates for the **single kick** $e^{itNA_N}$.
They do not estimate $\operatorname{Tr}U_N^m$ at $m\asymp N$,
and do not prove any instance of the requested `H_diag`.

## 1. The actual ordinary-half symbol

Set

$$
 W_N(k,l)=(-1)^{kl}T_N(l,k),\qquad
 Q_N(b)=\sum_{k,l}\widehat b(k,l)W_N(k,l).
$$

The exact symbol satisfying $A_N=Q_N(a)$ is

$$
 a(q,p)=\cos(14\pi q)+\frac{r(q)}{10}
       +\frac{r(q)\sin(2\pi q)}{100}-\frac1{10}
       +\frac{r(q+1/2)\cos(2\pi p-\alpha_0)}{100}.       \tag{1.1}
$$

The shift by $1/2$ is necessary: the factor $(-1)^{kl}$
changes the $q$-coefficient of every $l=\pm1$ mode by a half
translation. Thus this is the actual symbol of the original matrices,
including all odd composite moduli.

Write

$$
 \theta=2\pi q,\qquad \varphi=2\pi p-\alpha_0,
 \qquad c=\cos\theta,\quad s=\sin\theta,
 \quad z=\cos\varphi.
$$

The identity $r(q+1/2)=(1+\cos7\theta)(1-\cos\theta)$
gives the exact rearrangement

$$
 a=A(\theta,z)\cos7\theta+B(\theta,z),                  \tag{1.2}
$$

where

$$
 A=1-(1+c)(1/10+s/100)+(1-c)z/100,
$$
$$
 B=c/10+(1+c)s/100+(1-c)z/100.                          \tag{1.3}
$$

Here and below $\theta$-derivatives hold $\varphi$ fixed.

## 2. Uniform elementary derivative bounds

Since $|c|,|s|,|z|\le1$ and $1/10+s/100\ge9/100$,

$$
 \frac{19}{25}\le A\le\frac{51}{50}.                   \tag{2.1}
$$

Direct differentiation gives

$$
 A_\theta=s(1/10+s/100)-(1+c)c/100+sz/100,
$$
$$
 B_\theta=-s/10+[-s^2+(1+c)c]/100+sz/100,
$$
$$
 A_{\theta\theta}=c/10+2sc/100+s(1+2c)/100+cz/100,
$$
$$
 B_{\theta\theta}=-c/10-s(1+4c)/100+cz/100.
$$

The triangle inequality yields the rational uniform bounds

$$
 |A_\theta|,|B_\theta|\le\frac7{50},\qquad
 |A_{\theta\theta}|,|B_{\theta\theta}|\le\frac4{25}.    \tag{2.2}
$$

For example, the four terms in $A_{\theta\theta}$ are bounded
by $1/10,2/100,3/100,1/100$, respectively; their sum is
$4/25$. These bounds use no numerical sampling of the trigonometric
functions.

From (1.2),

$$
 a_\theta=-7A\sin7\theta+A_\theta\cos7\theta+B_\theta,
                                                               \tag{2.3}
$$

so whenever $|\sin7\theta|\ge1/4$,

$$
 |a_\theta|
 \ge7\frac{19}{25}\frac14-2\frac7{50}
 =\frac{21}{20}>1.                                    \tag{2.4}
$$

On the complementary fourteen closed arcs
$|\sin7\theta|\le1/4$, one has
$|\cos7\theta|\ge\sqrt{15}/4>19/20$. Moreover

$$
 a_{\theta\theta}=-49A\cos7\theta
       -14A_\theta\sin7\theta
       +A_{\theta\theta}\cos7\theta+B_{\theta\theta}.
$$

The last three terms have total modulus at most
$14(7/50)(1/4)+8/25$. Hence

$$
 |a_{\theta\theta}|
 >49\frac{19}{25}\frac{19}{20}
       -14\frac7{50}\frac14-\frac8{25}
 =\frac{4321}{125}>34.                                \tag{2.5}
$$

The leading term dominates the error, so the sign is
$-\operatorname{sgn}(\cos7\theta)$. In particular, for each
fixed $\varphi$, $a_\theta$ is strictly monotone on each
of these fourteen arcs.

It follows that, for every $0<u\le1$,

$$
 \operatorname{vol}\{|a_\theta|\le u\}
       \le\frac{7u}{17\pi}.                            \tag{2.6}
$$

Indeed, (2.4) places the sublevel set in the fourteen arcs. On each
arc the derivative bound (2.5) makes the length of its sublevel part
at most $2u/34=u/17$ in the $\theta$ variable. Divide the
sum by $2\pi$ to obtain normalized $q$-measure and integrate
over the normalized $p$ variable. Arcs crossing the origin of the
angular coordinate are read as single arcs on the circle; they do
not add an extra component.

## 3. Explicit bounds on the physical flow

Let $\kappa_t$ be the flow of

$$
 X=(a_p,-a_q)/(2\pi)
$$

in the original $(q,p)$ coordinates. Equip vectors with the
maximum norm and matrices with its induced row-sum norm.

All Fourier frequencies of (1.1) satisfy $|k|+|l|\le9$.
The Fourier one-norm of $r$ is exactly four, because

$$
 r=1+\cos\theta-\cos7\theta
          -\tfrac12\cos8\theta-\tfrac12\cos6\theta.
$$

Therefore the triangle inequality directly in (1.1) gives

$$
 \sum_{k,l}|\widehat a(k,l)|
 \le1+\frac4{10}+\frac4{100}+\frac4{100}+\frac1{10}
 =\frac{79}{50}<2.                                    \tag{3.1}
$$

The derivative factors in $X$ cancel the divisor $2\pi$.
Thus

$$
 \|X\|_\infty\le18,\qquad
 \|DX\|_\infty\le2\pi\cdot 9^2\cdot2
       =324\pi<2000.                                  \tag{3.2}
$$

For the second bound, each row is bounded by
$2\pi\sum|\widehat a(k,l)|\,|k|(|k|+|l|)$ or the same
expression with $|l|$ replacing $|k|$. This verifies the
induced matrix norm, not just each separate entry.

Fix the periodic lift of $X$ to $\mathbb R^2$, and use the
flow lift starting at a chosen lift of $z$. Denote its displacement
by $\Delta_t(z)=\kappa_t(z)-z$ in this lift. Equation (3.2)
gives

$$
 \|\Delta_t(z)\|_\infty\le18|t|.                       \tag{3.3}
$$

The following *relative* estimate, including its dependence on the
initial vector field, is useful:

$$
 \|\Delta_t(z)-tX(z)\|_\infty
 \le |t|\|X(z)\|_\infty
          \frac{L|t|}{1-L|t|},
 \qquad L=2000,\quad L|t|<1.                           \tag{3.4}
$$

To prove it for positive and negative $t$ at once, put
$\sigma=\operatorname{sgn}(t)$ and
$\gamma(s)=\kappa_{\sigma s}(z)$, $s\ge0$. The chain rule
and (3.2), followed by the integral form of Gronwall's inequality,
give

$$
 \|X(\gamma(s))\|_\infty
       \le e^{Ls}\|X(z)\|_\infty,
$$
$$
 \|X(\gamma(s))-X(z)\|_\infty
       \le(e^{Ls}-1)\|X(z)\|_\infty.
$$

These inequalities can also be obtained by iterating the integral
inequality and summing its exponential series. Integrate the second
inequality from zero to $|t|$, bound its integrand by its endpoint,
and use $e^x-1\le x/(1-x)$ for $0\le x<1$. This proves
(3.4). The estimate is valid also when $X(z)=0$, in which case
the flow remains stationary.

For $|t|\le10^{-20}$, one has
$L|t|\le2\cdot10^{-17}<1/3$. Consequently

$$
 \|\Delta_t(z)\|_\infty
      \ge\tfrac12|t|\|X(z)\|_\infty.                  \tag{3.5}
$$

Also (3.3) is less than $1/2$, so all its components are within
the range of the circle chord bound used next. No derivative of a
time-normalized displacement is needed in this comparison.

## 4. Explicit uniform sublevel estimate

Use exactly the normalized character differences from the audited
trace theorem:

$$
 b_1=e^{2\pi iq},\quad b_2=e^{2\pi ip},\qquad
 d_j(t,z)=\frac{b_j(z)-b_j(\kappa_tz)}{t},
$$
$$
 v_t(z)=|d_1(t,z)|^2+|d_2(t,z)|^2,                       \tag{4.1}
$$

with the continuous value $d_j(0,z)=-Xb_j(z)$ at zero.
In fact the exact integral identity
$$
 d_j(t,z)=-\int_0^1(Xb_j)(\kappa_{ut}z)\,du
$$
shows that every fixed spatial derivative is uniformly bounded through
$t=0$ on the stated compact time interval.
For real $|s|\le1/2$, concavity of the sine on $[0,\pi/2]$
gives

$$
 |e^{2\pi is}-1|=2\sin(\pi|s|)\ge4|s|.                \tag{4.2}
$$

Apply this to the two lift components of $\Delta_t$. Equations
(3.3)--(3.5) yield, for $0<|t|\le10^{-20}$,

$$
 \sqrt{v_t(z)}
 \ge\max_j|d_j(t,z)|
 \ge4\|\Delta_t(z)\|_\infty/|t|
 \ge2\|X(z)\|_\infty
 \ge2|a_\theta(z)|.                                   \tag{4.3}
$$

The last inequality uses $X_p=-a_q/(2\pi)=-a_\theta$.
At $t=0$ it follows by continuity (or directly from
$|Xb_j|=2\pi|X_j|$).

For $0<\delta\le1$, (4.3) and (2.6), with
$u=\sqrt\delta/2$, prove the fully uniform estimate

$$
 \boxed{
 \sup_{|t|\le10^{-20}}
 \operatorname{vol}\{z:v_t(z)\le\delta\}
       \le\frac7{34\pi}\sqrt\delta.}
                                                               \tag{4.4}
$$

Thus the sublevel exponent is explicitly $\beta=1/2$, on an
explicit interval containing the original physical time. This
conclusion uses the actual symbol and quantitative inequalities,
rather than choosing an unspecified maximum order from an analytic
covering argument.

## 5. Completion of the quantum trace estimate

For clarity, the precise audited estimate being used is

$$
 |\operatorname{tr}_N E_N(t)|
 \le C_{T_0}\left[\delta^{\beta/2}
                  +(N|t|)^{-1}\delta^{-6}\right],
 \quad T_0=10^{-20},                                   \tag{5.1}
$$

whenever the sublevel estimate with exponent $\beta$ holds at
scale $2\delta$, $0<|t|\le T_0$, and $0<\delta<1$.
Here is the chain that provides (5.1). The exact Weyl product gives
the product and commutator bounds of order $N^{-1}|b|_1|c|_1$.
Its sine remainder gives, for each of the two fixed characters,

$$
 E_N(t)Q_N(b_j)E_N(t)^*
      =Q_N(b_j\circ\kappa_t)+O(|t|N^{-2}),
$$

uniformly in $|t|\le T_0$. Cyclicity of trace then gives

$$
 |\operatorname{tr}_N(Q_N(u d_j)E_N(t))|
       \le C_{T_0}(N|t|)^{-1}|u|_1.
$$

For a fixed smooth cutoff $\chi$ equal to one on $[0,1]$
and zero on $[2,\infty)$, take
$\chi_\delta=\chi(v_t/\delta)$ and
$u_j=(1-\chi_\delta)\overline{d_j}/v_t$. Their needed Fourier
norms satisfy $|u_j|_1+|\chi_\delta|_2\le C_{T_0}\delta^{-6}$.
Five derivatives suffice for $|u_j|_1$, and six for
$|\chi_\delta|_2$; the constants are finite because the fixed
flow and its fixed derivatives are bounded on the compact interval.
The identity $\sum_j u_jd_j=1-\chi_\delta$ bounds the exterior
part of the trace. For the other part, the exact Fourier alias bound

$$
 \|Q_N(\chi_\delta)\|_{\rm HS}/\sqrt N
 \le\|\chi_\delta\|_2+C N^{-1}|\chi_\delta|_2
$$

and Cauchy--Schwarz give
$C\delta^{\beta/2}+C N^{-1}\delta^{-6}$. Absorb
$N^{-1}\le T_0/(N|t|)$ to obtain (5.1). All these steps and
the modular aliases were independently checked in the companion
audit; no universality theorem is an input.

Insert $\beta=1/2$ from (4.4). Put $R=N|t|$, and, for
sufficiently large $R$, choose

$$
 \delta=R^{-4/25}<1/2.
$$

Then $\delta^{1/4}=R^{-1/25}$, and
$R^{-1}\delta^{-6}=R^{-1/25}$ as well. This proves (0.1)
in the large-$R$ range. For the bounded remaining range
$1\le R\le2^{25/4}$, enlarge the finite constant and use
$|\operatorname{tr}_NE_N(t)|\le1$. Equation (0.2) is the
specialization to the unchanged physical constant.

## 6. Consequence and the unchanged original gap

One quantitative consequence for the physical kick is

$$
 \inf_{|z|=1}\frac1N\|e^{i10^{-80}NA_N}-zI\|_{\rm HS}^2
 =2-2\left|\operatorname{tr}_N e^{i10^{-80}NA_N}\right|
 =2+O((N10^{-80})^{-1/25}).                             \tag{6.1}
$$

The error approaches zero from below. The theorem rules out an
almost scalar matrix kick along any infinite odd subsequence, with
an explicit decay exponent. It says nothing about closeness of
unordered eigenvalue lists after an arbitrary conjugation.

The missing original estimate remains, for the fixed admissible
$b_*$ in the Round 12 target and $w=|\widehat b_*|^2$,

$$
 \frac1{N^2}\sum_{1\le m<2N}w(m/N)
 \left(\left|\operatorname{Tr}
 [(e^{i10^{-80}NA_N}M_N)^m]\right|^2-\min(m,N)\right)
       \longrightarrow0.
$$

Neither (0.1) nor (6.1) estimates that noncommuting product or this
signed sum. No conclusion about `H_diag` is asserted.

## 7. Provenance

The exact symbol comes from the problem's definitions and the ordinary
Weyl conversion in Section 1. The quantitative trace inequality is
audited from
`research_round12_2026_10_21/r12_countersequence_kick_recurrence.md`,
SHA-256
`7bb8b677cdee6f7a0a94f1d20833aec3069200056de5d6c587c365bbb89e8e1e`,
Sections 2--6. That complete mathematical part was read directly.

The $A\cos7\theta+B$ bounds were independently worked out in
this branch and by the root agent. The root proposed using them for
an explicit sublevel exponent. The relative-flow comparison
(3.4)--(4.3) supplies the stated uniformity with only the explicitly
bounded vector field and its first derivative. No claim of a new
general quantum-chaos principle is made.
