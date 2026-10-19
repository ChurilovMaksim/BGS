# Adversarial author review, 17 October 2026

This is a separate self-review, not independent-agent or external review.
The repository and the submitted attachment remain unmodified.

## Primary verdicts

1. Fixed finite colligation tensor-current limit: **proved as written** by
   the explicit characteristic function, a.e. differentiability, domination,
   and equality of finite first moments. Optional second-moment and rate
   formulas retain their stated integrability conditions.
2. Full-clock simultaneous K_N,N transfer: **conditional on [TC]**. The proof
   of the implication [TC]=>theorem (3) is complete here. The previous result
   supplies [TC] under rank condition R/full growing-channel input G, whose
   own project-local one-step dependencies were pinned but not re-proved here.
3. Rare star lower bound and bounded radial examples: **proved as written**,
   using the classical correctly normalized Ginibre trace identity. The
   auxiliary example is not unitary and does not refute BGS.
4. Full BGS/two-port universality: **incomplete**. Neither E T_N->1/2 nor the
   finite positive histogram defect e_N->0 has been established.

## Dependency graph

    finite unitary Schur rule -> positive tensor H2 law
      -> characteristic function -> fixed-V W1 limit
    finite source-averaged Kac identity -> uniform conditional kernel moment
      -> TV-input/W1-output Lipschitz bound
    [TC] + both previous arrows -> all fixed marked occupations uniformly in K
      -> marked UI + exchangeability + finite-population sampling
      -> entire normalized path clock and positive finite-window result

For the Haar reference calculation only: prior exact cavity density/mixture
MC16--MC24 -> projected Gaussian squared norm -> inverse Gamma(m+1).
This benchmark is not used in proving the general transfer.

    exact rooted-star enumeration + Gaussian h_(N,m)
      -> rare-event probability exponent
      -> divergent exponential Wick weight and radial lower bound
    positive Gaussian quadrature + finite moment perturbation
      -> bounded laws matching any finite Gaussian radial moment list

## Obligation matrix

| Obligation | Status and decisive check |
|---|---|
| Rooted rather than cyclic-equivalence word count | Passed: two parities and multinomial leaf arrangements; no extra factor m |
| Distinct hub count | Passed only for k>=2; k=1 explicitly excluded and exact double-count negative control included |
| Gaussian normalization for m>=N | Passed: kernel/hook continuation in pinned source proof; exhaustive small checks include m>=N |
| All coefficients after circular entry averaging positive | Passed: edge tables match independently; no signed-unitary conclusion |
| Threshold optimization | Passed: derivative sign in (12), minimum alpha=2s-1; threshold is construction-specific |
| Positive exponent signs | Passed with rational integer inequalities; numerical logs are descriptive only |
| Arbitrary finite moment matching and positivity | Passed: positive quadrature nodes/weights proved; perturbations leave all original masses >=w_i/2 |
| Shift sign and output binomial/multinomial factors | Passed: Parseval uses f(phi+theta/K) conjugate f(phi); K=1 controls and exact K<=6 sums agree |
| Boundary poles and dark channels | Passed in proof: poles null; unobservable dark channels have zero current; one-variable clock degree 0 or 1 |
| First derivative integration | Passed by one-variable positive clock and tensor Kac, not by an unproved L2 derivative bound |
| Fixed-V weak to W1 strengthening | Passed: nonnegative coordinate norm and exact finite norm-first-moment equality |
| Uniform K_N limit | Passed under [TC]: finite TV net plus a pointwise kernel limit and UNIFORM CONDITIONAL moment bound |
| Unbounded output under input TV coupling | Passed: (6) holds for every input V; residual input mass delta costs at most (2+q)delta |
| Association of marked coefficients with reduced matrix | Passed: rational Schur associativity + iterated Parseval + Tonelli |
| Uniform integrability | Passed: derived from W1 compact kernel images, not from a bounded mean alone |
| Growing number of marks | Passed for the AVERAGE: finite-population sample error and UI; no matching-sum CLT inferred |
| Conditioning on a time window | Passed: discarded first clock moment controlled by UI, with explicit residual coupling (14) |
| Haar current clock concentration | Rejected: inverse Gamma(3) reference has variance 1/4 |
| Haar identification from [TC] | Not proved and false without further hypotheses; coherent optical families in the attachment are controls |
| Identification under full original flatness/gaps and G | Open: new theorem transports an unknown joint endpoint/current law |
| Finite computations as universal proof | Explicitly not claimed |

## Checks actually run

star_run/: 25 exhaustive (N,m) cases, 629171 rooted words, exact full Gaussian
normalizations, three complete star sectors, radial moments and exact sign
tests. No Monte Carlo. All passed. Finite logarithmic rate tables are not
used for signs or asymptotic assertions.

current_run/: 12 rational-inner source/K cases and 72 exact identities.
Complete infinite coefficient sums use polynomial-times-geometric tails;
the references use low-degree contour residues independently. Two hundred
polynomial cases check binomial normalization and source clocks. All passed.
No finite Taylor cutoff, numerical phase integral or random sample is used.

Both execution manifests passed the mathbox validator with current input and
output hashes. Inputs were not edited after their runs. No Lean compilation,
C++ verification, Wolfram call, full-repository build or independent referee
review was performed during this continuation.

## Remaining risks and exact next mathematical decision

The new full-clock theorem needs [TC]. To advertise it unconditionally under
the original deterministic assumptions requires the entire pinned G/rank/TC
dependency closure to pass its own audit; this continuation does not provide
that certification by repeating its conclusion.

The central next problem is to identify the endpoint marginal of (T_N,J_N),
or its equivalent finite positive histogram. Independence from the current,
Gaussianity of cavity directions and the inverse-gamma clock law cannot be
substituted as assumptions without labeling the result conditional.

For the auxiliary Wick route, blanket exponential UI for arbitrary parameters
is now ruled out analytically. A possible small-tilt integrability regime and
the full tilted free energy remain open, with the explicit star lower bound
as a mandatory control. None of that evaluates the signed physical trace.
