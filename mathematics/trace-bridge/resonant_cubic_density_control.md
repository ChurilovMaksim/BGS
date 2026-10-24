# Resonant cubic deletion from local spectral density

**Claim ID:** `BGS-TRACE-011`. **Status:** project proof,
author self-review, credited external CUE moment formula and finite controls;
no external validation or priority
claim. The deterministic frozen-map application is conditional on estimates
explicitly left open below. Work dated 1 October 2026, without subagents.

This closes a subsidiary question left by
[TRACE-010](signed_heisenberg_comparison.md): its cardinality loss is
avoidable if local spectral density is controlled. It also supplies an
actual unitary counterexample to replacing the needed tail control by a
bounded critical third moment. Neither statement solves BGS.

## 1. Exact hypotheses and conclusion

Let the eigenvalues of an arbitrary unitary of dimension N be
$e^{2\pi i x_j}$, with $x_j\in\mathbb T=\mathbb R/\mathbb Z$, and write
$T_m=\sum_j e^{2\pi i m x_j}$. Multiplicities are counted. For the fixed
partition into N half-open intervals of length 1/N, let n_h be their
occupancies and define

$$
M_s(N)=\frac1N\sum_{h=0}^{N-1}n_h^s,\qquad s\ge1.       \tag{1}
$$

Fix $0<a<b$, $2b<1$, $I_N=[aN,bN]\cap\mathbb Z$,
$J_N=[aN,2bN]\cap\mathbb Z$, and a positive integer d. Set

$$
E_N=\frac1{N^2}\sum_{\substack{j\in J_N\\d\mid j}}|T_j|^2,
\qquad Q_N=\frac1{N^2}\sum_{j\in J_N}|T_j|^2.            \tag{2}
$$

For $W\in C_c^\infty((a,b)^2)$ and
$\mathcal R_d=\{(m,n)\in I_N^2:d\mid m\text{ or }n\text{ or }m+n\}$,
let

$$
Z_N(W)=N^{-3}\sum_{(m,n)\in\mathcal R_d}
 W(m/N,n/N)T_mT_n\overline{T_{m+n}}.                     \tag{3}
$$

**Theorem 1 (no cardinality loss).** Constants below depend on the fixed
weight/support and on s, but not on N or d:

$$
|Z_N(W)|\le C_W\sqrt{E_N M_4(N)}.                       \tag{4}
$$

More generally, for $3<s\le4$,

$$
|Z_N(W)|\le C_{W,s}
 E_N^{(s-3)/(s-2)}M_s(N)^{1/(s-2)}.                     \tag{5}
$$

Thus $E_N M_4(N)\to0$ suffices; neither bounded maximum occupancy nor
a rate involving the number of resonant times is required. The modulus
is outside the whole signed sum in (3). These are not bounds for the
sum of the absolute values of its summands.

Here is the full factorial version. With $L=|I_N|$, $\ell=L/N$, and
$\Delta_3(m,n)=D_3(m,n,-m-n)-2(N-m-n)$, define
$Y_N(W)=N^{-3}\sum_{\mathcal R_d}W\Delta_3$. Then

$$
|Y_N(W)-Z_N(W)|\le\|W\|_\infty
\left[3\ell E_N+6(\ell/d+1/N)Q_N
             +12b\ell(\ell/d+1/N)\right].              \tag{6}
$$

In particular $d\to\infty$, $E_N\to0$, and $\sup_N M_s(N)<\infty$
for any $s>3$ imply $Y_N(W)\to0$. The CUE counterterm is the exact
finite-dimensional positive-cone value, not a pointwise prediction for
one deterministic trace.

## 2. Positive smoothing and frequency selection

Use the positive Gaussian $\eta(u)=\sqrt\pi\exp(-\pi^2u^2)$, whose
Fourier transform (kernel $e^{-2\pi i u\xi}$) is $e^{-\xi^2}$, and set

$$
\rho_N(x)=\sum_{j=1}^N\sum_{v\in\mathbb Z}
 \eta\bigl(N(x+x_j+v)\bigr).
$$

The reflection of the phases is intentional. Then
$\int_{\mathbb T}\rho_N=1$ and

$$
\widehat\rho_N(m)=e^{-(m/N)^2}T_m/N,
\qquad c_s M_s(N)\le\|\rho_N\|_s^s\le C_s M_s(N).       \tag{7}
$$

