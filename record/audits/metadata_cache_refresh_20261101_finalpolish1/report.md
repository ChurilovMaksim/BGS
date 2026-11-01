# Metadata cache refresh, 1 November 2026: EXT-BR-1975 impact review (final-polish-1)

## Why
Since commit 469debb9 (27 October 2026) `bibliographic_metadata_audit.py` has failed on main with
`EXT-BR-1975: dependency graph changed`. The metadata refreshes for Lines I, J, K, L, M/N, N2–N4 and N5–N18b all recorded this
drift and deliberately left it alone. This refresh is the explicit impact review those reports deferred.

## Impact review
* EXT-BR-1975 (Bowen–Ruelle 1975) has one direct consumer, BGS-TRACE-113 (uniform original-family power-trace bound). This is
  unchanged.
* BGS-TRACE-116 ("Original-family compact pair test transfers through O(N^-2) matrix error", proved) depends on BGS-TRACE-113 and
  BGS-TRACE-115. Its registered boundary says it uses "existing TRACE-113 and its inherited external input". So it uses EXT-BR-1975
  only transitively, through BGS-TRACE-113. It does not apply the external theorem directly, and it changes no locator, mapping or
  application hypothesis.
* The impact set of EXT-BR-1975 therefore gains BGS-TRACE-116, as a transitive dependency only.

## Snapshot
`evidence/source_metadata/registry_metadata_20261101_finalpolish1.json` (+ `.sha256`):
* it carries forward the 68 records of `registry_metadata_20261101_lineNgas.json`
  (`current_review.previous_snapshot_sha256`);
* it adds BGS-TRACE-116 to `transitive_claim_dependencies` of EXT-BR-1975, which is the only record change;
* the previous `current_review` (Lines N5–N18b) moves to `supplemental_review_provenance` as
  `metadata_cache_refresh_20261101_lineNgas_carried_forward`.

No source observation, review hash, registry field or claim state changed. `literature/metadata_audit.json` now points to this
snapshot, and `computations/maintenance/v4_negative_controls.py` tampers the new digest-pinned cache.

## Result
`bibliographic_metadata_audit.py` and `--self-test` exit 0 (68 cached identities match; 614 mutation tests passed).
Non-claim: metadata agreement does not establish theorem applicability.
