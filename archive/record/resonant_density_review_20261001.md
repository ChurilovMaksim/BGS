# Research review: resonant cubic density and a critical tail obstruction

Date: 1 October 2026. Work without subagents. Review level: author
self-review, independent exact representations and finite adversarial
controls; no external referee or new Lean compilation.

## What is actually closed

[BGS-TRACE-011](../mathematics/resonant_cubic_density_control.md) proves
three subsidiary statements, without changing the frozen map or its coupling.

1. For every complex compact smooth positive-cone weight, the complete
   signed union of the strips d dividing m, n or m+n is bounded by
   $C_W\sqrt{E_N M_4(N)}$. This replaces the older
   $3\|W\|_\infty Q_N\sqrt{|R|E_N}$ budget under an explicit density
   condition. The modulus stays outside the signed sum. The full factorial
   counterterms have a separate exact finite budget.
2. Any bounded local occupancy moment of order s>3 suffices with E->0;
   at the critical order 3, uniform integrability of the positive smoothed
   density cubed suffices. A bounded third moment alone does not.
3. Rare periodically aligned clusters give a realizable sharp obstruction.
   With N=dq^3, cluster size dq and q-fold d-clock clusters, E is O(1/q),
   M3 is bounded, M4 has order q, yet the resonant factorial cubic tends
   to the integral of the weight. Replacing the clock background by a
   selected Haar-CUE realization preserves every signed smooth pair test
   and produces a deterministic counterexample on odd dimensions.
   Tiny phase perturbations remove all multiplicities without changing
   the limits. This is an abstract spectrum, not the maintained map.

The raw all-order analogue has budget
$C_{W,k}\sqrt{E_N M_{2(k-1)}(N)}$. It does not silently include proper
zero-sum subset strata or all higher factorial CUE counterterms.

## Proof review and attempted falsifiers

| Potential failure | Disposition |
|---|---|
| Lose the m+n resonance or double-count intersections | Exact arithmetic indicator equals the three individual strip indicators minus twice their common intersection. Checked both pointwise and through Fourier integrals. |
| Replace a signed sum by absolute summands | The proof keeps the integral of three frequency-filtered densities. Its estimates do not bound the absolute summand sum. |
| Impose bounded maximum occupancy | Not needed; the condition is the averaged fourth moment, or a higher-than-third averaged moment or critical uniform integrability. |
| Infer cubic tail control from pair convergence/positivity | Theorem 3 defeats that implication even with every smooth signed CUE pair test and simple spectra. |
| Use Gaussian traces at arbitrary Heisenberg degree | The all-band pair variance is proved by the projection cumulant bound 26H. Gaussian moment matching is used only for cubic mixed terms with 4bN<=H. |
| Assume microscopic CUE bins independent | Their cubic count covariances are bounded above by zero using the positive block determinant inequality; no independence is inserted. |
| Pass from countably many cubic weights using an unproved total-variation bound | A uniform negative-Sobolev mean-square bound and summability give convergence for all smooth weights on each compact subbox. |
| Claim a weak-process counterexample from an unbounded cubic statistic | Not claimed. Moment-tail control is distinct from weak local process convergence. |
| Treat all prime periods as sublinear | Not assumed or proved. The critical family uses abstract d, and the actual prime application retains its known order. |

For the explicit clock construction, the pair mass and local moments are
computed with integer bin allocation. Independent direct roots-of-unity
traces and positive Toeplitz matrices certify realizability of the small
controls. The smooth cubic is a Riemann sum, not a synthetic trace table.
The failed quadratic chirp construction in TRACE-010 stays a failed
construction; it is not repaired by assertion.

## Actual-map application and the next decisive estimates

For primes, retain exactly $U_p=e^{i\tau p A_p}M_p$ and
$\tau=10^{-80}$. TRACE-009 gives
$U_p^{d_p}=\zeta_p C_{p,d_p}$ with conjugates $M_p^jA_pM_p^{-j}$
in increasing-j ordered product. No new ordering convention is introduced.
Its resonant E equals
$p^{-2}\sum_{rd_p\in J_p}|\operatorname{Tr}C_{p,d_p}^r|^2$.

The new theorem deletes the entire positive-cone resonant factorial cubic
if this mass tends to zero and local density has a bounded moment of any
order above three, or critical cubic uniform integrability. A quantitative
alternative is E=O(1/d_p) with M4=o(d_p). Both alternatives are **open**
for the frozen spectrum. The known effective gap floor is much smaller
than 1/p; scalar exclusion, simple spectrum and all nonzero power traces
do not imply these conditions. The exact positive four-trace Gaussian
energy in the proof is an estimate to establish, not an evaluated limit.

When d_p is comparable to p, bounded Q and E->0 already close the cubic
sector by the earlier finite-cardinality bound. The density mechanism
addresses growing resonant sectors. It supplies no order-distribution
theorem that partitions every prime with the needed quantitative estimates.

The strongest next route justified by this cycle is therefore:

1. Obtain an upper bound on the actual block-power mass, uniformly over
   all r in each positive compact Heisenberg window. Use the exact Fejer
   comb identity of TRACE-009; scalar nonvanishing is not an upper bound.
2. Prove local spectral tail control for the same full propagator. A bounded
   positive quartic density energy would suffice for the cubic sector;
   pair limits alone stop at M4<=N M2^2 and Theorem 3 rules out a generic
   improvement. Any quantum finite-type/FIO argument must identify the
   actual operator and control its Heisenberg remainder before use.
3. Once these inputs close, estimate the nonresonant signed cubic with
   the correct finite CUE targets in every cone. Then treat composites,
   proper higher-order resonances and all bandwidths. The raw higher-order
   bound does not replace those tasks.

No actual-map mass/density estimate or signed nonresonant cubic has been
proved in this cycle. BGS-TRACE-005 and BGS-BGS-001 remain **OPEN**.

## Prior work and verification

Holder, positive convolution, arithmetic Fourier projection and interpolation
are prior tools. Pair information not determining all higher correlations is
also prior, including the corpus homometric example. The contribution is
this rigorous density-conditioned sector estimate, its critical boundary,
and the compatible asymptotic resonant construction. No exhaustive novelty
search or world-priority claim is made. The
[source note](../literature/resonant_density_sources.md) pins the reused
Diaconis--Evans theorem and credits related literature without importing
unverified theorems.

The [Python audit](../computations/verification/resonant_density_audit.py)
uses integer/Fraction cluster algebra, exact cumulant covariance in and
outside stable degree, a separate CUE Vandermonde-density constant term,
complex asymmetric Fourier/Holder controls and exact counterterm budgets.
The [Wolfram algebra](../computations/verification/resonant_density_checks.wl)
was actually evaluated. Source hashes, commands, focused checks and final
manuscript validation are preserved in the
[execution record](../evidence/executions/20261001-resonant-density.json).
Finite computations check identities and adversarial cases; asymptotic
claims rest on the written proofs.
