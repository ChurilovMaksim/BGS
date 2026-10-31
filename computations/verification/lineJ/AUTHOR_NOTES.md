# Line J notes (resume point). Started 2026-10-31 04:47 UTC+5.
Task: J1 certify c(beta)!=0 in the combination entering frozen R' (d=7 cross term), or prove it vanishes; J2 STRATEGY.md.
Rules: nice -n 10, moderate RAM, do not touch pids 716309/716609/632967/633068, no push. Labels [P]/[CA]/[N]/[H].
PY=/workspace/bgs-derand/phase3/venv/bin/python ; OMP_NUM_THREADS small.
## Log
- 04:56 read Line I reports, audits. Plan (see below).
- 05:20 KEY FINDING [N]: float T = Tr(J P_mu) = 1/6 to 1e-15 (class 1:3, K0=2 D=8064), c(beta)=3T=1/2. kappa(eig)=3.95.
  Explanation: finite state factors {A_n} have an 8-dim COMMUTATIVE commutant (16-state untwisted and 48-state twisted).
  Untwisted: isotypic ranks 1,1,1,1,2,2,4,4; rank-1: E J E = c E with c in {1/2, 1/2, e(1/8)/2, -e(1/8)/2}; rank 2,4: EJE=0.
  Twisted: ranks 3,3,3,3,6,6,12,12; tr(EJ) same values; EJE != cE but E = e x I3 presumably, then Z/3 averaging gives Tr(J P_mu)=c/3.
  => c(beta) = c_chi EXACTLY, nonzero iff top orbit lies in a rank-3 isotypic. Plan: exact commutant (monomials), block-reduce V to
  the rank-3 isotypic (D ~ 504!), certify the count there (cheap) => c(beta) != 0 rigorous [CA+P].
- 05:45 SECTOR STRUCTURE [N, exactness to be proved]: rank-1 isotypics f_a of the 16-state automaton: A_n f_a = e(a n/8) f_a,
  a in {0,2,4,6} (Line F even sectors); rank-2/4 isotypics W have u ⊥ W  => Tr(J X) = sum_a c_a Tr((I x |0><0|_cyc) X_a),
  c_a = <f_a|e0><u|f_a>, |c_a|=1/2 (case m=9,a=2: c_6=1/2, c_4=e(1/8)/2, c_0=-e(1/8)/2, c_2=1/2).
  => Zhat(beta) = c_m sum_a c_a [Tr Q_{beta,a}^{m/3} - Tr Q^E^{m/3}], Q = 3-step product of sector twisted ops (single lattice).
  => c(beta) = c_{a0} (sector of top orbit), coefficient of mu^m exactly 1 (Lidskii). Rest via Weyl: <= R^{m-1}||V_{beta,a}||_1/3.
  Z0 via Line F (TRACE-198/199): Z_{(-2,8)} = c_m(c_4^F mu*^m + eps), |eps| <= 2(T_V+T_E); kappa = k y' mod 8 [P, lineE note step 5],
  c_4^F = -e(kappa/8)/2, c_0^F = e(kappa/8)/2; mu* in D(b11,2e-6), b11 = 1.35723992 - 1.35164248 i.
  Plan: exact sector proof (Z[zeta8] exponent arithmetic) for 8 cases; sector builds (NS=3, D~500) ; certify top orbit sector +
  enclosures; rest radii per (class,sector); member weights W_C(m) (period 168 = lcm(24,42,8)); window lemma.
- 06:15 EXACT sector decomposition proved for all 8 cases (code/sectors_exact.py, logs/sectors_exact.{log,json}): 4 rank-1 sectors
  a=0,2,4,6, |c_a|=1/2; c_2=c_6=1/2 always; c_4^{(m,+2)} = -conj(c_0^{(m,-2)}) (table). u in span{f_a} exactly.
- Sector blocks built (code/certG_build_sector.py + gstates_sector.py; data/sec/, K0=2 K=36/30, D=504). Float tops (a=+2):
  1:3 s6 1.2837143 (next in s6 0.856; s4 1.0965); 2:1 s4 1.2835951 (next 0.606; other sectors <=0.95); 0:1 s0 1.2624306;
  1:2,1:5 s6 1.1671; 0:3 s4 1.1135; 1:0 .986; 0:2 .897; E all <0.36. a=-2: sector a -> a+4 (conj).
  Model check vs zpred: Zhat rel err 1e-7 (code/check_model.py); Z0 via Line F rel 1e-7 (check_z0.py).
