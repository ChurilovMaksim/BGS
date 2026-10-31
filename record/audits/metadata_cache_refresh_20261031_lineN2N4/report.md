# Metadata cache refresh, 31 October 2026: Lines N2–N4

## Why this snapshot exists

The Lines N2–N4 integration (BGS-TRACE-286…298, `mathematics/fixed-map/lineN2N4_inherited_level.md`) adds thirteen claims. It also adds
two dependencies: BGS-TRACE-277 to BGS-TRACE-266 (scope widening, state unchanged) and BGS-TRACE-293 to BGS-TRACE-276 (state unchanged).
It registers **no new external reference**. No registry field of any record changes (the owner audit of PR #66, R2, found the stale
impact sets).

Some new claims depend transitively on claims that use external theorems, so the transitive impact sets of five older records change:

| record | transitive claims added |
|---|---|
| EXT-DIRICHLET-1837 | BGS-TRACE-286, 287 |
| EXT-VINOGRADOV-1937 | BGS-TRACE-286, 287 |
| EXT-WEYL-1916 | BGS-TRACE-286, 287 |
| EXT-DAVENPORT-1980 | BGS-TRACE-286, 287 |
| EXT-WEIL-1948 | BGS-TRACE-286, 287, 289, 290, 294, 296 |

The paths run through these claims:
* BGS-TRACE-235, 245 and 246 (Theorem K3, Theorem W, K2′) for 286 and 287;
* additionally 241 and 253 for 286 (EXT-WEIL-1948);
* BGS-TRACE-250 (OP_abs) for 289, 290 and 294;
* 289, 290 and 294 for 296. They are
transitive only: the new claims do not apply these theorems directly.

## The snapshot

`evidence/source_metadata/registry_metadata_20261031_lineN2N4.json` (sha256 in the `.sha256` file next to it):
* carries forward the 68 records of `registry_metadata_20261031_lineMN.json` (`current_review.previous_snapshot_sha256`);
* refreshes only the impact sets listed above, and adds no record.

The pre-existing EXT-BR-1975 drift (stored cache vs the main graph, present on main) is **not** refreshed here. The bibliographic audit
still reports it, as on main.

Cited only as a remark, with no record: Cao–Feng–Huang (2008), the pressure interpretation in BGS-TRACE-288 (not registered).
