# Positive Abel decomposition and quantitative clock rigidity

**Claim ID:** `BGS-TRACE-092`. 16 October 2026.

**Status:** project proof, coordinator reconstruction and independent internal
review. The identities and quantitative theorem below are proved from their
displayed assumptions. They concern arbitrary unitary spectra and stationary
point processes, including multiplicities. They supply no estimate of the
unchanged physical propagator's Abel energy. No external priority, BGS solution or analytic Lean certificate is claimed.

The clock minimum itself is prior: see `BGS-TRACE-007` and its Cohn--Kumar
source. `BGS-TRACE-091` gives a different, Hardy-space positive remainder.
Here an elementary Fourier minorant splits the excess into low trace modes
and a nonnegative geometric pair defect. That defect also controls a local
transport distance to the clock.

## 1. Exact finite identity

Let the eigenvalues of any U in U(N) be exp(2 pi i theta_j), with theta_j in
R/Z, N>=1. Labels are retained when eigenvalues coincide. Set x_j=N theta_j,
T_m=Tr(U^m), and

\[
 L_N(s)=\frac1{N^2}\sum_{m\ge1}e^{-2sm/N}|T_m|^2,
 \qquad \delta_N(s)=L_N(s)-\frac1{e^{2s}-1},\qquad s>0.
\]

Use the Fourier convention ghat(xi)=integral g(x) exp(-2 pi i xi x) dx.
Define, with the continuous value of sinc at zero,

\[
 f_s(x)=\frac{s}{s^2+\pi^2x^2},\qquad
 q_s(x)=\frac{s^3}{\sinh^2s}
       \frac{(\sin(\pi x)/(\pi x))^2}{s^2+\pi^2x^2},
 \qquad H_s=f_s-q_s.
\]

Thus q_s>=0, q_s(0)=s/sinh^2(s), and its only real zeros are the nonzero
integers. The explicit Fourier minorant is

\[
 \widehat H_s(t)=
 \begin{cases}
 \displaystyle\frac{\sinh(2s(1-|t|))-2s(1-|t|)}{2\sinh^2s},&|t|\le1,\\
 0,&|t|>1.
 \end{cases}                                                    \tag{1}
\]

It is nonnegative, and strictly positive on (-1,1). For every N>=1,

\[
 \boxed{\displaystyle
 \delta_N(s)=\frac1{N^2}\sum_{m=1}^{N-1}
       \widehat H_s(m/N)|T_m|^2
  +\frac1{2N}\sum_{j\ne k}\sum_{\ell\in\mathbb Z}
       q_s(x_j-x_k+\ell N).}                                  \tag{2}
\]

The pair sum is ordered. Formula (2) is exact at finite N; no local limit,
simple-spectrum premise or independence assumption is used.

**Proof of (1).** The elementary transforms of f_s and sinc^2 are
exp(-2s|t|) and (1-|t|)_+, respectively. Therefore

\[
 \widehat q_s(t)=\frac{s^2}{\sinh^2s}
       \int_{-1}^1(1-|u|)e^{-2s|t-u|}\,du.                     \tag{3}
\]

For t>=1 the integral equals exp(-2st)sinh^2(s)/s^2. For 0<=t<=1,
split it at u=0 and u=t; integrating the three exponentials gives (1).
Evenness handles t<0. In particular

\[
 \widehat H_s(0)=\coth s-\frac{s}{\sinh^2s}.
\]

**Proof of (2).** For each kernel put
$g^{[N]}(x)=\sum_{\ell\in\mathbb Z}g(x+\ell N)$.
The real-space sums converge absolutely. Their Fourier series have
coefficients ghat(m/N)/N and converge absolutely: the H series is finite,
while the f and q coefficients have exponential tails. Hence

\[
 \frac1{2N}\sum_{j,k}f_s^{[N]}(x_j-x_k)=\frac12+L_N(s),
\]

\[
 \frac1{2N}\sum_{j,k}H_s^{[N]}(x_j-x_k)
  =\frac{\widehat H_s(0)}2
     +\frac1{N^2}\sum_{m=1}^{N-1}\widehat H_s(m/N)|T_m|^2.
\]

Since N is an integer, q_s(lN)=0 for l!=0, so the j=k terms contribute
exactly q_s(0)/2. Finally

\[
 \frac{\widehat H_s(0)+q_s(0)-1}{2}=\frac1{e^{2s}-1}.
\]

Subtracting proves (2). For N=1 both right-hand sums are empty.

