# src/maintenance/

One-off, idempotent maintenance scripts, kept for provenance so that every edit
to a document or paper is reproducible. Each verifies its target before acting and
reports NOOP if already applied.

| script | what it did |
|---|---|
| `repair_legacy_paper.py` | 6 audit-driven edits to `paper/resonance_laws_catmaps.tex` (closed the unbalanced `remark`, removed the retracted max/median figure, restated U4, downgraded the smooth law, withdrew a `cor:domination` clause, retracted the Hecke row) |
| `patch_theory_r71.py` | inserted the VOID banner above THEORY 8.0.4 and appended section 9 |
| `theory_section9.md` | the text appended by the above |
| `publish_r72.py` … `publish_r74.py` | appended the run entries to LEDGER.md and THEORY.md and refreshed README / ROADMAP / MANIFEST |
| `publish_lemmaF.py`, `publish_thmG.py`, `publish_r736.py` | the same for the individual R73 results |
| `hygiene_r72.py` | 7 hygiene fixes from the 2026-08-28 audit (invalid JSON, dead REPRO paths, quarantined r=6 artifacts, in-place retraction warnings, MANIFEST provenance warning, T13 row) |
| `fix_tex_rows.py`, `fix_tex_tr.py` | repaired LaTeX row terminators and a missing math operator |
| `consolidate.py` | recursive path resolution, stale-citation repair, stray-log tidy, empty-directory removal |
| `consistency_audit.py` | **the standing check**: every cited path exists, and all 27 headline numbers in the papers match the artifacts. Exit 0 means clean |
| `patch_auditor.py` | exempted citations explicitly annotated `(absent …)` |

Run `python src/maintenance/consistency_audit.py` after any edit to a document.
