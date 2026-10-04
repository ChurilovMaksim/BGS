# Current results and exact scope

## Actual-start comparison and logarithmic regularity, 4 October 2026

[FLOW-012](coboundary_general_start.md) compares the original uncentered
chain from any odd unitary with $|p_1|+|p_2|\le K$ to Dyson motion from
exactly its Möbius-centered initial matrix. The bound is
$C_{f,K}[\sqrt t+N^{-1}+N^4\varepsilon+N^9\varepsilon^2+
tN^9\varepsilon+tN^{10}\varepsilon^2]$.
The $O_f(N^{-1/3})$ comparison at $2N^{34}$ steps applies eventually to
the actual frozen map. Its reference limit at that faster time is open.

[FLOW-013](dyson_relaxation_obstruction.md) constructs an empty local
Dyson limit at each prescribed vanishing time, using schedule-dependent
globally uniform simple spectra with bounded fixed traces and nonzero
power traces. Its chain consequence retains finite unit intensity without
uniform integrability. [FM-017](frozen_mesoscopic_regularity.md) extracts
logarithmic-scale Poisson regularity from the existing FM-007 and gives
two controlled local stationary points and exponential unweighted
vertical phase-tail bounds for a slower heat phase.
[FLOW-014](circular_dyson_actual_start.md) now closes the gap-independent
resummed circular contour and the entire Fredholm series, including
repeated initial levels. Its reference Brownian Laplace bound is
$C_f[E_N+(Nt_N)^{-1/2}]$. For the unchanged actual spectrum,
$t_N=8g_N$, $g_N=4\log J_N/J_N$, and balanced
$\varepsilon_N=N^{-9}/\sqrt{t_N}$ give the original uncentered chain
Sine$_2$ with smooth Laplace error $O_f(\sqrt{g_N})$ after
$\lfloor2t_N^3N^{36}\rfloor$ steps. The imported finite kernel is prior;
the startup threshold is ineffective, priority unestablished and
deterministic noise removal still open.
The [review](../record/general_start_review_20261004.md) records independent
internal checking of the new implications and the finite evidence boundary.

## Polynomial original-coboundary limit, 4 October 2026

[FLOW-011](coboundary_polynomial_limit.md) proves, for independent
normalized GUE kicks from an odd clock, the smooth local Laplace bound

$$
C_f[\sqrt t+(Nt)^{-1}+N^{-2}+N^4\varepsilon
+tN^9\varepsilon+tN^{10}\varepsilon^2].
$$

With $t=N^{-2/3}$ and $\varepsilon=N^{-26/3}$, exactly $2N^{34}$
original uncentered steps have error $O_f(N^{-1/3})$.
The proof retains fast-coordinate suppression, establishes
dimension-uniform semigroup derivatives and uses positivity to bound
the sixth test norm by $C_fN^6$. The weaker slow-time polynomial
corollary already follows from FLOW-010; its former scope statement is
corrected. The [review](../record/polynomial_coboundary_review_20261004.md)
records an independent internal check of the new estimates and finite
controls. Actual-start relaxation is supplied separately by FLOW-014
at the logarithmic time; deterministic noise removal and BGS remain open.
Unbounded correlation transfer for the chain requires uniform integrability.

## Fixed-time trace closure and expansion/memory boundary, 4 October 2026

[FM-013](fixed_time_wavepacket_trace_bound.md) proves bounded unnormalized
traces at every fixed nonzero time for the original odd-N frozen operator.
The explicit Gaussian refinement gives eventual first-two-trace bounds
4 and 9 and closes the starting K=20 choice, with no effective threshold.
Its exact frame and finite-order sampled residual avoid the even-N trace
formula. [FM-016](egorov_overlap_rigidity.md) proves fixed-map overlap rigidity
and affine-quantizer separation. [TRACE-013](arithmetic_word_expansion_obstruction.md)
gives a different primitive irreversible arithmetic map with uniform auxiliary
mixing gaps and coherent words, surviving flat destruction of exact markers.
The exact even tensor hierarchy is computed. These are project proofs with
self-review; all Heisenberg estimates for the frozen map and BGS remain open.

## Projected-square control and block crowding, 1 October 2026

[TRACE-012](folded_quadratic_resonance_control.md) bounds the signed
resonant cubic by $C_W\sqrt{E_N\|P_d(\rho_N^2)\|_2^2}$, retaining
the factorial budget. A simple-spectrum family proves strict improvement
over the global fourth moment. Root allocation can produce a d^2 loss
if omitted from block density. Balanced counts give a general factorial
crowding obstruction. The actual-map application remains finite;
E/G asymptotics and BGS remain open. The
[review](../record/folded_quadratic_review_20261001.md) records the checks.

## Resonant density mechanism and its critical boundary, 1 October 2026

[TRACE-011](resonant_cubic_density_control.md) bounds the signed union of
all three resonant cubic strips by $C_W\sqrt{E_N M_4(N)}$, without the
number-of-times loss. A local moment above order three, or critical cubic
uniform integrability, closes the sector under vanishing resonant mass.
A realizable sharp cluster obstruction survives every signed smooth CUE
pair test after selecting a CUE background, even with simple spectra.
Actual-map mass/density estimates and BGS remain open; the
[review](../record/resonant_density_review_20261001.md) fixes the next inputs.

## Absolute obstruction and signed cubic continuation, 30 September 2026

[TRACE-010](signed_heisenberg_comparison.md) proves that simultaneous
unaveraged absolute pair and all-order CUE comparison is impossible: the
cubic error must grow at least as sqrt(N) under the pair premise, with
an explicit constant, and the fixed-order generalization grows as
N^(k/2-1). The exact signed bridge remains viable. A low-band CUE variance
calibrates arbitrary complex weights and resonant strips; a formal
quadratic-phase control has rapid cancellation but fails moment positivity.
The [review](../record/signed_heisenberg_review_20260930.md) records the
first actual-map signed cubic attack. It and BGS remain open.

## Prime-resonant sector audit, 30 September 2026

