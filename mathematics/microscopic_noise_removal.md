# Exact microscopic noise defect and barriers to deterministic transfer

**Claim ID: BGS-FLOW-015. Status: PROJECT PROOF + STANDARD EXTERNAL INPUTS +
INDEPENDENT INTERNAL CHECK OF NEW IMPLICATIONS + EXACT AND FINITE CONTROLS.**
5 October 2026. This is a deterministic-transfer diagnostic, not a proof
of the frozen-map BGS conjecture. The Dyson generator, its trace
cut-and-join calculus, Dynkin's identity and the clock relaxation mechanism
are standard or prior corpus inputs. The result here makes their precise
transfer boundary explicit and proves the initial-jet obstruction below.
Priority and external referee validation are not asserted.

## 1. Objects and the exact remaining implication

For a unitary $A$ of dimension $N$, write its eigenangles as
$\theta_1,\ldots,\theta_N$ modulo $2\pi$, with multiplicities. Given
$0\le f\in C_c^\infty(\mathbb R)$, put $\lambda_N=N/(2\pi)$ and

$$
f_N(x)=\sum_{\ell\in\mathbb Z}f(x+\ell N),\qquad
Z_f(\theta;\alpha)=\exp\left[-\sum_j
 f_N\bigl(\lambda_N(\theta_j-\alpha)\bigr)\right],
\quad \Phi_{N,f}(A)=\frac1{2\pi}\int_0^{2\pi}Z_f(\theta;\alpha)d\alpha.
\tag{D1}
$$

This definition has no branch discontinuity. At each fixed $N$ it is a
smooth class function on $U(N)$, including at repeated eigenvalues:
the sum in the exponent is the trace of a smooth function of $A$.
It is also invariant under common scalar rotation. Let $B_s$ be full
normalized unitary Brownian motion with mean $\mathbb E B_s=e^{-s/2}I$,
and $P_sF(A)=\mathbb E F(B_sA)$. Its generator on the simple-angle locus is

$$
G_N=\frac1{2N}\sum_j\partial_j^2+
\frac1{2N}\sum_j\sum_{k\ne j}
\cot\frac{\theta_j-\theta_k}{2}\,\partial_j.
\tag{D2}
$$

For rotation-invariant functions full and traceless Brownian semigroups
agree: their independent scalar Brownian factor is a common rotation.
This is an assertion about these observables, not equality of matrix laws.

For the unchanged frozen $U_N$, the general U1--U4 theorem of FLOW-014
applies directly with $A_N=U_N$, $d_N=CN^{-1/40}$ and $\kappa_N=0$,
using the existing FM-007 bound. It gives
$P_{t_N}\Phi_{N,f}(U_N)\to\Phi_{\rm Sine}(f)$ at $t_N=8g_N$,
$g_N=4\log J_N/J_N$, $J_N=\lfloor c\log N\rfloor$.
No commutation of Brownian evolution with Möbius centering is assumed.
The weak local deterministic target is
$\Phi_{N,f}(U_N)\to\Phi_{\rm Sine}(f)$ for every such positive test.
The stronger signed factorial target TRACE-005 remains separate;
unbounded correlation moments are not inferred from weak convergence.

## 2. Exact Laplace generator and integrated defect

In the following formula set
$f_j^{(a)}=f_N^{(a)}(\lambda_N(\theta_j-\alpha))$:

$$
\begin{split}
G_N\Phi_{N,f}(A)=\frac1{2\pi}\int_0^{2\pi}Z_f\left\{
 \frac{N}{8\pi^2}\sum_j\bigl[(f_j^{(1)})^2-f_j^{(2)}\bigr]
 -\frac1{4\pi}\sum_{j<k}\cot\frac{\theta_j-\theta_k}{2}
                    (f_j^{(1)}-f_k^{(1)})\right\}d\alpha.
\end{split}
\tag{D3}
$$

