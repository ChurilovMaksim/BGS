# Reviewed Schur continuation, 11 October 2026

The preceding integration is preserved in [its own checkpoint](chat_integration_20261011.md).
This continuation strengthens TRACE-060 and adds TRACE-073. It does **not**
resolve TRACE-005 or deterministic BGS. The new results identify what can be
proved from all-time entry flatness; they do not establish that premise.

## What was reconciled

All 199 retained original research files passed a fresh byte-hash comparison.
All sixteen preceding claim additions had existing source, evidence, verifier
and manuscript paths. The registry, generated claim table, topic membership
and repository link audit passed on the preceding main commit
`4c2afe539ff6b84be907899b38c8e80f94f547e8`.

The review found stale current-summary counts in the formalization guide,
research overview, open-question table and record navigation. They now
identify the 23 active Lean modules / 26 Lake jobs of that checkpoint;
earlier counts remain historical. The source mapping for Tropp was corrected
from “block matrix Freedman” to the **scalar maximal** theorem actually used
on stopped diagonal martingales. A new metadata review preserves the previous
cache rather than silently replacing its observations.

## Accepted mathematical changes

| Claim | Result and hypotheses | Boundary |
|---|---|---|
| TRACE-060 | Uniform incoming/outgoing first-delay concentration down to `ceil(log(2N)^(1+kappa))`, conditional in intersection probability on all-time entry flatness | No estimate for the probability of entry flatness |
| TRACE-060 | Every fixed killed normalized clock moment has a dimension-independent upper bound | Order is fixed; unrestricted exceptional-event moments are not controlled |
| TRACE-060 | Uniform second/third equality laws: `Y2(u)=2-u/N+o(1)` and `Y3(u)=6-6u/N+(u/N)^2+o(1)` | Fourth and all-order equality laws remain pending; expectation convergence is for killed quantities only and additionally requires flatness probability tending to one |
| TRACE-073 | All ordered centered singular values contract under classical stochastic complementation, including nonreversible doubly stochastic matrices | The deleted-block resolvent must exist |
| TRACE-073 | Quantum fresh-phase elimination has a bounded centered coherent increment; a stopped Schatten-p potential propagates a small initial position-chain gap down to `ceil(log(2N)^(3+kappa))` | This is again an intersection-probability theorem under all-time entry flatness; an individual quantum realization need not contract |

The complete proofs are [all fixed moments and equality laws](../mathematics/all_moment_delay_bootstrap_20261011.md)
and [censoring and the quantum gap](../mathematics/schur_censoring_gap_20261011.md).
The preceding [delay bootstrap](../mathematics/delay_bootstrap_20261011.md)
remains the process/formula source; its older cutoffs are explicitly identified
as superseded by the reviewed extension.

## Mechanisms that make the strengthening possible

The clock proof expands each trace increment into rank-two cyclic words.
Positivity and spectral-moment interpolation turn a word with r insertions
into a first-diagonal factor of degree r-1 and a single lower trace moment.
The killed recurrence therefore closes at every fixed order. Convex trace
powers supply the nonnegative frozen submartingale needed to control the
high-moment cap without a logarithmic union penalty. The incoming and outgoing
barriers are proved jointly. At a crossing, the complete transition is
retained in the appropriate frozen process.

Squaring the same words gives an expected trace-martingale bracket of order
`1/m`: order k needs the already bounded killed moment of order `2k-1`.
For k=2,3, the exact drifts have deterministic contractive coefficients.
Summation by parts bounds filtered noise by the maximum of the raw martingale,
so the drift comparison does not accumulate a spurious `log N` factor.
The normalized crossing value is frozen permanently; it is distinct from
the original trace and from the killed trace.

The censoring proof uses a centered harmonic lift from the retained ports.
An exact energy identity leaves a nonnegative correction. The positive
index of the resulting quadratic form gives the **entire ordered singular
spectrum** inequality, rather than just an eigenvalue or reversible-chain
argument. In the quantum process this contraction applies to the conditional
mean. A self-contained even-p Schatten smoothness estimate then controls
fresh coherent fluctuations in a stopped convex potential. It yields a
probability bound without invoking matrix Freedman.

These two cutoffs differ: the delay theorem reaches `log^(1+kappa)`, whereas
the gap theorem reaches `log^(3+kappa)`. Neither cutoff should be substituted
for the other.

## Independent internal proof review

One separate reviewer reconstructed three analytic arguments and did not edit
the sources. This is an internal independent reconstruction, not an external
referee report or a novelty certificate. Exact reviewed inputs and hashes are
retained in the [execution packet](../evidence/executions/20261011/cavity-continuation/README.md).

1. **All-fixed-moment bootstrap:** positivity, rank-word interpolation, closed
   killed recurrences, full crossing cap, dyadic diagonal concentration and
   final parameter choices all passed. The review clarified simultaneous
   crossings and the fixed-parameter large-N threshold.
2. **Censoring and gap:** the harmonic lift, all-singular-value min-max step,
   exact quantum mean, centered noise bound, even-p Hessian bound and stopped
   potential all passed. Padding applies to the centered matrix `P_u-J_u`;
   Frechet derivatives are real derivatives of Hermitian dilations.
3. **Second/third equality laws:** the full normalization increment, squared
   cyclic words, expected bracket, Doob estimate, exact reference residuals,
   stable Euler propagation and joint first-exit closure all passed. The
   expectation conclusion is explicitly restricted to killed moments.

The pending fourth-delay and all-order Schröder candidates are
[retained separately](research_candidates/20261011/README.md); their status
has not been promoted by the preceding reviews.

## Computation and literature boundaries

Python checks 700 exact harmonic-lift identities in 140 finite cases and
19,548 exact clock-word bounds in nine noncommuting positive examples through
order seven. C++ independently checks 720 exact lift identities in 144 other
finite cases, using arbitrary-precision rationals. Floating singular values
and phase quadrature are diagnostics. Wolfram checks four finite symbolic
identities, including a Walsh feedback realization whose gap equals one
although its conditional mean is exactly uniform.

These calculations test vulnerable finite algebra; they do not certify an
asymptotic probability bound or BGS. There is no new Lean formalization of
these analytic theorems. The existing 23 Lean modules retain their prior
finite algebraic scope. The [source review](../literature/cavity_sources_20261011.md)
checks the actual scalar concentration input and records why graph
universality cannot be imported into this model merely from an abstract.
World priority is not established.

## Remaining decisive obligations

The new results remove a conditional clock/gap bottleneck. They leave the
all-time entry-flatness probability, higher equality laws, complete scalar
microscopic cavity law, signed all-order Heisenberg trace comparison and
removal of auxiliary randomness unresolved. In particular, the chain's
conditional mean mixing is not sufficient: the Walsh example explicitly
separates it from realization mixing. No result here turns classical chaos
alone into microscopic universality for all chaotic systems.

Fresh final verification and source-bound build evidence are recorded in the
[packet](../evidence/executions/20261011/cavity-continuation/README.md), with
older receipts kept at their original source scope.
