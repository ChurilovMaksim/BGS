# Metadata cache refresh, 24 October 2026: P2-MATH wave 10a provenance

## Why this snapshot exists

After the phase-2 P2-MATH wave 10a move,
`computations/verification/bibliographic_metadata_audit.py --self-test`
failed on the post-move tree with exactly 8 errors, one per
touched contract:

```
EXT-BHATIA-2002: project_sources differs from reviewed cache
EXT-DE-2001: project_sources differs from reviewed cache
EXT-HSW-1999: project_sources differs from reviewed cache
EXT-JM-2015: project_sources differs from reviewed cache
EXT-MATSUMOTO-2007: project_sources differs from reviewed cache
EXT-OO-1997: project_sources differs from reviewed cache
EXT-VV-2017: project_sources differs from reviewed cache
EXT-ZIRN-2021: project_sources differs from reviewed cache
```

Diagnosis: the registry (`literature/external_dependencies.json`) names the
new `mathematics/trace-bridge/` paths for the touched contracts (migrated in
the same P2-MATH wave 10a commit, with reviewed amendment rows in
`record/external_epoch_amendments.json` for the sealed ones), while the
reviewed cache selected by `literature/metadata_audit.json` still accepted
the pre-move `mathematics/` root paths. A field-by-field comparison of all
57 registered references against the cache found these field values to be
the only divergence in the accepted fields.

## Review basis

Phase-2 package P2-MATH wave 10a (see `archive/MANIFEST-P2MATH10a.md`)
moved 22 trace-bridge notes from the `mathematics/` root into
the topical home `mathematics/trace-bridge/` per
`record/mathematics_topics.json` and migrated every live consumer in the same
commit, including the registry paths above. The reviewed cache was not
refreshed by that move; its stated policy is explicit reviewed selection
with no automatic refresh, so the divergence persisted until this review.

Two precisions, stated honestly:

- The sealed contracts among the touched set (if any) are SEALED
  external-epoch rows (39-contract snapshot of 2026-10-07). The cache refresh
  and the epoch amendment rows are two separate gates for the same migration:
  the rows in `record/external_epoch_amendments.json` admit the change to the
  external-epoch checker, and this snapshot admits it to the bibliographic
  guard, which compares every registry row (sealed and admitted alike)
  against the reviewed cache. Neither mechanism substitutes for the other.
  Admitted-later contracts migrate directly in the registry and are accepted
  here by the same provenance-only refresh.
- The moved notes are link-translated copies where cross-boundary links
  changed (see MANIFEST-P2MATH10a §2); the registry migration itself is a
  pure path relocation. No source was re-reviewed, no observation
  re-retrieved, and no review hash changed: every source observation,
  including the touched contracts' review hashes, is carried forward unchanged
  from the registry_metadata_20261024_p2math5.json snapshot (SHA-256 9977d815fb9b4e43b55faf58bf7f8330753a422f2138da38b104c7f61895c3cc).
  The snapshot also updates the duplicated top-level `project_sources`
  copies of the touched records (they mirror the accepted fields) so the
  snapshot stays internally consistent; the guard compares only the
  accepted fields.

## Scope

Provenance-only refresh. No new source review, no fresh retrieval, no claim
state change, no graph impact change (no claim's `external_dependencies`
changed in this wave). The superseded snapshot is preserved
byte-identically; this snapshot chains to it via
`current_review.previous_snapshot_sha256`.
