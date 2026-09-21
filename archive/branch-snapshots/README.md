# Historical branch provenance

This directory is intentionally **metadata-only**. Historical research branch source trees are not vendored into `main`: doing so would reintroduce superseded code (including the retired Julia stack), duplicate current sources, and make a normal checkout ambiguous.

The branch refs and Git history remain the byte-authoritative recovery mechanism. The table below records the heads and source-tree SHAs examined during the 2026-09-06 consolidation.

| snapshot | source branch | head commit | source tree |
|---|---|---|---|
| bgs-frontier-2026-09-04 | research/bgs-frontier-2026-09-04 | fe1c7e71cb3198041c37e0825679b0bf8a221751 | f6b261c301c9f5f830fd931bddf0c2552f7b1e95 |
| cayley-centered-fourier-2026-09-04 | research/cayley-centered-fourier-2026-09-04 | 62d069ace30b23c0be68607231054a7c92f6f03a | ef62ec05615e2db1dbd4bd00cff038dd836f5e94 |
| cayley-direct-energy-2026-09-04 | research/cayley-direct-energy-2026-09-04 | 3af07c5ce9df92fdcf214e43ca260383c398a41d | 595d7e7f95e670c925f3e7c77c5182fd4e2bf04a |
| cayley-energy-incidence-2026-09-04 | research/cayley-energy-incidence-2026-09-04 | 875bde8c1e0b59db231bbd58b11df34f2a609e4a | c4784b8202afe233cb0389e78edfd81052b071c1 |
| cayley-resultant-structure-2026-09-04 | research/cayley-resultant-structure-2026-09-04 | 6873c0b238cf1e968d94b12cb4e24ed5ab3aeee3 | e4c9ab50d19c91e2ddfd3ff7dcb96d3db8bf1c8f |
| coboundary-resonance-20260905 | research/coboundary-resonance-20260905 | 00f511188dd18a4931386bef646c877f352d4a14 | b459c9d01d71066b8e0f5ea58465a0c294350c1f |
| fixed-strength-locality-20260905 | research/fixed-strength-locality-20260905 | c18ba2c651ce00ca413d452071e980c2b619ca2f | bae32453b7721db9102a23dfef39eef709cdecbc |
| inverse-quartic-20260905 | frontier/inverse-quartic-20260905 | 914a1c47323832ee03e4674c49250794fd57808d | 360cc56b9ee42f9c10d44fff57c6ff4e675a6b62 |
| m1-cross-energy | research/m1-cross-energy | 057431853b02b4a65f16f32c79299adb9f46fcce | 8d4e243e54538aecf63de266577bb808633a2ae1 |
| product-row-elliptic-20260904 | research/product-row-elliptic-20260904 | 31926c38a42262179de9a649fa1ad5ff9a80650a | d79a5a1a049b2ab96d5caa55d48b75bf2175b94b |
| projective-bezout-row-20260904 | research/projective-bezout-row-20260904 | 7440eda59d866fca50483a54f3b7f362cb56bc48 | ad25780c2d1d3e3e9c0aa4550762927c5570b622 |
| smooth-cohomology-20260905 | research/smooth-cohomology-20260905 | bda36a531ba79a5df1159f48771994824c700f74 | 78d5f5e8a9b4ba144516842c69d231fbc2e16216 |

The current top-level `main` tree is authoritative. A historical branch/tree may contain exploratory or superseded claims and must not be treated as current merely because its SHA is recorded here.

The 21 September reconciliation additionally audited open PRs #11, #13, #14,
#15 and #16.  PR #13 is preserved as historical provenance rather than merged
wholesale because the dated referee audit records a corrected false exact
triple-filter anchor; its surviving inverse-support core has later maintained
formulations on the authoritative tree.  See
`../../record/final_research_handoff_20260921.md`.
