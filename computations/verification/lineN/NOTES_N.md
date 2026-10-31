# NOTES_N (Line N resumption notes) — 31 Oct 2026 (UTC+5)
Task: can BGK/Bourgain/explicit sum-product bounds replace Weil in Theorem W (Line L) for open levels c_W p^2 < q <= p^C; what stays open.
## State
- Reduction (K2 §2 W1/W3, verified): needed object = S(x) = (1/tau) sum_{h in H} e((A h + B/h)/q), H=<lam mod q>, A=sigma(x), B=sigma-bar(x);
  no polynomial phases survive (chirp/sector phases unimodular, dropped by OP_abs). Budget per level is an m-independent constant eps_F.
- Found: Ostafe–Shparlinski–Voloch IMRN 2023 (arXiv 2110.10941) Cor 2.9 / Thm 2.7: Kloosterman sums over subgroups << tau^{20/27} p^{1/9}
  (nontrivial tau > p^{3/7}). K2 §3 claim "explicit literature does not beat Weil for binomial" is superseded.
- Made explicit (code/n2_constants.py): |S|^{2kl} <= q^2 tau^{2kl-2k-2l} J_k J_l (elementary, a1 a2 != 0), J_2 <= 2tau^2 - tau (tau odd),
  J_3 <= 4*3^{4/3}(q tau/(q-1))^{2/3} tau^3 + 3 tau^5 q/(q-1)^2 + 12 tau^3 (Voloch+Weil point count, OSV Lemma 4.3 abs. irreducibility).
  => q <= c_N p^{7/3}, c_N = 10^{-113.80} (Line-L budget convention) ; beats Weil only for p >= 10^{264.5}.
- Isotropic (linear) sums: Cochrane–Pinner Thm 1.1: |sum_{x in A} e_p(ax)| <= 1.51967 |A|^{5/8} p^{1/8} -> q <= 10^{-101.5} p^3.
- Bourgain JAMS 2005 Cor (1.21): any C, ineffective-in-practice delta; covers prime q <= p^C.
- KEY NEW [P]: Theorem N3 — every conductor c with log_lam c >= theta_F r/2 + t_F (r=ord_c lam) carries slow beta=1 (orbit points
  lam^n/c near 0 for |n| < log_lam c - t). In particular c = h_p always (r=p, log_lam h_p = p/2-O(1)). So K2'-type
  "no slow orbit" can never be established; K2' conclusion is unconditionally true. [N] toy: logs/n5_slow_toy.log (beta=1 rate 1.43-1.71 > 1.284).
## Files
code/n1_factor.py (PARI factorisation of h_p, K_p) logs/n1_factor_*.jsonl ; code/n2_constants.py ; code/n3_check.py (FFT check of J_2,J_3,|S|)
code/n5_slow_toy.py ; code/n4_summary.py (bands) ; literature pdf/txt in logs/ (osv2110, wss2211, mss1701, cp).
## Status: DONE (REPORT_N.md written 31 Oct 2026). Possible follow-ups: weighted K2′; pressure bound at h_p (N4); read Bourgain JAM 101 for composites.
