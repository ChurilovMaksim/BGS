# Hamming runtime-provenance repair, 7 October 2026

Published checkpoint `129c676b8e6457e7e5f1bd6f786b3939cbd84653` had
207/208 hosted scientific checks. The author Hamming replay compared its
frozen Python 3.12 version string with the hosted Python 3.13 version string.
This record does not change the earlier complete local acceptance receipt.
The hosted failed raw author JSON was not retained; exact science equality
is established by separately identified fresh local cross-version reruns.

The repaired default verifier and archival full replay validate their exact
root schemas and separate only named top-level Python/SymPy/timing provenance.
All scientific fields, nested metadata-like names, unknown fields and JSON
scalar types remain strictly checked. Original expected bytes and mathematical
ports are unchanged. Fresh raw actual/expected results, source hashes, logs,
provenance and mismatch paths are retained before comparison, including failure;
the existing CI artifact upload receives all nine Hamming replay output directories.
Stale and symlink producer outputs are rejected; timeout partial logs and regular
actual outputs are explicitly retained before reporting failure.

[Exact repair map and preserved originals](fractional_hamming_provenance_repair_20261007.json)
join the dated historical source pins to the new implementation. This candidate
requires its own frozen full validation and independent review before publication.
No later mathematics is included. BGS and TRACE-005 remain OPEN.

## Post-run local acceptance

The exact frozen 3,998-file v2 candidate passed complete local validation and
independent review. [Acceptance receipts and historical failure](../evidence/hamming_ci_repair_acceptance_20261007/acceptance.json)
record Python 3.13 scientific 208/208, 163 maintenance tests in each of four
normal/optimized cross-version modes, 28/28 supplement, fresh C++22, twelve
archival family/mode replays, and all nine durable routes. The evidence-only
publication delta is separate from that tested source. New hosted CI remains
pending; the failed 129c676 run and superseded v1 are preserved as history.