In particular delta_N(s)>=0. Equality for one s>0 holds exactly for a
rotated N-clock. Indeed, for N>=2 vanishing of the q sum excludes repeated
phases and forces all pair differences to be integers modulo N. N distinct
points in one coset of Z/NZ fill that coset. The converse follows directly.
This recovers the known floor by a self-contained proof.

## 2. Sharp square-root rigidity for stationary processes

Let Xi be any stationary locally finite counting process on R with
intensity one. Multiplicities and an empty-configuration component are
allowed; ergodicity is not assumed. Suppose its ordered q-energy density
e is finite, meaning that for every bounded interval I,

\[
 \mathbb E\sum_{x\in\Xi\cap I}\sum_{y\in\Xi,\,y\ne x}
                q_s(x-y)=|I|e.                              \tag{4}
\]

Here y!=x excludes the particle itself, not other particles at its location.
For fixed R>=0 define the bounded local semimetric

\[
 d_R(\mu,\nu)=\min\left\{1,
 \sup_{\substack{\mathrm{supp}\,\phi\subset[-R,R]\\
                 \|\phi\|_\infty\le1,\ \mathrm{Lip}\phi\le1}}
          \left|\int\phi\,d(\mu-\nu)\right|\right\}.
\]

Let W_{d_R} be the infimum of its expectation over couplings. Put

\[
 c_s=\frac{4s^3}{\pi^2\sinh^2s(s^2+\pi^2)},\quad
 K=\lceil R\rceil+3,\quad J=2K+1,\quad M_R=J+2,
 \quad C_R=1+16J+4JM_R.
\]

If U is uniform on [0,1), then

\[
 \boxed{\displaystyle
 W_{d_R}(\mathcal L(\Xi),\mathcal L(\mathbb Z+U))
       \le \min\{1,C_R\sqrt{e/c_s}\}.}                     \tag{5}
\]

The exponent 1/2 is optimal already at R=2 uniformly over finite unitary
spectra, as shown in Section 4. The constants are explicit but not optimized.

### 2.1. Stationary gap measure, including multiplicities and empty states

A nonempty stationary locally finite configuration is almost surely
unbounded in both directions. Otherwise its leftmost or rightmost location
would have a nonzero finite translation-invariant subprobability law on R,
which is impossible. At a point of multiplicity r, order its copies by
ranks 1,...,r. This is translation-covariant. Each labelled particle then
has a successor and predecessor, with zero gaps between coincident copies.

Let g^+(x)>=0 be the outgoing gap. Define its intensity-mark law by

\[
 \nu(B)=\mathbb E\sum_{x\in\Xi\cap[0,1)}
                    \mathbf1_{\{g^+(x)\in B\}}.
\]

This is a probability measure since the intensity is one. Stationarity
implies that the joint mean measure of positions and marks is dx nu(dg):
for each mark set the position measure is translation-invariant and is
fixed by its mass on [0,1). Let p_0 be the probability of the empty
configuration. On every nonempty configuration the positive gap intervals
[x,x+g^+(x)) partition R; zero gaps have length zero. Tonelli applied to
coverage of the origin therefore gives

\[
 \int g\,\nu(dg)=1-p_0.                                    \tag{6}
\]

The same coverage calculation for an empty unit interval gives

\[
 \Pr\{\Xi([0,1))=0\}
     =p_0+\int(g-1)_+\,\nu(dg)
     =\int(1-g)_+\,\nu(dg)=:A.                            \tag{7}
\]

Endpoints are null under the mean Lebesgue measure. In particular, using
(6),

\[
 \int|g-1|\,\nu(dg)=2A-p_0\le2A.                         \tag{8}
\]

Incoming and outgoing gap mark laws coincide. For a bounded function h,
the sums of h of those marks over [0,L) differ only at its two boundary
edges, by at most 2||h||_infty. Their expectations equal L times the
respective mark means. Let L tend to infinity to equate the means; bounded
h determine the laws. Nonnegative integrable marks follow by truncation.
This also justifies incoming marks in the coupling below, without any
Palm-measure or ergodicity premise.

For 0<=g<=1 the sine chord bound gives

\[
 \frac{\sin(\pi g)}{\pi g}\ge\frac2\pi(1-g),\qquad
 q_s(g)\ge c_s(1-g)^2.                                    \tag{9}
\]

For g<=1/2 use sin(pi g)>=2g; for g>=1/2 use
sin(pi g)>=2(1-g) and g<=1. Continuous values cover g=0.
The outgoing nearest-neighbor pairs are a subset of the nonnegative
ordered pairs in (4). Thus integral q_s(g) nu(dg)<=e. Since nu has mass one,
Cauchy--Schwarz and (9) prove

