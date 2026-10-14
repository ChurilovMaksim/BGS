# Observed first-return pulses: proof and execution boundaries

This packet supports BGS-TRACE-083, an abstract-family theorem.
The original fixed-map TRACE-005 and BGS limit remain open.

The [complete frozen candidate](candidate_reviewed.md) is identical to
Git blob bbb8fc78e5405ada148fadbe52da9d95eaff0096 in unreferenced proposal
aaaa25c412147c08ab1ae8c4f83d85a0cefd6932. Its independent review is
[the complete R1--R5 reconstruction](independent_review.md), with verdict
proved as written. The maintained mathematical source preserves every
reviewed definition, formula, proof and boundary from the first n=4^k
definition through the final Boundary section. Only status prologue and
verification/prior-context links are added; see the [transfer receipt](transfer_receipt.json).

R1 computes all coefficients, not just a finite period.
R2 is about one observed memory coefficient and nearly all centered
diagonal directions. R3 selects one prime sequence for every fixed
sublinear exponent. R4 excludes p=3 and distinguishes unconjugated
powers from a conjugated covariance. R5 bounds positive all-source
amplitude-energy tails. Powers of a completed-return operator are not
later first-return coefficients. No physical measurement probability,
specific cavity-source law, BGS theorem, world priority or analytic Lean
certification follows from this packet.

## Actual finite executions

- [Root projected replay](controls.mjs) and [actual result](controls_result.json):
  functions V8, BigInt Z[omega] with omega^2+omega+1=0, all 12 diagonal
  source columns at N=12,k=1,p=3, 144 unitarity and 1728 first-return
  entries at times 1--12.
- [Root survival replay](survival_controls.mjs) and [actual result](survival_result.json):
  a separate actual V8 execution of those checks, plus all 1728 surviving
  matrix entries zero after time 6. The stdout Node wrappers were not run.
- [Wolfram Language source](wolfram_controls.wl) and [actual tool result](wolfram_result.json):
  exact rational n=4,p=5 memory-operator powers 1--9, traces
  0,0,12,0,0,12,0,0,12, with cube and Gram equal to the sector projection.
  This is not a direct projected-superoperator derivation.
- [Independent source](independent_controls.mjs) and [actual output](independent_controls_result.json):
  93376 exact first-return entries reconstructed from direct core powers,
  cyclotomic Gauss norms and full matrix renewal; three Gram partitions
  and 20 permutation cases. The report distinguishes the original run's
  candidate reference from the later final-source comparison.

All arithmetic coverage and exclusions are in the actual results.
The analytic proofs of genericity, min-max, perturbation estimates and
limits are independent of these finite checks.

## Source integration and unavailable execution

The local exec server subsequently reported 409 environment_offline.
The new R1--R5 work and source integration used V8 and the GitHub API.
No later local full Python regression, C++ build, Lean build or LaTeX
build was run or claimed. Pure JS source checks preserved all 133 earlier
claim records, kept both BGS targets OPEN, checked the 134-node dependency
DAG and reproduced the existing Python-rendered registry exactly before
rendering the added claim. These are structural checks, not the full
maintained CLI suite.

The [CI observation](ci_observation.json) belongs to main 57150ac:
both scientific attempts failed without available executable step logs;
formalization and computation were skipped. Its exact cause is
unestablished. The older successful main835 CI and the local 5 focused
checks / 236 tests have their own earlier source scope.
CoherenceBudget remains without a confirmed new compiler execution.

The delivered 301-page PDF belongs to the actually built TRACE-081/082
snapshot before TRACE-083's TeX addition. The later manuscript source
section is integrated, but a PDF rebuilt from that later tree has not
been produced. No previous build receipt is promoted to this new tree.
