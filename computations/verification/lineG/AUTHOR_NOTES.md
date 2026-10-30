# Line G notes (resume point). Started 2026-10-30 12:43 CET
- Inputs: Line E REPORT/doc, audit class sums T_{k1,full}_eta2.0_m{5..15}.npy in computations/verification/lineE/referee/logs (T[r] = sum over period-m z-orbits with Q(z)=r).
- |Z(nu)|^2 = h^-2 |S(v)|^2, S = ifft(T)*h, v = -(16 nu y')^-1 mod h  (aud.py Zabs2_all).
- Plan step1: rational reconstruction of N = nubar mod h (2D lattice), height vs |Z|^2.
- 13:00 code/classes_orb.c (orbit-canonical class sums, independent of audit classes.c): matches audit T to 1e-11 at m=11,13,15 (k1), 11,13 (full). m=15: 331 s. batch_orb.sh running m=15 full, then m=17 k1, m=17 full (~3.5h each) -> logs/Torb_*_m17.bin
- code/law.py: GENERAL rational-reconstruction law: any (a,b) with b nu ≡ a (mod 2h), k=(b nu-a)/2h:
  -nu P/2h = -(2a/b) q - kP/b exactly; P mod b via automaton (u,w)->(6u-w+n psi1, u+n psi0), contrib psi0 n^2+2nu, psi0=y', psi1=3y'-2h.
  Z = (1-lam^-m) Tr_H[(I x <1|) L^m (I x d0)].  check_law: 34/34 agree 1e-14..1e-9 vs brute n-sum (m=5,7, random weights) when coupling moderate;
  14 'BAD' are large |a|/b reps where Galerkin overflows (numerical, not law failure).
- step1 (logs/step1_*.log): families seen: N≡±4 (dominant), ±8, ±2, ±8/3, and N≡±4 mod h/d for d|h (d=7 when 3|m, d=41 when 5|m): |Z|^2 ≈ |Z*|^2/d^2.
  Non-resonant rest F/2m ≈ 2.0-2.2 (= B^sym/2m + chi ≈ 2, the COE/Γ-diagonal value).
- 13:25 box: check_dilution.py: dilution identity (Gauss sum over O/d + translated-kick sums) EXACT, 49 cases, err<=3e-14 (logs/check_dilution.log).
- step1e (logs/step1e_k1.log): fixed primaries PR={±(2,8),±(2,16),±(2,4),±(6,16)} [N≡±4,±8,±2,±8/3] + dilutions d|h, d<=sqrt h.
  nonres F/2m: m9 1.453, m11 1.782, m13 1.940, m15 2.070 (target 2). W'/m = -1.10,-0.44,-0.12,+0.14.
- tier2.log: growth rates r (|Z|^2~r^{2m}): (2,8) 1.915; (2,16) 1.615; (2,4) ~1.50; (±22,96) 1.41; (±2,12) 1.35; (4,18) 1.33. threshold lam^{1/4}=1.554.
  => asymptotically relevant k1 primaries: N≡±4, ±8 only. tier2full: full kick = 49× images, same r (1.92,1.65,1.49).
- predict17_law.py running (law L10 rho2.6 K50) -> logs/predict17_law.json. Then write PREDICTIONS_m17.json BEFORE Torb_*_m17 finishes.
- 13:45 PREDICTIONS_m17.json registered (sha fa8505f5...), no m17 output existed. Lean lean/LineG.lean compiles (phase_split, u_succ, w_succ, quad_form, nsw_dvd), axioms std only. logs/lean_LineG.out
- step1f: bulk F/2m insensitive to height cutoff H; k1 vs full nearly identical (kick-universal bulk): m9 1.45/1.43, m11 1.78/1.80, m13 1.94/1.96, m15 2.07/2.04.
- moment hierarchy idea: family with growth r matters for 2k-th moment iff r > lam^{1/(4k)}; 2nd tier r≈1.41>lam^{1/8}=1.2465 => 4th moment of bulk diverges (CLT moment form fails), mean OK.
- growth_law.py running: law |Z|^2 for primaries m=9..29.
- 13:40 box: formula_table (P*=±4,±8 + dilutions d|h<=sqrt h; full: +49x images + virtual level-7): W'_act/m k1 −0.82,−0.31,−0.04,+0.23; full −1.11,−0.33,−0.03,+0.14 (m=9..15). Nearly kick-universal -> testing eta-scan (code/eta_scan.py, logs/eta_scan.log).
- growth_law: r(±4) = 1.9154732 stable m<=29.
- REPORT.md draft written (G1–G7, tables, R′, rigor, literature). §5 m=17 pending. Corrected G4 claim: full kick only approx 7-periodic.
- check_law.py rerun with log -> logs/check_law.log.
- RESUME (box 13:35): eta_scan done: bulk F/2m NOT kick-universal; rises with m toward ~2 at all eta, faster for larger eta (m13: .86,1.83,1.92,1.93,1.97 for eta .5,1,2,3,4).
- PR #57 fetched (local ref pr57 only, no push): TRACE-183..196 cross-referenced in REPORT §8.
- eval17.py (registered definitions, PASS/FAIL) + watch17.sh detached: auto-evaluates when 'done k1 17'/'done full 17' appear -> logs/eval17_*.log. Dry-run on m15 OK (bulk 2.0704 reproduces step1e).
- batch_orb + classes_orb reniced to 10 (yield to Line E certificate). m17 k1 ETA several hours.
- REPORT.md finalized except §5 outcome (pending).
