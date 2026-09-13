# Intensity loss and unfolding: research and proof review

Checkpoint: return-local-limits, 13 September 2026.
Base: 26fa76b8eeb6d1259381474372b40e161383f219.
Authoritative proof: [return_trace_obstruction.md](../mathematics/return_trace_obstruction.md),
Theorem 3, its sharpness construction, (S22), (S24), and (S25)--(S26).

## Verdict

**Proved as written**, for the internal abstract-spectrum statements, after
adversarial self-review. This is not independent external review or a Lean
certificate. Cat-map consequences are **conditional on the existing project
harmonic return theorem**, whose full analytic proof was not re-audited here.
External priority is unverified; the positive BGS goal remains open.

For a deterministic limiting folded law $\mu=\rho\,dy+\mu_{\rm s}$ at
$K_D=o(D)$, the conditional local intensity obeys $h\le\rho$ even when
first moments escape. An ergodic local limit of intensity $\alpha$ requires
$\alpha\le\operatorname*{ess\,inf}\rho$. Every admissible value is realized
by an explicit simple-spectrum construction. A smooth positive prescribed
return density also admits lattice, Poisson, and sine limits after its
own local-density unfolding. These constructions are not quantizations of
the maintained classical map.

## Dependency chain

1. Finite origin-averaged intensity one gives local tightness.
2. The slow mark is unchanged by a limiting local translation.
3. The marked first-moment measure is translation invariant and absolutely
   continuous in the uniform mark.
4. Truncation and the finite convolution identity give measure domination,
   rather than an equality requiring uniform integrability.
5. Ergodicity makes the invariant coupling a product and gives the sharp cap.
6. Hidden clouds carry the residual folded law while their origin-hit
   probability vanishes; the surviving background specifies the local limit.
7. Density transport uses both a local dilation and the origin Jacobian.

The general chain has no free-probability input. The free Brownian support
formula is an external leaf only for (S24). The CUE kernel limit and
ergodicity are external leaves only for the sine starting example in (S26).
Their exact source versions and normalization are in
[the source record](../literature/return_local_limits_sources.md).

## Adversarial obligations

| Obligation | Outcome |
|---|---|
| Multiplicities, random spectra, and a fixed deterministic limit law | Passed: counting measures allow multiplicity; weak convergence in probability of bounded folded tests implies convergence of expectations |
| No hidden preservation of intensity | Passed: bounded truncation proves only $h\,dy\le\mu$ |
| Singular return mass | Passed: it cannot supply the absolutely continuous marked first moment |
| Whole process versus a finite empty window | Passed: a countable increasing family of windows identifies the empty process |
| Ergodicity with intensity below one | Passed: product coupling gives constant conditional intensity |
| Sharpness for every admissible alpha and every K=o(D) | Passed: K times a diverging number of quantile centers is still o(D); cloud multiplicity rounding has vanishing total error |
| Simple-spectrum requirement | Passed: distinct cloud levels can be chosen in finite nonempty arcs, avoiding all existing levels |
| Macroscopic equidistribution when K grows | Passed: averaging the K translates is a uniform Riemann sum |
| Uniform origin after unfolding | Passed: reweight by rho before applying the local dilation |
| Zero-density points in the unfolding theorem | Out of scope: (S25)--(S26) require a fixed strictly positive C1 density |
| Free endpoint t=4 | Out of scope: (S24) uses the strict support-gap range 0<t<4 |
| Full local limit of the cat map | Not addressed: an empty ergodic subsequential limit is not convergence of the whole sequence to empty |
| All-orders microlocal quantization class for constructed spectra | Not asserted |

## Routes and what changed

The density-transfer route closed an actual implication: the weighted
dilation formula (S25) identifies the change of local process, not merely
of the folded empirical measure. Its inverse proves non-identifiability of
unfolded local statistics from all fixed return moments.

The intensity-loss route removes the earlier intensity-one hypothesis and
gives an exact compatibility range, with constructive sharpness. At the
harmonic free endpoint this forces a positive empty component for 0<t<4,
and hence an empty limit whenever that limit is ergodic.

The analytic-resonance route was checked against the maintained bracket
rigidity and Wiener-stability proofs. Pointwise-zero cancellation is already
excluded for analytic symbols, but a nonzero analytic dynamical coboundary
remains possible on the current evidence. The finite-core bound supplies
no lower witness margin for every analytic function. No claim in that
separate open problem was advanced or silently closed.

The Heisenberg-scale route remains missing. For example the harmonic
absolute expansion error in (R9) is exp(2mK delta)/(N-1), with
delta=abs(tau)/sqrt(2K). At m of order D/K and fixed nonzero tau,
this bound grows exponentially in D/sqrt(K); it cannot be used as a
vanishing error. Positivity of the new obstruction does not repair that
loss of cancellation.

## Finite execution

[return_local_limits.py](../computations/verification/return_local_limits.py)
passes 144 exact rational origin-window cases for D=24,60,180,480,
K=1,3,7, alpha=0,1/3,2/3,1, and L=1/2,1,2. A direct interval-midpoint
enumerator independently agrees with the event sweep on all 36 D=24 cases.
The checks retain finite mean count L while the void probability approaches
that of the lower-intensity background.

Separate float64 controls check inverse-density transport at D=256,1024,4096,
four folded moments per dimension, the indispensable origin Jacobian, and
three finite CUE kernels. They are not interval certificates or simulated
cat-map evidence. Omitting the Jacobian gives mean 5/12 rather than 1/3 in
the explicit negative control.

The support-gap derivative and leading endpoint coefficient were checked
symbolically in SymPy and independently in the connected Wolfram evaluator.
The exact Wolfram input is retained in
[return_gap.wl](../computations/verification/return_gap.wl).
Both give coefficient 1/(6 pi) and numerical gap values 0.3910022189557706,
0.1816901138162093, and 0.0576688856224373 at t=1,2,3.

The maintained figure displays analytic lower bounds, not finite spectral
fits. The original full Python/C++ suite and Lean tree were not rerun;
no new analytic formalization is claimed.

## Next executable scientific obligation

Identify the conditional local law of the actual kicked propagator after
removing its return-density profile, or establish a dynamical estimate
which distinguishes it from the abstract inverse-density examples.
For a positive BGS theorem this still requires the appropriate fixed
classical regime, symmetry block, and Heisenberg-scale trace comparison.
The abstract compatibility theorem is complete in its stated scope; these
dynamical implications are not.

## Publication execution checkpoint

The bounded computation runner completed and its manifest validator passed.
The focused workspace run passed both return verifiers. Structural and
Markdown-to-TeX synchronization gates passed. The canonical manuscript built
to 222 pages without rejected reference or horizontal-overflow warnings.
New-content pages 97, 98, and 102 and the updated figure were visually inspected.
The saved PDF was retrieved: full text matches the build, and the last page
renders. Binary delivery differs, so byte-identical delivery is not asserted.

Verifier SHA-256: 695032a287cdb2f3ce0672902be91f599f3abd0211087d034c1b3446e16f09da.

Local PDF SHA-256: 55db5ab50797d13e9cc9e654320d9b9615d87cdc42292d82d9b5a784e9c00202.

Delivered PDF SHA-256: 5bc267a581344ad98b672a98fd1050aaabb0385a48e040f6c1113095bdb78884.

Generated execution files remain under build/return-local-limits-audit/ and
build/return-local-limits-focused/; the article manifest is under
build/return-local-limits-paper/. This records focused execution, not a
full historical proof audit or full Python/C++/Lean rerun.
