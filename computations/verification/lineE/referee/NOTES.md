> **Repository copy.** Absolute scratch-directory paths of the audit machine are replaced by placeholders in angle brackets (`<referee-dir>` = the first referee's working tree, copied to `computations/verification/lineE/referee/`; `<referee2-dir>` = this audit's working tree, copied to `computations/verification/lineE/referee2/`; `<author-packet>` = the author packet; `<audit-clone>` = a fresh clone of the repository). They are not part of the repository. The text is otherwise unchanged.

# Audit Line E notes
- 06:35 started; read REPORT/NOTES/OVERLAP
- 06:50 Paper check E1: derived independently. Z(nu)=sum Phihat e(-2nu q), q=n^T H^-1 n; -2nu q - q/2 = k h q/2 = k r/(8h), r=n^T X n, X=h(y' x_d - 2h y_d) => mod 8 using x_d=(-1)^d mod4, y_d=d mod2, y' odd => kappa=k y' mod 8. CORRECT. gcd(N,D)=1 automatic (N odd, N=-4 mod h). (1+4/N) factor correct.
- E2 paper: s_j recursion, diag term c(1+lam^-m)/(2(1-lam^-m)) matches; c_a Gauss sum; trace formula per word (affine contraction slope lam^-m) fine; Hardy H^2(D_rho) trace class since sum of weighted composition ops each with ||.||_1<=e^{2pi c|n|rho}/(1-theta). Lidskii OK (Hilbert). m-independence real (c_a depends on m mod 8 only).
- SCOPE ISSUE (major): TRACE-179 Conj R is for Line B's fixed 32-mode kick f (14 diagonal modes). k1 kick (0.9cos 2pi q) is a DIFFERENT, parity-even kick (chi_m==1). E5/E6 'Conj R fails' only for k1-analogue. E8 (full kick) is numerical only.
- TRACE-180 'contradicted': atom of mass 1/phi(h)->0 does not refute weak CLT; only moment version. Overstatement.
- cert.py: powers_bound cache keyed by id(Y) w/o holding ref -> id reuse possible (sector 6 may reuse sector 2 norms). Benign because L_6 = R L_2 R (R: phi(s)->phi(-s), unitary) -- I derived w_a(-n)=w_{-a}(n). Need rerun with cache fixed.
- E8: 49 not invertible mod h when 3|m (7|h_m). Scope.
- Independent F_m plan: class sums T(r) over gamma in Z[sqrt2]/h, |Z(nu)|^2 = h^-2 |sum_r e(v r/h) T(r)|^2, r=Q(z0,z1)=z0^2-6z0z1+z1^2, v*=4bar*ybar' (to verify sign numerically).
- 07:20 code in <referee-dir>/code (aud.py, classes.c, e1_exact.py, tmop.py, cmp_tm.py, direct_trace.py, run_classes.py). logs in ../logs.
  * e1_exact: identity exact for m=5..25 (40 random n each), kappa 7,5,3,1 table m<=41 OK; control nu*+2 fails; minus residue gives conj form.
  * class sums (my derivation: |Z(nu)|^2=h^-2|sum_r e(v r/h)T(r)|^2, v=-16bar nubar y'bar) validated vs n-sum (m=5 k1).
  * k1 eta=2 F/2m: m5 1.843, m7 2.805, m9 4.839, m11 6.894, m13 11.197. full: m11 5.5617 (=TRACE-182 5.56), m13 8.5896 (=author/LineB 223.3285).
  * full kick top residues N=+-196 mod h at m=7,11,13; none at m=9 (7|h_9). Removing +-196 at m=11 -> F/2m 2.04 (~baseline 4m/2m) => E10 numerically confirmed.
  * TO (my collocation code, L=10 rho=2.6) vs exact class |Z(nu*)|^2: rel 2e-9..6e-9 for m=5..13. L=6: 3e-5 (truncation).
  * direct dense traces at N=h-4 (m=5..11) vs TO with c(1+4/N): rel 6e-9..2e-8, complex ratio TrU/TrM matches to 1e-6. |TrM|=1.
  * NIT: author's predict_finiteN used L=12 with rho=2.0 < 12/(lam-1)=2.48 (trace-formula hypothesis violated; numerically harmless).
  * m=15 class sums running in background -> logs/classes_m15.out
- 07:45 Lean: lake exe cache get (no download) + lake env lean on copy w/ #print axioms: pell [propext], xy_mod [propext,Classical.choice,Quot.sound], certs [propext]; control evaluates false; my Neg.lean (cert 3 181 = true) FAILS as expected. Lean = finite fragment only (coefficient congruences m<=21, pell/xy_mod all d). Author log lacks axiom output (nit). Not integrated into formalization/Bgs (fix).
- own_bounds.py: E4/E5 arithmetic reproduced exactly for L6/L8b eta=2, eta=1.5, 1.75; all bounds < true values (TO numerics). m0 values for all 9 certs reproduced.
- eta=1.5: F/2m bound >2 only from m=21 (2.02), >2.5 only m in [23,33]: the 'violation' range is narrower than the positivity range [17,33] quoted in E5. eta=1.75 violation (F/2m>2.5) m in [19,27].
- cert rerun (original code) reproduces cert_L6.json (b11 differs ~1e-88: numpy eigvec nondeterminism; harmless).
- h_m factorizations all confirmed (logs/h_factor.log).
- OVERLAP nits: 't* coincidence' = identity h_{m-2}*y_{(m-1)/2} == 1 mod h_m (t*=y_{(m-1)/2}: 35=y_3, 1189=y_5); missing TRACE-117..119 (Pell-dimension spikes), FM-036 in overlap table.
- KM: abstract checked; no pseudo-symmetry operator exhibited -> 'concrete instance of KM pseudo-symmetry' is overstatement; resonance is m-specific (reciprocity, effective dual dimension -4), not a symmetry of U.
- 08:10 cert no-cache rerun: sector 6 identical to sector 2 (exact symmetry L_6=R L_2 R); in original run timing shows no cache hit -> latent bug only (nit F-fix).
- cert negative controls: K=60 -> sector4 fails; r1=1e-16 -> sector4 fails; r2=0.85 -> sectors 2/6 fail (rho 0.877). Behaves correctly.
- E10: full m=11 residues N=+-196 carry 3.52 of F/2m=5.56; remainder 2.04 (baseline ~2). m=13: 6.46 of 8.59, remainder 2.13. Confirmed numerically.
- waiting for m=15 class sums (k1 then full). Then write REPORT.
- 08:30 k1 m=15: F/2m=27.885 (author 27.9 OK), |Z(nu*)|^2=73486698.75 == my TO L=10 73486698 (1e-8). Author's 'observed 7.3491e7' = |Z(-nu*)|^2 (73491466) -> E7 mislabel; 6e-5 discrepancy spurious.
- t* identity h_{m-2} y_{(m-1)/2} == 1 mod h_m verified m=5..79 (logs/tstar_identity.log).
- Corollary idea: pure mode-7 kick f7 has Z_f7(nu)=Z_k1(49 nu) => F_m(f7)=F_m(k1) when 7 not | h_m (3 not | m). E5 transfers to f7 at m in {17,19,23,25,29,31,35,37}. Still not Line B kick.
- full m=15 running; then write REPORT.
- 08:55 full m=15 F/2m=3.910 (diluted resonance N=+-196 mod h/7, 12 classes carry 1.745). REPORT finalized; backed up.
