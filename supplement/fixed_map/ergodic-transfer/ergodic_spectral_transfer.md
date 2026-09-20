# Ergodic control of microscopic spectral displacement

Internal derivation and adversarial self-review, 18 September 2026.
Base: e0ada2e2c44dfe10bebf928dc8a1d6526ae15cb7. No priority claim or
Lean certification. This is a comparison theorem, not a proof of BGS for
either member of a comparison pair.

## 1. A finite-dimensional estimate

Let U be N-dimensional unitary, A=A* with Tr(A)=0 and ||A||op<=C, and put

    U_s=exp(i s A/N) U,  0<=s<=1,
    A_T=(1/T) sum_(r=0)^(T-1) U^(-r) A U^r,
    v_N(T)=||A_T||_2,       ||B||_2^2=Tr(B*B)/N.

There is a matching, with multiplicities, between the spectra of U and
U_1 with continuous phase lifts theta_j(s), in cycles, such that the
unfolded displacements d_j=N(theta_j(1)-theta_j(0)) satisfy

    max_j |d_j| <= C/(2 pi),                              (1)
    [(1/N) sum_j d_j^2]^(1/2)
       <= [v_N(T)+C^2(T-1)/N]/(2 pi)                     (2)

for every positive integer T. There is no spectral gap or simplicity
hypothesis. If A is not traceless, replace it by A-(Tr A/N)I and rotate
the final spectrum by the corresponding scalar phase.

Proof. The unitary path is real analytic. Local Cayley transforms reduce
its eigenangle branches to real-analytic Hermitian perturbation theory.
At almost every s, including a choice diagonalizing the generator inside
a multiple eigenspace, their derivatives have the form

    2 pi N theta'_j(s)=<v_j(s),A v_j(s)>.

This immediately gives (1). Let A_(T,s) be the same time average with U_s.
Every diagonal expectation in an eigenbasis of U_s is unchanged by time
averaging. Cauchy--Schwarz in that basis gives

    (1/N) sum_j |<v_j(s),A v_j(s)>|^2 <= ||A_(T,s)||_2^2. (3)

Telescoping powers of two unitaries and ||U_s-U||op<=C/N give

    ||U_s^r-U^r||op<=r C/N,
    ||U_s^(-r) A U_s^r-U^(-r) A U^r||op<=2r C^2/N.

Thus ||A_(T,s)-A_T||_2<=C^2(T-1)/N, uniformly in s. Apply this in (3),
integrate the angle velocities, and use Cauchy--Schwarz in s. This proves
(2). It controls the whole path; quantum ergodicity only at s=0 would
not, by itself, justify integrating a velocity estimate. QED.

## 2. Consequence of classical ergodicity

For a sequence (U_N,A_N), suppose C is uniform and

    lim_(T->infinity) limsup_(N->infinity) v_N(T)=0.      (4)

Then (2) implies that the matched unfolded RMS displacement tends to zero.
The maximum displacement need only stay bounded; it need not tend to zero.

Condition (4) follows from standard fixed-time quantization assumptions:
U_N quantizes an ergodic probability-preserving F, A_N quantizes a fixed
real mean-zero observable a, fixed-time Egorov holds, and normalized traces
of products converge to classical integrals. Indeed, for each fixed T,

    v_N(T)^2 -> integral |(1/T) sum_(r=0)^(T-1) a o F^r|^2.

The mean ergodic theorem makes the right side tend to zero. The inverse
map convention is immaterial to ergodicity but must be used consistently.
Centering by the exact quantum trace instead of the limiting integral
changes this fixed-time limit by o(1).

A quantitative version needs an explicit further assumption. If

    v_N(floor(c log N))=O((log N)^(-1/2))              (5)

for some c>0, then the RMS displacement is O((log N)^(-1/2)). One sufficient
way to obtain (5) is a uniform logarithmic-time correlation estimate
|N^-1 Tr(A_N U_N^-m A_N U_N^m)-int a(a o F^m)|<=C N^-eta
for |m|<=c log N, together with summable classical correlations. Expanding
v_N(T)^2 as a triangularly weighted correlation sum proves (5).

