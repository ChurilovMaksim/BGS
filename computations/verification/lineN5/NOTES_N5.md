# NOTES_N5 (Line N5) — times Asia/Yekaterinburg (UTC+5). N2–N4 files read only.

## 19:45 start. Plan: fast-half matrix element of the 16D=1 family; 7 h_p unit points; reassessment.
- code/a_model.py: Line F lift model of Zhat (V-E trace, sector-0 weights x e(n tau)); at (21,239) top point = 2.0 x TRACE-206 |Zhat|; other points differ (other sectors/families) -> use the true law instead.
- code/b_family.py: dominant family for h_p prime, p = 5,7,19,29,47,59 (h_p prime for p in {3,5,7,19,29,47,59,163,257} below 400).
  FINDING: twists stay within 0.05 of 1/2 for p-5 of p steps (not p/2). Two slow windows per period + two O(1) excursions.
- [P] half-period identity: for any delta with 4 q delta in O and q | h_p: eps^p delta == eps^-p delta (mod O^dual) (eps^p = 2 h_p - eps'^p, 2 h_p delta in (1/2)O ⊂ O^dual). => second window at i = (p+1)/2.
- code/c_true.py (TRUE TRACE-206 law, L2 twlaw L=8 K=32): validated p=5 (2.872), p=7 (172.740). Family rate: 1.0193 (5), 1.1535 (7), 1.3427 (19), 1.3782 (29), 1.4018 (47), 1.4089 (59), 1.4239 (163), 1.4262 (257) > T for p >= 19. Zhat/Zrho -> c* = 3.954525469821e-4 (10 digits by p=29). sign -1 identical.
- code/d_excursion.py: Zhat = (rA rB)^3 Zhat(all 1/2), Zhat(all 1/2) = Zhat(0); |rA| = 0.242977, |rB| = 0.302087; prediction matches to 1e-14.
  Excursion deviations: A: +-(2-sqrt2)/4 lam^-k (antisymmetric), B: -(sqrt2/4) lam^-|k| (symmetric).
- code/e_composite.py: composite squarefree h_p (p = 11,13,17,23,31,37,41,43): the fully isotropic depth-1 family at level h_p (one ideal of norm h_p out of 2^omega) has the same ratio c*, rate 1.2859 (11) ... 1.4135 (43) > T.
- Limit rate mu* lam^{-1/6} = 1.42775.  Cross part ~ 8p c* |Zrho|^2/h_p, rate ~ 2.7348 > xi_lo = 2.4587. Re((rA rB)^3) < 0 (arg = pi + 0.52).
- N4 §3 correction: window is p - O(1), not p/2; the N4 'G <= 1.547' target and remainder rates are moot.
- 7 h_p unit points: [P mod Theorem C inputs] via coset measure nu = uniform on the T-orbit of (y7 + G_p) (T-invariant), Lambda = sup over T^2 already covers y7 + y_p, collision majorant unchanged (phases e(<alpha,y7>) of modulus 1, nonnegative coefficients); 7-part unit weights <= 36 * 2/49 < 2; 7 || h_{3p} for p != 7.
