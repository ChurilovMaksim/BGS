# Uniform-step continuation and adversarial author audit

Checkpoint: `coboundary-joint-20260930`, based on local main
`ab3a6587a9bcc5c08370cd50f546638a132cd9f6` (tree
`79fe3096b36d885d1e9782c17bc0775f8c9fc766`). At the initial remote read,
main was `c11f45165c9dc2fdb720ec783aa94eba348a148e`: the 29 September
FLOW-008/009 continuation had not yet been uploaded. This continuation
integrates that pending work together with the checked extension.
No subagents were used; all mathematical reviews are author self-review.

## Outcome and original goal

**BGS-FLOW-010: proved as written, project proof with author self-review.**
For the original uncentered independent Gaussian coboundary chain from
an odd clock, the small-step and large-dimension limits can be taken
jointly at the explicit step $\varepsilon_N=e^{-N}$. If $t_N\to0$ and
$Nt_N\to\infty$, its phase-averaged local weak law tends to Sine$_2$.
For smooth nonnegative compactly supported tests, the choice
$t_N=N^{-2/3}$ has error $O_f(N^{-1/3})$.

The original BGS goal is **not reached**. This is an extension of the
random-chain result, not a theorem about the deterministic frozen map.
The exponential step count is a serious quantitative limitation.

The [maintained proof](../mathematics/coboundary_joint_limit.md) gives
the full intermediate bound, independent of dimension:

$$
C_f[\sqrt t+(Nt)^{-1}+N^{-2}+N^{20}e^{CNt}\varepsilon].
$$

## Mechanism and dependency closure

The gain is a uniform control of the fast first trace. Exact cancellation
of its linear kick term gives a Gaussian gradient of size
$O(\varepsilon^2/\sqrt N)$, hence centered increment moments
$O_k(\varepsilon^2/N)$. The stable quadratic mean and its full quartic
coefficient give stopped first-moment scale
$O(\varepsilon/N+\varepsilon^4)$. The absolute sixth-order forcing is
retained; higher means are not assumed to vanish on the centered slice.

Smooth localization, the covariance square root on the **traceless**
Hermitian space, and SDE variations give backward derivative growth
$e^{CNt}$. A discrete nonnegative second-trace Lyapunov bound controls
exits directly. This avoids a killed-boundary PDE and any uniform
regular-value assertion. Matrix Fourier tests remain smooth at collisions.

Dependencies: FLOW-003, FLOW-004, FLOW-007, FLOW-008, FLOW-009. The
Forrester Dyson-clock leaf is the already pinned and checked dependency
of FLOW-007. No new external theorem is inferred from a search abstract;
FM-013 remains conditional and is not used.

## Adversarial review

Primary verdict for FLOW-010: **proved as written** within its stated
random-chain scope. The fresh audit of FLOW-008/009 also found no failed
implication in their stated fixed-dimension/iterated scopes. These verdicts
are self-review, not independent referee approval.

| Obligation | Disposition | Reason |
|---|---|---|
| Exact chain and time convention | Passed | Original uncentered step; spectral-equivalent conjugate only for class tests; $h=\varepsilon^4/2$. |
| Uniform Gaussian input | Passed | Sphere-net operator moments and Gaussian rotation proof of centered gradient moments. |
| First-trace fourth mean | Passed | Full formula $P_4$; exact rational all-word contraction independently reproduced. |
| Higher-order bias | Passed | An absolute $O(\varepsilon^6)$ remainder creates the retained $\varepsilon^4$ equilibrium scale. |
| Long step-count moment control | Passed | Conditional $2p$ contraction, killed moments, $p=3$ union bound over $O(\varepsilon^{-4})$ steps. |
| Fast generator removal | Passed | Exact Möbius invariance of lifted rotation-invariant tests, not merely small drift. |
| Uniform square-root regularity | Passed | Restricted to the fixed traceless space; $N\mathcal C$ stays elliptic on the localized chart. |
| Derivative dimension accounting | Passed | Noise derivative energy $O(N)$, drift derivative size $O(N)$; six variational orders give $e^{CNt}$. |
| Boundary handling | Passed | Direct discrete Lyapunov exit bound and bounded backward tests; no stopped-process convergence used in the joint theorem. |
| Microscopic test derivatives | Passed | Fourier trace expansion gives $C^6$ norm $O_f(N^{12})$ without inverse gaps. |
| Quantitative rate versus weak limit | Passed | Rate only for smooth tests; $C_c^1$ weak limit by uniform $L^1$ approximation. |
| Unknown absolute constant | Passed | $e^{-N}$ dominates $e^{CNt_N}$ for every fixed $C$ because $t_N\to0$. |
| Deterministic BGS / polynomial step | Not addressed | Neither follows from external-noise relaxation at an exponential step count. |
| Independent review / Lean | Not addressed | No such validation was performed. |

The power 20 is checked by a loose budget: at most $N^4$ in the weak
generator error and $N^{12}$ in the microscopic test, with smaller exit
and time-rounding terms. It is not obtained by fitting finite data.

## Actual finite execution

The [new verifier](../computations/verification/coboundary_joint_limit.py)
uses exact Fraction arithmetic for all 16 four-letter words and the
three Wick pairings. It reproduces the five coefficients of $P_4$, with
the common nonplanar $m_1/N^2$ term cancelling exactly. Independent
complex128 matrix contractions at $N=3,4,5,7,9$, clock and perturbed
spectra, have maximum error $1.39\times10^{-17}$.

Full real Hermitian-basis Frechet gradients of the **actual** single
exponential, at steps $.01,.08,.25$, obey the analytic gradient bound
in all 30 tested cases; the largest ratio to the deliberately loose
bound is 0.111. These finite cases check algebra and implementation,+not a uniform theorem or a simulated joint limit.

The earlier FLOW-008/009 verifier was also rerun unchanged. Its Wick
maximum error remains $4.72\times10^{-16}$ and projection Hessian
maximum error $5.59\times10^{-8}$. Its output still embeds its original
29 September protocol date; the new manifest records the actual
30 September re-execution and does not rewrite the old evidence.

Fresh evidence is under `evidence/20260930/`. The accompanying integration
object records the structural checks and manuscript build actually run.
Neither full historical regression nor page-image review nor formal
compilation is claimed.

Fresh structural checks passed: scientific registry (50 claims, 16 external
dependencies), repository audit, registry rendering, fixed-map and
finite-orbit manuscript synchronization, and `git diff --check`.
The three-pass consolidated manuscript build passed at 239 pages;
PDF SHA-256 is
`0d562966bd46729128fdaad9053a32484a69ab1efaea1154221fdfc382f0ba70`.
These checks validate consistency and compilation, not analytic truth.

## Route state and next discriminating task

1. **Uniform simultaneous stochastic limit:** the explicit exponential
   regime is closed by FLOW-010. Polynomial steps remain open; a useful
   continuation must improve the semigroup stability or compare local
   observables directly, rather than assume bounded microscopic derivatives.
2. **Actual-map relaxation input:** still open, including the exact
   regularized-trace/quantization match in FM-013. Its hypotheses were not
   supplied by the clock theorem.
3. **Deterministic transfer / BGS-TRACE-005:** still the central target.
   The clock's changed local law refutes generic noise removal. Resume with
   a model-specific Heisenberg signed joint-trace estimate or microscopic
   approximate stationarity input; collective centering alone is insufficient.

Literature searches inspected current primary metadata, including the
semiclassical BGS papers and recent quantum-chaos applications. They
supplied no checked replacement for the missing deterministic estimate.
This bounded search is not an exhaustive priority determination and is
not evidence of a world-first result.
