# Final branch and historical-artifact reconciliation — 21 September 2026

This note is the final preservation audit performed before promoting the
21 September recovery branch to `main`.  It distinguishes four things that
must not be conflated:

1. Git ancestry;
2. byte-preservation in historical refs;
3. promotion of scientifically current material;
4. deliberate non-vendoring of obsolete/duplicate workspaces.

The authoritative scientific status remains
`record/claim_ledger.md`, `record/retractions.md`, and
`record/verified_state_reconciliation_20260921.md`.

## 1. Late integration refs

Immediately before the final fast-forward, the published `main` head was

`39d4e01ae6a6b3eb472ab30266b708ca71a70a16`.

The preservation-audit checkpoint before final verifier normalization was

`befd253b4f85515bb89c7492e6ed0c39ff5263cf`.

The branch actually promoted to `main` is
`research/recover-heisenberg-audit-20260921`; its exact merge head is the
new `main` head after the final fast-forward and must be read from Git rather
than hard-coded self-referentially in this pre-merge record.  The recovery
branch is a strict descendant of the pre-final `main`.  The following late
branches contain no commit absent from that lineage:

| branch | relation to pre-final main |
|---|---|
| `repair/post-merge-audit-20260921` | behind by 1, ahead by 0 |
| `research/final-integration-20260921` | behind by 3, ahead by 0 |
| `research/recovered-audit-20260920` | behind by 6, ahead by 0 |
| `session-consolidation-20260907` | behind by 75, ahead by 0 |

At the audit point there were **zero open pull requests**.

The recovery diff itself contains **no removed files**.  It adds recovered
proof/evidence files and edits status/navigation/manuscript surfaces.  The
only line deletions are stale prose replacements in entry-point Markdown.

## 2. Diverged research branches re-audited by tree SHA

Divergence does not imply a missing current result: many historical branches
were merged semantically during the repository reconstruction rather than by
retaining their original commit ancestry.

### Branches whose maintained mathematics is already same-path or later

The following branches were compared blob-by-blob with the recovery tree.
Their maintained mathematical source paths are present identically or in later
revisions; absent paths are old standalone manuscript/PDF surfaces, dedicated
workflows, one-shot publishers, or otherwise superseded artifacts:

- `fix/fibonacci-signed-identity-2026-09-04`;
- `research/bgs-frontier-2026-09-04`;
- `research/cayley-centered-fourier-2026-09-04`;
- `research/cayley-direct-energy-2026-09-04`;
- `research/cayley-energy-incidence-2026-09-04`;
- `research/cayley-resultant-structure-2026-09-04`;
- `research/product-row-elliptic-20260904`;
- `research/projective-bezout-row-20260904`;
- `research/coboundary-resonance-20260905`;
- `research/fixed-strength-locality-20260905`;
- `research/smooth-cohomology-20260905`.

For the small 4 September branches, the only absent files are the retired
standalone `manuscript/arithmetic_cat_map_moments.{tex,pdf}`.  The canonical
manuscript is now `manuscript/WoW_unified.tex`.

### `frontier/inverse-quartic-20260905`

Head:
`914a1c47323832ee03e4674c49250794fd57808d`.

This branch is **not** to be merged wholesale.  Its draft triple-filter claim
was falsified by the later referee audit: for example the asserted exact
factor `p` can be `5p`.  The necessary divisibility direction survives,
and the useful inverse/reflection/resultant core has later maintained
formulations in the current Cayley/inverse support notes.  The branch ref
preserves the old bytes; the absent draft theorem/workflow files are
quarantined rather than silently promoted.

### `hoplite/andros-a16085fa` and `rebuild/main-clean`

Heads:

- `89dc45e766a2fd2631e93849559723bb92be8cb9`;
- `7dd1fd591189c92af9ce0897794cfbc59500f0b2`.

These are large legacy workspaces (roughly one thousand historical blobs each)
containing old diagnostics, retired Julia sources, stale PDFs, duplicate paper
surfaces, and superseded claims.  They are the kind of source tree explicitly
excluded by `record/reconstruction.md`.  Their refs remain the byte-level
archive.  Re-vendoring them would violate the current repository contract and
would make obsolete code look maintained.

