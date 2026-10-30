# Absolute scratch paths in the Line I packet (whitelist)

The files below contain absolute paths of the machine on which the Line I computations, certificates and the referee audit were run
(argv and code paths inside `provenance` blocks, `sys.path` lines of reused code, logs and notes). They are records of the actual runs
and are byte-identical to the sha256 values in [`receipt.json`](../../../evidence/executions/20261031/lineI/receipt.json), so they are
whitelisted rather than edited: editing them would break the sha256 chain. The DF2 reruns (`cert_v3/`, `sym_v3/`) use paths relative
to the script. Reproduction commands in [README.md](README.md) use repository paths; scripts that still hard-code a scratch path
need the mapping below.

Scratch prefix → repository location:

* `/workspace/bgs-lineI/cert_v2` → `computations/verification/lineI/cert_v2`
* `/workspace/bgs-derand/phase3` → the Python virtual environment of the runs (`venv/bin/python`: python-flint 0.9.0, numpy, scipy with OpenBLAS); not in the repository
* `/workspace/bgs-lineI/dom_v3` → `computations/verification/lineI/dom_v3`
* `/workspace/bgs-lineI/cert2` → `computations/verification/lineI/cert2`
* `/workspace/bgs-lineI/code` → `computations/verification/lineI/code`
* `/workspace/bgs-lineI/cert` → `computations/verification/lineI/cert`
* `/workspace/bgs-lineI/lean` → `computations/verification/lineI/lean`
* `/workspace/bgs-lineH/code` → `computations/verification/lineH/code`
* `/workspace/bgs-lineG/logs` → `computations/verification/lineG/logs`
* `/workspace/bgs-lineF/code` → `computations/verification/lineF/code`
* `/workspace/bgs-next/lineE` → `computations/verification/lineE`
* `/workspace/bgs-lineI/dom` → `computations/verification/lineI/dom`
* `/workspace/audit/lineI` → `computations/verification/lineI/referee`
* `/workspace/audit/lineH` → `computations/verification/lineH/referee`
* `/workspace/audit/lineE` → computations/verification/lineE/referee (Line E audit scratch, referenced by reused Line E/F code)
* `/workspace/bgs-int/BGS` → (repository root, an earlier integration clone)
* `/workspace/bgs-lineI` → computations/verification/lineI (AUTHOR_*.md = scratch REPORT*.md / NOTES.md)
* `/workspace/audit` → (referee scratch root)