\[
 A\le\left(\int(1-g)_+^2\,\nu(dg)\right)^{1/2}
       \le\sqrt{e/c_s}.                                  \tag{10}
\]

### 2.2. Coupling with a uniform-phase clock

Take I=[-K,K+1), of length J. At each particle use both gap deviations:

\[
 D_I=\sum_{x\in\Xi\cap I}
            (|g^-(x)-1|+|g^+(x)-1|).
\]

The equal mark laws and (8) imply

\[
 \mathbb E D_I\le4JA.                                     \tag{11}
\]

Select the leftmost particle Y in [0,1), with a rank tie rule. Let
G be the event that this anchor exists and D_I<=1/4. Equations (7), (11)
and Markov give

\[
 \Pr(G^c)\le A+16JA.                                      \tag{12}
\]

On G no particles in I coincide, since a zero gap there would contribute
one to D_I. Index the bi-infinite particles in increasing order with p_0=Y
and compare them to a_n=Y+n. Telescoping incoming gaps for n<0 and outgoing
gaps for n>0 proves

\[
 |p_n-a_n|\le D_I                                         \tag{13}
\]

for each particle in I and for the first exterior particle on either side.
Every gap in each telescope is marked at an endpoint inside I, including
the last boundary-crossing gap. No gap occurs more than once in one
telescope. Having both incoming and outgoing marks ensures this statement
on both boundaries.

There are no unpaired clock sites in [-R-1,R+2]. Indeed, at the first
right exterior particle p_b one has

\[
 a_b\ge K+1-D_I\ge K+3/4>R+2.
\]

Any larger-index clock site is even farther right. At the first left
exterior particle one has a_b<=-K+D_I<-R-1; smaller-index sites lie
farther left. Conversely, by (13), every actual particle in [-R,R+1]
is paired to a clock site in [-R-1,R+2]. These strict margins handle
supports and the deterministic window boundary.

On G choose the clock Y+Z; off G choose Z. Introduce T uniform on [0,1),
independent of the entire construction, and translate both the process and
the chosen clock by -T. The process law remains Xi by stationarity. The
clock phase is exactly uniform conditional on the original configuration,
whether its chosen initial phase is Y or zero. This produces the required
clock marginal, even on the empty-configuration event.

For every test phi in d_R, the unshifted support lies in
[-R+T,R+T] subset [-R,R+1]. All contributing particles and sites are
covered by (13). If either member of a matched pair contributes, its clock
site lies in [-R+T-D_I,R+T+D_I], of length at most 2R+1/2. It contains at
most M_R=J+2 integer-spaced sites. Global Lipschitz continuity of phi,
including its zero extension outside its support, therefore gives

\[
 d_R(\Xi-T,\mathrm{chosen\ clock}-T)\le M_R D_I\quad\text{on }G.
\]

Off G the distance is at most one. Taking expectations with (11), (12)
proves W_{d_R}<=C_R A and hence (5) by (10). No separate uniform
integrability assumption, minimum spacing or simple-spectrum assumption
was used.

### 2.3. A supplementary local moment bound

Partition a bounded interval I into M cells of length at most 1/4, and put
c_0=min_{|u|<=1/4} q_s(u)>0. For n_I=Xi(I) and the ordered pair energy Q_I
inside I, a deterministic inequality gives

\[
 n_I^2\le M\sum_a n_a^2\le M(n_I+Q_I/c_0),\qquad
 \mathbb E n_I^2\le M|I|(1+e/c_0).                         \tag{14}
\]

Thus bounded e also supplies first-moment UI on bounded windows. Bounded
second moments are not being called second-moment UI; no higher-moment
statement is made.

## 3. Spectral consequence at a single Abel parameter

For the finite spectrum take A uniform on [0,N) and form

\[
 \Xi_N=\sum_{j=1}^N\sum_{\ell\in\mathbb Z}
                  \delta_{x_j+\ell N-A}.
\]

It is stationary with intensity one, and its q-energy density is

\[
 e_N=\frac1N\sum_{j\ne k}\sum_{\ell\in\mathbb Z}
                         q_s(x_j-x_k+\ell N)\le2\delta_N(s). \tag{15}
\]

Other images of the same labelled eigenvalue differ by a nonzero multiple
of N, so contribute zero. Thus (15) holds for every N, even when a test
window is longer than one period, and also when different labels coincide.
Absorbing sqrt(2) into the constant, (5) yields

