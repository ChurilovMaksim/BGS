# Fixed-map clustering and a frame identity for the remaining resolvent

Unpublished checkpoint, 2026-09-17. Base:
e0ada2e2c44dfe10bebf928dc8a1d6526ae15cb7, continuing
`build/coherent-return/research_checkpoint.md`. No Git commit or push.
The fixed-coupling Heisenberg cancellation problem remains open.
The arguments below are self-reviewed; no priority claim is made.

## 1. A quantitative statement for the prescribed fixed map

Let S=[[3,4],[2,3]], let M_N be the prescribed modular metaplectic
quantization, and put

    U_N=exp(i tau N A_N) M_N,       tau=10^(-80).

A_N is the Weyl quantization of the given real symbol f. The result
does not assume that A_N or U_N has simple spectrum. It survives the
ordinary/modular Weyl gauge repair, reversal of the cat matrix, and
reversal of the two operator factors: the norm estimate and projective
period used below survive these changes.

### Uniform kick norm

Write x=2 pi q, y=2 pi p and r=(1-cos 7x)(1+cos x). Exactly

    cos 7x+r/10 = 1/10+cos x/10-cos 6x/20
                 +9 cos 7x/10-cos 8x/20,
    r sin x = sin x+sin 2x/2+sin 5x/4+sin 6x/2
              -sin 8x/2-sin 9x/4.

The Fourier l1 norms of these two displayed functions are respectively
6/5 and 3. Also ||r cos(y-alpha)||_(Fourier l1)=4. Since each Weyl
operator is unitary,

    ||A_N|| <= 6/5+3/100+4/100 = C := 127/100.                 (1)

This deliberately uses an upper bound rather than identifying the exact
operator norm. Define delta=C tau N and eta=N delta. For delta<pi,

    ||U_N-M_N|| <= 2 sin(delta/2) <= delta.                     (2)

### Arithmetic period and spectral inclusion

For any odd K let N+F sqrt(2)=(1+sqrt(2))^K. Then
N^2-2 F^2=-1, N is odd, and

    S^K = [[N^2+2F^2,4NF],[2NF,N^2+2F^2]] = I mod N.

Covariance implies that M_N^K commutes with both the cyclic shift and
the diagonal clock matrix, hence M_N^K=zeta I. Its spectrum lies at
at most K equally spaced points of the circle. The spectral inclusion
for a normal matrix, followed by (2), puts all eigenvalues of U_N in
the K arcs of angular radius delta around these points. This is a
finite-dimensional statement with no stationary-phase remainder.

Define the factorial local pair mass

    B_N=(1/N) #{(j,k): j!=k,
                    circle_distance(theta_j,theta_k)<=2 pi/N}.

It counts ordered labels and keeps repeated eigenvalues. If eta<=pi,
all pairs within an individual arc are counted. Cauchy–Schwarz gives

    B_N >= N/K-1.                                            (3)

For wider arcs, divide each arc into bins of angular length <=2 pi/N.
Their total number is at most

    K ceil(eta/pi) <= K(1+eta/pi) <= K(1+eta/3).

Assign each eigenvalue to one containing arc and bin. Overlapping arcs
do not hurt this construction. If bin populations are n_b, then
sum n_b=N and sum n_b(n_b-1)>=N^2/(number of bins)-N. Therefore

    B_N >= N/[K(1+eta/3)]-1.                                 (4)

This bound remains useful long after individual clusters are wider
than one mean spacing. It is stronger in range than a bound based
only on microscopic stability of individual eigenvalues.

### Two exact finite certificates

At K=105,

    N=7769927470067109254612252866121474934193,
    eta<0.767,          B_N>7.3999*10^37.                      (5)

At K=203,

    N=252600454664614554703519770255050826534615034647211566192959636252856146870839,
    delta<0.003209,     B_N>3.606672814731669.                 (6)

At K=201 the dimension is approximately 4.33394*10^76 and B_N>26.1168.
All large integer arithmetic and rational inequalities are checked in
`frozen_crossover.py`, independently repeated in `exact_checks.wl`.
No matrix of these enormous dimensions was numerically diagonalized.

