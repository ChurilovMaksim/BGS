#!/usr/bin/env python3
"""Checks for the polymer gap constant (BGS-TRACE-353).

For F(x) = sum_{k<=K} a_k x^k with integer |a_k| <= A and sigma = +-1:
    |F(sigma eps)| |F(sigma epsbar)| < A^2 eps^{K+2} / 2,
hence d <= |N F(sigma eps)| forces K > log_eps d - 2 log_eps A - log_eps(eps^2/2), log_eps(eps^2/2) = 1.21355...
(A) the constant at 60 digits and the identity eps^{K+1}/sqrt2 * 1/(2 - sqrt2) = eps^{K+2}/2;
(B) exhaustive [CA]: every nonzero coefficient vector with |a_k| <= A, for (A, K) in {(1, 0..9), (2, 0..5), (3, 0..3)},
    computes the exact integer norm N(F(sigma eps)) = u^2 - 2 v^2 (F(sigma eps) = u + v sqrt2) and checks
    |N| < A^2 eps^{K+2}/2 (mpmath, 60 digits); reports the largest ratio |N| / (A^2 eps^{K+2}/2) (sharpness).
Output ../logs/polymer_const.json.  Usage: python code/polymer_const.py
"""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import itertools, json, pathlib, time
import mpmath
from mpmath import mp, mpf, sqrt, log

OUT = pathlib.Path(__file__).resolve().parents[1] / "logs" / "polymer_const.json"
mp.dps = 60
eps = 1 + sqrt(2)
const = log(eps ** 2 / 2) / log(eps)
assert mpf("1.213") < const < mpf("1.214")
ident = max(abs(eps ** (K + 1) / sqrt(2) / (2 - sqrt(2)) - eps ** (K + 2) / 2) / eps ** (K + 2) for K in range(50))
assert ident < mpf(10) ** -55


def powers(K, s):  # (s eps)^k = (u_k, v_k)
    out, u, v = [], 1, 0
    for _ in range(K + 1):
        out.append((u, v)); u, v = s * (u + 2 * v), s * (u + v)
    return out


t0 = time.time()
rows = []
for A, Ks in ((1, range(10)), (2, range(6)), (3, range(4))):
    for K in Ks:
        bound = A * A * eps ** (K + 2) / 2
        worst = mpf(0); n = 0
        for s in (1, -1):
            pw = powers(K, s)
            for a in itertools.product(range(-A, A + 1), repeat=K + 1):
                if not any(a):
                    continue
                u = sum(ak * p[0] for ak, p in zip(a, pw)); v = sum(ak * p[1] for ak, p in zip(a, pw))
                N = abs(u * u - 2 * v * v); n += 1
                r = N / bound
                assert r < 1, (A, K, a, s)
                worst = max(worst, r)
        rows.append(dict(A=A, K=K, polys_times_signs=n, max_ratio=float(worst)))
        print(json.dumps(rows[-1]), flush=True)
res = dict(log_eps_eps2_over_2=mpmath.nstr(const, 30), identity_max_rel_err=mpmath.nstr(ident, 3), rows=rows,
           all_below=all(r["max_ratio"] < 1 for r in rows), seconds=round(time.time() - t0, 1))
OUT.write_text(json.dumps(res, indent=1) + "\n")
print(json.dumps({k: v for k, v in res.items() if k != "rows"}))
