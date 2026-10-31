# Metadata cache refresh, 1 November 2026: Lines N5–N18b (gas route)

## Why
The Lines N5–N19b integration (BGS-TRACE-299..324, `mathematics/fixed-map/lineN5N18_gas_conditional.md`) adds 26 claims. It adds no
external reference and changes no registry field. It does not change any dependency of an older claim. Some new claims depend
transitively on claims that use external theorems, so the transitive impact sets of nine older records change:

| record | transitive claims added |
|---|---|
| EXT-DIRICHLET-1837, EXT-VINOGRADOV-1937, EXT-WEYL-1916, EXT-DAVENPORT-1980, EXT-OSV-2023, EXT-OSV-2024, EXT-CP-2011, EXT-BOURGAIN-2005 | BGS-TRACE-299, 305 |
| EXT-WEIL-1948 | BGS-TRACE-299, 303, 304, 305, 306, 320 |

The paths run through the Weil-range claims (BGS-TRACE-244, 251, 252, 280, 281, 282), which BGS-TRACE-305 (H7*) cites as partial
coverage, and through Theorem C′ (BGS-TRACE-296) for 304 and 320. All of these are transitive only; no new claim applies an external
theorem directly.

## Snapshot
`evidence/source_metadata/registry_metadata_20261101_lineNgas.json` (+ `.sha256`):
* it carries forward the 68 records of `registry_metadata_20261031_lineN2N4.json` (`current_review.previous_snapshot_sha256`);
* it refreshes only the impact sets above.

The pre-existing EXT-BR-1975 drift, which is present on main, is **not** refreshed.