For comparison the CUE limiting density is
1-(sin(pi x)/(pi x))^2, so its integral on [-1,1] is less than 2.
The discrepancy can also be stated with an admissible fixed smooth test:
choose 0<=h<=1, h=1 on [-1,1], supported in [-5/4,5/4]. Its CUE
integral is <=5/2, whereas at (6) the actual factorial statistic is
>3.60667. Thus its error exceeds 1 at that dimension.

This is NOT an asymptotic counterexample to BGS at the fixed tau.
Only finitely many Pell dimensions meet each small-kick condition.
It establishes a very late necessary onset along the specified sequence.

The positive position transition matrix can nevertheless mix rapidly.
Since a_N is a compression of Ad_(U_N), and |(M_N)_xy|^2=1/N,

    ||a_N-J|| <= 2 delta.                                    (7)

At (6) its singular-value gap is >0.99358 despite (6). This is a
statement about the unistochastic matrix, not an identification of its
gap with the classical Anosov mixing rate.

### Nonuniformity as the classical coupling tends to zero

The same calculation permits variable tau>0. Let L=log(1/tau),
beta=1+sqrt(2), a=log(beta)/(4C), and choose the largest odd Pell
index with N<=a/(tau L). Consecutive odd-index Pell N's have ratio
less than 6, so N>a/(6 tau L). For sufficiently small tau,
K<=L/log(beta), hence K delta<=1/4 and K/N<=1/12.
Equation (4) then gives B_N>=5.

Consequently any onset N_*(tau) after which the above fixed smooth
pair statistic is always within 1 of its CUE value must satisfy

    N_*(tau) >= c/[tau log(1/tau)]                            (8)

for all sufficiently small tau, with an absolute positive c depending
on the fixed symbol bound. If convergence never occurs, N_* is infinite
and the statement is still valid. This is a necessary lower bound,
not a predicted transition scale or an upper bound on the onset.

## 2. Removing the eigenvector-overlap hypothesis exactly

Let A=Ad_U, L_U=2I-A-A^*, s>0, a=s/N, and choose 0<r<1 by
(1-r)^2/r=a^2. Define, for arbitrary unitary U including multiplicities,

    S_N(s)=N^(-3) sum_(j!=k) [a^2+|e^(i theta_j)-e^(i theta_k)|^2]^(-1)
          =N^(-3){Tr(a^2+L_U)^(-1)-N/a^2}.                  (9)

This is the regularized pair energy itself, with no unknown eigenvector
weights. It directly gives

    pair_mass([-R,R]) <= (s^2+4 pi^2 R^2) S_N(s).            (10)

Complete mutually unbiased bases furnish an orthogonal decomposition of
traceless Hilbert–Schmidt matrices. For their diagonal projections P_b,

    sum_b P_b=I+N Pi_scalar,
    sum_b sum_x |<b_x,U^m b_x>|^2=N+|Tr U^m|^2.             (11)