[TRACE-009](prime_resonant_sector.md) proves the exact mass criterion for
the full prime-resonant sector, its Fejer spectral-comb representation
and a conditional one-coherent-mode obstruction. The product orientation
is corrected; -98 and the alleged exceptional primes are reconstructed,
and neither 29 nor 97 needs exclusion from the scalar test. Rains' prior
power-map theorem supplies the correct Haar reference. Actual frozen-map
sector cancellation and the complete BGS target remain open; see the
[independent reconstruction](../record/prime_resonant_review_20260930.md).

## Heisenberg-note completions, 30 September 2026

[FM-014](frozen_phase_finite_type.md) proves scalar transversality of order
14, and order 15 robust to linear phases. [FM-015](frozen_commutator_action.md)
constructs a local classical commutator action with explicit derivative
remainder that preserves transversality at the maintained fixed coupling.
[FUP-001](offdiagonal_digit_fup.md) classifies the ideal off-diagonal
digit alphabets by parity, using Cohen's prior criterion; its binary
norm is exact. [Supporting identities](heisenberg_trace_support.md)
complete the finite CUE cycle benchmark and conditional Fejer/transfer
arguments. The [audit](../record/heisenberg_note_review_20260930.md)
records the errors, checks, duplicates and still-open quantum/renewal arrows.

## Simultaneous random-kick limit, 30 September 2026

[FLOW-010](coboundary_joint_limit.md) makes the coboundary clock theorem
quantitative in dimension: the original uncentered chain has a joint
Sine_2 weak limit at epsilon_N=exp(-N), t_N -> 0, N t_N -> infinity.
The stopped first-trace scale is epsilon/N + epsilon^4. Smooth tests at
t_N=N^(-2/3) have error O_f(N^(-1/3)). This is a project proof with
author self-review. Polynomial step sizes are now treated in FLOW-011;
deterministic BGS remains open.
See the [audit](../record/coboundary_joint_review_20260930.md).

## Actual coboundary steps and Möbius reduction, 29 September 2026

[FLOW-008](coboundary_fourth_order_drift.md) computes the missing fourth-order
drift of finite Gaussian coboundary steps. [FLOW-009](coboundary_mobius_diffusion.md)
removes their faster mean through a Möbius spectral quotient and proves a
clock-to-Sine local limit for the uncentered random chain in an explicit
iterated limit. This closes a scoped connection from finite random kicks to
the noise mechanism, not deterministic BGS. See the
[self-audit](../record/coboundary_mobius_review_20260929.md).

## Quadratic-noise dynamics, 29 September 2026

- [FLOW-004](quadratic_noise_coupling.md): exact synchronous cancellation,
  every-even-moment bound, microscopic coupling at t log N -> 0, and
  phase-averaged local comparison without an occupancy hypothesis.
- [FLOW-005](quadratic_noise_reversibility.md): explicit Haar-reversible
  correction, gradient potential, and vanishing raw/corrected path TV at t -> 0.
- [FLOW-006](quadratic_noise_trace_fluctuations.md): fixed-trace OU limits
  for both processes and a fixed-positive-time obstruction to raw/Dyson coupling.
- [FLOW-007](quadratic_noise_clock_limit.md): phase-averaged Sine_2 weak
  limit from an odd clock at t -> 0, Nt -> infinity, using the credited
  Dyson clock formula; a strict obstruction to generic noise removal.
- [Historical FM-013 route](quadratic_noise_fixed_time_input.md): the
  sharper Faure source adaptation retains its conditional regularized
  trace identification. The [direct 4 October proof](fixed_time_wavepacket_trace_bound.md)
  now closes bounded fixed-time traces separately.

These auxiliary results do not close deterministic BGS. See the
[proof and computation audit](../record/quadratic_noise_review_20260929.md).

## Quadratic noise mechanism and exact boundaries, 28 September 2026

[BGS-FLOW-003](quadratic_coboundary_noise.md) computes the complete covariance
of $i[G,UGU^*]/\sqrt2$ for normalized GUE $G$. Centered noise is elliptic on
traceless Hermitian directions exactly when $|\operatorname{Tr}U^2/N|<1$;
explicit covariance whitening gives the infinitesimal traceless Dyson
generator. The original coboundary eigenphase covariance starts at fourth
order, consistently with the earlier second-order obstruction.

The raw noise fails exact Haar stationarity by $4+2/N^2$ on
$|\operatorname{Tr}U^2|^2$ for $N\ge4$. A local pair-generator bound for
small nonzero second trace requires microscopic occupancy control; this
and deterministic noise removal are unproved for the frozen map.
Finite-direction quadratic noise has rank at most $d(d+1)/2$.
See the [research checkpoint](../record/quadratic_noise_program_20260928.md).

## All-time periodic-point arithmetic and upload audit, 27 September 2026

[BGS-FM-012](frozen_periodic_point_annihilator.md) gives the exact rectangular
Fourier annihilator of $\operatorname{Fix}(S^m)$ for every $m\ge1$ by a Pell
factorization. The physical symbol averages exactly $-1/10,-1/20,0$ at
$m=1,2,\ge3$. This extends the explicitly indexed arithmetic control,
without implying any nonlinear weighted or quantum trace estimate.

The [CUE upload audit](../record/cue_upload_review_20260927.md) reproduces
the submitted suite but rejects its all-order implication. New controls
exhibit loss of higher correlations from pair-only data, a bispectrum
Fourier-sign error, and incorrect phase/cutoff diagnostics. The corrected
finite identities and fresh proxy data are recorded with their boundaries.

## Singular CUE benchmark and coboundary spectral flow, 25 September 2026

[BGS-CUE-001](cue_singular_energy.md) deduces a stable law for the
centered inverse-chord energy of **Haar CUE**, $3/2<p<3$, from the
checked Ben Arous--Bourgade small-gap theorem and an explicit
determinantal tail-variance estimate. For $p=2$ the exact
normalized mean is $(1-N^{-2})/6$, its variance is infinite,
and $N^{1/3}$ centered fluctuations have a $3/2$-stable limit.
It also shows that weak local point-process convergence alone
cannot justify an unregularized inverse-gap limit.

