# Metadata cache refresh, 24 October 2026: P2-MATH wave 8 provenance

## Why this snapshot exists

After the phase-2 P2-MATH wave 8 move,
`computations/verification/bibliographic_metadata_audit.py --self-test`
failed on the post-move tree with exactly five errors:

```
EXT-BAB-2013: project_sources differs from reviewed cache
EXT-POPESCU-2023: project_sources differs from reviewed cache
EXT-BG-2008: project_sources differs from reviewed cache
EXT-GAE-2007: project_sources differs from reviewed cache
EXT-DIRICHLET-1837: project_sources differs from reviewed cache
```

Diagnosis: the registry (`literature/external_dependencies.json`) names the
new `mathematics/spectral-obstructions/` paths for the five sealed contracts
(migrated in the same P2-MATH wave 8 commit, with reviewed amendment rows in
`record/external_epoch_amendments.json` for the external-epoch seal), while
the reviewed cache selected by `literature/metadata_audit.json` still
accepted the pre-move `mathematics/` root paths. A field-by-field comparison
of all 57 registered references against the cache found these five field
values to be the only divergence in the accepted fields.

## Review basis

Phase-2 package P2-MATH wave 8 (see `archive/MANIFEST-P2MATH8.md`) moved ten
spectral-obstructions notes from the `mathematics/` root into the topical
home `mathematics/spectral-obstructions/` per `record/mathematics_topics.json`
(three dated names renamed to subject names) and migrated every live
consumer in the same commit, including the registry paths above. The
reviewed cache was not refreshed by that move; its stated policy is explicit
reviewed selection with no automatic refresh, so the divergence persisted
until this review.

Two precisions, stated honestly:

- The five contracts are SEALED external-epoch rows (39-contract snapshot of
  2026-10-07), unlike the admitted-later contracts of the Pittel (20261023)
  and P2-SPECTRAL (20261024) refresh precedents. The cache refresh and the
  epoch amendment rows are two separate gates for the same migration: the
  rows in `record/external_epoch_amendments.json` admit the change to the
  external-epoch checker, and this snapshot admits it to the bibliographic
  guard, which compares every registry row (sealed and admitted alike)
  against the reviewed cache. Neither mechanism substitutes for the other.
- The moved notes are link-translated copies where cross-boundary links
  changed (see MANIFEST-P2MATH8 §2); the registry migration itself is a
  pure path relocation. No source was re-reviewed, no observation
  re-retrieved, and no review hash changed: every source observation,
  including the five contracts' review hashes, is carried forward unchanged
  from the wave 4 snapshot (SHA-256
  83b0639f1d69e4578ea532ba2d0574c6d88f35a97c2fa4a5c1ddf11d3d8df36c).
  The snapshot also updates the duplicated top-level `project_sources`
  copies and the `file_level_claim_matches[].source` copies of the five
  records (they mirror the accepted fields) so the snapshot stays internally
  consistent; the guard compares only the accepted fields.

## Scope

Provenance-only refresh. No new source review, no fresh retrieval, no claim
state change, no graph impact change (no claim's `external_dependencies`
changed in this wave). The superseded wave 4 snapshot is preserved
byte-identically; this snapshot chains to it via
`current_review.previous_snapshot_sha256`.
