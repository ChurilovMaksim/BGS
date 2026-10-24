# P2-MATH wave 5 (pell) — manifest

Topic `pell` of `record/mathematics_topics.json` (17 notes) moves from the
`mathematics/` root into the topical home `mathematics/pell/`. Same-commit
migration of every live consumer, two sealed claim amendments, five
follow-on claim sources, three sealed external-contract amendments, and a
provenance-only metadata-cache refresh for the same three contracts.
Nothing is pushed by this manifest; deletions of the 17 root originals are
a separate coordinator step after landing and readback.

## 1. Membership (measured, not improvised)

Home rule (wave plan §3): a note's home is the first wave, in wave order
(foundations, locality, information-theory, returns, pell,
cayley-arithmetic, resonance-cohomology, spectral-obstructions, fixed-map,
trace-bridge), whose topic lists it. The `pell` list holds exactly 17
paths; every one of them is first-listed by `pell` (no earlier wave
claimed any of them, none is listed by any other topic, so no other topic
entry needs a canonical-path update in this wave). No dated names: no
`pell` note is renamed (design §7 renaming applies to dated names only;
none of the 17 carries a date).

| Old path | New path |
|---|---|
| `mathematics/pell_all_orders_conjugacy.md` | `mathematics/pell/pell_all_orders_conjugacy.md` |
| `mathematics/pell_cat_map_gaussian_blocks.md` | `mathematics/pell/pell_cat_map_gaussian_blocks.md` |
| `mathematics/pell_coboundary_resonance.md` | `mathematics/pell/pell_coboundary_resonance.md` |
| `mathematics/pell_fixed_strength_review.md` | `mathematics/pell/pell_fixed_strength_review.md` |
| `mathematics/pell_floquet_normal_form.md` | `mathematics/pell/pell_floquet_normal_form.md` |
| `mathematics/pell_four_mode_coercivity.md` | `mathematics/pell/pell_four_mode_coercivity.md` |
| `mathematics/pell_harmonic_returns.md` | `mathematics/pell/pell_harmonic_returns.md` |
| `mathematics/pell_harmonic_transition.md` | `mathematics/pell/pell_harmonic_transition.md` |
| `mathematics/pell_microscopic_clustering.md` | `mathematics/pell/pell_microscopic_clustering.md` |
| `mathematics/pell_phase_rate.md` | `mathematics/pell/pell_phase_rate.md` |
| `mathematics/pell_polynomial_edgeworth.md` | `mathematics/pell/pell_polynomial_edgeworth.md` |
| `mathematics/pell_resonance_comb.md` | `mathematics/pell/pell_resonance_comb.md` |
| `mathematics/pell_resonance_lattice.md` | `mathematics/pell/pell_resonance_lattice.md` |
| `mathematics/pell_sharp_orbit_coercivity.md` | `mathematics/pell/pell_sharp_orbit_coercivity.md` |
| `mathematics/pell_single_orbit_sharp_constant.md` | `mathematics/pell/pell_single_orbit_sharp_constant.md` |
| `mathematics/pell_smooth_resonance.md` | `mathematics/pell/pell_smooth_resonance.md` |
| `mathematics/pell_weighted_gaussian_echo.md` | `mathematics/pell/pell_weighted_gaussian_echo.md` |

## 2. Move mechanics (content preserved)

16 notes are byte copies. One note changes by exactly one link, a depth
translation, not a content change: `pell_all_orders_conjugacy.md` —
`../literature/all_orders_conjugacy_sources.md` becomes
`../../literature/all_orders_conjugacy_sources.md` (one directory deeper).
All other intra-wave links are bare sibling links (`pell_X.md`), which stay
correct inside the shared new directory; prose code-span mentions of
sibling notes inside the moved notes stay correct for the same reason, and
the `literature/pell_floquet_sources.md` prose mention is repo-relative
and unchanged. No mathematical content, status, or boundary changed in any
moved note.

## 3. Epoch: sealed claims (2) and follow-on claims (5 + 1 unpinned field)