[BGS-FLOW-001 and BGS-FLOW-002](coboundary_spectral_flow_bound.md)
give a quantitative finite-matrix coboundary spectral-flow bound,
an abstract sequence attaining its leading constant, and the
infinitesimal sine-drift obstruction to producing Dyson diffusion
with a Gaussian coboundary. The previously maintained
three-exponential second-order normal form is credited as prior
project work. [Audit and checks](../record/research_pass_cue_flow_20260925.md).
No deterministic Heisenberg trace bound or full BGS claim is implied.

## Seven-cut smooth transfer and two-clock Gram falsifier, 25 September 2026

[`BGS-RES-007`](fixed_map_resolvent_frontier.md) upgrades the seven-cut
pair transfer to every fixed derivative in $s$ on compact positive
intervals. The scalar adjoint-resolvent traces of the two **full**
propagators differ by $O_{K,r}(\tau/\log N+1/N)$ in each such derivative;
neither trace has been shown to approach the CUE value.

[`BGS-TRACE-008`](two_clock_gram_falsifier.md) constructs simple abstract
odd-dimensional spectra with weak Haar empirical limit, unit-interval
occupancy at most three, every positive power trace nonzero and
$N^{-1}\operatorname{Tr}\Gamma_N^2\to4/3$, but an explicitly non-CUE
pair Abel limit. The even companion attains the exact finite-$N$ CUE
**expected** Gram moment. Neither construction is the maintained frozen
map. The [cycle review](../record/bgs_program_20260925.md) records the
remaining signed Heisenberg-trace and mixed-loop obstacle.

## Pair resolvent, universal Abel floor, and spectral-flow audit, 25 September 2026

[`BGS-RES-006`](fixed_map_resolvent_frontier.md) gives an exact
finite-dimensional resolvent representation of the pair Abel statistic and
shows that the CUE pair limit is equivalent to the corresponding scalar
resolvent limit. For fixed $s>0$, the explicit comparison error is at most
$2\cosh(2s/N)/(3N)$; the model-specific limit remains open.
[`BGS-TRACE-007`](fixed_map_resolvent_frontier.md) gives the sharp universal
floor $L_N(s)\ge1/(e^{2s}-1)$ from Cohn--Kumar's regular-polygon energy
theorem. The floor is strictly below the CUE value and does not identify the
limit.

The [spectral-flow audit](frozen_spectral_flow_controls.md) proves the exact
phase-velocity equations, retains the ordered product in powers of the
propagator, and supplies an isospectral clock control family with uniformly
delocalized kick entries. It refutes the tempting collapse of the ordered
product to one exponential for odd $7\nmid N$; it is not a
counterexample for the maintained frozen family. The accompanying exact
depolarizing-noise identity shifts the unknown Abel parameter and does not
bound the original long traces.

## Arithmetic returns and effective submicroscopic gap, 24 September 2026

[`BGS-FM-010`](frozen_arithmetic_trace_rigidity.md) computes
\(|\operatorname{Tr}M_N^m|^2\) exactly as a square of a Pell gcd for
every odd \(N,m\ge1\). Algebraic-time exponential independence then
shows \(\operatorname{Tr}U_N^m\ne0\) at the unchanged \(\tau=10^{-80}\).
Scalar powers of \(U_N\) occur only at \(N=7\), while algebraic-entry
commutants are scalar for \(7\nmid N\). These are qualitative exact
statements, not upper estimates of \(|\operatorname{Tr}U_N^m|\).

