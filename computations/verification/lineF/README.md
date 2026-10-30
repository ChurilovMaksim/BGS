# Line F verification packet (BGS-TRACE-197 to BGS-TRACE-202)

Canonical note: `mathematics/fixed-map/lifted_transfer_lineF.md`. Manuscript: `manuscript/unified_sections/lifted_transfer_lineFG.tex`. Evidence receipt: `evidence/executions/20261030/lineFG-lifted-transfer/receipt.json`. Referee audit (Lines F and G): `computations/verification/lineFG/referee/REPORT.md`.

## Environment
- Python 3.13 with python-flint 0.9.0 (arb, 128-bit working precision), numpy 2.5.4, scipy 1.18.1, sympy 1.14.0 (the Line E pins; not the repository runtime pins in `requirements.txt`).
- numpy is used only for preconditioning (approximate eigenvectors) and float diagnostics; certified enclosures are arb.
- Absolute scratch paths in scripts and logs are replaced by repository-relative paths or placeholders (`<backup-dir>`, `<integration-clone>`, `<venv>`). Run scripts from the repository root unless stated otherwise; `lift49.py` and `xcheck_class.py` import `computations/verification/lineE/step2` and the Line E referee class tables (`computations/verification/lineE/referee/logs/T_*.npy`).

## Layout

| path | content | claims |
|---|---|---|
| `code/lift.py` | vertex/edge lifted operators (Galerkin builders). | 197 |
| `code/cert_lift.py` | arb certificate per lattice, sector and η (`certV_eta*_a*.json`, `certE_eta*.json`). | 198, 201 |
| `code/bounds_lift.py` | Lidskii/Weyl chain to F_m/2m and W̃rest_m/m lower bounds and the closed form; integration fix: closed-form assertions and a 2048-bit check of 2(h−1) < λ^{m/2} (referee nit F.7). | 199–201 |
| `code/safe_table.py` | safe-direction rounding of every quoted number (lower bounds down, upper bounds up, enclosures outward) → `logs/safe_table.md`. Added at integration (referee fix F.6). | 198–201 |
| `code/spec_float.py`, `eta_curve.py`, `eta_thresh.py`, `grid_table.py` | float spectra and the η-window (not certified). | 202 |
| `code/lift49.py`, `xcheck_class.py` | f_B 49-state lift (float), and cross-checks against Line E class sums. | 202 |
| `code/run1.sh`, `run2.sh`, `after.sh`, `run_neg.sh` | batch drivers; `run_neg.sh` runs negative controls (`neg_*`). | — |
| `logs/` | certificates and bounds for η ∈ {1.25, 1.5, 1.75, 2, 2.25, 2.5}; `certV_eta2_a4_tight` (tight μ* enclosure); negative controls; `safe_table.md`; `lean_LineF.out` (author's Lean run, superseded by the evidence build). η = 2.5 (sector 6 by the reflection lemma, plus its own E certificate) was completed after the referee audit. | 197–202 |
| `AUTHOR_REPORT.md`, `AUTHOR_NOTES.md` | the author's report and notes, as submitted to the referee (numbers there are superseded by the safe-rounded values in the canonical note). | — |

## Reproduce

```
PY=python3   # with the pins above
$PY computations/verification/lineF/code/cert_lift.py ...   # see run1.sh / run2.sh for the exact argument lists (5-30 min per operator under load)
$PY computations/verification/lineF/code/bounds_lift.py <eta> <certV_a4> <certV_a0> <certV_a2> <certV_a6> <certE> <out.json>   # per eta (argument order: code/bounds_lift.py line 8)
$PY computations/verification/lineF/code/safe_table.py
```

Lean: `cd formalization && lake exe cache get && lake build Bgs` (covers `Bgs.LineF`).
