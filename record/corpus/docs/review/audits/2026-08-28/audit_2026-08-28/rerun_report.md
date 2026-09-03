# Independent re-run of the BGS verification suite

**Auditor:** independent re-run, no prior context.
**Date:** 2026-08-28
**Project root:** `C:\Users\churi\Desktop\BGS\BGS_portable_20260827\BGS`
**Environment:** Windows 10.0.26200 x64, Git Bash; `python` = 3.14.0 with
numpy 2.3.5 / scipy 1.16.3 / sympy 1.14.0 / mpmath 1.3.0; 12 cores, 8 GB RAM.
Julia was available but not needed for the requested list.

**Method.** Every command below was actually executed from the project root.
Full stdout/stderr of each run is in `C:\Users\churi\Desktop\BGS\_audit\logs\`.
Wall time was measured around the process with `date +%s%3N`.
Before running anything, all 121 top-level files of `artifacts/`
(`*.json`, `*.log`, `*.txt`, `*.md`) were copied unchanged to
`C:\Users\churi\Desktop\BGS\_audit\pre\`, so the committed values are
preserved for comparison. **No project source file was modified.**

---

## Global finding: stale hard-coded path breaks 7 of the 16 runs

34 of the 52 scripts under `src/` and `review/scripts/` hard-code

```
C:\Users\churi\OneDrive\Desktop\project_1\BGS\{src,artifacts}
```

which **does not exist on this machine** (`C:\Users\churi\OneDrive\Desktop`
contains no `project_1`). Breakdown: 21 of 36 `src/*.py`, 13 of 16
`review/scripts/*`.

Two distinct failure modes:

* **`src/` scripts** — the stale entry is only `sys.path.insert(...)`, and
  Python already puts `src/` on `sys.path[0]` when the script lives there, so
  imports succeed and the mathematics runs to completion. The script then dies
  with `FileNotFoundError` on the final `json.dump(...)`, i.e. **exit code 1
  and no artifact written**, after all numbers have already been printed.
* **`review/scripts/` scripts** — the stale path is the *only* source of
  `src`, so they die at import time and compute nothing.

`review/scripts/audit_independent_suite.py` is the worst case: it calls a
`dump()` helper after *every* sub-check, and the first `dump()` fires after
`v7()`, so as shipped **only V7 runs and V1–V6 never execute at all**.

To find out whether the underlying mathematics still reproduces, each of the
7 affected runs was repeated through an audit-only shim,
`C:\Users\churi\Desktop\BGS\_audit\audit_wrapper.py`, which prepends the real
`src/` to `sys.path` and redirects opens under the stale artifacts directory to
`C:\Users\churi\Desktop\BGS\_audit\redirect\`. The shim touches no project
file. Both results are reported below ("as shipped" and "wrapped").

---

## 1. `python src/verify_mean_law.py`

* exit code **0**, wall **13.7 s**
* script verdict: **PASS** (5/5 configs `OK`)

```
=== RUN 46 exact-mean verification ===
p=101 k=10: MC=0.09573 exact=0.09803 z=-1.47 OK
p=101 k=20: MC=0.78065 exact=0.78424 z=-0.57 OK
p=211 k=15: MC=0.07710 exact=0.07581 z=+0.66 OK
p=211 k=21: MC=0.21127 exact=0.20801 z=+0.87 OK
p=401 k=20: MC=0.04733 exact=0.04975 z=-1.33 OK
```

* artifact `artifacts/run46_exact_mean.json` rewritten **byte-for-byte
  identical** to the committed copy (`cmp` clean).
* MANIFEST claim "ring1_rerun_verify_mean_law.json (5/5 PASS, max |z|=1.47)" —
  confirmed, max |z| = 1.47 at p=101, k=10.
* **No discrepancy.**

## 2. `python src/audit_tail_bound.py`

* exit code **0**, wall **591.8 s** (9 min 52 s)
* the script prints no PASS/FAIL token; it reports ratio statistics.

```
=== RUN 36 audit tight-bound constant ===
configs tested: 196
vs floor+1: min=0.00 med=0.67 max=2.00
vs k^2/p+1: min=0.00 med=0.57 max=1.23
```

* artifact `artifacts/run36_audit.json` rewritten **byte-for-byte identical**.
* The MANIFEST claim is "Tail bound floor(k²/p)+2, 0 violations". Re-checked
  directly against the fresh artifact: **0 of 196 configs violate
  `maxN3 <= floor(k²/p)+2`**; 10 of 196 violate the tighter `floor(k²/p)+1`
  (e.g. p=73, k=8: maxN3=2 vs floor+1=1), which is exactly why the recorded
  constant is `+2`. Claim confirmed.
* **No discrepancy.**

## 3. `python src/char_expansion_cert.py`

* exit code **0**, wall **2.8 s**
* script verdict: **ALL PASS**

```
p=41 k=8: brute=168 lhs=2.783120e+05 Re(rhs)=2.783120e+05 rel_err=2.09e-16
p=41 k=8: brute=8 lhs=9.352000e+03 Re(rhs)=9.352000e+03 rel_err=7.78e-16
p=73 k=9: brute=0 lhs=-6.561000e+03 Re(rhs)=-6.561000e+03 rel_err=4.71e-15
ALL PASS
saved artifacts/char_expansion_cert.json
```

* artifact `artifacts/char_expansion_cert.json` rewritten **byte-for-byte
  identical** (`brute` = 168 / 8 / 0, `rel_err` = 2.0914535094953652e-16 /
  7.780108655029326e-16 / 4.713126026562957e-15, `all_pass: true`).
* **No discrepancy.**

## 4. `python src/verify_perturbation_wd.py`

**As shipped:** exit code **1**, wall **114.6 s** — computes everything, then
crashes writing the artifact.

```
=== RUN 31 multi-prime verification ===
p=2207: n=204, KS_WD=0.0533, KS_Pois=0.2672 [WD]
p=1597: n=138, KS_WD=0.0727, KS_Pois=0.2881 [WD]
p=2161: n=160, KS_WD=0.1004, KS_Pois=0.1706 [WD]
p=3001: n=178, KS_WD=0.1048, KS_Pois=0.1803 [WD]
FileNotFoundError: [Errno 2] No such file or directory:
'C:\\Users\\churi\\OneDrive\\Desktop\\project_1\\BGS\\artifacts\\run31_multiprime.json'
```

**Wrapped:** exit code **0**, wall **82.4 s**, identical console numbers,
artifact written to `_audit/redirect/run31_multiprime.json`.

**DISCREPANCY vs committed `run31_multiprime.json`.** `p`, `n_spacings` and
`clusters` reproduce exactly (204/[69,69,69], 138/[47,47,47],
160/[55,54,54], 178/[61,60,60]). The KS statistics do not:

| p | ks_wd recorded | ks_wd fresh | ks_poiss recorded | ks_poiss fresh |
|---|---|---|---|---|
| 2207 | 0.06648782921120105 | 0.05326512750963547 | 0.27696666383733315 | 0.2671626582660754 |
| 1597 | 0.07268387043990121 | 0.0726839199184921 | 0.28809948322583256 | 0.2880995303996655 |
| 2161 | 0.13426194723953866 | 0.10035429451758526 | 0.17410094409722182 | 0.1706058082163469 |
| 3001 | 0.09498480005571097 | 0.1047839362935481 | 0.19822210795387580 | 0.18025083083814558 |

**Root cause established, not guessed.** The script is fully seeded
(`rng = default_rng(seed=p)`), so the drift is not sampling noise. Re-running
the *same* script on the *same* machine with only `OMP_NUM_THREADS=1
MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1` gives a *third* set of values:

```
p=2207: n=204, KS_WD=0.0518, KS_Pois=0.2662 [WD]
p=1597: n=138, KS_WD=0.0944, KS_Pois=0.3098 [WD]
p=2161: n=160, KS_WD=0.0929, KS_Pois=0.1621 [WD]
p=3001: n=178, KS_WD=0.0963, KS_Pois=0.1701 [WD]
```

So `ks_wd`/`ks_poiss` in this artifact are **BLAS-thread-nondeterministic**:
`np.linalg.eigvals` reorders/perturbs eigenvalues at ~1e-13, and because a KS
statistic is a supremum over order statistics with near-ties, the attained
maximum jumps to a different point. These numbers are reproducible to roughly
one significant figure only.

**What does reproduce:** the qualitative claim. `KS_WD < KS_Poisson`, verdict
`[WD]`, in **4/4 primes in all three runs** — i.e. MANIFEST's
"Perturbation ⇒ WD-not-Poisson (4 primes)" holds. The specific KS decimals
quoted in the artifact do not.

## 5. `python src/verify_perturbation_unitary.py`

**As shipped:** exit code **1**, wall **214.3 s** — same pattern, all numbers
printed, then `FileNotFoundError` on
`...OneDrive\...\artifacts\unitary_perturbation.json`.

```
=== Unitary-flow perturbation verification ===
p=1597: n=138 clusters=[47, 47, 47] KS_WD=0.0672 KS_Pois=0.2828
p=2161: n=160 clusters=[55, 54, 54] KS_WD=0.0670 KS_Pois=0.2776
p=2207: n=204 clusters=[69, 69, 69] KS_WD=0.0638 KS_Pois=0.2778
p=3001: n=178 clusters=[61, 60, 60] KS_WD=0.0643 KS_Pois=0.2799
--- epsilon sensitivity at p=2207 ---
eps=0.001: n=204 KS_WD=0.0673 KS_Pois=0.2544
eps=0.0001: n=204 KS_WD=0.0663 KS_Pois=0.2614
eps=1e-05: n=204 KS_WD=0.0832 KS_Pois=0.2602
```

**Wrapped:** exit code **0**, wall **263.0 s**, identical numbers, artifact
written to `_audit/redirect/unitary_perturbation.json`.

**DISCREPANCY vs committed `unitary_perturbation.json`, same mechanism.**
`n`, `clusters` and `max_match_dist` reproduce to ~1e-12 (e.g. p=1597
0.0013728569807674152 recorded vs 0.0013728569807671292 fresh), which shows the
spectra and the matching are stable. Of the 7 KS rows, 4 agree to ~1e-10
(p=1597, p=2207, eps=1e-4, eps=1e-5) and 3 jump:

| row | ks_wd recorded | ks_wd fresh |
|---|---|---|
| p=2161 | 0.06888586171275707 | 0.06696279658113062 |
| p=3001 | 0.07555459195098381 | 0.06431863685591259 |
| eps=0.001 | 0.09053682489776738 | 0.06729249680190208 |

The MANIFEST claim "Unitary-flow WD 4 primes" reproduces qualitatively
(KS_WD ≈ 0.064–0.067 vs KS_Poisson ≈ 0.28, 4/4). The exact KS decimals do not.

## 6. `python review/scripts/smoke_test_src.py`

**As shipped:** exit code **1**, wall **0.25 s** — **ERROR, nothing verified.**

```
  FAIL core: catmap_core: No module named 'catmap_core'
  FAIL core: master_formula_strong (find_orbit_H): No module named 'master_formula_strong'
  FAIL renamed: reduced_resonance.n3_count: No module named 'reduced_resonance'
  FAIL renamed: audit_tail_bound import: No module named 'audit_tail_bound'
  FAIL renamed: diag_conditional_prob import: No module named 'diag_conditional_prob'
ModuleNotFoundError: No module named 'reduced_resonance'
```

All 5 "FAIL"s are the stale-path bug, not real module breakage.

**Wrapped:** exit code **0**, wall **0.74 s**, **5/5 PASS**:

```
  OK  core: catmap_core
  OK  core: master_formula_strong (find_orbit_H)
  OK  renamed: reduced_resonance.n3_count
  OK  renamed: audit_tail_bound import
  OK  renamed: diag_conditional_prob import
  mean=0.0967 vs exact=0.0980 (OK)

5/5 module smoke tests passed
```

The MANIFEST correction note "smoke-test denominator 6→5" is consistent with
the `5/5` line. No artifact. No numeric discrepancy.

## 7. `python review/scripts/quick_regression.py`

**As shipped:** exit code **1**, wall **0.25 s** — **ERROR, nothing verified.**

```
ModuleNotFoundError: No module named 'master_general'
```

**Wrapped:** exit code **0**, wall **23.9 s**, **3/3 PASS**:

```
[PASS] r=2 A=[2, 1, 1, 1]: err (5.9e-15,5.2e-16) (2.6e-15,8.2e-16) (1.2e-14,1.7e-15) (0.5s)
[PASS] r=4 A=[2, 1, 1, 1]: err (6.2e-16,1.1e-16) (4.3e-16,1.4e-16) (1.9e-15,3.7e-17) (13.9s)
[PASS] r=4 A=[3, 1, 2, 1]: err (2.4e-15,2.7e-16) (1.4e-16,1.8e-16) (5.8e-16,4.5e-17) (9.1s)
```

Errors match the corresponding rows of the fresh `master_general.json` exactly.
No artifact. No numeric discrepancy.

## 8. `python review/scripts/run45_lemma.py`

* exit code **0**, wall **0.25 s**
* script verdict: **8/8 `OK`**

```
p=5: n3 brute=12 closed=12 OK | n4 brute=52 v1=52 OK
p=7: n3 brute=30 closed=30 OK | n4 brute=186 v1=186 OK
p=11: n3 brute=90 closed=90 OK | n4 brute=910 v1=910 OK
p=13: n3 brute=132 closed=132 OK | n4 brute=1596 v1=1596 OK
```

Writes no artifact (MANIFEST lists it as "brute force in transcript"), so there
is nothing to compare; the closed forms `(p-1)(p-2)` and `(p-1)(p²-3p+3)` are
confirmed against brute force at all 4 primes. **No discrepancy.**

## 9. `python src/master_general.py`

* exit code **0**, wall **755.7 s** = **12 min 36 s** — inside the documented
  ~17 min budget, **no timeout**.
* script verdict: **ALL PASS** (5/5 configs)

```
=== RUN 12 Phase A: general-r master formula ===
[PASS] A=[2, 1, 1, 1] N=101 r=2: err (5.9e-15,5.2e-16) (2.6e-15,8.2e-16) (1.2e-14,1.7e-15) (0.5s)
[PASS] A=[2, 1, 1, 1] N=101 r=3: err (2.9e-15,2.9e-16) (2.8e-16,2.1e-16) (4.4e-15,8.2e-16) (23.1s)
[PASS] A=[2, 1, 1, 1] N=101 r=4: err (6.2e-16,1.1e-16) (4.3e-16,1.4e-16) (1.9e-15,3.7e-17) (13.0s)
[PASS] A=[3, 1, 2, 1] N=101 r=4: err (2.4e-15,2.7e-16) (1.4e-16,1.8e-16) (5.8e-16,4.5e-17) (9.1s)
[PASS] A=[2, 1, 1, 1] N=101 r=5: err (7.6e-17,1.2e-17) (7.3e-17,9.4e-18) (4.0e-16,3.8e-18) (709.5s)
saved artifacts/master_general.json
ALL PASS
```

* `artifacts/master_general.json` is **not** byte-identical, but agrees
  numerically: over all 15 rows, `max |lhs_recorded − lhs_fresh| = 1.9e-15`
  (largest relative change ~1e-14, i.e. last 1–2 bits), and `passed=true` on
  all 5 runs in both copies. This is floating-point summation order, expected.
* MANIFEST claims verified: "regression 4/4 PASS" (the first four configs) and
  "NEW r=5 ALL-PASS err~1e-17" — fresh r=5 errors are
  (7.6e-17, 7.3e-17, 4.0e-16) real / (1.2e-17, 9.4e-18, 3.8e-18) imaginary,
  matching the recorded (7.5e-17, 7.1e-17, 4.0e-16).
* Timing note: recorded `dt` values were 0.9/36.8/21.5/14.4/1030.9 s; this
  machine gave 0.5/23.1/13.0/9.1/709.5 s (faster host, not a discrepancy).
* **No numeric discrepancy.**

## 10. `python review/scripts/audit_orders.py`

**As shipped:** exit code **1**, wall **0.9 s** — all 10 rows printed, then
`FileNotFoundError` on `...OneDrive\...\artifacts\audit_orders.json`.

```
exp_multi p=1597: ord(a)=None  K_proj=17 (hit -I at 17? True)  SL_ord=34  p/K=93.9
exp_multi p=2161: ord(a)=40  K_proj=20 (hit -I at 20? True)  SL_ord=40  p/K=108.0
exp_multi p=2207: ord(a)=None  K_proj=16 (hit -I at 16? True)  SL_ord=32  p/K=137.9
exp_multi p=3001: ord(a)=50  K_proj=25 (hit -I at 25? True)  SL_ord=50  p/K=120.0
exp_beta p=3571: ord(a)=17  K_proj=17 (hit -I at 17? False)  SL_ord=17  p/K=210.1
exp_beta p=4481: ord(a)=64  K_proj=32 (hit -I at 32? True)  SL_ord=64  p/K=140.0
exp_beta p=5779: ord(a)=27  K_proj=27 (hit -I at 27? False)  SL_ord=27  p/K=214.0
ledger_R27 p=4481: ord(a)=64  K_proj=32 (hit -I at 32? True)  SL_ord=64  p/K=140.0
ledger_R27 p=2207: ord(a)=None  K_proj=16 (hit -I at 16? True)  SL_ord=32  p/K=137.9
ledger_R27 p=3001: ord(a)=50  K_proj=25 (hit -I at 25? True)  SL_ord=50  p/K=120.0
```

**Wrapped:** exit code **0**, wall **0.65 s**; the produced
`audit_orders.json` is **byte-for-byte identical** to the committed artifact.
The MANIFEST claim "K: 3571→17, 4481→32, 5779→27; 1597/2207 inert" is confirmed
(3571→17, 4481→32, 5779→27; `split=false` for 1597 and 2207).
**No numeric discrepancy.**

## 11a. `python src/deligne_check.py`

* exit code **0**, wall **22.4 s**
* script verdict: `stable: True`

```
p=1013: N=983664  N0=1022123.0  |dN|=3.846e+04  |dN|/p^1.5=    1.19
p=1013: N=977592  N0=1022123.0  |dN|=4.453e+04  |dN|/p^1.5=    1.38
p=2053: N=4235328  N0=4206603.0  |dN|=2.873e+04  |dN|/p^1.5=    0.31
p=2053: N=4214808  N0=4206603.0  |dN|=8.205e+03  |dN|/p^1.5=    0.09
p=4099: N=16662468  N0=16785411.0  |dN|=1.229e+05  |dN|/p^1.5=    0.47
p=4099: N=17121444  N0=16785411.0  |dN|=3.360e+05  |dN|/p^1.5=    1.28
PRE-REGISTER verdict: {'max_ratio': 1.381173513364356, 'stable': True}
saved artifacts/deligne_check.json
```

* `artifacts/deligne_check.json` rewritten **byte-for-byte identical**.
* **No discrepancy.**

## 11b. `python src/deligne_check_ext.py`

**As shipped:** exit code **1**, wall **138.7 s** — all 12 ratios printed, then
`FileNotFoundError` on `...OneDrive\...\artifacts\deligne_check_ext.json`.

**Wrapped:** exit code **0**, wall **154.5 s**; produced
`deligne_check_ext.json` is **byte-for-byte identical** to the committed
artifact (all 12 ratios agree to full double precision, e.g. p=8191 near_deg_82
= 1.9223251461119781).

```
p=1013: generic ratio=0.125     near-deg d=11: 0.188   near-deg d=51: 1.255
p=2053: generic ratio=0.794     near-deg d=21: 0.971   near-deg d=103: 0.706
p=4099: generic ratio=0.968     near-deg d=41: 1.156   near-deg d=205: 1.936
p=8191: generic ratio=1.215     near-deg d=82: 1.922   near-deg d=410: 1.547
```

**No numeric discrepancy.**

## 12a. `python src/master_formula.py`

* runnable as a script (has `if __name__ == "__main__"`).
* exit code **0**, wall **42.3 s**
* script verdict: **ALL PASS** (4 structure checks + 10 master rows)

```
=== M1 master moment formula (table-rho version) ===
[PASS] structure A=[2, 1, 1, 1] N=101 K=25: sigma fit=6.2e-15 tele=7.6e-14 rho_unimod=True (0s)
[PASS] master r=2 A=[2, 1, 1, 1] N=101: err=(5.9e-15,4.8e-16)[lhs=0.469] ... <|S|>/mf=6.64e-02
[PASS] master r=3 A=[2, 1, 1, 1] N=199: err=(6.1e-13,1.5e-14)[lhs=-4.035] ... <|S|>/mf=2.23e-02
[PASS] master r=4 A=[2, 1, 1, 1] N=521: err=(3.7e-14,1.1e-14)[lhs=0.441] ... <|S|>/mf=1.11e-01
[PASS] master r=4 A=[3, 1, 2, 1] N=101: err=(2.4e-15,2.4e-16)[lhs=0.007] ... <|S|>/mf=2.72e-02
saved artifacts/master_formula.json
ALL PASS
```

(full 16-line output in `_audit/logs/12a_master_formula.log`)

* `artifacts/master_formula.json` is not byte-identical but agrees numerically:
  10/10 master entries aligned on `(A, N, r)`, `max |lhs_recorded − lhs_fresh|
  = 1.9e-15`, `max |Δ mean_absS_over_mf| = 1.7e-18`, `passed=true` for all 10
  in both copies.
* **No numeric discrepancy.**

## 12b. `python src/master_formula_r4.py`

* runnable as a script. exit code **0**, wall **1.3 s**
* script verdict: **ALL CONFIRMED** (8/8 `[IDENTITY]`)

```
=== RUN 13 Phase 1: master formula certification ===
p=101 A=[2, 1, 1, 1] m=4: Tr[V^4]=0.0120+0.0021j [IDENTITY]
p=101 A=[2, 1, 1, 1] m=4: Tr[V^4]=0.0375+0.0182j [IDENTITY]
p=101 A=[2, 1, 1, 1] m=4: Tr[V^4]=0.0099+0.0027j [IDENTITY]
p=101 A=[2, 1, 1, 1] m=4: Tr[V^4]=0.0145+0.0002j [IDENTITY]
p=211 A=[2, 1, 1, 1] m=10: Tr[V^4]=-0.0171-0.0011j [IDENTITY]
p=211 A=[2, 1, 1, 1] m=10: Tr[V^4]=-0.0000+0.0098j [IDENTITY]
p=101 A=[3, 1, 2, 1] m=5: Tr[V^4]=-0.0022-0.0015j [IDENTITY]
p=101 A=[3, 1, 2, 1] m=6: Tr[V^4]=0.0053+0.0118j [IDENTITY]
saved artifacts/run13_master_cert.json
ALL CONFIRMED
```

* **Artifact had no committed baseline.** `artifacts/run13_master_cert.json`
  did **not exist** in the pre-run snapshot; this run created it. Nothing to
  compare against — the numbers are new, not reproduced.

## 12c. `python src/master_formula_strong.py`

* runnable as a script. exit code **0**, wall **0.8 s**
* script verdict: **6/6 `[MATCH]`** (the script prints no ALL-PASS token)

```
=== RUN 13 Phase 1b: strong master formula ===
p=101 A=[2, 1, 1, 1] mult=4 k=25: sol=1225 vs WD=1225 [MATCH]
p=101 A=[2, 1, 1, 1] mult=4 k=25: sol=1225 vs WD=1225 [MATCH]
p=101 A=[2, 1, 1, 1] mult=4 k=25: sol=1225 vs WD=1225 [MATCH]
p=101 A=[2, 1, 1, 1] mult=4 k=25: sol=1225 vs WD=1225 [MATCH]
p=211 A=[2, 1, 1, 1] mult=10 k=21: sol=861 vs WD=861 [MATCH]
p=211 A=[2, 1, 1, 1] mult=10 k=21: sol=861 vs WD=861 [MATCH]
saved artifacts/run13_strong_master.json
```

Sanity check of the theorem itself: 1225 = 2·25²−25 and 861 = 2·21²−21, i.e.
the odd-k branch `2k²−k` of the matched identity. Correct.

* **MANIFEST INCONSISTENCY.** MANIFEST.md cites `run13_strong_master.json` as
  the artifact backing "Matched identity, Thm core", but that file was **absent
  from `artifacts/` before this rerun** (it is not in the pre-run snapshot of
  121 files). The manifest pointed at a non-existent artifact; this run created
  it. No baseline to compare against.

## 13. `python review/scripts/audit_independent_suite.py`

**As shipped:** exit code **1**, wall **0.28 s** — **the worst failure in the
suite**: `dump()` is called immediately after `v7()`, so the run dies before
V1–V6 ever start.

```
V7 anchor p=5,k=2: total=6 types={'pairing': 6} PASS
FileNotFoundError: [Errno 2] No such file or directory:
'C:\\Users\\churi\\OneDrive\\Desktop\\project_1\\BGS\\artifacts\\audit_independent_suite.json'
```

As shipped, the "two-key" independent suite verifies **1 of 7 checks**.

**Wrapped:** exit code **0**, wall **106.3 s**, **all of V1–V7 pass**:

```
V7 anchor p=5,k=2: total=6 types={'pairing': 6} PASS
V1 matched identity: 51/51 pass
V2 zero counts: 8/8 pass
V3 p=5 k=2: COMPLETE enum matches k^3*Z4^2 = 21632
V3 p=7 k=2: COMPLETE enum matches k^3*Z4^2 = 276768
V3 p=7 k=3: COMPLETE enum matches k^3*Z4^2 = 934092
V5 collision lemma: worst=2 over 8 (p,k) configs (PASS)
V6 r=6 strata: 12/12 pass
V4 tail bound: 38/38 configs pass (violations=0, degenerate patterns skipped=72)
TOTAL runtime 105.9 s
SUMMARY: {'V1': True, 'V2': True, 'V3': True, 'V4': True, 'V5': True, 'V6': True}
```

* The produced `audit_independent_suite.json` is **byte-for-byte identical** to
  the committed artifact — all of V1–V7 reproduce exactly.
* MANIFEST claim "Independent suite V1–V6 (matched id, zerocounts, meanlaw
  complete enum p∈{5,7}, tail fresh grid, collision, r6 strata)" — confirmed,
  and the collision bound `C(u,v) ≤ 4` is comfortably satisfied (worst
  observed = 2).
* **No numeric discrepancy.**

---

## Artifact comparison summary

Files freshly written into `artifacts/` by this rerun, versus the pre-run
snapshot in `_audit\pre\`:

| Artifact | Written by | Comparison |
|---|---|---|
| `run46_exact_mean.json` | verify_mean_law | **identical (bytes)** |
| `run36_audit.json` | audit_tail_bound | **identical (bytes)** |
| `char_expansion_cert.json` | char_expansion_cert | **identical (bytes)** |
| `deligne_check.json` | deligne_check | **identical (bytes)** |
| `master_general.json` | master_general | changed; numerically equal, max Δlhs 1.9e-15, all `passed` unchanged |
| `master_formula.json` | master_formula | changed; numerically equal, max Δlhs 1.9e-15, max Δcancel 1.7e-18 |
| `run13_master_cert.json` | master_formula_r4 | **NEW file — no committed baseline** |
| `run13_strong_master.json` | master_formula_strong | **NEW file — no committed baseline, yet cited by MANIFEST.md** |

A full sweep of all 121 pre-existing top-level artifact files confirms **only
these 4 were modified and only these 2 created**; nothing else in `artifacts/`
was touched.

Artifacts that the scripts *tried* to write to the stale OneDrive path and that
were therefore captured in `_audit\redirect\` instead:

| Artifact | Written by | Comparison vs committed |
|---|---|---|
| `audit_orders.json` | audit_orders | **identical (bytes)** |
| `deligne_check_ext.json` | deligne_check_ext | **identical (bytes)** |
| `audit_independent_suite.json` | audit_independent_suite | **identical (bytes)** |
| `run31_multiprime.json` | verify_perturbation_wd | **DISCREPANCY** — p/n/clusters identical, `ks_wd`/`ks_poiss` differ in 3 of 4 primes (up to 25% rel.) |
| `unitary_perturbation.json` | verify_perturbation_unitary | **DISCREPANCY** — n/clusters/max_match_dist identical to ~1e-12, `ks_wd`/`ks_poisson` differ in 3 of 7 rows (up to 26% rel.) |

---

## Final table — script → outcome

"As shipped" is the verdict for the exact command requested. "Wrapped" is the
same script through the audit shim that repairs only the stale absolute path.

| # | Command | Exit | Wall | As shipped | Wrapped | Artifact vs committed |
|---|---|---|---|---|---|---|
| 1 | `python src/verify_mean_law.py` | 0 | 13.7 s | **reproduces** | — | identical |
| 2 | `python src/audit_tail_bound.py` | 0 | 591.8 s | **reproduces** | — | identical |
| 3 | `python src/char_expansion_cert.py` | 0 | 2.8 s | **reproduces** | — | identical |
| 4 | `python src/verify_perturbation_wd.py` | 1 | 114.6 s | **errors** (path) | reproduces qualitatively only | **discrepancy (KS)** |
| 5 | `python src/verify_perturbation_unitary.py` | 1 | 214.3 s | **errors** (path) | reproduces qualitatively only | **discrepancy (KS)** |
| 6 | `python review/scripts/smoke_test_src.py` | 1 | 0.25 s | **errors** (path) | **reproduces** 5/5 | none |
| 7 | `python review/scripts/quick_regression.py` | 1 | 0.25 s | **errors** (path) | **reproduces** 3/3 | none |
| 8 | `python review/scripts/run45_lemma.py` | 0 | 0.25 s | **reproduces** 8/8 | — | none |
| 9 | `python src/master_general.py` | 0 | 755.7 s | **reproduces** 5/5 ALL PASS | — | equal to 1.9e-15 |
| 10 | `python review/scripts/audit_orders.py` | 1 | 0.9 s | **errors** (path) | **reproduces** | identical |
| 11a | `python src/deligne_check.py` | 0 | 22.4 s | **reproduces** | — | identical |
| 11b | `python src/deligne_check_ext.py` | 1 | 138.7 s | **errors** (path) | **reproduces** | identical |
| 12a | `python src/master_formula.py` | 0 | 42.3 s | **reproduces** ALL PASS | — | equal to 1.9e-15 |
| 12b | `python src/master_formula_r4.py` | 0 | 1.3 s | runs, ALL CONFIRMED | — | **no baseline (new file)** |
| 12c | `python src/master_formula_strong.py` | 0 | 0.8 s | runs, 6/6 MATCH | — | **no baseline (new file)** |
| 13 | `python review/scripts/audit_independent_suite.py` | 1 | 0.28 s | **errors** (path); only V7 of 7 ran | **reproduces** V1–V7 | identical |

**Timeouts: 0.** `master_general.py` finished in 12 min 36 s, well inside the
25-min allowance. No script had to be killed.

### Counts

* **16** script invocations attempted, **16** completed (none skipped, none hung).
* **9 reproduce as shipped**: 1, 2, 3, 8, 9, 11a, 12a — plus 12b and 12c, which
  ran clean but have no committed baseline to reproduce.
* **7 error as shipped** (4, 5, 6, 7, 10, 11b, 13), every one of them from the
  single stale-path defect. Of these, **5 reproduce exactly once the path is
  repaired** (6, 7, 10, 11b, 13) and **2 reproduce only qualitatively** (4, 5).
* **Genuinely reproduced claims: 18 distinct check groups** — mean law (5/5),
  tail bound (196 configs, 0 violations of floor(k²/p)+2), character expansion
  (3/3), zero-count lemmas Z₃/Z₄ (8/8), general-r master formula r=2…5 (15/15
  rows, incl. r=5 at err ~1e-17), Deligne pre-register (`stable: True`,
  max_ratio 1.381), Deligne extended (12/12 ratios), r≤4 master formula (10/10
  rows + 4 structure checks), projective orders (10/10 rows), independent-suite
  V1 (51/51), V2 (8/8), V3 (3/3), V4 (38/38, 0 violations), V5 (worst 2 ≤ 4),
  V6 (12/12), V7 anchor, module smoke test (5/5), quick regression (3/3).
* **Non-reproductions: 2** — the recorded KS statistics in
  `run31_multiprime.json` and `unitary_perturbation.json`. Their *verdicts*
  (WD, not Poisson, 4/4 primes) reproduce; their *numbers* do not, and are not
  reproducible even on this single machine.
* **2 artifacts had no committed baseline** (`run13_master_cert.json`,
  `run13_strong_master.json`), so their numbers are recorded here for the first
  time rather than reproduced.

---

## Scripts NOT run, and why

`src/` holds 36 `.py` files, `review/scripts/` holds 16 files (15 `.py` +
1 `.jl`). 16 invocations covering 16 distinct files were requested and run.
The remaining 36 files were not executed:

### `src/` — 25 not run

Outside the requested list; not part of the canonical verification sequence:
`audit_matching.py`, `check_split_vs_inert.py`, `diag_conditional_prob.py`,
`exact_verify_run5.py`, `fast_weil.py`, `find_small_period_primes.py`,
`hecke_local_law_test.py`, `pair_classifier.py`, `phase1c_forms.py`,
`phase2_beta.py`, `phase2_mc_reference.py`, `phase2_pooled.py`,
`phase3_Apk_sweep.py`, `phase3_Dpk.py`, `phase3_odd_fit.py`,
`phase3_r6_families.py`, `resolve_1122.py`, `ring2_subgroup_kloosterman.py`,
`smoothness_check.py`, `task_a_entries.py`, `task_b_compensation.py`,
`task_k22_anomaly.py`, `test_arithmetic_perturbation.py`.

Two of the 25 are libraries, not scripts, and were exercised indirectly by the
runs above: `catmap_core.py` (imported by master_formula / master_general /
verify_perturbation_*) and `reduced_resonance.py` (imported by verify_mean_law /
audit_tail_bound / smoke_test). Both import and run clean.

`src/archive/` and `src/llm/` were not touched at all (archive is explicitly
historical per MANIFEST.md).

### `review/scripts/` — 11 not run

* `julia_crosscheck.jl` — Julia, not `python`; not in the requested list.
* `gpu_replicate.py` — requires CUDA torch; no GPU in this environment.
* `degenerate_strata_scan.py`, `compare_SJ.py`, `no_threshold.py`,
  `grok_check.py`, `run34b.py`, `run34c.py`, `run34d.py`, `diag_one.py`,
  `diag_primes.py` — outside the requested list.

Note that 10 of these 11 also carry the stale OneDrive path, so most would fail
the same way if run today.

---

## Recommendations (not applied — no project file was modified)

1. Replace all 34 occurrences of
   `C:\Users\churi\OneDrive\Desktop\project_1\BGS` with a path derived from
   `__file__` (`master_general.py`, `master_formula*.py`, `deligne_check.py`
   already do this correctly and are the ones that ran clean). This single
   change would take the suite from 9/16 to 14/16 green.
2. In `audit_independent_suite.py`, move `dump()` out of the hot path or make it
   fault-tolerant; as written, one bad path silences 6 of 7 verifications while
   still printing a `PASS`.
3. Stop treating the `ks_wd` / `ks_poiss` decimals as reproducible quantities.
   Either record them with an explicit tolerance ("KS_WD ≈ 0.05–0.10, KS_Poisson
   ≈ 0.17–0.29") or pin BLAS threading and eigenvalue ordering. The physics
   conclusion is unaffected.
4. Regenerate or de-cite `run13_strong_master.json` in `MANIFEST.md` — the
   manifest referenced a file that was not in the tree.

## Files produced by this audit

```
C:\Users\churi\Desktop\BGS\_audit\rerun_report.md      this report
C:\Users\churi\Desktop\BGS\_audit\pre\                 121 pre-run artifact files
C:\Users\churi\Desktop\BGS\_audit\logs\                verbatim stdout/stderr, 26 files
C:\Users\churi\Desktop\BGS\_audit\redirect\            artifacts intercepted from the stale path
C:\Users\churi\Desktop\BGS\_audit\audit_wrapper.py     path shim (audit-only)
C:\Users\churi\Desktop\BGS\_audit\run.sh               timing/capture harness
```










