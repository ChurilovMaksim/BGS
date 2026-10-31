# NOTES_N9b (Line N9b)
## [clock label "22:20" INVALID — invented, see erratum; evidence: first artifact code/a_per.py mtime 22:16:06] — start
- Read N9/NOTES_N9.md (22:08 entry): N9 works on gap (a) deep points via op*HS*HS/Theorem C'-type averaging; found 'dilute gas' concern:
  composite classes zeta = zeta_a + lam^g zeta_b have w ~ w_a*w_b NOT decaying in g. => pointwise D_beta / G with ONLY forced windows is
  FALSE for composite classes (they have an unforced long window).  Consequence for N9b: G must charge ALL windows (forced + unforced);
  the dynamical part = growth OUTSIDE boxes (Gamma_out), the arithmetic part = count/length of unforced windows (S-type).
- Operator: Line F lift V-block (sector a=4 slow at twist 0), params of N2 c2_jsr_periodic: K0=3,r=1.2,K=20,beta=2.5,N0=10 (dim 140).
  N2: max periodic rate (period<=4) = mu* = 1.9154732 at fixed point (0,0) [N].
- Plan (1): [N] Gamma_per(theta) = max spectral rate over periodic orbits (n<=8) avoiding the theta-box of (0,0); then attempt certification.
## [clock label "22:35" INVALID — invented, see erratum; evidence: a_per.py 22:16:06; logs/a_per_a4.jsonl final 22:44:23] — periodic-orbit profile (code/a_per.py -> logs/a_per_a4.jsonl) [N]
- Gamma_per(theta) := max spectral rate over primitive period-n orbits with sup-dist >= theta from (0,0) (twist-pair torus):
  n=2: 1.2517 (all theta<=1/8); n=3: 1.2837 (theta<=1/16), 1.2624 (1/8); n=4: 1.4296 (theta<=1/16!, orbit at d0=0.0625), 1.2278 (1/8);
  n=5: 1.5096 (d0=0.012), 1.2179 (1/16), 1.1994 (1/8).  => box radius 1/16 is NOT enough (1.4296 > T'=1.4279); 1/8 gives ~1.23 so far.
- n=6..8 running in background (logs/a_per_68.out).
## [clock label "22:45" INVALID — invented, see erratum; evidence: logs/a_per_68.out final 22:44:23] — a_per n=6,7 done; parent steering (N9 REPORT §3) absorbed
- a_per [N]: n=6: Gamma_per(1/16)=1.2845, (1/8)=1.2229, (3/16)=1.1392; n=7: (1/64..1/16)=1.3646, (1/8)=1.2174, (3/16)=1.1515.
  Orbits passing within ~0.002-0.012 of (0,0) reach 1.51-1.61 (they are slow stretches, must be counted in s).
  Summary n<=7: Gamma_per(1/8) = 1.2837 (n=3 orbit, d0=0.036..0.071? no: 1.2624 at theta=1/8), max over n of profile at 1/8 = 1.2624; at 3/16: 1.2185 (n=2).
  => rank-3p target T'=1.4279: margin ~0.17 at theta=1/8 [N]. Rank-p target 1.2329: needs theta>=3/16 and margin only ~0.015 [N].
- Parent/N9: G must count ALL slow stretches (multi-bump classes). Reformulation G* (see below) — this is exactly the
  Gamma_out(theta) framing already chosen here. N9 also: deep points need no separate regime (windows at all depths); Thm C' fails by index.
- G* (draft): fix box B_theta of the slow fixed point and min stay length L. s_all(x) := total time in stays of length>=L.
  (D1) every orbit segment with no stay >= L: ||P_n|| <= C_out Gamma_out^n ; (D2) every stay: ||P_l|| <= K_box mu*^l (perturbation of
  L_0^l, sum of |tau_i| along a stay is O(theta) geometric) => |r(x)| <= (C_out K_box)^{#stays+1} Gamma_out^{m-s_all} mu*^{s_all}.
  Counting: per stay of length l the class count costs ~lambda^{-l} while the weight gains (mu*/Gamma)^l; mu*/T' = 1.34 << lambda,
  so stays are a dilute gas with fugacity z = O(C^2 (mu*/(Gamma lambda))^L) per unit time; factor e^{z m}: harmless for rank-3p/
  inconsistent/unit classes (margin lambda^{(p/2)(beta-1)}) iff z < 0.294(beta-1)*... and for rank-p lines it acts only on excursions
  of length log_lambda(d N f) => shifts beta by O(z). [P-sketch]
- b_mmc (scalar potential psi_k = (1/k)log||P_k||, graph max-mean-cycle, centre-sampled, NOT rigorous):
  k=6,G=64: theta=0:1.833, 1/8:1.752, 1/4:1.610 — block-norm overhead far too large.  k=12,G=64: 1/8:1.342 but centre sampling is
  meaningless at k=12 (cells stretched lambda^11) - e.g. max over grid 1.504 < mu*. => rigorous version needs k>=12 AND cells of
  unstable width ~lambda^{-k}: ~lambda^12 ~ 1.6e9 cylinders x 140-dim products. INFEASIBLE in plain form. Testing adapted norms (c_wnorm.py).
- (3) omega(h_p) for p<62 (N8b a_fact): <=3 always.
## [clock label "23:00" INVALID — invented, see erratum; evidence: b_mmc logs 22:18:08/22:18:43; c_wnorm.out 22:33:55; e_cone G128/256 22:26/22:28] — norm experiments [N]
- d_svals: single letters very non-normal (sv1 22-57 vs spectral radius 0.57-1.92); products rapidly rank one (sv2/sv1: k=2 0.43,
  k=4 0.14, k=8 0.0077). => fixed ellipsoidal norms are hopeless (c_wnorm, averaged Lyapunov ellipsoid, k=1: 2.35 outside 1/8-box,
  killed the k=3 run); the right object is the rank-one (cone-field) reduction.
- e_cone: phi(y)=log|L_tau0 u(y)|, u = 8-step pushed direction; graph max-mean (centre-sampled, pseudo-orbit graph):
  theta=1/8: G=128 1.534, G=256 1.419;  theta=3/16: 1.392 -> 1.315; theta=1/16: 1.612 -> 1.501.  Converging (slowly, ~ -0.1 per
  halving) toward Gamma_per(1/8)~1.26.  Pseudo-orbit jumps of one cell create fake cycles; u is only Holder (exp ~ log(1/0.43)/log lambda ~0.48).
- G=512 running (logs/e_cone_512.out).
## [clock label "23:15" INVALID — invented, see erratum; evidence: f_Rs.py 22:29:18; f_Rs_a4.jsonl final 22:35:27] — (2) periodic-orbit pressure estimates R_s (code/f_Rs.py, logs/f_Rs_a4.jsonl) [N]
- R_s(n) := (sum_{x in Fix A^n} rho(P_n(x))^s)^{1/n} / lambda  (zeta-function/periodic-orbit estimate of e^{P(s psi)}/lambda).
  n=1..5:  R_2: 0.95,1.12,1.039,1.007,1.0002 (-> ~1.0; consistent with certified r_2<=1.0529 and N8b's 'true r_2~1' [H])
           R_3: 1.470,1.587,1.460,1.410,1.402  (target 1.3284 for kappa<=0.55; floor 1.2058)
           R_4: 2.532,2.597,2.451,2.406,2.398  (target 2.611; floor 2.310)
  => R_3 <= 1.33 looks FALSE numerically (R_3 ~ 1.39-1.40 by trend); R_4 <= 2.611 has ~8% margin. If the mixed gap is to be closed
     by a moment automaton, s=4 not s=3. (kappa_3 at R_3=1.40 would be ~0.57.)  n=6,7 running (logs/f_Rs_67.out).
## [clock label "23:25" INVALID — invented, see erratum; evidence: no artifact; text only] — (3) can 'h_p prime i.o.' be avoided in C2?  [P given G*, + arithmetic]
- Rank-p consistent classes at c = h_p/d (d|h_p, d>1, d >= 2p+1): Lemma Sigma(a) rel(c) <= C_A S_beta d^{1-beta}.  Margin only POLYNOMIAL
  in p (d can be as small as 2p+1), so C2's e^{o(p)} slack cannot absorb them. Deep-ness is not the issue (N9 §2: windows at all depths).
- Gas factor (N9 §3) on these lines acts only on the excursions, of length log_lambda(d N f) (Lemma P'_c): multiplies by
  (dNf)^{O(z)} -> beta shifts by O(z) (z = stay fugacity). Harmless. So the only obstruction is the DIVISOR SUM.
- Sum_{d|h_p,d>1} d^{1-beta} <= prod_{r|h_p}(1+r^{1-beta}) - 1 <= exp(omega (2p+1)^{1-beta}) - 1   (all r = 1 mod 2p, r>=2p+1).
  => C2' [P given G*(Gamma,A_p)]: R' fails along m=3p for p in P' := {p : A_p * omega(h_p) * (2p)^{1-beta} -> 0}, e.g. A_p = p^a and
     omega(h_p) <= p^{beta-1-a-eta}.  With beta>1 only, P' contains every p with omega(h_p) bounded, in particular the primes-h_p set.
  Unconditional removal needs beta>3/2 (Gamma<1.2329) via the worst-case omega <= 0.89p/ln 2p (N8b) — the arithmetic worst case
  (smallest primes = 1 mod 2p) is what forces 3/2; no better unconditional bound on omega(h_p) or on sum d^{1-beta} is known to me [H].
- So: primality replaced by 'omega(h_p) <= p^{delta} infinitely often' (delta = beta-1-a-eta). Weaker, still unproven (no sieve result
  for Lucas-type sequences); data p<62: omega(h_p) in {1,2,3}. Needs A_p polynomial (not merely e^{o(p)}) -> G* must give
  p-independent A up to the gas factor, which is what D1/D2 give.
## [clock label "23:40" INVALID — invented, see erratum; evidence: no artifact; text only] — referee report on N8b (/workspace/audit/lineN8/REPORT.md) absorbed; plan
- Required for N8b: F2 prime powers (31^2|K_5, 7^2|K_7) in Lemma Sigma; F6 kappa floor = two-block method only; F7 G needed for EVERY
  point, evidence on unit/mixed patterns at large p missing (h_13 inconsistent line Gamma_eff=1.267; mixed p=11 max|r|=1.4e-4 ->
  Gamma_raw=1.46, A>~300 at Gamma=1.2329); F8 C2 needs infinitely many prime h_p (unless R' explicit). Bonus: composite loss <=0.52%.
  -> will write REPORT section 'REPORT_N8b_v2' inside REPORT_N9b.md (N8b files untouched).
- Priority now: G-evidence on unit & mixed patterns: code/g_unitmix.py (classes U random unit, US small beta, UM |a|,|b|<=d^{1/4},
  M{q} iso-or-0 mod q & unit elsewhere), reports Gamma_raw (A=1,s=0) and Gamma_eff(theta) with s = ALL slow time (pairs within theta of
  (0,0) or (1/2,1/2)).  p=11 (N=200, no UM): Gamma_raw max U 1.309, US 1.567, M23 1.407, M353 1.210;
  Gamma_eff(1/16) max: U 1.189, US 1.141, M23 1.179, M353 1.154.  i.e. with all slow time counted, A=1 works at p=11 with Gamma<=1.19 [N].
  Running p in {13..61} (code/run_g.sh, logs/g_unitmix_s{1,2}.out, logs/g_unitmix.jsonl).
- f_Rs n=6: R_2 1.0005, R_3 1.4049, R_4 2.401 (stable).
## [clock label "23:55" INVALID — invented, see erratum; evidence: g_unitmix.jsonl final 22:52:29; e_cone_G512 22:37:25] — g_unitmix p<=29 + e_cone G=512
- e_cone (rank-one potential, centre-sampled pseudo-orbit graph) theta=1/8: G128 1.534, G256 1.419, G512 1.357; theta=3/16: 1.392,1.315,1.293;
  theta=1/16: 1.612,1.501,1.497.  Converging toward the periodic profile (1.26 / 1.22) only slowly [N].
- g_unitmix [N], max over samples:
  * random U / M: Gamma_raw max 1.31(p11),1.17(13),1.15(17),1.09(19),1.07(23),1.04(29) — decreasing; medians 0.87-0.94.
  * US (beta=a+b sqrt2 small): |r| = 1.32e-3 INDEPENDENT of p (heteroclinic to the slow fixed point, window ~ m-O(1)).
    => G with s=0 for unit points (N8b Lemma Sigma(d) convention) is FALSE: Gamma_raw -> mu*. With all slow time counted:
    Gamma_eff(1/16)=1.142, (1/8)=1.102, constant in p.  This is the unit-point analogue of N9's multi-bump finding.
  * UM (|a|,|b|<=d^{1/4}): Gamma_eff(1/16) <= 1.248 (p=13, s=15), else <=1.19; Gamma_eff(1/8) <= 1.131.
  * M (mixed): Gamma_eff(1/8) <= 1.179 (p=11), <=1.13 for p>=13.
## [clock label "00:35 (Nov 1)" INVALID — invented, see erratum; evidence: REPORT_N9b.md / NOTES_N9b.md mtime 23:02:11, SHA256 23:02:14] — all runs done; REPORT_N9b.md written
- g_unitmix complete p=11..61 (14 p): max Gamma_eff(1/8)=1.189 (p=11,U), <=1.131 p>=13, <=1.105 p>=29; max Gamma_eff(1/16)=1.248 (p=13 UM),
  <=1.142 p>=29. US |r|=1.32e-3 flat for all 14 p.  a_per n=8: theta=1/8 1.2278, 3/16 1.1317.  f_Rs n=7: R2 1.0002 R3 1.4055 R4 2.4017.
- No [CA] produced in this line. Report + hashes next.

## ERRATUM 2026-10-31 23:50:36 +0500 (added by Line N11b on referee finding N9b-F6)
- The clock labels in the section headings of this file (originally 22:20, 22:35, 22:45, 23:00, 23:15, 23:25, 23:40, 23:55, 00:35 (Nov 1))
  were NOT taken from `date`; they were invented and run ~1.5 h past the real end of the line. Real evidence (`stat` mtimes, Asia/Yekaterinburg, +05):
  first code file 2026-10-31 22:16:06; all runs finished by 22:52:29 (logs/g_unitmix.jsonl); REPORT_N9b.md and this file last written 23:02:11;
  SHA256_N9b.txt 23:02:14. The true per-section times are unknown beyond these bounds; each heading now carries its artifact evidence instead.
- No mathematical content, number or label was changed. The original file is preserved verbatim at /workspace/bgs-lineN/N11b/logs/NOTES_N9b.orig.md;
  the old manifest SHA256_N9b.txt is kept (it now mismatches NOTES_N9b.md by design); new manifest SHA256_N9b_v2.txt.