Sealed rows are measured against the wave2 snapshot
(`evidence/wave2_checked_20261007/raw/provenance/base_navigation/record/claims.json`,
canonical SHA: `sort_keys=True`, `separators=(',',':')`,
`ensure_ascii=False`).

- BGS-RET-001 (`proved`): already carried a phase-1 amendment row
  (authority corrections, SHA
  `9dbdb912ab367d8d6ad0fa7d3758c8074a40e93378491c1a370dd278053439b5`).
  A second row on the same id is mechanically impossible
  (`check_prior_claims` builds `amendments={row['id']:row}` and requires
  `len(amendments)==len(rows)` and `set(amendments)==approved`), so the
  existing row is EXTENDED, wave 7 precedent: `fields` gains
  `source: mathematics/pell/pell_harmonic_returns.md`, disposition gains
  the relocation sentence, `review` is repointed to this manifest (which
  documents both the inherited authority part and the new source part);
  `historical_row_sha256` is unchanged. Row count does not move for this
  claim.
- BGS-RET-002 (`proved`): no prior row; sealed SHA
  `881476b450767aeb07e3eb3bb739c7b2df5677a2f3a63c0eec6d1c73211540d1`.
  NEW row appended at the tail of `historical_claim_amendments`:
  `fields={source: mathematics/pell/pell_harmonic_transition.md}`,
  disposition in wave 4 style, `review: archive/MANIFEST-P2MATH5.md`.
- `approved` in `computations/verification/wave2_integration_audit.py`:
  70 → 71 (`'BGS-RET-002'` appended to the literal; no checker logic
  touched). `wave2 run()` delta is exactly two fields:
  `unchanged_prior_claims` 26 → 25,
  `explicitly_amended_prior_claims` 70 → 71; JSON SHA
  `eee32a75…` → `1c395af9…`, all other fields byte-identical.
- Follow-on sources (claims.json `source` + `after_wave3` row, same
  commit; gate pins `state`+`source`, states unchanged): BGS-FLOW-022 and
  BGS-FLOW-025 (`pell_floquet_normal_form.md`), BGS-FLOW-023 and
  BGS-FLOW-024 (`pell_coboundary_resonance.md`), BGS-RES-008
  (`pell_sharp_orbit_coercivity.md`). Their `after_wave3` dispositions
  contain no pell path mentions and are untouched.
- BGS-RES-008 `proof_dependencies`:
  `mathematics/pell_single_orbit_sharp_constant.md` →
  `mathematics/pell/pell_single_orbit_sharp_constant.md` in claims.json
  ONLY. It is not a pinned epoch field: the `after_wave3` row carries no
  `proof_dependencies` key, so no epoch row changes for it. It migrates
  because it is a live consumer — `scientific_registry_audit` applies
  `require_path` to every `proof_dependencies` entry, so leaving the old
  path would fail the registry audit after the deletions. This reading of
  the brief ("not pinned") is flagged for the coordinator: if the intent
  was to leave the value untouched, the registry audit would go red and
  the wave would not be green.

## 4. External epoch channel (3 rows) + cache refresh

Recursive scan of `literature/external_dependencies.json` (including
nested `additional_uses[].project_sources`): exactly 3 values, all in
sealed (39-row snapshot) contracts, none admitted-later, none with a
second field. Store `record/external_epoch_amendments.json` grows 5 → 8
rows (wave 4 rows untouched, order preserved, new rows appended):

| Contract | Field | Sealed contract SHA | Old → new |
|---|---|---|---|
| EXT-DR-2009 | `project_sources` | `14a22959…b2cd0` | `mathematics/pell_sharp_orbit_coercivity.md` → `mathematics/pell/…` |
| EXT-DEMNI-2016 | `project_sources` | `fea323c1…83a` | `mathematics/pell_harmonic_returns.md` → `mathematics/pell/…` |
| EXT-COSY-2024 | `project_sources` | `2de7f9bd…073` | `mathematics/pell_harmonic_transition.md` → `mathematics/pell/…` |

