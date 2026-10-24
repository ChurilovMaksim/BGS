# MANIFEST — P2-MATH wave 4 (returns): mathematics/ root → mathematics/returns/

Wave 4 of the P2-MATH topical reorganization (topics map
`record/mathematics_topics.json`, topic `returns`). Base: wave-7 post tree
overlaid with the landed P2-SPECTRAL staging (live main commit fdf9179,
verified: `literature/external_dependencies.json` blob ccb3c946… == live main,
`record/claims.json` blob eebf6feb… == live main, record/ root listing
60 files + 2 dirs on live main incl. the still-present spectral originals)
and the verified-but-not-yet-pushed external-epoch channel staging (3 files).
This staging is the SECOND wave-4 assembly: the first
(`pkg_p2_math4_final/`, 35 files) predates waves 7/spectral/channel and is
superseded by it — its note moves and consumer migrations were re-verified
against this base, not copied blindly. Two of its translations are WRONG on
this base (see §2, resonance links) and are corrected here.

Membership is strictly the topics-map `returns` list: exactly 9 notes, in no
other topic. No dated names occur in this wave, so no renaming.

## 1. Moves (old path → new home, SHA-256 of file bytes)

- `mathematics/analytic_kick_return_gas.md` → `mathematics/returns/analytic_kick_return_gas.md` — link-translated copy (§2)
  - base: 2d6125b255f0541d5a852e31ecae8cedc5fdb1fd3b0cca7da55f16a20d38792c
  - post: 65454c4c76c6778d660c78c78f9ad77cd68bd58d451ddfe4e67ce4540e5850bf
