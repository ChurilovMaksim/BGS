# P2-MATH wave 8 manifest: spectral-obstructions → mathematics/spectral-obstructions/

Base: live main 49cdacb (wave 4 closed; all 9 returns originals deleted,
`mathematics/returns/` holds exactly the 9 files), as verified by connector
readback before assembly (claims.json blob 219ff8f3…, external_dependencies
blob 2a5efd69…, topics blob 3736eb86… — all equal to the local base tree).
Local base: the wave-4 post tree (which already reflects the wave-4
deletions). This package pushes NOTHING; the parent pushes the staging and
deletes the 10 originals afterwards (see §7 for the one deletion with a
separate gate).

Membership is strictly the `spectral-obstructions` list of
`record/mathematics_topics.json`, homed by first listing in wave order
(foundations, locality, information-theory, returns, pell,
cayley-arithmetic, resonance-cohomology, spectral-obstructions, fixed-map,
trace-bridge). Five of the ten notes are also listed under fixed-map (1) or
trace-bridge (4); those other entries are updated to the canonical path in
this same wave (§3). No note of this wave is listed under any other topic.

## 1. Old → new path map (10 notes; 3 dated names renamed to subject names)

| Old path | New path | SHA-256 (old root file) | SHA-256 (new file) | Change |
|---|---|---|---|---|
| mathematics/arithmetic_translation_exclusion.md | mathematics/spectral-obstructions/arithmetic_translation_exclusion.md | 7ff84cac…b962cb1 | 53b17b35…f7b | link translation only (§2) |
| mathematics/arithmetic_word_expansion_obstruction.md | mathematics/spectral-obstructions/arithmetic_word_expansion_obstruction.md | 8cf36bc4…0769b86 | c85cd81c…ee9b | link translation only (§2) |
| mathematics/coherence_memory_plateau_20261014.md | mathematics/spectral-obstructions/coherence_memory_plateau.md | 629c5d16…2e059e | bd0386d4…6448b | renamed + link translation |
| mathematics/coherent_first_return_pulse_20261014.md | mathematics/spectral-obstructions/coherent_first_return_pulse.md | f6deb5aa…862ff | fcc20d9a…f17 | renamed + link translation |
| mathematics/cue_singular_energy.md | mathematics/spectral-obstructions/cue_singular_energy.md | 13efcb31…77d72c | e995ea22…f2c9965 | link translation only (§2) |
| mathematics/flat_spectrum_obstruction_20261014.md | mathematics/spectral-obstructions/flat_spectrum_obstruction.md | 4e236e23…20bfe8 | 33cda26a…e53b | renamed + link translation |
| mathematics/general_hyperbolic_prime_spectra.md | mathematics/spectral-obstructions/general_hyperbolic_prime_spectra.md | f8c4bb71…e8773e | f8c4bb71…e8773e | byte copy (no links) |
| mathematics/isospectral_clock_moment_control.md | mathematics/spectral-obstructions/isospectral_clock_moment_control.md | 00ee83a0…3658b | 44034dbe…96e96 | link translation only (§2) |
| mathematics/magnetic_quotient_semicircle.md | mathematics/spectral-obstructions/magnetic_quotient_semicircle.md | 8c9eb05b…16747f1 | 8c9eb05b…16747f1 | byte copy (no links) |
| mathematics/microscopic_rounding_control.md | mathematics/spectral-obstructions/microscopic_rounding_control.md | 68a0b67c…34c6889 | 68a0b67c…34c6889 | byte copy (prose code-spans point at unmoved notes, unchanged) |

Full hashes: old flat_spectrum_obstruction_20261014 =
4e236e230962909581522f8941e1c9085a5947963c69b48074385c5da620bfe8;
new flat_spectrum_obstruction =
33cda26a263327c89dc943485b1dacc9e5e21ba0bd3cc767629864bc5689e53b.
No mathematical content changed anywhere: every differing line in the eight
translated copies is a link target (verified by per-file diff).

## 2. Link-translation rule (moved notes only)

