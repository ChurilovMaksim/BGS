# NOTES_N8b (Line N8b)
## 21:34 — start. Read N7/REPORT_N7.md, N7b/NOTES_FROM_N7.md.
- Read N7 REPORT (Lemma P' [P], identity (I), Prop X' [P-sketch], A-infinity) and NOTES_FROM_N7.
- Factorisations p<62 (code/a_fact.py -> logs/a_fact.json): h_p composite at p=11,13,17,23,31,37,41,43,53,61.
- KEY ALGEBRA (derived 21:50): gamma = x_{k+1}+y_k sqrt2, N(gamma)=+-h_p. From eps^p - (-1)^k = sqrt2 gamma eps^k and conj:
  eps^p + (-1)^k = +- sqrt2 gammabar eps^{k+1}.  For c | h_m and the CONSISTENT line {s*gamma_3 mod c} (frak c | gamma_3):
  (eps^{M} - sigma) beta / c in sqrt2 O  => tau_i(beta) == sigma*Tr(eps^{2i-M} beta)/c (mod 1) exactly (M = p if c|h_p, 3p if c|K_p), sigma=(-1)^{k_M+1}.
  => two windows per period M, each of length log_lam(c/N(f)) + O(1), depth N(f) = min|N(Y)|/c, Y in 8beta + cO.
  Consistent c-line = c-torsion of the h_M isotropic line; in N7 terms x = z + e gamma/(8q) with e = +- f * gbar'' (N(e) = (q/c) N(f)).
  So these classes are DEEP classes of gap (a) (depth >= q/c >= 2p+1) but carry weight ~2/c per point at level c instead of 2/q: amplification q/c.
## 22:20 — code
- code/b_cline.py (c-line class sums, Lin convention, exact identity check, rounding floor), jobs code/jobs1.txt via code/run_jobs.sh -> logs/b_cline.jsonl.
- code/c_kappa.py -> logs/c_kappa.out [CA arithmetic]: kappa_2 floor with Lam=mu*: 0.7060 (certified r2); 0.678 if r2=1 [H]; 0.5 iff r2 = mu*^2/lam.
  s-th Schatten moments: kappa_s(Lam_8V, R_s=mu*^s/lam) = 0.5211 (s=3), 0.5138 (4), 0.5068 (5). For kappa<=0.55 need R_3<=1.3284 (floor 1.2058), R_4<=2.611 (floor 2.310).
- First b_cline results: calibration c = h_37 full line: depth-4 class |r| = 3.95e-4 = |w*| (the family) OK.
  depth-4 'family analogues' at c|h_p: |r| = 1.31e-8 (q/c=47,p=23), 1.67e-10 (223,p=37), 6.1e-18 (37223), 2.2e-24 (8.3e6), 3.8e-25 (8.76e6):  |r| ~ N(e)^{-3.0..-3.2}.
- code/d_puni.py: exact rewrite of a c-line class as N7 (z,e) point; twist identity err = 0 exactly; p-uniformity: (z,e)=((6+6r2)/8, 118+84r2), N(e)=-188:
  p=23: 1.08869e-8+7.36498e-9i ; p=31: 1.08941e-8+7.34779e-9i.  => c-line class ratio IS N7's w(z,e) at e = f*gbar''.
## 22:45 — results batch 1 (logs/b_cline.jsonl, logs/e_summary.out, logs/d_puni.jsonl)
- 44 runs, identity_bad = 0 everywhere (exact identity tau_i = sigma Tr(eps^{2i-M}beta)/c).
- c = h_p lines (calibration): rel ~ 1.15 (family + gap-(a) residue), top class depth 4 |r| = 3.95e-4 = |w*|.
- rank-p consistent lines, c|h_p proper: rel_abs = 1.2e-3 (q/c=23,p=11), 1.7e-3 (47,p=23), 3.5e-5 (79), 1.7e-4 (103), 1.0e-4 (223,p=37), 1.0e-9 (3.7e4), 1.8e-14..5e-14 (8.3e6).
  Fit rel_c ~ (1.4..5)*(q/c)^{-2} [N]. Pointwise decay exponent beta_min over top classes: 2.06..4.2 (|r| ~ |w*|(N(e)/4)^{-beta}).
- inconsistent lines (c composite): 1e-15..1e-18 (one forced window/period).
- rank-3p lines (c|K'): <= 3.6e-7 (p=13), 7.5e-11 (19), 1.4e-16 (29), 3.8e-23 (37), 4.6e-26 (41), <= 2.7e-36 (61, at rounding floor).
- signs MIXED (e.g. +1.4e-3 at q/c=47, -6.7e-4 at 23): no positivity to exploit.
- d_puni: p-uniformity confirmed when forced windows >= ~8 steps (rank p, c >= ~1e6): e.g. (37,1953705007): -6.0464e-18 at p=37, -6.0468e-18 at 41,53,61.
  For short windows (rank 3p, c ~ 1e4) the actual value is 1e3-1e4 x LARGER than the long-window limit w(z,e): w-limit is NOT an upper bound there.
- fixed points: (lam-1) = 2 eps, fixed set (sqrt2/8)O/O^vee (4 points); d_puni z chosen accordingly (8z in sqrt2 O).
- jobs2 (inconsistent fully-isotropic lines AT c = h_p, composite h_p) launched: not covered by N7 Lemma P' (only (gamma),(gammabar)).
## 23:20 — batch 2 + fits
- Inconsistent fully-isotropic lines AT c = h_p (composite h_p; not covered by N7 Lemma P'): rel_abs 2.7e-3 (p=11), 7.9e-3 (p=13), 5.9e-5 (17), <= 4.6e-14 (37), <= 1.5e-14 (41), 1.5e-18 (43). Bookkeeping: they are conductor h_p => gap (a)/(b') (flag for N7 author).
- Gamma_eff (code/f_gamma.py -> logs/f_gamma.out): <= 1.069 on all residual (c < h_p) lines; 1.267 at p=13 inconsistent line at h_p (small p).
- (beta_min column in e_summary is meaningful only for consistent lines.)
- Summation lemma: primes r | h_p satisfy r == 1 mod 2p [P] (2 is a QR mod r since x_p^2-2y_p^2=-1; ord(eps mod frak r) | 2p, not | 2).
  => sum_{d|h_p,d>1} d^{-delta} <= exp(2(2p)^{-delta} omega^{1-delta}/(1-delta)) - 1 -> 0 for delta > 1/2.
- Writing REPORT_N8b.md.
## 23:35 — finalisation
- REPORT_N8b.md written (sections 0-10 + erratum candidate for N7 Lemma P'(i): 4 fixed points (sqrt2/8)O/O^vee, not 8; N7's checks used z in {1/4, 0}, both genuine).
- Residual-line max Gamma_eff = 1.069 (p=17, c=15607, deep class); inconsistent at c=h_p (gap a/b'): 1.267 at p=13.
- Conditional theorems: C1 (G(Gamma,A), Gamma<1.2329, A p-independent, + A-infinity) ; C2 (h_p prime subsequence, Gamma<T'=1.4279, e^{o(p)} slack).
- Mixed gap: not settled; kappa floor 0.7060; targets R3<=1.3284 / R4<=2.611 for kappa<=0.55.
- SHA256_N8b.txt over code/ logs/ NOTES REPORT; self-hash SHA256_N8b.txt.sha256. Nothing pushed; N7b untouched.
