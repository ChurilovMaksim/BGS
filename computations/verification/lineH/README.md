# Line H verification packet: 49-state certificate for the Line B kick f_B (η = 2, s = −1)

These files support claims BGS-TRACE-207..209. The mathematics is in `mathematics/fixed-map/lineH_49state_certificate.md`, and the
referee report is `referee/REPORT.md` (ACCEPT AFTER FIXES; fixes applied).

## Layout
* `code/`: byte-identical copies of the archived code. The run hashes are in `logs/SHA256_code_v4_runs.txt`, and each certificate
  JSON also carries a `provenance` block with sha256 values.
  * `ghat_arb.py`: rigorous ĝ for f_B.
  * `cert49_build.py`: arb bounds δ₁, δ₂, Δ, ‖X‖, the trace norm, and the Galerkin mid/rad matrices.
  * `rig_spec.py` (v4): the spectral certificate. It uses the rounding constant √2·γ_{2n+2}, padded inputs and an a-posteriori
    Householder residual.
  * `rig_spec_v3.py`: the earlier version, kept for the record. The pre-fix V_0 run (`logs/prodV_rig0.log`, `prodV_dom0_scan.json`)
    came from an unarchived predecessor of this file and is superseded.
  * `bounds49.py`: the all-m chain.
  * `tracechk.py`: the trace identity against the exact class sums.
  * `kappa_check.py`: the κ lemma, checked exactly.
  * `run_v4.sh`: the run script.
  * `h1_*.py`, `f49.py`: H1 float numerics only; these are not part of any claim.
* `data/`: build JSONs (bounds only). The Galerkin `.npy` matrices (0.1–1.1 GB each) are **not** included; regenerate them with the
  commands below.
* `logs/`:
  * `v4_V0_dom.json`, `v4_V{2,4,6}_rest.json`, `v4_E{0,2,4,6}_rest.json`: the certificates.
  * `bounds49_v4.json`: the all-m chain.
  * `tracechk.log`, `kappa_check.log`, `neg_rest_pilot0.*`: checks and the negative control.
* `referee/`:
  * the referee's independent code: `ref_rig.py`, `ref_bounds.py`, `ref_entries.py`;
  * outputs: `out/refV0.json` (**the V_0 certificate of record**) and `refE0.json`;
  * logs and `CERTIFICATE_OF_RECORD.md`.

## Reproduce (from the repository root; python-flint 0.9.0, numpy with OpenBLAS)
```
export PYTHONPATH=computations/verification/lineE/step2:computations/verification/lineH/code
cd computations/verification/lineH/code
# the scratch sys.path entries inside the scripts are harmless when absent
python cert49_build.py V -1 2 0.85 30 3.5 150 40 0,2,4,6 ../data/prodV 128 24      # ~3-4 min per sector
python cert49_build.py E -1 2 0.85 22 3.5 150 40 0,2,4,6 ../data/prodE 128 18
python rig_spec.py ../data/prodV 0 dom 1.5,1.55,1.6 0.05,0.08,0.1,0.13 32 ../logs/v4_V0_dom.json     # ~40 min at load 20
python rig_spec.py ../data/prodV 4 rest 1.45,1.5,1.55 0 24 ../logs/v4_V4_rest.json                   # likewise b = 2, 6
python rig_spec.py ../data/prodE 0 rest 1.0,1.2 0 20 ../logs/v4_E0_rest.json                         # likewise b = 2, 4, 6
python bounds49.py ../logs/v4_V0_dom.json ../data/prodV.json ../logs/v4_V{2,4,6}_rest.json ../data/prodE.json ../logs/v4_E{0,2,4,6}_rest.json ../logs/bounds49_v4.json
python kappa_check.py
```
In the author's runs, sectors V_2/V_4/V_6 were built under the prefix `prodVr`; its bounds are identical to those in `prodV.json`.
