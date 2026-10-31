# NOTES_N13b (Line N13b) — mixed classes at composite h_p without G*_gas: routes R1 (restricted pressure), R2 (arithmetic/averaged), R3 (reformulation)
## 2026-11-01 00:37:36 +0500 — start; pre-flight plan (~20 min): R1 periodic-orbit R3^out; R2 subgroup-average vs C' rate from existing p=11 data; R3 what TRACE-206 needs.
## 2026-11-01 00:43:11 +0500 — pre-flight findings so far
- R1 (a_press.py, Line-F op, n<=6, closed 1/8 box) [N]: R3 restricted to orbits with all box runs < L: L=1 0.74-0.78, L=2 0.95, L=3 1.07, L=4 1.15-1.23, L=5 1.29, all 1.40.
  BUT the slow fixed point alone gives exactly mu*^3/lam = 1.206 (= the threshold) per stay step, so long stays can never be absorbed by a pressure < 1.206;
  stays must again be separated (gas), and for mixed points the stays come from the iso component (length up to ~p). R1 reduces back to a stay-gas problem. Not closing.
- R2 (theory): C' (E_{G_p}|Z^|, Bowen-ball lemma over the full level-h lattice) with weight 2/q_u gives |Y_mixed| <= e^{o(p)} 4 h d (1.2744/mu*)^{3p}·(1/... ) — handles iso part d <= 1.4065^p only;
  for every composite h_p some mixed class has d >= sqrt(h) > 1.4065^p, so C' alone <=> h_p prime. Needed: subgroup lemma E_{H_d}|r| <= e^{o(p)} d^c (1.2744/mu*)^{3p} with c < 0.387 (H_d = iso-mod-d sublattice).
  p=11 data: E_{H_353} ~ 1.8 E_G (c ~ 0.10), E_{H_23} ~ 11 E_G (c ~ 0.76 but d=23 <= 1.4065^11=42.7 so trivial loss suffices).
- R3: (i) prime h_p (NSW primes: p=5,7,19,29,47,59,163,...) -> no mixed classes; infinitude = open conjecture. (ii) CS weights cannot kill mixed classes:
  any member weighting w has kappa_w(mixed) ~ -1/(q_u-1) relative (Fourier support argument) [P-sketch]. (iii) level-q_i switch: needs cross-level accounting (small levels) — open.
- Committing to R2: measure subgroup averages E_{H_d}|r| vs E_G|r| at p=11,13,17 by unbiased random sampling (b_subgroup.py).
## 2026-11-01 00:47:53 +0500 — R1 numbers final (n<=7); b_subgroup chain (re)launched
- a_press n=7: R3(L) = 0.745 (L=1), 0.950 (2), 1.077 (3), 1.153 (4), 1.217 (5), 1.324 (6), 1.4055 (all); R1 0.896, R2 1.0002.
  Threshold mu*^3/lam = 1.2061 is crossed between L=4 and L=5; the fixed point itself sits exactly at 1.2061 -> stays must be gas-separated (R1 not closing alone).
- first chain launch waited forever (pgrep matched its own command line) — killed and relaunched directly at the time above.
- R2 theory note: naive 'coarser-separated sublattice' Bowen argument gives c = log(sup g/avg g)/log lam = log(1/0.2945)/1.7627 = 0.694 > 0.387 (fails);
  needed: genuine equidistribution on the iso sublattice (= N3 §4 item 1 'beyond-Ehrenfest').
## 2026-11-01 01:17:53 +0500 — R2 sampling done; R3(iii) level-q test; steering (N12b referee) absorbed
- b_subgroup (1500 unbiased samples per set; heavy-tailed, means dominated by single maxima) [N]:
  p=11 (23*353): E_G 9.57e-9; E_H23 1.50e-8 (c 0.14); E_H353 4.60e-8 (c 0.27; exact all-points mean 1.76e-8 -> c 0.11).
  p=13 (79*599): E_G 1.26e-9; E_H79 1.60e-9 (c 0.06); E_H599 1.69e-10 (c -0.31).
  p=17 (103*15607): E_G 1.88e-14; E_H103 4.83e-13 (c 0.70, one outlier 2.6e-10; d=103 <= 1.4065^17=330 so trivial index loss suffices); E_H15607 1.38e-13 (c 0.21).
  E_G / C'-rate (0.2945^p): 6.6e-3, 1.0e-2, 2.0e-5. Mixed bound 8h E_H: p=11 3.0e-3, p=13 6.1e-4, p=17 6.2e-6 (vs |X| 0.018, 0.022, ~0.026): decaying ~e^{-0.8p} here.
- c_levelq p=11 q=353 (exact, all 124609 points): X_q = -4.4e-7 + 3.9e-7 i (NO gas at a proper prime level), |1+X_q+Y_q| = 1.0000053. => level switch R3(iii) dead.
- Steering 00:56: N12b referee — add REPORT_N12b_v2 (theta-robustness, K at Gamma~T', K=C^2 C_theta, 'K>~1' [N/heuristic]); witness-orbit arb certification optional (not done).
## 2026-11-01 01:17:53 +0500 — REPORT_N13b.md (+ REPORT_N12b_v2 section) written; hashes. Nothing pushed.
