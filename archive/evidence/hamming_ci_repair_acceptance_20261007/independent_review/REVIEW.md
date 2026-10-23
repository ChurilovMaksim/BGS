# Independent Hamming CI repair review, frozen final v2

Verdict: PASS for the narrow runtime-provenance, exact scientific comparison, output freshness, all-nine-entry routing, and durable failure-evidence repair. All findings raised against v1 are closed in the exact v2 bytes. No additional blocker was found in this focused review. Publication still depends on the separately owned final-byte aggregate/archival/maintenance gates; this review does not substitute for them or establish an asymptotic mathematical claim.

## Exact reviewed input and seal

- Frozen source: `/workspace/shared/bgs_hamming_ci_repair_validation_v2/source_snapshot`
- 3,998 maintained source files
- Source manifest SHA-256: `06c5611a1f9a68b00c0a96b2515f5251261b6614b9698147150485fc7035d55f`
- Exact repair diff SHA-256: `aae7ec93a65aae412c995e3e5b36705535a219ec43d1312dc8bf78df2d14a8d2`
- Base: `129c676b8e6457e7e5f1bd6f786b3939cbd84653`

`integrity_check.json` verifies every maintained file hash and the exact archive source inventory, using the repository's declared `workspace_sources.EXCLUDED` policy. It records generated `__pycache__` files from concurrent broader gates separately. No maintained source bytes changed. Thirteen existing wrapper/routing/test files changed relative to the base; seventeen files were added (comparator, regressions, dated repair records, preserved originals). The repair map exactly covers those changed files and validates every current/original/new hash. All preserved originals match the base publication snapshot. The mathematical adapters and their mapping, frozen expected bytes, `evidence/`, `mathematics/`, `manuscript/`, and `formalization/` remain byte-identical to the base. Frozen v1 remains unchanged and is not accepted or relabelled.

## Independent final-v2 execution

- 592 custom behavioral probe outcomes on Python 3.12.14 and pinned-dependency Python 3.13.5, each normal and `-O`: 146 main probes plus two archival stale/timeout probes per version/mode. Reports: `probes_{312,313}_{0,1}.json` and `extra_full_probes_{312,313}_{0,1}.json`.
- Eight targeted unittest invocations: `test_fractional_provenance.py` (17 tests) and `test_replay_artifact_routing.py` (2 tests), on both versions and modes. All passed. Logs: `target_{312,313}_{normal,optimized}_*.log`.
- Four executions of exact maintained `fractional_hamming/check_routing.py`, both versions/modes. All passed with explicit fixture outputs, actual nine-entrypoint selection, and unchanged repository bytes. Reports: `current_entry_routing_{312,313}_{normal,optimized}.json`.

The final custom review scripts contain no optimization-sensitive `assert` statements: their test checks are explicit exceptions and remain active under `-O`. An initial assert-syntax test attempt is archived separately and is not the acceptance evidence. The final reports above were regenerated from the optimization-safe scripts. The fixture producers supply scientific fixture payloads; they do not claim expensive mathematical re-execution. The publisher owns final-v2 real archival normal/-O, complete Python/C++, formalization, manuscript, and maintenance gates, so those were not duplicated. Earlier independently run real author+synthesis replays apply only to v1 and are not represented as final-v2 executions.

## Closed v1 findings

1. All nine workspace Hamming routes now pass `--output-dir` to distinct absent paths below the uploaded CI logs directory. All eight split wrappers use the common `cli(case)` and preserve the original exact case selection. Independent fixtures execute the actual default and eight split scripts with command-line durable arguments, both passing and corrupted science. Every failure retains raw expected/actual and a failed receipt; normal successful routes remain silent. The no-argument path retains its documented temporary-output behavior.

2. Archival full replay now requires each result path absent and nonsymlink immediately before the result producer runs, then requires a regular nonsymlink fully resolved result before reading/comparing. The exact v1 stale/no-op-producer and symlink fixtures now fail closed. Successful regular output, failed scientific output, invalid metadata, malformed JSON, and missing results are also covered. Failed returned regular actuals are declared before comparison.

3. Both replay entrypoints now retain timeout partial stdout/stderr and any permitted regular raw result. The default receipt marks the failed attempt `timed_out: true`, with no fabricated exit code; raw actual/expected and streams are hashed. The archival manifest declares the existing actual and partial streams; its aggregate report records the failed timeout attempt. Exact v1 archival timeout fixture now passes the retention checks in both Python versions/modes. Default timeout fixtures additionally verify actual.raw equals the original JSON and partial stream bytes are exact.

4. The strict parser now rejects positive, negative, and nested exponent-overflow JSON numbers through finite-checked `parse_float`, as well as duplicate keys and NaN/Infinity tokens.

## Comparator and scientific boundary

All v1 schema/type/corruption controls were rerun on final v2. Only declared top-level author `/python`, `/sympy`, `/elapsed_seconds` and independent aggregate `/runtime_seconds` provenance is separated. Version fields are required and bounded nonempty strings. Historical expected timings are required; only the already documented maintained-output timings may be absent. Present timings are numeric, finite, nonboolean and nonnegative. Synthesis and split independent cases have no provenance exemptions.

Every required root field is enforced. Unknown roots, nested provenance/version/hash-like additions, and scientific value/type changes remain failures. Recursive comparisons distinguish bool/int/float/string/null, retain every scientific field, and report bounded mismatch paths/counts with JSON-pointer escaping. The comparator and production failure guards use explicit checks that remain active under `-O`. Raw provenance and hashes remain available in evidence rather than being erased from historical output.

The hosted run `37573539762` remains a historical 207/208 failure whose actual was not retained. No hosted field-by-field scientific diff is claimed. This acceptance is a new local focused code/fixture review of v2, conditional on the separate final-byte execution gates.
