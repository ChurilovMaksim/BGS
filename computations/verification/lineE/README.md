# Line E verification packet (BGS-TRACE-183 to BGS-TRACE-196)

Canonical note: `mathematics/fixed-map/resonant_residue_lineE.md`. Evidence receipt: `evidence/executions/20261030/lineE-resonant-transfer/receipt.json`.

## Environment (pinned for the committed logs)
- Python 3.13 with python-flint 0.9.0 (arb), numpy 2.5.4, scipy 1.18.1, sympy 1.14.0. These are the Line E pins; they are not the repository runtime pins in `requirements.txt`.
- `step2/zres.c` is built by `step2/build_zres.sh` (`gcc -O3 -march=native -ffp-contract=off -fno-fast-math -fopenmp`). The source also carries `#pragma GCC optimize("fp-contract=off")`, and the script refuses a binary whose disassembly contains FMA instructions (second referee, N4).
  - The rounding analysis assumes IEEE binary64 without FMA contraction, and x86-64 80-bit `long double` (u_L = 2^-64).
- numpy is used only to precondition (approximate eigenvectors) in `code/cert.py`. b11 may differ between runs (1e-88 in the first referee's rerun; up to 1.3e-61 in the 2026-10-30 regeneration). The certified enclosures do not depend on it.

## Layout

| path | content | claims |
|---|---|---|
| `code/` | Author code. `pell.py` and `resid.py` (exact E1 check, m ≤ 41); `ifs_explore.py` (Galerkin builder); `trace_check.py` (E2 vs brute force); `cert.py` (arb certificates, cache keyed by sector, referee fix F9); `bounds.py` (E4/E5 bounds, explicit Bessel tail, F9); `run_certs.sh` (regenerates all nine certificates); `tm2.py`. | 183–187, 189 |
| `logs/` | The nine certificates `cert_*.json` with their `.out` and `_bounds.json` / `_bounds.out`, regenerated with the fixed code on 2026-10-30. `cert_L6.json` is the η = 2, L = 6 certificate (r₁ = 1e-6). | 185–187 |
| `review/` | Author-side independent checks. `indep_trace.py` and `indep_trace_full.py` (matrix-free physical traces; vendored, F7); `predict_finiteN.py` (E2 finite-N law with ρ > L/(λ−1) asserted, F8) and its log; `indep_trace.jsonl`; Line B `fast_classes` replay at m = 13. | 184, 190 |
| `referee/` | The independent referee audit: `REPORT.md`, `NOTES.md`, `code/`, `logs/` (class-sum tables `T_*.npy` for m ≤ 13; m = 15 omitted for size, regenerate with `referee/code/run_classes.py`), `certrun/` (rerun, no-cache variant, negative controls), `lean/`. | 183–192 |
| `step2/` | Audited by the second referee (`referee2/`). `lawlib.py`, `tm49.py` (a²-resonance law, 49-state Galerkin); `check_phase.py`, `check_trace.py`, `cert49_py.py`, `check_finiteN.py`, `cmp_full.py` (checks of E12); `check_propG.py`, `cert_class.py` + `zres.c` + `build_zres.sh` (Prop. G and the rigorous Line B kick bounds, E13; `cert_class.jsonl` records the residues ±196 and ±4); `check_f7.py` (E11); `spec_full.py`, `predict.py` (E14 evidence and the m = 17 prediction). | 193–196 |
| `referee2/` | The second independent referee audit (of PR #57; E11–E14 and a recheck of E1–E10): `REPORT.md`, `NOTES.md`, `code/` (`e12_phase.py`, `e12_trace.py`, `propG_nsum.py`, and the directed-rounding interval kernel `ivsum.c` + `ivcert.py`), `logs/`, `lean/` (extra false controls). Absolute scratch paths are replaced by placeholders. Build: `gcc -O2 -fopenmp -frounding-math -fno-fast-math -ffp-contract=off -o ivsum ivsum.c -lm`, then `python ivcert.py full 11 2.0 196,-196,4,-4 8`. | 193–196 |

## Reproduce

```
PY=python3   # with the pins above
bash code/run_certs.sh                                    # E3-E5: nine certificates + bounds (about 15 min single-core)
$PY code/resid.py; $PY code/trace_check.py               # E1, E2
$PY review/predict_finiteN.py 11; $PY review/indep_trace.py 11 2.0 512
cd step2 && bash build_zres.sh
$PY check_phase.py; $PY check_trace.py; $PY cert49_py.py; $PY check_propG.py; $PY check_f7.py; $PY check_finiteN.py
$PY cert_class.py full 13 2.0 196,-196,4,-4 8            # E13 at m = 13 (seconds); m = 11 likewise; m = 17 takes several hours
```

Lean: `cd formalization && lake exe cache get && lake build Bgs`. This covers `Bgs.LineE` and `Bgs.LineEResonance`.
