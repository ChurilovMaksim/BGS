# NOTES_N2 — Line N2: the inherited level h_p as a periodic-orbit / pressure problem
(Working log. Times are Asia/Yekaterinburg, UTC+5. REPORT_N.md is under concurrent referee audit and was NOT modified. Nothing pushed.)

Labels: [P] proved (modulo explicitly named standing inputs from Lines F/J3/K/K2/L/L3), [CA] computer-assisted rigorous (arb ball arithmetic),
[N] numerical (floating point, no error control), [H] heuristic.

## 1. Setup checks (code/a_index_identity.py -> logs/a_index_identity.json)
- [P + N] Fix(A^p) has 4 h_p^2 points, A^p - I = h_p B with det B = -4, so G_p=(1/h_p)Z^2/Z^2 has index 4 in Fix(A^p) (checked for p<=47).
  ERRATUM to REPORT_N §7/N4 and to the brief: the index is 4, not 32 = N(4 sqrt2). (Not edited in REPORT_N; recorded in REPORT_N2 §1.)
- [P + N] O/h_p -> (Z/h_p)^2, y -> (Tr y, Tr lam y) mod h_p, is a bijection; Fourier identity for E_{G_p} prod g(A^i y) checked at p=5 (err ~1e-13).
- Attribution: REPORT_N's N3 (slow beta at prime scarred conductors) duplicates L2 Prop S; only composite conductors (e.g. h_p) are new.

## 2. Theory (a),(b)
- Theorem A (weighted K2'): Omega^F_m(k,a) with |W_{c,beta}| weights and exp(S_m psi_{k,a}); implies H_mid => (Theorem K) R' false. Non-trivial:
  the N3 slow orbit contributes (mu*/lam^{1/3})^m ~ 1.0644^m < T^m (uses the Line F spectral gap ||L_4^n|| <= C mu^n).
- Theorem B: Zhat_beta at c=h_p = sum a_F Tr(J_F M_F(y)^3), y in G_p; E_{G_p} = cyclic-state-path sum (lattice B^{-T}Z^2); Bowen-ball lemma.

## 3. Pressure reduction (c)
- Theorem C: limsup (1/p) log E_{G_p}|Zhat^F| <= log Lambda^F_{k'} + log r_2^F(k) + eta.
- 16:10–16:45: tried a u-only continuous discretisation of the carry automaton (code/b2_u_operator.py): Perron 1.0006–1.016, INCONSISTENT with
  r_abs=1.0511 — the Perron eigenvector lives on the countable set U={b - a/lam} and is not continuous in u. Abandoned (kept for the record).
- 16:50 KEY FIX (rigorous r_2 with no tail): rho_hat_i = |u_hat_i|^2 >= 0 is majorised pointwise by g_i = (truncation |d|<=V) + eps_i;
  exact collisions with letters <= V have carries <= V/4 (Green kernel sums to exactly 1/4: (lam+1)/((lam-1)(lam-1/lam)) = sqrt2/(4 sqrt2)).
  So the finite automaton with E0 = floor(V/4) is EXACT for the majorant -> finite Collatz–Wielandt in arb (code/e_r2_cert.py).
  [CA] r_2(4000) <= 1.0529012 (8V), 1.0519234 (8E), 1.0534557 (16V), 1.0529202 (16E). Matches float b_r2_float.py.
- JSR input Lambda (op-norm sup over the torus of k'-step twisted products) NOT certified:
  [N] c2: periodic points of period <=4: max spectral rate = mu* (fixed points); sup sampling = constant-twist point: 2.12342/2.01677/1.98242 at k'=10/20/30.
  [N] c3 beam search: greedy, useless (stuck in low branches). c4 coordinate ascent over FREE twist sequences: maxima = constant tau=1/2 plus
  boundary excursions: k=12: 2.1172 (const 2.0873); k=24: 2.0138 (const 1.9995) — consistent with free JSR = mu* (boundary transients only).
  [N] c5 Lyapunov ellipsoid from L_{1/2} alone: fails (9.15) — a certificate would need an SDP extremal norm over the tau family + truncation control.
- Thresholds: need Lambda*r_2 < T^3: 8V Lambda < 2.00859; 8E < 2.01046; 16V < 3.04126; 16E < 3.04280.
  At k'=30 with the [N] value 1.98242: rate (1.98242*1.05290)^{1/3} = 1.27799 < 1.28359. Asymptotic (mu*): 1.26344.

## 4. Level split numerics (code/d_level_split.py)
- (m,q)=(15,41): unit-part rate 1.1209, isotropic-part rate 1.0559, both < 1.28359 (max single unit point rate 1.441 — single points can exceed T,
  the average does not).
- (21,239): see logs/d_level_split.jsonl (filled in REPORT_N2 when finished).

## 5. (d)
- Pressure lever covers only 'light' (unit) points at h_p and conductors d >= h_p kappa^{-p/2}. Blocked: isotropic lines at every q | h_p,
  small divisors, K_p-prime and mixed rank-3p conductors in (c_N p^{7/3}, L_m). Index-loss barrier [P] shows the pressure method cannot reach
  them. No refutation of R' along m=3p.

## 6. Resume after interruption (2026-10-31 17:00 +05)
- Referee (/workspace/audit/lineN/REPORT.md) confirms index 4 ([O^vee:O]=8 missed); N-F2: source N3's |Z_rho| lower bound per family from
  TRACE-198 [CA] (rho(L_0^F) >= mu*), with r > 2(N+k). Incorporated in REPORT_N2 §1.1 and §2. REPORT_N.md untouched.
- r_2 certificates rerun with the rounding guard: logs/e_r2_cert.jsonl (16 runs, all four families, k=200..4000); values match the table (rounded up).
- (21,239) level split still running (started 16:37 +05; expected ~45 min CPU).
- 17:10 +05: the (21,239) d_level_split process had vanished without output (load avg ~34 from audit jobs). Restarted 17:11 +05,
  PID 3104943, appending to logs/d_level_split.jsonl. Not waited for; REPORT_N2 marks it pending. Conclusions do not depend on it.
- Manifest SHA256_N2.txt written at the end of the session (it excludes the still-growing d_level_split.jsonl/.err).
