# Final independent audit, 1 November 2026 (base main 7e143d40)

A cold read by an internal reviewer acting as an external referee, time-boxed to about 40 minutes. It is an internal review,
not external refereeing. No claim state, frozen packet, hash-pinned file or manuscript source was changed.

## What was checked

* **README.md / README.ru.md.** Every claim id with an adjacent state word (table cell or the text right after the id) against
  `record/claims.json` (`trace_status_check.py`, also run on RESULTS.md, RESEARCH.md, mathematics/results.md,
  mathematics/open_questions.md and CHANGELOG.md: 1478 id occurrences). All relative links and `#anchors` (`link_check.py`, 9 files,
  0 broken). EN/RU parity: identical multisets of claim ids and of numbers; same 23 headings; identical mermaid graphs (valid syntax).
  Counts recomputed from source: 419 claims = 338/17/21/42/1; the phase table (I–VII) by id range; 226/197 and 193/141; 144 non-open
  claims with Lean files; 155 modules under `formalization/Bgs`; 2186 `theorem`/`lemma`; `native_decide` 37 uses in 8 modules
  (comments and strings stripped); ERRATA 65 entries; 24 `referee/` folders; frozen packets 39 directories / 368 files; PDF 381
  pages; 40 test files. The README "Lean" column matches each claim's `formalization` field.
* **Theorem R♯-mod v5.** README, RESULTS.md, RESEARCH.md, open_questions.md and manuscript Section 126 against
  `THEOREM_DRAFT_v5.md` and the registry: Re Λ′_lo = 6.234e-4, δ_true ≤ 5.0313e-6 (= 2.2102e-6 + 2.712658e-6 + 1.0843e-7 + 3.1e-13),
  S_ρ ≥ c·1.13287^m, crossover 3305/3307 (C ≤ 0.082), 1726/1733, 1402/1409 (C ≤ 8.8e-4), +1% → 3359, Prop. K a ≤ 2.70e-3 and
  budget 2.738e-4, thresholds 1289/339/81/165, T′ = 1.42785; Table 5 rows all proved; Table 6 states. All agree.
* **Manuscript** (`pdftotext`): abstract, introduction, Lines I–N chapter (Section 126), conclusion (Section 127). Searched for
  stale current values (1386/1390/1397/1399 as threshold, 2.470e-6, v4 as current, 88 `native_decide`, old page counts): every
  occurrence is explicitly historical or superseded (BGS-TRACE-318, BGS-TRACE-322 a fortiori).
* RESULTS.md, RESEARCH.md, mathematics/results.md, open_questions.md, CHANGELOG.md, manuscript/README.md for stale or contradictory
  statements. Overstatement: BGS is consistently "not proved", R′ "open, not refuted", referees "internal".

## Findings

| # | Severity | Finding | Action |
|---|---|---|---|
| 1 | minor | README/README.ru use h_m, h_p, η, m, k1 kick, F_m, W′, RMT_m, "levels", "Robin" without definitions; a first-time reader cannot parse Phases VI–VII or the v5 section | **fixed**: a short notation paragraph (EN and RU) before Phase VI, taken from the Line B/G/I notes and Section 126.1 |
| 2 | minor | RESEARCH.md, 31 October section, lists "pending TRACE-320, 322–324" and "first prime 1399" without saying these are no longer current (322, 323 proved on 1 Nov; 1399 charges δ only) | **fixed**: dated qualifier added in place |
| 3 | minor | CHANGELOG.md has no entry for PR #73 (native_decide 88 → 37, p = 17 q = 103 exact [N] run) | **fixed**: entry added (no claim change) |
| 4 | cosmetic | Manuscript TOC order: Chapter 13 precedes Chapter 12, chapters interleave with "(continued)" dividers, and "Appendix B" sits mid-volume followed by non-appendix sections 53–60 | left: documented on purpose (manuscript/README.md, Figure 1 "no-reorder rule"); reordering would renumber sections cited across the record |
| 5 | cosmetic | Section 125 title reads "at eta two"; Section 127 is still labelled "Draft note" / "(DRAFT)" | left: wording only; would require a full 381-page rebuild for no content change |
| 6 | cosmetic | Registry titles of superseded claims keep old values (BGS-TRACE-318 "first prime 1399", BGS-TRACE-322 "2.470e-6", BGS-TRACE-301 "a = 5.93e-6") | left: each boundary states the supersession or a-fortiori status; the titles are true as stated, so no registry edit is warranted |
| 7 | info | `trace_status_check.py` reports 10 candidate mismatches, all false positives (state words that belong to a neighbouring clause, e.g. "open → proved" in CHANGELOG, "leaves the following open"), and 8 "unregistered" hits that are id ranges spanning the unregistered 138/139/334 | none needed |

No material error was found: no wrong state, count, link, threshold or constant in the reviewed surfaces, and no overstatement.

## Checks after the edits

`checks_branch.log` (23 checkers + all 8 `render_*.py --check`) and `checks_main_7e143d40.log` (same list on main): identical;
only `sync_return_sections.py --check` fails, on both, because pandoc is not installed (pre-existing). Unit tests:
`unittests_branch.log` (40 files, 266 tests, OK, 1 skip, serial run, 152 s; `test_fractional_routing` passed in that run). The manuscript was not edited, so it was not rebuilt.
