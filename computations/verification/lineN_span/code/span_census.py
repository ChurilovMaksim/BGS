#!/usr/bin/env python3
"""Exact census of the balanced eps-digit span on Z[sqrt2] (span theorem, BGS-TRACE-337..339).

Arithmetic: exact Python integers. Every comparison with sqrt2 is an exact sign test of
u + v sqrt2 (squares compared); floors use math.isqrt (Lemma 9 of the note). Floats are used
only (i) to choose a digit window, which is then checked exactly at both edges (assert), and
(ii) for the reported min/max defect span - L, recomputed with mpmath at 40 digits.
Derived from the independent referee census (audit of PR #83, 4 Nov 2026); does not import
PR #83 / PR #85 code.

Usage: python3 span_census.py [J=16]     (from the repository root)
Outputs: computations/verification/lineN_span/logs/span_census_J{J}.json and .jsonl
"""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import json, math, sys, time, pathlib
from math import isqrt
from collections import Counter
import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[4]
OUT = ROOT / 'computations/verification/lineN_span/logs'
J = int(sys.argv[1]) if len(sys.argv) > 1 else 16
mp.mp.dps = 40
EPS = 1 + mp.sqrt(2)

def sgn(u, v):  # exact sign of u + v sqrt2
    if u >= 0 and v >= 0: return 0 if (u == 0 and v == 0) else 1
    if u <= 0 and v <= 0: return -1
    if u > 0: return 1 if u * u > 2 * v * v else -1
    return 1 if 2 * v * v > u * u else -1

def floor_s2(U, V):  # exact floor(U + V sqrt2)
    if V == 0: return U
    r = isqrt(2 * V * V)
    return U + (r if V > 0 else -r - 1)

PW = {}
def pw(k):  # eps^k = p + q sqrt2
    if k not in PW:
        p, q = 1, 0
        for _ in range(abs(k)):
            p, q = (p + 2 * q, p + q) if k > 0 else (-p + 2 * q, p - q)
        PW[k] = (p, q)
    return PW[k]

def theta(a, b, k):  # theta_k = (U + V sqrt2)/4, alpha eps^k = A + B sqrt2, U = 2B, V = A
    p, q = pw(k); A = a * p + 2 * b * q; B = a * q + b * p
    return 2 * B, A, B

def n_k(a, b, k):  # floor(theta_k + 1/2) = floor((U + 2 + V sqrt2)/4)
    U, V, _ = theta(a, b, k)
    return floor_s2(U + 2, V) // 4

def abs_ge_half(U, V):  # |(U + V sqrt2)/4| >= 1/2  <=>  (U + V sqrt2)^2 >= 4
    return sgn(U * U + 2 * V * V - 4, 2 * U * V) >= 0

def word(a, b):
    x1 = abs(a + b * math.sqrt(2)); x2 = abs(a - b * math.sqrt(2)); le = math.log(1 + math.sqrt(2))
    kL = math.log(1 / (2 * x1 * math.sqrt(2) / 4)) / le; kR = math.log(2 * x2 * math.sqrt(2) / 4) / le
    k0 = math.floor(kL) - 8; k1 = math.ceil(kR) + 8
    n = {k: n_k(a, b, k) for k in range(k0 - 2, k1 + 1)}
    for k in range(k0 - 2, k0 + 1): assert n[k] == 0, (a, b, k)          # exact left edge
    for k in range(k1 - 2, k1 + 1): assert n[k] == theta(a, b, k)[2], (a, b, k)  # n = T at right edge
    E = {k: n[k] - 2 * n[k - 1] - n[k - 2] for k in range(k0, k1 + 1)}
    nz = [k for k in sorted(E) if E[k] != 0]
    w = [E[k] for k in range(nz[0], nz[-1] + 1)]
    zr = max([y - x - 1 for x, y in zip(nz, nz[1:])], default=0)
    # exact K_L = min{k : |theta_k| >= 1/2}, K_R = max{k : |conj theta_k| >= 1/2}
    KL = next(k for k in range(k0 - 2, k1 + 1) if abs_ge_half(*theta(a, b, k)[:2]))
    KR = max(k for k in range(k0 - 2, k1 + 1) if abs_ge_half(theta(a, b, k)[0], -theta(a, b, k)[1]))
    return w, zr, nz[0], KL, KR, n

def eps_le(m, N2):  # exact test 2 eps^m < N  (N2 = N), returns sign of N - 2 eps^m
    p, q = pw(m); return sgn(N2 - 2 * p, -2 * q)

def floorlog(N):  # floor(log_eps(N/2)): largest m with 2 eps^m <= N
    m = -5
    while eps_le(m + 1, N) >= 0: m += 1
    return m

