# One consolidated manuscript

`WoW_unified.tex` is the canonical reading/build entry point for this packet.
It has one abstract, contents list and bibliography. The `unified_sections/`
files are the reviewed TeX units; `unified_sources/` retains the selected
immutable proof-source texts for provenance. Older article sources are kept
only as historical/verification inputs, not as separate deliverable PDFs.

Build from repository root:

```sh
python computations/maintenance/build_unified_manuscript.py --publish
```

This uses an out-of-tree build directory, runs three LaTeX passes and rejects
undefined references/citations, duplicate labels and horizontal overflow. The
build manifest records exact TeX/PDF hashes. It does not prove the mathematics.
The delivered PDF additionally underwent page-image review.

The conceptual additions and exact review limits are in
`record/final_consolidation_audit_20260906.md`. The source map is
`record/consolidation_map.json`; the external-input ledger is
`literature/consolidation_sources_20260906.md`. None is a priority certificate,
a new Lean proof, or a statement that remote main/CI was updated.

To retain the completed review, edit the canonical TeX and corresponding
proof note coherently. The first-pass import used Pandoc, but subsequent
hypothesis restoration, notation reconciliation and conservative corrections
are recorded in the audit; blindly reimporting historical Markdown can undo
them. LaTeX is now the authoritative typeset source.
