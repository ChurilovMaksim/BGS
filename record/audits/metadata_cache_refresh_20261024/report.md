# Metadata cache refresh, 24 October 2026: EXT-BR-1975 provenance

## Why this snapshot exists

After the phase-2 P2-SPECTRAL move,
`computations/verification/bibliographic_metadata_audit.py --self-test`
failed on the post-move tree with a single error:

```
EXT-BR-1975: project_sources differs from reviewed cache
```

Diagnosis: the registry (`literature/external_dependencies.json`) names
`record/spectral_research/trace_closure.md` among the EXT-BR-1975 project
sources (migrated in the same P2-SPECTRAL commit), while the reviewed cache
selected by `literature/metadata_audit.json` still accepted the pre-move path
`record/trace_closure_20261022.md`. A field-by-field comparison of all 57
registered references against the cache found this one string to be the only
divergence in the accepted fields.

## Review basis

Phase-2 package P2-SPECTRAL (see `archive/MANIFEST-P2SPECTRAL.md`) moved the
three spectral-line documents from the root of `record/` into the line's home
`record/spectral_research/` with dates stripped from their names, and migrated
every live consumer in the same commit, including the EXT-BR-1975
`project_sources[2]` value. The reviewed cache was not refreshed by that move;
its stated policy is explicit reviewed selection with no automatic refresh, so
the divergence persisted until this review.

Two precisions, stated honestly because they differ from the 20261023 precedent:
- The Pittel move (phase-1 package C) was byte-identical; this move is not.
  The moved `trace_closure.md` differs from the old path only by link-geometry
  translation (its markdown links re-expressed for the deeper directory, as
  recorded in MANIFEST-P2SPECTRAL §1); no mathematical content changed.
- That distinction does not touch what the cache certifies for EXT-BR-1975.
  The cache's accepted field is a project-internal file location, and the
  external source observation is untouched: the Bowen–Ruelle published PDF
  hash and the review hash recorded in the EXT-BR-1975 source observation are
  carried forward verbatim, as are all other observations. The moved file is a
  project note, not the external source itself.

The gate for the move itself was settled before assembly: EXT-BR-1975 is not
one of the 39 historical external contracts (it belongs to the 18 explicitly
admitted later inputs), so migrating its `project_sources` is a consumer
migration, not an epoch amendment; `test_external_epoch_preservation` passes
6/6 on the post-move tree.

## What this snapshot changes

Following the succession practice of the 2026-10-22 recheck and the 20261023
refresh, this snapshot
(`evidence/source_metadata/registry_metadata_20261024_refresh.json`)
supersedes `registry_metadata_20261023_refresh.json`, which is preserved
byte-identically; the pointer `literature/metadata_audit.json` now selects
this snapshot and its adjacent digest, with its policy line unchanged.
All 57 records are carried forward; exactly one accepted field changes:

- EXT-BR-1975, `accepted_registry_fields.project_sources`:
  `record/trace_closure_20261022.md` →
  `record/spectral_research/trace_closure.md`.

Every `source_observations` block — including the EXT-BR-1975 review path and
hash, a historical observation of where the review was recorded — is preserved
verbatim. The superseded snapshot's `current_review` is carried into
`supplemental_review_provenance` as
`metadata_cache_refresh_20261023_carried_forward`, as the previous succession
did for the recheck review. The snapshot's `checked_on`, `scope` and
`current_review` are updated to this refresh (previous snapshot SHA-256
`c27cff0f8593af9373e6822e2ab499bdd1455e6a63943a5c7e1ec69007fb2a7c`;
new snapshot SHA-256
`16e01d7975ff75f79af0462388b4747eae907c41798949cea1aa1560180ba711`).
No registry field, claim state, dependency-graph entry or bibliographic fact
changes.

## Verification

`bibliographic_metadata_audit.py --self-test` passes (515 mutation tests)
and the full audit run reports 57 cached identities matching, with the
recorded application coverage unchanged and the claim-dependency impact
sets still in agreement. The superseded snapshot and its digest verify
byte-identically against their pre-refresh hashes.

This refresh certifies only that the reviewed cache again agrees with the
registry on a project-internal file location. It is not a fresh source
review, a theorem-applicability verdict, or a claim-state change.
