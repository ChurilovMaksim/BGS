# BGS research workspace

Research workspace for arithmetic quantum chaos around the Bohigas–Giannoni–Schmit programme, with the quantised cat map as the main rank-1 model and exploratory Sp(4) extensions.

> **Audit notice (2026-09-02).** The repository is undergoing a full reproducibility and proof-status audit on branch `research/audit-r111`. Do not infer `[PROVEN]` status from an old paper title, historical run log, or a compiled PDF. The current audit record is `docs/review/repository_surgery_2026-09-02.md`.

## Current source-of-truth order

1. `docs/review/repository_surgery_2026-09-02.md` — current audit findings and repository-surgery decisions.
2. `THEORY.md` — living mathematical framework, but older sections may contain claims superseded by later runs.
3. `HISTORY.md` — chronological research ledger/history. It currently has a known encoding defect and many legacy path references; treat it as historical evidence, not as a clean API.
4. `HANDBOOK.md` — compact claim/status index, being re-audited.
5. `data/MANIFEST.md` — artifact inventory; paths are also being checked after the `src/` → `code/` and `artifacts/` → `data/` migration.

Historical review snapshots under `docs/review/audits/` and retired material under `docs/archive/` are evidence. They are intentionally not rewritten merely to make old paths look current.

## Repository layout

```text
code/                 executable research code
  core/                quantisation and shared core routines
  theorems/            theorem-oriented implementations
  verification/        rerunnable verification/falsification scripts
  diagnostics/         exploratory and diagnostic programs
  kloosterman/         subgroup/Kloosterman utilities
  large_m/             large-m experiments
  shape_automaton/     shape-language computations
  sp4/                 rank-2 experiments
  maintenance/         repository/reproducibility tooling

data/                 machine-readable artifacts and retained measurements
  proof/               proof-support and rerun outputs
  diagnostics/         diagnostics
  legacy/              historical artifacts retained for provenance
  moments/             moment data
  spectral/            spectral data
  rank2_sp4/           rank-2 data
  tools/bin/           local build utility binary

formal/               Lean 4 project
paper/                TeX sources, historical patch scripts, compiled outputs
docs/                 status, reviews, literature notes, archive
```

## Audit status of central claims

The following table reports **this audit's status**, not the most optimistic historical label.

| Claim / component | Current audit status |
|---|---|
| R82 twisted-Jacobi baseline at N=199 and N=3571 | **[NUMERICALLY-SUPPORTED / rerun PASS]**; max reproduced deviation `2.353672812205332e-13` |
| H3 k=2 exact reduction and `|P|=(K-1)(K-2)` | **[PROVEN identity + rerun PASS]** at the audited designs; Lean source also exists and still needs an executable Lean environment for this audit |
| Python source syntax after current Git fixes | **PASS**, 164/164 audited Python files compile under Python 3.13.5 |
| `word_trace_algebra.py` as a verification certificate | **FAIL / quarantine candidate**; rewrite engine leaves `('V','V')` unresolved |
| M1 / standalone Möbius-fiber `δ=o(1)` theorem | **[OPEN GAP]**; the current standalone proof has an invalid fixed-K asymptotic, missing cross-twist justification, inconsistent Fourier normalization, and its own K=17 measurement exceeds the displayed envelope |
| GOE spacing / rigidity experiments | historical numerical evidence exists; **rerun pending** after migration-path repair |
| Sp(4) diagonal identities / rank-2 numerics | historical evidence exists; **full re-audit pending** |
| General BGS | **not proved** |

The M1 downgrade does **not** retract the exact k=2 combinatorics, the existence of the character/twist reductions, or unrelated independently verified identities. It removes only the unsupported promotion of the full asymptotic M1 claim to `[PROVEN]`.

## Fast health gate

Run this before any research edit:

```bash
python code/maintenance/repo_health.py
```

It checks the current repository layout, rejects regenerated Lean build trees, and compiles the Python layer. It is structural, not a scientific proof checker.

## Audited verification commands

The first two commands below have been repaired for the post-R82 directory layout and rerun successfully in the current audit environment:

```bash
python code/verification/baseline_r82.py
python code/verification/h3_k2_exact_reduction.py
```

Other verification scripts are being migrated one by one. A script living in `code/verification/` is **not automatically a certificate** until it has been rerun successfully after the migration audit.

Lean sources are under `formal/Bgs/`. The current audit environment does not have Lean installed, so no fresh `lake build` is claimed in this pass.

## Papers

`paper/final/` contains presentation copies, but several files are byte-for-byte duplicates of older names in `paper/`. Those duplicates are being consolidated only after all patch-script references are migrated. Compiled PDFs are snapshots of historical claim states, not authority over the current audit status.

In particular, `paper/final/mobius_fiber_theorem.{tex,pdf}` is retained as an important failed/unfinished proof attempt, not as a definitive proof, until M1 is rederived.

## Archive comparison

The user-provided pre-Git ZIP contains 1100 files. Exactly 70 are excluded by its own `.gitignore` (48 Lean build outputs and 22 `.out` logs), leaving 1030 expected source/artifact files. Comparison with the first complete Git import and subsequent commits found no evidence of a post-import project-file deletion. The main pre-existing defects are migration drift, duplication, stale paths, and the corrupted/renamed ledger history.

## Working discipline

New work should follow three rules:

- never promote numerical evidence to proof;
- every load-bearing result must point to a rerunnable script/artifact or a gap-free derivation;
- historical files are preserved for provenance, while current documentation must state the present audited status.

The immediate research priority after repository repair is to rederive M1 from the exact twist expansion with all cross terms and normalizations explicit. Only after that should the M3/M4 programme be used as a dependency chain.