\[
 W_{d_R}(\mathcal L(\Xi_N),\mathcal L(\mathbb Z+U))
          \le \min\{1,C'_{s,R}\sqrt{\delta_N(s)}\}.           \tag{16}
\]

Consequently delta_N(s_0)->0 at just one fixed s_0>0 forces the local weak
limit to be the uniformly shifted clock. The estimates for every fixed
window, or the count tightness from (14), identify the local vague law.
This is a stability statement for the clock floor, not an implication from
finite equality alone.

## 4. Optimality of the square-root exponent

For any even N and 0<epsilon<1/4 take x_j=j+epsilon(-1)^j, 0<=j<N,
and theta_j=x_j/N modulo one. The unfolded configuration is periodic
with period two; its gaps alternate between 1-2epsilon and 1+2epsilon.
With z=exp(-s), traces vanish unless m=kN/2, and then

\[
 |T_{kN/2}|^2/N^2=[1+(-1)^k\cos(2\pi k\epsilon)]/2.
\]

An exact geometric sum gives, independently of the even N,

\[
 \delta_N(s)=
 \frac{z(1-z)[1-\cos(2\pi\epsilon)]}
      {2(1+z)[1+2z\cos(2\pi\epsilon)+z^2]}
 =\frac{\pi^2z(1-z)}{(1+z)^3}\epsilon^2+O_s(\epsilon^4).       \tag{17}
\]

For every translate mu of this configuration and every target clock Z+t,

\[
 d_2(\mu,\mathbb Z+t)\ge\epsilon.                            \tag{18}
\]

Indeed, [-1,1) contains exactly two consecutive particles, whose fractional
phases have circular distance 2epsilon. At least one is epsilon away from
t modulo one. The function

\[
 \phi_t(x)=\min\{\operatorname{dist}(x,\mathbb Z+t),
                         (2-|x|)_+,1\}
\]

is nonnegative, globally 1-Lipschitz, bounded by one and supported on [-2,2].
It vanishes on the clock and is at least epsilon at that particle in
[-1,1]. It is an admissible test proving (18), including boundary translates.
Every coupling therefore has W_{d_2}>=epsilon. The strictly positive
quadratic coefficient in (17) excludes any uniform bound with exponent
larger than 1/2. This works already at N=2 and along any even N->infinity.

## 5. CUE reference and the precise missing physical input

For Haar CUE, E|T_m|^2=min(m,N). The expected low-mode part of (2) tends to

\[
 I_s=\int_0^1t\widehat H_s(t)\,dt
    =\frac{\sinh(2s)-2s-\tfrac43s^3}{8s^2\sinh^2s}.          \tag{19}
\]

Its expansion starts s/30-s^3/126+19s^5/14175. The total expected excess
tends to the already known positive quantity

\[
 G_s=\frac{1-e^{-2s}}{4s^2}-\frac1{e^{2s}-1}>0.
\]

The complementary geometric reference is

\[
 G_s-I_s=\frac12\int_{\mathbb R}q_s(x)
                    [1-(\sin(\pi x)/(\pi x))^2]\,dx>0.       \tag{20}
\]

For completeness, (20) follows without an exchange of unbounded random
limits. The finite CUE factorial density at difference x is
1-[sin(pi x)/(N sin(pi x/N))]^2, between zero and one. Periodizing q and
unfolding one period rewrites its mean pair defect as one half the integral of q
times this density. Dominated convergence applies since q is integrable;
its pointwise limit is the integrand in (20). Formula (19) follows by an
ordinary Riemann sum. These arguments use the established finite CUE
kernel, not any statement about the frozen physical family.

Formula (2) offers a sufficient route to the physical Abel pair statistic at that s by proving
convergence of its two nonnegative components to I_s and G_s-I_s. It does
not prove either convergence, and the total pair limit alone need not give
the two separate limits. All-order TRACE-005 requires additional information.
In particular, forcing delta_N(s)->0 would prove the clock law, which differs
from the positive CUE excess required by the maintained BGS target.

## 6. Review, sources and finite checks

The [independent internal reconstruction](../archive/record/reviews/abel_rigidity_20261016.md)
checks the transform, labelled diagonal, N=1, count hypotheses and coupling.
The elementary proof is self-contained; the CUE reference uses the standard
kernel and trace second moment already used in `BGS-CUE-002`.
[Source and priority audit](../literature/abel_gaussian_sources_20261016.md).

The [finite verifier](../computations/verification/research_20261016/verify_abel.py)
checks the Fourier convolution and two independent finite energy evaluations
on clocks, repeated phases, perturbed clocks and rational spectra. Actual
commands, precision, source hashes and output are in the
[execution record](../evidence/executions/20261016/abel-gaussian/README.md).
Wolfram source and its returned residuals are saved beside the verifier and
execution record. These checks supplement the proof; they do not certify
the universal quantifiers in (2), (5) or (16).
