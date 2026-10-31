# Absolute scratch paths in the Line J packet (whitelist)

The files below contain absolute paths of the machine on which the Line J computations, certificates and the referee audit were run.
They appear in argv and code paths inside `provenance` blocks, in `sys.path` lines of reused code, and in logs and notes. They are
records of the actual runs and are covered by the sha256 manifests (`logs/SHA256_*.txt`, `J3/SHA256_J3*.txt`,
`referee/rerun/SHA256_referee.txt`) and by [`receipt.json`](../../../evidence/executions/20261031/lineJ/receipt.json). They are
therefore whitelisted rather than edited, since editing them would break the sha256 chain.

Scratch prefix → repository location:

* `/workspace/bgs-lineJ/J3` → `computations/verification/lineJ/J3`
* `/workspace/bgs-lineJ/logs` → `computations/verification/lineJ/logs`
* `/workspace/bgs-lineJ/code` → `computations/verification/lineJ/code`
* `/workspace/bgs-lineJ/data` → `computations/verification/lineJ/data` (bounds JSON only; `.npy` matrices not included)
* `/workspace/bgs-lineJ` → `computations/verification/lineJ` (`AUTHOR_*.md` = scratch `REPORT.md`, `STRATEGY.md`, `NOTES.md`)
* `/workspace/audit/lineJ` → `computations/verification/lineJ/referee`
* `/workspace/audit/pr60` → an owner-audit checkout of PR #60. The only file used is
  `computations/verification/lineF/logs/certV_eta2_a4_tight.json`, sha256 c77348b6…2795db1, which is identical to the repository
  file.
* `/workspace/bgs-lineI/dom_v3` → `computations/verification/lineI/dom_v3`
* `/workspace/bgs-lineI/code` → `computations/verification/lineI/code`
* `/workspace/bgs-lineI/data` → Line I float scratch arrays (`zpred_*.npy`, `base_*.npz`). These are not in the repository; they are
  used only by the float diagnostics `check_model.py`, `check_z0.py`, `model_lead.py` and `model_cross.py`.
* `/workspace/bgs-lineI` → `computations/verification/lineI`
* `/workspace/audit/lineI` → `computations/verification/lineI/referee`
* `/workspace/audit/lineH` → `computations/verification/lineH/referee`
* `/workspace/bgs-derand/phase3` → the Python virtual environment of the runs (`venv/bin/python`: python-flint 0.9.0, numpy, scipy
  with OpenBLAS); not in the repository.
