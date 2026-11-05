# Final polish pass, 5 November 2026

Branch `final-polish-20261105`, based on main `4487e66a`. Editorial integration of Phase VIII (BGS-TRACE-337..355),
release preparation for `research-2026.11.2`, and a set of wording fixes. **No claim state changed**, no file was deleted,
no frozen packet (`computations/maintenance/frozen_evidence_packets.json`: 39 directories, 368 files) was touched, and
`formalization/Bgs/SevenPrimary.lean` and its pin in `computations/verification/seven_primary_certificate.py` are
unchanged.

## Registry

* **BGS-CAYLEY-002, wording sync (no state change).** The boundary said that `CayleyEnergy.lean` checks the (461,23,23)
  design "by native_decide". The module has 21 theorems; 19 are now kernel-checked by `decide +kernel`, and only
  `k23_energy` and `k23_has_excess` (the K = 23 collision energy and its excess comparison) use `native_decide`. The
  boundary in `record/claims.json` now says so, and the sealed row is admitted by the amendment row for BGS-CAYLEY-002 in
  `record/claim_integration_epochs.json` (disposition "2026-11-05 wording sync (final polish)"). The text is the one
  proposed in PR #84.
* `record/claim_registry.md` re-rendered by `render_claim_registry.py`.
* `record/claim_verification_inventory.json`: the CAYLEY-002 boundary and `source_blob_sha` synced by
  [`edit_inventory.py`](edit_inventory.py), which asserts that the boundary of BGS-CAYLEY-002 is the only registry
  difference.
* `record/claim_ledger.md` (hand-written): dated sections for BGS-TRACE-337..355 and the CAYLEY-002 sync.

## Generated views (by their renderers only)

* `RESULTS.md` from `record/results_spec.json` (Phase VIII section; known issues on CI, `native_decide`, broken links and
  manuscript depth) and `computations/maintenance/render_results.py` (one phrase in the summary paragraph: the explicit H6
  threshold is conditional on squarefree h_p).
* `manuscript/appendix_a_claim_index.tex` by `render_appendix_a.py` (new mention locations in the front matter,
  introduction and conclusion).
* `evidence/executions/20261101/lean_inventory/INVENTORY.md` by its `make_inventory.py` (needs commit `a562e0cf`; the
  status sentence now names batches 6 and 6b). Registry-wide: 182 non-open claims link Lean; 195 modules.

## Hand-written pages

* `README.md` / `README.ru.md` (in parity): Phase VIII part of the abstract split into five numbered items (i)–(v), with BGS-TRACE-343 marked
  conditional; Phase VIII counts and narrative; results-table rows for BGS-TRACE-337, 342, 343, 346, 348, 352, 355; the
  v5 input table split into H5, H6, H7*, H8; a frontier bullet for the **unregistered** research (H5 structural ceiling
  with c_B = 0.7375 [P-sketch], θ_B = 0.2624, threshold 0.4753, Mersenne/Wagstaff-type question [C], heuristic [H];
  Lemma U with the open step (C-U) [C]; the "estimate U" of the Lemma S pass); mermaid node for Phase VIII; badges
  (conditional 25, concept DOI, CI, 380 pages); CI wording; Lean paragraph; checker pointer; known issues; citation
  `research-2026.11.2` with the concept DOI 10.5281/zenodo.23919483; -ize spelling in EN; the missing blank line after the
  RU results table (it made the "Метки" line render as a table row).
* `RESEARCH.md`, `mathematics/open_questions.md`, `docs/reader_guide.{en,ru}.md`, `mathematics/README.md`,
  `mathematics/topics/fixed-map/README.md`, `formalization/README.md` ("Current graph" paragraph), `manuscript/README.md`.
* `CHANGELOG.md`: the research-2026.11.1 release block moved below the 4 November span-theorem entry (it had been placed
  between two 4 November entries), "Lines A–N" corrected to "Phase V and Lines B–N" (there is no Line A), and new entries
  for this pass and for research-2026.11.2.
* `CITATION.cff` (version, `date-released: 2026-11-05`, top-level DOI = concept DOI; the 23919484 identifier is kept as
  the archive of research-2026.11.1) and `.zenodo.json` (version).
* `literature/bibliography.md`: one moved link repointed to
  `archive/evidence/source_metadata/registry_metadata_20261006.json` (the file is not hash-pinned); hash-pinned broken
  links are now 23 in 10 files.
* `evidence/breakthrough/` (README and 17 method notes): the 65 `sandbox://` links replaced by repository links,
  carried over verbatim from PR #84 (head `0550302d`); see [breakthrough_audit](breakthrough_audit/README.md).

## Manuscript

`front_matter.tex`, `ch01_introduction.tex`, `unified_sections/ch15_conclusion.tex`: eight phases and the 5 November
counts (438 = 353 / 17 / 25 / 42 / 1). The conclusion's "Draft note" label is now "Scope note" and the figure caption
no longer says "DRAFT". `figures/fig_reading_map.tex` adds the "Lines B–H" and "Lines I–N" parts and drops "(DRAFT)"
(this file is listed with an older sha in the historical receipt
`evidence/formalization/aristotle_20261027/receipt.json`; no checker reads that entry, and the receipt is not edited).
`unified_sections/lifted_transfer_lineFG.tex` and `lineH_49state_certificate.tex`: "eta two" → η = 2 in two headings.
`BGS_unified.tex`: date. No chapter reordered; section and theorem numbers are unchanged.

Build: `python computations/maintenance/build_unified_manuscript.py --engine auto --output-dir <tmp> --publish` with
pandoc 3.12.1 and pdfTeX (TeX Live 2026): status PASS, 380 pages
([manifest](logs/manuscript_build_manifest.json)). The previous published PDF had 381 pages; the TeX distribution
differs from the one used on 1 November.

## Checks (local, after all edits)

* 18 checkers: [logs/checks_18.log](logs/checks_18.log), all exit 0.
* Six further audits and the SevenPrimary certificate: [logs/checks_extra.log](logs/checks_extra.log), all exit 0.
* Unit tests: `python -m unittest discover -s computations/maintenance/tests` — 266 tests, OK (1 skipped)
  ([log](logs/unittests.log)).
* `git diff --diff-filter=D` against `4487e66a`: empty. No path in the frozen-packet registry is changed.
* Lean was not rebuilt locally (no `.lean` file changed); CI runs `lake build`.

## Deliberately not changed

* `formalization/Bgs/SevenPrimary.lean` (22 of the 37 `native_decide` uses; hash-pinned). The count 37 in 8 modules
  is described as is.
* The 23 remaining broken links in hash-pinned files.
* Chapter order of the manuscript; no new manuscript section for Phase VIII (its `manuscript` registry fields stay empty).
* The content of draft PRs #83 and #85 beyond what main already integrated; PR #84's SevenPrimary/FORMAL-003 change.
* Estimate U: added as an evidence-only research note, `evidence/research/20261105_estimate_u/` (verbatim copies of
  REPORT, BRIDGED, C0, CERT and REFEREE_CERT, small text/JSON logs under ~0.3 MB, and NOTE.md); large binaries and code
  are not copied. It produced no new full [CA] result, so nothing is registered, and the README frontier wording uses the
  tags of NOTE.md.
* No tag, release or Zenodo record is created here.
