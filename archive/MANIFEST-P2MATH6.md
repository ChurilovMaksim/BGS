# P2-MATH wave 6 (cayley-arithmetic) — move manifest

## 1. Base and live verification

Base: the wave-4 post tree (`p2_math4b_work/post_tree`, 6,683 files),
copied byte-identically (recursive manifest check) as the wave-6 base.
Live main at assembly time: HEAD `be4fef7a88eca2484a28084f85981e460274f3cc`
(wave-4 deletion commits landing). Connector readback confirmed the base
matches live main on every file this wave touches:

- `record/claims.json` blob `219ff8f310e1065c5d37bdf304a9522888dda284` == live.
- `record/claim_integration_epochs.json` blob
  `343db2026b4c0711d0a4b4d7cc4e19ceef802683` == live.
- `literature/external_dependencies.json` blob
  `2a5efd69a1d9500d7501818efa5d816c8e4a8eda` == live.
- `record/external_epoch_amendments.json` blob
  `25de10f4ea2f19a2d29de1910b1dbd94269374c6` == live (wave-4's 5 rows).
- `mathematics/returns/` new home present live; its
  `return_trace_obstruction.md` blob `47411584e9f88fe092dd95d1ff669f2923d5a390`
  == base. `mathematics/cayley-arithmetic/` does not exist live yet.
- The 9 wave-4 old returns paths were still partially present live at the
  first check (deletions in flight) and are CONFIRMED fully deleted by the
  coordinator (last deletion commit short SHA `49cdacb`, old paths 404,
  `mathematics/returns/` holds exactly the 9 files; wave 4 closed). The
  base tree already models that end state (no old returns paths), so their
  absence is not a discrepancy, and no staging file references them.

Nothing was pushed from this assembly; the push is the coordinator's step.
The post tree below is the end state AFTER the coordinator deletes the 36
old root notes (§9); the staging (§10) carries the 36 new-home copies plus
every edited file, and the deletions happen only after landing + readback.

## 2. Move: 36 notes, root → mathematics/cayley-arithmetic/

Membership is strictly the `cayley-arithmetic` list of
`record/mathematics_topics.json` (36 entries); every entry's first listing
in wave order (foundations, locality, information-theory, returns, pell,
cayley-arithmetic, resonance-cohomology, spectral-obstructions, fixed-map,
trace-bridge) is cayley-arithmetic itself — no multi-topic note, no dated
name, so no renaming and no cross-topic canonical update was needed.

Link rule (wave-4 precedent): sibling links inside the wave stay bare
(valid in the common home); every other relative link gains one `../`.

- 34 notes: byte copies (SHA-256 identical to the base root files).
- `cayley_trace_gaussian_limit.md`: one link edit,
  `../literature/arithmetic_dependency_closure_20261022.md` →
  `../../literature/arithmetic_dependency_closure_20261022.md`.
- `pell_coboundary_fourth_moment.md`: one link edit,
  `pell_coboundary_resonance.md` → `../pell_coboundary_resonance.md`
  (the target still lives in the root; the pell wave has not moved it).
- Intra-wave links that stay bare (same home): centered_energy →
  direct_energy; exact_baseline_density → trace_gaussian_limit;
  jacobi_trace_average → trace_gaussian_limit; product_row_coefficient_ideal
  → product_row_real_trace_ideal; resultant_mass_budget →
  direct_energy/centered_energy; resultant_structure → additive_energy (×2);
  elliptic_pencil → offoff_elliptic_spike_theorem; fibonacci_ratio_energy_proof
  → resultant_structure; fourth_moment_reduction →
  offoff_elliptic_spike_theorem/elliptic_pencil.
- No note contains a `mathematics/` full-path string; no other link forms
  exist in the 36 notes.

## 3. Consumers migrated in the same commit (all asserted by occurrence count)

- `record/mathematics_topics.json` — 36 paths of topic `cayley-arithmetic`;
  `updated` already 2026-10-24, unchanged.
- `mathematics/topics/cayley-arithmetic/README.md` — 44 links
  `../../<stem>.md` → `../../cayley-arithmetic/<stem>.md` (3 capsules +
  5 reading-sequence + 36 membership).
- `papers/arithmetic-cayley/README.md` — 4 links
  `../../mathematics/<stem>.md` → `../../mathematics/cayley-arithmetic/<stem>.md`.
- `papers/arithmetic-cayley/paper.json` — 4 `authoritative_sources`.
- `literature/bibliography.md` — 8 prose code-spans → new-home path form
  (additive_energy, centered_energy, direct_energy, jacobi_trace_average,
  ratio_orbit_factorization, trace_gaussian_limit, fibonacci_ratio_energy_proof,
  offoff_elliptic_spike_theorem).
- Verifier docstrings (12 files, path prose only, except where noted):
  `cayley_uniform_cutoff_regression.py` (additive_energy),
  `cayley_curve_uniform.py`, `cayley_difference_discriminant.py`,
  `cayley_energy_curve_regression.py`, `cayley_frobenius_extension.py`,
  `cayley_higher_moments.py` (docstring + the FUNCTIONAL
  `associated_proof_sha256` path list — the verifier reads the note's bytes,
  so this migration is load-bearing, not cosmetic),
  `cayley_jacobi_trace_regression.py`, `cayley_product_discriminant.py` (×2),
  `cayley_resultant_mass_budget.py` (×2), `cayley_resultant_fibonacci.py` (×2),
  `pell_coboundary_fourth_moment.py`, `offoff_elliptic_spike_regression.py`.
- Lean comments (2 files, prose only): `formalization/Bgs/CayleyCurveEnergy.lean`,
  `formalization/Bgs/FibonacciRatioSmall.lean`.
- Regenerated (not hand-edited): `docs/corpus_atlas.md` (exactly 36 lines,
  paths only), `record/claim_registry.md` (exactly 7 lines, CAYLEY sources),
  `record/scientific_dependency_graph.md` (exactly 7 lines), `STATUS.md`
  (exactly 1 line: 70 → 72 historical claim amendments).
  Byte-identically regenerated and NOT in the push set:
  `record/scientific_dependencies.json`, `ERRATA.md`, `mathematics/results.md`,
  `literature/references.bib`.
- Maintained count control: registered == maintained == 334
  (root −36, home cayley-arithmetic +36).

## 4. Claims channel: sealed amendments ×4 (field `source`), follow-on ×3

Sealed wave2 rows (96-row snapshot) and their canonical SHA-256
(sort_keys, separators `(',',':')`, `ensure_ascii=False`, same serializer
as `check_prior_claims`):

- BGS-CAYLEY-001, sealed SHA
  `04dff239fcba6148a7334ec5010980dd053ca1e392e3effd0c68021efdd257ae`:
  pre-existing amendment row EXTENDED — `fields` gains `source`:
  `mathematics/fourth_moment_reduction.md` →
  `mathematics/cayley-arithmetic/fourth_moment_reduction.md`
  (existing fields `ledger_status`, `boundary` untouched; disposition
  gains one sentence recording the wave-6 relocation; sealed SHA untouched).
- BGS-CAYLEY-002, sealed SHA
  `0382809cd2bfa421e253af29a82c582571ee1454f77e4f1fca4d1512fdb05703`:
  NEW amendment row, `fields = {source}`:
  `mathematics/cayley_additive_energy.md` →
  `mathematics/cayley-arithmetic/cayley_additive_energy.md`.
- BGS-CAYLEY-003, sealed SHA
  `be91ec6c297192b1657db6605457ef6dd96b498a254bd93f0f7eda8e87fd3349`:
  pre-existing amendment row EXTENDED — `fields` gains `source`:
  `mathematics/cayley_direct_energy.md` →
  `mathematics/cayley-arithmetic/cayley_direct_energy.md`
  (existing fields `state`, `ledger_status` untouched; disposition gains
  one sentence; sealed SHA untouched).
- BGS-CAYLEY-004, sealed SHA
  `bfad12bd6cbc245a0cafa2b3503833a0c27f1104a19a87b2f61046c37f75c48d`:
  NEW amendment row, `fields = {source}`:
  `mathematics/cayley_curve_uniform.md` →
  `mathematics/cayley-arithmetic/cayley_curve_uniform.md`.
- All four rows: `review: archive/MANIFEST-P2MATH6.md` for the two new rows;
  the two extended rows keep `review: record/errata.json` and gain the
  relocation sentence in `disposition`. `approved` in
  `computations/verification/wave2_integration_audit.py` extended 70 → 72
  (`'BGS-CAYLEY-002'`, `'BGS-CAYLEY-004'` inserted beside the existing
  CAYLEY entries; channel code untouched).
- `wave2_integration_audit.run()` delta base → post is EXACTLY two lines:
  `unchanged_prior_claims` 26 → 24, `explicitly_amended_prior_claims`
  70 → 72; every other field byte-identical (JSON SHA base
  `eee32a75…` → post `333a4679…`).
- Follow-on (`after_wave3`, gate pins state+source; states unchanged):
  BGS-CAYLEY-006 `source` → `mathematics/cayley-arithmetic/cayley_trace_gaussian_limit.md`,
  BGS-CAYLEY-007 `source` → `mathematics/cayley-arithmetic/cayley_product_row_real_trace_ideal.md`,
  BGS-CAYLEY-008 `source` → `mathematics/cayley-arithmetic/cayley_scaling_rigidity.md`
  — in `record/claims.json` and in the `after_wave3` rows, same commit.
- BGS-CAYLEY-007 `boundary` (which names
  `mathematics/cayley_inverse_resultant_transversality.md` and
  `mathematics/cayley_product_row_subresultants.md`) is NOT pinned by any
  gate and is LEFT UNTOUCHED per the wave brief; the same prose appears in
  the CAYLEY-007 `after_wave3` disposition, likewise untouched.
- BGS-CAYLEY-005 is sealed but its `source` is `mathematics/open_questions.md`
  (not a wave note) — untouched. `wave3_integration_audit.run()` fails on
  the clean base (`earlier theorem contract changed: BGS-CAYLEY-001`) and
  fails identically on post; that pre-existing failure is NOT fixed here
  (CI does not invoke it) and is not caused by this wave's amendments.

## 5. External channel: sealed rows ×5, admitted-later ×5

Recursive scan of `literature/external_dependencies.json` (all fields,
including nested `additional_uses[].project_sources`): no `additional_uses`
hit; all hits are `project_sources[0]`.

Sealed contracts (amendment rows APPENDED to
`record/external_epoch_amendments.json`, 5 → 10; wave-4's rows untouched;
canonical contract SHA formula as in `check_external_epoch`):

- EXT-VM-2015, contract SHA
  `4ff83d0fbcf886634b4f1072c9787ea6d82585d800cb0d3f1bf049c8f08eb5fa`:
  `mathematics/cayley_direct_energy.md` →
  `mathematics/cayley-arithmetic/cayley_direct_energy.md`.
- EXT-CZ-2013, contract SHA
  `084ae21434daea283c7f7dbdfc914ced91865ff88ffeacb44959c8007b66e807`:
  `mathematics/cayley_curve_uniform.md` →
  `mathematics/cayley-arithmetic/cayley_curve_uniform.md`.
- EXT-FKM-2014, contract SHA
  `3eec299ce4a4e4f0dad32d8bc6daab333dd0d14c2130109e02a88ce11ae5a37d`:
  `mathematics/offoff_elliptic_spike_theorem.md` →
  `mathematics/cayley-arithmetic/offoff_elliptic_spike_theorem.md`.
- EXT-BLV-2009, contract SHA
  `8de2a438b99765194471318a67d7ddd0bbdb3bed30d9a9d753404f9338a43c54`:
  same offoff path migration.
- EXT-IK-2004, contract SHA
  `8f0cedf583583b9e070cc1019bc102f03bfef894ae17a2670b640ec1025145a3`:
  `mathematics/cayley_jacobi_trace_average.md` →
  `mathematics/cayley-arithmetic/cayley_jacobi_trace_average.md`.
- All five rows: `field: project_sources`, `wave: P2-MATH wave 6`,
  `review: archive/MANIFEST-P2MATH6.md`, old_value == sealed list (verified
  against the sealed snapshot, not copied from the live registry).
- `check_external_epoch` on post: `(39, 18)`.

Admitted-later contracts (migrated directly, no store row — by design of
the pre-existing seal; their field values are covered by
`scientific_registry_audit.py` require_path and by the bibliographic guard):

- EXT-WANG-1982, EXT-FI-1980, EXT-ZAGIER-1997, EXT-BORDA-2020:
  `mathematics/cayley_trace_gaussian_limit.md` →
  `mathematics/cayley-arithmetic/cayley_trace_gaussian_limit.md`.
- EXT-BT-1971: `mathematics/cayley_product_row_real_trace_ideal.md` →
  `mathematics/cayley-arithmetic/cayley_product_row_real_trace_ideal.md`.

## 6. Bibliographic cache refresh (Pittel recipe, second use)

Post-move stage 1 failed `bibliographic_metadata_audit --self-test` with
exactly the ten errors of §5 (5 sealed + 5 admitted fields — the guard
compares all 57 rows regardless of seal class). The refresh follows the
wave-4 precedent exactly:

- New snapshot `evidence/source_metadata/registry_metadata_20261024_p2math6.json`
  (SHA-256 `ae93dc33fe4f1468db2b61a65092e1a360d003b8dd34362c7f627b63755a7e3e`)
  + `.sha256` + report
  `record/audits/metadata_cache_refresh_20261024_p2math6/report.md` +
  pointer repoint in `literature/metadata_audit.json` (exactly 3 lines).
- Text diff vs the superseded wave-4 snapshot is exactly 38 lines: 15 path
  leaves (10 accepted `project_sources` + 5 duplicated top-level mirrors
  for the sealed records; the admitted records carry no top-level copy) +
  `scope` + `current_review.{record, previous_snapshot_sha256, scope}`.
  Chain: `previous_snapshot_sha256`
  `3f84faf500161b3a6cf9cd10192874af27dfdbc3893c54c3b7b30400bc7b2826`
  == the wave-4 snapshot file's own SHA-256. No observation re-retrieved,
  no review hash changed, no claim state or graph impact change. The
  superseded snapshot is preserved byte-identically.
- Self-test after refresh: rc=0, 515 mutation tests, 57 cached identities.

## 7. Controls (base → post; delta empty except as stated in §§4–6)

Fast set (`run_controls.sh`): registry audit OK (197 claims, 57 ext);
repository audit rc=0; bibliographic self-test rc=0 (515) after §6
(rc=1 with exactly the ten §5 errors before it); epoch test 12/12;
render_claim_registry / errata / research_views / status / bibliography
--check rc=0; audit_manuscript_references rc=0; wave2 run() delta exactly
§4; sync_return_sections / finite_orbit / fixed_map --check rc=1 with
stale lists byte-identical to base (known pandoc CI debt, pre-existing).
`check_external_epoch` run explicitly: (39, 18).
Rehearsal (`rehearsal.py`): ALL PASS — 334 registered == 334 maintained,
all claims mathematics/ paths resolve, all migrated markdown links resolve,
all verifier/lean/paper/topic-view paths resolve, STATUS 72, atlas 334.
Full discover: see REPORT.md (250 tests OK expected; one run on the final
post tree).
Known pre-existing reds, NOT chased: `wave3_integration_audit.run()` fails
on clean base (CAYLEY-001, no amendment channel there; CI does not invoke
it) — identical signature on post; Hardy verifier timeout on this 2-vCPU
machine; `resonant_density_audit` needs numpy>=2 (passes under the pinned
venv) — environment, not a repo defect.

## 8. Residual classification (post tree; zero live pointers at old paths except as listed)

Full scan for the 36 old `mathematics/<stem>.md` strings (live tree,
excluding archive/ and evidence/ frozen carriers; classification by file):

- LIVE, intentional: `record/external_epoch_amendments.json` (old_values
  of the 5 new sealed rows, §5); `record/claim_integration_epochs.json`
  (CAYLEY-007 `after_wave3` disposition prose quoting the old boundary
  paths, §4 — the boundary mention left untouched per the brief);
  `record/claim_registry.md` (regenerated view embedding the untouched
  CAYLEY-007 boundary prose, §4); `record/claims.json` itself (the
  untouched CAYLEY-007 `boundary` field, §4).
- LIVE, pre-existing dispositions (unchanged by this wave, byte-identical
  to base): `record/claim_ledger.md` (narrative table prose, waves 1–3
  precedent — not markdown links, repository_audit green);
  `manuscript/unified_sections/cayley_trace_gaussian.tex` (generated
  chapter, stale on base under the pandoc CI debt; sync --check stale
  lists base-identical; NOT hand-edited, updated at the next sync
  regeneration — wave-4 precedent for .tex chapters).
- FROZEN (never edited, resolved by this manifest): all `archive/**` and
  `evidence/**` carriers (dated manifests, workspace snapshots, sealed
  checkpoint inputs, sealed external snapshot itself, superseded cache
  snapshots), `record/audits/20261006/coverage.json` and
  `record/audits/era_baseline_attestation_20261023/inventory_*.json`
  (dated snapshots), `record/audits/repository_recheck_20261022/**`
  (dated audit), and the dated literature provenance notes
  `literature/arithmetic_dependency_closure_20261022.md` (2 links) and
  `literature/cyclotomic_row_support_sources_20260905.md` (1 code-span) —
  dated files remain provenance per the P2-BIB design rule; the moving
  note's outbound link TO the closure file was re-pointed (§2), but the
  frozen files themselves were not edited.
- NOT present anywhere live: any migrated consumer, any regenerated view,
  any claims/epochs field except the intentional prose cases above.
- Pre-existing break (not wave-caused, noted, not fixed here):
  `literature/bibliography.md:377` links to
  `../evidence/source_metadata/registry_metadata_20261006.json`, absent
  on base and post alike (same as the wave-4 finding).

## 9. Deletions (coordinator, AFTER landing + readback)

The 36 root originals, each with 404-verification and confirmation of
`mathematics/cayley-arithmetic/` (36 files). Do NOT delete before the push
lands:

1. `mathematics/cayley_additive_energy.md`
2. `mathematics/cayley_centered_energy.md`
3. `mathematics/cayley_curve_uniform.md`
4. `mathematics/cayley_difference_discriminant.md`
5. `mathematics/cayley_direct_energy.md`
6. `mathematics/cayley_energy_curve_bound.md`
7. `mathematics/cayley_exact_baseline_density.md`
8. `mathematics/cayley_fourier_hybrid.md`
9. `mathematics/cayley_frobenius_amplification.md`
10. `mathematics/cayley_inverse_pair_sum_factorization.md`
11. `mathematics/cayley_inverse_resultant_transversality.md`
12. `mathematics/cayley_jacobi_trace_average.md`
13. `mathematics/cayley_multiplicative_rigidity.md`
14. `mathematics/cayley_principal_subresultant_support.md`
15. `mathematics/cayley_product_discriminant.md`
16. `mathematics/cayley_product_row_coefficient_ideal.md`
17. `mathematics/cayley_product_row_elliptic.md`
18. `mathematics/cayley_product_row_intersections.md`
19. `mathematics/cayley_product_row_projective_bezout.md`
20. `mathematics/cayley_product_row_real_trace_ideal.md`
21. `mathematics/cayley_product_row_reflection.md`
22. `mathematics/cayley_product_row_subresultants.md`
23. `mathematics/cayley_ratio_orbit_factorization.md`
24. `mathematics/cayley_resultant_mass_budget.md`
25. `mathematics/cayley_resultant_structure.md`
26. `mathematics/cayley_scaling_rigidity.md`
27. `mathematics/cayley_shift_psc_transversality.md`
28. `mathematics/cayley_shifted_energy_orbits.md`
29. `mathematics/cayley_sylvester_fitting_support.md`
30. `mathematics/cayley_trace_gaussian_limit.md`
31. `mathematics/cayley_trace_intercept_rigidity.md`
32. `mathematics/elliptic_pencil.md`
33. `mathematics/fibonacci_ratio_energy_proof.md`
34. `mathematics/fourth_moment_reduction.md`
35. `mathematics/offoff_elliptic_spike_theorem.md`
36. `mathematics/pell_coboundary_fourth_moment.md`

## 10. Push order note for the coordinator

This wave assumes the wave-4 push AND its 9 deletions have landed (base
already models the wave-4 end state; live verification §1 confirms the
touched files). The wave-5 (pell) push is independent: it does not touch
any file in this staging except, potentially, the pell topic list (no —
the pell list does not contain `pell_coboundary_fourth_moment.md`'s new
path; that note is cayley-arithmetic's, and its link to the still-root
`pell_coboundary_resonance.md` becomes `../pell_coboundary_resonance.md`
here, and must be re-pointed again by the pell wave when that target moves
to its own home — flagged for the pell assembler, not fixed here).
One connector push-files commit carries the staging (§10 of REPORT.md);
readback of every blob SHA follows; then the §9 deletions, each 404-checked.
