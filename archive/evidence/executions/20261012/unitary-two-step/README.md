# Unistochastic two-step obstruction: proof and execution scope

Promoted 12 October 2026 from the candidate written on 11 October.
[Canonical proof](../../../../mathematics/unitary_two_step_obstruction_20261012.md)
and [research outcome](../../../../record/unitary_two_step_continuation_20261012.md)
state the theorem and its boundary.

- *inputs/unitary_obstruction_review_input.md* is the byte-exact original
  candidate, SHA256
  c0b024469d84b91ae92e74b4d04b15cf259c9f11d55b2071d5422562da45a5f1.
  *review.json* records independent internal reconstruction.
- *maintained_transfer_review.json* pins the final maintained proof and
  distinguishes its higher-step and one-step variance companions.
- *finite-controls/manifest.json* is the accepted version-two execution
  record. The pinned source is
  *computations/verification/unitary_two_step_obstruction.py*; the contract
  states the exact arithmetic, floating diagnostics, inputs and exclusions.
  The actual run exited zero in 0.618057 seconds, with enforced limits of
  90 wall seconds, 80 CPU seconds, 1 GiB address space, one core and one
  library thread. Input hashes were unchanged; manifest validation passed.
- *finite-controls/results.json* records four rational orthogonal
  constructions in dimensions 8 and 12, one complex rational rank-one
  primitive, the symbolic centered fourth-moment combination and the
  exact sharp row--column Cauchy equality. Six floating QR constructions
  in dimensions 32, 64 and 128 separately check numerical identities.
  Their maximum unitarity error was \(2.93\,10^{-15}\).
- *initial_control_disposition.json* and its preserved inputs identify the
  earlier 80-second timeout. Replacement by rational orthogonal full
  constructions plus a complex primitive changed the exact coverage; it
  is not a successful replay of the expensive complex fixtures.

The analytic argument proves asymptotic existence; the finite executions
do not. Independent internal review is not external peer review. No
all-time Schur trajectory, analytic Lean certificate, chaotic quantizer,
BGS counterexample or world-priority claim is supplied.