Apply both bounds to $\rho_N(-x)$, whose norm equals that of rho and
whose phase positions agree with the original half-open bins exactly.
For the lower bound, every x in a bin has distance at most 1/N from
all its phases; use $\min_{|u|\le1}\eta(u)>0$ and integrate.
For the upper bound, on each bin bound the kernel by a
summable cyclic convolution of occupancies with
$C_A(1+\operatorname{dist}(h,0))^{-A}$, where $A>1$, and apply discrete
Young. All constants are uniform in N, including bins with endpoint atoms.

For $w\in C_c^\infty(\mathbb R)$ define

$$
F_w(x)=N^{-1}\sum_m w(m/N)T_m e^{2\pi i m x}.
$$

This is a convolution multiplier of $\rho_N$ with symbol
$w(\xi)e^{\xi^2}$. Its periodized kernel is
$N\sum_v \mathcal F^{-1}[we^{\xi^2}](N(x+v))$, with L1 norm at most
$\|\mathcal F^{-1}[we^{\xi^2}]\|_{L^1(\mathbb R)}$. Hence

$$
\|F_w\|_s\le C_w\|\rho_N\|_s.                          \tag{8}
$$

Multiplying w by $e^{2\pi i t\xi}$ just translates this kernel, so its
L1 constant is independent of t. No positivity of w is assumed.

The arithmetic projection is a positive contraction on every Ls:

$$
P_d f(x)=\frac1d\sum_{h=0}^{d-1}f(x+h/d),\qquad
\widehat{P_df}(m)=\mathbf1_{d\mid m}\widehat f(m).        \tag{9}
$$

It commutes with these multipliers. If w is supported in the scaled
window $J_N/N$, Parseval gives the crucial estimate

$$
\|P_dF_w\|_2^2\le\|w\|_\infty^2 E_N.                   \tag{10}
$$

## 3. Proof of the trilinear estimates

First take a factorized weight
$w_1(m/N)w_2(n/N)\overline{w_3((m+n)/N)}$. Its signed sum on the first
strip is exactly

$$
\int_{\mathbb T}(P_dF_{w_1})F_{w_2}\overline{F_{w_3}}.   \tag{11}
$$

Cauchy--Schwarz and Holder, followed by (7)--(10), bound this by
$C\sqrt{E_N}\|\rho_N\|_4^2\le C\sqrt{E_N M_4(N)}$.
The other two strips obey the same bound, with the projected factor
in the second or third place. Intersecting two strips forces all three;
the same argument with additional projections still applies, since
P_d contracts L4.

The union is exactly the sum of the three strip indicators minus twice
$\mathbf1_{d\mid m,d\mid n}$. This accounts for overlaps without
discarding phases or silently omitting the strip $d\mid m+n$.

For general W, choose smooth real cutoffs $\chi_1,\chi_2$ inside (a,b)
and $\chi_3$ inside (2a,2b), equal to 1 on the corresponding projections
of the compact support of W. Fourier inversion on $\mathbb R^2$ yields

$$
W(x,y)=\chi_1(x)\chi_2(y)\chi_3(x+y)
 \int_{\mathbb R^2}\widehat W(u,v)e^{2\pi i(ux+vy)}\,du\,dv.
$$

The factorized constants above are independent of u,v by the kernel
translation observation after (8). Since $\widehat W\in L^1$, integrate
the bound against $|\widehat W|$. This proves (4) for arbitrary complex
smooth weights; finite frequency sums make the interchange immediate.

For $3<s<4$, put $r=s/(s-2)$ and $\theta=2(s-3)/(s-2)$. Then
$1/r=\theta/2+(1-\theta)/s$, and Holder in (11) gives

$$
\|P_dF_{w_1}\|_r\|F_{w_2}\|_s\|F_{w_3}\|_s
 \le C E_N^{\theta/2}\|\rho_N\|_s^{3-\theta}.
$$

Since $(3-\theta)/s=1/(s-2)$, this is (5). At s=4 it is (4).
For s>4, $\|\rho_N\|_4\le\|\rho_N\|_s$ and a bounded Ms suffices too.

## 4. Exact counterterm budget

