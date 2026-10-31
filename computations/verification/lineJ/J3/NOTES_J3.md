# Line J3 notes (started 2026-10-31 06:10 +05)
Task: (a) certify (±2,16) d=7 members negligible [CA]; (b) control O_m / alternative observable; float surveys of other levels. Deliver J3/REPORT_J3.md. Do not edit ../REPORT.md or existing certs.
- 06:10 Frozen def read (bgs-int/BGS/mathematics/fixed-map/resonance_classification_lineG.md §3): levels = ALL d|h, 1<d<=sqrt h, cut |Z_rho|^2/d^2>=4m;
  Res includes -RMT per member; P*={(±2,8),(±2,16)}. => W' = W'_A + phi^-1 sum Dev, W'_A >= -RMT.
- (±2,16): 64 states, 16 operator cases (m mod 48 x sign). Commutant dim 18; 8 two-dim invariant blocks carry the read-out (|c|=1/2 each),
  monomial in a suitable basis (code/sector16*.py). code/blocks16_exact.py: exact verification all 16 cases (running).
  Plan: builder with 2-state finite factor + phases /16; rest certs (no count) + resolvent bound => |Z| <= ||J|| R^m Res ||V||_1 (Cauchy).
- 06:17 blocks16_exact fixed (pairing by first non-diagonal letter; unequal supports 32/64): case (3,2) ALL EXACT CHECKS PASSED, 8 blocks, u in span. Full 16-case run in background.
- 06:24 Referee fixes F1-F11 applied to ../REPORT_v2.md, ../STRATEGY_v2.md (see ../NOTES.md). J3 jobs untouched.
- 06:24 levels_survey [N] (toy single-disc Galerkin K=40, reproduces d=7 top 1.2837 and mu* 1.9155 exactly): per-step twisted radii
  41 (rank 5) 1.5096, 239 (rank 7) 1.5658, 199 (rank 9) 1.4700, 353 (rank 11) 1.3957  >  1.2836 (2:1)  => these levels would DOMINATE D7 when r(q)|m.
  23 (rank 11) 1.151, 79 (13) 1.211, 31 (15) 1.077, 103 (17) 1.222, 47 (23) 1.008, 49 (21) 1.2837 (=d7 top, inherited) < 1.2836? (49: equals 1:3 top, not 2:1 -> check cancellation).
  => refutation subsequence must avoid r(q)|m for 'strong' small-rank q: take m=3p, p prime >= 13 (then levels: 7, rank-p and rank-3p primes, composites).
  Lyapunov (b=8) e^gamma ~0.81 per step for long generic periods [N] -> mu*·0.81 ~ 1.55 << sqrt(lam) [H].
- 06:45 blocks16_exact: ALL EXACT CHECKS PASSED for all 16 cases (8 blocks each, u in span, |J|_F=1/2).
- 06:56 wordtest16 [N]: <u|A_w|e0> = sum_B tr(A_{B,w}J_B) to 1.1e-14 on 3200 random words (validate16 full-64-state float check OOM-prone at 6.5GB -> killed my own job, replaced by wordtest16).
- 06:56 32 distinct (sign, block action) factors (logs/blocks16_reps.json). Pipeline code/pipe16.py (arb build V K0=3 rho1.2 K40 / E K0=3 rho.8 K30,
  float top, rig_spec rest at R=1.02 top+0.02, delete npy for disk) running in 2 workers (code/run_pipe16.sh 0|1). r0 untwisted top 1.6154 (= twrad16 mu), cert R=1.6677.
