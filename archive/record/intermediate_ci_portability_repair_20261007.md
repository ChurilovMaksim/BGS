# Intermediate replay portability repair

Scientific CI 37553863591 on d37c92e5 passed 191 of 192 checks with unchanged
sources. The failing intermediate wrapper compared Python/NumPy/SymPy version
strings as mathematical results. Its subprocess completed successfully; this
was not a timeout or a failed arithmetic assertion. The original failed
receipt and independently retained Python 3.13.5 replay are hash-bound in
[evidence](../evidence/ci/20261007/intermediate-environment/failed_ci_summary.json).
All six cross-runtime scientific outputs and source hashes match the immutable
originals after exactly the declared runtime and seven version fields.

The maintained comparator now excludes only step-specific top-level runtime
and environment fields. Nested keys, types, coefficients, flags, extra/missing
structure and source_sha256 remain strict. Environment provenance is retained
separately. Runtime metadata must be finite, nonnegative and nonboolean.
Expected raw bytes are cached before a worker can overwrite a same-path result.
On mismatch, bounded exact JSON paths, observed environment and actual/original
result hashes are recorded before raising; both raw results survive in external
scratch. Regression tests cover these failure modes in both Python modes.

Maintained replay paths no longer force concurrent subprocesses onto the same
minimum CPU core. CPU, memory, wall and single-library-thread caps remain.
Independent fractional controls are partitioned into their original five
families, with the four full-End cases separately bounded. Every old case and
scientific field is retained; historical one-core and full-suite receipts are
unchanged. No generic timeout is raised and no new mathematical claim follows.
Fresh hosted CI is still required; local cross-runtime agreement is not a claim
that the repaired commit has passed CI.
