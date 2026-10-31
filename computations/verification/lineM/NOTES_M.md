# NOTES_M (Line M, fresh-eyes search for a new route). Resumption notes.
- 15:13 start. Read claims 206,232,235-247, L/L2/L3 reports, Line G note.
- Key reformulation used: W'_m = (1/phi)[sum_nonres(|Z|^2-RMT) + sum_{rho,d incl} (cross_d + square_d)];
  cross at prime q = 2Re(conj Z_rho (D_iso - E_b/q)) (K1). Everything reduces to linear functional D_iso at open levels.
- Plan: evaluate (i)-(v) + own ideas; prove small [P] lemmas making negatives crisp; numerics for capacities.
- ~16:00 Evaluated (i)-(v). All reduce to the linear functional D_iso-E_b/q at open levels (cross part). Key new [P] facts:
  M1 strong divisibility -> open conductors of distinct m=3p disjoint (logs/m_checks.log, 0 failures m,n<=301).
  M2 averaging: positive-weight averaged H-nat => H-nat (delta/2); signed weights lose positivity of square/bulk. So (i) is no easier.
  M3 inherited level h_p is open for every p and has positivity capacity >= c*1.13288^m >> 1.0184^m (code/m_checks.py).
  M4 frozen inclusion rule = {d|h, 1<d<=sqrt h} for (+-2,8) from m>=11 (|Z|>=mu^m/2); no family overlaps (3 not| h_m). (iii) no artifact.
  M5 fiber quadratic minimisation: squares offset a cross deficit X only if q >~ |Z|^2/X ~ L_m: positivity threshold sharp. (iv) dead.
  M6 rho<->-rho antiunitary RK: sectors 2,6 cancel at EVERY conductor (generalises J 1:3); sectors 0,4 survive -> no exact vanishing of O-nat.
  M7 KR/Bourgain: every open conductor has ord <= 3p; h_p has ord p = 2log_lambda h_p + O(1) (FND minimal period); density-one theorems never apply.
  Quantum dictionary [H]: Theorem U = operator Parseval; D_q = block-trace deviation of a rank h/q projector compression.
- Verdict: crisp negative. Writing REPORT_M.md.
- 15:40 REPORT_M.md written (M1-M7 + (e) Gram form). M6 downgraded to P-sketch. Done unless new idea.
- 15:55 v2: REPORT_M_v2.md (M-F1..F12), m_checks_v2/m_incl_v2 run+logged, referee Lean copied & compiled (exit 0).
