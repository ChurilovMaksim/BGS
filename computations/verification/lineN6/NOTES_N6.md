# NOTES_N6 (Line N6) — times Asia/Yekaterinburg (UTC+5). N2–N5 read only. Do not push.
## 19:58 start
Tasks: (1) Prop X -> [P] with explicit error; arb [CA] for c* and arg; (2) full signed aliased contribution over all included d with h_p | d (+ 7h_p iso),
vs frozen main term, xi_lo^m, D7; (3) if not cancelled: precise refutation requirements + attempt.
Key bookkeeping (from TRACE-206/213 + I2'/G3): members of level d: Z_t = (G_d(t)/d^2) sum_beta e(tbar Nm beta/d) Zhat(beta), t over units mod d, n_d = phi(d).
 => Dev_d = d^-2 sum_{u,u'} A_u conj(A_u') c_d(u-u') - phi(d)|Z_rho|^2/d^2,  A_u = sum_{Nm beta = u} Zhat(beta)  (c_d Ramanujan sum).
 Linear (cross) part: (2/d^2) Re( conj(Z_rho) sum_{beta!=0} c_d(Nm beta) Zhat(beta) ).  Fully isotropic beta carry c_d(0)=phi(d) (same weight as the main term).
 => relative to the frozen level main term phi(d)|Z_rho|^2/d^2 the aliased family enters as 2 Re X_d (+|X_d|^2 ...), X_d = sum_{beta!=0} c_d(Nm beta) Zhat(beta) / (phi(d) Z_rho).
 The frozen main term (Res_m) uses |Z_rho|^2/d^2 only; the aliased family is NOT in it (it sits in Dev_d, i.e. in W'_m).
## 20:05 SIGN CORRECTION (N5 error)
- [N] Zhat(all 1/2) = -Z_rho (complex, not just modulus; m = 3p odd). So the family ratio is -(rA rB)^3 = +3.435779e-4 + 1.957981e-4 i
  (sg=+1; conjugate for sg=-1), arg = +0.5180, Re > 0.  N5 §0/§2/§4 statement "Re < 0 (arg = pi+0.52)" is WRONG (forgot the -1). (logs/g_sign_s*.json)
- sector-0 beta = gamma (|N gamma| = q) has ratio only 2e-9 (not a strong family).
## 20:05 full isotropic sums X_{h_p} (logs/f_iso_p*_K16_s1.json)
- p=5: X = 0.003533+0.002496i; p=7: 0.010724+0.005761i; p=11 (8119=23*353): 0.016493+0.008231i, dominated by the 1/2-family (44 pts, 3.4358e-4+1.9604e-4i each)
  plus a near-0 family (44 pts, 2.98e-5-6.6e-6i each); everything else < 1e-4 relative.  2ReX+|X|^2 > 0 in all cases.
## 20:10 POSITIVITY LEMMA [P] (key structural point)
- members of level d: t in S_d (units, minus those giving non-unit nu); |Z_t|^2 = d^-2 |Z_rho + E_t|^2, E_t = sum_{beta!=0} e(tbar Nm beta/d) Zhat(beta) (I2'/G3, TRACE-212/204).
- Dev_d(rho) = d^-2 sum_{t in S_d} (2Re(conj Z_rho E_t) + |E_t|^2) >= Lin_d(rho) := (2/d^2) Re(conj Z_rho sum_{beta!=0} kappa_d(Nm beta) Zhat(beta)), kappa_d(u)=sum_{t in S_d} e(tbar u/d).
- non-resonant units: |Z_nu|^2 - RMT >= -RMT.  => W'_m >= -RMT_m + phi^-1 sum_{rho, d incl} Lin_d(rho)   (exact lower bound; bulk and all squares dropped).
- So a refutation needs only: the linear parts sum to >= (4+delta) m phi infinitely often. The aliased family at levels with h_p | d gives a POSITIVE linear part
  ~ (2(d-2)/d^2)|Z_rho|^2 * 2Re X per rho, rate (mu*^2 lam^-1/6)^m * p after phi^-1 ~ p*1.1329^m.  New per-level threshold for the rest: 1.42775 (was 1.28359).
## 20:40 p=13 full (3614 orbits): X = 0.019429+0.009762i; p=19 screened (thr 9/19, 2733 orbits): X = 0.028554+0.014250i.
- families: 1/2-family 4p pts x (3.43578e-4+1.958e-4i); near-0 family 4p pts x (2.987e-5-6.60e-6i) (stable p=11..19); rest <= 0.6%.
- exact level-h_p Dev (all d^2 beta, G3 members): p=5: Dev/main 0.153, Lin/main 0.029, Lin_iso/main 0.0071; p=7: 0.281, 0.0236, 0.0214. Dev >= Lin holds.
## 20:50 [CA] route for r_A, r_B: Line F certV_eta2_a4_tight representation (cert_core.py = verbatim set-up), Line F float check:
  r_A = conj(N5 TW value) (coef sign <-> rho=(-2,8)), -(rA rB)^3 = 3.43577e-4 - 1.95798e-4 i = TW sg=-1 family ratio.  n_cert.py: first run KK=14
  radius 0.0145/0.031 (tail-dominated: Cpow~3247, N1=573.6); rerun KK=18.  GA (sub-product Frobenius, rigorous) = 8.78, RA(Gamma)=27.4, ||Pi-Pi_T||<=2.8e-5.
## 20:40 parent steering (N5 referee: sign error confirmed; redirect to refutation program). Wrote N5/REPORT_N5_v2.md (F1-F10), originals untouched.
## 20:55 [CA] n_cert.py (KK=18): r_A = 0.175180+0.168374i +- 0.00323 (box), r_B = -0.178594+0.243641i +- 0.00321;
  c* in [3.447e-4, 4.443e-4]; w* = -(rA rB)^3: Re in [2.890e-4, 3.982e-4], Im in [-2.520e-4,-1.396e-4], arg in [-0.717,-0.337] (rho=(-2,8); conj for (2,8)).
  Error budget dominated by ||Pi - Pi_T|| * ||products|| (2.8e-5 * 37 * 2) ; tails 1e-5.
## 21:05 q_propx.py: explicit Prop X error, constants Cpow 3247, Gb 3.9e8, T1 381; w0=290 -> p0 = 1165 (error <= 1.43e-4 <= Re w*_lo/2).
## 21:05 k_scale: P_m/m (level h_p only, both (+-2,8), phi<=h) = 2.44 (p19), 10.9 (p23), 103 (p29), 8.7e4 (p47), 1.4e10 (p79).
## 21:10 squarefree: driver needs none (I2'/G3 any odd d; kappa_d(0)=n_d; family via cyclic ideal of norm h_p). Prime powers only add
  partially-isotropic/proper-divisor type terms (Ramanujan c_{q^2}(u) = 0 if q not| u, -q if q||u) -> folded into open item (iv).
