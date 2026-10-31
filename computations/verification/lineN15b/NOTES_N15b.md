# NOTES_N15b (Line N15b) — exponential-sum / dual-lattice route to sublattice equidistribution beyond separation time
## 2026-11-01 01:29:33 +0500 — start; time-box 60-90 min; plan: (1) pre-flight: ceiling of any equidistribution route that passes through the C' majorant; (2) subgroup sizes vs known theorems (BGK, Bourgain, Korobov, MVW); (3) cat-map literature (Kurlberg-Rudnick, Bourgain, Kelmer, FNDB, Bonechi-De Bievre).
## 2026-11-01 01:31:30 +0500 — majorant pre-flight
- sampled (a_majorant_ceiling.py) is unreliable (heavy tail); exact enumeration (b_majorant_exact.py) p=11:
  E_G F = 0.787, E_H23 = 0.264, E_H353 = 0.0521 (c_maj = -0.35, -0.46). Smooth-equidistribution heuristic M/N_b (=21 for G) is WRONG
  by 1.5 orders: digit measure W(b) is not smooth at target-lattice scale. Earlier 'ceiling c=0.899' heuristic withdrawn [N].
- p=13 exact launched (nice 19, background).
## 2026-11-01 01:39:51 +0500 — p=13 exact: E_G=0.994, E_H79=0.180, E_H599=0.0728 (c_maj=-0.39,-0.41). Majorant sublattice averages are BELOW the G average at p=11,13 [N]. Next: orbit sums c_orbitsums.py.
## 2026-11-01 01:41:05 +0500 — orbit sums + literature
- c_orbitsums.py: ord(lam mod q) = p; ord/log q = 1.76-6.0 (large factors ~1.8-2.4); log ord/log q = 0.25-0.41 (->0).
  max_a |sum_{i<ord} e(a L^i/q)|/ord = 0.50, 0.48, 0.59, 0.56, 0.54 for q=353,599,15607,424577,865087: NO o(ord) cancellation.
- literature checked: BGK (|H|>=q^delta), Bourgain (log|H| > C log q/loglog q), MVW conj (|H|/log q -> inf), Kowalski 2024 expo
  (even (log p)^C open); Kurlberg-Rudnick 2000, Bourgain GAFA LNM1910 2007 (ord>=N^eps), Bonechi-De Bievre CMP 2000 (equidist. only up
  to |log hbar|/gamma), Faure-Nonnenmacher-De Bievre CMP 239 (2003) (scars at minimal period ~2 log N/log lam). None applies.
- note: N14b (D) value c_D=0.899 is the beta=0 term of SUBGROUP averages; mixed sets remove it (inclusion-exclusion), so it is not a
  ceiling for mixed averages; p=11,13 exact majorant data give c_maj ~ -0.4.
## 2026-11-01 01:41:05 +0500 — REPORT_N15b.md written; manifest next (last action).
