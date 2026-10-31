# Metadata cache refresh, 31 October 2026: Line J external theorems

## Why this snapshot exists

The Line J integration registered three external theorems in `literature/external_dependencies.json`. All three are used by
BGS-TRACE-231 (Theorem J3) to make S⁺ infinite under H_arg:

* EXT-VINOGRADOV-1937: Vinogradov's equidistribution of (pγ) mod 1 over primes.
* EXT-WEYL-1916: Weyl 1916, the Weyl criterion.
* EXT-DAVENPORT-1980: Davenport GTM 74, 2nd ed., the prime number theorem in arithmetic progressions.

Without cache records for them, `bibliographic_metadata_audit.py --self-test` reports
`registry/cache coverage differs; new references require review`.

This snapshot is `evidence/source_metadata/registry_metadata_20261031_lineJ.json` (sha256 in the `.sha256` file next to it).
* It carries forward the 60 records of `registry_metadata_20261031_lineI.json` unchanged: the records list is equal as parsed JSON,
  and the old file re-serialises byte-identically with the same formatting.
* It then appends one reviewed record per new reference.

## Review of the new references

The review record is `literature/lineJ_sources_20261031.md`.

| ID | Primary text | Locator | Application status |
|---|---|---|---|
| EXT-VINOGRADOV-1937 | **not obtained** | Chapter XI of the 1954 book, via the Kuipers–Niederreiter Notes (read); page not pinned | unverified_application |
| EXT-WEYL-1916 | not obtained | criterion read as Kuipers–Niederreiter Theorem 2.1, with attribution to this paper | verified_application_reviewed_in_note |
| EXT-DAVENPORT-1980 | not obtained | §§20, 22 from the publisher contents page | unverified_application |

The v2 J3 text cited Iwaniec–Kowalski Theorem 13.6. That theorem is only the minor-arc estimate, so the citation was replaced
(see the source review).

## Impact graph

The graph is computed from `record/claims.json`. Each of the three has direct dependency BGS-TRACE-231 and no transitive
dependencies. The new Line J claims do not change the impact set of any earlier record.

## Not done here

The pre-existing EXT-BR-1975 dependency-graph drift (transitive BGS-TRACE-116, present on main) is **not** refreshed. The
self-test therefore still fails on that line only, exactly as on main.

`computations/maintenance/v4_negative_controls.py` now tampers the new digest-pinned cache instead of the superseded one.

No claim state changed because of this snapshot.