- 06:20 *** MAJOR: combining rho=(2,8) and (-2,8), the d=7 cross term's leading coefficient for class C is
  B_C = c_0^F (c^+_C - conj(c^-_C)) W^+_C ; W^- = conj W^+ ; |W_C| = (12/49)|cos(pi t_bad N_C/7)| (5 members) or 6/49 (49|h).
  => class 1:3 (sector 6/2, c=1/2 both): B=0 EXACTLY -> top class CANCELS between the two rho.
  => class 2:1 (sector 4/0): B = 2 c_0^F c_4^+ W^+ != 0, |B|=|W|/2 in {.0272,.0612,.0763,.1103}. |xi|=mu* |mu_21| = 2.45866 > sqrt(lam).
  => 0:1 also survives (|xi| 2.41815, ratio .98352 vs 2:1). Model (code/model_lead.py) matches exact cross to 1e-6 rel at m=39..123.
  Plan: Line-F-like params (K0=4, rho=1.2, beta=2.5, K=55) for pert~1e-9; small-disc enclosure of mu_21; rest radii; window lemma.
- MILESTONE (certs, code/run_cert_build.sh, run_cert_tracked.sh; logs/cert/): sector blocks rebuilt at K0=5 rho=1.2 K=60 (V, D=1980, pert~7e-13)
  and E (K0=4 rho=.8 K=40). [CA] rig_dom3b k=3 counts: 2:1 (a=2 s4, a=-2 s0) R=0.8; 0:1 (a=2 s0, a=-2 s4) R=0.9; 1:3 (a=2 s6, a=-2 s2) R=1.0.
  [CA] rig_disc (new, code/rig_disc.py) r=1e-7 discs: mu21+ c=1.2795445309020579+0.10189336561597884j (|.|=1.2835951326);
  mu01+ c=-1.068708899896592+0.6720062370877713j (1.26243063); mu13+ c=-1.2554152882657945+0.268057540175505j. F~0.19.
  Rest certs (run_cert_rest.sh, rig_spec rest) running in background.
  Window: theta=168*arg(xi21) mod 2pi = 1.1309 -> lemma (step<=arc) gives cos>=cos(theta/2)=.844 in every 7 consecutive k.
- 05:37 RESUMED after interruption: all 122 rest certs present (run_cert_rest.sh finished before interruption); numerics_large_m done; twrad16 done ((±2,16): mu 1.615413, rtw_max 1.2144 [N]).
- 05:37 58 V rest certs had FAILED (Neumann p=32 too short). Rerun: R=min(1.25,top+0.08), p=64 (code/run_cert_rest2_{0,1}.sh). E rests all certified R=0.45.
- 05:38 [P-check] code/exact_B.py -> logs/exact_B.{json,log} ALL EXACT CHECKS PASSED: c+_a = conj c-_{a+4} (a=2,6), = -conj (a=0,4), all 4 cases; W(-2)=conj W(+2) exactly in Z[zeta7], W21,W01 != 0 for all 28 residues; period checked.
- 05:56 ALL 122 rest certs CERTIFIED (V R<=1.25, E R=0.45). Running code/assemble.py.
- 05:56 ASSEMBLY DONE (code/assemble.py -> logs/assemble.{log,json}): |mu21| in [1.28359503,1.28359523], xi21>=2.4586893, growth >=1.0184224;
  theta=168 arg xi21 in [1.13068,1.13105]; window N=6 consecutive members of m=j mod 168, c=0.84431. M0(j) in 297..495, M1(j) (|D7|/(m phi)>=1) in 417..621.
  Numerics (logs/numerics_large_m.log): D7/(mh) O(1) at m~435-453 (+2.18 at 447, -1.43 at 441); 1:3 parts cancel exactly.
  NEXT: REPORT.md, STRATEGY.md, SHA256.
- 05:58 REPORT.md written.
- 05:58 STRATEGY.md written. J1+J2 DONE.
- 06:23 [F11 correction] the 06:20 entry 'model matches exact cross to 1e-6 rel at m=39..123' is inaccurate: it is 6.6e-4 at m=39 and <=2e-5 from m=63 on.
- 06:23 REFEREE FIXES F1-F11 applied: REPORT_v2.md, STRATEGY_v2.md, code/assemble_v2.py (+logs), code/fixes_checks.py (+log). M0/M1 unchanged; K_minus=K_plus>=table. SHA256 -> logs/SHA256_v2.txt. v1 files untouched.
- 08:53 Referee DELTA2+J3 received: Theorem J v2 ACCEPTED (DF8-DF10 editorial); J3 accept modulo J3-F1..F7. Applying now. Pre-edit sha REPORT_v2.md 9e8e01a57f0ec6f6.
- 08:53 DF8-DF10 applied to REPORT_v2.md (in place, editorial).
- 08:55 J3 v2 + DF8-DF10 done; manifests: logs/SHA256_v2.txt regenerated (REPORT_v2.md edited), J3/SHA256_J3_v2.txt new (v1 J3/SHA256_J3.txt left as historical: entries for theta_big.py, rat_excl.{py,json}, NOTES_J3.md now differ by design).
