# Line H notes (resume point). Started 2026-10-30 16:20 box clock (box clock = UTC+5, Asia/Yekaterinburg; corrected per referee rec. 10).
Read: lineG REPORT, lineF REPORT, audit lineFG REPORT, claim registry TRACE-179/187-196. Repo clone: BGS/ (e378ad11), read-only.
## Plan
- PRIORITY H2: certify 49-state lifted operators for Line B kick f_B (eta=2), one sign s suffices.
  Key ideas: (i) K0=1 or 2 core (dominant letters x=n/7 small -> core closed), (ii) only need ONE eigenvalue outside |z|=R
  (R in (1.30,1.88)), others inside R (Weyl with R^{m-1}*tracenorm), no small-r2 needed; (iii) big linear algebra in float BLAS with
  rigorous Rump-type error bounds (mid-rad), entries from arb; resolvent via Schur + comparison matrix or Neumann/Frobenius.
  kappa odd always (k odd, u odd, y' odd) => |c_b|=1/2 for b even, 0 for b odd.
- H1: numerics on uniform-in-b spectral radius of non-resonant (a,b) operators (later).
## Log
- 16:50 Line G pre-registered m=17 (k1) outcome EXISTS (lineG/logs/eval17_k1.log, run by lineG watcher at 16:26; predictions sha fa8505f5 verified = file):
  ALL items PASS. total F/2m=39.0651, bulk F/2m(H=8)=2.0249, W'_act/m=+0.092 (m=15: +0.23) -> upward drift REVERSED. Strong support for R'.
- float f49.py (own builder, K0=1 core = 3 discs): s=-1,b=0,K=14: top 1.89683463 (LineF K0=2: 1.896835), next 1.294,1.285,1.257. eig D=2058 took 168s (box slow).
- 17:05 ghat_arb.py: rigorous ghat for f_B via Jacobi-Anger convolution of 7 Bessel sequences (k=1,2,5,6,7,8,9), weighted-l1 truncation
  error by telescoping; matches FFT to 5.5e-16. cert49_build.py (arb bounds + mid/rad Galerkin export) written & runs (K0=1 test).
- FINDINGS: (1) true resolvent sup on |z|=1.5 (core, K=10, s=-1,b=0) ~ 25 -> mild non-normality; crude Neumann/Frobenius-power bound ~1e6 (useless).
  (2) K0=1 core NOT closed: letters |x|>=9.7 escape, W*M(rho=1.2) ~ 0.07 -> Delta ~0.1. Need K0>=2 (rho~1.0) or 3. Multiplier growth e^{2pi c0|x| rho}.
  (3) gauge identity: c0[sum x u + x^2/2] = (lam/2) sum u_j^2 on periodic orbits (global gauge e(alpha u^2), alpha=c0 lam^2/2) -> multiplier
      letter-independent e(lam u^2/2) but huge on complex discs: no gain. 7-adic analogue: chirp gauge makes U_n = Q*P_n (Q diag chirp, P_n affine perm).
      C^49 irreducible under the U_n (Heisenberg) -> no exact reduction.
  (4) eigen 1.896835 already stable at K=10, K0=1.
- 17:25 KEY: matmul runs at ~50 GFlops (eig/LAPACK slow, BLAS3 fast) -> power-based rigorous Neumann at D~7k is cheap (~45 s/matmul).
  float neum_test (K0=1,K=10,rho=1.0,s=-1,b=0, deflated Y): sharp sum_j ||Y^j||_2 R^-(j+1) = 12.7 (R=1.6), 8.2 (R=1.75): mild transients.
  Bounds scan (cert49_build): K0=2, rho=.85, beta=3-3.5, K=28-30 (|c|<=1), K2=22-24 (|c|=2): delta1~2-4e-3, Delta~1.6-2.6e-3, ||X||~1-1.6,
  proxy (delta+Delta)(1+X/1.6) ~ 7e-3..1e-2 => need rigorous ||R_core|| <~ 100. D ~ 6.3-6.8k.
- rig_spec.py written (Householder deflation + explicit powers Y^j, Frobenius / sqrt(n1 ninf) norms, rigorous float rounding bounds,
  b12 Y^j row vectors for the coupling term). pilot.sh launched (K=16,K2=12 -> D=3528) -> logs/pilot.log

## 17:5x resume-2
- h1_scan: fixed filter (|a|<=b, b<=Bmax). Result: Galerkin spectral radii for |a|/b >~ 0.3 are garbage (e.g. (±2,4): 11.07, (1,1): 1733), multipliers e^{2pi|coef|n rho} with coef=-4a c0/b ill-conditioned. Small |a|/b (a=±1,b=3,5): 1.14-1.27 < lambda^{1/4}=1.5538? (lambda^{1/4}=1.5538). Killed; NOT usable as evidence beyond those rows.
- rig_spec v1 bug: power error recursion e*=||Y||_F grew like 37^j (6e6 at j=12). Fixed (v2): e_j <= sum_i ||E_i|| N_{j-i}. Backup rig_spec_v1.py.
- pilot ARPACK eigs sector0: mu=1.34314+1.33939i (|mu|=1.89683), next |.|=1.294,1.287,1.25,1.24,1.22. single dominant.
- pilot v2 running -> logs/pilot_rig2.log, pilot_dom.json
- 18:0x prodV sector0 build done (D=6762, delta1 2.03e-3 delta2 2.6e-5 Delta 2.60e-3 X 0.947 trace 10673). rig_spec v3 (R,r1 scan) launched -> logs/prodV_rig0.log; pilot v3 test logs/pilot_rig3.log. Pilot v2: Rcore_R=65.7 Rcore_r1=129 (r1=.05), true resolvent ~25 => bound ~2.6x loose; prod need pert*fullR<1, expected F_R2~0.5
## 18:0x resume-3 (new worker)
- prodV sector0 DOM CERTIFIED (logs/prodV_dom0.json, logs/prodV_rig0.log, p=32, 1211 s): e.g. R=1.55,r1=0.05: F_R1=0.914,F_R2=0.540 -> exactly one eig of V_0 in |z|>1.55, |mu| in [1.84683479,1.94683480]; R=1.5..1.7 all certified.
- queue_rest.sh alive (pid 1483549): prodVr build sectors 2,4,6 running -> then rig rest V2,4,6 then E build+rig. Do not restart.
- bounds49.py rewritten (v1 had undefined pell_h; now per-operator radii, closed-form tail constant C/4). Draft kept as bounds49_v1_draft.py.
- tracechk.sh launched (cert49_build K=16/12 V,E sectors 0,2,4,6 -> Tr identity vs audit/lineE T_full exact class sums, m=5,7,11,13) -> logs/tracechk.log
- Audit pass of cert49_build/rig_spec logic: Galerkin exactness, H^2 composition bounds, block row/col sqrt-sum-of-squares norm bounds, weighted ratios, Neumann tails, Householder kappa: no error found.
- 18:3x E rest sectors 0,2,4,6 ALL CERTIFIED (logs/prodE_rest{0,2,4,6}.json; R=1.0: F_R2~0.053; R=1.55: 0.0216). E_DONE.
- neg control logs/neg_rest_pilot0.log: rest mode on V_0 (|mu|=1.897) at R=1.6,1.85,1.9 -> NOT certified (as required).
- H1: code/h1_lift.py (Line F vertex/edge lift x C^{b^2}) reproduces h1_scan small-|a|/b radii (1.1388/1.1400, 1.2069/1.2082, 1.25806/1.25803, 1.27394/1.27395)
  and gives SANE radii where single-disc was garbage: (2,4,1) 1.4956 (single 11.07), (3,5,1) 1.1389 (single 37.0). Convergence run h1_conv.sh -> logs/h1_conv.log
  (configs K0=3,r=.8,K=24,Lk=5 and K0=3,r=.7,K=30,Lk=7; list incl. (±4,6),(±1,1)).
- V6 rest launched in parallel -> logs/prodV_rig6p.log / prodV_rest6p.json; queue2 will ALSO try b=6 later: kill queue2 V6 run when V4 done (or just let it, harmless but slow).
## 18:50 resume-4
- NOTE: queue_rest.sh (pid 1483549) no longer exists: killed at 18:0x, replaced by queue2.sh (pid 1495118) which runs V2 -> V4 -> V6 rest sequentially; V6 also running in parallel (pid 1504933 -> prodV_rest6p.json).
- V2 rest at j=24 (2448 s) -> scan imminent. h1_conv.sh bash killed to save load (first config python 1504746 continues; second config K=30 NOT run).
- 18:55 V2 rest CERTIFIED (logs/prodV_rest2.json): R=1.45 F_R2=0.732, R=1.5 0.496, R=1.55 0.389 (R=1.4 fails 1.89; 1.35 Neumann fails).
  queue2 bash killed after it launched V4 (pid 1508868 -> prodV_rest4.json) so it will not rerun V6; V6 = pid 1504933 -> prodV_rest6p.json.
  After both finish: run bounds49.py with prodV_rest6p.json for sector 6. prodVr_b2 npy deleted by queue2; b4/b6 npy remain (delete after).
- 19:2x H1 lifted float (logs/h1_conv.log cfg1 K0=3,r=.8,K=24,Lk=5; logs/h1_conv2.log cfg2 K0=4,r=.7,K=32,Lk=7):
  (2,4,1) [N≡2 family, theta=-1]: 1.49555 -> 1.49565 CONVERGED (Line G two-point estimate for N≡±2: ~1.50). Single-disc gave 11.07/47.07 (garbage).
  (±1,1) [N≡±1, theta=∓2]: 1.551->1.411 and 1.707->1.530: NOT converged -> no conclusion. (3,5),(−3,5),(±4,6): only cfg1 (1.139,1.236,1.237) -> unconfirmed.
- dom json lacked scan (rig_spec v3): built logs/prodV_dom0_scan.json from prodV_rig0.log (30 options, 29 certified). bounds49 dry run with V2 standing in for V4/V6: m0=47.
- 19:5x V4 (R=1.45 F=0.841) and V6 (prodV_rest6p, R=1.45 F=0.732) CERTIFIED. ALL SECTORS CERTIFIED.
  bounds49_final: m0=47 (odd, 3∤m), F/2m>=7.0e3 (m=47), tail g=1.41279, C=0.25. SHA256 in logs/SHA256_H2.txt. REPORT.md §0,§1.4,§2 written (final).
  prodVr_b4/b6 npy deleted. Remaining optional: Lean numeric instance; s=+1 sign; m≡0 mod 3; H1 cfg2 for (3,5),(4,6).
## 20:20 referee fixes (audit/lineH/REPORT.md: ACCEPT AFTER FIXES)
- rig_spec.py -> v4 (old archived as rig_spec_v3.py sha a1528502…): gc=sqrt2*gamma_{2n+2}; JSON inputs padded 1+2^-40; outputs fu/fl (nextafter);
  a-posteriori Householder residual (from referee ref_rig.py); provenance block with sha256 of code/build json/npy; arb strings for F.
- run_v4.sh launched: V0 dom (p=32) || [rebuild prodVr 2,4,6 -> E0..6 rest -> V4,V2,V6 rest]. logs/v4_*.json/.log, code sha in logs/SHA256_code_v4_runs.txt
- 20:5x v4 V0 dom CERTIFIED (logs/v4_V0_dom.json): R=1.5,r1=0.05 F_R1=0.91352 F_R2=0.62352 (pert 4.649079e-3, epsH a-post 3.2e-10); r1=0.1 F_R1=0.5859.
  v4 E0..E6 rest certified (R=1.0 and 1.2). prodVr rebuilt (bounds == prodV). V4 v4 running (pid 1554490, seq bash killed); V2,V6 v4 launched in parallel.
- Lean lean/LineH.lean (namespace Bgs.LineH, + kappa lemmas) compiles in /workspace/bgs-int/BGS/formalization; axioms log logs/lean_v3_axioms.log (std 3 only).
- kappa_check.py: 398 (m,s) pairs exact OK. referee files adopted in referee_cert/ (README, SHA256).
- 21:10 resume: written (not yet run) tools/new_claims_h.py, tools/make_packet.py, tools/update_report.py, packet/*.tmpl + README_*.md.
  ORDER once V2/V4/V6 v4 done: bounds49.py (v4 jsons) -> logs/bounds49_v4.json; tools/new_claims_h.py; tools/make_packet.py; tools/update_report.py; INTEGRATION_NOTES.md.
- 21:35 v4 V4 rest CERTIFIED (R=1.5 F_R2=0.54371, R=1.55 F_R2=0.41740). V2,V6 at j=20. INTEGRATION_NOTES.md drafted.
- 21:46 v4 V2,V6 rest CERTIFIED (R=1.5: F_R2 0.49578/0.49593; R=1.55: 0.38904/0.38912). ALL v4 sectors done.
- 21:50 bounds49 v3 on v4 inputs -> logs/bounds49_v4.json: m0=47 W/m>=1.4e4; table matches referee (53 2.8e5/5.7e5, 71 1.5e8/3.1e8, 85 1.6e10/3.3e10, 49 W 7.6e4). mu_lo 1.84683, R0 1.5, r1 0.05.