[`BGS-FM-011`](frozen_effective_gap_floor.md) uses
[Roy, Theorem 1.1](https://arxiv.org/pdf/1607.00579v1.pdf) to turn
the pre-existing simple-spectrum result into an explicit but
astronomically weak \(N\)-dependent eigenphase gap floor at \(7\nmid N\).
The [two-file audit](../record/two_continuations_review_20260924.md)
lists source boundaries and omitted duplicate claims. In particular,
the claimed alternative 492-degree finite certificate was not
provided, and neither new claim approaches the required \(N^{-1}\)
statistics or the Heisenberg signed joint traces.

## Exact fixed-coupling seven-cut and algebraic bounds, 24 September 2026

The [seven-cut theorem](frozen_seven_cut_reduction.md) (`BGS-FM-007`)
removes seven nearly zero Jacobi edges from the exact fixed generator.
The nuclear distance of the full propagators is at most
$28\pi^2\tau/(25N)$, and their *existing* sine-kernel laws of every
fixed order are equivalent. Their pair and infinite Abel statistics
differ by $O(\tau/\log N)$ without assuming CUE. The cut generator has
seven path blocks; the full propagator retains strong metaplectic
interblock coupling.

[Total minor nonvanishing and fixed-time spectral simplicity](frozen_algebraic_spectral_simplicity.md)
(`BGS-FM-008`) apply at all odd $7\nmid N$ and nonzero real algebraic
couplings, including $\tau N$. The [commutator-cube certificate](frozen_common_antireversor_certificate.md)
(`BGS-FM-009`) excludes a common antiunitary of $(A_N,M_N)$ at every
odd $N\ne7$ and, with algebraic entries, a reversor of $U_N$.
Neither result supplies a quantitative eigenphase gap. The
[submission audit](../record/submitted_article_review_20260924.md)
separates these statements from the still-open Heisenberg joint-trace
comparison and main BGS law.

## Nonlinear classical pressure boundary, 23 September 2026

For the **actual nonlinear Anosov map** of the fixed frozen model,
[`BGS-FM-006`](nonlinear_bracket_pressure.md) proves that the squared norm of
the physical symbol's lag-$r$ Poisson bracket is comparable to
$\exp(rP(\log J^u))$, where $P(\log J^u)>2\log(3+2\sqrt2)$ at every
allowed nonzero coupling. Hence the linear $\lambda^{-r}$ normalization
cannot have a uniform nonlinear full-lag upper bound. A perturbation
calculation gives the exact positive leading coefficient
$(\pi^4/2)(7834656061/500000)$ for the pressure gap as the classical
coupling tends to zero. The [exact coefficient check](../computations/verification/nonlinear_pressure_variance.py)
does not establish the pressure theorem. The classical result does not
estimate fixed-strength Heisenberg-time quantum traces or BGS statistics.

## Full-lag gap and exact generator rank, 23 September 2026

For the **actual physical symbol** of the frozen model under the linear cat
transport, [a uniform Riesz bound](frozen_full_lag_resonance.md) controls every
positive lag and simultaneous dynamical translate, including the first lag:
the singular bound is at least `7*pi/2`. It persists for arbitrary real
weighted-Wiener perturbations of radius `1/100`, including observables with
infinitely many frequency orbits. The proof uses a one-visit property of the
specific Fourier support; its [internal independent audit](../record/frozen_full_lag_review_20260923.md)
and exact coefficient check are separate evidence. This is a classical
linear-map result, not an estimate for the nonlinear kicked flow.

The [frozen generator rank boundary](frozen_kick_rank_boundary.md) gives at
most `gcd(N,7)` eigenvalue multiplicity and exact
`rank(U_N-zM_N)>=N-gcd(N,7)` for odd `N>=3`. It uses the existing Jacobi
representation and a checked Hermite–Lindemann input. The quantitative
approximate-rank bound is restricted to `|tau N|79/50<=pi`; it gives no
fixed-strength large-`N` trace bound. Status, limits and verification scope
are in the [continuation record](../record/integration_20260923.md).

## Clustered Abel transform and positive-time windows, 22 September 2026

For unitary spectra in \(K\) arcs of radius \(\eta\), the exact Poisson-kernel
bound in [the proof](clustered_abel_window_boundary.md) yields
\(L_D(s)\to\infty\) if \(K/D\to0\) and \(K\eta\to0\).
The explicitly compensated Pell family inherits this consequence in its
existing larger pinning range. An explicit simple-spectrum construction has
the same Abel divergence and spacing collapse, yet its form factor tends to
zero uniformly on each \(m\in[aD,bD]\), \(0<a<b\). This limits what
clustering alone can prove about Heisenberg-time traces. Claim
`BGS-TRACE-006` is independent of the unproved frozen-map estimate;
see its [dated research record](../record/abel_window_research_20260922.md).

## Smooth finite-orbit rigidity, 22 September 2026

**Project proof; adversarial self-review and exact finite regressions.**
For every hyperbolic A in SL(2,Z), the finite lag classes
`{g,C^r g}/(4*pi)` are independent modulo L2 coboundaries for every real
nonconstant smooth g supported on finitely many signed A-orbits.
The pair-channel normal form is a common real entire all-pass filter of a
finite Fourier polynomial. A zero-variance smooth counterexample therefore
requires unbounded `abs(det(k,Ak))` on its support.
See [proof](finite_orbit_resonance_rigidity.md),
[audit](../record/finite_orbit_proof_audit_20260922.md), and
[scope record](../record/research_pass_20260922.md).
This does not prove arbitrary-analytic nondegeneracy, a uniform coercivity
bound, quantum microscopic statistics, or external priority.


Stable claim IDs and cross-layer links are in `../record/claims.json`; status
authority remains `../record/claim_ledger.md`. The thematic navigation layer
is `topics/README.md`. This index is expository and cannot strengthen the
claim ledger.


## Fixed-map continuation, 21 September 2026

**Project proofs with fresh exact/finite replay; external priority and referee
validation unestablished.**  The late fixed-map handoff adds the following
maintained results while leaving microscopic BGS open:

| Result | Established scope | Boundary |
|---|---|---|
| [Actual frozen-model symmetry theorem](fixed_model_symmetry_theorem.md) | Exact raw-to-midpoint Weyl dictionary; analytic Anosov classical map; trivial (C^1) centralizer, no (C^1) reversor, no relevant affine (C^1) conjugacy for (0<\operatorname{abs}(\kappa)\le10^{-12}) | Does not exclude (N)-dependent quantum commutants or prove trace cancellation |
| [Full-symbol odd-Pell crossover](fixed_model_pell_crossover.md) | Gaussian moment law for (\sqrt K\,\overline A_K), exact variance (1650797/4000000), and necessary escape ( \operatorname{abs}(\epsilon_K)\sqrt K\to\infty) for CUE pair behaviour in the stated family | Frozen (\epsilon_K=\tau N_K) lies beyond the proved crossover window |
| [Moment controls and transfer](fixed_map_moment_control_and_transfer.md) | Stronger two-level moment interval, exact repeated-clock loop-test falsifier, and RMS perturbation-transfer estimate | Conditional/asymptotic inputs do not reach fixed (\tau) |
| [Three-orientation barrier](three_orientation_resolvent_barrier.md) | Under three normalized mixed-residual hypotheses, explicit lower barrier with additive (s^3/[64(1+s^2)^{7/2}]) | Residual decay for the actual propagator is still unproved |
| [Fourier-line resonance coercivity](fourier_line_resonance_coercivity.md) | Sharp lower constant on every real Fourier-line (H^{1+\beta}) class when (\kappa_\beta>0); (\kappa_1=\sqrt{(T-2)/(T+2)}), hence (1/\sqrt2) for the stated project convention; (H^{3/2}) positivity for (\operatorname{abs}(\operatorname{tr}A)\ge6) | Does not solve the full two-dimensional analytic cohomological equation |
| [Local jet obstruction](local_jet_resonance_obstruction.md) | Exact polynomial local coboundary with a strict local minimum | Local model only; shows why fixed-point jets cannot settle the torus problem |

The [final integration audit](../record/final_research_handoff_20260921.md)
records the recovered archive hashes, fresh replay and old-PR disposition.

## Fixed-family reductions, 20 September 2026

[The fixed-map chapter](fixed_map_resolvent_frontier.md) consolidates
algebraic-return, coherent-memory, determinant-ratio and mixed-loop work.
The new exact p=3 mixed identity gives a conditional bounded interval for
the Abel pair statistic when the first two residuals vanish. Those
residuals remain unproved for the fixed map, and the interval does not
identify the CUE value. The full all-order criterion is conditional on an
external loop-characterization theorem and a still-open model estimate.
All recovered proof and computational records are in the indexed supplement.

## Recovered finite-window result and scope corrections

The [compensated-family note](compensated_heisenberg_trace_control.md),
(H8)--(H9), gives an explicit separated-cluster bound and its averaged
Heisenberg-window consequence at epsilon=o(N^(1/3)). The parent operator
estimate, inversion symmetry and vanishing classical strength remain inputs.
The [trace bridge](trace_to_local_statistics_bridge.md) now includes an exact
short-trace counterexample while retaining its later bandlimit extension.
The Cayley support proposals imply exclusion with a fixed power margin;
K^(4+o(1)) is insufficient for the full K=o(p^(1/4)) regime.
See [recovery audit](../record/recovery_audit_20260920.md).

## Short returns and ergodic local limits

**Project proof; self-reviewed; priority unverified.** An ergodic stationary
intensity-one local limit forces vanishing normalized traces uniformly over
all sublinear frequency windows. More generally it forces uniform density
in spatial L1 on every window containing a diverging number of mean spacings.
No second-moment convergence assumption is needed for this implication.
The proof uses a slowly changing mark and preservation of first moments.

Applied to the existing cat-map return laws, it excludes such local limits
when $\epsilon_K\to0$ and $K\epsilon_K^2$ remains bounded. Positive-variance
universality would require $K\epsilon_K^2\to\infty$; this is not sufficient.
An independent Gaussian pair inequality gives explicit Poisson/sine-kernel
discrepancies and low-frequency budgets. The critical conclusion depends on
global mean-spacing unfolding. See
[return_trace_obstruction.md](return_trace_obstruction.md) and its linked review.

Theorem 3 now allows intensity loss. For a folded law
$\mu=\rho\,dy+\mu_{\rm s}$, every marked local limit has conditional
intensity $h\le\rho$; an ergodic limit of intensity $\alpha$ requires
$\alpha\le\operatorname*{ess\,inf}\rho$. Explicit simple-spectrum
constructions attain every admissible $\alpha$. This sharpness is in the
class of abstract spectra, not in the cat-map quantization class.
For the free Brownian harmonic endpoint, $0<t<4$, every local limit has
empty-component weight at least $1-b(t)/\pi$; an ergodic limit is empty.
The density-transport formula also constructs identical return laws with
different locally unfolded statistics. Review and finite evidence:
[return_local_limits_review_20260913.md](../record/return_local_limits_review_20260913.md).

## General hyperbolic return laws and sharp regularity

**Project proof with limited internal review; external priority unverified.**
For every fixed hyperbolic matrix in SL(2,Z), explicit odd-dimensional
arithmetic subsequences support Gevrey return suppression and an absolute
Gaussian approximation of order $K^{-1/2}$ at the stated small scaled
replica amplitude. Every fixed finite Gevrey order is allowed; constants
are not uniform as the Fourier-decay exponent tends to zero.

For period-averaged observables, a square-root logarithmic Fourier weight
suffices for a joint Gaussian limit. For each map a fixed continuous symbol
shows that every smaller logarithmic exponent is insufficient, even after
subtracting the quantum mean. See
[general_cat_return_laws.md](general_cat_return_laws.md), Theorems 1–3.
These are global, arithmetic-subsequence results. They do not close the
Heisenberg-time, fixed-classical-strength BGS comparison.

## Harmonic-scale laws of the actual kicked return propagator

**EXACT (project proof; independently audited by a second agent).** In the
Pell harmonic window described below, set $\epsilon=\tau/\sqrt{2K}$ and
$U_{\epsilon,a}=e^{i\epsilon B_a}U_0$. For every fixed $m,\tau$, the normalized
odd trace of $U_{\epsilon,a}^{mK}$ converges in $L^2$ over harmonics to the
absolutely convergent cycle-pair diagram series in `pell_harmonic_returns.md`.
It determines a weakly continuous family of probability measures on the
circle. At $\beta=0$ its moments are $e^{-m^2\tau^2/2}$; at $\beta=1/2$
they are $e^{-m\tau^2/2}L_{m-1}^{(1)}(m\tau^2)/m$.
The second moment equals
$e^{-t}(1-te^{-(1-2\beta)t/2})$ for $t=\tau^2$ and $\beta\ge1/6$.

The key additional estimate is uniform control of nonzero aggregate
relations in the full Fourier--Bessel expansion, using the integer image
of $S^2-6S+I$ and its $\ell^1$ lower bound. The endpoint probability laws
are known. Arithmetic priority, external referee assessment and BGS are
not established. Fixed $mK\asymp\log N$ is the precise time scope.

## Harmonic-scale transition in the fixed Pell cat map

**EXACT (project proof).** For prime Pell periods $K\to\infty$, sample
integers $1\le a\le L_K\le\sqrt{N_K}$ coprime to $N_K$, with
$\log L_K/\log N_K\to\beta\in[0,1/2]$. Compressions of the physical harmonic
$2\cos(2\pi ax/N_K)$ have global empirical spectral measures converging in
probability, uniformly over all odd cat eigenspaces, to the circle-graphon
law of radius $(1-2\beta)/2$. Every fixed moment converges in $L^2$.

The fourth moment is $3-2\beta$. With $\rho=1-2\beta$, the sixth is
$5+6\rho+15\rho^2/4+(3\rho/2-1)_+^2$. These laws have unbounded support for
$\beta<1/2$, while the endpoint is the variance-one semicircle. They vary
weakly continuously. A weighted ordered-moment theorem interpolates between
commuting Gaussian and free semicircular fields; normalized complementary
half-window commutators have limiting squared norm $8\beta(1-\beta)$.

The proof, exact scopes and prior graphon results are in
`pell_harmonic_transition.md`. The key arithmetic input is quadratic
harmonic-phase averaging, not finite independence of the Weyl variables.
This does not prove local statistics of a quantum propagator. Priority
for the arithmetic realization remains unverified.

This is the concise theorem index. The repository-wide status authority is
[`../record/claim_ledger.md`](../record/claim_ledger.md); historical commits or
notes do not override it.

## September 9: full Cayley--Jacobi trace Gaussian limit

**EXACT + EXTERNAL-THEOREM.** For odd prime subgroup order `K`, split prime `p`,
and `n=K-1`, the real variable
`n^(-1/2) sum_(a in c(H\{1})) e_p(qa)`, with uniform `q!=0`,
converges to `N(0,1)` whenever `K->infinity` and `K=o(log p)`.
At any finitely many distinct positive fixed integer multiples of `q`,
the joint limit is a vector of independent standard normals.

The same empirical joint laws converge weakly in probability over dyadic
split designs `K in (Q/2,Q]`, `p in (X/2,X]`, whenever
`Q->infinity`, `log Q=o(log X)`. The proof controls all fixed weighted moments
by a global `O_w(K^r)` collision budget. Its quantitative average normalized
excess is `O_w(Q^(r/2+1)/X)`.

The scalar law also has the quantitative pointwise estimate
`d_Kol <= C((K-1)^(-1/2)+sqrt((K-1)/log p))`.
For sufficiently large `X,Q` with `Q<=X^(1/4)`, outside a design fraction
`O((log X)X^(-1/4))`, its Kolmogorov distance is
`O(Q^(-1/2)+sqrt(log Q/log X))`. The additional input is classical
Esseen smoothing; the uniform growing-moment budget is proved explicitly.

This is a full-trace distribution theorem, not a local spectral theorem or
a theorem about traces of matrix powers. External inputs: Chowla independence,
and Bombieri--Vinogradov/PNT for the density version. Global novelty has not
been established. See [`cayley_trace_gaussian_limit.md`](cayley_trace_gaussian_limit.md).

## 1. Pair-key / fourth-moment reduction — EXACT

For odd prime `p`, the off-diagonal key

```text
u=x/y, v=(x-1)/(y-1), d=x-y
```

is bijective with the maintained inverse formulas; the diagonal has
multiplicity `p-2`. Under subgroup constraints there are exactly
`(K-1)(K-2)` off-diagonal pairs and

```text
|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K.
```

The corrected distribution is

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}.
```

See [`fourth_moment_reduction.md`](fourth_moment_reduction.md).

## 2. Cayley additive-energy reduction — EXACT

For

```text
c(h)=(h+1)/(h-1),
A=c(H\{1}),
```

one has `d(u,v)=2/(c(u)-c(v))` and `c(h^-1)=-c(h)`.  Thus the mixed layer is
controlled by `E_+(A)`.  Prime-order characteristic-zero additive collisions
are only the forced identity/inversion-swap relations.

## 3. Best uniform pointwise theorem — EXACT + EXTERNAL-THEOREM

For

```text
100<K<p^(3/4)/3,
```

Vyugin--Makarychev gives

```text
E_+(A)<34K^(8/3).
```

The sharp target remains

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))).
```