### `research/m1-cross-energy`

Head:
`057431853b02b4a65f16f32c79299adb9f46fcce`.

This branch is also a legacy-workspace branch (more than two thousand blobs)
and must not be merged wholesale.  It contains a corrected M1 line whose
scientific status is important to preserve:

- the pair-key table is multiplicity-weighted, with the diagonal
  ((1,1,0)) key carrying multiplicity (p-2);
- cross-twist terms do not vanish by an automatic orthogonality;
- the regular-fiber single-twist character sum was reduced to a complete
  polynomial character sum and bounded by (3sqrt p) (and (2sqrt p) at
  (d=pm1)) under the cited finite-field Weil theorem;
- centering over (q
e0) removes the singular-singular constant exactly but
  leaves the scaled (k=2) fluctuation and a regular-regular variance;
- the assembled regular-regular/cross-twist variance and downstream spectral
  implication remain **OPEN**.

The current maintained `mathematics/fourth_moment_reduction.md` already
contains the corrected weighted diagonal, exact constrained-pair count,
coupled-key decomposition, and exact nonzero-frequency mean/variance
reduction.  The larger historical M1 branch is therefore preserved as a
research branch, not copied into `main`.  Its extra regular-twist lemma is
recorded here as historical provenance rather than promoted to a current
BGS closure claim without a new source-level referee pass.

## 3. Early 14 September BGS artifacts

The Library inventory found several pre-v7 artifacts that were absent from the
initial 20--21 September handoff.  They were hash-audited and their supplied
checks were freshly executed.

| artifact | SHA-256 | disposition |
|---|---|---|
| `BGS_verified_state_2026-09-14.md` | `3381449c560103a61b1142b0ed181fb6048f8d9dd74df1b8d60c8cb53b885d31` | early single-shear/COE + candidate-state audit; superseded by v2/v6/v7 chronology |
| `BGS_research_progress_2026-09-14_v2.md` | `eef3ab6d4481d36dc828d747359048b567201ea00b871260b930a23621b6840d` | Fejer--Hermite candidate, not the final frozen operator |
| `bgs_fejer_candidate_checks.py` | `7568d42ae40fcb68c8ebc9a4e468df5c57de67b6687c8366873d9fe68dd68fa0` | freshly rerun: PASS |
| `bgs_exact_checks.py` | `bcb89ced7ae47014cc43f6fb9e2c609ee33415e08fcf4e1aa3ceee87838c5d1d` | freshly rerun: PASS; arithmetic/rank core later re-derived in maintained notes |
| `BGS_research_progress_2026-09-14_v6.md` | `665d36b64ea4330db4ecf2671ae822b33d89906ef83c3a696c11096766c7b720` | different two-directional candidate with (c=10^{-8}); superseded by v7 frozen (c=10^{-80}) model |
| `bgs_final_candidate_v6.py` | `1a7b738c1eee0ff7b4bc2e004e694bdc1882d096a5b22c1daeaf0d67820dae69` | freshly rerun: PASS for the superseded v6 candidate |
| `BGS_full_resolution_dossier_v7.md` | `49c4298eadbd13d7cf561a5282471e6d800e1f02433bd6e82db8c52a1845f56f` | byte-identical to the already audited v7(1) copy |

The important point is model identity: v2/v6 are not missing proofs for the
final frozen operator.  Promoting their model-specific symmetry/simple-spectrum
claims into the active fixed-map ledger would be scientifically wrong.
Their reusable Heisenberg/arithmetic components are already represented by the
repaired maintained notes.

## 4. Preservation conclusion

No historical branch is deleted by this reconciliation.  Old bytes remain
recoverable by Git refs/history and the original Library artifacts remain
hash-identified.  Current `main` contains only maintained results, explicit
retractions/quarantines, and the compact provenance needed to find the old
sources without reviving obsolete workspaces.

This is stronger than claiming that every old file belongs in `main`:
**nothing scientifically identified is silently lost, while obsolete source
trees are not misrepresented as current.**
