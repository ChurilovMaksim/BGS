# Final corpus-revision execution evidence — 6 October 2026

This is an execution receipt, **not theorem certification**. It neither proves BGS universality nor authenticates an upstream Git commit. Finite tests, native computations, Lean kernels and manuscript compilation have separate scopes.

## Recorded results

- `workspace.json`: 161/161 Python/C++ checks passed in archive mode against an immutable 1,048-file snapshot; the source tree remained unchanged during the run. `archive_manifest.json` is the exact, unmodified manifest. Its SHA-256 agrees with the runner, and its files map equals the runner's source manifest.
- `cpp_build.json`: 21 successful fresh standalone C++ builds. All 22 C++ execution records (including an additional replay) match their build's source and executable hashes. This joins the runner's prebuilt-binary evidence to the separate fresh-build evidence; no reproducible-binary guarantee is inferred.
- `checks/`: all 217 available run-output artifacts, including logs and certificates. Every one of the 161 per-check raw log hashes matches the corresponding runner record. Arithmetic, bounded parameters, timings, commands and exclusions remain in the individual outputs and maintained source.
- `lean.log`: successful build of 17 active modules, 20 Lake jobs. `lean_axioms.txt` extracts the 61 printed dependency reports: 37 mention native-decide-generated axioms, 14 print no axiom dependencies, and 10 print other dependencies. These are only the declarations printed by this build, not a complete axiom inventory. Native-decision trust boundaries remain material; neither these counts nor a successful build formalize the unencoded analytic arguments. The log itself contains no per-source hash linkage; the snapshot and observed Lean sources were separately compared.
- `unit_tests.log` and `unit_tests_optimized.log`: 17 regression tests pass in each environment, including assertion preservation, source mutation, stale-output and replay safeguards. These logs do not themselves record the launching command or environment variables; the optimized-environment designation comes from the execution record supplied with the artifact.
- `manuscript_build.json` and `manuscript_logs/`: separate three-pass, 256-page PDF build, with no forbidden warnings under the recorded filter. All recorded TeX input hashes match the observed repository. A separately recorded visual spot-check inspected pages 1, 244, 251 and 256 at 1100/1200-pixel render widths without clipping or overlap. This is a four-page sample, not full-document visual inspection. The PDF is not duplicated here; its exact hash is in the build manifest.

## Snapshot versus finalization

The executable run used its immutable snapshot, not the later final tree. At the observation recorded in `receipt.json`, there were no computational, mathematical, or active Lean source differences. Later reproduction-guide, reader-guide, audit-dossier and master-report edits, plus regenerated `fixed_map_frontier.tex`, are explicitly listed with old and observed hashes; checkpoint evidence additions are listed too. The regenerated TeX is covered by the later manuscript build's independent input hashes. Documentation and dossier edits were finalized separately and are not silently relabeled as having been executed in the earlier snapshot.

The comparison is an observation-time inventory using the maintained `workspace_sources.inventory` exclusions, with this new evidence directory additionally excluded to avoid circular hashing. Later edits require a fresh comparison. The directory name “final” identifies the final execution batch, not an immutable claim about every byte of the subsequently assembled tree.

## Provenance and normalization

`receipt.json` gives every supplied artifact's original SHA-256 and byte count, its public copy's SHA-256 and byte count, and whether path normalization changed it. Public text copies replace environment-specific absolute roots with the semantic placeholders declared there. Embedded execution/source/binary/log hashes are never rewritten: they continue to identify the raw inputs or outputs. Consequently, a normalized log may intentionally have a different public-file hash from the raw-log hash quoted by `workspace.json`; the receipt connects the two. The archive manifest is byte-for-byte unchanged.

`${SOURCE_SNAPSHOT}`, `${RUN_OUTPUT}`, `${CURRENT_REPOSITORY}`, `${BOOST_INCLUDE}`, `${PYTHON_EXECUTABLE}` and `${TEXMF_VAR}` denote local environment roles, not literal runnable filesystem locations. Substitute your own roots when reproducing. Original environment path spellings are intentionally not published. This normalization removes environment-location details only; it does not alter substantive results.

`SHA256SUMS` covers every public file in this directory except itself. Verify with `sha256sum -c SHA256SUMS` from this directory. Receipt assertions were derived from the preserved inputs and a read-only comparison, not a rerun of the full suite during curation.