- `mathematics/fixed_harmonic_return_gas.md` → `mathematics/returns/fixed_harmonic_return_gas.md` — link-translated copy (§2)
  - base: 264577142b622a5f4318b549dd3530cd72585bfd92bddf5b50703f988b5bdd60 (differs from the first assembly's base: wave 7 moved its link target into `resonance-cohomology/`)
  - post: a16a89d031eb9fafbe0837ac29e50802a8700219ef8ef023e97ece2d153da5cf
- `mathematics/general_cat_return_laws.md` → `mathematics/returns/general_cat_return_laws.md` — link-translated copy (§2)
  - base: 7327182cb21ffc4537b458cb603e4ecff289eb6f7c1230fff6ef8b32e3bd8546
  - post: abb8c7cbb9a6dddc7a5b39ab3affc2ed7fa0d256ec38bc3ff51af55074148c4d
- `mathematics/hyperbolic_return_pressure.md` → `mathematics/returns/hyperbolic_return_pressure.md` — byte copy
  - base = post: 0996851f0cf684006632d3794639f514e195d38ca76b7cc887ff7ec78e096806
- `mathematics/noncommuting_return_words.md` → `mathematics/returns/noncommuting_return_words.md` — byte copy
  - base = post: 6c6beb439424ed8e724d1296226d0b8f9687766b8f6149e8c2a8ba2409ceac28
- `mathematics/periodic_point_trace_comparison.md` → `mathematics/returns/periodic_point_trace_comparison.md` — link-translated copy (§2)
  - base: 15cc5be5926855d35afc3dd76c72c86fcc9b3235230a0013f719b388cbcb01e1 (differs from the first assembly's base: wave 7 moved its link target into `resonance-cohomology/`)
  - post: d90b99291807cecef4229ef7e79bafe56e8df9a0856787285f37b60a17e65c25
- `mathematics/phase_space_return_gas.md` → `mathematics/returns/phase_space_return_gas.md` — link-translated copy (§2)
  - base: 95acc1bc4b196a68852a62cc813201bf2494a9ad36083fc45ec58d7f4ead6385
  - post: 3d818bc6a06975f35e53175003f76e4db11b4d47ad688763d19eeab9f116c71f
- `mathematics/return_trace_obstruction.md` → `mathematics/returns/return_trace_obstruction.md` — link-translated copy (§2)
  - base: 8641f69d69b1a14c63a8c76c5077d5d5418f54356704adc6e0ce8b9280f3ccf4
  - post: f231d062c33b09087d8efd746bc66e75e26fe842c9dbbf1cae165c95ea5d1be4
- `mathematics/smooth_recurrence_and_compensation.md` → `mathematics/returns/smooth_recurrence_and_compensation.md` — byte copy
  - base = post: 772bfc483e79ceac9d286846acff96ec4d4643fe15882fd85c5e89de593ea89f

Cross-check: for the 7 notes whose base bytes are unchanged since the first
assembly, the post SHA-256 values above reproduce the first assembly's post
values exactly; the 2 changed notes differ only by the corrected resonance
translations (§2). No mathematical content changed anywhere.

## 2. Cross-boundary link translations inside moved notes (base → post)

Rule (mechanical, applied to every relative markdown link except http(s)/
anchors and the TeX false positive `\right](r\epsilon)` in
`fixed_harmonic_return_gas.md`): sibling links inside the wave stay bare
(valid in the common home); every other relative link gains one `../`
(bare root notes, `../X` paths, and `subdir/X` paths alike — the parent
moves from `mathematics/` to `mathematics/returns/`).

- analytic_kick_return_gas.md: `../computations/verification/analytic_kick_return_gas.py` → `../../computations/verification/analytic_kick_return_gas.py`.
- fixed_harmonic_return_gas.md: `resonance-cohomology/even_period_spin_resonance.md` → `../resonance-cohomology/even_period_spin_resonance.md` (CORRECTED vs the first assembly, which wrote `../even_period_spin_resonance.md` — valid only pre-wave-7, when the target still lived in the root; on this base that path does not exist); `../computations/verification/fixed_harmonic_return_gas.py` → `../../computations/verification/fixed_harmonic_return_gas.py`.
- general_cat_return_laws.md: `../computations/verification/general_cat_return_laws.py` → `../../computations/verification/general_cat_return_laws.py`. (Sibling links to `phase_space_return_gas.md` / `periodic_point_trace_comparison.md` stay bare.)
- hyperbolic_return_pressure.md: no link changes (byte copy).
- noncommuting_return_words.md: no link changes (byte copy).
- periodic_point_trace_comparison.md: `resonance-cohomology/weighted_wiener_resonance.md` → `../resonance-cohomology/weighted_wiener_resonance.md` (CORRECTED vs the first assembly's `../weighted_wiener_resonance.md`, same wave-7 reason); `../computations/verification/periodic_point_trace_comparison.py` → `../../…`; `../literature/periodic_return_clt_sources.md` → `../../…`; `pell_smooth_resonance.md` (×2) → `../pell_smooth_resonance.md`. (Sibling links to `fixed_harmonic_return_gas.md` / `phase_space_return_gas.md` stay bare.)
- phase_space_return_gas.md: `../computations/verification/phase_space_return_gas.py` → `../../…`; `../literature/periodic_return_clt_sources.md` → `../../…`. (Sibling links stay bare.)
- return_trace_obstruction.md: `pell_harmonic_returns.md` → `../pell_harmonic_returns.md`; `../literature/return_local_limits_sources.md` → `../../…`; `../record/return_obstruction_review_20260912.md` → `../../…`; `../record/return_local_limits_review_20260913.md` → `../../…`. (Sibling link to `general_cat_return_laws.md` stays bare.)
- smooth_recurrence_and_compensation.md: no link changes (byte copy).

## 3. Consumers migrated in the same commit (all asserted by occurrence count)

- `record/mathematics_topics.json` — 9 paths of topic `returns` (1 occurrence each); `updated` already 2026-10-24, unchanged.
- `mathematics/topics/returns/README.md` — 15 links `../../<stem>.md` → `../../returns/<stem>.md`; the `../../../archive/…` link untouched.
- `computations/maintenance/sync_return_sections.py` — SOURCES: 6 names → `returns/<stem>` (render builds `mathematics/returns/<stem>.md` and the `% Source:` header itself).
- `computations/verification/repository_audit.py` — ACTIVE path `mathematics/return_trace_obstruction.md` → `mathematics/returns/…` (only that line; the wave-7 resonance-cohomology ACTIVE entries are preserved — the first assembly's whole-file copy would have reverted them).
- `computations/verification/phase_space_return_gas.py` — docstring path → new home.
- Linking notes (1 link each): `mathematics/compensated_heisenberg_trace_control.md` (smooth), `mathematics/dyson_relaxation_obstruction.md` (return_trace), `mathematics/frozen_periodic_point_annihilator.md` (periodic_point), `mathematics/fixed_model_pell_crossover.md` (smooth), `mathematics/resonance-cohomology/even_period_spin_resonance.md` (`../hyperbolic_return_pressure.md` → `../returns/hyperbolic_return_pressure.md`; same note as the first assembly's root linking note, now in its wave-7 home with wave-7 link geometry).
- `mathematics/open_questions.md` — 1 prose code-span → path form.
- `literature/periodic_return_clt_sources.md` — 2 links → new homes.
- `literature/bibliography.md` — 1 prose code-span → path form.
- `papers/return-laws/README.md` (2 links) and `papers/return-laws/paper.json` (2 `authoritative_sources`) → new homes.
- `record/return_obstruction_review_20260912.md`, `record/return_local_limits_review_20260913.md` — 1 link each (ACTIVE_MARKDOWN files, hence live despite dated names).
- `record/errata.json` — ERR-050 `authority` → new home (no epoch pins on errata lines).
- Regenerated (not hand-edited): `docs/corpus_atlas.md` (exactly 9 lines, paths only), `record/claim_registry.md` (exactly 2 lines, RET-003/004 source), `record/scientific_dependency_graph.md` (exactly 2 lines), `STATUS.md` (exactly 1 line: 69 → 70 historical claim amendments). `record/scientific_dependencies.json`, `ERRATA.md`, `mathematics/results.md` regenerated byte-identically and are NOT in the push set.
- Maintained count control: registered == maintained == 334 (root −9, home returns +9).

## 4. Claims channel (existing mechanism, rebased onto the wave-7 state)

Base state (verified mechanically): 197 claims; `historical_claim_amendments`
69 rows; `approved` set 69 ids; wave2 run() signature unchanged 27 / amended
69. After this wave: amendments 70, approved 70, unchanged 26, amended 70.

- Sealed amendment (first P2-MATH sealed amendment, proof_dependencies class):
  BGS-FM-002 (`proved`), `fields = {proof_dependencies}` only.
  Sealed wave2 row canonical SHA-256 (sort_keys, separators `(',',':')`,
  ensure_ascii=False, same serializer as `check_prior_claims`):
  `77c66814b3f714c21a6eaef51e2b87302b89a1c18db101da5f763204e4f98d78`
  (identical to the first assembly's value — the sealed row never changed).
  `proof_dependencies[0]`: `mathematics/smooth_recurrence_and_compensation.md`
  → `mathematics/returns/smooth_recurrence_and_compensation.md`; the other
  2 list elements and `source` (`mathematics/fixed_model_pell_crossover.md`)
  untouched. Amendment row appended to `record/claim_integration_epochs.json`
  (disposition: sealed row preserved, only the topical relocation admitted,
  no status/source/content change; review: this manifest). `approved` in
  `computations/verification/wave2_integration_audit.py` extended 69 → 70
  (`'BGS-FM-002'` appended to the literal; channel code untouched).
  `wave2 run()` delta base → post is EXACTLY two lines:
  `unchanged_prior_claims` 27 → 26, `explicitly_amended_prior_claims`
  69 → 70; every other field byte-identical (JSON SHA base
  5b53fba8… → post eee32a75…).
- Follow-on source ×2 (after_wave3 gate pins state+source; state unchanged):
  BGS-RET-003 (`conditional`) and BGS-RET-004 (`proved`), `source`
  `mathematics/noncommuting_return_words.md` →
  `mathematics/returns/noncommuting_return_words.md`, in `record/claims.json`
  (2 occurrences) and in the 2 `after_wave3` rows of
  `record/claim_integration_epochs.json`. No sealed amendments for them
  (not in the wave2 snapshot).
- Full claims.json scan (all fields, all 197 rows) finds no other mention of
  any returns note. `formalization[]` contains no mathematics/ paths.

## 5. External channel (new mechanism; re-measured on THIS base)

Re-measurement (recursive scan of `literature/external_dependencies.json`
for all 9 stems, all fields including nested `additional_uses[].project_sources`):
exactly 5 field-values in 4 SEALED contracts (39-contract snapshot
2026-10-07; all sealed rows byte-identical to the snapshot on base).
This CONFIRMS the channel agent's note (5 rows for 4 contracts) and
contradicts the executor's earlier recount of "4 mentions": the fifth
mention is EXT-SOSH-2000's second field, `additional_uses`, whose nested
`project_sources` names `return_trace_obstruction.md` — a plain
top-level-only scan misses it. No admitted-18 row names any returns note
(recursive scan: zero admitted hits), so no admitted row takes any path.

Rows added to `record/external_epoch_amendments.json` (from the channel's
empty set; one row per (contract, field); canonical contract SHA-256 with
the same serializer as §4):

| Contract | Field | Old value | New value | historical_contract_sha256 |
|---|---|---|---|---|
| EXT-SOSH-2000 | project_sources | […, `mathematics/return_trace_obstruction.md`] (element 4) | […, `mathematics/returns/return_trace_obstruction.md`] | b64623c64b7731feda6aed90041a57c07e1d0e2f7bc17e16e9e8a420ae3f2f44 |
| EXT-SOSH-2000 | additional_uses | [{…, `project_sources`: [`mathematics/return_trace_obstruction.md`]}] | [{…, `project_sources`: [`mathematics/returns/return_trace_obstruction.md`]}] | b64623c64b7731feda6aed90041a57c07e1d0e2f7bc17e16e9e8a420ae3f2f44 |
| EXT-CC-2013 | project_sources | [`mathematics/periodic_point_trace_comparison.md`] | [`mathematics/returns/periodic_point_trace_comparison.md`] | 2bccdbd9a14080051525eb78ac200801ddf29fe4624051503434131f960030fc |
| EXT-PY-2015 | project_sources | [`mathematics/fixed_harmonic_return_gas.md`] | [`mathematics/returns/fixed_harmonic_return_gas.md`] | 992da7bd6b3c04079516c4fef81020d9d382e7a280c44e7eea58eda82bae881b |
| EXT-DH-2011 | project_sources | [`mathematics/return_trace_obstruction.md`] | [`mathematics/returns/return_trace_obstruction.md`] | 3b71070ce48c7d8c61da5aa4aff328330e6e3b65689aaf473c407776545183f5 |

Each row: `wave: P2-MATH wave 4`, disposition (sealed contract preserved;
only the topical relocation in this field admitted; no other change),
`review: archive/MANIFEST-P2MATH4.md`. `metadata_audit` is NOT amended
(provenance pointer, governed by the cache guard — see §6).
`check_external_epoch` on post: `(39, 18)`. Scratch proof that the rows
are load-bearing (not vacuous): post checker + epochs + snapshot +
registry with an EMPTY store fails with
`historical external contract changed: EXT-SOSH-2000`; with the post
store it passes `(39, 18)`. The pre-channel failure mode (unrecorded
sealed change fails) is thereby preserved and the wave passes through
the reviewed channel, not around it.

## 6. Bibliographic cache refresh (second gate for the same migration)

Measured, not assumed: `bibliographic_metadata_audit.validate()` compares
`project_sources`/`additional_uses` of EVERY registry row — sealed and
admitted alike — against the reviewed cache. Stage-1 post (external rows
migrated, store rows present, cache untouched) failed the self-test with
exactly the 5 errors of §5. The epoch store rows therefore do NOT suffice
for the bibliographic gate; the sealed rows need the cache-refresh recipe
too, as a separate mechanism (the store governs the epoch seal; the
snapshot governs the bibliographic guard; neither substitutes for the
other). Admitted-18 rows: none touched, so no admitted row takes the
cache-only path — the cache refresh here serves sealed rows' bibliographic
gate only, and is stated as such to keep the two mechanisms separate.

- New snapshot `evidence/source_metadata/registry_metadata_20261024_p2math4.json`
  (SHA-256 `3f84faf500161b3a6cf9cd10192874af27dfdbc3893c54c3b7b30400bc7b2826`)
  + `…_p2math4.sha256`, chaining to the 2026-10-24 refresh snapshot
  (`current_review.previous_snapshot_sha256`
  `16e01d7975ff75f79af0462388b4747eae907c41798949cea1aa1560180ba711`).
  Diff vs the superseded snapshot is exactly 13 leaves: 9 path copies
  (accepted fields ×5 + duplicated top-level `project_sources` copies ×4,
  updated so the snapshot stays internally consistent) + `scope` +
  `current_review.{record, previous_snapshot_sha256, scope}`. No observation
  re-retrieved, no review hash changed, no claim state or graph impact
  change. The superseded snapshot is preserved byte-identically.
- Pointer `literature/metadata_audit.json` repointed by exactly 3 lines
  (cache, digest, review → `record/audits/metadata_cache_refresh_20261024_p2math4/report.md`).
- Self-test after refresh: rc=0, 515 mutation tests, 57 cached identities.

## 7. Channel-test fixture fix (first-wave consequence, test only)

The channel's epoch tests as landed assume the committed store is empty:
the fixture copies the LIVE registry into scratch roots and `save_store`
replaces the committed store. Once wave 4 lands 5 rows, that assumption is
false — demonstrated, not theorized: stage-1 post epoch tests ran 11/12,
the single failure being `test_reviewed_amendment_admitted_at_exact_value`
(`historical external contract changed: EXT-SOSH-2000`, its
`additional_uses` left unrecorded in the scratch store). Fix, in
`computations/maintenance/tests/test_external_epoch_preservation.py` ONLY
(the checker `wave2_integration_audit.py` is untouched except the §4
approved literal): the fixture now builds the scratch registry from the
SEALED baseline (snapshot's 39 rows) plus the live admitted-later rows
(which are not byte-compared), instead of copying the live registry
wholesale; the docstring records why. All scratch controls then test the
channel mechanics independently of which waves have landed. Post-fix:
epoch tests 12/12. The alternative (leaving the fixture, accepting 11/12
on main after this wave) was rejected: it would land a red test that the
wave itself caused.

## 8. Residual classification (post tree; zero live pointers at old paths)

Full scan for the 9 old `mathematics/<stem>.md` strings (109 files):
- LIVE, intentional: `record/external_epoch_amendments.json` (old_values,
  §5); `record/claim_integration_epochs.json` (FM-002 disposition prose
  quoting the old path while describing the relocation);
  `computations/maintenance/tests/test_external_epoch_preservation.py`
  (scratch-test strings for sealed old values, temp roots only).
- LIVE, pre-existing dispositions (unchanged by this wave, byte-identical
  to base): `record/claim_ledger.md` (narrative table prose, waves 1–3
  precedent — not markdown links, repository_audit green);
  `manuscript/unified_sections/return_{gas,position,periodic,phase,general,obstruction}.tex`
  (generated chapters, already stale on base under the pandoc CI debt;
  sync `--check` stale lists base-identical; NOT hand-edited, updated at
  the next sync regeneration);
  `supplement/fixed_map/algebraic-return/checkpoint.json` (content pin
  on pre-move bytes, no consumers, deliberately not rotated).
- FROZEN (never edited, resolved by this manifest): all `archive/**` and
  `evidence/**` carriers (dated manifests, workspace snapshots, sealed
  checkpoint inputs, superseded cache snapshots incl.
  `registry_metadata_20261024_refresh.json`, the sealed external snapshot
  itself), `record/audits/**` dated snapshots and era inventories, and
  `archive/MANIFEST-P2MATH7.md` / `archive/MANIFEST-Adata.md` prose.
- NOT present anywhere live: any migrated consumer, any regenerated view,
  any claims/epochs field except the two intentional prose cases above.
- Pre-existing break (not wave-caused, noted, not fixed here):
  `literature/bibliography.md:377` links to
  `../evidence/source_metadata/registry_metadata_20261006.json`, absent
  on base and post alike (same as the first assembly's finding).

## 9. Deletions (coordinator, AFTER landing + readback)

1. `mathematics/analytic_kick_return_gas.md`
2. `mathematics/fixed_harmonic_return_gas.md`
3. `mathematics/general_cat_return_laws.md`
4. `mathematics/hyperbolic_return_pressure.md`
5. `mathematics/noncommuting_return_words.md`
6. `mathematics/periodic_point_trace_comparison.md`
7. `mathematics/phase_space_return_gas.md`
8. `mathematics/return_trace_obstruction.md`
9. `mathematics/smooth_recurrence_and_compensation.md`

Each with 404-verification and confirmation of `mathematics/returns/`
(9 files). Do NOT delete before the push lands.

## 10. Push order note for the coordinator

This wave assumes the external-epoch channel commit has landed first
(empty store → this wave's 5 rows; the channel staging's 3 files are part
of the base, not of this push, except the test-file fixture fix in §7,
which IS in this push). The P2-SPECTRAL deletions (3 record/ originals)
are independent of this wave and are not included here.