- 06:56 levels_survey2 [N]: 599 (rank 13) 1.381 > 1.2836 also; periods >= 35: r_max <= 1.056, decreasing to ~0.90 at period 131 (Lyapunov ~0.81).
- 07:02 *** INHERITANCE (code/inherit7q.py, logs/inherit7q*.log) [N, exact to 1e-5 printed]: for d = 7q and beta = q*beta' (trivial q-part),
  W_{7q, qC} = (n_q/q^2) W_{7,C} with n_q = q-2 (q||h: 41, 23) or q-1 (q^2|h: 31), POSITIVE REAL, same for all classes, both signs.
  CRT proof sketch [P-sketch]: G^{(7D')}_t(D'beta') = G^{(7)}_{t/D'}(beta') G^{(D')}_{t/7}(0), |G^{(D')}(0)|^2 = D'^2; labels t/D' mod 7 = j' y' with j' = j/D' mod 7 runs over the level-7 member set; D'-conditions independent (CRT).
  Twist tau = Tr(D'beta' lam^i)/(7D') = Tr(beta' lam^i)/7 -> same Zhat. => inherited composite-level cross terms = (sum_{D'} n_{D'}/D'^2) x cross_7: REINFORCE D7, no cancellation.
- 07:18 RESUMED after interruption: pipe16 workers were still alive (8/32 reps done), not restarted.
- 07:18 INHERITANCE PROOF [P] written (CRT): see REPORT_J3 §2. Generalisation: for gcd(c,e)=1, beta = e*beta' => W_{ce,e beta'} = (n_e/e^2) W_{c,beta'},
  n_e = #{j mod e: j unit mod e, nu unit at primes l|e with v_l(h)=v_l(d)}. Square parts of Dev are >= 0 (|omega|=1) -> drop on the m+ side.
- 07:18 slowtwist [N] (code/slowtwist.py): large primitive q | h_p have 'slow' beta (|beta|~1) with per-step radius up to 1.83 (rho=log_lam q/P ~0.49).
  BUT for prime q || h the label set is all t except one => sum_t e(kappa t^-1/q) complete: |W_{q,beta}| <= 2/q^2 for N(beta) != 0 mod q (all small beta), (q-2)/q^2 for isotropic beta.
  On m=3p: effective rate r_beta * lam^{-2 rho/3} ~ 1.0 << 1.2836 [H]. FIXED-rank levels (rank 17..53 all have slow-beta radius > 1.2836) dominate D7 eventually along multiples of their rank
  => m must have no divisor r in [5, o(m)]: m = 3p essentially forced.
- 07:18 theta_big [CA]: window modulus 360360 too coarse (theta interval contains 0); 27720 ok. On m=3p (not an AP) the window lemma is replaced by
  Vinogradov equidistribution of p*theta over primes in APs (needs arg xi/2pi irrational) -> H_arg.
- 08:00 inherit_proof_check [P-check arb 200 bits]: W_{7q,qC} = (n_q/q^2) W_{7,C} to 1e-55 for (m,a,q) = (15,2,41),(15,-2,31),(33,2,23). ALL CHECKS PASSED.
- 08:00 primelevel_W [N]: q=41 (q||h): max q^2|W| non-isotropic = 1.994 <= 2, isotropic (80 = 2(q-1) beta) q^2|W| = 39 = n_q; q=31 (q^2|h): 1.000 and 30.
- 08:00 rat_excl [CA]: arg(xi21)/2pi not rational with denominator < 1339.
- 08:00 *** (±2,16) DONE [CA]: all 576 rest certificates certified (32 reps x V/E x {u, 8 classes}); R_u <= 1.6677, R_t <= 1.2587,
  rates R_u R_t <= 2.0991 (= 0.8538 xi_lo), R_t^2 <= 1.5843. code/assemble16.py: E16 <= 1% of (K_min/2) xi_lo^m for m >= 213 (>= 243 incl. inheritance factor 1+ (m/2)ln lam).
- 08:00 (fix) ../code/assemble_v2.py docstring line 4 updated (stale v1 wording); output byte-identical; ../logs/SHA256_v2.txt regenerated.
- 08:01 REPORT_J3.md written; SHA256_J3.txt (1495 files). J3 deliverable DONE.
- 08:53 J3-F7 done: theta_big.py relative paths + refuses empty run (output byte-identical); rat_excl.py outward rounding (b_min 1339 unchanged); code/make_reps16.py regenerates blocks16_reps.json byte-identically.
- 08:54 writing REPORT_J3_v2.md (J3-F1..F6); lemma L16 cites TRACE-203 (G2), TRACE-197 (F1), TRACE-207 (termwise per word, finite monomial state factor), Line I v2 step 3.
- 08:55 [N-check] r(q)=ord_q(lambda) matches ranks.json for all 88 primes; q = 1 mod 2r for all prime ranks. REPORT_J3_v2.md written (J3-F1..F7). v1 REPORT_J3.md kept.
