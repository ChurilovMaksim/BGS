# Metadata cache refresh, 24 October 2026: P2-MATH wave 9B provenance

## Why this snapshot exists

After the phase-2 P2-MATH wave 9B move (second half of the fixed-map wave:
73 notes, completing the 135-note wave), the bibliographic self-test
failed on the post-move tree with exactly 18 errors: one
`project_sources differs from reviewed cache` error for each of the 17
sealed contracts whose registry paths moved in this subwave (10 contracts
migrating for the first time, 7 contracts whose lists also contain 9A
notes and which were already migrated in 9A), plus a second
`additional_uses differs from reviewed cache` error for EXT-ROY-2016
(whose nested `additional_uses[].project_sources` also moved in 9B).

```
EXT-PESIN-1977: project_sources differs from reviewed cache
EXT-RUELLE-1978: project_sources differs from reviewed cache
EXT-PP-1990: project_sources differs from reviewed cache
EXT-POPESCU-2023: project_sources differs from reviewed cache
EXT-ROY-2016: project_sources differs from reviewed cache
EXT-ROY-2016: additional_uses differs from reviewed cache
EXT-FORRESTER-1996: project_sources differs from reviewed cache
EXT-FAURE-2007: project_sources differs from reviewed cache
EXT-COHEN-2025: project_sources differs from reviewed cache
EXT-RAINS-2003: project_sources differs from reviewed cache
EXT-DE-2001: project_sources differs from reviewed cache
EXT-KLZF-2022: project_sources differs from reviewed cache
EXT-LEMOINE-2025: project_sources differs from reviewed cache
EXT-EHL-2018: project_sources differs from reviewed cache
EXT-GHANMI-2017: project_sources differs from reviewed cache
EXT-KM-2017-BOX: project_sources differs from reviewed cache
EXT-MANE-1981: project_sources differs from reviewed cache
EXT-KELMER-2008: project_sources differs from reviewed cache
```

Diagnosis: the registry (`literature/external_dependencies.json`) names the
new `mathematics/fixed-map/` paths for these contracts (migrated in the
same P2-MATH wave 9B commit, with reviewed amendment rows in
`record/external_epoch_amendments.json` for the sealed external-epoch
seal — 11 new rows, 7 extensions of 9A rows with `9A, extended by 9B`
chaining), while the reviewed cache selected by
`literature/metadata_audit.json` (the 9A snapshot) still accepted the
pre-9B paths. A field-by-field comparison of all 57 registered references
against the cache found these 18 field values to be the only divergence
in the accepted fields.

## Review basis

Phase-2 package P2-MATH wave 9B (see `archive/MANIFEST-P2MATH9B.md`) moved
the remaining 73 fixed-map notes from the `mathematics/` root into the
topical home `mathematics/fixed-map/` per `record/mathematics_topics.json`
(5 dated names renamed to subject names) and migrated every live consumer
in the same commit, including the registry paths above. The reviewed cache
was not refreshed by that move; its stated policy is explicit reviewed
selection with no automatic refresh, so the divergence persisted until
this review.

Two precisions, stated honestly:

- All 17 contracts are SEALED external-epoch rows (39-contract snapshot of
  2026-10-07). The cache refresh and the epoch amendment rows are two
  separate gates for the same migration: the rows in
  `record/external_epoch_amendments.json` admit the change to the
  external-epoch checker, and this snapshot admits it to the
  bibliographic guard, which compares every registry row (sealed and
  admitted alike) against the reviewed cache. Neither mechanism
  substitutes for the other. The 7 extended rows keep their sealed
  old values and historical contract hashes; only their new values,
  wave labels (`9A, extended by 9B`), dispositions (9B sentence appended)
  and reviews (both manifests) changed.
- The moved notes are link-translated copies where cross-boundary links
  changed (see MANIFEST-P2MATH9B §2); the registry migration itself is a
  pure path relocation. No source was re-reviewed, no observation
  re-retrieved, and no review hash changed: every source observation,
  including the 17 contracts' review hashes, is carried forward unchanged
  from the P2-MATH wave 9A snapshot (SHA-256
  6d4425df12eb9f6168e7df6960ceb524546ceef81a0dfef30f3b1f178a3a92ad).
  The snapshot also updates the duplicated top-level `project_sources`
  copies, the `file_level_claim_matches[].source` copies and the
  `review_paths` copies of the same records so the snapshot stays
  internally consistent; the guard compares only the accepted fields.

## Scope

Provenance-only refresh. No new source review, no fresh retrieval, no claim
state change, no graph impact change (no claim's `external_dependencies`
changed in this subwave). The superseded P2-MATH wave 9A snapshot is preserved
byte-identically; this snapshot chains to it via
`current_review.previous_snapshot_sha256`.

## Result

New snapshot `evidence/source_metadata/registry_metadata_20261024_p2math9b.json`
(SHA-256 f75e26a008d6387a5c5bfaa92a5d65f7cd901155254258b93b62174f659a5ced)
+ `…_p2math9b.sha256`, pointer `literature/metadata_audit.json` repointed
by exactly 3 lines (cache, digest, review). Self-test after refresh: rc=0.
Diff vs the superseded snapshot is exactly 66 path-copy leaves plus
`scope` + `current_review.{record, previous_snapshot_sha256, scope}`.
