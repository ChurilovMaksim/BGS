# Repository rebuild completeness correction — v2

Date: 2026-09-02

## Why this correction exists

The first canonical rebuild correctly separated audited claims from historical overclaims, but it compressed the active workspace too aggressively. Although the complete pre-rebuild tree remained recoverable under `archive/legacy-workspace/`, too many useful experiments, intermediate outputs, theorem scripts, literature notes and rank-2/Sp4 results were no longer visible in ordinary working paths.

That is the wrong trade-off for a live research repository. The corrected policy is **preserve broadly, trust narrowly**.

## What was restored to ordinary working paths

Research code:

- `code/core/`
- `code/diagnostics/`
- `code/kloosterman/`
- `code/large_m/`
- `code/llm/`
- `code/shape_automaton/`
- `code/sp4/`
- `code/theorems/`
- `code/utils/`
- old verification and maintenance scripts under explicitly historical `code/legacy_verification/` and `code/legacy_maintenance/`

Research outputs/reference data:

- `data/diagnostics/`
- `data/legacy/`
- `data/moments/`
- `data/proof/`
- `data/rank2_sp4/`
- `data/spectral/`

Documentation:

- literature corpus;
- review/red-team/referee corpus;
- old run archive;
- major standalone research notes;
- full pre-rebuild theory notebook;
- full pre-rebuild research ledger.

Paper material:

- `paper/sections/`
- `paper/patches/`
- `paper/final/`
- root historical paper snapshots consolidated under `paper/historical_snapshots/`

## What remains intentionally excluded

- `formal/.lake/build/` and `.lake/packages/` generated material;
- bundled `data/tools/` binary/tool tree;
- duplicate root `tools/tectonic.exe`;
- Python `__pycache__` / `.pyc` files;
- other generated outputs excluded by `.gitignore`.

These exclusions are build/tool hygiene, not scientific-data deletion.

## Validation

A local mirror of the corrected layout was checked after cache removal:

- 168 Python source files under `code/`: **0 compile errors**;
- 255 JSON files under `data/` + `results/`: **0 parse errors**;
- approximately 1062 active/research files outside the full legacy-workspace snapshot;
- generated Lean build/dependency directories absent;
- duplicate tool binary absent.

The current `code/maintenance/repo_health.py` deliberately applies strict path conventions only to the canonical code layer, while requiring the broader corpus to remain present and syntactically intact.

## Trust policy

The restored files are not all promoted to theorem status. `STATUS.md` remains authoritative. In particular:

- M1 remains **OPEN GAP**;
- `data/proof/word_trace_proof.json` is quarantined;
- the historical `N=95419` spacing test is quarantined because it compared a gap-ratio statistic with the ordinary spacing CDF;
- historical `mobius_fiber_theorem` / `M4D_PROOF` remains a failed proof attempt, not an active theorem.

The point of this correction is to preserve the experimental and mathematical trail needed for future work without restoring old overclaims.