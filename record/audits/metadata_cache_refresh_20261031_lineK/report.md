# Metadata cache refresh, 31 October 2026: Line K

## Why this snapshot exists

The Line K integration (BGS-TRACE-234…247, `mathematics/fixed-map/lineK_harg_removal.md`) changes the reviewed registry in
three ways:

* It registers one new external theorem, **EXT-WEIL-1948** (A. Weil, "On some exponential sums", PNAS 34 (1948) 204–207). It is
  used by Lemma W1 (BGS-TRACE-241).
* It records a new use of four existing references by Theorem K3 (BGS-TRACE-235): EXT-DIRICHLET-1837 (rational case, CRT) and
  EXT-VINOGRADOV-1937, EXT-WEYL-1916, EXT-DAVENPORT-1980 (irrational case). Each gets an `additional_uses` entry, and the Line K
  note and the source review are appended to its `project_sources`.
* The new claims, together with BGS-TRACE-231's new dependency on BGS-TRACE-235, change the impact sets of those four records.

Without a refresh, `bibliographic_metadata_audit.py` reports a coverage difference, field mismatches, and graph drift.

This snapshot is `evidence/source_metadata/registry_metadata_20261031_lineK.json` (sha256 in the `.sha256` file next to it).
* It carries forward the 63 records of `registry_metadata_20261031_lineJ.json`. Only the four records listed below are changed:
  their `accepted_registry_fields` and `project_sources` mirror the registry, and their direct and transitive claim sets plus
  `file_level_claim_matches` are refreshed.
* The change list is in `current_review.older_record_impact_changes`.
* One reviewed record is appended for EXT-WEIL-1948.

## New reference

The review record is `literature/lineK_sources_20261031.md`.

| ID | Primary text | Locator | Application status |
|---|---|---|---|
| EXT-WEIL-1948 | **partial**: pp. 204–205 set-up read in a search-index text extract; pp. 206–207 (the final estimates) not read | no equation pinned | unverified_application |

## Refreshed older records (impact sets)

| ID | direct added | transitive added |
|---|---|---|
| EXT-DIRICHLET-1837 | BGS-TRACE-235 | 231, 236, 239, 240, 245, 246 |
| EXT-VINOGRADOV-1937 | BGS-TRACE-235 | 236, 239, 240, 245, 246 |
| EXT-WEYL-1916 | BGS-TRACE-235 | 236, 239, 240, 245, 246 |
| EXT-DAVENPORT-1980 | BGS-TRACE-235 | 236, 239, 240, 245, 246 |

No record lost a claim. No other record's impact set changed.

## Not done here

The pre-existing EXT-BR-1975 dependency-graph drift (present on main) is **not** refreshed. The audit therefore still fails on
that line only, exactly as on main.

No claim state changed because of this snapshot.