| file | absolute path roots |
|---|---|
| `AUTHOR_NOTES.md` | `/workspace/audit`, `/workspace/audit/lineI`, `/workspace/bgs-derand/phase3` |
| `AUTHOR_REPORT_session4.md` | `/workspace/audit/lineI` |
| `AUTHOR_REPORT_v1.md` | `/workspace/bgs-derand/phase3`, `/workspace/bgs-int/BGS`, `/workspace/bgs-lineI`, `/workspace/bgs-lineI/lean` |
| `AUTHOR_REPORT_v2.md` | `/workspace/audit/lineI`, `/workspace/bgs-derand/phase3`, `/workspace/bgs-int/BGS`, `/workspace/bgs-lineI`, `/workspace/bgs-lineI/lean` |
| `cert/cert49_build_orig.py` | `/workspace/bgs-lineH/code`, `/workspace/bgs-next/lineE` |
| `cert/gstates.py` | `/workspace/bgs-lineI/code` |
| `cert/logs/E_0_1_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/E_0_2_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/E_0_3_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/E_1_0_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/E_1_2_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/E_1_3_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/E_1_5_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/E_2_1_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/V_0_1_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/V_0_2_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/V_0_3_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/V_1_0_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/V_1_2_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/V_1_3_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/V_1_5_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/logs/V_2_1_rest.json` | `/workspace/bgs-lineI/cert` |
| `cert/rig_spec.py` | `/workspace/audit/lineH` |
| `cert/run_sq.sh` | `/workspace/bgs-derand/phase3`, `/workspace/bgs-lineI/cert` |
| `cert2/gstates.py` | `/workspace/bgs-lineI/code` |
| `cert2/logs/E15m_1_3_rest.json` | `/workspace/bgs-lineI/cert2` |
| `cert2/logs/V15m_1_3_rest.json` | `/workspace/bgs-lineI/cert2` |
| `cert2/rig_spec.py` | `/workspace/audit/lineH` |
| `cert2/run_xcheck.sh` | `/workspace/bgs-derand/phase3`, `/workspace/bgs-lineI/cert2` |
| `cert_v2/bounds_sq_v2.py` | `/workspace/bgs-lineI/cert`, `/workspace/bgs-lineI/cert_v2` |
| `cert_v2/logs/R6_stored_matrices.txt` | `/workspace/audit/lineI` |
| `cert_v2/mk_report_v2.py` | `/workspace/audit/lineI`, `/workspace/bgs-lineI` |
| `code/base.py` | `/workspace/audit/lineE`, `/workspace/bgs-lineG/logs` |
| `code/gstates.py` | `/workspace/bgs-lineI/code` |
| `code/liftchk.py` | `/workspace/bgs-lineF/code` |
| `code/step1b.py` | `/workspace/audit/lineE` |
| `dom/gstates.py` | `/workspace/bgs-lineI/code` |
| `dom/logs/V36_1_3_dom3b.json` | `/workspace/bgs-lineI/dom` |
| `dom/logs/V36_2_1_dom3b.json` | `/workspace/bgs-lineI/dom` |
| `dom/logs/pil_dom3.json` | `/workspace/bgs-lineI/dom` |
| `dom/logs/pil_dom3b.json` | `/workspace/bgs-lineI/dom` |
| `dom/run_dom.sh` | `/workspace/bgs-derand/phase3`, `/workspace/bgs-lineI/dom` |
| `dom_v3/gstates.py` | `/workspace/bgs-lineI/code` |
| `dom_v3/logs/V36_1_3_dom3b_v3.json` | `/workspace/bgs-lineI/dom_v3` |
| `dom_v3/logs/V36_2_1_dom3b_v3.json` | `/workspace/bgs-lineI/dom_v3` |
| `dom_v3/run_dom_v3.sh` | `/workspace/bgs-derand/phase3` |
| `logs/zpred_K40.log` | `/workspace/audit/lineE` |
| `logs/zpred_d7_K40_r2.6_L10.json` | `/workspace/audit/lineE` |
| `pre_delta/NOTES.md` | `/workspace/audit`, `/workspace/audit/lineI`, `/workspace/bgs-derand/phase3` |
| `pre_delta/REPORT_session4.md` | `/workspace/audit/lineI` |
| `pre_delta/REPORT_v2.md` | `/workspace/audit/lineI`, `/workspace/bgs-derand/phase3`, `/workspace/bgs-int/BGS`, `/workspace/bgs-lineI`, `/workspace/bgs-lineI/lean` |
| `referee/REPORT.md` | `/workspace/audit/lineI`, `/workspace/bgs-int/BGS`, `/workspace/bgs-lineI`, `/workspace/bgs-lineI/code` |
| `referee/bsq/logs/E_0_1_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/E_0_2_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/E_0_3_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/E_1_0_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/E_1_2_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/E_1_3_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/E_1_5_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/E_2_1_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/V_0_1_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/V_0_2_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/V_0_3_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/V_1_0_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/V_1_2_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/V_1_3_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/V_1_5_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/bsq/logs/V_2_1_rest.json` | `/workspace/bgs-lineI/cert` |
| `referee/cert/cert49_build_orig.py` | `/workspace/bgs-lineH/code`, `/workspace/bgs-next/lineE` |
| `referee/cert/gstates.py` | `/workspace/bgs-lineI/code` |
| `referee/cert/rig_spec.py` | `/workspace/audit/lineH` |
| `referee/cert/run_sq.sh` | `/workspace/bgs-derand/phase3`, `/workspace/bgs-lineI/cert` |
| `referee/delta/code/bounds_sq_v2_copy.py` | `/workspace/audit/lineI`, `/workspace/bgs-lineI/cert` |
| `referee/delta/code/gstates.py` | `/workspace/bgs-lineI/code` |
| `referee/delta/code/monomial_intertw.py` | `/workspace/bgs-lineI/cert` |
| `referee/delta/logs/V36_2_1_dom3b_rerun.json` | `/workspace/audit/lineI` |
| `referee/delta/run.sh` | `/workspace/audit/lineI`, `/workspace/bgs-derand/phase3` |
| `referee/logs/lean.out` | `/workspace/audit/lineI` |
| `sym/intertw.py` | `/workspace/bgs-lineI/cert` |
| `sym/monomial_intertw.py` | `/workspace/bgs-lineI/cert` |
