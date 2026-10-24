# Metadata cache refresh, 24 October 2026: P2-MATH wave 5 provenance

## Why this snapshot exists

After the phase-2 P2-MATH wave 5 move,
`computations/verification/bibliographic_metadata_audit.py --self-test`
failed on the post-move tree with exactly three errors:

```
EXT-DR-2009: project_sources differs from reviewed cache
EXT-DEMNI-2016: project_sources differs from reviewed cache
EXT-COSY-2024: project_sources differs from reviewed cache
```

Diagnosis: the registry (`literature/external_dependencies.json`) names the
new `mathematics/pell/` paths for the three sealed contracts (migrated in
the same P2-MATH wave 5 commit, with reviewed amendment rows in
`record/external_epoch_amendments.json` for the external-epoch seal), while
the reviewed cache selected by `literature/metadata_audit.json` still
accepted the pre-move `mathematics/` root paths. A field-by-field comparison
of all 57 registered references against the cache found these three field
values to be the only divergence in the accepted fields.

## Review basis

Phase-2 package P2-MATH wave 5 (see `archive/MANIFEST-P2MATH5.md`) moved
seventeen pell notes from the `mathematics/` root into the topical home
`mathematics/pell/` per `record/mathematics_topics.json` and migrated every
live consumer in the same commit, including the registry paths above. The
reviewed cache was not refreshed by that move; its stated policy is explicit
reviewed selection with no automatic refresh, so the divergence persisted
until this review.

Two precisions, stated honestly:

- The three contracts are SEALED external-epoch rows (39-contract snapshot of
  2026-10-07), as in the wave 4 precedent. The cache refresh and the
  epoch amendment rows are two separate gates for the same migration: the
  rows in `record/external_epoch_amendments.json` admit the change to the
  external-epoch checker, and this snapshot admits it to the bibliographic
  guard, which compares every registry row (sealed and admitted alike)
  against the reviewed cache. Neither mechanism substitutes for the other.
- The moved notes are link-translated copies only where a cross-boundary
  link changed (see MANIFEST-P2MATH5 §2); the registry migration itself is
  a pure path relocation. No source was re-reviewed, no observation
  re-retrieved, and no review hash changed: every source observation,
  including the three contracts' review hashes, is carried forward unchanged
  from the 2026-10-24_p2math6 snapshot (SHA-256
  ae93dc33fe4f1468db2b61a65092e1a360d003b8dd34362c7f627b63755a7e3e).
  The snapshot also updates the duplicated top-level `project_sources`
  copies of the three records and their `file_level_claim_matches` source
  mirrors (RET-001/RET-002 claim sources, which moved in the same wave) so
  the snapshot stays internally consistent; the guard compares only the
  accepted fields.

## Scope

Provenance-only refresh. No new source review, no fresh retrieval, no claim
state change, no graph impact change (no claim's `external_dependencies`
changed in this wave). The superseded 2026-10-24_p2math6 snapshot is
preserved byte-identically; this snapshot chains to it via
`current_review.previous_snapshot_sha256`.

## Leaf diff vs the superseded snapshot

Exactly 12 leaves: 8 path leaves (accepted `project_sources` ×3,
duplicated top-level `project_sources` ×3, `file_level_claim_matches`
source ×2 for the two claims whose sources moved) + `scope` +
`current_review.{record, previous_snapshot_sha256, scope}`. New snapshot
SHA-256: 9977d815fb9b4e43b55faf58bf7f8330753a422f2138da38b104c7f61895c3cc
(see `evidence/source_metadata/registry_metadata_20261024_p2math5.sha256`).
