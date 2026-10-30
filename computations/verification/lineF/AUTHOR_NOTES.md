# Line F notes (resume point). Started 2026-10-30 12:45 CET (box clock).
Goal: unconditional proof that full-alphabet resonance TO has isolated eigenvalue |mu|>lam^{1/4} (k1 eta=2; then 49-state full kick).
## Key idea (12:50)
Full-alphabet trace t_m = sum_{w in Z^m} prod w(n_j) e(c n_j s_j) [s_j real periodic orbit, s_{j+1}=(s_j+n_j)/lam].
H^2(D_rho) can't host all letters. FIX = lifted operators on weighted direct sums of Hardy spaces of a lattice of discs:
 vertex states k in Z, disc D(k,r), r>0.6036; letter n: k -> f_n(k)=round((k+n)/lam); block phi_{f_n(k)} -> w(n) e(cns) phi((s+n)/lam) on D(k,r).
 edge states (k,k+1), disc D(k+1/2,rE), rE>0.1036; transition only if f_n(k+1)=f_n(k)+1.
 Composite integer map F_w nondecreasing, increments in {0,1}, F(k)-k -> -+inf => Fix(F) nonempty interval => #fixed vertices - #fixed edges = 1.
 => t_m = Tr Lv^m - Tr Le^m EXACTLY (Manning/Bowen-style inclusion-exclusion). Both trace class on weighted l^2(+)H^2 (weights e^{-beta|k|}).
 => certify Lv (sector 4) one eigenvalue mu*, rest |z|<=r2; Le all |z|<=r2; sectors 0,2,6 both <=r2. Weyl => t_m = mu*^m + O(r2^{m-1}(Tv+Te)).
 Truncation: core |k|<=K0, letters |n|<=N0, Galerkin degree K; Delta (far comps / big letters) in operator norm, superexp small.
## Log
- 13:10 lift.py float prototype: trace identity t_m=(1-lam^-m)(Tr V^m - Tr E^m) verified m=1..5 (L=3) to 1e-15. Float spectra (logs/spec_float.log):
  V a=4: 1.915473 (=physical L=10 value), next 0.7278; V a=0 .574, a=2/6 .877; ghosts .3624,.2659 in BOTH V and E (cancel); E radius .3624. Stable in K0,r,K.
- Design of rigorous cert (cert_lift.py): core |c|<=K0 states, Galerkin K; far rows: X (far<-core, kept, block-lower-triangular => no spectrum) + Delta (big letters / far<-far / |k|>Kmax), weights 1 on core, e^{-beta(|c|-Rc)} off core.
- 13:40 cert_lift.py written (arb). BUG caught & fixed before results: `if Mx[i,j]!=0` would skip balls containing 0 -> now aggregates blocks with acb_mat ops, no skip. run1.sh launched (V a=4,0,2,6 K0=4 rho=1.2 K=55 beta=2.5 p=40 r2=1; E K0=4 rho=.8 K=40 p=30).
  Bounds (sector-indep): V delta=4.5e-11, Delta=1.86e-9, ||X||=6.16, trace-norm<=730.1; E delta=1.2e-10, Delta=7.5e-14, ||X||=.32, trace<=22.93.
- 13:55 Lean lean/LineF.lean compiles (lake env lean in formalization, cache get: no download): step_round, edgeOK_iff,
  edge_closed_iff, count_identity, fix_outside, vertex_minus_edge (main). Axioms propext/Classical.choice/Quot.sound. No sorry. log logs/lean_LineF.out
- (box clock 13:20) BATCH 1 DONE, ALL CERTIFIED (k1 eta=2, full alphabet): V a=4: unique eig in D(b11,1e-3), |mu*| in [1.914473,1.916473], rest |z|<1 (F_R1=4.9e-4,F_R2=6.1e-6);
  V a=0,2,6 and E all: spectrum |z|<1. T_V<=730.15, T_E<=22.94. logs/certV_eta2_a*.json, certE_eta2.json.
- xcheck_class.py: lifted full-alphabet law vs referee exact class sums |Z(nu*)|^2, m=5..15: rel err <=9e-14 (logs/xcheck_class.log).
- 13:22 run2.sh launched: eta grid (K0=4 r2=1 for eta<=1.75; K0=5 r2=1.45 for eta>=2.25) + eta=2 a=4 tight r1=2e-6.
- 13:32 tight r1=2e-6: |mu*(eta=2, FULL alphabet)| in [1.9154712, 1.9154752] (float 1.9154733). bounds_eta2.json: m0=13 (Z>0), all odd m>=15: F/2m>=5.92, Wrest/m>=7.84; growth 1.518^m.
- eta=1.25 certified V a=0,2,4,6 & E (K0=4). eta_curve.log: sector-4 |mu*| > lam^{1/4} for eta in (0.9511, 3.2115) (eta_thresh.log, float); sector 0 exceeds at eta>=~4.6.
- lift49.py (float, K0=2,K=14): full kick s=+1 b=4 top 1.883926 (matches Line E step2 1.884), cluster ~1.27-1.30 real; E radius .367. Rigorous 49-state needs ~24k dims (K0=4,K=55,x49): NOT feasible here -> report as finite reduction, open.
- Lean generalized to real shifts (49-state law uses x=n/7). run_neg.sh negative controls launched (r2=.85 a2; K=25 a4; K0=2 a4).
- (resume 13:34) killed run_neg (load 35); rerun controls later serially. run2 at eta=1.5. lift49 s=-1 running.
- 13:45 REPORT.md drafted (placeholders GRID_TABLE, LIFT49_CHECK)
- 13:50 lift49 vs exact class sums full kick m=5..13 both s: rel<=5.9e-7 (in REPORT). after.sh queued neg controls after run2.
- 14:25 eta 1.5,1.75 certified+bounds; grid_table.py; waiting K0=5 etas
- 14:25 resume#2: killed run2 loop (eta 2.75/3.0 dropped), eta 2.5 jobs reniced; after.sh will run neg controls when run2 gone
- 14:40 neg K25 fails (ok); report controls section added; waiting r2=.85 control and eta 2.5 a4/E
15:04 neg r2=.85 fails as predicted (root .932); eta2.5 V a4 certified [1.8666,1.8686]; E sectors 2,6 pending
15:14 REPORT finalized; eta2.5 E sectors 2,6 pending (pid 552224 -> logs/certE_eta2.5.*)
