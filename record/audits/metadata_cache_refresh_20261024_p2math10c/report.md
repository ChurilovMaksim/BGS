# Metadata cache refresh, 24 October 2026: P2-MATH wave 10c provenance

## Why this snapshot exists

After the phase-2 P2-MATH wave 10c move,
`computations/verification/bibliographic_metadata_audit.py --self-test`
failed on the post-move tree with exactly 2 errors, one per
touched contract:

```
EXT-AGG-1989: project_sources differs from reviewed cache
EXT-STANLEY-1981: project_sources differs from reviewed cache
```

Diagnosis: the registry (`literature/external_dependencies.json`) names the
new `mathematics/trace-bridge/` paths for the touched contracts (migrated in
the same P2-MATH wave 10c commit, with reviewed amendment rows in
`record/external_epoch_amendments.json` for the sealed ones), while the
reviewed cache selected by `literature/metadata_audit.json` still accepted
the pre-move `mathematics/` root paths. A field-by-field comparison of all
57 registered references against the cache found these field values to be
the only divergence in the accepted fields.

## Review basis

Phase-2 package P2-MATH wave 10c (see `archive/MANIFEST-P2MATH10c.md`)
moved 25 trace-bridge notes from the `mathematics/` root into
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
  changed (see MANIFEST-P2MATH10c §2); the registry migration itself is a
  pure path relocation. No source was re-reviewed, no observation
  re-retrieved, and no review hash changed: every source observation,
  including the touched contracts' review hashes, is carried forward unchanged
  from the registry_metadata_20261024_p2math10b.json snapshot (SHA-256 08772757efe24322e1becf15c72930d3f6f1f458e3b312cb5a5bb000d5d7e071).
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
