# Line I notes (resume point). Started 2026-10-30 19:45 (box clock UTC+5).
Task: principled proof / rigorous partial proof of Conjecture R' (TRACE-206) via averaging across residues.
Read: lineG REPORT, lineH REPORT+NOTES, lineE REPORT, claims TRACE-163..206 (esp. 169 Prop C, 170 Thm W, 195 Prop G).
Data: k1 class sums lineG/logs/Torb_k1_m{15,17}.bin, audit/lineE/logs/T_{k1,full}_eta2.0_m{5..15}.npy, Torb_full_m15.bin.
Do-not-touch pids: 716309 716609 633068 552224 599729, polish2/lineE/lineG/lineH jobs, /workspace/audit.
## Log
PY=/workspace/bgs-derand/phase3/venv/bin/python
- 20:05 code/base.py (cache data/base_*.npz: |Z|^2 all units, vectorised Gauss reduction, frozen TRACE-206 res mask), reproduces lineG W'_act/m:
  k1 m7..17: -1.226,-0.819,-0.314,-0.041,+0.229,+0.092. full m=15/9 need virtual-primary handling (not done; full only m=11,13 used).
- strat.py -> logs/strat.log: W' by dyadic shortest-vector length. Low heights (l<64) contribute positive excess that DECAYS in m
  (l in[4,8): .137,.099,.066,.055,.034 for m=9..17 = (±2,4) family r~1.5<lam^{1/4}); top bins mean|Z|^2/RMT: .74,.88,.94,1.02,0.9965.
- dil.py -> logs/dil.log: P* dilation members vs Gauss main term. Frozen def (main term) differs from act by +0.24 W/m at m=15
  (d=41: rel +15%, d=287 +37%, d=7 (-2,8) +1.8%). d=7: rel 0.29 (m=9) -> 0.0005/0.018 (m=15); m=17 d=103 rel 0.002.
  RISK for frozen R': main term grows like (mu^2/sqrt lam)^m ~1.52^m, so relative dilation error must decay faster than 1.52^-m.
  Derived: members Z_t = sum_gamma W(gamma) e(-t Nm gamma/d), W = pushforward of w(n)=Phihat e(-nu0 P/2h) under alpha_n mod d;
  coset Parseval sum_{t mod d}|Z_t|^2 = d sum_u |W_u|^2; deviation = cross term 2 eps Re(conj Z_rho delta_0) (norm-zero class only) + d sum|delta_u|^2.
  delta's = twisted (kick translated by Tr(beta lam^i)/d, period ord_d(lam) | m) operator traces, radius r_tw. Cross term o(1) iff r_tw < sqrt(lam)/mu=1.2603 (unless delta_0 special); square term iff r_tw<lam^{1/4}.
