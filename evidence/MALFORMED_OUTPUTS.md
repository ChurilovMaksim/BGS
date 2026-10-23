# Malformed historical output files

Machine-readable index of the three historical output files that are not
valid JSON as stored. All three are preserved byte-for-byte as historical
evidence; do not "repair" them in place. Any tool walking
`evidence/**/*.json` should skip exactly the paths listed here.

Classification as recorded in the repository reconciliation of
20 October 2026
([record/repository_reconciliation_20261020.md](../record/repository_reconciliation_20261020.md),
"Three malformed-as-JSON historical output files are explicitly
classified and preserved byte-for-byte") and its integrity record
([integrity.json](../archive/evidence/executions/20261020/repository-reconciliation/integrity.json)).

| Path | Bytes | SHA-256 | Classification |
|---|---:|---|---|
| `evidence/research_checkpoint_20261007/raw/bgs_astra_corrected_integral/compact_portability_check.json` | 6414 | `b8b8932a073a9809507353a247020d1edcaa741a3ffccc7e5eeac232f3661cbd` | Preserved progress-prefixed log with valid trailing JSON (JSON begins at byte offset 35) |
| `evidence/schur_reduction_20261007/raw/review/failed_attempts/attempt1/checks.json` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | Preserved empty failed-attempt output |
| `evidence/schur_reduction_20261007/raw/review/failed_attempts/attempt2/checks.json` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | Preserved empty failed-attempt output |
