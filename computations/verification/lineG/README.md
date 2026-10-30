# Line G verification packet (BGS-TRACE-203 to BGS-TRACE-206)

Canonical note: `mathematics/fixed-map/resonance_classification_lineG.md`. Manuscript: `manuscript/unified_sections/lifted_transfer_lineFG.tex`. Evidence receipt: `evidence/executions/20261030/lineFG-lifted-transfer/receipt.json`. Referee audit: `computations/verification/lineFG/referee/REPORT.md` (Part G).

## Pre-registration (BGS-TRACE-206)
`PREDICTIONS_m17.json`, sha256 `fa8505f503790ae2c6265f917debdd4b023b2c50b79412daac7d14f72b8aa344` (`PREDICTIONS_m17.sha256`; `sha256sum -c PREDICTIONS_m17.sha256`). The referee verified the hash before any m = 17 output existed; this commit is its first external record. The evaluator is `code/eval17.py`; W′_17 under the frozen definition is computed by `code/formula_table.py k1 17`. No m = 17 outcome is included in this packet.

## Environment and omissions
- Python 3.13 (numpy, scipy, sympy as for Line F); C class-sum kernels `code/classes_orb.c`, `classes_orb2.c`, `classes_sym.c` (`gcc -O3 -fopenmp`; binaries not committed).
- The class-sum tables `*.bin` (tens of MB) are not committed; their sha256 values are in `logs/bin_sha256.txt`; regenerate with `code/run_orb.py`, `run_orb2.py`, `run_classes_sym.py`.
- Absolute scratch paths are replaced by repository-relative paths or placeholders.

## Layout

| path | content | claims |
|---|---|---|
| `code/law.py`, `check_law.py`, `tune.py`, `law_vs_class.py`, `growth_law.py` | the G2 partial-trace law (Galerkin) and its checks against brute force and class sums. | 203, 205 |
| `code/check_dilution.py`, `dil_stats.py` | G3 checks at prime d (numerical). | 204 |
| `code/step1*.py`, `tier2*.py`, `probe.py`, `eta_scan.py` | outlier classification, second tier, η-scan. | 205 |
| `code/formula_table.py` | the frozen R′ quantities (RMT_m, Res_m, W′_m "pred" and "act"). | 206 |
| `code/predict17_law*.py`, `eval17.py`, `watch17.sh` | m = 17 prediction and evaluator. | 206 |
| `logs/` | outputs of the above; `lean_LineG.out` (author's Lean run, superseded by the evidence build). | 203–206 |
| `AUTHOR_REPORT.md`, `AUTHOR_NOTES.md` | the author's report and notes as submitted (the R′ definition and the §3 claim there are superseded by the canonical note). | — |

Lean: `cd formalization && lake exe cache get && lake build Bgs` (covers `Bgs.LineG`).