This is a known 2-design property, not a new claim:
[Klappenecker–Rötteler, Theorem 3 and Remark 2](https://arxiv.org/abs/quant-ph/0502031).
Complete MUBs are not assumed to exist in every dimension.

An explicit weighted design works in every dimension instead. Give the
N coordinate vectors total weight 1/(N+1), equally divided. Give all
3^N flat vectors psi_x=omega^(a_x)/sqrt(N), a_x in {0,1,2}, total
weight N/(N+1), equally divided. Independent cube-root phase averaging
gives

    E |psi psi><psi psi| = (I+Swap)/[N(N+1)].                (12)

Indeed the flat-vector fourth moment retains the two equal-multiset
contractions, but counts the all-equal diagonal only once. The coordinate
part supplies precisely that missing diagonal term. This proves (12)
directly; it is a finite weighted identity, not randomization of U.
The exponential number of probes makes this a theoretical identity,
not a proposed efficient algorithm.

Let rho_psi=|psi><psi|, viewed as a unit Hilbert–Schmidt vector, and
C_psi(z)=<rho_psi,(I-zA)^(-1)rho_psi>. The scalar first-return function
F_psi satisfies C_psi=(1-F_psi)^(-1) inside the disk. Formula (12) gives

    E C_psi(z)=[Tr(I-zA)^(-1)+N/(1-z)]/[N(N+1)],
    S_N(s)=N^(-3){N(N+1)[2 Re E C_psi(r)-1]/(r^(-1)-r)
                  -2N/a^2}.                               (13)

Thus the previous additional lower bound on eigenvector overlaps can be
removed. No bound on the right side for the fixed map has been obtained.

If U has multiplicities m_lambda, let M=sum m_lambda^2. Deleting the
ENTIRE invariant subspace in (9) instead of subtracting N/a^2 would
erase the genuine factorial contribution

    (M-N)/(s^2 N).                                         (14)

Our preceding simple-spectrum return formulas were explicitly conditional
on simplicity; (13) avoids that prerequisite. One must not use full
commutant subtraction to conceal unproved simplicity or real degeneracies.

## 3. Why two attempted closures do not supply the missing bound

For MUB projections onto traceless diagonal subspaces define
K_ab=||P_a Ad_U P_b||_HS^2/(N-1). It is doubly stochastic, but in
general K(U^2) != K(U)^2. Already for a qubit,

    U=(sigma_x+sigma_y+sigma_z)/sqrt(3),     U^2=I,
    Ad_U on Pauli axes = 2*ones(3,3)/3-I,
    K diagonal=1/9, off-diagonal=4/9,
    spectrum(K)={1,-1/3,-1/3}.

All three complementary channels mix under the positive model, while
the true quantum evolution returns exactly after two steps. This is an
exact counterexample to Markov closure, not a fixed-map BGS counterexample.
Finite checks at prime N=5,11,23,43 with conjugated involutions and
simple-spectrum perturbations give large one-step gaps and order-one
two-step defects. They do not prove a uniform asymptotic gap theorem.

The noisy-propagator literature also does not fill the closed-system gap.
[Nonnenmacher, Theorem 1](https://arxiv.org/abs/nlin/0301014) fixes nonzero
noise before taking N to infinity; the paper discusses noncommuting limits.
An elementary obstruction to direct operator-norm transfer is that if
||T-Ad_U||<=delta, every eigenvalue of T is within delta of the unit
circle. A spectral gap bounded below independently of N cannot arise
from an operator-norm perturbation tending to zero. This only rules out
that transfer mechanism; it does not rule out a more delicate trace argument.

## 4. Checks, remaining target, and a possible next route

`design_return.py`: MUB frame and trace identities, the cat permutation
control, and non-Markovian counterexamples. `all_dimensions.py`: the
explicit weighted design at N=2,4,6, both simple and degenerate spectra;
(13) errors below 3e-14, with (14) checked separately. `exact_checks.wl`
also verifies the trigonometric decompositions and the qubit counterexample.

The main missing input remains a coherent fixed-map estimate for (13),
or the earlier small Wiener-insertion representation, at r=1-O(1/N).
Equation (8) demonstrates that constants uniform in arbitrarily small
coupling cannot be obtained from classical hyperbolicity bounds alone.
Beyond the occupied-arc regime, no proof of pair tightness or the CUE law
has been obtained in this iteration.

The finite-symbol Floquet extension has now been proved in
`finite_symbol_normal_form.md`: its one-step normalized HS error is at
most 17 pi F1^2 epsilon^2/sqrt(K), initially for prime K. The proof retains
Weyl-translation orthogonality in the commutator and uses two unitary
Duhamel comparisons. Finite tests check a non-even two-dimensional symbol.
Its small-quantum-kick regime still does not cover fixed tau as N->infinity.
This is an internal proof, not independent external review or formalization.

## 5. Continuation, 18 September 2026

Base remains local revision e0ada2e2c44dfe10bebf928dc8a1d6526ae15cb7.
No tracked edits, commit or push were made. The main fixed-map Heisenberg
barrier and all-k BGS remain open.

Three executed advances/checks:

1. `sparse_orbit_theorem.md` proves the exact fixed submodules of S^d
   modulo N_K and a lower bound on the orbit length of a q-term Weyl label.
   For the frozen Fourier support this removes the prime-index hypothesis
   at every odd K>=39. Explicit p-term examples, with p the least prime
   divisor of K, demonstrate actual shorter orbits at the first possible
   arity; the theorem is not silently extended to arbitrary word lengths.
2. `fixed_coupling_barrier.md` proves a necessary onset lower bound
   N_*(tau)>=c_f/[tau sqrt(log(1/tau))], conditional only on such an
   eventual CUE approximation threshold existing. It improves this
   checkpoint's earlier 1/[tau log(1/tau)] lower bound. It is a tau->0
   family statement, not a fixed-tau BGS counterexample.
   Rational certificates for the actual tau=10^-80, now using the exact
   variance 1650797/4000000 and saturated commutators, give B_N>1332.17,
   226.23, 37.42 and 5.15 at K=199,201,203,205 respectively. The largest
   dimension is 1472263341690459751560022662071732344879659802345870466465594433532459189239641.
3. The same note proves that a fixed-classical-strength one-harmonic kick
   cannot be approximated in normalized HS norm by O(log N) Fourier modes
   or by a polynomial of that degree: the best error tends to 1. An FFT
   check reaches N=1048575, epsilon=41943, a genuinely different regime
   from the earlier small-epsilon tests. This falsifies a specific proposed
   truncation route; it does not exclude nonlinear-phase resummation.

Verification: 348 integer divisor identities; 1,009,120 nonzero label-pair
cases; 40,000 radius-nine stress cases; sharp shorter-orbit examples;
independent Fourier/Jacobi assembly and Duhamel checks at N=41,239 in both
midpoint conventions; a separate Wolfram exact variance computation;
rational large-N certificates; and FFT/Bessel comparisons for the failed
bandwidth route. Sources and outputs are distinct from the analytic proofs.

The next required input is genuinely nonperturbative in epsilon=tau N:
control the coherent long-time evolution without a small-epsilon remainder
or a short Fourier/word truncation. Neither the orbit lemma nor the noisy,
positive-Markov or prequantum reformulations audited above supplies it.

## 6. Further continuation: ergodic spectral comparison

`../ergodic-transfer/ergodic_spectral_transfer.md` proves a different
comparison mechanism. For V_N=exp(i A_N/N)U_N, bounded centred A_N and
vanishing iterated time-average HS norm, matched unfolded eigenphase
displacements tend to zero in mean square. Fixed-time ergodic quantization
assumptions imply this time-average condition. With explicit logarithmic
correlation control the rate is O(1/sqrt(log N)). Local all-k limits
transfer when the reference higher local moments are bounded; point-process
limits transfer without that moment assumption.

This improves the previous o(1/N) operator comparison criterion for a
structured class of O(1/N) corrections. An exact Pell example attains the
logarithmic displacement scale. Three failure controls check the necessity
of ergodic time averages, path uniformity and moment control. Finite checks
and the separate self-review are in `../ergodic-transfer/`.

The proposed application to natural quantization remains blocked: a fresh
primary-source check supplies neither a unitary reference with a known CUE
law nor the required smooth 1/N comparison. The new theorem cannot compare
the cat map directly to the finite classical-strength kick, whose quantum
exponent grows as tau N. Main BGS status is unchanged; no git publication.

## 7. Continuation, 19 September 2026: external reports and corrected target

The two new uploaded research summaries were audited in
`../report-audit-20260919/audit.md`, with full source hashes in that
directory's checkpoint. The original fixed-map target and the publication
condition remain unchanged. No tracked edit, commit or push was made.

Two spectral implications in the reports fail: unitarity plus resonance
sparsity gives O(N/rho), not O(1/rho), and unsubtracted connected CUE trace
products need not vanish at Heisenberg scale. An exact cubic reference
equals N-(N-a)_+-(N-b)_++(N-a-b)_+. Its smooth normalized test tends to
1/2 in L2, with variance O(1/N). An exact variance formula, a 48-chamber
rational certificate and an independent cyclic-partition verifier are
retained. These are reference calculations, not a deterministic BGS law.

The report's f_star classical quartic algebra, explicit hyperbolicity
bound and non-C1 affine-conjugacy obstruction were reconstructed; the
classical topological classification input was checked in Newhouse (1970).
The broad finite-dimensional symmetry conclusion needs geometric scope.
The proposed reduced quartic obstruction is not defined in the summaries,
and its necessity for BGS is not supplied. A finite-N Weyl quartic
coefficient differs from its classical counterpart. The claimed exclusion
of f_star is therefore not accepted.

For any fixed hyperbolic S, rho_N >= 2 acosh(N/2)/log(lambda) holds for
every N>=3, strengthening the report's density-one period growth.
Actual resonant suppression still requires a monodromy return estimate.
An exact Fejer-energy criterion and a sufficient discrepancy condition
are proved in `resonant_normalization.md`.

Auxiliary f_star experiments at fixed kappa=0.0001 and 0.0004 reached
N=1393, with conventions checked before execution. Arithmetic return
energy falls substantially and is close to its CUE mean at the largest
dimension. The cubic values were calibrated against exact finite CUE
variance. These are finite diagnostics of another candidate, not the
frozen tau=10^-80 map and not an asymptotic result.

## 8. Continued attempt: local bounds do not supply return suppression

`../report-audit-20260919/folded_spectrum_control.md` proves a stronger
negative control for the repaired resonance route. Explicit simple
spectra have uniformly bounded local correlations at every fixed order,
macroscopic equidistribution and exponentially small traces below a
logarithmic resonant stride. Their Heisenberg-window return energy still
tends to 1/sqrt(1-alpha^2)-1>0. The proof controls Fourier-grid aliases by
a contour estimate, not by a finite-order expansion. Tests through
N=47321 corroborate the formulas.

This eliminates a closure based only on those spectral inputs. It does
not construct a counterexample in the prescribed smooth quantization
class. The next actual proof obligation remains a dynamical estimate of
the coherent, CUE-subtracted trace sums or folded monodromy energy at
fixed nonzero classical coupling. The original main barrier remains open.

## 9. Continued fixed-model attempt: exact algebraic nonreturn

`../algebraic-return/exact_return_theorem.md` proves, using the checked
Lindemann--Weierstrass theorem, that for the original raw frozen model at
tau=10^-80, every odd N>=3 except N=7 has no scalar quantum return at any
positive integer time. More strongly, no positive power is a scalar
multiple of an algebraic-entry matrix. At least one eigenvalue ratio is
transcendental. The statement holds at every nonzero real algebraic tau.

The input is not an asymptotic approximation: an S-orbit functional on
the exact Weyl expansion has real value at least 169/500. It proves the
cat-period average of the frozen A is nonscalar for all these N, including
composite moduli and modular aliases. N=7 is a genuine raw exception:
A_7=I and M_7^3 is scalar. Gauge signs must be applied to integer labels
before reducing them modulo N.

A separate specialization criterion reduces simplicity at every nonzero
algebraic exponent to simple first-order splitting of the cat blocks.
Exact finite-field certificates establish this for raw N=3,5,9,15,21,41,
239,1393 and ordinary-midpoint N=7,41. Independent Python and C++ replay
checks the rational-resolvent certificate, squarefree characteristic
polynomial and Weyl covariance; corrupted input is rejected. This is
finite certified simplicity, not an all-N simplicity theorem.

The analytic implications received a separate internal audit. No Lean
execution or external refereeing is asserted. All programs, certificates,
scope controls and hashes are under `../algebraic-return/`. The earlier
weak-kick Gaussian route was checked for relevance and already covered
by maintained results; it was not relabelled as new progress.

The new theorem removes exact arithmetic returns for the actual frozen
model but provides no rate of suppression of approximate returns. Even
simple spectra with every distinct eigenvalue ratio transcendental can
have diverging local pair mass, as an explicit rational-generator control
shows. The Heisenberg-time quantitative barrier and the full BGS target
remain open. No tracked change, commit or push has been made.

The subsequent quantitative continuation is in
`../algebraic-return/quantitative_split.md`. Cyclicity of a finite-field
reduction already implies simplicity of a normal characteristic-zero
lift, even without squarefreeness of the reduced polynomial. No uniform
cyclicity proof for the frozen matrices was obtained. A separate exact
example shows that simple A plus nonscalar E_M(A) is insufficient.

A self-contained discriminant-norm argument supplies explicit lower
bounds for the certified first-order block gaps. A Schur-complement
argument then gives min_gap(exp(i epsilon A)M)>=|epsilon| delta/3 when
|epsilon|<=g delta/(18 C^2). Exact evaluation shows the conservative
bound covers the frozen exponent only at N=3 among the recorded cases;
it becomes far too weak at larger N. Effective Lindemann--Weierstrass
literature was checked, but no uniform microscopic estimate was imported
or proved. This quantitative extension is self-reviewed, separately from
the earlier internally reviewed qualitative theorem.

## 10. Actual cat blocks: uniform one-step mixing does not close memory

`../block-memory/block_memory_theorem.md` proves a uniform Doeblin bound
for the prescribed frozen symbol on prime Pell periods K>=13. For
0<|epsilon|<=1/10, the exact block transition matrix satisfies
T_rs>=epsilon^2 pi_r/300. It represents repeated block measurement
**and maximally mixed repreparation**. Its mixing bound is not a bound
for the closed propagator.

If K|epsilon|(593/500)<=1/4, the actual unmeasured map retains at least
1-4K^2 epsilon^2(593/500)^2 of every initial cat-block population at
every integer time. The proof uses nearby invariant spectral projectors;
the bound does not accumulate with time. With epsilon=N^-a, 0<a<1/2,
the TV discrepancy from the iterated Markov chain tends to one uniformly
on and beyond Heisenberg windows. This asymptotic has shrinking classical
coupling; it is not a fixed-tau BGS counterexample.

At the actual tau=10^-80 and prime K=199, an exact rational certificate
gives closed block retention >0.9987680352 for all times, while the
Markov approximation differs by TV>0.9937 for all m>=N. The certified N
is about 7.43586e75. This is one finite instance, not a giant simulation.
Dense checks at N=41,239 corroborate the charge, edge, projector and
transition identities; their epsilon=0.03 is explicitly auxiliary.

`../block-memory/abel_memory_bound.md` quantitatively applies the earlier
Schur memory identity to these cat blocks. In ordinary Hilbert--Schmidt
normalization the invariant compression is >=cI, c=(1-2rho^2)^2,
rho=K|epsilon|593/500. Hence
||z^2 K(z)-(I-F)||<=(1-z)(1+c^-1). At z=1-1/N this prevents the total
Abel memory from being a smaller-order correction to the Markov drift
in the stated regime. The identity at z=1 was already known in
`../coherent-return/`; this is a quantitative actual-model application.
It does not locate the memory at long lags or imply a trace correlation.

The prior Lindemann--Weierstrass specialization also proves every
block transition is strictly positive at every nonzero real algebraic
epsilon for these dimensions, beyond the smallness regime. That
qualitative extension supplies no uniform size or mixing time.

The main theorem and quantitative memory deduction received a separate
internal audit. A normalization mismatch was caught and repaired before
recording the memory deduction. Exact rational checks, floating matrix
diagnostics, a plot, commands and artifact hashes are in
`../block-memory/`. No Lean verification or external refereeing is
claimed. The full fixed-tau coherent Heisenberg estimate remains open.
Tracked files are unchanged; no commit or push.

## 11. Direct fixed-coupling attempt; no new principal estimate

The 20 September continuation is recorded in `../secular-route/attempt.md`.
It attempted exact spectral-determinant resummation, replacement of actual
phases by independent phases, and transfer of a long-time prequantum trace
formula. None yielded the required fixed-tau weighted pair comparison.
This checkpoint adds no claimed breakthrough or completed BGS subcase.

The exact principal-minor expansion and unitary self-inversiveness leave
coherent weighted subset-energy sums at degree proportional to N. They
were independently checked on the frozen finite matrices. Pigeonholing
subset energies rejects a uniform characterwise phase replacement over
polynomial parameter intervals; it does not estimate the determinant
sum with its actual weights. The original-tau floating checks at tiny N
are explicitly below kick resolution and have no asymptotic significance.

The published Faure--Tsujii comparison, Theorem 10.3.2, has an unspecified
positive power of hbar and almost-unitary, corrected Toeplitz operators.
It does not provide the structured 1/N unitary comparison required by
our ergodic transfer theorem. No source-to-target identification was proved.
The exact determinant resummation and recent circuit semiclassics likewise
do not supply the omitted uniform coherent cancellation.

Individual secular coefficients must not be required to converge to their
CUE second-moment mean: the middle CUE coefficient tends to zero in
probability. That source check prevents introducing an incorrect new
target. The maintained target remains the weighted trace comparison and
ultimately all-k microscopic statistics of the fixed family. No git
publication; tracked tree unchanged.

## 12. Weighted secular sums and a corrected determinant endpoint

The continuation `../weighted-secular/attempt.md`, checkpoint
`weighted-secular-20260920-covariance-control-and-ratio-target`, is a child
of section 11. It enumerates the actual middle principal minors at
N=15,19,23, tests coherent frequency windows at several auxiliary common
exponents, and checks the result through an independent trigonometric
Jacobi assembly. Substantial cancellation occurs both within and between
frequency windows; independent phase replacement is not justified.
These are finite diagnostics, not original-tau asymptotic estimates.

`determinant_boundary.md` proves an elementary control showing that even
exact CUE covariance of characteristic polynomials, at every argument and
every dimension, need not give CUE pair statistics. The rotated deleted
clock has that covariance and regular microscopic spacings. It is an
abstract unitary control, not a counterexample for the fixed Anosov map.

The exact determinant-ratio transform instead contains the Abel trace
energy L_N(s). Its CUE target is (1-exp(-2s))/(4s^2). Convergence on one
countable arithmetic progression of positive s suffices for every compact
weighted pair test; the converse uses an explicit Fejer tail bound.
These reductions and the standard CUE ratio formula are reconstructed and
self-reviewed, with exact rational and independent floating checks.
No estimate of L_N for the prescribed fixed coupling has been proved.
The Bouclet--De Bievre long-time Egorov theorem was also checked at its
exact logarithmic time range and supplies no Heisenberg comparison.

Main BGS status: OPEN. No breakthrough, all-k theorem, independent review
or Lean certification is claimed. No tracked edit, commit or push.

## 13. Mixed loop hierarchy and limits of noise comparison

The continuation `../resolvent-flow/loop_bridge.md`, checkpoint
`resolvent-flow-20260920-mixed-hierarchy`, is a child of section 12.
Bourgade--Huang, arXiv:2607.07617v2 (9 September 2026), supplies a
conditional all-order route through approximate microscopic loop
identities. The exact cotangent resolvent of the fixed spectrum fits its
particle-generated Herglotz convention after the intensity factor pi.
Using the whole origin-probability space, the moment bootstrap also gives
all compactly tested anchored factorial correlations, not merely weak
point-process convergence. The mixed-loop hypothesis for the frozen map
is unproved.

Every same-half-plane loop test is automatically zero for every unitary
spectrum. The first mixed test is exactly 8i(L_N+C_N^0-1/(4s^2)); the
cubic C_N^0 may be complex. The unitary Brownian derivative of L_N is
one half the s-derivative of the real, finite-CUE-corrected defect. A
clock control satisfies all same-half tests and violates the mixed one.
Direct cotangent/Fourier/geometric calculations and full Hermitian-basis
finite differences check the exact identities, using auxiliary coupling
only. No original-tau asymptotic evidence is claimed.

A linear cat-transport noise covariance has rank at most the cat period;
transport by a simple-spectrum V has rank-one instantaneous eigenphase
covariance. Neither establishes isotropic Dyson noise. Separately,
`entropy_obstruction.md` proves that preserving a deterministic spectrum
at vanishing unfolded RMS distance modulo rotation/permutation forces
global CUE relative entropy divided by N to diverge. This excludes a
specific global smoothing comparison, not local entropy methods or BGS.

A fresh internal agent audited the conditional all-k bridge, first mixed
identity, entropy argument, and simple-spectrum qualification. External
peer review and Lean certification are not claimed. Main BGS status:
OPEN. No tracked edits, commit, or push.
