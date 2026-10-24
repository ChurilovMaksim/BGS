# Closure of the inserted-trace and global spectral-distance inputs

Final self-review: 22 October 2026. Parent checkpoint: main
`2271f00b17b2480f8f833fe55754a55c1b8c8bde` (tree
`e9b9cd628f96704e1e731806995eb414409908eb`). Work started on 21 October.
The original fixed-coupling microscopic hierarchy and BGS remain open.

## 1. What changes mathematically

| Claim | Previous status | Current result and reason |
|---|---|---|
| TRACE-109 | Conditional numerical asymptotic application | Proved by a finite-grid, one-step parametrix retaining $B_0+hB_1$; no all-time sector construction is needed |
| TRACE-110 | Conditional on uniform physical trace input (T) | Proved global spectral bounds; (T) is closed by TRACE-113, and an independent upper-bound proof is supplied by TRACE-112 |
| TRACE-112 | New maintained claim | Uniform classical displacement density, a logarithmic-time quantum trace saving and $O(1/\log N)$ global spectral matching |
| TRACE-113 | New maintained claim | One threshold $N_0$ and $1<a<\sqrt{3+2\sqrt2}$ with $|\operatorname{Tr}U_N^m|\le Ca^m$ for every $m\ge1$ and every odd $N\ge N_0$ |

These are analytic proofs with adversarial self-review. The published external
classical input is checked separately; there is no new external referee,
fresh-agent certification, Lean proof or world-priority claim.

## 2. Executed routes and the exact mathematical moves

### A. Finite-grid insertion, closed

The leading four-sheet approximation has Hilbert--Schmidt error
$O(N^{-1/2})$ and would allow $O(1)$ trace error. The additional amplitude
solves one inhomogeneous transport equation. Its entry residual is
$O(h^2/\sqrt N)$, and unitary Duhamel gives matrix error $O(N^{-3/2})$.
Consequently the original and inserted traces have $O(N^{-1})$ error.
Poisson summation includes every discrete alias; deck permutations handle
wrapped grid shifts and overlapping coordinate cutoffs. The four exact
stationary classes give the unchanged protected monodromy constants.

[Complete finite-grid proof](../../mathematics/finite_grid_one_step_trace_20261021.md).
The quantum commutant and two-copy consequences in TRACE-109 therefore
retain their numerical constants unconditionally.

### B. Gaussian scalar and pressure, closed at the stated scope

The earlier all-time argument was read at its exact comb normalization,
translation-uniform Gaussian summability, Abel composition, saturated contour,
trace-class convergence, past/future graph splitting and zero-order Gaussian
period normalization steps. A complete audit map is in
[TRACE-113](../../mathematics/fixed_kick_uniform_trace_bound_20261021.md).

The simplification is to use only $\gamma_h\to\gamma_0$ uniformly.
It gives per-edge log-modulus error $\epsilon(h)\to0$. Since the actual
classical pressure gap $\Delta>0$ is fixed, one choice
$\epsilon(h)\le\Delta/4$ works for every iterate. No quantitative
$O(h^2)$ expansion, parity argument or differentiated repetition remainder
is needed for this claim. The zero-order normalization still uses exact
Gaussian repetitions, whose residual is exponentially bounded.

The Bowen--Ruelle source was authenticated and its theorem formulas visually
checked on printed pp.187,189--190,192. The actual smooth constant-roof
suspension satisfies the basic-hyperbolic-attractor hypotheses. Mixing of
that flow is not assumed. The fixed multiplier strictly exceeding
$3+2\sqrt2$ forces the pressure gap by the Gibbs/volume contradiction.
[Source record](../../literature/bowen_ruelle_trace_closure_20261021.md).

### C. Independent upper bound and attempted falsification

An anisotropic Fourier operator for the actual classical map differs in trace
norm from the linear operator by $\epsilon_R<10^{-56}$. The linear
nonconstant powers have zero diagonal. Exact telescoping improves the
displacement-density estimate to

$$
\|q_m-1\|_\infty\le\epsilon_R m(1-1/8000)^{m-1}
\le8\cdot10^{-53},\qquad m\ge1.
$$

The proof uses finite Fourier compressions to justify telescoping the
unbounded weights; it does not assert a bounded similarity on $L^2$.
This density gives a uniform two-dimensional displacement sublevel bound.
Fixed-character Egorov and positive-square localization then give
$|\operatorname{tr}_N U_N^m|\le Ce^{Km}N^{-1/5}$, and hence a uniform
power saving on a sufficiently short logarithmic window. Squared Fejér
kernels yield global discrepancy and sorted spectral matching of order
$1/\log N$, without the all-time quantum/pressure route.
[Full proof](../../mathematics/displacement_density_trace_bound_20261021.md).

The four stationary aliases, their exact action residues, actual Fourier
Hessians and Jacobian normalization were recomputed as discriminating tests.
They reproduce the claimed signs and constants, rather than yielding a
physical counterexample. The bare-coupling and arbitrary-kick countermodels
from earlier work remain different mathematical families.

## 3. Verification and its limits

`trace_closure_checks.py`, run with `python3 -O`, uses exact rational Fourier
algebra and explicit exceptions. It checks four stationary classes, 49
canonical Hessian cases, 2737 exact Gauss matrix entries across 49 odd dimensions and the error exponents.
The first draft used Python's negative integer power of `-1`, which produces
a float; its equality check failed. Replacing sign powers by parity restores
exact rational arithmetic. This was a verifier implementation defect, not a
change to the theorem or its constants. The fresh evidence records the fix.

These checks do not certify analytic convergence, pressure or the asymptotic
theorems. Source parsing, dependency/registry consistency, the mandatory
finite-orbit synchronization and the manuscript build have separate receipts.
The historical 56-check packet and original source archive remain unchanged.
Current governance summaries and generated navigation were aligned with
`SOURCE_OF_TRUTH.md`: registered status is controlled by `claims.json`, and
the dated ledger records its interpretation and additional scoped results.
This resolves inherited contradictory authority descriptions; it promotes no
additional historical claim.

## 4. Remaining physical task and handoff

For the fixed admissible band-two test, the full signed off-rotation sum must
still supply $-\delta_*$, $\delta_*>0$. The new all-time exponential bound
is useful before and around logarithmic times and becomes larger than the
trivial bound at times proportional to $N$. The independent Egorov route has
the same logarithmic boundary. Neither evaluates the fixed pair defect or
its higher factorial analogues.

An executable continuation is to estimate the signed cross-orbit contribution
in the exact scalar-cocycle representation, including its nonzero plateau
correction. Repeating positive classical displacement bounds or replacing the
complete remainder by $o(1)$ will not supply that term. This route remains
open; it is not declared exhausted. The original BGS goal is not reached.

Two inherited manuscript overflows were corrected by giving long file paths
proper breakpoints. Only their typesetting changed. The primary classical
source was added to the bibliography with exact theorem locators.

The bibliographic guard now selects a new 52-source snapshot: 51 old source
observations are carried forward, and Bowen--Ruelle has the fresh scoped
primary-source review. Its recorded impact is TRACE-113 directly and
TRACE-110 transitively. The previously omitted Demni-to-RET-001 registry
edge is also reflected in the new impact inventory; that bookkeeping repair
is not a fresh theorem-applicability review. The old snapshot is preserved.
