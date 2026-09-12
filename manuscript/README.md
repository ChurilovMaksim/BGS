# Manuscript

`WoW_unified.tex` is the single maintained publication entry point on `main`.

The files in `unified_sections/` are source segments of that one manuscript. Some long sections are split into sequential `*_partN.tex` files solely to preserve exact recovered bytes while retaining later corrections already present in `main`; the parts are non-overlapping and are included in order by `WoW_unified.tex`.

The five `unified_sections/return_*.tex` chapters are generated from the
corresponding maintained Markdown proofs by
`computations/maintenance/sync_return_sections.py`. Their headers record the
source hashes. Edit the Markdown sources and regenerate; `--check` detects
drift. Other sections remain directly maintained TeX. New return-law equation
tags carry a `Ret.` prefix to distinguish them from older article tags.

Build with:

```sh
python ../computations/maintenance/build_unified_manuscript.py --output-dir ../build/unified-paper
```

or from the repository root:

```sh
python computations/maintenance/build_unified_manuscript.py --output-dir build/unified-paper
```

Old standalone article `.tex/.pdf` copies are intentionally absent from the current tree. They were inputs to the consolidation process and remain recoverable from Git history; they are not separate maintained deliverables.

The scientific claim-status authority is `../record/claim_ledger.md`; the source-consolidation map is `../record/consolidation_map.json`.
