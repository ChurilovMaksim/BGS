# Research index

This file answers two questions: **what has actually been done in this repository?** and **where should a researcher look for it?** It is intentionally broader than `STATUS.md`. `STATUS.md` says what is currently trusted; this index maps the full scientific program, including intermediate and failed lines.

## Scientific objective

The project studies quantized hyperbolic cat maps and the route from exact finite-field/character-sum identities to random-matrix spectral statistics after symmetry reduction. The long-term target is a rigorous BGS/local-law result. General BGS is not yet proved.

## Current load-bearing line

The current proof program is built around the exact pair-key fourth-moment distribution `B(t)` and its Fourier transform `Sigma4(q)`.

What is currently in good shape:

- exact finite pair-key/fourth-moment identities and independent finite checks;
- exact Fourier mean/variance duality for `Sigma4`;
- exact mixed `k=2` reduction to Cayley-set additive energy outside explicit cyclotomic exception primes;
- the mean geometry and generic off/off elliptic-family description;
- a restricted M1 proof chain for odd prime `K`, explicit nonexceptional split primes and `K=o(N^(1/4))`.

What is not yet a final theorem:

- the restricted M1 chain still needs a line-by-line proof audit/formalization, especially computer-assisted algebraic factorizations and the precise sheaf-theoretic hypotheses/citations;
- general BGS/local eigenphase statistics remain open.

See `STATUS.md`, `research/theory.md`, `research/problems/m1_fluctuation_energy.md`, `research/notes/k2_cayley_energy.md` and `research/notes/m1_offoff_elliptic_family.md`.

## Where the multi-year work lives

### Quantization and finite-field core

- `code/core/` — cat-map quantization, independent constructions, reduced resonance and subgroup/Kloosterman foundations.
- `code/math/` — promoted mathematical kernels used by current checks.
- `src/python/bgs/` — current reusable exact/symbolic implementation layer.

### Exact moments, large-m and local-law experiments

- `code/large_m/` — the large historical research surface: exact/empirical moments, shape modes, rigidity controls, local-law pilots, spectral fourth moments, finite-size diagnostics and successive M1/M2 experiments.
- `data/moments/` — stored moment outputs.
- `data/spectral/` — stored spectral/statistical outputs.
- `results/numerical/` — promoted numerical evidence only.

### Pair-key / M1 fourth-moment program

- `research/` — current derivations and theorem-draft chain.
- `experiments/verification/` — current reproducible identity/falsifier drivers.
- `src/cpp/verification/` — independent exact C++ verification where scientific independence matters.
- `results/verified/` — promoted finite certificates.

### Shape automata, relation counting and Run-82 line

- `code/shape_automaton/` — historical Python research around shape/word/relation automata.
- `code/large_m/` — related historical DP/calibration experiments.
- `src/cpp/shape/relation_automaton.cpp` — consolidated supported C++20 relation-DP implementation replacing useful Julia variants.
- `inputs/r82-legacy/` — preserved regression inputs.

### Kloosterman, subgroup and number-theory investigations

- `code/kloosterman/` — subgroup/Kloosterman experiments.
- `code/utils/` — supporting number-theory utilities retained from the research workspace.
- `src/cpp/number_theory/catmap_order.cpp` — supported order/prime-scan replacement for the useful Julia scan.
- `experiments/number_theory/` — current deterministic probes.

### Rank-2 / Sp4 program

- `code/sp4/` — rank-2/Sp4 computational experiments.
- `data/rank2_sp4/` — corresponding data products.
- `docs/sp4_project_scope.md` — scope and interpretation notes.
- historical multiplicity falsifiers remain available because negative results matter for narrowing the theorem statement.

### Diagnostics, falsifiers and red-team work

- `code/diagnostics/` — calibration, moment certification, Hecke/local-law diagnostics and other falsifiers.
- `data/diagnostics/` — diagnostic outputs.
- `docs/review/` — referee/red-team/checking corpus.
- `docs/REVIEW_FINDINGS.md` — current review findings; older `REVIEW_ERRORS.md` is retained for provenance but is superseded where they conflict.
- `docs/cycle2_falsifier.md`, `docs/trace_fluctuation_lemma.md` and related standalone notes document important negative or corrective work.

### Historical proof attempts and research ledger

- `docs/archive/` — old run notes and failed/provisional routes retained as research history.
- `docs/THEORY_FULL_PRE_REBUILD.md` — full old theory notebook.
- `docs/HISTORY_FULL_PRE_REBUILD.md` — full old research ledger preserved verbatim; it contains known mojibake from earlier encoding mishandling but is not data-loss.
- `data/proof/` — historical directory name only. Contents are not automatically proofs; use `data/MANIFEST.md` and `STATUS.md`.

### Formalization

- `formal/` — Lean sources for finite/combinatorial pieces and related formal experiments. Generated `.lake/build` and dependency trees are intentionally not versioned.

### Literature and manuscript

- `references/` — current bibliography/provenance used by the active proof program.
- `docs/literature/` — broader historical literature notes.
- `paper/main.tex` — the only active manuscript source.
- `paper/main.pdf` — synchronized build target.
- historical competing manuscripts stay only in the immutable provenance snapshot/Git history, not as active `final`, `proof`, `complete`, or section-level TeX alternatives.

## Trust levels

### A — current/audited

Use by default for new theorem work:

`STATUS.md`, `research/`, `src/`, `experiments/`, `results/verified/`, current `formal/`, `paper/main.tex`.

### B — research corpus

Scientifically useful but not automatically theorem-certified:

`code/`, `data/`, `docs/`, `inputs/`.

These paths include successful experiments, intermediate calculations, old APIs, finite evidence and falsified routes. They are kept because research provenance is useful; individual files must be promoted deliberately before becoming theorem dependencies.

### C — immutable provenance

`archive/legacy-workspace/`.

This is the full pre-restructure snapshot and the single retained home of old Julia sources. It exists as insurance and reconstruction provenance, not as the default workspace.

## Language migration status

The historical Julia layer contained 31 paths but only 23 byte-distinct sources. The active repository does not duplicate those files. `research/engineering/language_migration.md` gives the complete path-by-path disposition.

Current policy:

- Python for exact/symbolic orchestration and readable analysis;
- C++20 for heavy finite-field/exhaustive kernels and independent exact verifiers;
- Fortran only if profiling produces a genuine dense-numerical use case;
- no duplicate implementation merely to say that a result was checked in another language.

The migration itself is also an audit: several Julia claims were found to be mislabeled or false and therefore became permanent falsifiers rather than mechanically translated production code.

## Known quarantines that must not be forgotten

- General BGS is not proved.
- Historical M4D/Mobius-fiber theorem is not an active theorem input.
- Historical N=95419 spacing script compared a gap-ratio statistic against an ordinary spacing CDF; its verdict is invalid for the named test.
- Historical word-trace certificate had an unresolved word case.
- Hecke-centering Julia series was a failed line and is retained only as provenance/refutation.
- Historical `cdense_transfer.jl` Perron bracket is falsified by the zero-cost self-loop.
- Historical `sol6_closed_form.jl` closed-form claim is falsified by exact finite rows.

## Recommended entry sequence for a new collaborator

1. `README.md`
2. this file
3. `STATUS.md`
4. `research/theory.md`
5. `research/ledger.md`
6. `data/MANIFEST.md`
7. `code/README.md`
8. `research/engineering/language_migration.md`
9. only then the broad `docs/archive/` or `archive/legacy-workspace/` if provenance is needed.

The repository policy is: **do not delete a useful failed experiment; do not promote it merely because it exists.**
