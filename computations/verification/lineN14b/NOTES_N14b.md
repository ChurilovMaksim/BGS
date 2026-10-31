# NOTES_N14b (Line N14b) — subgroup-C' lemma: E_{H_d}|r| <= e^{o(p)} d^c (1.2744/mu*)^{3p}, c < 0.387
## 2026-11-01 01:23:54 +0500 — start; pre-flight of arguments (A) trivial, (B) coarser-separation Bowen ball, (C) min-shift+pressure,
   (D) Poisson/collision automaton with target ideal, (E) stay counting on H (geometry of numbers). Jobs nice 19, sequential.
## 2026-11-01 01:26:16 +0500 — pre-flight results (code/a_cvalues.py, code/b_g0.py; logs/*.json)
- need: c*theta*ln(lam) < -ln(eps*0.2945) = 0.3411; c* = 0.387 at theta=1/2.
- (A) trivial c=1 -> d <= 1.4065^p (= C' range).
- (B) separation time n=p-log_lam d for H (admissible ideal => [P]); C' on window n, leftover l=log_lam d by sup ||P_l|| <= C Lfree^l [CA]:
  c_B = ln(Lfree^3/(Lam r2))/ln lam = 0.7375 -> d <= 1.588^p. [P-sketch, on C' inputs]. With Prop-E majorant sup instead: c=0.95 (worse).
- (C) min-shift + pressure: slow fixed point forces c(1/2) >= 0.826. Dead for theta near 1/2.
- (D) Poisson/automaton: g(0)=(sum|J_a(1.8)|)^2 = 5.614 (> threshold 3.58); kappa=0.915, c_D=0.899. Majorant too peaked at slow twist. Dead.
  Also: nonzero targets b in 𝔟 have |b'| >= 1/(40 d V) so integer carries grow ~lam^p/(dV): no finite exact automaton; the
  congruence automaton mod 𝔟 is just the H-average restated (circular).
- (E) stay counting on H: no excess for stays s <= p-log_lam d [P-sketch]; but outside segments still need H-equidistribution (D1-type), dead per N12b.
- verdict: best c = 0.7375 (B). Covers h_p whose largest proper divisor <= 1.588^p (prime or balanced semiprime); p<=89: only p=31 newly covered [N].
## 2026-11-01 01:26:47 +0500 — REPORT_N14b.md written; next: SHA256 manifest (last action, nothing appended after).
