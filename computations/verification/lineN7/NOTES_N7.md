# NOTES_N7 (Line N7), started 2026-10-31 20:48 UTC+5
- 20:50 audit/lineN6 dir exists (code/lean/logs), REPORT.md not yet present.
- 20:52 h_rho16 [N] (logs/h_rho16.out): |Z16| 665, 1.18e4, 3.74e6, 3.73e11 at m=15,21,33,57 -> per-step growth 1.6154 (m 21->33 and 33->57 identical);
  (2,16) family ratio at p=19: -1.45e-4 - 6.14e-4i (Re<0!) but weighted by |Z16|^2 << |Z8|^2.
- 20:55 KEY IDEA (+-2,16) at ALL levels: trivial floor Dev_d(16) >= -n_d|Z16|^2/d^2, sum_d 1/d <= sigma_{-1}(h_m) = O(loglog h) [Robin].
  Needs |Z16| rate < sqrt(mu*^2 lam^{-1/6}) = sqrt(2.7350) = 1.6538; J3 certified only 1.6677 (rest cert R=1.02 top+0.02). Run J3 rig_spec in 'dom' mode.
- 20:57 dom16 rep 0 [CA]: |mu| in [1.5954,1.6354] (r1 0.02), rest < 0.95, F_R1 6.1e-7, F_R2 1.6e-7. Launched reps 2,9,12,16,21,24,27.
- 20:58 o_levels p=7 [N]: d=1673: inherited 0.010724+0.005761i, level7 2.10e-4+2.97e-4i, mixed -2.1e-5+1.43e-4i (counts 476/12/5712).
- 21:00 PATTERN LEMMA: exact closed form found. gamma = (eps^{k+1} - eps'^k)/sqrt2 = x_{k+1} + y_k sqrt2, N(gamma) = h_p (p=2k+1);
  beta=(q+gamma)/4; Tr(lam^i beta)/q = 1/2 + d1_i (mod 1), 2sqrt2 d1 = [e^{2i+k+1}+e^{k-2i}+(-1)^k(e^{-2i-k-1}-e^{2i-k})]/D, D=2q=e^{2k+1}-e^{-2k-1};
  d2 = d1 - y_{2i-k} (integer): 2sqrt2 d2 = (-1)^k e^{k-2i} + [e^{2i-3k-1}+e^{k-2i}+(-1)^k(e^{-2i-k-1}-e^{2i-k})]/D. Windows (-k/2,k/2),(k/2,3k/2); junctions A/B with a=e^{-1}/(2sqrt2), b=1/(2sqrt2).
- 21:00 pattern lemma VERIFIED exact (logs/b_pattern.out): closed forms d1,d2 match exact integer twists mod 1 to 1e-167..1e-390 for p=5..163;
  slow count p-5; junction values a=0.1464466, b=0.3535534. c_patZ: closed-form beta gives Zhat/Z = 3.43578e-4 +- 1.95796e-4 i (=N6 family) p=19,29.
- 21:05 STEERING: N6 referee landed (audit/lineN6/REPORT.md: N5v2 READY; N6 READY-after-fixes). Do: REPORT_N6_v2 (F1,F3,F4,F5,F6,F7,F9; F2 via pattern lemma [P]);
  focus gap (a) [referee route: parametrize iso points (q+gamma alpha)/(4q), series in alpha]; F6 (h_rho16 + W/W+ threshold p1); F7 mixed classes. Gap (b) -> other author in N7b.
- 21:10 dom16 ALL 8 reps certified [CA]: |mu16| <= 1.635413 (r1=0.02), rest < 0.95.  d_Z16.py: |Z_(+-2,16)| <= C16 1.6355^m, C16 = 2.273e5;
  Sigma_rho|Z_rho|^2 <= 4|Z8|^2 for m >= 51; (+-2,16) members at ALL levels (Dev floor + Robin sigma(n)/n) cost <= 0.01 F_m for p >= 337. => (+-2,16) removed from Omega# entirely.
- 21:15 iso parametrisation: every iso point on line (gamma) is x = z + s*e*gamma/(8q), z one of 8 fixed points (1/8)O/O^vee. base 1/4 (twist 1/2): e=2alpha;
  base 0: e = 2 sqrt2 alpha. e_isodepth p29/p47: values p-independent to 4 digits; eps*alpha, -alpha identical. base-1/4 alpha=1 = family 3.4358e-4+1.958e-4i;
  base-0 alpha=1 = near-0 family 2.9866e-5-6.599e-6i; next depths (N(alpha)=7,9,17,...) ~1e-8..1e-7 (base 1/4), 1e-7..1e-12 (base 0).
- 21:20 f_mixed MC (p=11, 13) running; e_isodepth3 p47 K600 both bases running.
- 21:09 NOTE: the time stamps of the entries labelled 21:00-21:20 above were written ahead of the box clock (approximate); actual box time now 21:09. From here on stamps use $(date).
- 21:22 i_shells p47 j=4..26 done (table logs/i_shells_p47_table.out): decay beyond 2^12, heavy tails; j>=10 total ~8.5e-5 of Re w_fam.
- 21:22 f_mixed p=11 [N]: abs majorant class A 0.149+-0.098, class B 0.022+-0.006 of family term (not negligible at small p). p=13 running.
- 21:22 REPORT_N6_v2.md (F1-F9) and REPORT_N7.md written; N7b/NOTES_FROM_N7.md left.
- 21:22 F5 CORRECTION: referee's composite loss 4/(2p-1) assumes omega<=2; general worst case 1-2omega/(2p-1), omega<=p ln eps/ln(2p-1): loss<=11.4% at p=1165 -> F_m >= 2.06e-3 p|Z8|^2/h_p; d_Z16 rerun: p16 = 339.
- 21:31 f_mixed p=13 [N]: ratio_A 0.0023+-0.0007, ratio_B 0.0032+-0.0011 (p=11 value driven by heavy tail). Hashing.
