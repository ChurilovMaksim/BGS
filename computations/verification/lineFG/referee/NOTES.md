# Audit Line F/G notes (referee). Start box clock $(date)
- plan: clone repo; read F code cert_lift.py, bounds_lift.py, LineF.lean; own recompute; then G.
Fri Oct 30 15:14:58 +05 2026
- 15:25 read F REPORT + cert_lift.py fully. Line-by-line: Galerkin exactness ok (M lower, C upper), block norm/trace bounds ok, row-sum (l2 of l1 rows) op-norm bound valid,
  delta1 (col CS) ok, delta2 = HS via Cauchy on 2rho ok, far analytic rows |c|>Rmax ok, Bessel tail |J_n|<=(x/2)^n/n! ok, edge |delta_E|<=1/(2lam) re-derived ok,
  Householder from midpoint vector -> exact unitary in ball: no float leakage; contour argument (two circles + P_out=I-P_in) valid; Weyl/Lidskii chain ok.
  bounds_lift: closed form 0.169*1.5197^m/m re-derived ok (h<lam^{m/2}/2). TODO: c_a=1/2 check, F_m def, mtimes vs fix, own recompute, Lean.
- 15:35 cert logs all start 13:05:15 = cert_lift.py mtime (runs launched right after final save; current code has no entry skip) -> all certs postdate fix. OK.
  Lean F reviewed (statement = adjacent-fixed-pair count; link to edge chains via edge_closed_iff). Lean builds launched -> logs/leanF.out, leanG.out.
  own float check: code/own_lift.py, check1.py -> logs/check1.log (running). Next: own_cert.py (independent arb cert).
  G issues so far: §3 'original R false for these kicks along all m' overclaim (full kick only conditional; k1 now via F); §8 contradicts §3;
  G7 'second moment of bulk ... CLT moment form is false' is float-based -> conditional; R' formula differs §0 vs §3 (RMT subtraction); G2 automaton exact via Line E X_ij=phi(|i-j|) (cyclic remark confusing).
  origin/main moved to e378ad11 (2 files, no claims change); last claim TRACE-196.
- 15:55 own float lift (own_lift/own_fast): sector4 top 1.9154732041 (matches); m=5 brute(L=8) rel 7.8e-7 (= brute truncation); check2 running (brute L=12 + physical finite-N table m=5..13).
  own_cert.py written; run_own.sh detached (V K0=4 rho1.1 K40 beta2 N50; then E) -> logs/own_V_eta2.*, own_E_eta2.*. V: delta 9.2e-7, Delta 1.8e-10, X 7.06, T 524.
  g_law.py: G2 law exact 1e-15 for |a|/b<=1 (m=5); large coupling = Galerkin ill-conditioning (as G says).
  ROUNDING VIOLATIONS in F (unsafe direction): W~rest/m>=8.07 (true 8.0695 -> 8.06), 68.9(68.87), 6.96e3(6956.6), 3.46e5(345923), F/2m 1.73e5(172963), 5.7e15(5.66e15);
  eta1.25 'F/2m>=2.928 from m=31' (true 2.92798), 0.144(0.1437), §5 mu lower 1.708751 (true 1.70875096; §3 has 1.708750 -> inconsistent); eta1.5 1.1(1.097),7.32(7.319), rate 1.3584(1.35836), 1.5198(1.51976);
  enclosure uppers rounded down: 1.9154752 (true 1.91547520413), 1.915475; T_V 730.1 in §5 table (730.142).
  L6 ~ L2 unitary via (U Phi)_c(s)=Phi_{-c}(-s) (verified on paper, V and E) -> eta=2.5 E sector 6 follows from sector 2 if lemma added.
- 16:10 OWN CERT V sector4 eta2 CERTIFIED: |mu*| in [1.91447320,1.91647321] simple (FR1 .146, FR2 1.9e-3), own T_V<=524.2 (rho=1.1). V sectors 0,2 + E running.
  check2: m=5 brute(L=12, own Hinv quadratic form + kappa=7) vs own full lift rel 3.8e-11. Physical finite-N table pending.
  Lean F: builds EXIT 0 (315 s), axioms std. G m=17 class sums at 160k/1.6M after 2.6h (~1 day) -> G m=17 test will not be available.
- 16:25 Lean G builds EXIT 0 (80 s), std axioms. (Lean G does not tie 1607521 to nsw 17 - nit.) Degli Esposti-Winn 2005 citation verified (N-dependent symmetries; s=1 for our S, so different mechanism) -> F should cite too.
  F code re-audited a 2nd time: no gaps found. Plan packets TRACE-197.. (F1,F2,F3,F4,F5,F6/F7 record; G law, G3, G5-7, R').
  Waiting: own V sectors 0,2; own E; check2 physical table.
- (resume 2) own V sectors 4,0,2 CERTIFIED (r2=1). own E running (T_E<=18.53, delta 5.5e-7, X .40). check2 physical: m5 rel 1.4e-13, m7 rel 2.0e-11 (table digits). Next: write REPORT.md F part now.
- REPORT.md F part checkpointed (placeholders EVAL_E, OWN_BOUND)
- REPORT G part + packets written; waiting own E 0,2 + check2
- own E certified; own bounds F15/2m>=6.654; REPORT complete (check2 m11,13 still running, pid 599729)
