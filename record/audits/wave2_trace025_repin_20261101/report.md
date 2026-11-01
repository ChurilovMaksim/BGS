# Wave2 TRACE-025 wrapper re-pin, 1 November 2026 (final-polish-2)

## What failed
`computations/verification/wave2_integration_audit.py` had failed on main since commit 469debb9 (27 October 2026, "Integrate
operator-resolution results into the maintained BGS programme"). That commit edited the BGS-TRACE-025 wrapper
`mathematics/fixed-map/rounding_simple_spectrum_endpoint_barriers.md`. Two pins still held the earlier bytes:

| pin | file | old sha256 | new sha256 |
|---|---|---|---|
| `cards[BGS-TRACE-025].integrated_wrapper_sha256` | `record/wave2_promotion_mapping.json` | `d918c7a5b49c041d68a0820f556e98e8be7cfec71a52c551c447f3fe983697ca` | `814d6da2b7eb8d7268c81c876706d2b0719560746bf8dd91219286e05d787b89` |
| `authoritative_wrappers[...rounding_simple_spectrum_endpoint_barriers.md]` | `record/wave2_manuscript_mapping.json` | `d918c7a5b49c041d68a0820f556e98e8be7cfec71a52c551c447f3fe983697ca` | `814d6da2b7eb8d7268c81c876706d2b0719560746bf8dd91219286e05d787b89` |

The old pin is the wrapper as moved in 8b48450b (phase 2, wave 9b). It is still retrievable with
`git show 8b48450b:mathematics/fixed-map/rounding_simple_spectrum_endpoint_barriers.md`.

## The 469debb9 edit (complete diff)
```diff
diff --git a/mathematics/fixed-map/rounding_simple_spectrum_endpoint_barriers.md b/mathematics/fixed-map/rounding_simple_spectrum_endpoint_barriers.md
index f915d8a6..32e4cd52 100644
--- a/mathematics/fixed-map/rounding_simple_spectrum_endpoint_barriers.md
+++ b/mathematics/fixed-map/rounding_simple_spectrum_endpoint_barriers.md
@@ -2,7 +2,7 @@
 
 Stable claim: **BGS-TRACE-025**.
 
-The constructions below are independently accepted with the precise restriction in this wrapper. This card is integrated into the separate candidate checkout; canonical publication remains pending. Both change the quantizer; neither is an actual-model counterexample.
+The constructions below are independently accepted with the precise restriction in this wrapper. This card is part of the maintained corpus; the original candidate-checkout wording is historical. Both change the quantizer; neither is an actual-model counterexample.
 
 For each fixed nonzero nonnegative smooth positive-band weight, a fixed sufficiently fine microscopic root grid gives an O_w(N^-1)-close rounded family that retains the reviewed coarse dynamics, flatness/P/reverse/charge estimates, theta=0 compact charge-pinch limit and fixed-word/triple-log scopes, while its genuine signed high-Hamming/high-switch offcharge aggregate has positive liminf and its damped endpoint vanishes. Fix the grid parameter L before N->infinity; the statement is eventual N>=L. Uniform Schatten S_p preservation for p>2 is conditional on an independently supplied bound and does not prove such a bound for the actual map.
 
@@ -12,4 +12,6 @@ MANDATORY SCOPE CORRECTION: line 34 of the immutable rounding source contains a
 
 The original [rounding proof](../../evidence/wave2_checked_20261007/raw/rounding_sources/rounding_offcharge_upgrade.md) and [split proof](../../evidence/wave2_checked_20261007/raw/rounding_sources/simple_spectrum_companion.md) are copied byte-exactly. Read them with the [accepted restricted audit](../../evidence/wave2_checked_20261007/raw/rounding_review/audit.md), especially Sections 5-9, [discriminator contract](../../evidence/wave2_checked_20261007/raw/rounding_review/must_discriminate.md) and [review seal](../../evidence/wave2_checked_20261007/raw/rounding_review/review_seal.json).
 
+The [TRACE-114 balanced construction](balanced_rounding_research_20261027.md) separately preserves absolute o(1) errors in polynomially many short traces, at the coarser O(N^-alpha), alpha<1, norm scale. It does not assert the charge/high-switch preservation of this theorem.
+
 No arbitrary occupation-twist compactness, actual Schatten theorem, unnormalized o(1) short-trace preservation from nearest rounding, exact kick identity, subprincipal or all-order smooth-symbol preservation is inferred. Literal masked T16, BGS-TRACE-005, the balanced microscopic law, higher factorial comparison and deterministic BGS remain OPEN.
```

## Assessment: non-substantive
* Line 5 changes the integration-status sentence only. "Integrated into the separate candidate checkout; canonical publication remains
  pending" becomes "part of the maintained corpus; the original candidate-checkout wording is historical". The surrounding sentence
  ("Both change the quantizer; neither is an actual-model counterexample") is unchanged.
* The added paragraph is a cross-reference to BGS-TRACE-114, which is a separate registered claim with its own source. It says
  explicitly that TRACE-114 "does not assert the charge/high-switch preservation of this theorem". So it adds no hypothesis, conclusion
  or scope to BGS-TRACE-025.
* The statement paragraph, the mandatory scope correction, the links to the byte-exact sources and the closing list of non-claims
  and OPEN items are byte-identical. The audit's content guards still pass, among them "no particular proof method" for TRACE-025.

The two pins are therefore re-pinned to the current bytes rather than reverting the edit. No claim state, statement or boundary
changes. The other four scoped cards, the preparation seal, the 85 immutable copies, the 50 reviewed input pins and
`section_sha256` are unchanged.

## Result
`wave2_integration_audit.py` exits 0 (status passed).
