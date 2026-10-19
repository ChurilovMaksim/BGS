# Adversarial self-review of the new continuation

17 October 2026. These are author checks, not an independent referee report.
No new agents were used. The submitted file's own reports of prior checking
are not substituted for the checks recorded here.

## Classical all-size compression

* The matrix need not be normal, reversible, or unistochastic. Row AND column
  stochasticity are used; the row/column l2 bounds for P-J are both required.
* The internal inverse exists from the singular-value gap, not an unsupported
  eigenvalue-only bound on a nonnormal restriction.
* The zero-sum right-hand side is extended by zero before applying the full
  Green inverse. Centering on A then proves the exact compressed inverse.
* The identity K-J=Q M_AA(I-K) uses column stochasticity to remove the right
  Q, and the column l1 norm of I-K is exactly 2(1-K_jj). No small block norm
  or Neumann inversion of M_AA is assumed.
* For the return clock, r=1+h is nonnegative and has total mass N. This is
  what makes the entrywise M bound give a constant per-port error.
* Singleton A and empty E are covered; exact controls include both cases.
* Classical K is not quantum ET. The exact S4=23/45 control prevents that
  false inference. The generally nonnormal rational tests cover 498 subsets.

## TV compactness

* G is retained as a hypothesis. Its use includes reversed directions and
  eighth moments, not only disjoint off-diagonal Gaussian probes.
* G for EVERY diverging u=o(N) is essential in the diagonal-sequence step.
  A logarithmic lower cutoff tied to N would not give the same double limit.
* A nonzero complex minor is chosen at zero, its numerator is a nonzero
  polynomial, and its torus zero set is null. Complex independence implies
  real independence of the angular derivatives; the target tangent dimension
  is m^2, rather than 2m^2.
* Parameter-TV continuity is proved locally in fixed phase coordinates.
  Smooth cutoffs are independent of W; they capture at least 1-epsilon input
  mass. Fixed compact cutoff supports and a nonvanishing Jacobian give L1
  convergence after change of variables. The omitted mass is uniformly charged.
* Compactness is in the L1 norm. Its closed convex hull is norm compact by
  finite epsilon-net approximation and completeness. Weak compactness alone
  would be insufficient.
* The conclusion applies to N->infinity cluster measures. Finitely many
  early singular distributions do not become AC by assertion.
* Scalar Poisson laws approaching a point show TV continuity fails at a
  degenerate rank point. The theorem uses a compact rank lower bound.
* Marked columns are measurable-kernel images of larger fixed-level laws.
  First clock moments converge to one because the limiting cavity is AC.
  This justifies uniform integrability and W2, but no higher clock moments
  or Haar conditional isotropy are inferred.

## Positive Bernstein path law

* Every product coefficient is formed coherently before its modulus is squared.
  Ordered tensor entries have binomial multiplicity; this gives exactly the
  Bernstein marginal and total mass one.
* The factor 1/2 in the clock is obtained by averaging the two incoming
  columns. A single unspecified column need not have that clock.
* Tensor differentiation gives K times the column clock on the unitary
  boundary. Squared derivative energy would be a different quantity and
  could introduce a false K^2 factor.
* Hardy projection uses analyticity to exclude downward degree leakage and
  norm <=1 of the vector multiplier. It works uniformly over K.
* The short path bound includes degree zero. The long tail uses the actual
  degree-weighted positive mass; dark modes reduce its upper bound.
* The normalization in the retained window is only used when epsilon<1.
  Its TV distance from the original grid marginal is at most the discarded
  mass, without a hidden inverse surviving probability.
* The binomial coupling is only a coupling of the k-marginal. No coupling
  or independence of the path length with the original T is assumed.
* The logarithmic rate is W1 ONLY. A discrete grid and a continuous uniform
  law have TV distance one even as their W1 distance tends to zero.
* The beta kernel is symmetric and Markov and preserves the uniform density.
  Continuous-function approximation plus L1 contraction proves strong L1
  approximation. Finite nets make it uniform on compact L1 families.
* The extension to asymptotically TV-compact measures uses AC cluster points,
  not the false claim that a smoothing converges in TV to a delta measure.
* No quantitative TV rate follows without a modulus for that compact family.
  The explicit one-variable negative control has mean T=4/5, so positivity
  and the exact clock do not themselves select the uniform target.
* The resulting polynomial density is on a fixed two-channel observable.
  It does not provide the needed low-degree approximation on a growing U(v).

## Remaining mathematical risk and frontier

No fatal error was found in these new analytic arguments
under their stated assumptions. This is not a claim that every auxiliary
classification theorem or numerical table in the 850KB attachment has been
independently certified. The attached auxiliary routes retain their source
dependencies; unrerun numerical evidence stays diagnostic.

The central unproved estimate is the L1 convergence of the explicit positive
path density to one, or its unconditional W1-grid counterpart. It requires
coherent cancellations at internal lengths of order N. Neither exact mass,
first clock, classical compression, compactness, nor finitely many Gaussian
moments evaluates those coefficients. Full BGS and the two-channel theorem
are therefore left OPEN in the checkpoint.
