# Rounded and simple-spectrum endpoint barriers

Stable claim: **BGS-TRACE-025**.

The constructions below are independently accepted with the precise restriction in this wrapper. This card is part of the maintained corpus; the original candidate-checkout wording is historical. Both change the quantizer; neither is an actual-model counterexample.

For each fixed nonzero nonnegative smooth positive-band weight, a fixed sufficiently fine microscopic root grid gives an O_w(N^-1)-close rounded family that retains the reviewed coarse dynamics, flatness/P/reverse/charge estimates, theta=0 compact charge-pinch limit and fixed-word/triple-log scopes, while its genuine signed high-Hamming/high-switch offcharge aggregate has positive liminf and its damped endpoint vanishes. Fix the grid parameter L before N->infinity; the statement is eventual N>=L. Uniform Schatten S_p preservation for p>2 is conditional on an independently supplied bound and does not prove such a bound for the actual map.

Separately, the reviewed growing-period N=p^2 family admits an O(N^-3) split with simple spectrum, no root-of-unity ratio between different eigenvalues and no positive scalar power. Its residual grows at least (sqrt(N)/2) integral w-O_w(1) for p prime, p=2 mod 3. The audit also proves a combined rounded-and-split construction with the positive rounding lower bound and no exact recurrence. Divergence is not claimed for that fixed-L construction.

MANDATORY SCOPE CORRECTION: line 34 of the immutable rounding source contains a stronger strategy sentence than was accepted. The accepted conclusion is: a successful endpoint proof must add a property or estimate excluding the witnesses and identify its use in the signed calculation. Exact raw-Weyl/all-order information is one possible discriminator; no particular proof method is logically required by the barrier.

The original [rounding proof](../../evidence/wave2_checked_20261007/raw/rounding_sources/rounding_offcharge_upgrade.md) and [split proof](../../evidence/wave2_checked_20261007/raw/rounding_sources/simple_spectrum_companion.md) are copied byte-exactly. Read them with the [accepted restricted audit](../../evidence/wave2_checked_20261007/raw/rounding_review/audit.md), especially Sections 5-9, [discriminator contract](../../evidence/wave2_checked_20261007/raw/rounding_review/must_discriminate.md) and [review seal](../../evidence/wave2_checked_20261007/raw/rounding_review/review_seal.json).

The [TRACE-114 balanced construction](balanced_rounding_research_20261027.md) separately preserves absolute o(1) errors in polynomially many short traces, at the coarser O(N^-alpha), alpha<1, norm scale. It does not assert the charge/high-switch preservation of this theorem.

No arbitrary occupation-twist compactness, actual Schatten theorem, unnormalized o(1) short-trace preservation from nearest rounding, exact kick identity, subprincipal or all-order smooth-symbol preservation is inferred. Literal masked T16, BGS-TRACE-005, the balanced microscopic law, higher factorial comparison and deterministic BGS remain OPEN.