The distinct-label identity is
$D_3=T_mT_n\overline{T_{m+n}}-|T_m|^2-|T_n|^2-|T_{m+n}|^2+2N$.
Consequently

$$
\Delta_3=T_mT_n\overline{T_{m+n}}
         -|T_m|^2-|T_n|^2-|T_{m+n}|^2+2(m+n).            \tag{12}
$$

For any one of these three pair terms, fixing its own resonant
frequency allows at most L companions. If its frequency is not
resonant, there are at most $2(L/d+1)$ companions in the other strips.
Each term is therefore bounded by
$LN^2 E_N+2(L/d+1)N^2Q_N$. The union has at most
$3L(L/d+1)$ points, and $2(m+n)\le4bN$. This proves (6).
Finally $Q_N\le e^{8b^2}\|\rho_N\|_2^2\le C_{s,b}M_s^{2/s}$ by
Parseval and (7). Thus the stated factorial limit follows.

## 5. The critical third moment and its sharp failure

There is a valid critical version: if the functions $\rho_N^3$ are
uniformly integrable on the unit circle and $E_N\to0$, (3) tends to
zero. Together with $d\to\infty$ this gives the factorial limit.
Uniform integrability is stronger than $\sup_N M_3<\infty$.

To prove it, positive kernel majorants in (8) and the positive average
(9) preserve uniform integrability of their cubes. Normalize the
absolute kernel to a probability measure nu and write
$g=\nu*\rho_N\le R+\nu*(\rho_N\mathbf1_{\rho_N>R})$.
On $g>2R$, its cube is bounded by eight times the cube of the second
term. Jensen and integration therefore give
$\int_{g>2R}g^3\le8\int_{\rho_N>R}\rho_N^3$.
Kernel masses are uniformly bounded, including all translations u,v;
composition with P_d is still convolution by a positive probability
measure. Thus the cubes of $P_dF_w$ are uniformly integrable.
Their L2 norms tend to zero by
(10), so splitting at a fixed amplitude threshold, then sending the
threshold to infinity, gives $\|P_dF_w\|_3\to0$, uniformly for the
cutoff translations. Holder with three L3 factors and Fourier inversion
proves the assertion. This argument is a tail criterion, not a
consequence of bounded third moment alone.

**Theorem 2 (realizable critical obstruction).** Let $q\to\infty$ and
$d\to\infty$ be integers, and set $N=dq^3$, $K=dq$, $H=N-K$. Take a
unitary spectrum consisting of an H-clock and q copies of a d-clock.
For every nonzero integer $j<H$,

$$
T_j=K\mathbf1_{d\mid j}.                               \tag{13}
$$

For the fixed cone above, all involved frequencies are below H for
large q. Hence

$$
E_N=O(1/q),\quad Q_N=E_N,\quad \sup_N M_3(N)<\infty,
\qquad Z_N(W)\longrightarrow\int_{\mathbb R^2}W(x,y)\,dx\,dy. \tag{14}
$$

Indeed only m,n both divisible by d contribute; $N/d=q^3$ and
$K^3/(Nd^2)=1$, so (3) is the Riemann sum with mesh $1/q^3$.
Equation (6) shows the same nonzero limit for $Y_N(W)$ whenever
$\int W\ne0$. The H-clock contributes at most two phases to each
1/N bin; the rare d-clock bins contain q additional phases. Their
normalized third occupancy moment is $dq^3/N=1$, whereas their
fourth moment is of order q. This realizes the exact critical failure.
The pair mass is small because $K^2/(Nd)=1/q$; its product with M4
need not tend to zero, consistently with (4).
For $3<s\le4$, its Ms has order $q^{s-3}$; the right-hand side of
(5) stays of constant order. The interpolation exponents are therefore
sharp in the scaling of this family, without any claim about best constants.

One can remove every multiplicity: order all phase labels and replace
$x_j$ by $x_j+j/N^6$ modulo 1. Distinct original phase positions have
separation at least $1/(Hd)>N^{-2}$; identical positions now separate.
For $|m|\le2bN$, each trace changes by $O(N^{-3})$. The whole normalized
cubic sum changes by $O(N^{-2})$ using $|T_m|\le N$ and O(N^2) modes;
pair mass changes by $O(N^{-3})$. Clusters occupy at most two adjacent
bins, so M3 remains bounded. The obstruction therefore persists for
simple spectra. It is not caused solely by exact degeneracy.

