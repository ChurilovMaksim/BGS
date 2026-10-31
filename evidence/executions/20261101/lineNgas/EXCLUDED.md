# Files and directories not committed (Lines N5–N19b integration)

Files larger than 5 MiB are not committed and are listed here with sha256. The directories `.lake`, `.venv`, `__pycache__` and `.git`
are regenerable and are listed with their size: the referee Lean project `lineN12/referee/lean/proj/.lake` (Mathlib build) and the
Python byte caches. The sources stay at /workspace/bgs-lineN and /workspace/audit on the integration box.

## Files > 5 MiB

| path | bytes | sha256 |
|---|---|---|
| `computations/verification/lineN12/logs/adapted_norm_t0.0_k0.45.npz` | 15699622 | `a4b36f30c1e75ffce8435c15190f2eebbe5faca49371b5af71e46987e3c10fe3` |
| `computations/verification/lineN12/logs/a_ops.npz` | 239147580 | `c7f741182b9b92da8d887be32dacc32fabadc12021e1579ed2d2e5c72b962550` |
| `computations/verification/lineN12b/logs/b_cone_G16_th0.125_cells.npz` | 6721236 | `66fe4c84094828468d51052b33ff1f38cc475d114be89f7fd05f0c5f7ac8c63a` |

## Directories

| path | bytes |
|---|---|
| `computations/verification/lineN5/code/__pycache__` | 7984 |
| `computations/verification/lineN6/code/__pycache__` | 17581 |
| `computations/verification/lineN11/code/__pycache__` | 5207 |
| `computations/verification/lineN12/code/__pycache__` | 5162 |
| `computations/verification/lineN12b/code/__pycache__` | 2721 |
| `computations/verification/lineN14/code/__pycache__` | 28381 |
| `computations/verification/lineN15/code/__pycache__` | 28584 |
| `computations/verification/lineN16/code/__pycache__` | 4517 |
| `computations/verification/lineN11/referee/code/__pycache__` | 8545 |
| `computations/verification/lineN12/referee/lean/proj/.lake` | 7574549315 |
