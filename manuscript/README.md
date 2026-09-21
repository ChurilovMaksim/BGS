# Manuscript

`WoW_unified.tex` is the single maintained publication entry point on `main`.

The files in `unified_sections/` are source segments of that one manuscript. Some long sections are split into sequential `*_partN.tex` files solely to preserve exact recovered bytes while retaining later corrections already present in `main`; the parts are non-overlapping and are included in order by `WoW_unified.tex`.

The six `unified_sections/return_*.tex` chapters are generated from the
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

The 21 September fixed-map continuation is maintained directly as
`unified_sections/research_20260921.tex` and is included immediately after
the generated fixed-map frontier.  Its detailed theorem statements live in
`../mathematics/`; the TeX section is a publication summary, not a second
claim authority.

The fixed-map frontier chapter is generated from
`../mathematics/fixed_map_resolvent_frontier.md` by
`computations/maintenance/sync_fixed_map_section.py`. Use `--check` to detect
drift. Its detailed proofs and computational evidence are indexed in
`../supplement/fixed_map/README.md`; the conditional loop criterion is not
an established BGS limit for the frozen map.


The recovered Heisenberg direct-attack layer is summarized in
`unified_sections/recovered_heisenberg_20260921.tex`.  Its authoritative
proofs are the maintained Markdown notes
`../mathematics/fixed_map_weyl_path_escape.md`,
`../mathematics/hyperbolic_19adic_dephasing.md` and
`../mathematics/one_shear_antiunitary_no_go.md`; the historical v7--v11
dossiers are provenance, not parallel claim authorities.