This counterexample does not satisfy full CUE pair comparison: its
background is a clock. It proves exactly that resonant pair mass plus
bounded third local moment does not control the resonant cubic. It is
not the spectrum of the maintained map or a prime-subsequence theorem.

## 6. A critical obstruction compatible with every signed pair test

The clock background in Theorem 2 is unnecessary. The following stronger
construction uses Haar measure only to prove existence of abstract
deterministic spectra; it does not randomize the frozen quantum map.

**Theorem 3 (pair-invisible resonant clustering).** There exists a sequence
of odd dimensions $N_l\to\infty$, integers $d_l\to\infty$, and simple
unitary spectra such that, for every $f\in C_c^\infty((0,\infty))$,

$$
N_l^{-2}\sum_{m\ge1}f(m/N_l)
 \bigl(|T_m|^2-\min(m,N_l)\bigr)\longrightarrow0,        \tag{15}
$$

$\sup_l M_3(N_l)<\infty$, and E in (2) tends to zero on every compact
positive window. Nevertheless, for any fixed $0<a<b<1/4$ and every
$W\in C_c^\infty((a,b)^2)$, both the resonant-sector factorial discrepancy
and the full-box factorial discrepancy tend to $\int W$. In particular
a weight of nonzero integral violates the cubic CUE comparison.
The d's are prescribed abstract resonance periods, not proved orders of
the actual cat map modulo prime dimensions.

**Proof.** Take odd $q_l=2^l+1$, $d=q$, $N=q^4$, $K=q^2$ and $H=N-K$.
Replace the H-clock by the spectrum of Haar $V_H$, whose traces are V_m;
retain q copies of the d-clock. Then $T_m=V_m+h_m$ with
$h_m=K\mathbf1_{d\mid m}$ for every positive m.

We first establish the needed CUE reference controls without treating
arbitrary Heisenberg powers as independent Gaussians. Its joint density
is the finite projection determinant with
$P_H$ projecting onto $1,e^{2\pi ix},\ldots,e^{2\pi i(H-1)x}$.
The identity

$$
\mathbb E\exp\Bigl(\sum_j t_j V_{m_j}\Bigr)
 =\det\left(I+P_H(e^{\sum_jt_je^{2\pi i m_jx}}-1)P_H\right)
$$

follows by expanding the Vandermonde density and integrating its rows
(equivalently the elementary determinant integral identity). Expanding
the logarithm and differentiating gives the cumulant as the sum over
ordered nonempty set partitions, with coefficient $(-1)^{v-1}/v$ and
terms $\operatorname{Tr}(P_HE_{s_1}P_H\cdots E_{s_v}P_H)$.
Every multiplication $E_s$ is unitary and each trace has magnitude at
most H. Thus $|\kappa_4|\le26H$, since
$\sum_{v=1}^4(v-1)!S(4,v)=1+7+12+6=26$.
Rotation invariance and the two-block formula give
$\mathbb EV_m=0$ and
$\mathbb E V_m\overline V_n=\mathbf1_{m=n}\min(m,H)$ for positive modes.
The moment--cumulant relation therefore yields

$$
\operatorname{Cov}(|V_m|^2,|V_n|^2)
 =\mathbf1_{m=n}\min(m,H)^2+\kappa_4(m,-m,n,-n).         \tag{16}
$$

For any bounded weights supported at $m\le BN$, the normalized signed
pair variance is consequently $O_B(N^{-1})$, uniformly in H<=N.
Also $\min(m,N)-\min(m,H)\le K$ and $K/N=q^{-2}$.
The cluster pair mass is $O_B(q^{-1})$. Its cross term with V is bounded
by the geometric mean of this mass and the CUE pair mass, which is
bounded in probability. This proves (15) in probability for each test.
The mean resonant mass of V is $O_B(d^{-1}+N^{-1})$, and the cluster
mass is $O_B(q^{-1})$, so the total E tends to zero in probability.

