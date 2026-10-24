# Metadata cache refresh, 24 October 2026: P2-MATH wave 6 provenance

## Why this snapshot exists

After the phase-2 P2-MATH wave 6 move,
`computations/verification/bibliographic_metadata_audit.py --self-test`
failed on the post-move tree with exactly ten errors:

```
EXT-VM-2015: project_sources differs from reviewed cache
EXT-CZ-2013: project_sources differs from reviewed cache
EXT-FKM-2014: project_sources differs from reviewed cache
EXT-BLV-2009: project_sources differs from reviewed cache
EXT-IK-2004: project_sources differs from reviewed cache
EXT-WANG-1982: project_sources differs from reviewed cache
EXT-FI-1980: project_sources differs from reviewed cache
EXT-ZAGIER-1997: project_sources differs from reviewed cache
EXT-BORDA-2020: project_sources differs from reviewed cache
EXT-BT-1971: project_sources differs from reviewed cache
```

Diagnosis: the registry (`literature/external_dependencies.json`) names the
new `mathematics/cayley-arithmetic/` paths for the ten contracts (migrated
in the same P2-MATH wave 6 commit), while the reviewed cache selected by
`literature/metadata_audit.json` still accepted the pre-move `mathematics/`
root paths. A field-by-field comparison of all 57 registered references
against the cache found these ten field values to be the only divergence
in the accepted fields.

## Review basis

Phase-2 package P2-MATH wave 6 (see `archive/MANIFEST-P2MATH6.md`) moved
36 cayley-arithmetic notes from the `mathematics/` root into the topical
home `mathematics/cayley-arithmetic/` per `record/mathematics_topics.json`
and migrated every live consumer in the same commit, including the
registry paths above. The reviewed cache was not refreshed by that move;
its stated policy is explicit reviewed selection with no automatic
refresh, so the divergence persisted until this review.

Two precisions, stated honestly:

- Five of the ten contracts are SEALED external-epoch rows (39-contract
  snapshot of 2026-10-07): EXT-VM-2015, EXT-CZ-2013, EXT-FKM-2014,
  EXT-BLV-2009, EXT-IK-2004. For them the cache refresh and the epoch
  amendment rows are two separate gates for the same migration: the rows
  in `record/external_epoch_amendments.json` admit the change to the
  external-epoch checker, and this snapshot admits it to the bibliographic
  guard, which compares every registry row (sealed and admitted alike)
  against the reviewed cache. Neither mechanism substitutes for the other.
  The other five contracts (EXT-WANG-1982, EXT-FI-1980, EXT-ZAGIER-1997,
  EXT-BORDA-2020, EXT-BT-1971) are admitted-later rows, which the
  external-epoch checker does not byte-compare; for them this cache
  refresh is the only epoch-class gate, following the Pittel (20261023)
  and P2-SPECTRAL (20261024) refresh precedents.
- The moved notes are link-translated copies where cross-boundary links
  changed (see MANIFEST-P2MATH6 §2); the registry migration itself is a
  pure path relocation. No source was re-reviewed, no observation
  re-retrieved, and no review hash changed: every source observation,
  including the ten contracts' review hashes, is carried forward unchanged
  from the 2026-10-24 wave-4 refresh snapshot (SHA-256
  3f84faf500161b3a6cf9cd10192874af27dfdbc3893c54c3b7b30400bc7b2826).
  The snapshot also updates the duplicated top-level `project_sources`
  copies of the five sealed records (they mirror the accepted fields) so
  the snapshot stays internally consistent; the guard compares only the
  accepted fields. The five admitted-later records carry no top-level
  `project_sources` copy.

## Scope

Provenance-only refresh. No new source review, no fresh retrieval, no claim
state change, no graph impact change (no claim's `external_dependencies`
changed in this wave). The superseded 2026-10-24 wave-4 snapshot is
preserved byte-identically; this snapshot chains to it via
`current_review.previous_snapshot_sha256`.
