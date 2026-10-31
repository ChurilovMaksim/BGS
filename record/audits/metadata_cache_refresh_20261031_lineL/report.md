# Metadata cache refresh, 31 October 2026: Line L

## Why this snapshot exists

The Line L integration (Lines L, L2, L3; BGS-TRACE-248…268, `mathematics/fixed-map/lineL_op_open_range.md`) adds twenty-one claims and adds
dependencies to BGS-TRACE-244, 245 and 246 (state reviews open/conditional → proved). It registers **no new external reference**
and changes **no registry field** of `literature/external_dependencies.json`. Several new claims depend transitively on claims
that use external theorems (through Lemma W3, BGS-TRACE-243, on the Weil bound, and through Theorem W / Theorem K on Theorem J3),
so the transitive impact sets of five records change. Without a refresh, `bibliographic_metadata_audit.py` reports graph drift.

This snapshot is `evidence/source_metadata/registry_metadata_20261031_lineL.json` (sha256 in the `.sha256` file next to it).
* It carries forward the 64 records of `registry_metadata_20261031_lineK.json` (`current_review.previous_snapshot_sha256`).
* Only the transitive claim sets of the five records below are refreshed (no direct use is added or removed; no
  `file_level_claim_matches` change, since no new claim cites an external theorem directly):

| record | transitive claims added |
|---|---|
| EXT-DIRICHLET-1837 | BGS-TRACE-257, 258 |
| EXT-VINOGRADOV-1937 | BGS-TRACE-257, 258 |
| EXT-WEYL-1916 | BGS-TRACE-257, 258 |
| EXT-DAVENPORT-1980 | BGS-TRACE-257, 258 |
| EXT-WEIL-1948 | BGS-TRACE-250, 251, 252, 253, 257, 258, 260, 262, 267 |

* The pre-existing EXT-BR-1975 drift (stored cache vs the main graph, present on main) is **not** refreshed here; the bibliographic
  audit still reports it, as on main.

Standard results used in Line L without an external-dependency record (as for other textbook facts in the registry): the
Neumann/Graf addition theorem for Bessel functions (Theorem U), Minkowski's convex-body theorem for a cube (Lemma B2) and Cauchy's root
bound (L2-F2), the Jacobi–Anger expansion (L3 S1). They are named in the claim boundaries.

The pointer `literature/metadata_audit.json` now names this snapshot, its digest and this report.
`computations/maintenance/v4_negative_controls.py` mutates the current cache file in one negative control; its path (a data
string) was updated from the Line K snapshot to this one. No check was weakened.