Here is a uniform third-occupancy bound. Let a_h count CUE phases in the
fixed 1/N bins. The determinant density and Hadamard give
$\mathbb E(a_h)_r\le(H/N)^r\le1$. Hence
$\mathbb E a_h^3\le5$ and $\mathbb E a_h^6\le203$, the corresponding
Stirling-number sums. For disjoint bins, the block determinant inequality
for positive Gram matrices gives
$\mathbb E(a_h)_r(a_j)_s\le\mathbb E(a_h)_r\,\mathbb E(a_j)_s$.
To see this without a negative-association theorem, apply
$\det\left(\begin{smallmatrix}A&B\\B^*&C\end{smallmatrix}\right)
\le\det A\det C$ pointwise to the CUE kernel, and integrate the two
groups of positions over their disjoint bins. The singular case follows
by continuity from positive definite Gram matrices. Since powers are
nonnegative combinations of falling factorials, the cubic counts have
nonpositive cross covariances. Thus

$$
\mathbb E\left[N^{-1}\sum_h a_h^3\right]\le5,
\qquad\operatorname{Var}\left[N^{-1}\sum_h a_h^3\right]\le203/N.
$$

The clusters alone have third moment 1, so
$(a_h+c_h)^3\le4(a_h^3+c_h^3)$ shows that the full M3 is at most 28
with probability tending to one; the failure probability is at most
203/N. This does not give uniform integrability of the cubic density.

For the cubic, $4bN<H$ for all sufficiently large q. We may therefore
use Diaconis--Evans Theorem 2.1(a), with weighted degree at most 4bN,
for every sixth, fourth and second moment below. Expanding the cubic
product gives seven terms containing V and the pure cluster term.
Every V-containing term has zero mean. The all-V normalized weighted
sum has variance $O_W(1/N)$, even after restriction to the union.
A term containing one h has variance at most
$C_W K^2/(N^2d)$: exact Gaussian moment matching forces the unordered
remaining mode pair to match; there are O(N^2/d) terms, each covariance
at most $C N^2$. A term containing two h's is a weighted linear trace
sum. Group by its remaining frequency: there are O(N/d) groups, each
has O(N/d) coefficients, and each trace variance is O(N). Its variance
is at most $C_W K^4/(N^2d^3)$. The same estimates hold without the
union restriction, since the h-containing terms are already on it.
Their combined mean-square error is therefore bounded by

$$
C_W\left(N^{-1}+K^2/(N^2d)+K^4/(N^2d^3)\right)
 =O_W(q^{-3}).                                         \tag{17}
$$

The pure cluster term has the Riemann-sum limit $\int W$ as before.
Equation (6) disposes of all factorial counterterms in the union.
For the full box, the three counterterms are weighted signed pair
errors: their CUE variances, after multiplication by coefficients
of size O(N), are still O(1/N) by (16). Cluster pair and cross terms
vanish by the same Cauchy--Schwarz argument used for (15).
Thus both cubic discrepancies converge to $\int W$ in probability.

To obtain deterministic spectra, use a countable dense family of smooth
pair and cubic tests and compact windows. Along the stated exponential
q_l, the variance bounds are summable; apply Chebyshev to each fixed
test, Markov to the positive resonant mass and the bound 203/N to M3.
The first Borel--Cantelli argument gives simultaneous almost-sure limits
for the countable family and eventual bounded M3. Bounded mass extends
pair convergence by uniform approximation. For cubic convergence on
each fixed cone, (17) bounds its mean-square error by $O(q^{-3})$ times
the squared sup norm of W. A uniform Sobolev argument extends to all
smooth weights; no unproved bound on the total variation of the cubic
measure is needed. Explicitly expand a smooth W in a fixed box
Fourier series, inserting fixed smooth cutoffs around its compact support.
Each translated smooth cutoff coefficient has the same
variance bound. Weighted Cauchy--Schwarz against summable Fourier
coefficients gives $\mathbb E\|\mathcal E_l\|_{H^{-t}}^2=O(q_l^{-3})$
for any $t>1$ in two variables. Markov and summability imply the
V-containing error tends to zero in H^{-t} almost surely. The full-box
pair counterterms obey the analogous one-dimensional bound; the
deterministic cluster pair error is uniformly O(1/q). Countably many
compact subboxes cover all the stated smooth weights. Select one
such realization. Finally distinct background points occur almost surely;
move each phase by a different amount of magnitude at most N^{-5},
avoiding the finitely many collisions. The trace and cubic budgets in
Theorem 2 preserve all limits. Every phase moves to at most an adjacent
bin, so the bounded third moment survives with a fixed constant.
This proves Theorem 3.