The two derivatives of $Z_f$ are
$\partial_jZ_f=-\lambda_N f_j^{(1)}Z_f$ and
$\partial_j^2Z_f=\lambda_N^2[(f_j^{(1)})^2-f_j^{(2)}]Z_f$.
Pairing the two oriented drift terms gives exactly (D3), with no extra
factor two. The difference of derivatives cancels the cotangent pole
at a collision. The resulting expression is the restriction of the
smooth group generator and extends by continuity to repeated angles.

For every fixed $N$, $t\ge0$ and $A$, the exact signed defect is

$$
\mathfrak D_{N,f}(A,t):=
\int_0^t P_s(G_N\Phi_{N,f})(A)\,ds
=P_t\Phi_{N,f}(A)-\Phi_{N,f}(A).
\tag{D4}
$$

**Proof.** On the compact group, a smooth function and all its iterated
generator derivatives are bounded. The semigroup equation and integration
give (D4), without a minimum-gap assumption or an asymptotic interchange.
All integrals are at fixed dimension first.

Consequently, whenever the noisy Laplace limit is Sine$_2$, the
deterministic weak local limit is Sine$_2$ **if and only if**
$\mathfrak D_{N,f}(A_N,t_N)\to0$ for every positive smooth compact test.
For the actual map this is an exact reduction, not a proved estimate.
The modulus belongs outside the entire signed integral. A bound
$t_N\sup_{0\le s\le t_N}|P_sG_N\Phi_{N,f}(U_N)|=o(1)$ would suffice;
no such bound is established here.

## 3. Exact mixed-trace hierarchy: what a Fourier attack must control

Let $p_m(A)=\operatorname{Tr}A^m$, $p_0=N$, and
$P_{\boldsymbol m}=\prod_{a=1}^kp_{m_a}$ with all $m_a\ne0$.
The generator has the exact algebraic action

$$
\begin{split}
G_NP_{\boldsymbol m}={}&-\frac12\sum_a|m_a|P_{\boldsymbol m}
 -\frac1{2N}\sum_a|m_a|\sum_{b=1}^{|m_a|-1}
 P_{\boldsymbol m\setminus m_a\,\cup\,(\sigma_ab,\,m_a-\sigma_ab)}\\
 &-\frac1N\sum_{a<b}m_am_b
 P_{\boldsymbol m\setminus(m_a,m_b)\,\cup\,(m_a+m_b)},
 \qquad \sigma_a=\operatorname{sgn}m_a.
\end{split}
\tag{D5}
$$

A zero merged index contributes the scalar $p_0=N$; it must be removed
with that factor, not replaced by one. Repeated indices in the tuple are
distinct factor positions and carry their displayed multiplicities.

**Derivation.** For $m>0$, the cotangent identity
$i\cot((\theta_j-\theta_k)/2)=-(z_j+z_k)/(z_j-z_k)$, $z_j=e^{i\theta_j}$,
and $z_j^m-z_k^m=(z_j-z_k)\sum_{b=0}^{m-1}z_j^{m-1-b}z_k^b$ give

$$
G_Np_m=-\frac m2p_m-\frac m{2N}\sum_{b=1}^{m-1}p_bp_{m-b},
\qquad
G_N(p_mp_n)-p_nG_Np_m-p_mG_Np_n=-\frac{mn}{N}p_{m+n}.
\tag{D6}
$$

Conjugation gives negative $m$; the diffusion product rule gives (D5).
In particular $G_N|p_m|^2=m^2-m|p_m|^2-
(m/N)\Re(\bar p_m\sum_{b=1}^{m-1}p_bp_{m-b})$ for $m>0$,
which reproduces the prior pair identity in the resolvent frontier.

For charge-zero tuples, the spaces spanned by products with
$\sum_{m_a>0}m_a=\sum_{m_a<0}|m_a|\le q$ are finite and preserved by
$G_N$: splitting preserves $q$, same-sign merging preserves it, and
opposite-sign merging decreases it. At $q\ge N$ there can be algebraic
trace relations; treating the spanning symbols as independent is not
justified. This is a finite closed hierarchy, not closure at fixed
correlation order or uniformly bounded complexity when $q\asymp N$.

