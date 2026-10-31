#!/usr/bin/env python3
"""Isotropic case of Proposition N1.3 / Theorem W+ (BGS-TRACE-279, 280): coverage check.

Owner audit of PR #65, item R1.  For isotropic x the orbit sum S(x) is a Gauss period over a
subgroup (or coset) A of F_q^* of order tau >= p, and Theorem W+ needs |S|/tau <= eps_F on the
whole beyond-Weil range  c_W p^2 < q <= c_N p^{7/3}.  Available bounds (Cochrane-Pinner, QJM 62
(2011), Thm 1.1, lambda = 2/3^{1/4}; ranges as in the 5 Oct 2009 author preprint):
  (G)   |S| <= sqrt(q)                                   (any tau; Gauss period)
  (CP3) |S| <= lambda tau^{3/8} q^{1/4}   for  q^{1/2} <  tau <= q^{2/3}/3
  (CP5) |S| <= lambda tau^{5/8} q^{1/8}   for  3 q^{1/3} < tau <= q^{1/2}
Coset sums: sum_{x in gA} e(ax/q) = sum_{x in A} e(agx/q), so the same bounds apply.

Part 1 (analytic, all p): in log10 units Q = log q, t = log tau >= P = log p, e = log eps_F,
L = log lambda.  Split by Q:
  A: Q <= 2t + 2e            -> (G) gives |S|/tau <= eps.
  B: 2t + 2e < Q < 2t        -> tau > q^{1/2}; tau <= q^{2/3}/3 iff t <= 2Q/3 - log 3, implied by
                                t >= 3 log 3 - 4e (=: T_B1); and L + Q/4 - 5t/8 < L - t/8 <= e iff
                                t >= 8(L - e) (=: T_B2).
  C: 2t <= Q <= Q_top        -> tau <= q^{1/2}; tau > 3q^{1/3} iff Q < 3t - 3 log 3, implied by
                                Q_top = logc_N + 7P/3 <= logc_N + 7t/3 < 3t - 3 log 3 (all t > 0 when
                                logc_N < -3 log 3); and L + Q/8 - 3t/8 <= L + logc_N/8 - t/12 <= e
                                for all t >= 0 iff L + logc_N/8 <= e.
These three cases cover every q in the range for every tau >= p as soon as p >= 10^max(T_B1,T_B2).
The beyond-Weil part is non-empty only for p >= 10^264.5 > 10^max(T_B1,T_B2), so the isotropic
case is covered for ALL p (no upper limit), with all three Cochrane-Pinner/Gauss branches.
Part 2 (numerical grid, independent of the case split): scan log10 q over the range in steps of
0.01 for log10 p in [264.5, 400] (step 0.1) and, with 2000 points plus the case boundaries,
log10 p in {500, 1000, 1e4, 1e6, 1e9}, tau in {p, 3p} and
tau = p * 10^j; report uncovered points with all branches (expected 0) and with (G)+(CP5) only
(the registered text before R1; expected > 0 from p ~ 10^264.6 on).
"""
import json, os
from mpmath import mp, mpf, log10, sqrt

mp.dps = 50
HERE = os.path.dirname(os.path.abspath(__file__))
n2 = [json.loads(l) for l in open(os.path.join(HERE, '..', 'logs', 'n2_constants.log')) if l.startswith('{')]
fams = {r['fam']: mpf(r['log10_eps']) for r in n2 if r['budget'] == 'LineL eta/3A'}
L = log10(2 / mpf(3) ** (mpf(1) / 4))
L3 = log10(mpf(3))
LCW = mpf('-25.62')   # registered c_W (rounded down: smaller range bottom is harmless)
LCN = mpf('-113.80')  # registered c_N (binding family (+-2,8)V); uniform range of Theorem W+
ok_all = True

print('Part 1: analytic case split (log10 units), registered range q <= max(c_W p^2, c_N p^{7/3})')
for f, e in sorted(fams.items()):
    TB1 = 3 * L3 - 4 * e
    TB2 = 8 * (L - e)
    condC1 = LCN < -3 * L3
    condC2 = L + LCN / 8 <= e
    # beyond-Weil threshold: c_W p^2 < c_N p^{7/3}  <=>  P > 3 (LCW - LCN)
    Pmin = 3 * (LCW - LCN)
    good = condC1 and condC2 and max(TB1, TB2) < Pmin
    ok_all &= good
    print(f'  {f}: log10 eps_F = {mp.nstr(e,8)}; T_B1 = {mp.nstr(TB1,6)}, T_B2 = {mp.nstr(TB2,6)}; '
          f'C: logc_N < -3log3 {condC1}, L + logc_N/8 = {mp.nstr(L+LCN/8,6)} <= e {condC2}; '
          f'beyond-Weil from log10 p = {mp.nstr(Pmin,6)} -> {"COVERED for all p" if good else "FAIL"}')

print('Part 2: numerical grid in floats (all families, tau = p*10^j); step 0.01 in log10 q for log10 p <= 400,')
print('        2000 equispaced points plus the case boundaries 2t+2e, 2t, 1.5t for larger p')
import math
Lf, L3f = float(L), float(L3)
def branches(Q, t, e):
    r = []
    if Q / 2 - t <= e: r.append('G')
    if Q / 2 < t <= 2 * Q / 3 - L3f and Lf + Q / 4 - 5 * t / 8 <= e: r.append('CP3')
    if L3f + Q / 3 < t <= Q / 2 and Lf + Q / 8 - 3 * t / 8 <= e: r.append('CP5')
    return r
lcw, lcn = float(LCW), float(LCN)
Ps = [264.5 + 0.1 * i for i in range(0, 1356)] + [500.0, 1000.0, 1e4, 1e6, 1e9]
tot = bad_all = 0
first58 = None; n58 = 0
for f, e in sorted(fams.items()):
    e = float(e)
    for P in Ps:
        lo, hi = lcw + 2 * P, max(lcw + 2 * P, lcn + 7 * P / 3)
        if hi <= lo: continue
        for j in (0.0, L3f, 1.0, 5.0, 20.0):
            t = P + j
            if P <= 400:
                Qs = [lo + 0.01 * i for i in range(int((hi - lo) / 0.01) + 1)] + [hi]
            else:
                Qs = [lo + (hi - lo) * i / 2000 for i in range(2001)]
            for c in (2 * t + 2 * e, 2 * t, 1.5 * t):
                Qs += [c + d for d in (-1e-6, 0.0, 1e-6) if lo <= c + d <= hi]
            for Q in Qs:
                b = branches(Q, t, e); tot += 1
                if not b: bad_all += 1
                if f == '8V' and j in (0.0, L3f) and not ('G' in b or 'CP5' in b):
                    n58 += 1
                    if first58 is None: first58 = (P, Q)
print(f'  grid points: {tot}; uncovered with G+CP3+CP5: {bad_all}')
print(f'  (8V, tau in {{p,3p}}) uncovered with G+CP5 only (pre-R1 text): {n58}'
      + (f'; first at log10 p = {first58[0]:.1f}, log10 q = {first58[1]:.2f}' if first58 else ''))
ok_all &= (bad_all == 0) and n58 > 0
print('ISO_COVERAGE_OK' if ok_all else 'ISO_COVERAGE_FAIL')
raise SystemExit(0 if ok_all else 1)
