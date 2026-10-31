# NOTES_N4 (Line N4) — running notes; times Asia/Yekaterinburg (UTC+5)

## Setup (18:05)
- Box: nproc 2, 16 GB; load varied 4–34 (other users' jobs). Policy: at most 2 worker processes, nice 5.
- python-flint was not present in any interpreter at 18:10 (seems removed since N3); reinstalled python-flint 0.9.0 into /workspace/bgs-lineN/.venv.
- N3 files untouched (read-only use of N3/logs/g_R_V_final.npy and N3 code as templates).

## (A) probe for 8V [N] (code/a_probe.py, logs/a_probe.out)
- Lip (spectral) 274.70, (Frobenius) 339.70; L2 = sum (2 pi n)^2 ||C_n||_2 = 9216; ||C_n|| ~ 3e-9 at |n|=21.
- ||Y(tau)||_2 peak 1.9233 at 1/2; <= 1.75 outside [0.32,0.68]; ||Y'|| 42–58.

## (B16) (+-2,16) families (18:15–)
- KEY observation [P]: every one of the 16 distinct 2x2 block actions (J3 blocks16_exact.json) has the SAME permutation pattern: identity for n even, swap for n odd.
  The phase-blind entrywise majorant M = sum_n |J_n| |B_n| (x) P_n therefore dominates |A_{B,tau}| for all tau, all blocks B, both signs of a.
- Float Perron root of M [N]: 16V 2.94139 (independent of rho, beta: tried (1.2,2.5),(0.9,0.3),(0.6,2.5)); 16E 0.44744.  Thresholds 3.04126 / 3.04280.
- Schur test with D = diag(sqrt(x/y)) turns the Perron root into a NORM bound ||D^-1 A D|| <= sqrt(alpha beta). Code: code/b16_schur.py (arb).
- Error terms with |C| = c0/2: code/cert_lift16.py (copy of Line F cert_lift with cc -> c0/2) [CA]:
  - V (K0 4, rho 1.2, K 55, beta 2.5, Nmax 60, Rmax 40): delta1 5.74e-13, delta2 3.28e-15, Delta 8.91e-16, ||X|| 0.9526.
  - E (K0 4, rho 0.8, K 40, beta 2.5): delta1 2.1e-23, delta2 5.30e-12, Delta 1.25e-17, ||X|| 0.1063.
  - Tensor with the 2-dim internal factor: HS-type abs-majorant bounds inflate by <= sqrt 2 (each letter fills 2 of the 4 internal entries).
- Lemma I analogue: O1 spaces 16V (0.9,0.3), 16E (0.2,0.3); F spaces (1.2,2.5)/(0.8,2.5): theta(V,O1->F)=0.784, theta(V,F->O1)=0.510, exponent -0.3+2.5/lam^2=-0.226; E as 8E. Internal factor unitary (f1,f2 orthogonal, equal norms: J3 exact).
- Relevance note: Line L §5(b) already absorbs (+-2,16) levels q >= 1.1311^{m(1+eta)}; h_p ~ 1.342^m is above that for p large, so at q = h_p the 16-family Lambda is not needed; it matters for Theorem C at smaller levels.

## (B16) results (18:16) [CA]
- code/b16_schur.py (arb Schur test) both permutation patterns PAR=0/1: 16V f_core <= 2.9413896 (alpha 2.9413889, beta 2.9413903, cond D 1.03e4); 16E f_core <= 0.4474392 (cond 1.2e4).
- code/b16_final.py: error terms x2 for the tensor (even/odd letter split = averages of +-1 phase twists) -> penalties 3.9e-8 (V), 3.8e-7 (E).
  Lambda_free^{16V} <= 2.9413896 < 3.04126 (margin 3.3%);  Lambda_free^{16E} <= 0.4474396 < 3.04280.  Unit-point rates (Lambda r2)^{1/3}: 1.45788 (V) < 1.4742, 0.77811 (E).
- Bonus: same Schur test for 8E (FAM=8): f_core 0.4915878, penalty 5.3e-6 -> Lambda_free^{8E} <= 0.4915932 [CA] (logs/b8E_final.json) — replaces the N3 [CA*] 1.660338. For 8V the phase-blind bound is 3.932 (useless), so 8V needs the cell scheme.

## (B) 8V arb cells (started 18:17): code/b_arb_cert.py V ... NC0=400 ftarget 1.9657, 2 workers, prec 80. 8E cell run (identity norm) was started and stopped after ~20 cells (all n0 = 1.63660 flat in tau; partial logs kept as logs/b8E_partial_w*.jsonl) because the Schur certificate supersedes it.

## (C) isotropic slow orbits (18:20–)
- Gauge lemma [P]: for L_tau Phi(s) = sum_n w(n) e(nτ) e(c n s) Phi((s+n)/lam) on functions on (a neighbourhood of) R:
  L_tau T_sigma = T_{lam sigma} L_{tau - c lam sigma} (translation),  L_tau G_nu = G_{nu/lam} L_{tau+nu/lam} (modulation e(nu s)).
  Hence for a REAL two-sided geometric twist tau_i = t0 + a lam^i + b lam^-i:  prod_{i<n} L_{tau_i} = T G L_{t0}^n G' T'  exactly (gauges explicit).
- Isotropic twists: tau_i = Tr(lam^i y) is literally real two-sided geometric. Slow orbits = y near the fixed point z4 = 1/4 of the dual torus (Tr(lam^i/4) = 1/2 mod 1: sector 4).
  delta = y - 1/4, sector-4 depth D = q min|N(delta + O^dual)|; window ~ log_lam(eps^2 q/D); 16D integer.
- [N] (code/c_depth4.py): (21,239): 16D=1 family has 2p=14 points per line, 88.9% of |iso|, |Zhat|=172.74; (15,41): 2p=10 points, 62.0%.  16D=1 <=> 4beta - q = prime generator of the ideal (explicit family).
- Sector-4 spectrum at tau=0 [N] (code/c_mu2.py): |mu_1| = 1.91547, |mu_2| = 0.72778 (Line F certV sector-4 'Yp_root' 0.76905 is the certified complement bound). Other sectors < 1.

## 18:35 referee N3 report received (READY-after-fixes N3-F1..F11)
- N4 cell scheme already satisfies F7 (arb ||R||_F, arb twiddles, exact rational labels). F6 stated in REPORT_N4 §5. F8: squarefree hypothesis + d_squarefree.py (no q^2 | h_p for q<3e6, p<=1e5; 2750 pairs). F9: 7 h_p unit points P-sketch.
- Wrote N2/REPORT_N2_v3.md (3 residuals) and N3/REPORT_N3_v2.md (F1..F11). Originals untouched.

## 19:39 8V [CA] finished
- 442 cells (400 + 42 bisections; 77 spectral X'), exact coverage OK; max cell 1.9656276; penalty 7.7e-6 (||R||_F 35.87, ||R^-1|| <= 26.22, kappa 4036).
- Lambda_free^{8V} <= 1.9656353 [CA] (logs/b8V_final.json); rate 1.27438.
- Item (3) rates recomputed with mu* upper 1.916473 and Lambda 1.9656353: remainder j=1 1.2426, j=2 1.0672, j=3 0.9165; leading worst-case 1.4468; G threshold 1.547.
- REPORT_N4.md complete; N2/REPORT_N2_v3.md and N3/REPORT_N3_v2.md final (N3 v2 cites the 8V [CA] value). SHA256_N4.txt written.
