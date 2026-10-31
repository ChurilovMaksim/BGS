# NOTES_N10b (Line N10b)
## 23:05 — start. Tasks: (1) cone-field cert of Gamma_out(1/8) [CA*], (2) 4-fold automaton R4<=2.611, (3) D2 + stay count, (4) h_13 line w/ all slow time.
- N11 NOTES read (22:42-23:01): Line F certs r2=.85/.80, t_classes, 'coding lemma: c_min=.1716 g0=5 G0=6 eps-steps'.
## 23:15 — (2) first finding [N]
- 4-fold automaton = 2-fold carry automaton with letter weight rho -> rho*rho (|A|_HS^4 <= Cpair^2 * prod rhohat^2, rhohat^2 = FT(rho*rho)>=0).
  code/a_r4_float.py: tau=0 letter matrix spectral radius: s=2: 1.051116 (=N2 r_abs), s=4: 5.411513 (E=6,10,14 identical).
  Target 2.611. => the Lemma-O1-majorant automaton CANNOT certify R4<=2.611: its rate is >= rho(M4(0)) = 5.41 since middle
  letters have tau_j>=0 and rho_d is increasing in tau (entrywise domination), C_pair^2>=1. (Same number as N9's joint A+B rate 5.409.)
  Reason: majorant peak rhohat(0)=sum rho=5.614 vs true per-step HS^2 rate <= mu*^2=3.67; loss squares at s=4.
## 23:30 — (1) pre-flight of the cone-field certificate: FAILS as designed [N]
- code/b_conecheck.py: cone K(a) around rank-one direction u_y; invariance under P_k needs |alpha0|>s2 and (|alpha0|-s2)^2>=4 s1 b0.
  raw norm: feasible at 0/40,0/40,0/40,4/40,7/40 random points for k=1,2,4,6,8 (median s2/|alpha0| 38,25,7.3,4.5,2.1);
  averaged-Lyapunov norm (J=8): 0,2,15,19,24 /40 (median 2.8,3.1,0.70,0.38,0.23).  A certificate needs EVERY cell/edge to pass.
  k-step letters need cells of tau-width w at each of k steps: ~lambda^{k-2}/w^2 cells (k=8, w=1e-3: ~4e10). => infeasible here.
## 23:35 — full Z: all four fixed twists 0,1/4,1/2,3/4 are slow (c_constZ: |Z(const t)|^{1/39} = 1.8817 for all four; 1/8 -> 1.4509).
  (sector shift: tau+1/4 <-> a+2).  N9b counted only 0,1/2 -> its Gamma_eff values are conservative upper estimates (still valid).
## 23:40 — N11 steering (modulus form): VERIFIED [P-sketch, bookkeeping] — see REPORT §1. Target for D1 becomes Gamma < T' (any beta>1,
  strictly), with NO 1.2329 and NO arithmetic (primality/omega) condition, provided A is e^{o(p)}; rank-p divisor sum
  exp(C p^{2-beta}) = e^{o(p)} is absorbed by the e^{~6.2e-4 p} budget for all large p.
- D2 with N11's certified constants (Cpow=3246.8, N1=573.59) is [P] but K_box ~ exp(6e6 * sum delta) — astronomically large per stay;
  the gas argument then needs an adapted norm = SAME open item as N11 §2 (bump interaction prefactor). Shared stay/bump lemma.
- (2) via G*: R_s <= max(Gamma_out^s, mu*^s/lambda) (variational principle + stays have ~0 entropy) -> R4<=2.611 needs Gamma_out<=1.2712.
## 23:55 — results in
- (2) e_r4_lower [CA]: arb Collatz-Wielandt lower bound on a 75-state principal submatrix: rho(M4(0)) >= 5.41151079436262 (s2 sanity 1.05111584).
- (1) f_preflight (4000 random 1024-grid cells outside 1/8 boxes of all 4 fixed points, W-norm): cone invariance holds at 41.6% (k=6),
  52.9% (k=8), 58.4% (k=12) of cells; max s2/|alpha0| 91/179/60.  => certificate as designed cannot pass; NOT launched as hours-long run.
- (4) d_h13 (p=13, c=47321, inc:79, 1794 classes): Gamma_raw=1.367 (A=1,s=0); slow time at {0,1/2} only: unchanged 1.367 (top class
  s=157 sits near 1/4,3/4); slow time at ALL FOUR fixed twists: Gamma_eff max 1.181 (theta=1/16), 1.104 (theta=1/8); top class -> 1.177 / 0.640.
- Note left: /workspace/bgs-lineN/N11/NOTE_FROM_N10b.md (new file).
