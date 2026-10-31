# NOTES_N12b (Line N12b) — D1 cone-field certificate Gamma_out(1/8) < T' (closed box) with N12 adapted norm; NOTES_N10b timestamp fix
## 2026-11-01 00:10:53 +0500 — start
- Inputs: N12/adapted (T, H, P, Phi, psi, s; stepnorm table NG=4096; Lip_H=167.2; cond 21.06), N11b REPORT_N9b_v2 (gas form, z<2e-4).
- Plan: (0) N10b erratum; (1) pre-flight: sigma2/sigma1 of k-blocks in v~, derivative sizes -> required cell width; (2) certified cheap bounds (k=1 graph);
  (3) coarse cone pre-flight; (4) fine run only if (1)-(3) say feasible. All jobs nice 19, OMP=1, sequential.
## 2026-11-01 00:15:52 +0500 — N10b erratum done; a_blocks pre-flight [N]
- NOTES_N10b.md: headings relabelled with stat evidence (first code 23:03:25, last log 23:13:31, files 23:16:30) + ERRATUM; orig at logs/NOTES_N10b.orig.md;
  N10b/SHA256_N10b_v2.txt self-hash 92a8bd0e7736b417d21bcaa11b4841e6118508c8a0d82162b991c4c19425b164.
- a_blocks (150 random outside + periodic, closed 1/8): max rates MU*sigma1^{1/k}: 5.51/3.22/2.02/1.81 (k=1..4);
  MU*sigma2^{1/k}: 2.51/1.57/1.253/1.184.  => k=2 rank-one cones impossible (sigma2 rate 1.57 > T'); k=3 is the minimum (sigma2 1.253 < T').
  ||dP3/dy0|| <= 24.1, ||dP3/dy1|| <= 117.6 (median 7.0/39.4) -> cell width ~3e-4 for 10% of target (0.414) by derivative alone.
- Design: k=3 blocks, cell split v = a u_c + q (u_c = backward-iterated dominant direction, J=10), 2x2 nonneg edge bounds
  [[|alpha|, beta],[gamma, D]], D <= sigma1 sin(u',u_L) + sigma2; vector value iteration on the F^3 pseudo-orbit graph. Coarse non-rigorous pre-flight (centre values) first.
## 2026-11-01 00:22:24 +0500 — coarse cone pre-flight G=16; k=1 graph bound; steering (N11b referee, N12-F3)
- b_cone/b_cone2 G=16 (212 cells, mean out-degree 142 under F^3) [N, centre values, NOT rigorous]: Gamma_pf(2x2) = 2.067; alpha-only 1.197 (meaningless alone).
  Off-cone D rate median 1.49 / max 1.99: past-iterated u_{c'} at successor centres is misaligned with block output u_L (sin large) — the direction field
  varies along the STABLE direction at scale lambda^{-j}; coarse cells cannot carry it.
- c_graph1 (k=1 pseudo-orbit graph, N12 stepnorm table + add-on): 5.522 (G=64), 5.494 (G=256) ~ MU*max N_H. Per N12-F3 the table/Lip_H are [N] => this is [N], not certified.
- d_trivial [CA*]: t-uniform ||A(t)|| <= sum|w_n| ||M_n||_F = 57.22 (original 2-norm). Only rigorous D1-type bound in hand; useless.
- Steering 00:21: N11b referee READY after minor F1-F5 -> REPORT_N11b_v2 section in N12b at end; N12-F3: N12 constants are [N].
- b_cone2 G=32 running (CPU shared; slow), G=64 queued.
## 2026-11-01 00:34:34 +0500 — G=32, alignment, killed G=64, f_perL (min stay length) — decisive
- b_cone2 G=32 (852 cells, 181k edges) [N, centre values]: Gamma_pf(2x2) = 2.125 (G=16: 2.067) — no improvement with G; D-rate median 1.45.
- e_align (40 pts): sin(u(F^3 y + delta e_s), u_L(P3(y))): delta=0: med 0.179 (max 0.90); 1e-3: 0.53; 1e-4: 0.23; 1e-5: 0.178. Unstable-direction delta: no effect.
  => cone direction must be resolved to ~1e-5 along the stable direction; P3 to ~3e-4 along unstable => ~3e8 cells (x ~0.2 s each): infeasible (~4 orders).
- killed b_cone2 G=64 at 00:28 (only U phase done; no result; frees the shared core).
- f_perL (N9b a_per + box-run statistic, n<=7, Line-F op, closed 1/8 box) [N, lower bounds]: Gamma_per(1/8, L) = max rate over orbits whose box runs are < L:
  L=1: 1.2624, L=2: 1.3426, L=3: 1.4336 (> T'), L=4: 1.5117, L=5: 1.5683, L>=6: 1.6141.
  => D1 with minimum stay length L >= 3 is FALSE at theta=1/8; L<=2 makes fugacity z(L)/K = 0.83 (L=1), 0.26 (L=2) (K = C*C_theta per-stay constant).
  Rank-3p needs Gamma*e^z < T': K < 0.149 (L=1) / 0.234 (L=2) (upper limits). Rank-p needs z<2e-4: K < 2.4e-4 / 7.6e-4. G*_gas as stated cannot be met at theta=1/8.
- d_trivial [CA*] 57.22 is the only rigorous bound.
## 2026-11-01 00:35:27 +0500 — REPORT_N12b.md, REPORT_N11b_v2.md written; hashes next. Nothing pushed.
