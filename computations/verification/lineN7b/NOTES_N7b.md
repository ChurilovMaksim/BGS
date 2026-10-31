# NOTES_N7b (Line N7b: gap (b) of Omega#) — times Asia/Yekaterinburg (UTC+5). Do NOT push. N2–N7 read-only.
Labels [P] proved, [CA] arb, [N] numerics, [H] heuristic.
## 21:10 start. Read REPORT_N, N2v3, N3v2, N4, N5v2, N6, NOTES_N6, audit N5/N6, REPORT_L_v2, NOTES_N7 (gap (a) author).
- From NOTES_N7 21:10: (+-2,16) removed from Omega# at ALL levels (|Z16|<=C16*1.6355^m [CA], floor + sigma(h)/h). So gap (b) = (+-2,8) only.
- Plan: (A) conductor decomposition of Lin at non-h_p levels; (B) block-split Bowen bound (2 HS blocks of length n=log_lam(c^2/g), op on rest)
  -> criterion c^2/g >= lam^{kappa p}; (C) 8E by sup bound (Lambda_8E=0.4916<1.42785) at all levels; (D) Theorem W at relaxed target
  (recompute c_W); (E) divisor-window / subsequence analysis + heuristics; (F) numerics at non-h_p levels (p=5..13).
## 21:25 (D) Theorem W at relaxed target [CA] (code/w_relaxed.py = Line L l4_const.py with target mu*_lo lam^{-1/6}; logs/w_relaxed_8V.jsonl)
- 8V (rho .75, beta .25): OP certified for k>=10 (k=9 rate 1.45098 > 1.42785). log10 c_k: k10 -18.62 (q0 1e9.3), k11 -18.95, k12 -19.71, k15 -22.53.
  => c_W improves 10^-25.62 -> 10^-18.62 (8V binding; 8E not needed: sup bound). Non-vacuous p >~ 10^18.9 (was 10^25.9). Scan rho/beta for k=9,10 running.
- Factorisations p<=37 (sympy): h_p prime p=5,7,19,29; K_p/7: p=7 4663 (and 7^2), p=11 prime, p=13 313*4088137, p=19 457*14593*7521721, p=23 prime ...
## 21:45 (B) Prop B1 constants [CA] (code/b1_const.py -> logs/b1_const.out)
- Block split: |Tr(X1X2X3X4)| <= ||X1||_HS ||X2||_op ||X3||_HS ||X4||_op; HS blocks of length n, op rest; lattice Bowen lemma with
  points-per-(n,eps)-ball <= C(1+eps^2 lam^-n c^2/N(a)) (norm-form count); weight/N(a) <= 2^omega.  => pattern (c,a) with iota=c^2/N(a):
  handled iff iota >= lam^{(kappa+eta)p}, kappa_8V <= 0.737592 [CA].  Units: c >= lam^{0.36880 p}; c|h_p: log_lam(h_p/c) < 0.13120 p
  (vs 0.09677 p for Theorem C + index loss at relaxed target, 0.0061 p at old target).  8E: sup bound 0.4916 < 1.42785 at ALL levels/patterns.
- Barrier [P, for the majorant]: any (points-per-Bowen-ball x Lebesgue integral) bound >= mu*^m/iota => needs iota > lam^{p/2}.
  Fully isotropic pattern at c has iota = c <= L* ~ h_p e^{o(p)} < lam^{p/2} e^{o(p)}: below barrier. Units: barrier c >= lam^{p/4}.
- Floor refinements [P]: level d absorbed alone iff d >= ~860 h_p/(delta p) (2 n_d|Z8|^2/d^2 vs F_m >= 2.33e-3 p|Z8|^2/h_p).
  => 7h_p costs <= 122.6/p of F_m (<=10.5% at p=1165): can be floored; all h_p*e (e|K_p, e>=6p+1) cost <= 143/p^2 F_m each.
  Proper divisors of h_p never floorable (factor >= 1720).
## 21:50 (D) relaxed W final: best (k,rho,beta)=(10,0.75,0.25): c_W' = 10^-18.62, q0=10^9.3 (scan logs/w_relaxed_8V_scan.jsonl no better).
  => eps_F' = 2 sqrt(c_W') = 10^-9.01; W+ (3,3): c_N' = eps'^9/17.31 = 10^-82.3; crossover p > 10^191 (was 10^264.5); Cochrane-Pinner iso 10^-73.5 p^3.
## 21:55 (F) numerics running: b_levels p=5,7,11,13,19 (all conductors <= sqrt h_m, patterns, sampled units); e_iso exact iso lines p=19,29,37,41;
  d_slow (slow time near z4, eps=1/16, p<=80, Q<=3e6): s_max/log_lam c <= ~2 (iso) , unit s_max/(2 log_lam c) <= 2.01; windows grow with rank
  (random short visits ~ r*4eps^2). Consistent with [H] S(c): slow time = O(log c) + O(r eps^2).
- c_prp_census p<=4000 running (h_p and K'=K_p/7 BPSW).
## 22:10 census done (logs/c_prp_census_4000.jsonl, p<=3989, 548 primes): h_p PRP at p=5,7,19,29,47,59,163,257,421,937,947,1493,1901 (13; heuristic 14.8);
  K'=K_p/7 PRP at 7,11,23,83,97,127,197,283,859,1913,3931 (11; heur. 9.1); BOTH only p=7 (heur. 2.2, convergent sum ~ (log p/p)^2).
- e_iso exact (logs/e_iso.jsonl): rank-3p primes Q: p19 Q457 rel_abs 1.0e-11, Q14593 7.5e-11; p29 Q13921 2.0e-17; p37 Q223(h) 3.4e-23, Q6217 3.8e-23;
  p41 Q2297(h) 3.1e-21, Q9103 4.1e-26.  max per-point rate |Zhat|^{1/m} 0.87-0.97 (target 1.42785).  Matches referee N5 (d=457 2e-11, 14593 -5e-11).
- correction: 7h_p floor cost ratio = (12/49)/(2.330e-3 p) = 105/p (not 122.6/p). single-level floor threshold d >= 858 h_p/(delta' p).
- [P] reformulation of slow time: visits of y (level c) to the eps-box of z4 <-> elements gamma in the coset alpha_y<eps> mod 2sqrt2 c O lying in the box
  |gamma|,|gamma'| <= 8c eps; window length ~ log_lam(64 c^2 eps^2/|N gamma|). Units gamma=eps^k form ONE window. Deep windows <-> small norms in a
  multiplicative coset of size 2r in (O/2sqrt2 c)^*  (BGK-type question; random model gives r*O(eps^2) shallow visits, matches d_slow).

## 22:30 — finalisation
- b_levels p=19 complete (54 rows, json written). Max rel 7.17e-9 at c=24061985479, pattern [457], rate_max 1.014 — matches REPORT table (7.2e-9 / 1.02). No new maxima.
- REPORT_N7b.md final. SHA256_N7b.txt manifest over code/, logs/, NOTES, REPORT generated; self-hash in SHA256_N7b.txt.sha256. Nothing pushed.