From `mathematics/` (depth 1) to `mathematics/spectral-obstructions/`
(depth 2): every `](../X)` becomes `](../../X)` (repo-root targets:
archive, computations, evidence, literature, formalization); bare sibling
links to notes still in the root become `../<stem>.md`
(`fixed_model_symmetry_theorem`, `frozen_operator_transfer_coercivity`,
`egorov_overlap_rigidity` — fixed-map wave 9 homes later;
`unconditional_feedback_flatness_20261013` — trace-bridge wave 10 home
later; those waves' own scans will re-point these links);
`locality/fixed_strength_locality.md` becomes
`../locality/fixed_strength_locality.md` (wave 2 home); same-wave dated
bare links become the renamed bare names. Root-absolute prose paths
(`mathematics/locality/…`, `mathematics/<unmoved>.md` code-spans in
`microscopic_rounding_control.md`) stay valid and are unchanged.

## 3. Consumers migrated in the same commit

- `record/mathematics_topics.json`: 15 path values (10 spectral entries +
  1 fixed-map + 4 trace-bridge entries).
- `record/claims.json`: 8 `source` values (CUE-001, TRACE-013/014, FM-023,
  TRACE-081/082/083, CAYLEY-009) + TRACE-072 `proof_dependencies[2]`
  (non-pinned field; its `after_wave3` row pins only state+source, both
  unchanged — no epoch row touched for TRACE-072).
- `record/claim_integration_epochs.json`: `after_wave3` sources ×4
  (TRACE-081/082/083, CAYLEY-009); sealed amendments: CUE-001 NEW row
  (sealed SHA 31d0cda413e2f46cceedee78ed1ff4ab44cbe2b2a1e329dd6a93864783ac9a2f,
  fields `{source}`); TRACE-013/014/FM-023 rows EXTENDED with `source`
  (their sealed SHAs are unchanged and still match their existing rows:
  9bbaa57a…, 53a4a89b…, 60ef64cd…; dispositions and reviews extended with
  this wave's relocation and this manifest). One row per id is preserved
  (the checker keys amendments by id).
- `computations/verification/wave2_integration_audit.py`: approved set
  70 → 71 (`'BGS-CUE-001'` appended at the tail).
- `literature/external_dependencies.json`: 5 `project_sources` values (§4).
- `record/external_epoch_amendments.json`: 5 new rows, extending wave 4's
  5 rows to 10 (§4).
- `evidence/source_metadata/registry_metadata_20261024_p2math8.json` +
  `.sha256` + `literature/metadata_audit.json` pointer repoint +
  `record/audits/metadata_cache_refresh_20261024_p2math8/report.md`
  (Pittel recipe for the bibliographic guard, §4).
- Verifiers: `computations/verification/expansion_wavepacket_audit.py`
  (`sources[0]`); `computations/verification/spectrum_coherence_controls.py`
  (name tuple renamed + `ROOT/'mathematics/spectral-obstructions'/name`);
  `computations/verification/spectrum_coherence_contract.json`
  (4 path values: `execution_artifacts` ×2, `inputs` ×2);
  `computations/python/bgs/magnetic_quotient.py` (docstring path).
- Prose/link consumers: `RESEARCH.md` (5 links), `mathematics/results.md`
  (5), `mathematics/open_questions.md` (5),
  `mathematics/fixed_map_resolvent_frontier.md` (2),
  `mathematics/deterministic_path_transport_20261011.md` (1),
  `mathematics/foundations/hyperbolic_signed_trace_extension.md` (1),
  `mathematics/resonance-cohomology/analytic_poisson_rigidity.md` (1),
  `mathematics/topics/spectral-obstructions/README.md` (12),
  `mathematics/topics/fixed-map/README.md` (1),
  `mathematics/topics/trace-bridge/README.md` (4),
  `mathematics/symplectic_half_radius_obstruction.md` (1 code-span path),
  `literature/cue_singular_energy_sources.md` (1),
  `literature/coherence_first_return_context_20261014.md` (1),
  `literature/magnetic_quotient_sources_20260905.md` (1 code-span),
  `literature/bibliography.md` (1, hand prose — the bibliography generator
  only normalizes `references.bib` and checks consistency),
  `docs/reader_guide.en.md` + `docs/reader_guide.ru.md` (1 each).
- Regenerated (not hand-edited): `docs/corpus_atlas.md` (30 lines: 15 old
  + 15 new paths), `record/claim_registry.md` (16 lines: 8 claims ×2),
  `record/scientific_dependency_graph.md` (16 lines: 8 claims ×2),
  `STATUS.md` (exactly 1 line: 70 → 71 historical amendments),
  `mathematics/results.md` (regenerator preserves the 5 hand edits above;
  its generated block is byte-identical to base). Byte-identical after
  regeneration and therefore NOT in the package:
  `record/scientific_dependencies.json`, `ERRATA.md`.

## 4. External epoch: 5 sealed contracts, 5 new amendment rows

All five contracts are in the sealed 39-row snapshot
(`archive/evidence/executions/20261011/chat-research/baselines/external_dependencies_20261007.json`);
none is admitted-later. Field `project_sources` in each row.

| Contract | Sealed SHA-256 (first 16 hex) | Migrated element |
|---|---|---|
| EXT-BAB-2013 | 263edd88d87528e7 | cue_singular_energy.md → spectral-obstructions/cue_singular_energy.md |
| EXT-POPESCU-2023 | e44bf55725007477 | arithmetic_word_expansion_obstruction.md → spectral-obstructions/… |
| EXT-BG-2008 | 6c0f2f4bc913325e | same as POPESCU |
| EXT-GAE-2007 | 02c22fcf3ea7e7f9 | same as POPESCU |
| EXT-DIRICHLET-1837 | ecfcc43150477217 | same as POPESCU |

The bibliographic guard additionally required the cache refresh of §3:
before it, the self-test failed with exactly these five
`project_sources differs from reviewed cache` errors; after the new
snapshot (chained to the wave-4 snapshot SHA-256
3f84faf500161b3a6cf9cd10192874af27dfdbc3893c54c3b7b30400bc7b2826;
new snapshot SHA-256
51a2ff09bd3d4e250c5ac33e846bf5f2bf9375a28eac2db2e150aef2deb6f3a5),
the self-test passes 515 mutation tests. Per contract, 3 snapshot leaves
were updated (accepted field + duplicated top-level copy +
`file_level_claim_matches[].source`) for internal consistency.

## 5. Deliberately NOT touched (with reasons)

- `record/claim_ledger.md` (narrative prose, waves 1–4 precedent) and
  `manuscript/unified_sections/*.tex` (stale generated chapters; the next
  sync/build regenerates them — waves 1–4 precedent).
- `record/wave2_replay_source_bindings.json`,
  `record/wave2_scoped_input_bindings.json`,
  `record/charge_strengthening_*.json`,
  `record/research_checkpoint_import.json`: sealed replay-complex machines
  (F-STAY class; re-basing them is phase-7-class work). The wave2 audit
  `run()` reads the SEALED copies, so it is unaffected — but see §7.
- `mathematics/scaled_weyl_overlap_20261015.md:332`: a historical citation
  naming a fetched blob hash at the old path; re-pointing it would falsify
  the citation. Left as a dated citation.
- `computations/verification/general_hyperbolic_prime_spectra.py:2`:
  docstring names the stem only, not a path; the stem is unchanged.
- Frozen carriers (`archive/`, `evidence/` sealed inputs, era-attestation
  inventories, superseded cache snapshots): never edited; resolved by this
  manifest.

## 6. Controls (post tree = landed state: originals removed, as in wave 4)

See the wave report for the full table. Headlines: fast controls green
except the three known pre-existing pandoc sync reds (signatures identical
to base) AND the §7 blocker (wave2 `run()` cannot complete in the landed
state — it stops at the pinned-path read; the amendment machinery itself
is verified by the epoch tests 12/12, and the wave2 count delta was
measured in a scratch copy of the post tree with only the pinned file
temporarily restored from base — see the wave report for the measured
delta, which is exactly the CUE-001 amendment);
`check_external_epoch` returns (39, 18); full discover — see the wave
report for the measured result (note: `test_wave2_portable_replay` calls
`sealed_source_bytes()`, which reads the live pinned path, so the §7
blocker reaches into the discover suite as well);
maintained count 334 == 334; repository audit rc=0; bibliographic
self-test rc=0 (515); staging == post byte comparison over every staging
file. Pre-existing reds NOT chased: `wave3_integration_audit.run()` fails
on the clean base (CAYLEY-001, no amendment channel; CI does not invoke
it); Hardy verifier timeout on 2 vCPU; `resonant_density_audit` needs
numpy>=2.

## 7. Deletions (parent, after landing + readback) — WITH ONE GATE

Delete the 10 root originals:

1. `mathematics/arithmetic_translation_exclusion.md`
2. `mathematics/arithmetic_word_expansion_obstruction.md`
3. `mathematics/coherence_memory_plateau_20261014.md`
4. `mathematics/coherent_first_return_pulse_20261014.md`
5. `mathematics/cue_singular_energy.md`
6. `mathematics/flat_spectrum_obstruction_20261014.md`
7. `mathematics/general_hyperbolic_prime_spectra.md`
8. `mathematics/isospectral_clock_moment_control.md`
9. `mathematics/magnetic_quotient_semicircle.md`
10. `mathematics/microscopic_rounding_control.md`

GATE on item 10: `computations/verification/wave2_portable_replay.py
--check-sources` (a CI step) reads the LIVE path
`mathematics/microscopic_rounding_control.md` through
`wave2_replay_source_bindings.json` and requires its SHA-256
(68a0b67c…, unchanged by this byte-identical move). Deleting the root
original therefore breaks that CI step until the sealed complex is
re-based or its `historical_resolutions` mechanism is extended by a
governed decision (the checker currently hard-codes exactly the three
governance resolutions, so no wave-8 edit can route around it without
editing sealed-complex code — which this wave refuses to do). The parent
must either hold deletion 10, accept the CI break explicitly, or take the
re-basing decision separately; deletions 1–9 are clean. The other nine
notes do not appear in the replay bindings.