- 20:00 perb.py/angle.py/theta.py/halo*.py (logs/*.log). KEY FINDING "resonance halo": nonresonant nu whose shortest vector (a,b)
  has theta=2a/b near the resonant couplings ±1/2 (also ±1/4, ±3/4) carry excess: window |th|=0.5±0.1 contributes +.073,+.068,+.062,+.048
  W'/m (m=11..17, k1), x=1.31..1.20; concentrated on 8|b (x 2.2-2.7) and small e=b-4|a| (e≡0 mod 8 strongest, growing in m at fixed e).
  Away from resonant couplings ("rest", 85% of residues) x = 0.722,0.865,0.948,1.019,0.999 (m=9..17): bulk is RMT to 0.1% at m=17.
  m=17 W'/m=+0.092 = low-height/broad-dil +0.040 + halo(±1/2) +0.048 + halo(±1/4,±3/4) +0.016 + theta~0 -0.008 + rest -0.004.
- halo4: relative reconstruction delta=nu-nu_rho ≡ c/d' (c even small): NOT a clean 1/d'^2 'generalized dilation' law (y grows with d').
  Concept: Z(nu0+delta) = Z_rho * sigmahat(delta) exactly, sigma = resonant (complex) measure pushed to P mod 2h; dilations=c=0, halo=small c.
  Link: Pisot (Erdos-Salem) non-decay of Fourier transforms of self-similar measures with ratio 1/lam.
- 20:10 verify_coset.py -> logs/verify_coset.log: dilation-coset L^2 law (a)-(d) EXACT, max err 1.5e-12 (m=5 d=41, m=9 d=7, m=11 d=23, m=7 d=239).
- twist.py: dense G2 operator (K=40,L=10,rho=2.6, dim 2560) for (2,8): top |eig| 1.915473 (x2), next 1.251697; law |Z|^2 = class sums
  (m=9: 30042.0 vs 30042.05; m=15: 7.34915e7 vs 7.34915e7). Dense eig takes ~6 min under load: avoid.
- shape.py -> logs/shape.log: shape-space SL2(Z)\SL2(R) (tau=w/v, phi=arg v): unweighted Hecke points = Haar (rms z 0.95-1.1).
  Weighted local mean x per cell: y<3 cell sd 0.31/.08/.09 (m13) -> .13/.05/.04 (m15) -> .043/.013/.018 (m17) = pure noise level at m=17.
  Structure only at y>=3 (cusp), phi in [75,105) deg (directions (1,4),(1,8)): halo.  => R' <=> weighted Hecke equidistribution + cusp control.
- 20:30 dilpred.py (twisted G2 law -> predicted d=7 members, coset terms) running in bg, m=9,15,21,27 -> logs/dilpred_d7.log, data/zhat_*.npy
- 20:31 lean/LineI.lean COMPILES (0 errors, no sorry/native_decide): cross_term, sum_N_sq, coset_decomp, norm_count_7, norm_count_23_zero;
  axioms only propext/Classical.choice/Quot.sound -> logs/lean_LineI.out. (Indexing: p=d+1 residues as Fin (d+1); pure algebra.)
- 20:34 RESUMED. dilpred d=7 m=9 (2,8): twisted-G2 prediction of the 5 unit members matches class sums to 2.6e-8 rel;
  Z0=30042.05, main_each=613.10, cross=877.61, square=319.51, pred_rel=+0.2937 (= dil.log 0.29), max|Zhat(beta≠0)|^2=30.16.
  => deviation of dilation members from frozen main term is EXACTLY cross(δ_0)+square(δ_u) of twisted traces (Prop I2), numerically closed.
  Job pid 1544180 continues m=9(-2,8),15,21,27 (~7 min per (m,rho) at m=9, scales ~m). Next: REPORT.md.
- 20:35 REPORT.md written (statements I1,I2,I4,I5 classified; failures; referee list). dilpred continues.
## Session 3 (20:36 UTC+5): tasks (1) dilpred analysis, (2) certify r_tw d=7, (3) (E'') off-diagonal.
- dilpred m=9 (-2,8): pred_rel -0.0144, match 2.0e-8.
- params.py: 7|h iff m≡3 mod 6. (±2,8) operator parameters (k,psi0,psi1 mod 8) period 24 in m: 4 cases each (m=9,15,21,27 cover all).
- Zhat(beta*lam)=Zhat(beta) (3.8e-15, cyclic shift) -> 16 beta-classes mod 7.
- NEW Prop I2' (per-member, any odd d|h, gcd(d,2)=1, t unit mod d): Z_t = omega_t Z0/d + Delta_t, |omega_t|=1 (Gauss sum G_t(0)/d),
  |Delta_t| <= (1/d) S_d, S_d = sum_{beta≠0 mod d}|Zhat(beta)|  (|G_t(beta)|=d for nondegenerate Nm, d coprime to 8).
  => ||Z_t|^2-|Z0|^2/d^2| <= (2|Z0|S_d+S_d^2)/d^2.  m=9 (2,8): S/|Z0|=0.723.  Works for composite d (287) too.
- Heuristic: for LARGE levels d~|Z0|/sqrt(4m) rigorous bounds need sqrt-cancellation in twisted sums (diag mass of Zhat: sum_beta|Zhat|^2 = d^2(1+offdiag));
  fixed-d theorems (m->inf along progression) are feasible; uniform-in-d (D) is NOT reachable by operator bounds.
- twrad.py (bg, logs/twrad_K40.log): float radii of 3-step twisted products, single disc K=40 rho=2.6.
- 20:58 IMPORTANT perf: numpy BLAS threads thrash under load -> always export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 (100x faster).
  killed own dilpred (pid 1544180, thrashing at m=15); replaced by fast restricted-state predictor (zpred.py).
- reach.py: reachable states of (±2,8) automaton from state 0 = 16 of 64 (invariant), co-reachable 16. Restrict to 16 states.
- twrad2.py K=30 rho=2.6 L=10 (logs/twrad2_K30.log): all 8 operator cases (m=9,15,21,27; ±) give IDENTICAL spectra:
  mu=1.915473 (x2), 3rd 1.053852 (restricted!), twisted r_tw over 16 classes: 0.8967,0.9974,1.1135,1.1671(x4),1.2624,1.2836,1.2837 (pairs).
  r_tw max = 1.2837 > sqrt(lam)/mu = 1.2603  => cross term heuristically NOT o(1): (mu r/sqrt lam)^m = 1.0186^m growth. square ok (r<1.554).
- 21:25 MILESTONES since 20:58:
  * twradq: r_tw stable in K (30/40) and rho (2.2/2.6) at L=10: top 1.28371,1.2836,1.26243,... ; L=12 single-disc = ARTEFACTS (radius 26) -> never use L>10 single-disc.
  * zpred.py (code/, K=40 rho=2.6 L=10, bg -> logs/zpred_K40.log, data/zpred_d7_*): matches class sums m=9 (2.6e-8) and m=15 (8e-9).
    m=75,81: maxZhat^(1/m)≈1.27 (-> r_tw), Dev/(m^2 h) ~1e-5..1e-4 oscillating.
  * Symmetries [P]: Zhat(beta*lam)=Zhat(beta) (cyclic shift, lam^m≡1), Zhat(-beta)=Zhat(beta) (ghat even, P even) -> 8 classes of beta≠0 mod 7.
    Top classes (2,0)~(1,3) r=1.28371; (4,0)~(2,1) 1.2836; cone(Nm=0) lines x≡±3y are self-dual; top classes off-cone.
  * VERDICT (1) [N]: d=7 relative error decays like (r_tw/mu)^m=0.6702^m, SLOWER than 1.52^-m=0.6579^m; frozen d=7 term contributes
    ~C*1.0187^m/m^2 to W'/m: negligible for all computable m but -> infinity eventually (heuristic: needs nonzero leading coefficient).
    => frozen R' (TRACE-206) heuristically FALSE asymptotically (m in the 1000s); amend: use actual member values (R'_A), equivalently
    exact Prop I2' member formula via twisted traces.
  * liftchk.py: lifted V/E lattice (K0=2,r=0.8,K=12) twisted 48-state cyclic op: Zhat = Tr(B V^m)-Tr(B E^m) to 1e-6 (m=9), B=I x |e_(0,0)><1_{i=0}|.
  * cert/: certG_build.py (adapted cert49_build: x=n, C=-4a c0/b, k1 Bessel tail, gstates monomial factor), rig_spec.py = Line H v4 (sha f346e22c identical).
    pilot V m=9 (2,8) class 2:0 K=16/12: D=3456, delta1=.121 delta2=.210 (too big -> need K~30), Delta 6.2e-4, ||X|| .684, 15 s.
  * Plan (2): certify square term only (target R<lam^{1/4}=1.5538; float r 1.284, margin 21%): 8 classes x (V,E), case m≡9 mod 24, rho=(2,8).
- 21:36 zpred DONE m=9..123 (logs/zpred_K40.log, json logs/zpred_d7_K40_r2.6_L10.json): maxZhat^(1/m) 1.208->1.2765 (-> r_tw 1.2837);
  frozen d=7 contribution to W'/m (=Dev/(m phi)): m21 -.013, m27 +.007/+.021, m33 +.009, m39 -.019, m45 +.021 ; Dev/(m^2 h) envelope ~1-4e-4 flat m=33..123
  (consistent with 1.0187^m/m^2 having its min near m~108). Extrapolation: W'/m contribution ~0.3 at m~300, ~8 at m~500 (sign oscillating).
  => frozen R' predicted to FAIL (W'/m not -> 0) around m ~ 300-400 along m≡3 mod 6, from d=7 alone [N + heuristic extrapolation].
- run_sq.sh started 21:28 (cert/, OMP 3): per class E build+rig (R=1.0,1.2) then V build+rig (R=1.45,1.5,1.55, p=24); progress cert/logs/run_sq.progress.
  E 1:3: CERTIFIED R=1.0 (F=0.01383), R=1.2 (F=0.00959); trace norm E 815.3, pert 6.67e-4.
  cert/trchk.py pilot: core V (K=16) partial trace = Zhat(2,0) m=9 to 1e-4 ; top |eig| 1.28371 (x3, cyclic).
- 21:51 CERT class 1:3 (top, r_float 1.28371): V CERTIFIED R=1.45 (F=0.357), 1.5 (0.229), 1.55 (0.177); pert 2.50e-3, D=6624, ~22 min.
  cert/bounds_sq.py (arb): |Zhat| <= 6.77e6*1.45^m + 6.86e4*1^m (this class); square term/phi <= ... (0.8709)^m, <0.01 from m=321.
  Theorem needs all 8 classes (run_sq.sh continuing, ~25 min/class).
  [P] operator case depends only on (h,y') mod 8 = (1+sqrt2)^m mod 8 (h+y'sqrt2=(1+sqrt2)^m, checked m=9), k ≡ 3 h^{-1} mod 8 (from 4 nu ≡ 1 mod h, nu odd <2h).
- theory_E2.md written: step (3) routes A (DI large sieve -> h^eps barrier even with RMT 4th moment), B (Kuznetsov: l^1 5.57^m), C (Bowen-Margulis wrong measure); Prop I8 one-sided; halo quantified.
- 22:16 RESUMED. run_sq alive (pid 1573921). class 2:1 CERTIFIED (V R=1.45..1.55, E). 2/8 done; ~22 min/class. REPORT.md S3 section drafted (S3.4 pending).
- 22:39 class 0:1 done (3/8).
- 22:51 class 1:2 done (4/8).
- 23:08 class 1:5 done (5/8).
- 23:26 class 0:3 done (6/8).
- 23:45 class 1:0 done (7/8); last 0:2 running.
- 00:04 run_sq ALL_DONE (8/8).
- 00:10 bounds_sq.py DONE: all 8 classes V<1.45 (F<=0.357), E<1.0; Theorem I6 assembled (square-term/phi <=0.01 for m>=321, rate 0.8709^m). REPORT S3.4-S3.7 written (R'_A amendment). FINAL.
## Session 4 (00:10 UTC+5 Oct 31). Referee reviews /workspace/audit/lineI: DO NOT modify existing files it reads; new outputs in new dirs (sym/, cert2/, dom/).
- 00:20 ITEM 1 via EXACT SYMMETRY (no new certs needed): sym/monomial_intertw.py (integer mod-8 arithmetic, json sym/monomial_intertw.json):
  for every case (m in {9,15,21,27}) x (a=±2) there is a monomial UNITARY intertwiner X (16 states, 8th-root phases):
   a=2: X A_n^{(9,2)} X^-1 = A_n^{(m,2)} (all n mod 8);  a=-2: X (-1)^n conj(A_n^{(9,2)}) X^-1 = A_n^{(m,-2)};  and Y A_{-n} Y^-1 = A_n (reflection).
  Lifted op identities [P]: L^{(m,2)}_beta = U L^{(9,2)}_beta U^-1 (U=I x X x I3);  L^{(m,-2)}_beta = J L^{(9,2)}_{-beta} J^-1 (J = K x X x I3, K = complex conj
  on the disc lattice; uses conj ghat(n) = (-1)^n ghat(n), K M_C K = M_{-C});  L_{-beta} = (R x Y x I3) L_beta (..)^-1 (R: s->-s, c->-c lattice reflection;
  uses ghat even, round(-x)=-round(x) off half-integers).  Norms/trace norms invariant => Theorem I6 bounds hold for ALL m≡3 mod 6, rho=(±2,8).
- 00:21 cert2/run_xcheck.sh started: direct cert of transferred case m=15,a=-2,class 1:3 (V R=1.45, E R=1.0) as consistency check.
- 00:39 ITEM 2: dom/rig_dom3b.py (counting cert, k=3 Householder deflation; v2 bounds ||R_Lam b12 R_Y|| POINTWISE on grid + resolvent-identity covering). Pilot D=3456 (K=16/12, data/pil): Rcore 293 at R=1.24 (v1 crude bound gave 6221) -> at D=8064 (pert~9.4e-4) expect F~0.45. Pilot itself not certified (pert 0.33, expected). cert2 xcheck E15m(a=-2) F=0.013833 == Session-3 E value (transfer consistent). dom/run_dom.sh queued (waits XCHECK_DONE; classes 1:3, 2:1; K=36/30 D=8064; R in 1.22..1.262, p=32); sha in dom/logs/SHA256_dom.txt.
- 00:41 ITEM 3 recorded in theory_session4.md: S4.1 Poisson/aliasing identity with units [P]; S4.2 unbounded prime support of h_m (BHV) => no fixed S-arithmetic operator [P mod cited thm]; S4.3 Hecke / S4.4 L^2-in-m: reduce to same aliasing collisions, no weakening obtained [assessment].
- 00:41 cert2 xcheck DONE: direct cert m=15,a=-2,class 1:3: E R=1.0 F=0.013833, V R=1.45 F=0.356981 -- equal (to 6 digits) to Session-3 m=9,a=2 values, as the exact intertwiner predicts. Item 1 confirmed independently. dom run started.
- 00:44 REFEREE FIXES (verdict ACCEPT AFTER FIXES, /workspace/audit/lineI/REPORT.md). New files only: cert_v2/bounds_sq_v2.py (+logs/bounds_sq_v2.{json,log}, SHA256_v2.txt): B1 outward rounding CV=6768179.601->6.769e6, CE 68586.18->6.859e4, q=0.870884015->0.8709 (rate <=0.87089^m); table over ALL m≡3 mod 6: first m with all later <0.01 = 321 (0.004574; 315 gives 0.01046); R1 rigorous tail m>=1425 (decreasing, <=4.7e-69). theory_E2_v2.md: B6 Lemma I5' (C(k) sign; unit-restricted form with Ramanujan sums; ALSO the diagonal meets all c_{2hj}, not only c_0 -> 'invisible' withdrawn; needs horocycle equidistribution + C(0)=O(m)); B7 Prop I8 hypotheses; B8 scope; B9 Route A/B -> [assessment]. lean/LineI_v2.lean (R5 docstring norm_count_23_zero), compiling -> logs/lean_LineI_v2.out. R2: cert_v2/gstates.py imports law from own dir; run_sq.sh sha 49dee38c (mtime 21:29:34) in cert_v2/logs/SHA256_run_sq_sh.txt. R6: referee matrices /workspace/audit/lineI/data/{V,E}_1_3_b0_{mid,rad}.npy sha == provenance (cert_v2/logs/R6_stored_matrices.txt) -> designated stored copy.
- 00:46 REPORT_v2.md written (generator cert_v2/mk_report_v2.py, line-wise replacements of REPORT.md v1, kept): B1 6.769e6/0.87089, B2 'algebraic core Lean-checked', B3 non-unit t=2 + member Dev 900.47, B4 cyclic-invariance proof, B5 Thm I4 quantifiers (one Y(m), K_m uniform; or diagonal choice) + unit normalisation, B6 -> Lemma I5' pointer, B8 c_m=1-λ^-m, TRACE-197 cite, referee checks, scope, B9 (a)-(g) heuristic wording, /m not /m², caveats, TRACE-206 OPEN, R'_A 'conjectured'; R1 tail, R3 [P] mod 2h, R4 proofs, R5 ε=+1, R6, R7. lean/LineI_v2.lean EXIT=0, axioms propext/Classical.choice/Quot.sound (logs/lean_LineI_v2.out).
- 00:54 REPORT_session4.md drafted (S4.2 dom results pending).
- 01:29 ITEM 2 CERTIFIED (class 1:3): dom/logs/V36_1_3_dom3b.json (rig_dom3b sha dc6aec1f): exactly 3 eigenvalues of V_beta in |z|>R for R=1.22 (F=0.4133),1.24,1.25,1.262 (F=0.6843). With Z/3 symmetry => sigma ∩ {|z|>1.22} = {mu, w mu, w^2 mu}, simple, 1.262<|mu|<1.45 => r_tw(1:3) > 1.262 > 1.26038 [CA]. c(beta)≠0 NOT certified. REPORT_session4 S4.2 (Theorem I9) written. Class 2:1 running.
- 01:32 RESUME after box-load interruption: (a) referee fixes already done (00:44/00:46 entries), (b) other 7 cases done by exact symmetry + cross-check (no run_sq jobs needed/live), (c) class 1:3 certified; class 2:1 rig_dom3b live (pid 1686105, j=8 at 206 s), (d) theory_session4.md recorded. Waiting for 2:1.
- 01:42 ITEM 2 class 2:1 CERTIFIED: R=1.22..1.262 (F=0.3076..0.6489), dom/logs/V36_2_1_dom3b.json; DOM_DONE. Theorem I9 for classes 1:3, 2:1. REPORT_session4.md finalized (S4.0-S4.6). json sha appended to dom/logs/SHA256_dom.txt.
- 02:30 DELTA FIXES DF1-DF7 applied (pre-fix copies pre_delta/; REPORT_session4 S4.7). DF4 rerun dom_v3/ (both classes certified at R=1.22..1.262). DF2 cert_v3/, sym_v3/ (reruns identical). Integration clone integ/ (branch line-I-rprime).
