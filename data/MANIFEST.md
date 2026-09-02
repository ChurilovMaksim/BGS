# Data / result corpus manifest

`data/` is the restored research corpus. It is intentionally broader than `results/verified/`.

**Important:** the directory name `data/proof/` is historical. A file being present there does **not** mean the corresponding statement is currently proved. Current claim status is governed by `STATUS.md`; audited current outputs live in `results/verified/`.

## Directory roles

| Directory | Role | Trust level |
|---|---|---|
| `diagnostics/` | diagnostic scans, logs, falsifiers, calibrations and intermediate numerical outputs | research corpus |
| `legacy/` | preserved theorem/run inputs and earlier artifact layout used by many historical scripts | reference / provenance |
| `moments/` | fourth/fifth moment calculations, design sweeps and surface-term outputs | research corpus |
| `proof/` | historical proof-oriented numerical outputs | mixed; inspect status before use |
| `rank2_sp4/` | rank-2 / Sp4 computational results and calibration scripts | experimental research corpus |
| `spectral/` | spectral-law, toy-model and convergence outputs | numerical research corpus |
| `LEGACY_MANIFEST.md` | original pre-rebuild manifest with old `src/` / `artifacts/` vocabulary | historical only |

The bundled Tectonic/tool binary tree is intentionally not restored here. It is not a scientific result and remains recoverable from the legacy workspace if ever needed.

## Canonical audited outputs

Use these instead of similarly named historical files in `data/proof/`:

- `results/verified/baseline_r82.json`
- `results/verified/h3_k2_exact_reduction.json`
- `results/verified/theorem_ii_new_primes.json`

Current numerical evidence is under `results/numerical/`.

## Explicit quarantine / supersession notes

- `data/proof/word_trace_proof.json` is **not** a proof certificate. The corresponding engine failed on an unresolved `('V','V')` word during audit.
- `data/proof/bgs_spacing_N95419.json` is historical only: the producing driver formed consecutive-gap ratio statistics and compared them with the ordinary GOE spacing CDF, so the named KS test was not testing the stated distribution.
- M1-related historical outputs, including `m1_killer_test.json`, are finite-N evidence only. They do not repair the analytic M1 gap documented in `research/M1.md`.
- `number_variance_goe_control.json`, spacing outputs and spectral convergence files are numerical evidence, not theorem certificates.

## Preservation rule

Do not delete a data file merely because a later interpretation changed. If a result becomes invalid or superseded, preserve the raw output and record the reason in this manifest or `STATUS.md`. When a historical result is rerun with current code, write the new output under `results/verified/` or `results/numerical/` rather than silently overwriting the old record.