## 4. Fixed-product rows — EXACT

For one valid pair put `u=xy`, `s=x+y`. Then

```text
c(x)+c(y)=2(u-1)/(u-s+1).
```

At fixed product and nonzero parameter there is at most one unordered subgroup
pair. If `I_K(p)` is the maximal intersection size of two distinct product
rows, then

```text
Delta_K(p)<=4 I_K(p)(K-1)(K-2).
```

The normalized row ratio `r` has affine trace map

```text
Y=alpha_r X+beta_r,
alpha_r=U_(r-1)(tau/2),
beta_r=-2U_(r-2)(tau/2),
tau=zeta+zeta^-1.
```

## 5. Exact maximal-real order-three support — EXACT + EXTERNAL-THEOREM

Let `C_K(T)` be the minimal polynomial of `tau` and

```text
H_K(T)=(T-2)C_K(T).
```

After removing the unique invalid characteristic-zero trace, the source/target
cofactors have fixed degree `m=(K-1)/2`. For every split embedding prime,

```text
deg gcd(P_(K,r),Q_(K,r) mod q)=row intersection count.
```

The first three fixed-degree subresultants define an ideal contracting to
`Lambda_(K,r)^(3) Z`, and

```text
p|Lambda_(K,r)^(3)
iff
some row pair in ratio class [r] has I>=3.
```

