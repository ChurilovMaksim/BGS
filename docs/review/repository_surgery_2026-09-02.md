# Repository surgery audit — 2026-09-02

Status: **active audit on `research/audit-r111`**. This document records the evidence used before any destructive cleanup. Historical material is not rewritten merely to make the tree look cleaner.

## Sources compared

1. Current GitHub branch lineage, with `main` at `34dd6562172e8fe6774cd52275991b346b6e363e` when this audit started.
2. First complete Git import, `ff19b5d35830ce2435b562167ca432ca1a491c9f`.
3. User-provided pre-Git workspace archive `BGS(1).zip`.

The ZIP contains 1100 files in the project root. Exactly 70 files are excluded by the archive's own `.gitignore`: 48 files under `formal/.lake/build/` and 22 `*.out` review logs. Thus the expected source import contains 1030 non-ignored files. The first Git import explicitly states that the complete workspace was imported while honoring those ignore rules. Comparing that import with the current `main` shows no project-file deletions: later commits only adjust `.gitignore`, README paths, Python docstrings, paper-patch docstrings, and add `.hoplite/settings.json`.

**Conclusion:** there is no evidence of a post-import file-loss event. Missing material must either have been absent before the ZIP snapshot or intentionally excluded as generated output.

## Pre-Git ledger migration defect

The ZIP does not contain a root `LEDGER.md`, despite many live and historical references to it. `HISTORY.md`, however, begins with `# RESEARCH LEDGER — BGS CONJECTURE (single persisted source of truth)` and contains the chronological RUN/RETRACTION material through R110. Therefore the data were not simply deleted: the ledger was effectively renamed to `HISTORY.md` without completing the reference migration.

There is a second defect: only `HISTORY.md` contains systematic mojibake (`вЂ—`, `ОІ`, `ПЂ`, etc.). The corruption is reversible (the text is UTF-8 containing a prior CP1251 mis-decoding), but the repair must be performed as a dedicated provenance-preserving migration rather than silently rewriting historical text.

## Structural duplication

The ZIP contains exact byte-for-byte duplicates, including:

- `tools/tectonic.exe` == `data/tools/bin/tectonic.exe` (50,167,808 bytes each).
- `paper/exact_wd_and_subgroup_moments.{tex,pdf}` == `paper/final/cat_map_bgs_main.{tex,pdf}`.
- `paper/BGS_COMPLETE.{tex,pdf}` == `paper/final/bgs_complete_paper.{tex,pdf}`.
- `paper/BGS_PROOF.{tex,pdf}` == `paper/final/h_coupling_research_note.{tex,pdf}`.
- `paper/M4D_PROOF.{tex,pdf}` == `paper/final/mobius_fiber_theorem.{tex,pdf}`.

Additional duplicates exist between `data/legacy/`, review snapshots, and current diagnostic/proof locations. Those are often intentional provenance snapshots and must not be deduplicated blindly.

## Runtime/reproducibility audit

All 164 Python files in `code/` plus `paper/patches/` compile under Python 3.13.5 after applying the two docstring fixes already present in current Git.

The verification layer is nevertheless broken by the R82 workspace migration. Several scripts still add `src/theorems` and `src/large_m` to `sys.path` and still read/write `artifacts/...`, although the live tree is `code/...` and `data/...`.

A local non-destructive path repair produced the following results:

- `code/verification/baseline_r82.py`: **PASS** at N=199 and N=3571; max absolute fourth-moment deviation `2.353672812205332e-13`.
- `code/verification/h3_k2_exact_reduction.py`: **PASS**; exact identity reproduced and `|P|=(K-1)(K-2)` at N=53 and N=199.
- `code/verification/word_trace_algebra.py`: **FAIL after reaching the mathematics**; the rewrite engine leaves `('V','V')` unresolved and raises `RuntimeError`. This file must not be treated as a green certificate.
- long GOE/rank-2 jobs were not promoted on this pass because they exceed the bounded audit execution window; they remain to be rerun after path repair.

The old `code/maintenance/consistency_audit.py` is itself non-functional after migration: it opens `artifacts/MANIFEST.md` and `ROADMAP.md`, neither of which is the live path. `check_manifest_refs.py` has the same stale `artifacts/MANIFEST.md` assumption.

## Scientific status correction: M1 / Möbius-fiber theorem

The standalone `paper/final/mobius_fiber_theorem.tex` cannot presently support a `[PROVEN] δ=o(1)` status.

Load-bearing defects found in the audit:

1. It states `O(1/K^2)=o(1)` along a scaling with **K fixed and N→∞**. A nonzero bound depending only on fixed K does not tend to zero with N.
2. The numerical table itself reports `|δ|=6.9%` for K=17 against the claimed `16/K^2=5.5%` envelope.
3. The energy decomposition replaces the squared norm of a sum over twist pairs by a sum of per-twist energies without proving the required orthogonality; cross-twist terms are therefore missing.
4. Parseval/Fourier normalizations are used inconsistently in the displayed energy bound.
5. The claim that the rational character product is a perfect K-th power only for the jointly trivial twist requires a separate divisor/character analysis and is not established as written.

Until a new derivation closes these points, the correct status is **[OPEN GAP]** for the asymptotic M1 claim. The exact twist identity / key-table reductions and the independently rerun k=2 result remain separate claims and are not retracted by this finding.

## Surgery policy

The cleanup proceeds in this order:

1. Repair executable verification paths and replace the broken standing consistency checker.
2. Establish one current audit ledger/status document while preserving the historical chronology.
3. Correct README/HANDBOOK/programme-status claims so no `[PROVEN]` label depends on the invalid M1 step.
4. Remove only proven exact duplicates whose canonical copy and references are unambiguous (the duplicate Tectonic binary is the first candidate).
5. Keep historical review snapshots and retracted artifacts immutable unless a separate manifest proves they are redundant.
6. Rerun the cheap verification suite; quarantine scripts that fail mathematically instead of hiding their failures.
7. Only after the repository baseline is reproducible, resume frontier research on M1/M3/M4.

## Current dominant risks

- The repository currently overstates scientific closure in README/HANDBOOK/programme-status relative to the audited proof.
- A large number of historical `src/` / `artifacts/` strings remain. Only runtime/current-document references should be migrated; historical audit transcripts must keep original paths.
- `HISTORY.md` contains reversible encoding corruption and needs a dedicated migration with before/after checksums.
- The existing verification directory mixes true rerunnable certificates with exploratory/incomplete scripts.
