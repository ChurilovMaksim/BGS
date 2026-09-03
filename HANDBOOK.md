# Research handbook

This repository is a live mathematical research workspace, not a release tarball. The operating rule is **preserve broadly, trust narrowly, migrate deliberately**.

## Before changing mathematics

Read `STATUS.md` and `RESEARCH_INDEX.md`. `STATUS.md` is authoritative for theorem/draft/retraction status. A historical filename such as `proof`, `final`, `theorem` or `certificate` does not promote a claim.

## Directory roles

- `src/`: supported reusable implementations.
- `experiments/`: reproducible drivers and falsifiers.
- `research/`: current mathematical program and proof notes.
- `results/`: promoted current outputs.
- `code/`, `data/`, `docs/`, `inputs/`: broad working/research corpus retained from the multi-year project.
- `formal/`: Lean/formal work.
- `paper/`: one canonical manuscript.
- `archive/legacy-workspace/`: immutable provenance snapshot only.

Do not move useful working material into `archive/` merely to make the root look small. Conversely, do not treat the broad research corpus as automatically audited.

## Promotion protocol

A historical or exploratory result becomes a current dependency only after:

1. reconstructing what statistic/object the producer actually computes;
2. checking mathematical normalization and asymptotic regime;
3. running an appropriate falsifier/regression test;
4. using an independent implementation when independence materially strengthens the certificate;
5. recording the status change in `STATUS.md`/`research/ledger.md` and, where relevant, `data/MANIFEST.md`.

Negative results and counterexamples are retained and labeled; they are not deleted to make the story cleaner.

## Language policy

Python is the default for readable exact/symbolic work and analysis. C++20 is preferred for performance-critical finite-field/exhaustive kernels. Fortran is introduced only for a profiled dense-numerical kernel with a concrete benefit. Old Julia code is not copied around: the historical source exists once under `archive/legacy-workspace/`; `research/engineering/language_migration.md` records its supported replacement or quarantine status.

A second implementation is justified only when it provides scientific independence, not as routine duplication.

## Manuscript policy

`paper/main.tex` is the only active TeX manuscript. Supporting figures/data may be separate assets, but there must not be competing `final`, `complete`, `proof` or section-level active manuscript trees. Retracted historical manuscripts remain recoverable through the immutable archive and Git history.

## Reproducibility

Prefer deterministic seeds, exact arithmetic where feasible, explicit finite-field conventions, and machine-readable outputs. Numerical evidence must be labeled numerical; finite exact checks must not be described as asymptotic proofs.

Generated build trees, caches and bundled tool binaries are repository hygiene exclusions, not scientific-data exclusions.
