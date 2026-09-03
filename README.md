# Quantized cat maps and BGS — complete research workspace

This repository is the working research record for quantized hyperbolic cat maps, symmetry reduction, moment identities and the BGS/local-statistics program. It is deliberately **broad in preservation and narrow in trust**: useful experiments, intermediate calculations, negative results, literature notes and historical derivations stay available, while theorem status is controlled separately.

**Bottom line:** general BGS is not proved. The strongest current line is the exact pair-key/fourth-moment program summarized in `STATUS.md`; a restricted M1 concentration theorem for explicit split primes and `K=o(N^(1/4))` is an assembled proof draft pending line-by-line audit/formalization. M1 is therefore the present bottleneck, not the whole repository.

## Read this first

1. `RESEARCH_INDEX.md` — map of the entire research program and where the multi-year corpus lives.
2. `STATUS.md` — authoritative theorem/draft/retraction boundary.
3. `research/theory.md` — current mathematical core.
4. `research/ledger.md` — current research chronology and decisions.
5. `data/MANIFEST.md` — status/provenance guide for the broad output corpus.
6. `code/README.md` — map of the broad executable research corpus.
7. `research/engineering/language_migration.md` — Julia-to-Python/C++ audit and replacement map.
8. `paper/main.tex` — single canonical manuscript source; `paper/main.pdf` is the synchronized build target.

## Repository layers

### 1. Current/audited layer

- `src/python/bgs/` — reusable current Python kernels.
- `src/cpp/` — performance-critical and independently verified C++20 kernels.
- `experiments/` — current reproducible drivers/falsifiers; not a second library tree.
- `research/` — current proof program, notes, problem statements and engineering records.
- `results/verified/` — promoted exact/finite certificates.
- `results/diagnostics/` — current falsifiers and diagnostic outputs.
- `results/numerical/` — numerical evidence only.
- `formal/` — Lean sources/certificates with status stated explicitly.
- `paper/` — one active manuscript, not a forest of competing TeX drafts.

### 2. Full research corpus

These paths are ordinary working material, not hidden archive storage:

- `code/` — broad historical and intermediate Python research code: core quantization, diagnostics, Kloosterman, large-m, shape automata, Sp4, theorem-oriented computations, utilities, verification and maintenance.
- `data/` — diagnostics, moments, spectral data, rank-2/Sp4 data, proof-era outputs and preserved legacy numerical artifacts with an explicit manifest.
- `docs/` — literature notes, referee/red-team material, old run archive, project notes, full pre-rebuild theory notebook and full historical research ledger.
- `inputs/` — immutable legacy inputs used for regression/reconstruction.

The broad corpus is retained because failed routes, finite counterexamples, calibration outputs and old computational experiments are part of the scientific provenance and often become useful again during proof repair.

### 3. Immutable provenance snapshot

- `archive/legacy-workspace/` — one complete pre-restructure snapshot used only as insurance/provenance.

It does **not** override `STATUS.md`, and it is not the primary place to browse the project. Old Julia sources live there once; they are intentionally not duplicated back into the active research corpus after migration.

## Language policy

- Python: symbolic/exact orchestration, data analysis, moderate numerical work and readable research implementations.
- C++20: expensive finite-field loops, exhaustive combinatorics, dynamic programs and independent exact verification.
- Fortran: only if profiling identifies a dense numerical kernel for which it materially improves the implementation; no language is introduced for cosmetic diversity.
- Independent duplicate implementations are kept only when independence is itself part of a scientific certificate.

All 31 historical Julia paths are accounted for in `research/engineering/language_migration.md`. Useful mathematics is consolidated into a smaller set of supported Python/C++ components; falsified or superseded Julia lines are preserved only in the immutable archive/Git history rather than translated mechanically.

## Trust rule

A filename containing `proof`, `theorem`, `final` or `certificate` is not sufficient evidence of theorem status. `STATUS.md` is authoritative. In particular, the historical Mobius-fiber/M4D route, the old N=95419 spacing verdict, the unresolved word-trace certificate and several Hecke-centering/transfer claims remain explicitly quarantined.

The intended working rule is simple: **preserve broadly; promote only after reconstruction, falsification attempts and an appropriate independent check.**
