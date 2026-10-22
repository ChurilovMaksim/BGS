# Reviewed bibliographic impact extension, 6 October 2026

## Trigger and exact change

The first frozen next-proof verification completed 169/170 entries; the metadata guard rejected stale graph-impact sets for the three records below. That failed run remains historical. This is an explicit dependency-impact review, not an automatic digest refresh or a new external-source review.

### EXT-PESIN-1977

- Direct claims before and after: BGS-FM-006.
- Transitive claims before: BGS-FM-018, BGS-FM-019, BGS-FM-020.
- Transitive claims after: BGS-FM-018, BGS-FM-019, BGS-FM-020, BGS-FM-023.
- Sole added impact: BGS-FM-023. No removals or direct additions.
- Application status before and after: `unverified_exact_theorem`.

### EXT-RUELLE-1978

- Direct claims before and after: BGS-FM-006.
- Transitive claims before: BGS-FM-018, BGS-FM-019, BGS-FM-020.
- Transitive claims after: BGS-FM-018, BGS-FM-019, BGS-FM-020, BGS-FM-023.
- Sole added impact: BGS-FM-023. No removals or direct additions.
- Application status before and after: `unverified_application`.

### EXT-PP-1990

- Direct claims before and after: BGS-FM-006, BGS-FM-018.
- Transitive claims before: BGS-FM-019, BGS-FM-020.
- Transitive claims after: BGS-FM-019, BGS-FM-020, BGS-FM-023.
- Sole added impact: BGS-FM-023. No removals or direct additions.
- Application status before and after: `unverified_application`.

## Reviewed paths and mathematical roles

For Pesin and Ruelle the newly visible registered path is FM-006 -> FM-018 -> FM-023. For Parry–Pollicott it is the direct FM-018 -> FM-023 path, also reachable through FM-006. FM-001 has no registered external dependencies and is not the cause of any of these three additions. TRACE-015, TRACE-016 and FORMAL-002 do not enter these impact sets.

The FM-023 source's Section 0 specifies the needed roles: FM-001 supplies the exact fixed operator, midpoint symbol and coefficient dictionary, not its classical symmetry conclusion. FM-016 supplies the overlap architecture, not affine-centralizer exclusion; the cutoff/product/trace argument is reconstructed quantitatively in Sections 5.1–6. FM-018 supplies its actual finite-Fourier kick-Egorov mechanism (O7), rederived via Weyl multiplication and Duhamel in Section 5.0. Its later classical mixing estimate O11, pressure/Gibbs identification and channel-gap claims are explicitly not required.

Those registered whole-claim dependencies retain conservative provenance reachability. At lemma level this is not evidence that FM-023 newly depends on Pesin's entropy formula, Ruelle's inequality or Parry–Pollicott's mixing theorem. We keep the existing claim graph unchanged rather than quietly narrowing it merely to satisfy this audit. The impact note now makes this granularity limitation explicit. A future finer-grained dependency schema could separate proof-source attribution from load-bearing theorem leaves.

## Preserved source and application states

Only `transitive_claim_dependencies` and the explanatory `dependency_coverage_note` change in these three cached records. The prior coverage note was exactly: “Computed from record/claims.json; absence of an edge is not proof of no mathematical use.” All other records and fields are unchanged. Source titles, authors, identifiers, pinned versions, locators, observations, hashes, inherited mappings, application reviews and statuses are untouched; literature/external_dependencies.json and record/claims.json are untouched.

In particular, the original Pesin Theorem 5.1 locator remains unverified after the recorded HTTP 403 failures; no new retrieval or applicability verification is claimed. Ruelle and Parry–Pollicott retain their recorded located-but-not-fully-reviewed locator coverage and unverified_application statuses. The Parry–Pollicott digitization-cover caution is retained.

Prior complete cache SHA256: c6391cf0f8354061fe3212e5dd48fce5b93b21e3ecf17a03f40c063befdf9c28.

Reviewed complete cache SHA256: a345ee5adcda4b2588a767daee67a07712b76f8bda9d2f203d404c6c8ad42146.

The digest changes only after the exact impact delta and unchanged-field comparison above. Validation: `python3 computations/verification/bibliographic_metadata_audit.py --self-test` checks metadata and exact live impact sets, plus its 308 mutation tests. A pass is metadata consistency, not theorem applicability.
