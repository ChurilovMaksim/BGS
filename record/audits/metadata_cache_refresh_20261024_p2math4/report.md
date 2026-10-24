# Metadata cache refresh, 24 October 2026: P2-MATH wave 4 provenance

## Why this snapshot exists

After the phase-2 P2-MATH wave 4 move,
`computations/verification/bibliographic_metadata_audit.py --self-test`
failed on the post-move tree with exactly five errors:

```
EXT-SOSH-2000: project_sources differs from reviewed cache
EXT-SOSH-2000: additional_uses differs from reviewed cache
EXT-CC-2013: project_sources differs from reviewed cache
EXT-PY-2015: project_sources differs from reviewed cache
EXT-DH-2011: project_sources differs from reviewed cache
```

Diagnosis: the registry (`literature/external_dependencies.json`) names the
new `mathematics/returns/` paths for the four sealed contracts (migrated in
the same P2-MATH wave 4 commit, with reviewed amendment rows in
`record/external_epoch_amendments.json` for the external-epoch seal), while
the reviewed cache selected by `literature/metadata_audit.json` still
accepted the pre-move `mathematics/` root paths. A field-by-field comparison
of all 57 registered references against the cache found these five field
values to be the only divergence in the accepted fields.

## Review basis

Phase-2 package P2-MATH wave 4 (see `archive/MANIFEST-P2MATH4.md`) moved nine
returns notes from the `mathematics/` root into the topical home
`mathematics/returns/` per `record/mathematics_topics.json` and migrated every
live consumer in the same commit, including the registry paths above. The
reviewed cache was not refreshed by that move; its stated policy is explicit
reviewed selection with no automatic refresh, so the divergence persisted
until this review.

Two precisions, stated honestly:

- The four contracts are SEALED external-epoch rows (39-contract snapshot of
  2026-10-07), unlike the admitted-later contracts of the Pittel (20261023)
  and P2-SPECTRAL (20261024) refresh precedents. The cache refresh and the
  epoch amendment rows are two separate gates for the same migration: the
  rows in `record/external_epoch_amendments.json` admit the change to the
  external-epoch checker, and this snapshot admits it to the bibliographic
  guard, which compares every registry row (sealed and admitted alike)
  against the reviewed cache. Neither mechanism substitutes for the other.
- The moved notes are link-translated copies where cross-boundary links
  changed (see MANIFEST-P2MATH4 §2); the registry migration itself is a
  pure path relocation. No source was re-reviewed, no observation
  re-retrieved, and no review hash changed: every source observation,
  including the four contracts' review hashes, is carried forward unchanged
  from the 2026-10-24 refresh snapshot (SHA-256
  16e01d7975ff75f79af0462388b4747eae907c41798949cea1aa1560180ba711).
  The snapshot also updates the duplicated top-level `project_sources`
  copies of the four records (they mirror the accepted fields) so the
  snapshot stays internally consistent; the guard compares only the
  accepted fields.

## Scope

Provenance-only refresh. No new source review, no fresh retrieval, no claim
state change, no graph impact change (no claim's `external_dependencies`
changed in this wave). The superseded 2026-10-24 refresh snapshot is
preserved byte-identically; this snapshot chains to it via
`current_review.previous_snapshot_sha256`.