Outside the product support `Lambda'_K^(3)`,

```text
I_K(p)<=2,
Delta_K(p)<=8(K-1)(K-2),
E_+(A)<=11(K-1)(K-2).
```

Exact anchors include

```text
Lambda'_(13,12)=5^2,
Lambda'_(17,10)=103,
Lambda'_(23,18)=47^3*139.
```

The older dehomogenized `D'/G'` invariants remain one-way obstructions only;
their converse failed a degree-drop audit at projective infinity.

See [`cayley_product_row_real_trace_ideal.md`](cayley_product_row_real_trace_ideal.md).

## 6. Characteristic-zero trace-intercept rigidity — EXACT + EXTERNAL-THEOREM

For trace classes define

```text
gamma_r(a,b)=t_b-alpha_r t_a.
```

Bass's prime-conductor cyclotomic-unit theorem implies multiplicative
independence of

```text
|1-zeta|,...,|1-zeta^m|.
```

Using

```text
|s_n|=E_[2n],
|t_x-t_y|=E_[x-y]E_[x+y],
```

one gets a complete fibre classification: every characteristic-zero fibre has
size at most `2`. For `r=-1` doubletons are swaps; for `r!=+-1` every doubleton
is, up to signs/exchange,

```text
([a],   [a+1-r]),
([a+2], [a+1+r]).
```

