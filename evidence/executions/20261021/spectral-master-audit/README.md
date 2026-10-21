# Spectral snapshot audit: execution and source evidence

This packet accompanies the [review](../../../../record/spectral_master_audit_20261021.md)
and the two maintained proofs
[TRACE-106](../../../../mathematics/physical_kick_trace_decay.md) and
[TRACE-107](../../../../mathematics/physical_trace_polynomial_approximation.md).

The uploaded master has SHA256
`10b90c7d12668cd7327bcc08bda292f4c7d6cf82218ee95d5d4f7603fac86cef`.
Its original file is not edited. Five selected raw sources are retained here
byte-exactly; their relative references to the author's wider workspace are
historical provenance, not maintained repository links. Self-contained adopted
proofs are in `mathematics/`.

- `coverage.json`: 265 explicitly delimited blocks, their locators and actual
  review status. All 207 recognized declared source hashes matched. Nested
  historical books are not claimed fully reviewed.
- `receipt.json`: frozen input, execution scope and artifact hashes.
- `coefficient_replay.json`: fresh output of the unchanged imported script;
  its bytes match the author's embedded output.
- `finite_checks.json`: fresh run of the maintained independent finite checker
  under Python `-O`. No asymptotic theorem is computationally certified.
- `validation.json` and manuscript logs: repository projection, link and build
  checks, with their actual scope recorded after execution.

The accepted imported 1/25 estimate is strengthened to 1/9 by a separate
positive-square argument. This is an analytic author proof with self-review.
The all-order polynomial error estimate extends the imported pair estimate.
The general BGS claim, the original signed trace hierarchy and most historical
proof-review obligations remain open. Internal source audits are not external
refereeing, and the packet contains no Lean certificate.

Reproduction of the finite part:

```sh
python3 -O computations/verification/physical_kick_trace_checks.py
python3 evidence/executions/20261021/spectral-master-audit/sources/coefficient_check_original.py
```

The second command writes the author's JSON filename beside the script; run it
in a temporary copy when preserving this evidence directory unchanged.
