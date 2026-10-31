# NOTES_N16b (Line N16b)
## 2026-11-01 01:42:04 +0500 — start: (1) N14 §3 second-moment requirement vs c_B; (2) exact mixed-class majorant averages p=17,19,23; (3) THEOREM_DRAFT.md.
## 2026-11-01 01:44:23 +0500 — a_mixed_majorant.py exact p=11,13 (sublattice enumeration, one ideal): E_M/W0 = 0.174 (q=23), 0.0337 (353), 0.106 (79), 0.0426 (599); c_coll -0.56,-0.58,-0.51,-0.49. Launching p=17 q=15607 exact, then samples p=17 q=103, p=23 q=47, q=6771937 (nice 19, sequential).
## 2026-11-01 01:50:23 +0500 — results (2) + analysis (1)
- p=17 q=15607 EXACT (1.62e8 pts, 49 s): E_M=0.04415, E_M/W0=0.0212, c_coll=-0.40.
- p=17 q=103 SAMPLED 2.2e7: E_M/W0=0.065 (c=-0.59) — max single term = 19% of sum (tail not converged) [N, caveat]. exact would need ~2.5e10 pts (~2 h): not run.
- p=19: h_19=9369319 prime -> no mixed classes (trivial case confirmed, sympy isprime).
- p=23 SAMPLED 2.1-2.2e7: q=6771937 E_M/W0=2.05e-3 (c=-0.39); q=47 E_M/W0=4.55e-3 (c=-1.40); max term 32-34% of sum [N, caveat].
- (1) N14 §3: c_B (first moment vs C' rate) is a different object; not transferable. Second-moment: positivity gives c=0 if per-point weights are not d-amplified (S subset of Parseval-exact group);
  with d-amplified weights (N13b bookkeeping) trivial c=1 on the final activity. Lemma-2 analogue with Nsum<=8.33 [CA] is worse than trivial.
  Units: 0.380 per lambda-step => condition c*ln d < 0.967*l0, i.e. c < 0.549*l0/log_lam d (N14 wrote 0.97*l0/log_lam d: factor ln(lam)=1.763 slip unless log is natural).
## 2026-11-01 01:52:09 +0500 — REPORT_N16b.md + ../THEOREM_DRAFT.md written; manifest next (last action).