For example put $X=|p_1|^2$, $Y=|p_2|^2$,
$Z=\Re(p_2\bar p_1^2)$ and $W=|p_1|^4$. Directly from (D5),

$$
\begin{aligned}
G_NX&=1-X,&G_NY&=4-2Y-2Z/N,\\
G_NZ&=-2Z-(W+Y)/N+4X/N,&G_NW&=-2W-2Z/N+4X.
\end{aligned}
\tag{D7}
$$

The CUE values $(1,2,0,2)$ are stationary for $N\ge2$.
This check does not determine the actual starting values.

For $h=1-e^{-f}$ and $N$ larger than the diameter of its support, let
$\widehat h(\xi)=\int h(x)e^{-2\pi ix\xi}dx$. The distinct-index sum
$D_A(\boldsymbol m)$ is that of TRACE-001 with angles $\theta/(2\pi)$.
Finite inclusion-exclusion and Fourier expansion yield exactly

$$
\Phi_{N,f}(A)=\sum_{k=0}^N\frac{(-1)^k}{k!N^k}
\sum_{\substack{\boldsymbol m\in\mathbb Z^k\\\sum_am_a=0}}
 \left(\prod_a\widehat h(m_a/N)\right)D_A(\boldsymbol m).
\tag{D8}
$$

The $k=0$ term is one and the $k=1$ term is $-\int h$.
For each fixed $N,k$ the inner series and its generator derivatives
converge absolutely, since $h$ is smooth and compactly supported.
Substituting the prior partition-Mobius formula for $D_A$, then (D5),
gives an exact trace expression for (D3)--(D4).
It requires signed mixed products with indices of order $N$;
fixed trace bounds do not estimate it. No passage through an infinite
$k$ expansion or uniform-in-$N$ derivative series is asserted.

## 4. A flatness theorem for separated configurations

Let the support of $f$ lie in an interval of length $w<1$, and put
$a_f=\int_{\mathbb R}(1-e^{-f(x)})dx$. Suppose the minimum cyclic
unfolded eigenangle gap of $A$ is strictly greater than $w$.
Then an observation window can meet at most one eigenangle, so

$$
\Phi_{N,f}(A)=1-a_f.
\tag{D9}
$$

Indeed $\prod_j(1-h_N(\lambda_N(\theta_j-\alpha)))$
equals $1-\sum_jh_N(\lambda_N(\theta_j-\alpha))$ pointwise; each
summand integrates to $a_f/N$ under the uniform origin.
The strict gap inequality persists in a neighborhood of $A$ in $U(N)$
by continuity of its multiset of eigenvalues. Thus $\Phi_{N,f}$ is
constant on that neighborhood, and locality of the group differential
operator proves the much stronger assertion

$$
G_N^r\Phi_{N,f}(A)=0\quad(r\ge1),\qquad
\left.\frac{d^r}{dt^r}P_t\Phi_{N,f}(A)\right|_{t=0+}=0.
\tag{D10}
$$

The second equality uses the fixed-$N$ smooth semigroup equation.
It is a smooth flat jet, not an analytic Taylor expansion in time.

## 5. All-positive-trace control and a nonvanishing integrated defect

For every odd $N\ge3$, modify one eigenvalue of the clock:

$$
A_N=\operatorname{diag}\bigl(e^{iN^{-4}},
 e^{2\pi i/N},\ldots,e^{2\pi i(N-1)/N}\bigr).
\tag{D11}
$$

Its minimum unfolded gap is $1-N^{-3}/(2\pi)$. Its spectrum is simple,
globally uniform in the limit, and has bounded occupancy on each fixed
unfolded window. For every integer $m>0$,