(Full SHAs in the store rows; `check_external_epoch` on the post tree:
`(39, 18)`.) As in wave 4, the bibliographic guard is a second, separate
gate: the post-move tree failed its self-test with exactly those three
errors, so this wave carries the Pittel-recipe refresh —
`evidence/source_metadata/registry_metadata_20261024_p2math5.json`
(SHA-256 `469898c51d0bad04976a83c6d40ffddf9198beabae2fb2ed8be736b6a76d6583`,
chained to the p2math4 snapshot `3f84faf5…b2826` via
`current_review.previous_snapshot_sha256`) + `.sha256` + pointer repoint
in `literature/metadata_audit.json` (cache, digest, review — 3 lines) +
report `record/audits/metadata_cache_refresh_20261024_p2math5/report.md`.
Leaf diff vs the superseded snapshot: exactly 12 (accepted
`project_sources` ×3, duplicated top-level `project_sources` ×3,
`file_level_claim_matches` source ×2 for RET-001/RET-002, `scope`,
`current_review.{record, previous_snapshot_sha256, scope}`). No source
re-reviewed, no review hash changed, no claim `external_dependencies`
changed.

## 5. Other live consumers migrated (same commit)

- `record/mathematics_topics.json`: 17 pell paths → new homes (no other
  topic entry touched; `updated`/`policy` untouched).
- Topic view `mathematics/topics/pell/README.md`: 23 links
  `../../pell_X.md` → `../../pell/pell_X.md` (the archive link untouched).
- Root linkers (bare sibling links → `pell/` subpath):
  `mathematics/coboundary_spectral_flow_bound.md`,
  `mathematics/fixed_map_resolvent_frontier.md`,
  `mathematics/pell_coboundary_fourth_moment.md` (×1 each, all to
  `pell_coboundary_resonance.md`).
- Returns-home linkers: `mathematics/returns/periodic_point_trace_comparison.md`
  (×2, `../pell_smooth_resonance.md` → `../pell/…`) and
  `mathematics/returns/return_trace_obstruction.md` (×1,
  `../pell_harmonic_returns.md` → `../pell/…`).
- Prose path-form migrations (wave 1 / wave 7 precedent):
  `mathematics/open_questions.md` (code-span
  `` `pell_harmonic_returns.md` `` → `` `pell/pell_harmonic_returns.md` ``),
  `mathematics/exact_homoclinic_potential.md` (see-list
  `pell_smooth_resonance.md` → `pell/pell_smooth_resonance.md`),
  `supplement/fixed_map/design-return/finite_symbol_normal_form.md`
  (code-span `mathematics/pell_floquet_normal_form.md` → `mathematics/pell/…`).
- Papers: `papers/return-laws/README.md` (2 links) and
  `papers/return-laws/paper.json` (2 `authoritative_sources`).
- Computations (docstrings + live path constants, all resolve-checked):
  `computations/verification/pell_coboundary_regression.py`,
  `pell_floquet_regression.py`, `pell_gamma_interval.py`,
  `pell_harmonic_transition.py`,
  `computations/analysis/pell_harmonic_transition_figure.py`.
- Manuscript (GitHub href URLs only, wave 7 precedent):
  `manuscript/unified_sections/return_obstruction.tex` (×1),
  `return_periodic.tex` (×2), `fixed_map_frontier.tex` (×1).
- Regenerated (not hand-edited): `docs/corpus_atlas.md` (exactly 17
  Pell-section lines), `record/claim_registry.md` (7 claim lines),
  `record/scientific_dependency_graph.md` (7 claim lines), `STATUS.md`
  (exactly 1 line: 70 → 71 historical claim amendments).
  Byte-identically regenerated and NOT in the package:
  `record/scientific_dependencies.json`, `mathematics/results.md`,
  `literature/references.bib`, `literature/bibliography.md`,
  `record/errata.json`, `ERRATA.md`. Maintained count: 334 == 334.

