# Metadata cache refresh, 23 October 2026: EXT-PITTEL-2016 provenance

## Why this snapshot exists

`computations/verification/bibliographic_metadata_audit.py --self-test`
failed on main with a single error:

```
EXT-PITTEL-2016: project_sources differs from reviewed cache
```

Diagnosis: the registry (`literature/external_dependencies.json`) names
`archive/literature/chat_integration_sources_20261016.md` among the
EXT-PITTEL-2016 project sources, while the reviewed cache selected by
`literature/metadata_audit.json` still accepted the pre-move path
`literature/chat_integration_sources_20261016.md`. A field-by-field
comparison of all 57 registered references against the cache found this
one string to be the only divergence.

## Review basis

Phase-1 package C (commit `a99b7de4`) moved the chat-integration journals
to `archive/<original path>` and migrated the registry paths in the same
reviewed package. `archive/MANIFEST-C.md` records the move of
`literature/chat_integration_sources_20261016.md` to
`archive/literature/chat_integration_sources_20261016.md` as byte-for-byte
(identical blob SHA, 0 changed lines). The reviewed cache was not refreshed
at the time; its stated policy is explicit reviewed selection with no
automatic refresh, so the divergence persisted until this review.

The migration is provenance-only for this record: the archived journal's
SHA-256 still equals the `review_sha256` recorded in the EXT-PITTEL-2016
source observation, so the reviewed bytes are unchanged; only their
location changed. The 2026-10-22 recheck already set the precedent for
this class of update: its contracts "remain unchanged apart from
provenance-only cache pointers" (see
`record/audits/repository_recheck_20261022/report.md`).

## What this snapshot changes

Following the succession practice of the 2026-10-22 recheck, this
snapshot (`evidence/source_metadata/registry_metadata_20261023_refresh.json`)
supersedes `registry_metadata_20261022_recheck.json`, which is preserved
byte-identically; the pointer `literature/metadata_audit.json` now selects
this snapshot and its adjacent digest, with its policy line unchanged.
All 57 records are carried forward; exactly one accepted field changes:

- EXT-PITTEL-2016, `accepted_registry_fields.project_sources`:
  `literature/chat_integration_sources_20261016.md` →
  `archive/literature/chat_integration_sources_20261016.md`.

Every `source_observations` block — including the EXT-PITTEL-2016 review
path and hash, a historical observation of where the review was recorded —
is preserved verbatim. The superseded snapshot's `current_review` is
carried into `supplemental_review_provenance` as
`repository_recheck_20261022_carried_forward`, as the previous succession
did for the trace-closure review. No registry field, claim state,
dependency-graph entry or bibliographic fact changes.

## Verification

`bibliographic_metadata_audit.py --self-test` passes (515 mutation tests)
and the full audit run reports 57 cached identities matching, with the
recorded application coverage unchanged and the claim-dependency impact
sets still in agreement. The superseded snapshot and its digest verify
byte-identically against their pre-refresh hashes.

This refresh certifies only that the reviewed cache again agrees with the
registry on a project-internal file location. It is not a fresh source
review, a theorem-applicability verdict, or a claim-state change.
