# NOTES_L (Line L)
- 12:27 Started. Goal: OP certification for true k1 operators; open-range attack (a)-(d).
- 13:05 KEY FINDINGS so far:
  (U) Scalar L2-unitarity [P]: R(v)=sum_n w(n)conj w(n-v) = e(nu0 P(v)/2h) prod_j kappa(v_j,theta_j), theta_j = nu0 y' Tr(lam^-j alpha_v)/(2h);
      exact collisions (alpha_v=0) and alpha_v in hO give R(v)=0 for v!=0 (since sum_a ghat(a)conj ghat(a-d)=delta_d). Hence
      sum_{x in O}|A(x)|^2 = 1 and sum_{c in O/h}|A(c)|^2 = 1 (i.e. sum_{beta mod h}|Zhat(beta/h)|^2 = h^2). Checked m=5 (logs/l1_unit_m5_L4.log).
  (OPabs) BIG: OP provable WITHOUT cancellation: I_k <= sum over exact-collision pairs of ||M_w||_HS ||M_w'||_HS; lattice word HS
      norm <= |Phihat_w| * exp(2 pi C0 rho sum|n_j| lam^-j) * HS(C_psi) * weights -> product form; collision sum = carry automaton with
      weights rho(d)=sum_a|J_a||J_{a-d}|: spectral radius r_abs = 1.0511158 (EMAX 2..8 converged, logs/l2_rabs.log). r_abs^(1/2)=1.0252 << 1.28359.
      => OP for TRUE operators (any representation; only end constants). Next: rigorous CA bound on r_abs (Perron vector + tails),
      constants C_I, A_k ~ G^{2k} (G=2.3694), explicit k, c_k, p0.
  Open range: N=2 segment-Hoelder with r_abs gives only q >~ lam^{m/4} (=sqrt h): useless. Large sieve fails by (2.414/1.2836)^m.
- 14:10 l3 scan (logs/l3_scan.jsonl, E0=6,t=2): OP CERTIFIED at k=24 for all four families (rate I_k^{1/2k} upper):
    8V 1.1700 (rho .7 b .2), 8E 1.0888 (rho .2 b .4), 16V 1.2273 (rho .8 b .2), 16E 1.1786 (rho .3 b .4); k=30 even better.
    k=40 worse only because chernoff tail (E0=6) blows up -> need larger E0 for big k (irrelevant: small k preferred for c_k).
  Next: l4_const.py: eta (max, delta->small), c_k=(eta/6A_k)^2, T_k(q) chernoff with a=lam^{-k/2}, q0, p_eff=max(q0/2, 2/c_k); scan small k.
- 14:35 l4_const.py (A_k, eta, c_k, T_k chernoff, q0) works. 8V rho.7 b.2: k=16 log10 c_k=-26.4, q0=1e14; k=24 c_k=1e-35.
  OP fails at k<=14 for 8V (k=14 rate 1.2858), passes k=15 (1.2657, b=.3). Smaller k => better c_k (A_k~G^{2k}).
  Scan running: logs/l4_scan.jsonl (code/l4_scan.sh, k 14..20, all 4 families). Then pick common k, c_k=min.
  p_eff (Weil range nonvacuous) = 2/c_k ~ 1e26 vs old 1e800.
- 15:05 FINAL CONSTANTS (logs/final_constants.jsonl, final_op_cert.jsonl): per-family k allowed (W2' per family).
   8V k15 rho.75 b.25: rate<=1.26278 (<1.28359), A_k<=1.74e14, eta=162.8, c=10^-25.62, q0=10^13.2   <- binding
   8E k14 rho.2 b.3: 1.13642, c=10^-20.93; 16V k14 rho.9 b.3: 1.39243 (<1.4742), c=10^-22.53; 16E k14: 1.30276, c=10^-20.84
   => c_W = 10^-25.62, p0 = 10^13.2/2 , nonvacuous from p >= 2/c ~ 8.2e25.  Writing REPORT_L.md next.
- 15:30 REPORT_L.md written; manifest via make_manifest.sh
- resume: REPORT_L_v2 cites PR #63 W2' errata; manifest regenerated.
