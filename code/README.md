# Code map

`code/` is the broad executable research corpus. It is intentionally much larger than the supported library layer in `src/` because old experiments, diagnostics and theorem-oriented computations remain scientifically useful even when they are not current theorem dependencies.

## Supported current implementation layer

New reusable work should normally live in:

- `../src/python/bgs/` — current Python exact/symbolic kernels;
- `../src/cpp/` — current C++20 performance/exhaustive kernels and independent verifiers;
- `../experiments/` — current reproducible drivers and falsifiers.

Do not create a second library implementation in `code/` merely to mirror `src/`.

## Broad research corpus

- `core/` — cat-map quantisation and foundational constructions.
- `diagnostics/` — diagnostic, falsifier and calibration scripts.
- `kloosterman/` — subgroup/Kloosterman explorations.
- `large_m/` — large-m moments, spectral diagnostics, local-law pilots and successive M1/M2 investigations.
- `shape_automaton/` — shape/word/relation-automaton investigations.
- `sp4/` — rank-2/Sp4 experiments.
- `theorems/` — theorem-oriented computational derivations.
- `utils/` — supporting utilities.
- `llm/` — local research-assistance helpers retained from the workspace.
- `math/`, `verification/`, `experiments/`, `maintenance/` — promoted pre-restructure Python checks/kernels retained because they remain useful and auditable.

## Historical code that remains deliberately visible

- `legacy_verification/` — pre-rebuild verification scripts, including checks later superseded or quarantined.
- `legacy_maintenance/` — pre-rebuild one-off repository/ledger maintenance scripts.

Historical visibility is not theorem certification. Before reusing one of these scripts as evidence, reconstruct what it computes, update stale paths/APIs, and compare it against the current mathematical object.

## Julia migration

No `.jl` file should live in this active `code/` tree. The original Julia sources exist once under `../archive/legacy-workspace/` and Git history. Every historical Julia path is accounted for in `../research/engineering/language_migration.md` and maps to a supported Python/C++ replacement, a consolidated component, or an explicit falsified/retracted status.

This avoids both failure modes: hiding the multi-year codebase in an archive, and keeping obsolete Julia copies next to their replacements.
