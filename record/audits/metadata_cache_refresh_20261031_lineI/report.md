# Metadata cache refresh, 31 October 2026: Line I external theorems

## Why this snapshot exists

The owner audit of PR #60 (Line I, fix R1) registered three external theorems in `literature/external_dependencies.json`:

* EXT-RS-1962: Rosser–Schoenfeld 1962, Theorem 15. Used by BGS-TRACE-215.
* EXT-BHV-2001: Bilu–Hanrot–Voutier 2001, Theorem 1.4. Used by BGS-TRACE-219.
* EXT-CARMICHAEL-1913: Carmichael 1913. Used by BGS-TRACE-219 as corroboration; it is not load-bearing.

Without cache records for them, `bibliographic_metadata_audit.py --self-test` reports
`registry/cache coverage differs; new references require review`.

This snapshot is `evidence/source_metadata/registry_metadata_20261031_lineI.json` (sha256 in the `.sha256` file next to it). It
carries forward the 57 records of `registry_metadata_20261024_p2math9b.json` unchanged. The records list is equal as parsed JSON,
and the old file re-serialises byte-identically with the same formatting. It then appends one reviewed record per new reference.

## Review of the new references

The review record is `literature/lineI_sources_20261031.md`.

| ID | Primary text | Locator | Application status |
|---|---|---|---|
| EXT-RS-1962 | journal scan read (sha256 8e37b06f…ab556) | Theorem 15, pp. 71–72, (3.41)–(3.42), verified | reviewed in the note §6 |
| EXT-BHV-2001 | **not obtained**: HAL copy behind a bot challenge, publisher copy paywalled | Theorem 1.4 corroborated by the abstract and a secondary citation; page not pinned | unverified_application |
| EXT-CARMICHAEL-1913 | not inspected | secondary sources conflict (XXIII vs 21); unverified | unverified_application (corroborating only) |

## Impact graph

The graph is computed from `record/claims.json`:

* EXT-RS-1962: direct BGS-TRACE-215; transitive BGS-TRACE-217.
* EXT-BHV-2001: direct BGS-TRACE-219.
* EXT-CARMICHAEL-1913: direct BGS-TRACE-219.

## Not done here

On main, the audit already fails with `EXT-BR-1975: dependency graph changed`. The cause is a transitive BGS-TRACE-116 edge, which
is unrelated to Line I. That impact review is **not** refreshed in this snapshot, so the self-test still fails on that line only,
exactly as on main.

`computations/maintenance/v4_negative_controls.py` now tampers the new digest-pinned cache instead of the superseded one.

No claim state changed because of this snapshot.
