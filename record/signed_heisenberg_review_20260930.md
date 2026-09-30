# Research continuation: absolute obstruction and signed cubic mechanism

Date: 30 September 2026. Work performed without subagents. Review level:
author self-review and independent algebraic representations, not an
external referee report. The fixed map, tau=10^-80, symmetry convention
and complete BGS goal are unchanged.

## Exact result and scope

[BGS-TRACE-010](../mathematics/signed_heisenberg_comparison.md) proves a
universal obstruction to the unaveraged all-order absolute CUE norm. If the
pair absolute error on a positive Heisenberg interval tends to zero,
the normalized absolute factorial triple error on a smaller positive
box is at least $(1/1024+o(1))\sqrt N$ for the stated box. A quantitative
finite bound and a theorem at every fixed $k\ge3$ are given, with growth
$N^{k/2-1}$. The proof counts bad subset sums and compares the leading
singleton partition with lower partitions; it does not use chaos or primes.

The original TRACE-003 sufficiency theorem remains correct, including
averages taken before the modulus. What is excluded is its simultaneous
unaveraged absolute hypothesis at every order. ERR-025 records this
stronger boundary, rather than retracting a valid implication. TRACE-005
now explicitly places the modulus outside the weighted signed sum.
The sparse positive pair criterion in TRACE-009 remains valid.

## Three attempted mechanisms and their dispositions

| Route | Checked outcome | Consequence |
|---|---|---|
| Promote pair absolute control to all-order absolute control | Impossible for every deterministic spectrum under the pair premise; quantitative project proof. | Stop this strengthening; retain the signed bridge. |
| Use cancellation between weighted cubic modes | Exact Haar-CUE complex variance for arbitrary weights below the stable degree threshold, including all factorial pair counterterms. Bounded weights give O(1/N); restricting three resonant strips gives O(1/(Nd)+1/N^2). | A reference scale and proof budget; no estimate for the frozen map. |
| Assign quadratic phases to square-root pair amplitudes | Signed positive-cone partition sums cancel faster than any fixed inverse power for smooth weights, but the N=3 Toeplitz moment determinant is negative. | Formal algebra control only; no unitary construction or universality theorem. |

The resonant pair mass estimate does not automatically close a cubic
estimate. An exact Cauchy--Schwarz bound exposes a loss
$3\|W\|_\infty Q\sqrt{|R|E_R}$, with $|R|$ of order N/d.
Failure of that upper bound to vanish is not an actual-map counterexample.

## Relation to existing work

The [25 September programme](bgs_program_20260925.md) and the
19 September CUE audit already identified the signed mixed cubic and its
nonzero high-band reference. The continuation adds the universal
absolute-norm incompatibility, the low-band arbitrary-weight variance,
the explicit phase control and its failed realization check. Prange's
prior non-self-averaging warning is credited in the
[source audit](../literature/signed_heisenberg_sources.md).
Neither a claim of world-first priority nor a prize-level characterization
is supported by this work.

## Next decisive attack and exact success condition

1. Prove the actual-map weighted factorial cubic comparison for each compact
   Fourier test, first isolating the three strips d_p dividing m, n, or m+n.
   Use the correctly oriented ordered block from TRACE-009, with no kick,
   dimension, or random-phase average inserted into the deterministic model.
2. Estimate the nonresonant signed cubic contribution. Scalar classical
   finite type and logarithmic-time trace bounds do not supply this quantum
   Heisenberg estimate. A quantum identification and summation argument must
   be proved if those inputs are used.
3. Retain the exact nonzero CUE counterterms beyond the stable cone and all
   proper zero-sum strata at higher orders. A theorem on one small box would
   be a subsidiary advance, not the full all-bandwidth BGS conclusion.

The cheapest decisive negative test remains a coherent positive-time trace
on an infinite dimension subsequence, as in TRACE-009. The finite coherence
range at the tiny fixed tau is not an asymptotic subsequence proof.
Both alternatives remain open for the maintained map.

## Verification actually performed

The maintained [Python verifier](../computations/verification/signed_heisenberg_audit.py)
checks the finite CUE positive-cone cycle identity, the covariance kernel
against the existing general cumulant formula, an independent determinant
density constant term, complex asymmetric weights and the stable-range gate.
It checks the finite cubic bound on unitary spectra and formal adversarial
tables, direct distinct-label sums, higher-order partition budgets and
the exact negative Toeplitz determinant. Floating phase controls illustrate
cancellation but are not asymptotic proofs.
The saved [Wolfram source](../computations/verification/signed_heisenberg_checks.wl)
was actually evaluated; its algebra and equivalent radical determinant
agree with the Python derivation. The
[execution record](../evidence/executions/20260930-signed-heisenberg.json)
separates these checks, repository synchronization and the validated
three-pass manuscript build, with visual review of the updated pages.
No new Lean compilation or model-specific trace theorem is asserted.