def classes(J):
    Nmax = 2 ** (J + 1); X = isqrt(int(Nmax * 5.83)) + 3; out = []
    for b in range(-X, X + 1):
        for a in range(-2 * X, 2 * X + 1):
            N = abs(a * a - 2 * b * b)
            if N == 0 or N >= Nmax: continue
            if sgn(a, b) <= 0 or a * b < 0: continue                 # sigma+ > 0, sigma+ >= |sigma-|
            s = sgn(a, -b)
            if sgn(a - s * (3 * a - 4 * b), b - s * (2 * a - 3 * b)) >= 0: continue  # sigma+ < lambda |sigma-|
            out.append((N.bit_length() - 1, a, b, N))
    return sorted(out)

def defect(N, span): return span - mp.log(mp.mpf(N) / 2) / mp.log(EPS)

t0 = time.time(); C = classes(J); res = []; FL = {}
bad_letter = bad_formula = bad_strict = 0
for j, a, b, N in C:
    w, zr, first, KL, KR, _ = word(a, b)
    s = len(w)
    if any(x not in (-1, 0, 1) for x in w): bad_letter += 1
    if N != 2 and s != KR - KL + 3: bad_formula += 1
    if N == 2 and (s, KR - KL + 3) != (2, 3): bad_formula += 1
    # strict two-sided bound L+1 < s < L+3  <=>  2 eps^(s-3) < N < 2 eps^(s-1), exact
    if not (eps_le(s - 3, N) > 0 and eps_le(s - 1, N) < 0): bad_strict += 1
    if N not in FL: FL[N] = floorlog(N)
    res.append(dict(j=j, a=a, b=b, N=N, span=s, zr=zr, KL=KL, KR=KR, fl=FL[N], word=w))
kappa = mp.log(2) / mp.log(EPS)
cnt = Counter(r['j'] for r in res)
hist = Counter(r['span'] - r['fl'] for r in res)
dmin = min(res, key=lambda r: defect(r['N'], r['span'])); dmax = max(res, key=lambda r: defect(r['N'], r['span']))
shellcap = {j: int(mp.floor(j * kappa)) + 3 for j in sorted(cnt)}
shell_att = Counter(r['j'] for r in res if r['span'] == shellcap[r['j']])
first_shell_att = {}
for r in res:
    if r['span'] == shellcap[r['j']] and r['j'] not in first_shell_att: first_shell_att[r['j']] = [r['a'], r['b'], r['span']]
idx = {(r['a'], r['b']): r for r in res}
def wit(a, b):
    r = idx[(a, b)]; return dict(alpha=f"{a}+{b}sqrt2", N=r['N'], j=r['j'], span=r['span'], zr=r['zr'], word=r['word'],
                                  defect=mp.nstr(defect(r['N'], r['span']), 15))
w2 = word(2, 0)
out = dict(
    J=J, arithmetic='exact integers (sign tests in Z[sqrt2], isqrt floors); mpmath dps 40 for defects only',
    n_classes=len(res), counts=dict(sorted(cnt.items())), excess_hist_span_minus_floorL=dict(sorted(hist.items())),
    n_letter_outside_pm1=bad_letter, n_span_formula_failures=bad_formula, n_strict_two_sided_failures=bad_strict,
    n_viol_floor_plus3=sum(r['span'] > r['fl'] + 3 for r in res),
    n_viol_shell_form=sum(r['span'] > shellcap[r['j']] for r in res),
    n_span_gt_2j_jge2=sum(r['j'] >= 2 and r['span'] > 2 * r['j'] for r in res),
    defect_min=dict(alpha=[dmin['a'], dmin['b']], N=dmin['N'], value=mp.nstr(defect(dmin['N'], dmin['span']), 12)),
    defect_max=dict(alpha=[dmax['a'], dmax['b']], N=dmax['N'], value=mp.nstr(defect(dmax['N'], dmax['span']), 12)),
    c_eps=mp.nstr(kappa, 16), shellcap=shellcap, shell_form_attained_count=dict(sorted(shell_att.items())),
    shell_form_first_attaining=first_shell_att,
    shells_never_attaining=[j for j in sorted(cnt) if j not in shell_att],
    alpha_2=dict(n_k_minus2_to_4=[w2[5][k] for k in range(-2, 5)], word=w2[0], span=len(w2[0]), floorL_plus3=FL[4] + 3),
    witnesses=[wit(116, 0), wit(0, 82), wit(118, 0)] if J >= 13 else [],
    shell2_span4=[[r['a'], r['b']] for r in res if r['j'] == 2 and r['span'] == 4],
    eps4_gt_32=dict(eps4='17+12sqrt2', test='12 sqrt2 > 15 <=> 288 > 225', exact=sgn(17 - 32, 12) > 0),
    secs=round(time.time() - t0, 1))
OUT.mkdir(parents=True, exist_ok=True)
(OUT / f'span_census_J{J}.json').write_text(json.dumps(out, indent=1) + '\n')
with open(OUT / f'span_census_J{J}.jsonl', 'w') as f:
    for r in res: f.write(json.dumps({k: r[k] for k in ('j', 'a', 'b', 'N', 'span', 'zr', 'KL', 'KR')}) + '\n')
print(json.dumps(out, indent=1))
