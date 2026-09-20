# Self-review and continuation state

18 September 2026. Base e0ada2e2c44dfe10bebf928dc8a1d6526ae15cb7.

**New theorem verdict:** proved as written under its explicit hypotheses,
by internal derivation and a separate adversarial self-review. This is not
independent external review or a formal proof certificate.

**Original BGS target verdict:** incomplete. No reference CUE theorem,
fixed-map Heisenberg cancellation bound, or applicable natural-operator
comparison has been established.

## Claim and dependency audit

| Claim | Evidence and critical obligation | Status |
|---|---|---|
| Finite unfolded RMS estimate (2) | Analytic eigenangle flow; time-average HS bound; telescoping unitary powers; exact 2pi normalization | Passed |
| Uniformity along the path | Operator comparison of A_(T,s) with A_(T,0), not an assumed uniform eigenbasis | Passed |
| Multiple eigenvalues | Compression of the Hermitian generator inside an eigenspace; orthonormal eigenbases; no gap division | Passed |
| Vanishing RMS from (4) | Fixed T before N->infinity, then T->infinity | Passed |
| Semiclassical use of (4) | Fixed-time Egorov, normalized product traces, ergodicity, uniformly bounded observable | Conditional on precisely these model assumptions |
| Logarithmic rate | Explicit correlation/time-average hypothesis (5), stronger than merely quoting endpoint diagonal variance | Passed as a conditional implication |
| Transfer of kth correlations | Bounded maximum displacement plus local moment bound of order 2k-1, or k+1 for convergence without the same rate | Passed |
| Schwartz extension | Enlarged reference boxes and the existing translated occupation bound | Passed with all-order reference boundedness |
| Local point-process transfer | Uniform-origin integral and average displacement; does not assert convergence of correlation expectations without moments | Passed |
| Sharp Pell displacement scale | Previously proved finite-symbol normal form and exact orbit variance; explicit separation of clusters; unitary logarithm matching estimate | Passed subject to those pinned internal proofs |
| Application to prescribed/natural quantum maps | Smooth 1/N comparison and unitary reference not supplied | Not established |

Three independent mechanisms invalidate weakened claims: the commuting
alternating clock, a rare cluster with divergent third moment, and a
two-level-block family with zero initial diagonal variance but nonzero
limiting displacement. The last example specifically tests the uniform
path argument rather than only the size of the perturbation.

## Verification performed

`OPENBLAS_NUM_THREADS=1 python build/ergodic-transfer/finite_checks.py`
completed successfully. It checks the finite RMS bound and sampled path
variance at N=31,63,127 for seeded unitary fixtures; degenerate Pell-cat
fixtures at N=41,239; a direct compact pair statistic; and the three failure
controls. Samples along a path are diagnostics, not a proof of uniformity.

For the Pell fixtures the observed RMS displacements are about 0.045663
and 0.038651. Their ratios to sigma/(2pi sqrt(K)) are 0.99865 and 1.00017.
These finite numbers support the algebraic setup; the large-K sharpness
statement is proved analytically, not fitted from two dimensions.

Schubert's primary paper was checked at Section 4, Theorem 4 and equations
(65)--(70), for the existing quantum-ergodicity method. Faure--Tsujii was
checked at Theorems 1.37, 1.38 and 1.69: unit-circle concentration and an
O(h^delta) comparison do not provide the exact unitarity and smooth 1/N
comparison required here. Neither literature check is a proof of novelty.

No new Lean theorem is claimed. No commit or push was made.

`endpoint_check.wl` records the executed Wolfram check of the two-level
trace, determinant and limits. The first limit evaluation emitted intermediate
singular-expression warnings; an independent Taylor-coefficient evaluation
returned {(-1-Pi^2)/2, s^2, Pi^2+s^2} without warnings. The analytic argument
does not rely on interpreting those warnings as a certificate.

## Research consequence

An operator-norm threshold o(1/N) is not necessary for smooth ergodic
comparison: a structured correction exp(i Op(a)/N) is harmless for an
already established all-k local law. This removes one overly strong
accuracy demand in a possible comparison route. It leaves two concrete
obligations: construct a comparison satisfying this structure, and prove
a microscopic reference law. An all-time trace formula alone does not
provide the latter.

Trying to transfer the result from the cat spectrum to the fixed nonlinear
kick by many such increments does not close the problem. The fixed kick
exp(i tau N A) consists of order tau N^2 increments of size A/N; summing
the available logarithmic displacement estimate over them is divergent.
No cancellation in that parameter evolution has been proved.
