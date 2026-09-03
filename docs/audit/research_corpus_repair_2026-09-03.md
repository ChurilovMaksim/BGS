# Full research-corpus repair and language-migration boundary

Date: 2026-09-03

## Why this repair was necessary

A later repository restructure kept the old work recoverable under `archive/legacy-workspace/`, but again compressed the ordinary working tree too aggressively. `main` no longer exposed the broad `code/`, `data/`, `docs/` and `inputs/` corpus, so the repository visually resembled a small M1-only project even though the multi-year research record still existed.

That organization was unsuitable for a live research laboratory. The repair restores the broad corpus to ordinary paths while retaining the newer exact pair-key/M1 work, Python/C++ migration, single-manuscript structure and explicit trust boundary.

## Preservation source

The broad corpus was reconstructed from the previously audited completeness tree rooted at commit `a8c3da78fa5195bfa2feceb031ffbf0c082dc14e`. That audit had already checked approximately 1062 working/research files outside the immutable snapshot, 168 Python sources with zero compile errors, and 255 JSON files with zero parse errors.

The newer language/paper/M1 branch was a strict descendant of the then-current `main`, so the repair was built on top of that newer branch rather than by reverting to the old tree. The result is a superset of the current scientific line and the broad research corpus.

## Ordinary working paths restored

- `code/` — broad research code: core, diagnostics, Kloosterman, large-m, shape automata, Sp4, theorem-oriented calculations, utilities, verification and maintenance.
- `data/` — diagnostics, legacy scientific artifacts, moments, proof-era outputs, rank-2/Sp4 and spectral outputs.
- `docs/` — literature, reviews/red-team material, old run archive, full pre-rebuild theory notebook and full research ledger.
- `inputs/` — immutable legacy regression/reconstruction inputs.

The newer `src/`, `experiments/`, `research/`, `results/`, `references/`, formal M1 work and single `paper/main.tex` remain in place.

## Julia handling

The broad trees were not restored byte-for-byte because doing so would have reintroduced obsolete Julia next to its supported replacements. Instead, original Git subtrees were reused and only the explicitly inventoried Julia paths were removed from ordinary working paths.

Removed from active `code/`:

- six `code/large_m/*.jl` files;
- four `code/shape_automaton/*.jl` files;
- five Julia utilities;
- `legacy_verification/julia_cross_key.jl`.

Removed from active `data/`:

- six byte-identical Julia duplicates under `data/legacy/`.

Removed from active `docs/`:

- eight Hecke-centering Julia versions under the failed-line archive;
- one review Julia cross-check.

Every one of the 31 historical Julia paths is mapped in `research/engineering/language_migration.md`. The unique historical source remains once under `archive/legacy-workspace/` and Git history. No second Julia archive was created.

Post-repair recursive Git-tree checks find zero `.jl` paths in active `code/`, active `data/`, and active `docs/`.

## Formal-source reconciliation

The compact newer formal tree had added `Bgs/M1DegenerateFiber.lean` but dropped the older `Bgs/OpLocal.lean`. The repair merges the two sets. The active formal tree now retains:

- `K2Reduction.lean`
- `K4Variety.lean`
- `M1DegenerateFiber.lean`
- `OpLocal.lean`
- `ScaleLaw.lean`
- `TorusLevelSets.lean`

Generated `.lake/build` and dependency trees remain excluded.

## Manuscript boundary

Historical TeX documents remain inside documentation/provenance archives when they are part of the research record, but there is only one active article source: `paper/main.tex`. Historical `M4D_PROOF`, `BGS_COMPLETE`, section fragments and other competing manuscript snapshots are not restored as active paper sources.

## Navigation repair

The root documentation was rewritten so that the repository no longer looks like an unexplained M1 fragment:

- `README.md` explains the three repository layers;
- `RESEARCH_INDEX.md` maps the multi-year scientific program;
- `STATUS.md` states the current theorem/draft/retraction boundary;
- `THEORY.md` gives the current mathematical architecture;
- `HISTORY.md` gives the readable phase history and points to the full ledger;
- `ROADMAP.md` separates proof audit, generalization, numerical/local-law work, corpus re-certification, language migration and formal/manuscript work.

## Scientific status preserved

This repair changes repository organization, not theorem status.

- General BGS remains unproved.
- The restricted M1 `K=o(N^(1/4))` chain remains a theorem draft pending proof audit/formalization.
- The historical Mobius-fiber/M4D theorem, N=95419 spacing verdict, unresolved word-trace certificate, failed Hecke-centering series, `cdense_transfer` Perron bracket and `sol6` closed-form claim remain quarantined/retracted as documented in `STATUS.md`.

The repository policy after this repair is: **broad working visibility, single-source provenance, no language duplication, and explicit promotion gates.**