The identity comes from `t_(x+r)-t_(x-r)=s_r s_x`.  A third point would create
a triangle in the step-two quotient of an odd cycle, which is impossible.

An independent C++20 group-ring verifier checks every normalized ratio through
the quick range `K<=199`; the recorded extended run reaches prime `K=809`.

See [`cayley_trace_intercept_rigidity.md`](cayley_trace_intercept_rigidity.md).

## 7. Cyclotomic-unit matching and general scalar support — EXACT

With `u_n=s_n/s_1`, valid row intersections satisfy exactly

```text
W_r(b)=V_r(a) mod q,
W_r(b)=u_((b+r)/2)u_((b-r)/2),
V_r(a)=u_r u_((a+1)/2)u_((a-1)/2).
```

Define the scalar shift resultant

```text
R_(K,r)(Z)
 =Res_T(P_1(T),R_r(alpha_r T+beta_r+Z))
 =c_0+c_1Z+c_2Z^2+....
```

Then

```text
ord_0 R_(K,r)=I_(1,r),
I>=3 iff c_0=c_1=c_2=0 mod q.
```

The three-generator contraction `Omega_(K,r)^(3)` has the same split
rational-prime support as `Lambda_(K,r)^(3)`.  For each fixed ratio,

```text
sum_(p==1 mod K, I_r(p)>=3) log p=O(K^3).
```

This is not a polynomial largest-prime theorem; summing over `O(K)` ratios
returns the existing `O(K^4)` scale.

## 8. Inverse-row reflection — EXACT

For `r=-1`,

```text
alpha=-1,
beta=2tau,
Q(T)=-P(2tau-T).
```

Writing

```text
F(X)=P(tau+X)=E(X^2)+X O(X^2),
```

one has for every split embedding prime

```text
I_-1(q)=2 deg gcd(E,O mod q).
```

Thus inverse intersections are automatically even. A fixed-degree half-size
support ideal defines `Xi_K`. At `(K,p)=(31,1303)`, the direct intersection
size is `4`.

See [`cayley_product_row_reflection.md`](cayley_product_row_reflection.md).

## 9. Inverse pair-sum perfect square — EXACT

Let the roots of `F` be `x_1,...,x_m` and define

```text
R_-(Z)=Res_X(F(X),F(Z-X)).
```

Then universally

```text
R_-(Z)=2^m F(Z/2) S(Z)^2,
S(Z)=prod_(i<j)(Z-x_i-x_j).
```

For split primes, `2^mF(0)` is a unit, so

```text
I_-1(q)=2 ord_0 S(Z),
I_-1(q)>=3 iff S(0)=S'(0)=0 mod q.
```

The two-scalar ideal `(S(0),S'(0))` contracts to `Theta_K`; `Theta_K` has the
same split order-three support as `Xi_K` and the inverse factor of `Lambda`.
Full integer equality is not claimed.

See [`cayley_inverse_pair_sum_factorization.md`](cayley_inverse_pair_sum_factorization.md).

## 10. Inverse pair sums are a translated half-degree resultant — EXACT

The square root itself has a much cheaper description. Translate

```text
F_Z(X)=F(X+Z/2)=E_Z(X^2)+X O_Z(X^2).
```

Then, up to a convention-dependent sign,

```text
S(Z)=+-Res_Y(E_Z,O_Z).
```

In particular

```text
S(0)=+-Res(E,O),
S'(0)=+-d/dZ Res(E_Z,O_Z)|_(Z=0).
```

The first-order deformation is

```text
dE_Z/dZ|_0=(O+2Y O')/2,
dO_Z/dZ|_0=E'.
```

Hence inverse order-three support is simultaneous vanishing of a half-degree
resultant and its translation derivative. Both scalars can be computed with
one Sylvester determinant over dual numbers `eps^2=0`, avoiding the degree-`m^2`
shift resultant.

Exact two-scalar anchors are

```text
Theta'_7=1,
Theta'_11=1,
Theta'_13=5,
Theta'_17=1,
Theta'_19=37,
Theta'_23=47^2*137.
```

For comparison `Xi'_23=47*137`: split prime support agrees, valuations differ.
The translated route is orders of magnitude faster than the full shift
resultant in the maintained SymPy reference computation; Smith normal form is
the next finite-algebra bottleneck.

## 11. Square collision resultants and canonical discriminants — EXACT

Every maintained prime-order cleared collision polynomial satisfies

```text
Res(Phi_K,P)=K^3M^2.
```

The Fibonacci slice

```text
Res(Phi_K,X^2+3X+1)=F_K^2
```

shows individual resultants may be exponentially large.  The canonical
difference polynomial gives for split primes

```text
Delta_K(p)>0 iff p|Disc(S_K),
Delta_K(p)<=4v_p(Disc(S_K)),
```

with exact ratio-orbit fourth-power structure

```text
|Disc(S_K)|
 =2^((K-1)^4/4)K^((K-1)(K^2-7)/4)J_K^4.
```

## 12. Global split-prime mass and averaged theorems — EXACT / EXTERNAL-THEOREM

For odd prime `K`,

```text
sum_(p==1 mod K) Delta_K(p)log p
 <=(K^3-5K^2+6K+1)((K-1)log12-3logK).
```

For prime `K~X^theta`, split prime `p~X`, Bombieri--Vinogradov and PNT imply

```text
average Delta_K(p)/K^2 <<_theta X^(3theta-1)
```

for fixed `theta<1/3`.  For fixed `theta<1/5`, asymptotically almost every split
pair has the exact baseline

```text
Delta_K(p)=0,
E_+(A)=3(K-1)(K-2).
```

## 13. Frobenius amplification in minimal finite extensions — EXACT

For arbitrary prime `p!=2,K`, put

```text
f=ord_K(p), q=p^f, H=mu_K(F_q).
```

Every non-forced collision Frobenius orbit has size exactly `f`, hence

```text
f | Delta_K^ext(p).
```

