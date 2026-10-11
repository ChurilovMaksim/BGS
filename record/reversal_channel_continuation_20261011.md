# Reversal-channel gap continuation, 11 October 2026

The singular-spectrum mechanism of [TRACE-073](../mathematics/schur_censoring_gap_20261011.md)
also propagates the reversal channel. This is a separate independently
reconstructed analytic extension of the [preceding cavity continuation](cavity_continuation_20261011.md),
from main `0db2e1ad42c3c53b56fc5aecbed791c8faa9b732`.

## New theorem and its application

If C is **any complex contraction**, and `I-C_DD` is invertible, every ordered
singular value of its algebraic Schur complement is bounded by the
corresponding singular value of C. Positivity, normality, stochasticity and
a Perron mode are unnecessary. An exact harmonic lift proves first that the
complement is a contraction, then transfers every strictly positive singular
subspace by positive inertia. This statement does not use J-centering.

For a unitary S, the Hermitian reversal matrix is
`R_ij=S_ij conjugate(S_ji)`. Its absolute row and column sums are at most one,
by Cauchy–Schwarz and unitarity. It is a contraction but need not be positive
semidefinite. The incorrect pointwise assertion `|R_ij|<=|S_ij|^2` is not used.

Fresh-phase elimination has exactly the algebraic Schur complement of R as
its conditional mean. The coherent increment has operator norm at most
`8 delta` on a pre-exit state with `delta=max |S_ij|^2<=1/4`. The stopped
even-p Schatten potential therefore gives the same explicit probability
bound as the intensity channel, now applied to R itself without subtracting J.
A finite union bound controls both channels on the same all-time-flatness
event, down to `ceil(log(2N)^(3+kappa))`.

[FM-022](../mathematics/reversed_path_decay.md) defines exactly this initial
matrix and proves its norm tends to zero for the unchanged fixed-coupling
odd-dimensional family. It supplies only the initial leaf, without an
effective startup. The inherited FM-022 proof was not reaudited in this
extension. Together FM-021 and FM-022 supply the two initial gaps needed for
the conditional application.

## Independent reconstruction and finite execution

The separate internal reviewer directly checked the general complex lift,
all-singular-value positive-inertia step, the transpose and conjugation in
the exact phase expansion, the noise constant, full crossing-state stopping,
and the literal correspondence to the FM-022 statement. No substantive gap
was found. This verdict is distinct from the earlier intensity-channel
review and from external peer review.

The [exact review input](../evidence/executions/20261011/reversal-gap/inputs/reversal_review_input.md)
has SHA256 `fb77ad79121e77f0c723ebd1bbde5fa5ede3db0a6e2ca7ddb6dc4680c28f67b3`.
The maintained proof adds the explicit `s=1` contraction step recommended
by the review.

A separate Wolfram execution returned four exact True results on one rational
complex 3-by-3 unitary: unitarity, Hermiticity of R, the fresh-phase expansion
and the general lift energy identity for arbitrary complex input coordinates.
Its real phase parameter and finite matrix scope are explicit. The
[execution packet](../evidence/executions/20261011/reversal-gap/README.md)
retains the code, actual tool response, review input and subsequent checks.
No finite computation certifies the all-matrix or asymptotic theorem.

## What remains open

The common all-time entry-flatness probability remains unproved. The
extension does not reach below its cutoff, identify a scalar microscopic
law, complete the physical symmetry classification, remove auxiliary
randomness, establish signed TRACE-005 or resolve BGS. World priority is
not established. There is no new analytic Lean formalization.
