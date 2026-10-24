# Metadata cache refresh, 24 October 2026: P2-MATH wave 9A provenance

## Why this snapshot exists

After the phase-2 P2-MATH wave 9A move (first half of the fixed-map wave:
62 notes, alphabetical split at `frozen_phase_finite_type.md`),
`computations/verification/bibliographic_metadata_audit.py --self-test`
failed on the post-move tree with exactly 13 errors: one
`project_sources differs from reviewed cache` error for each of the 12
sealed contracts whose registry paths moved in this subwave, and one for
the admitted-later contract EXT-BR-1975 (whose dated note was renamed to
a subject name).

```
EXT-BH-2026: project_sources differs from reviewed cache
EXT-CK-2006: project_sources differs from reviewed cache
EXT-EV-2015: project_sources differs from reviewed cache
EXT-PP-1990: project_sources differs from reviewed cache
EXT-POPESCU-2023: project_sources differs from reviewed cache
EXT-ROY-2016: project_sources differs from reviewed cache
EXT-FORRESTER-1996: project_sources differs from reviewed cache
EXT-DE-2001: project_sources differs from reviewed cache
EXT-KLZF-2022: project_sources differs from reviewed cache
EXT-SOSH-2000: project_sources differs from reviewed cache
EXT-KT-2009: project_sources differs from reviewed cache
EXT-KELMER-2008: project_sources differs from reviewed cache
EXT-BR-1975: project_sources differs from reviewed cache
```

Diagnosis: the registry (`literature/external_dependencies.json`) names the
new `mathematics/fixed-map/` paths for these contracts (migrated in the
same P2-MATH wave 9A commit, with reviewed amendment rows in
`record/external_epoch_amendments.json` for the sealed external-epoch
seal, except EXT-BR-1975 which is admitted-later and needs no store row),
while the reviewed cache selected by `literature/metadata_audit.json`
still accepted the pre-move `mathematics/` root paths. A field-by-field
comparison of all 57 registered references against the cache found these
13 field values to be the only divergence in the accepted fields.

## Review basis

Phase-2 package P2-MATH wave 9A (see `archive/MANIFEST-P2MATH9A.md`) moved
62 fixed-map notes from the `mathematics/` root into the topical home
`mathematics/fixed-map/` per `record/mathematics_topics.json` (4 dated
names renamed to subject names) and migrated every live consumer in the
same commit, including the registry paths above. The reviewed cache was
not refreshed by that move; its stated policy is explicit reviewed
selection with no automatic refresh, so the divergence persisted until
this review.

Two precisions, stated honestly:

- The 12 contracts other than EXT-BR-1975 are SEALED external-epoch rows
  (39-contract snapshot of 2026-10-07), unlike the admitted-later
  EXT-BR-1975 (Pittel-line precedent). The cache refresh and the epoch
  amendment rows are two separate gates for the same migration: the rows
  in `record/external_epoch_amendments.json` admit the change to the
  external-epoch checker, and this snapshot admits it to the
  bibliographic guard, which compares every registry row (sealed and
  admitted alike) against the reviewed cache. Neither mechanism
  substitutes for the other. EXT-BR-1975 takes the cache-only path: no
  store row exists or is needed for it. EXT-SOSH-2000's row extends the
  wave-4 row (its sealed list also names a wave-4 returns note); the
  extension keeps the wave-4 element and the sealed old value.
- The moved notes are link-translated copies where cross-boundary links
  changed (see MANIFEST-P2MATH9A §2); the registry migration itself is a
  pure path relocation. No source was re-reviewed, no observation
  re-retrieved, and no review hash changed: every source observation,
  including the 12 contracts' review hashes, is carried forward unchanged
  from the P2-MATH wave 4 snapshot (SHA-256
  3f84faf500161b3a6cf9cd10192874af27dfdbc3893c54c3b7b30400bc7b2826).
  The snapshot also updates the duplicated top-level `project_sources`
  copies, the `file_level_claim_matches[].source` copies and the
  `review_paths` copies of the same records so the snapshot stays
  internally consistent; the guard compares only the accepted fields.

## Scope

Provenance-only refresh. No new source review, no fresh retrieval, no claim
state change, no graph impact change (no claim's `external_dependencies`
changed in this subwave). The superseded P2-MATH wave 4 snapshot is preserved
byte-identically; this snapshot chains to it via
`current_review.previous_snapshot_sha256`.

## Result

New snapshot `evidence/source_metadata/registry_metadata_20261024_p2math9a.json`
(SHA-256 6d4425df12eb9f6168e7df6960ceb524546ceef81a0dfef30f3b1f178a3a92ad)
+ `…_p2math9a.sha256`, pointer `literature/metadata_audit.json` repointed
by exactly 3 lines (cache, digest, review). Self-test after refresh: rc=0.
Diff vs the superseded snapshot is exactly 66 path-copy leaves plus
`scope` + `current_review.{record, previous_snapshot_sha256, scope}`.
