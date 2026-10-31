# NOTES_N11b (Line N11b)
## 2026-10-31 23:35:54 +05 — start
## 2026-10-31 23:45:23 +05 — unit types + certificates
- code/u_cert.py = N9 n9_cert.py machinery verbatim with ONE core zeta_U = 2 beta/eps (derivation: lam^p = 1 + 2 h_p eps^p, so tau_i = Tr(lam^i beta)/h_p
  is p-periodic; window at 0, single bump per period at i0=(p-1)/2; lam^{i0}/h_p = (2/eps)/(1-lam^{-p})).  w_U = r_U^3 (3 periods).
- [CA] (limit p->oo, conj convention of n9_cert = complex conjugate of Zbatch sg=+1):
  eps (1+sqrt2): |w| in [1.064e-3, 1.526e-3], Re in [4.14e-4, 7.31e-4]; exact Zbatch p=47: 5.728e-4 - 1.1842e-3 i (|.|=1.3154e-3).
  6: |w|<=2.81e-4 (exact 2.16e-4); 3eps: |w|<=2.11e-4 (1.45e-4); 2eps: <=1.32e-4 (9.0e-5); 1: <=9.93e-5 (6.46e-5); sqrt2: <=6.07e-5 (3.63e-5).
- p=47 single-bump types (a_unit_single_p47.json, |a|<=6,|b|<=5): see log; two-bump gas test running.
## 2026-10-31 23:50:18 +0500 — exact level-h_p X/Y split (p=5,7) + Lambda_U
- code/b_exactXY.py (N6 j_exactdev set-up verbatim; S exact; kappa(u)=sum_{t in S} e(tbar u/d)). [N]
  p=5 (d=41,n=39): X=0.003533+0.002496i, Y=0.010944+0.001375i (|Y|=0.0110 > |X|!), |1+X+Y|=1.01448, |1+X|=1.00354, CS lower 0.0292 <= Dev/main 0.153.
  p=7 (d=239,n=237): X=0.010724+0.005761i, Y=0.001066+0.000328i, |1+X+Y|=1.01181, |1+X|=1.01074, CS 0.0238 <= 0.281.
  max|kappa(u!=0)| = 1.994 / 1.9998 (<=2 as proved). sum|r_unit| = 1.087 / 1.898 (grows, but /n shrinks: 2*sum/n = 0.056 / 0.016).
- Unit points ARE in the same CS bracket (same Zhat, same Z normalisation), weight kappa(N beta)/n, |.|<=2/(h_p-2).
- c_LambdaU.py p=47: Lambda_U = 1.005e-3 - 1.834e-3 i (|.|=2.09e-3), A_U=sum|r|=3.96e-3 over 102 lam-classes (|a|<=6,|b|<=5).
  Re Lambda_U (1.0e-3) > Re Lambda (7.49e-4): unit gas grows faster than iso gas UNWEIGHTED; weight 2/n ~ 4 eps^{-p} kills it.
- launched a_unit_single p=29,59 (nohup) for Lambda_U stability.

## 2026-10-31 23:57:41 +0500 — Lambda_U stable; model table; N9b erratum done; mixed p=11 sample
- Lambda_U identical at p=29,47,59 (to ~1e-11): 1.005429e-3 - 1.834361e-3 i, A_U = 3.957e-3 [N].
- e_model.py: unit-gas Y central ~ -(2/n)*2[(1+Lam+Lam_U)^p-(1+Lam)^p]; |Y_gas|/|X| = 0.13 (p=5), 2.1e-2 (7), 6e-4 (11), 8e-11 (29), 1e-17 (47).
  exponents/p: X growth +6.236e-4; unit gas relative -0.880; C' bulk -0.341; mixed (G*) eps*(Gamma/mu*)^3: Gamma=T' +9.4e-5 (marginal!), 1.36 -0.146, 1.2624 -0.369.
- NOTES_N9b.md: headings relabelled with artifact evidence + ERRATUM appended (original kept at logs/NOTES_N9b.orig.md). 
- a_per box convention: profile uses dist >= theta as OUTSIDE => OPEN box. Closed box at 1/16: n=4 value drops 1.4296 -> 1.2407; Gamma_per(1/16,closed, n<=8) <= 1.3646.
- d_mixed p=11 (d=8119=23*353), iso mod 23 / unit mod 353, 2% sample of 126896 reps: Y_mixed ~ -4.6e-4 - 2.3e-4 i (|.|=5.2e-4), max|kappa|=42, max|r|=2.1e-4. [N, sampled]

## 2026-11-01 00:04:21 +0500 — mixed p=11 exact; steering (N12 adapted norm) absorbed
- d_mixed p=11 iso mod 353 / unit mod 23 (ALL 7766 reps, 341220 pts) [N]: Y_mixed = -9.3e-7 + 4.08e-5 i; max|kappa| = 695 (weight 695/7371 = 0.094 ~ 2/23,
  polynomial as referee N11-F6(c) says) but max|r| = 4.2e-5, sum|r| = 6.0e-3 => |Y_mixed| = 4.1e-5 = 0.2% of |X| (0.0184). Polynomial kappa compensated by small |r|.
- iso mod 23 / unit mod 353 (2% sample): |Y_mixed| ~ 5.2e-4 (2.8% of |X|), weight <= 42/7371.
- Steering 00:02: N12 adapted norm (cond 21.06, N_H(t)<=1+3.19e3 t^2, K_stay ~1e2). 1 core shared -> d_mixed reniced to 19; new jobs nice 19, OMP=1.
- REPORT_N9b_v2 F2 updated: with adapted norm z<2e-4 needs L >= 9-11 (const 5.3) / 11-14 (const 111).
- launched f_D1preflight_H.py 300 0.125 (k-block norms in v~=Tv, closed 1/8 box) niced.

## 2026-11-01 00:08:09 +0500 — p=11 unit-unit sample; D1 pre-flight in v~; reports written
- d_mixed p=11 unit-unit (0.2% of 1.37e6 reps): Y ~ -2.0e-5, max|kappa| = 3.96 (<= 2^omega). Total p=11 |1+X+Y| ~ 1.0160 vs |1+X| 1.0165. [N, sampled]
- g_D1perorb_H: N12 operator reproduces a_per rates (1.2185, 1.2624). k-block norms in v~ along the 1.2624 orbit: k=8 1.31-1.41, k=16 1.33-1.38, k=48 1.27-1.30.
- f_D1preflight_H (300 random outside pts, closed 1/8 box): max g_k = 5.51/3.23/1.80/1.43/1.14/1.10 (k=1/2/4/8/12/16). => k-block D1 infeasible (needs k>=12); cone needed. Not launched (1 shared core).
- REPORT_N11b.md, REPORT_N9b_v2.md written. Next: hashes.
## 2026-11-01 00:08:09 +0500 — hashes: SHA256_N11b.txt (+.sha256); N9b/SHA256_N9b_v2.txt (+.sha256). Line closed. Nothing pushed.