$$
p_m(A_N)=\begin{cases}
e^{imN^{-4}}-1,&N\nmid m,\\
N-1+e^{imN^{-4}},&N\mid m.
\end{cases}
\tag{D12}
$$

These traces are all nonzero: in the first case $mN^{-4}$ is a nonzero
rational and cannot be $2\pi$ times an integer, by irrationality of
$\pi$; in the second their modulus is at least $N-2>0$.
For $1\le m<N$, $|p_m|\le mN^{-4}$. Thus this family satisfies the
entire FM-007-type logarithmic trace window, bounded first two
unnormalized traces, and the strip/potential hypotheses of FLOW-014
at its logarithmic time. For that last assertion one can take
$J=\lfloor c\log N\rfloor$, $d=J/N^5$, $\kappa=0$,
$g=4\log J/J$, $t=8g$ in U1--U3 of FLOW-014.
It is an abstract spectral control, not the actual frozen map.

Let $f$ be nonzero, smooth, nonnegative and supported in an interval
of length $w<1$. For every sufficiently large $N$, (D9)--(D10) hold
for (D11), at **every** finite derivative order.
Nevertheless, for every $t_N\to0$ with $Nt_N\to\infty$,

$$
P_{t_N}\Phi_{N,f}(A_N)\longrightarrow\Phi_{\rm Sine}(f),\qquad
\mathfrak D_{N,f}(A_N,t_N)\longrightarrow
\delta_f:=\Phi_{\rm Sine}(f)-(1-a_f)>0.
\tag{D13}
$$

**Noisy limit.** Couple $B_tA_N$ and $B_tC_N$ with the same Brownian
matrix; their operator distance is $|e^{iN^{-4}}-1|\le N^{-4}$.
The phase-matching bound and uniform-origin integration give