The weighted resultant budget and canonical discriminant classification extend
to all such rational primes.  For unrestricted prime pairs `K~X^theta,p~X`,
PNT + Brun--Titchmarsh + the Frobenius multiplicity give a density-one exact
baseline for every fixed `theta<1/3` in the minimal extension.  This does not
improve the split slice, where `f=1`.

See [`cayley_frobenius_amplification.md`](cayley_frobenius_amplification.md).

## 14. Full Cayley/Jacobi trace identity — EXACT

For the normalized full annihilator twisted-Jacobi matrix,

```text
1_Ahat(r)=K Tr M_S(2r),
sum_q|Tr M_S(q)|^2=p(K-1)/K^2,
sum_q|Tr M_S(q)|^4=pE_+(A)/K^4.
```

The normalized fourth/second moment ratio tends to `3` in the maintained split
double average below `theta<1/3`. This is not a CLT and not a local spectral
law.

## 15. Corrected off/off elliptic theorem — EXACT + EXTERNAL-THEOREM

Every generic class has a coherent reducible fibre of exact size `2p-8`.
After extraction, Igusa monodromy and Deligne/Fouvry--Kowalski--Michel
quasi-orthogonality give

```text
Var O << pE_+(A)+K^2p+K^4sqrt(p)+K^4.
```

Thus the elliptic layer is governed by the same Cayley-energy bottleneck.

## 16. Exact trace-to-local-statistics bridge — EXACT

For an `N x N` unitary matrix, partition-lattice Mobius inversion expresses
distinct-index exponential sums through products of traces. Poisson summation
then gives microscopic factorial statistics as weighted sums of those trace
products. In particular,

```text
C_(2,N)(U;phi)
 =N^(-2) sum_m phihat(m/N)(|Tr U^m|^2-N).
```

Band-limited microscopic tests require trace powers `|m|=Theta(N)`.
A weighted Heisenberg-scale joint-trace comparison with the target RMT ensemble
is sufficient for the corresponding band-limited microscopic theorem. For
positive normalized averages and a reference Schwartz limit, comparison on
**every** compact Fourier support extends automatically to all Schwartz tests.
The proof uses a positive band-limited majorant and uniform translated-cube
bounds; see `bandlimited_correlation_extension.md`. The required dynamical
Heisenberg-scale estimates remain **OPEN**; a fixed Fourier cap is insufficient.

See [`trace_to_local_statistics_bridge.md`](trace_to_local_statistics_bridge.md).

## 17. Verification and adversarial controls

Promoted finite controls include:

- `(K,p)=(29,728017)` and `(31,1042903)` with `p>K^4` but positive excess;
- `(K,p)=(41,2908049)` with a row pair sharing two parameters;
- `(K,p)=(31,1303)` with inverse intersection size `4`;
- `(K,p)=(131,F_131)` with exact excess `32`;
- C++20 characteristic-zero intercept regression through an extended prime
  anchor `K=809`;
- inverse translated-resultant/Smith anchors through `K=23`;
- minimal-extension controls
  `(K,p,f,Delta)=(7,13,2,32),(11,43,2,128),(13,3,3,432),(13,5,4,496)`.

Finite computation proves only its explicit finite statements.

## 18. Current frontier — OPEN

The arithmetic chain is

```text
common split divisors of small cyclotomic scalar systems
        -> pointwise centered Cayley energy
        -> complete fourth-moment control.
```

A sufficient target remains, for example,

```text
P_split^+(Lambda'_K^(3))<=K^(4+o(1)),
```

or an equivalent theorem for `Omega` / inverse `Theta` support.

The microscopic chain is independently

```text
Heisenberg-scale desymmetrized joint traces
        -> correlations at every compact Fourier support
        -> Schwartz correlations by positivity and occupation bounds.

The dynamical trace comparison is open; the extension arrow is proved.
Spacing/process conclusions require their own stated hypotheses.
```

Full microscopic universality remains **OPEN**.

## Magnetic quotient: restricted global law (2026-09-05)

See [the complete proof](magnetic_quotient_semicircle.md). Exact: geometric
antiunitary, orbit-basis equivalence and all-order signed trace histograms.
Derived under explicit hypotheses: quantitative even-moment L2 bounds and
global semicircle convergence for prime K=o(log p). Not derived: fixed-cat-map
or microscopic BGS universality. Equation (21) proves the fixed-map obstruction.

## Pell Floquet normal form and recurrence spectrum (2026-09-05)

The [self-contained proof](pell_floquet_normal_form.md) establishes an explicit
normal form for the actual fixed-map cosine-kicked propagator: odd normalized
HS error at most 12 epsilon^2/sqrt(K), for every real epsilon and odd prime
K>=11, with composite Pell moduli allowed. At epsilon=tau/sqrt(2K), the
K-th power has wrapped normal eigenvalue law, with Fourier coefficients
exp(-m^2 tau^2/2). Subcritical folded phases have a W2 Gaussian limit under
epsilon sqrt(K)->0. These are project proofs, not externally refereed or
fully Lean-formalized results; priority and microscopic BGS remain open.

The corrected fourth-moment decimal is 5.614220692151198071627965... . A
separate integer-interval verifier certifies it without floating point.

## Compact-test microscopic obstruction in the Pell family

Section 7 of `mathematics/pell_floquet_normal_form.md` proves a negative
microscopic consequence under global mean-density unfolding of the complete
odd space. For every fixed L and finite nonzero tau=lim epsilon sqrt(2K),
liminf C_d(phi_L)>=Theta(tau)-1/L and liminf Var N_L>=L^2(Theta(tau)-1),
where Theta(tau)=sum_m exp(-m^2 tau^2)>1. Subcritical tau->0 gives divergence
of every such fixed-L pair statistic. Therefore a bounded clustering pair
limit requires |epsilon|sqrt(K)->infinity. Compact tests avoid any hidden
Schwartz-tail assumption. No sufficient condition for positive universality,
no density-adapted unfolding result, and no further-sector result is claimed.
The forty finite configurations are checked independently by pair sums and
moving-window integration; they are evidence about implementation, not the
proof. Priority and analytic Lean formalization are not established.
