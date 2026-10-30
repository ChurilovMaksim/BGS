# Line I verification packet: reduction of Conjecture R′ (BGS-TRACE-206) and the d = 7 twisted certificates

These files support claims BGS-TRACE-211..220. The mathematics is in
[`mathematics/fixed-map/lineI_rprime_reduction.md`](../../../mathematics/fixed-map/lineI_rprime_reduction.md). The referee
report is [`referee/REPORT.md`](referee/REPORT.md): ACCEPT AFTER FIXES. Rounds B1–B9 and R1–R7, plus the delta fixes DF1–DF7 (DELTA
section), are applied. BGS-TRACE-206 stays open. R′_A (BGS-TRACE-220) is an open conjecture with heuristic evidence only.

## Layout
* `AUTHOR_REPORT_v1.md`, `AUTHOR_REPORT_v2.md`, `AUTHOR_REPORT_session4.md`, `AUTHOR_NOTES.md`, `theory_E2*.md`, `theory_session4.md`:
  the author's reports and notes. `REPORT_v2.md`, `REPORT_session4.md`, `theory_session4.md` and `NOTES.md` carry the DF1–DF7 edits.
  Their pre-fix copies are in `pre_delta/` with `SHA256_pre_delta.txt`.
* `code/`: float exploration and checks (`base.py`: W′/W′_act tables; `verify_coset.py`: I2 numerics; `zpred.py`, `dilpred.py`,
  `twist.py`: twisted-trace closure; `halo*.py`, `strat.py`, `shape.py`: heuristic R′_A evidence). **None of these is a certificate.**
* `cert/`: Theorem I6 (BGS-TRACE-215), m = 9, ρ = (2,8). It contains `certG_build.py` (arb bounds and Galerkin matrices of the lifted
  twisted G2 operators), `rig_spec.py` (Line H rig_spec v4, unchanged), `run_sq.sh` and the 16 rest certificates `logs/{V,E}_*_rest.json`.
  `data/*.json` holds the bounds only; the `.npy` matrices are not included (regenerate them with `run_sq.sh`).
  `bounds_sq.py` / `logs/bounds_sq.*` are the v1 all-m table, **superseded by `cert_v3/`** (via `cert_v2/`).
* `cert_v2/bounds_sq_v2.py`: the outward-rounded all-m chain (R1 tail m ≥ 1425); **superseded by `cert_v3/`**. `cert_v3/bounds_sq_v3.py`
  (the verifier of record) is the DF2 rerun with script-relative paths. Its log is byte-identical to the v2 log, and its JSON differs only in `version`/`code_sha256`.
* `cert2/`: the direct cross-check certificate of a transferred case (m = 15, a = −2, class 1:3). It reproduces the m = 9 values
  F = 0.356981 (V, R = 1.45) and 0.013833 (E, R = 1.0).
* `sym/monomial_intertw.py`: the exact monomial intertwiners (BGS-TRACE-216), in integer arithmetic mod 8; **superseded by `sym_v3/`**. `sym_v3/` (of record) is the DF2
  rerun with script-relative paths; its JSON is identical except `code_sha256`.
* `dom/`: Theorem I9 (BGS-TRACE-217). `rig_dom3b.py` v2 (**superseded by `dom_v3/`**) is the counting certificate (k = 3 Householder deflation, resolvent grid with
  covering, homotopy), with `run_dom.sh` and `logs/V36_*_dom3b.json`. `dom_v3/` is the **DF4** rerun of `rig_dom3b.py` v3, where
  gmax is taken over the exact upper ends `g.upper()`. It ran on the unchanged D = 8064 matrices (input sha256 in
  `dom_v3/logs/SHA256_inputs.txt`, equal to the v2 provenance), with `nice -n 10`. All of R = 1.22, 1.24, 1.25, 1.262 are certified
  with count 3 for both classes:
  * F(1.262) = 0.6842758739 for class 1:3 (unchanged);
  * F(1.262) = 0.6489779088 for class 2:1 (v2: 0.6488989; this equals the referee's rerun).
  The v3 certificates of record are `dom_v3/logs/V36_{1_3,2_1}_dom3b_v3.json`, with sha256 in `dom_v3/logs/SHA256_dom_v3.txt`.
* `lean/`: the author's Lean files, kept for the record. `LineI.lean` (v1) is superseded by `LineI_v2.lean`. The integrated modules are `formalization/Bgs/LineI.lean` (from
  `LineI_v2.lean`, namespace `Bgs.LineI`) and `formalization/Bgs/LineIArith.lean` (new at integration: ε = +1, 7 | h_m ⇔ m ≡ 3 mod 6,
  U_2m = 2h_m U_m, and the finite-prime-set deduction with the primitive-divisor theorem as a hypothesis).
* `integration_checks/`: independent float re-implementations written at integration, directly from the definitions (not from
  author code). They cover I1, I2/I2′, I4, I5′, the aliasing identity and the prime-support facts at m = 5, 7, 9, and composite
  d = 287 (m = 15) and d = 49 (m = 21). `lineI_G3_form_check.py` (owner audit) checks the completing-the-square identity
  G_t(β) = e(t̄·Nm β/d)·G_d(t) and the BGS-TRACE-204 G3 formula against brute force for 19 (m, d) pairs, including composite
  d = 217, 287, 961, 1271, 49, 1673 (max error 8.4e−15). All three logs end `ALL_OK`.
* `referee/`: the referee's independent code (`code/`, `delta/code/`), logs and outputs. This includes `own_rig.py` (an independent
  REST certificate for class 1:3), `brute.py` (brute force from the definitions), `galcheck*.py` (intertwiner Galerkin check) and
  the DF4 rerun.

## Reproduction (repository root; Python with python-flint 0.9.0, numpy, scipy/OpenBLAS)
```
nice -n 10 python3 computations/verification/lineI/integration_checks/lineI_identity_checks.py
nice -n 10 python3 computations/verification/lineI/integration_checks/lineI_composite_d_check.py
nice -n 10 python3 computations/verification/lineI/integration_checks/lineI_G3_form_check.py
nice -n 10 python3 computations/verification/lineI/sym_v3/monomial_intertw.py
nice -n 10 python3 computations/verification/lineI/cert_v3/bounds_sq_v3.py
```
The certificate runs (`cert/run_sq.sh`, `cert2/run_xcheck.sh`, `dom/run_dom.sh`, `dom_v3/run_dom_v3.sh`) regenerate the Galerkin
matrices (0.1–1 GB each) and take hours. They hard-code the scratch interpreter path; see [PROVENANCE_PATHS.md](PROVENANCE_PATHS.md).

## Scope
* Theorem I6 controls only the **square** part of the d = 7 dilation remainder, and only for ρ = (±2,8). The (±2,16) level-7
  members are not controlled. The value 0.004574 at m = 321 uses the exact constants; the rounded displayed constants give 0.004575.
  The prime-sum constant is Rosser–Schoenfeld 1962 Theorem 15 (EXT-RS-1962).
* Theorem I9 certifies 1.262 < |μ| < 1.45. The value 1.28371 is a float diagnostic. The nonvanishing of the leading coefficient
  c(β) is **not** certified.
* μ₀ := liminf |Z_m(ν*)|^(1/m), the growth rate of the resonant sum. BGS-TRACE-199 gives |Z_m(ν*)| ≥ ½(1−λ^(−m))(1.9154712^m − 3012.30)
  for odd m ≥ 13, so μ₀ ≥ 1.9154712 and √λ/μ₀ ≤ 1.260376.
* Nothing here proves or disproves R′ (BGS-TRACE-206), R (BGS-TRACE-179) or BGS.