## 6. Deliberately NOT touched (classified residual)

- Frozen carriers: `archive/**`, `evidence/**` (except the new cache
  snapshot, which is a new file, not an edit), `record/audits/**`
  (except the new refresh report), dated snapshots and sealed inputs —
  old pell paths there are historical records, resolved by this manifest.
- `record/claim_ledger.md`: narrative prose code-spans (RET-001/002,
  FLOW-era lines) — ledger narrative precedent of waves 1–4; not links,
  not resolvers.
- Bare-name prose that is not a path: sibling code-spans inside moved
  notes (still siblings in `pell/`); `pell_coboundary_fourth_moment.md`
  evidence/code-span lines naming its own verifier and certificate;
  `computations/cpp/pell_minimal_relation_verifier.cpp` comment naming
  its note; `--only` stems in `REPRODUCE_unified.md` and
  `computations/maintenance/verify_workspace.py`; module imports
  (`from pell_harmonic_transition import …`); figure SVG paths in
  `assets/` and reader guides; `manuscript/BGS_unified.tex`
  `\input{unified_sections/pell_*.tex}` (section files, not mathematics
  paths); bare `\path{…}`/`\url{…}` names in manuscript sections
  (wave 7 precedent: only full GitHub href URLs migrate);
  `record/consolidation_map.json`
  `historical_inputs_removed_from_active_tree` (historical list);
  `record/publication_review_20260912.md` (dated review);
  `mathematics/exact_homoclinic_potential.md`'s bare
  `periodic_point_trace_comparison.md` (a returns note — wave 4/7 both
  left it bare; not this wave's note, not re-opened here).
- Pre-existing gap, unchanged: `literature/bibliography.md:377` link to
  the absent `registry_metadata_20261006.json` (present on base and post
  alike; not this wave's).

## 7. Controls (post tree, after deletions applied locally)

Fast set (`run_controls.sh`): registry audit OK, repository audit rc=0,
bibliographic self-test rc=0, epoch tests 12/12, all five render
`--check`s rc=0, manuscript references rc=0, `wave2 run()` passed with
the §3 delta, `check_external_epoch` (39, 18). The three sync `--check`s
are rc=1 with stale lists byte-identical to base (known pandoc CI debt
№3; pre-existing, not this wave). Full discover (see REPORT.md) and the
rehearsal script (`p2_math5_work/rehearsal.py`, ALL PASS, including two
negative epoch controls) are recorded in REPORT.md.

## 8. Deletions (coordinator, after landing + readback)

The 17 root originals of §1, each 404-checked, with `mathematics/pell/`
confirmed at 17 files. No staging file references any of the 9 deleted
wave-4 returns root paths (checked at staging assembly).

## 9. Addendum: wave-4 returns hrefs in the two touched tex files

The coordinator's wave-4-closure check requires no staging file to
reference the 9 deleted returns root paths as live paths. Two tex files
already in this package carried pre-existing live GitHub hrefs to those
now-deleted roots (wave 4 migrated no manuscript hrefs); the three hrefs
inside files this wave already touches are repaired here, same mechanism
as the pell hrefs:
`return_obstruction.tex:344` (`general_cat_return_laws.md`),
`return_periodic.tex:358` (`fixed_harmonic_return_gas.md`) and
`return_periodic.tex:673` (`phase_space_return_gas.md`) — each gains the
`returns/` segment. Deliberately left, and reported as wave-4 residual for
a manuscript-href sweep (not this wave's files): live hrefs to deleted
returns roots in `return_general.tex` (×2), `return_phase.tex` (×3) and
`return_position.tex` (×1); `% Source:` comment headers naming deleted
roots in six tex files (comments are stripped by the manuscript audit's
`active_tex` and were left untouched by wave 7 in the same position);
and the intentional `old_value` / disposition mentions of deleted roots
in the epoch store and FM-002 disposition, which the seal checkers
require to stay byte-exact. After this repair, no staging file contains
a live link or path reference to a deleted returns root.