The time-averaging method and logarithmic quantum-ergodicity bounds have
established antecedents. [Schubert, Section 4, Theorem 4 and equations
(65)--(70)](https://arxiv.org/abs/math-ph/0503045) treats smooth Hamiltonian
perturbations of cat maps and bounds the eigenfunction variance by C/log N.
That is not a microscopic spectral-statistics theorem. Our finite estimate
(2) is proved above rather than imported from that paper. No identification
of the upload's inconsistent conventions with its hypotheses is presumed.

## 3. Deterministic transfer of local statistics

Let x_j=N theta_j be a spectrum on a circle of length N. Let a second
spectrum have matched lifts x_j+d_j, where

    |d_j|<=D,   q_N^2=(1/N) sum_j d_j^2 -> 0.          (6)

Write C_(k,N) for the anchored factorial statistics in
`mathematics/trace_to_local_statistics_bridge.md`. For k>=2 and a compactly
supported C^1 test phi, fix R containing its support and define

    n_j(L)=#{ell: dist_(R/NZ)(x_ell,x_j)<=L},
    M_p(L)=(1/N) sum_j n_j(L)^p,
    L=2(R+2D).

For all sufficiently large N the following finite bound holds:

    |C_(k,N)(x+d;phi)-C_(k,N)(x;phi)|
                      <= C_(k,phi) q_N M_(2k-2)(L)^(1/2). (7)

Proof. A term whose interpolation encounters the support of a derivative
of phi has all original labels within R+2D of its anchor. Relative to any
chosen one of these k labels all are within L. The mean-value theorem,
followed by summing with that chosen label fixed, gives the bound

    (C_(k,phi)/N) sum_j |d_j| n_j(L)^(k-1).

Cauchy--Schwarz proves (7). Periodization causes no extra factor: once
N>2(R+2D), each supported coordinate has at most one relevant lift. The
argument allows repeated eigenvalues but always uses distinct eigenvalue
labels in the factorial statistic. QED.

Bounded reference statistics through order 2k-1 imply bounded M_(2k-2)(L).
For example, with p=2k-2, the integer inequality
n^p<=C_p[1+(n-1)_p] expresses this directly using anchored p-tuples of
distinct neighbors. Smooth compactly supported majorants of their boxes
give the required correlation bound. Hence (7) tends to zero.

One extra moment order suffices if a rate is not needed. Holder gives

    error <= C [N^-1 sum |d_j|^k]^(1/k) M_k(L)^((k-1)/k)
          <= C D^(1-2/k) q_N^(2/k) M_k(L)^((k-1)/k),    (8)

and M_k is bounded by the reference (k+1)-point local bound. For k=2
interpret D^0 as 1, including the trivial D=0 case.

If reference correlations of every fixed order are bounded on positive
Schwartz tests, the perturbed correlations have the same boundedness:
every local target tuple is contained in an enlarged reference box.
The translated-box occupation bound already proved in
`mathematics/bandlimited_correlation_extension.md` then gives uniform
Schwartz tails. Compact-test convergence extends to every Schwartz test.

Consequently, if an ergodic quantization U_N has all fixed-k microscopic
limits, then exp(i A_N/N)U_N has the SAME limits for any fixed smooth
observable A_N satisfying the stated quantization assumptions. Scalar
rotations do not affect these statistics. With (5) and reference bounds
through 2k-1, the compact-test difference is O((log N)^(-1/2)).

This includes operator differences of order 1/N, whereas arbitrary such
differences do not preserve local statistics. It does not assert invariance
under arbitrary quantizations of the same classical map: for example a
factor exp(i Op(a)) is not the factor exp(i Op(a)/N) treated here. In
particular the word 'subprincipal' would be ambiguous without the explicit
operator scale, so it is not used as a substitute for this hypothesis.

## 4. Local point processes need no higher-moment hypothesis

Couple the two spectra by the same uniform circle origin, after removing
any common scalar rotation. If Xi_N and Xi'_N are their lifted local point
processes, then for phi in C_c^1(R),

    E |<Xi'_N-Xi_N,phi>| <= ||phi'||_1 (1/N)sum |d_j|
                         <= ||phi'||_1 q_N.             (9)

This follows by integrating |phi(y+d_j)-phi(y)| over y before summing j.
A countable determining collection of such tests shows that the distance
of the coupled point measures tends to zero in probability in the vague
topology. Thus their point-process limits agree whenever one exists.
Unlike correlation expectations, this assertion needs no higher moments.

## 5. Three exact failure controls

Small operator norm without ergodicity is insufficient. For even N take
the diagonal clock U_N and A_N=2 pi a diag((-1)^j), 0<a<1/4. Then A_N
commutes with U_N, v_N(T)=2 pi a for every T, and the unfolded shifts
are exactly (-1)^j a. The pair statistic near spacing 1 changes by one,
as in the existing clock counterexample. Condition (4) fails.

Small average displacement with only bounded pair statistics is also
insufficient. Set N=m^2 with m even. Put m labels at 0 and the remaining
N-m labels at uniformly spaced positions in [10,N-10] on the unfolded
circle. Move half of the cluster to a and half to -a, with 0<a<1/4.
Choose a smooth pair test supported in (-a,a) and equal to 1 at zero.
All background and cross-cluster contributions vanish for large m. The
two pair statistics are exactly

    1-1/m,     1/2-1/m.

Yet q_N=a/sqrt(m)->0 and max |d_j|=a. The reference pair statistics on
every compact test remain bounded, while the anchored third local moment
diverges like m. This verifies that the moment condition in (7)/(8)
cannot simply be discarded. The example is not an ergodic quantization.

Even zero diagonal variance at the INITIAL operator alone is insufficient.
For even N, take N/2 two-dimensional blocks

    U_(j,N)=exp(4 pi i j/N) diag(exp(i pi/N),exp(-i pi/N)),
    A_(j,N)=[[0,1],[1,0]],       0<=j<N/2.

The initial spectrum is a rotated clock and every diagonal expectation of
A_N in its (simple) eigenbasis is exactly zero. But the block phases after
the perturbation exp(i A_N/N) are the centre plus or minus

    b_N=arccos(cos(1/N) cos(pi/N)).

Their unfolded displacements have absolute value

    d_N=[N b_N-pi]/(2 pi)
        -> [sqrt(pi^2+1)-pi]/(2 pi)>0.                 (11)

The alternating spacings therefore change by a nonzero amount. Directly,

    v_N(T)=|sin(T pi/N)/(T sin(pi/N))| -> 1

for each fixed T. Thus (4) fails although the endpoint diagonal variance
is zero for every N. At an intermediate path parameter s>0 the diagonal
variance tends to s^2/(pi^2+s^2), not zero. This is why the proof controls
the full perturbation path via time averages rather than silently reusing
an endpoint eigenbasis. The example is not a fixed smooth-observable
quantization of an ergodic map.

## 6. The logarithmic displacement rate is attained on Pell dimensions

Let M_N be the Pell cat quantization and let A_N be the centred frozen
finite symbol, in the explicit T(l,k) position convention of the preceding
checkpoint. For every odd K>=39, its exact period average obeys

    ||Abar_N||_2^2=sigma^2/K,
    sigma^2=1650797/4000000.

Set V_N=exp(i A_N/N) M_N. Let W_(2,N) denote the optimal RMS matching
distance between spectra, using unfolded circular distance N/(2 pi)
times angular distance. The proved finite-symbol normal form gives

    |W_(2,N)(V_N,M_N)-sigma/(2 pi sqrt(K))|
                    <= (17 pi F1^2)/(4 N sqrt(K)).       (10)

For sufficiently large K the derivation is as follows. The normal form at
epsilon=1/N conjugates V_N to B_N=exp(i Abar_N/N)M_N with normalized HS
error <=17 pi F1^2/(N^2 sqrt(K)). Since Abar_N commutes with M_N, B_N
shifts each cat cluster by its block eigenvalues divided by N. The blocks
remain closer to their own root than to any other root, since
||Abar_N||op/N <=F0/N < pi/K. Matching within each block is therefore
optimal and gives exactly sigma/(2 pi sqrt(K)).

For two unitaries B,D, take a Hermitian logarithm H of BD*, with eigenvalues
in [-pi,pi]. Then ||H||_2<=(pi/2)||B-D||_2. Integrating eigenangle velocities
along exp(i s H)D, exactly as in Section 1, bounds unfolded RMS matching
distance by N||H||_2/(2 pi), hence by N||B-D||_2/4. Apply this bound and the
triangle inequality for W_(2,N) to obtain (10). This supplies the needed
matching estimate directly; degeneracies do not affect the argument.

Thus the logarithmic rate cannot be replaced by a universal power of 1/N
under the present ergodicity assumptions. The cat reference fails the
bounded microscopic-correlation hypotheses; (10) supplies a sharpness
example for displacement, not CUE statistics.

## 7. Relevance and remaining gap

The result is usable if two already constructed UNITARY quantizations can
be compared, up to scalar rotation and unitary conjugation, as

    V_N=exp(i Op_N(a)/N) U_N + o(1/N) in operator norm,

with a fixed smooth real symbol and fixed-time ergodic correspondence.
The existing maximum-displacement theorem handles the final o(1/N) term.
An all-k reference law would then transfer. No such reference law or
comparison with the natural prequantum operator has been proved here.

In particular an unspecified O(N^-delta) comparison, a nonunitary reference,
or a rough N-dependent logarithm cannot be inserted into this statement.
The earlier O(N^-delta) natural-quantization estimate remains insufficient
on the evidence presently available. A fresh check of [Faure--Tsujii,
Theorem 1.69, equation (1.75)](https://arxiv.org/abs/1206.0282) gives only
some delta>0 and a corrected continuous potential. Theorem 1.37 states
concentration of the outer spectrum near the unit circle, which does not
assert exact unitarity. Neither statement supplies the hypotheses above.
An all-time trace formula still requires control of its oscillatory orbit
sum before it becomes a CUE law.

The result also does not repair the upload's modular-versus-ordinary
midpoint or metaplectic orientation mismatch: those changes have not been
shown to be smooth operator corrections of size 1/N. The principal
fixed-map BGS problem and its Heisenberg-time coherent estimate remain open.