The pair-versus-higher-correlation distinction is prior mathematics,
already exhibited by the project's finite homometric example. Theorem 3
adds this specific resonance/critical-tail construction and its checked
scales. It asserts no universal chaos counterexample or world-first priority.
Failure of an unbounded factorial correlation test does not by itself
exclude weak convergence of the local point process. No weak-process
counterexample is claimed here; moment tails are a separate issue.

## 7. All-order raw version and the unchanged actual-map obligation

The same proof for k factors, $m_k=-\sum_{j<k}m_j$, bounds any fixed
smooth signed raw product sum restricted to the union of the k strips
$d\mid m_j$ by

$$
C_{W,k}\sqrt{E_N M_{2(k-1)}(N)}.                        \tag{18}
$$

Here let $\mathcal A_N$ be the union of the integer frequency windows
supporting the smooth one-variable cutoffs used to factor the weight,
and define
$E_N=N^{-2}\sum_{j\in\mathcal A_N,\ d\mid j}|T_j|^2$.
This includes positive and negative frequencies and also $j=0$ whenever
it is active. Since $T_0=N$, an active zero mode gives $E_N\ge1$;
this bound then supplies no vanishing-energy deletion conclusion.
Weights supported away from every zero-frequency hyperplane admit
cutoffs using only nonzero windows, as in the positive-cone theorem above.
Each projected factor has the Parseval bound (10). Use L2 for it and
$L^{2(k-1)}$ for the others; inclusion--exclusion has finitely many
terms depending only on k. Fourier inversion in k-1 variables handles
general weights. This is a raw-product bound, not an automatic
all-order factorial comparison: proper subset resonances and exact
finite-CUE counterterms must still be treated.

For the maintained prime family, substitute the correctly oriented
block $U_p^{d_p}=\zeta_p C_{p,d_p}$ from
[TRACE-009](../fixed-map/prime_resonant_sector.md). Its mass in (2) is exactly
$p^{-2}\sum_{rd_p\in J_p}|\operatorname{Tr}C_{p,d_p}^r|^2$.
The elementary lower bound on d_p implies $d_p\to\infty$. Therefore
two explicit estimates, $E_p\to0$ and bounded $M_s(p)$ for some s>3
(or critical cubic uniform integrability), delete the entire resonant
factorial cubic sector. Both estimates are currently **OPEN for the
actual frozen map**. The existing effective gap floor is far smaller
than 1/p and supplies neither. The seven-cut transfer, scalar finite
type and reference CUE variance do not establish these hypotheses.
The quantitative alternative $E_p=O(1/d_p)$ and $M_4(p)=o(d_p)$
also suffices. If instead $d_p\ge cp$ on a subsequence, its bounded
number of resonant times already makes the earlier TRACE-010 bound
sufficient under $Q_p=O(1)$ and $E_p\to0$. The new density mechanism
matters particularly when that number grows. Neither regime is assumed
to cover all actual prime orders with the required estimates proved.

The remaining signed nonresonant cubic, other Fourier cones, composites
and all higher factorial orders are separate obligations. The frozen
coupling stays $\tau=10^{-80}$; no random or coupling average is inserted.
Elementary smoothing and Holder are prior methods; no claim of a new
general interpolation theorem or a world-first discovery is made.

An attempt to obtain the density hypothesis from pairs alone stops at
$M_4\le N M_2^2$: use $\max_h n_h^2\le\sum_hn_h^2=NM_2$.
Bounded second moment therefore gives only O(N), and Theorem 3 shows
that full signed pair comparison cannot supply critical cubic tails.
An exact positive reformulation of the next estimate is

$$
\|\rho_N\|_4^4=N^{-4}\sum_{m_1+\cdots+m_4=0}
 e^{-\sum_j(m_j/N)^2}\prod_{j=1}^4T_{m_j}=O(1).         \tag{19}
$$

The Gaussian makes this identity absolutely convergent at each N. It is
a bounded positive four-trace energy, not the full fourth-order CUE law.
No argument from the frozen ordered block presently estimates (19).

Verification: [finite audit](../../computations/verification/resonant_density_audit.py),
[review](../../archive/record/resonant_density_review_20261001.md).
