# Frozen compact-stratum centering packet

## Result

The deferred ordinary centering candidate is independently accepted on its intended almost-everywhere finite-N domain for every odd N≥3. The exact formula retains all normalized circle/disk measures and every extracted source coefficient. It has a uniformly nonzero ordinary gauge determinant Δ≥2N−1 and a separate, explicitly computed mixed coarea factor.

The packet also proves a new effective **finite-N** collective-center cutoff approximation for the actual completed signed source and its fixed source derivatives. A cap-counting bound supplies a worst-stratum power ε^((N−1)/2); an explicit BB-pivot coefficient majorant supplies finite constants. No uniform microscopic or normalized tail is claimed.

## Files

- `compact_stratum_centering.md`: complete proof, exact N=1/N=2 restrictions, fixed-N source consequence, and next missing implication.
- `audit.md`: independent audit of the candidate; new results explicitly separated from that independent review.
- `checks/verify_centering.py`: new exact ordinary-coordinate controls.
- `checks/results.json` and `checks/run.log`: 20 successful exact controls and software versions.
- `inputs/centering_candidate.md`: byte-exact reviewed candidate.
- `input_manifest.json`: source hashes matched against the checked snapshot manifest.
- `source_binding_check.json`: independently checked manifest identity and input membership.
- `manifest.json`: frozen output hashes and completed execution scope.
- `validate_packet.py`: read-only packet integrity and source-pin verification.

Run the exact controls with `python checks/verify_centering.py`. Run integrity verification with `python validate_packet.py`. Integrity checks do not prove the mathematics.

## Proof boundaries

The candidate was independently reconstructed. The added determinant lower bound, cap estimate and coefficient majorant are new author results with self-review; this packet does not claim they have already received a second independent review. No external referee or formal proof-assistant certificate is asserted.

All source/canonical files remain unchanged. No ledger events or publication were performed. The input remains the exact supplied 3930-file snapshot, manifest d6d5ade7444d9a2de43be89fd9636554404a275aa6703fa93910e55c1a1826ba; no as-yet-unverified main publication commit is assumed.

The next missing implication is dimension-uniform control of the complete signed source-differentiated coefficient combination, including its boundary strata, at microscopic sources. Ordinary centering does not supply a super-Berezinian, positive full supermeasure, normalized tail or BGS theorem.
