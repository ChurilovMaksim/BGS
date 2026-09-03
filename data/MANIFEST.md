# Data / result corpus manifest

`data/` is the broad research corpus. It is intentionally much larger than `results/verified/` because intermediate, negative and historically misinterpreted outputs are part of the research record.

**Important:** the directory name `data/proof/` is historical. A file being present there does **not** mean the corresponding statement is currently proved. Current claim status is governed by `STATUS.md`; audited current outputs live in `results/verified/`.

## Directory roles

| Directory | Role | Trust level |
|---|---|---|
| `diagnostics/` | diagnostic scans, logs, falsifiers, calibrations and intermediate numerical outputs | research corpus |
| `legacy/` | preserved theorem/run inputs and earlier artifact layout used by historical scripts | reference / provenance |
| `moments/` | fourth/fifth moment calculations, design sweeps and surface-term outputs | research corpus |
| `proof/` | historical proof-oriented numerical outputs | mixed; inspect status before use |
| `rank2_sp4/` | rank-2 / Sp4 computational results and calibrations | experimental research corpus |
| `spectral/` | spectral-law, toy-model and convergence outputs | numerical research corpus |
| `LEGACY_MANIFEST.md` | original pre-rebuild manifest with old vocabulary | historical only |

Historical Julia copies that used to appear in `data/legacy/` are intentionally absent from the active tree. They were byte-identical duplicates of code-side Julia sources; the unique historical sources remain in `archive/legacy-workspace/`, and their disposition is recorded in `research/engineering/language_migration.md`.

Bundled Tectonic/tool binary trees are also intentionally excluded because they are not scientific results.

## Canonical audited outputs

Prefer current `results/verified/` artifacts over similarly named historical files in `data/proof/`. Current numerical evidence belongs under `results/numerical/`, while falsifiers/diagnostics belong under `results/diagnostics/`.

## Explicit quarantine / supersession notes

- `data/proof/word_trace_proof.json` is **not** a proof certificate. The corresponding engine failed on an unresolved `('V','V')` word during audit.
- `data/proof/bgs_spacing_N95419.json` is historical only: the producing driver formed consecutive-gap ratio statistics and compared them with the ordinary GOE spacing CDF, so the named KS verdict does not test the statistic claimed by the filename.
- Historical M1-related outputs are finite-N evidence only. The current M1 theorem-draft line is documented in `research/problems/m1_fluctuation_energy.md`, `research/notes/` and `STATUS.md`; numerical files do not substitute for its proof audit.
- number-variance, spacing and spectral-convergence outputs are numerical evidence unless explicitly promoted elsewhere.
- historical proof-era filenames are retained for provenance even when their interpretation was later retracted.

## Preservation rule

Do not delete a data file merely because a later interpretation changed. Preserve raw scientific outputs and record the correction in this manifest, `STATUS.md`, or the research ledger. When a historical result is rerun with current code, write the new result under `results/verified/`, `results/diagnostics/` or `results/numerical/` rather than silently overwriting the old record.