$$
|\Phi_{N,f}(V)-\Phi_{N,f}(W)|
 \le\frac{\|f'\|_1}{2\pi}\sum_j|\Delta\theta_j|
 \le\frac{\|f'\|_1 N}{\pi}\arcsin(\|V-W\|/2).
\tag{D14}
$$

Here the derivative of the exponential is bounded by the sum of
absolute derivatives because $f\ge0$; the integrated derivative for
each eigenangle is $\|f'\|_1$, even with periodization. The distance
above therefore costs $O_f(N^{-3})$ uniformly in $t$. The prior
Dyson clock bound, FLOW-007 (2)--(4), proves the first part of (D13),
with error $C_f[(Nt)^{-1}+N^{-2}]+O_f(N^{-3})$.

**Strict positive defect.** The positive sine-kernel operator weighted
by $h=1-e^{-f}$ has eigenvalues $0\le\eta_j<1$, trace $a_f<w<1$,
and Fredholm determinant $\Phi_{\rm Sine}(f)$. Set

$$
e_2=\frac12\iint h(x)h(y)\left[1-
 \left(\frac{\sin\pi(x-y)}{\pi(x-y)}\right)^2\right]dxdy>0.
\tag{D15}
$$

It is the second elementary symmetric function of the eigenvalues.
Nonzero smooth $f$ is positive on an interval, so the strict inequality
holds off the diagonal. Bonferroni's inequality for the eigenvalue
product gives $\prod(1-\eta_j)\ge1-a_f+e_2-e_3$;
$3e_3\le a_fe_2$ follows by expanding the nonnegative sums.
Both facts pass from finite products to the trace-class limit. Hence

$$
\delta_f\ge(1-a_f/3)e_2>0.
\tag{D16}
$$

Combining (D4), (D9) and the noisy limit proves (D13). In particular,
eventually
$\sup_{0\le s\le t_N}|P_sG_N\Phi_{N,f}(A_N)|\ge\delta_f/(2t_N)$,
despite all initial generator derivatives being exactly zero.
No finite or infinite formal heat-jet cancellation at the starting
matrix can replace the required signed integrated estimate.
The statement is for these narrow tests; it does not assert flatness
for every compact test of arbitrary support.

## 6. Unscaled full stationarity is impossible with bounded starting traces

The required microscopic cancellation must not be strengthened into
unscaled Brownian stationarity for every class function. Suppose
$|p_1(A_N)|+|p_2(A_N)|\le K$ and use $X,W,Z$ from (D7). Set
$c_*=(\sqrt{17}-1)/4$. Then

$$
\max\{|G_NX(A_N)|,|G_NW(A_N)|\}
\ge c_*-2K^3/N.
\tag{D17}
$$

Indeed $W=X^2$ at a deterministic matrix, $X\ge0$ and
$|Z|\le |p_2||p_1|^2\le K^3$. With $y=X-1$ the two expressions
without $-2Z/N$ have absolute values $|y|$ and $2|1-y^2|$.
If $|y|\ge c_*$ the first suffices; otherwise
$2(1-y^2)>2(1-c_*^2)=c_*$. Perturbing the second expression
by at most $2K^3/N$ proves (D17).

By FM-013, this applies eventually to the **actual** frozen family
with $K=20$, albeit with an ineffective startup threshold. It rules out
unscaled full-class infinitesimal Haar stationarity as a deterministic
transfer premise. It does not rule out the normalized microscopic mixed
loop hierarchy of LOOP-001, and is not a necessary-condition failure for
BGS. No fixed-frequency Haar moment law is demanded by the local target.

## 7. A quantitative boundary for uniform backward heat inversion

The following is a formal consequence of standard unitary character
calculus, not a new Casimir formula. For odd $N\ge3$ and $r\ge1$, let
$\chi_{N,r}$ be the irreducible character of highest weight
$(r,0,\ldots,0,-r)$ and $d_{N,r}=\chi_{N,r}(I)$. It is invariant under
common scalar rotation. For $F_{N,r}=\chi_{N,r}/d_{N,r}$,

$$
\|F_{N,r}\|_\infty=1,\qquad
G_NF_{N,r}=-\gamma_{N,r}F_{N,r},\qquad
P_tF_{N,r}=e^{-t\gamma_{N,r}}F_{N,r},\quad
\gamma_{N,r}=\frac{r(r+N-1)}N.
\tag{D18}
$$

Here the supremum bound follows from the unitary representation and
equality at the identity. One can check the normalization directly:
put $\rho_i=(N+1-2i)/2$ and use the Weyl alternant
$\chi_\lambda=\det[e^{i(\lambda_i+\rho_i)\theta_j}]/
\det[e^{i\rho_i\theta_j}]$ on the simple locus. The circular
Vandermonde $H=\det[e^{i\rho_i\theta_j}]$ satisfies
$\partial_j\log H=\frac12\sum_{k\ne j}\cot((\theta_j-\theta_k)/2)$.
Therefore the scalar heat conjugation gives

$$
G_N\chi_\lambda=-\frac1{2N}
\left[\sum_i(\lambda_i+\rho_i)^2-\sum_i\rho_i^2\right]\chi_\lambda.
\tag{D19}
$$

The quotient extends as the smooth character at collisions. Substituting
the two nonzero highest-weight entries yields (D18). This agrees with
Lemoine, arXiv:2303.11286, PDF internally marked v3, Section 1.2 and
equations (17)--(18): its normalized Casimir is twice our $\gamma$.
For full Brownian motion, the fundamental and determinant characters
both decay as $e^{-t/2}$. Under traceless motion the determinant is
constant and the fundamental decays as $e^{-(1-N^{-2})t/2}$;
the charge-zero mode in (D18) is unchanged. Thus the scalar factor is
accounted for explicitly.
No asymptotic Yang--Mills theorem is used.

Any linear left inverse of $P_t$ on an image containing this eigenmode
has sup-norm operator bound at least $e^{t\gamma_{N,r}}$. The same lower
bound holds for a Lipschitz inverse containing the two points $0$ and
$P_tF_{N,r}$. At $r=N$ it is $e^{(2N-1)t}$. Thus at FLOW-014's
logarithmic time it exceeds every fixed power of N. Polynomially small
uniform output errors cannot support a uniformly stable inversion on
this function class.

This is an obstruction to **uniform** inversion over these growing-degree
class functions. It does not prove a lower bound for one particular local
Laplace test, or exclude a model-specific comparison for $U_N$.
The character eigenmodes are global objects; they must not be silently
identified with the positive compact local tests in D1.

## 8. Infinite entropy of every finite deterministic spectral field

For any dimension $N\ge3$ and any fixed unitary spectrum, including the
actual map, define its stationary periodic field on the full line by

$$
\Xi_N=\sum_{j=1}^N\sum_{\ell\in\mathbb Z}
\delta_{x_j+\ell N+V},\quad
x_j=N\theta_j/(2\pi),\quad V\sim\operatorname{Unif}[0,N).
\tag{D20}
$$

It has intensity one, including multiplicities. Write $Q_N$ for its law
and $\Pi$ for the unit-intensity Poisson law. For every interval $I$ of
length at least two,

$$
\operatorname{Ent}(Q_N|_I\,\|\,\Pi|_I)=+\infty,
\qquad \operatorname{ent}(Q_N\,\|\,\Pi)=+\infty.
\tag{D21}
$$

**Proof.** The $N$ cyclic gaps sum to N, so one is $d\le1$. Two
consecutive labelled points at this gap fall in an interval of length two
with probability $(2-d)/N>0$. Their distance is the fixed value d.
The event of two points at that exact distance has probability zero for
Poisson: conditional on any finite count, the point locations have a
Lebesgue density; d=0 is excluded by Poisson simplicity. Thus
$Q_N|_I$ is not absolutely continuous with respect to $\Pi|_I$, proving
the first assertion. Restriction to that subinterval gives the same
failure on every larger window. Consequently every sufficiently large
window has infinite relative entropy, so its entropy divided by window
length is still infinite. This proves the specific-entropy assertion.

This definition is that of Erbar--Huesmann--Leblé, arXiv:1812.06929v1,
Definition 2.9, (2.17). Their Theorem 1 and Corollary 1.1 characterize
Sine$_\beta$ as the unique free-energy minimizer; they do not say that
arbitrary stationary fields minimize it. One cannot apply a finite-entropy
near-minimizer argument directly to the raw $Q_N$, since (D21) applies
to **every** finite deterministic spectrum. A variational route could
instead concern an already obtained subsequential limit or a justified
regularization with the order of limits explicit. This remains a
different, open model-specific obligation. Infinite finite-N entropy
does not preclude a weak limit with finite entropy; no upper
semicontinuity of entropy is assumed. This is not an obstruction to BGS
itself or to the published variational characterization.

## 9. Actual-map boundary and verification contract

The strict-gap assumption in Section 4 is **not** established for $U_N$.
Its purpose is a falsifier of a transfer method. D3--D8 hold for the
actual map, but neither its signed integrated defect nor its signed
Heisenberg factorial hierarchy is estimated here. Initial low traces,
global Poisson regularity, nonzero positive traces and noisy Sine$_2$
are insufficient for the proposed heat-jet shortcut. BGS-FLOW-014 is
retained with its stated noisy scope; BGS-TRACE-005 and BGS-BGS-001
remain open.

The companion verifier checks (D5) against an independent direct
Laurent-polynomial radial generator in rational arithmetic, (D7) and
finite charge closure, the separated-window identity by quadrature,
the constants in (D3), and a numerical sine determinant versus (D16).
It also checks bounded character eigenmodes and exact finite cyclic-gap
instances. These are finite controls, not proofs of the entropy or
all-highest-weight statements.
These finite checks do not prove all-$N$ estimates, actual-map noise
removal, or analytic formalization.
