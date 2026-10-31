# Metadata cache refresh, 31 October 2026: Lines M and N

## Why this snapshot exists

The Lines M/N integration (BGS-TRACE-269…285, `mathematics/fixed-map/lineMN_conductor_structure.md`) adds seventeen claims. It also
adds the dependency BGS-TRACE-283 to BGS-TRACE-246 and 258 (annotations; states unchanged). It registers **four new external
references** for Line N:

| record | used directly by | review |
|---|---|---|
| EXT-OSV-2023 | BGS-TRACE-279, 280 | Lemma 4.3 (absolute irreducibility) |
| EXT-OSV-2024 | BGS-TRACE-279, 280 | Lemma 2.1 (Voloch's point count, cited via OSV) |
| EXT-CP-2011 | BGS-TRACE-279, 280 | Theorem 1.1 (explicit Heath-Brown–Konyagin) |
| EXT-BOURGAIN-2005 | BGS-TRACE-281 | Theorem 1 / Corollary (1.21), Remark (1), §5(1) |

The review record is `literature/lineMN_sources_20261031.md`. No registry field of an older record changes. Several new claims depend
transitively on claims that use external theorems, so the transitive impact sets of five older records change:

| record | transitive claims added |
|---|---|
| EXT-DIRICHLET-1837 | BGS-TRACE-270, 271, 278, 279, 280, 281, 282, 284 |
| EXT-VINOGRADOV-1937 | BGS-TRACE-270, 271, 278, 279, 280, 281, 282, 284 |
| EXT-WEYL-1916 | BGS-TRACE-270, 271, 278, 279, 280, 281, 282, 284 |
| EXT-DAVENPORT-1980 | BGS-TRACE-270, 271, 278, 279, 280, 281, 282, 284 |
| EXT-WEIL-1948 | BGS-TRACE-271, 278, 279, 280, 281, 282, 283, 284 |

## The snapshot

This snapshot is `evidence/source_metadata/registry_metadata_20261031_lineMN.json` (sha256 in the `.sha256` file next to it).
* It carries forward the 64 records of `registry_metadata_20261031_lineL.json` (`current_review.previous_snapshot_sha256`).
* It refreshes only the impact sets above and adds the four new records (68 in total).
* The pre-existing EXT-BR-1975 drift (stored cache vs the main graph, present on main) is **not** refreshed here. The bibliographic audit
  still reports it, as on main.

Cited only as annotation or context, with no record (see the review note):
* Kurlberg–Rudnick, CMP 222 (2001), volume verified;
* Bourgain–Glibichuk–Konyagin (JLMS 2006);
* Bourgain, J. Anal. Math. 101 (2007) (the open BGS-TRACE-282);
* Faure–Nonnenmacher–De Bièvre;
* Stewart.

## Other updates

* The pointer `literature/metadata_audit.json` now names this snapshot, its digest and this report.
* `computations/maintenance/v4_negative_controls.py` mutates the current cache file in one negative control. Its path, a data string,
  was updated from the Line L snapshot to this one.
* Data lists were extended for the four new ids:
  * the `allowed` set of `computations/verification/wave2_integration_audit.py` and its docstring count (25 → 29);
  * the expected count in `computations/maintenance/tests/test_external_epoch_preservation.py` ((39, 25) → (39, 29));
  * `external_dependency_extension.added_ids` and its scope in `record/claim_integration_epochs.json`.

No check was weakened.
