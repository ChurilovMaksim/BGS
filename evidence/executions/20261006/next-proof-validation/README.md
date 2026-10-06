# Next-proof batch validation

The final frozen snapshot passes 170/170 executable workspace checks.
It contains 1550 files and retains null upstream provenance. The named
integration base is context, not authenticated provenance for the byte archive.
This package is execution evidence, not a new proof audit or a BGS theorem.

## Evidence and boundaries

- `receipt.json` summarizes verified scope and fingerprints public artifacts.
- `workspace.json` retains commands, outcomes, toolchain and source/binary/log
  hashes; its source manifest is factored into `archive-manifest.json`.
- `raw-check-log-index.json` records all independently matched raw log hashes;
  selected new-result and metadata-audit logs are retained in `check-logs/`.
- `fresh-cpp-build.json` records 22 fresh standalone compilations. Their sources
  and executed binaries match all 23 C++ workspace executions. Local
  CMake configuration failed because the required Boost package configuration
  was unavailable; `cmake-configure.log` preserves that failure. Remote CI is
  a separate gate and is not claimed here.
- `lean-build.json` and its log record an incremental full active build: 18
  active modules, 21 successful Lake jobs. Existing modules were replayed and
  FourCutKernel freshly compiled. Native-decision generated axioms are explicit.
  Compression/lifting and analytic proofs are outside this formalized scope.
- Maintenance passed 35 tests normally and 35 under an optimized parent.
- The manuscript passed three LaTeX passes with 85 immutable TeX inputs and
  263 pages. All source, PDF and build-log hashes were independently checked.
  Visual inspection covered physical pages 226, 256, 257, 258 and 259 only, with
  no clipping or overlap reported; this is not a complete visual audit.

## Failed first capture and explicit correction

`initial-failed/` preserves the first 169/170 receipt, its 1,549-file manifest,
failed bibliographic-audit log and full-run log. The failure was stale cached
external-dependency impact closure, not a passing run. The exact reviewed
correction is documented in
[the bibliographic impact review](../../../../record/bibliographic_impact_review_20261006.md).
`snapshot-delta.json` records the exact changes before the complete rerun.
All reused C++, Lean and TeX source hashes match the final frozen snapshot.
Historical receipts outside this new package are unchanged.

## Disclosed public curation

Machine-specific paths use declared role placeholders; hash strings and null
provenance remain intact. `raw-public-hashes.json` distinguishes raw execution
bytes from curated bytes. Source manifests appear once per snapshot instead of
being repeated inside receipts. The archive files named in those manifests are
not all separate executions or proof readings. This package and the linked
integration addendum were created after execution and were not present in the
frozen snapshot. BGS and TRACE-005 remain OPEN.
