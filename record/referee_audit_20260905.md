# Referee audit: verified failures and scope

Date: 2026-09-05. Audited source snapshots: main `f678b5283f5edbc769a22d452c6ec3721e1f7fa8` and draft PR #13 head `af4395f0608d02e86b8a4097df503f316af5c11a`.

## Execution coverage is not a complete proof audit

The first independent local execution of all 37 executable verification scripts on the PR head, plus the committed spectral-diagnostics verification, gave 36 successful commands and two failures. All seven maintained C++ executables compiled and passed their default regression commands. This is implementation evidence, not verification of every line of the approximately 14,000-line mathematical corpus. No claim that all project proofs, the microscopic BGS conjecture, or an all-orders universality statement have been certified follows from this audit.

## Substantive correction: triple filters are not exact

The new `cayley_inverse_multi_edge_resultant_filter.py` fails because several asserted numerical anchors are false. Its proven necessary condition remains valid: a simultaneous same-embedding event implies that p divides every pair filter and their gcd. Equality of every triple gcd with p is not valid, even on the advertised finite controls.

With the deterministic first-maximal-embedding convention implemented by `maximal_embedding`:

| K | p | embedding | distinct triple-filter gcds |
|---|---|---|---|
| 29 | 59 | 2 | 59 |
| 43 | 173 | 1 | 173, 865 |
| 83 | 167 | 12 | 167, 334, 668, 2672, 5344, 21376, 27889, 85504 |
| 89 | 179 | 5 | 179, 358, 716, 1611, 2864, 5728, 15394 |

At K=29 the edges are `(3,11),(4,8),(6,12)` and the three ordinary pair filters are `944,1357,1888`, namely `16*59,23*59,32*59`, not the displayed `2*59,23*59,59`.

At K=43 the first maximal embedding has edges `(2,21),(7,10),(11,19),(15,16)`; a triple filter is `865=5*173`. Thus the assertion that all 96 triples have gcd exactly p must be withdrawn. The gcd of all pair filters of the complete maximal zero-edge set is p on each of the four controls; this weaker finite fact was reproduced.

The newly added multi-edge verifier was absent from the maintained row-support CI command list. A green older workflow therefore did not check this claim. Repair requires a negative-control regression preserving the extra factors, corrected numerical text, and an explicit CI gate, not merely deleting the failing assertion.

## Structural audit false positive

The Markdown-link scanner treats mathematical expressions inside code spans/fences, including `Z[T](w_e,w_f)`, as links. Three proof notes trigger false missing-file errors. The scanner must exclude code before extracting actual Markdown links and must retain genuine missing-link detection.

## Other review findings

For an arbitrary subgroup H, the Cayley image contains zero exactly when K is even; the unrestricted setup in `cayley_direct_energy.md` should not state that zero is always absent. The proved energy estimate does not use that erroneous assertion.

The descriptive empirical CDF supremum must examine both sides of every empirical jump. Using only `i/n-F(x_i)` in absolute value can underestimate the supremum. Correcting this diagnostic requires regenerating its promoted numerical output; it does not change an exact arithmetic theorem.

## Scientific boundary

Structural inverse multiplicity four at very large split primes is compatible with a quadratic energy target; absence of every collision is unnecessarily strong. Independently, control of finitely many global moments does not provide Heisenberg-scale desymmetrized traces or microscopic BGS statistics. These are separate unresolved obligations.
