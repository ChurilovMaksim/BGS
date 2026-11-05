#!/usr/bin/env python3
"""Constant check for the conditional H5(b) cross-line sufficiency (BGS-TRACE-355) [CA].

(A) w_max(p) = max{w : (p-1)^w w! <= eps^p} (Lemma W, BGS-TRACE-342), exactly: eps^p = a_p + b_p sqrt2 and an integer
    X satisfies X <= a + b sqrt2 iff X - a <= 0 or (X - a)^2 <= 2 b^2; p = 1409 and 3307 (w_max = 112, 231; the source
    report's 228 at p = 3307 is wrong).
(B) rooms: the idealised slack of grok47 h5_factor.md Prop. 4 (research note on branch research-grok46-1104 @ f7986a9f,
    PR #85, not registered): slack(1409, robust delta) = 0.0201129655928..., slack(3307, fragile delta) = 0.0033471847517...
    (80-digit values copied from its logs/h5_factor.json; inputs, not recomputed here).
(C) thresholds c*(p, C) = [ln(2^{w_max} - 2) + ln C - ln slack(p)] / p for C = 1 (and the variants with no room, the
    source's 228, c_sharp and the crude p/ln(p-1) cap); and the direct check that c = 0.058, C = 1 gives
    (2^{w_max} - 2) e^{-0.058 p} < slack at both primes (so C <= 1 is enough).
Output ../logs/h5b_const.json.  Usage: python code/h5b_const.py
"""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, math, pathlib
from mpmath import mp, mpf, log, exp

OUT = pathlib.Path(__file__).resolve().parents[1] / "logs" / "h5b_const.json"
mp.dps = 80
SLACK = {1409: mpf("0.020112965592839825999768955618625953739134408912547077071274222758089719243256262"),
         3307: mpf("0.0033471847517073722854792437517753134485279674655607159165283717785594678028771909")}


def ab(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = a + 2 * b, a + b
    return a, b


def le_eps_pow(X, p):
    a, b = ab(p)
    d = X - a
    return d <= 0 or d * d <= 2 * b * b


def wmax(p):
    w, X = 0, 1
    while le_eps_pow(X * (p - 1) * (w + 1), p):
        X *= (p - 1) * (w + 1); w += 1
    return w


rows = []
for p in (1409, 3307):
    wm = wmax(p)
    X = (p - 1) ** wm * math.factorial(wm)
    assert le_eps_pow(X, p) and not le_eps_pow(X * (p - 1) * (wm + 1), p)
    cs = int(math.floor(p * math.log(1 + 2 ** .5) / math.log(p - 1))); crude = p / math.log(p - 1)
    row = dict(p=p, wmax=wm, csharp=cs, p_over_ln=crude, slack=str(SLACK[p])[:24])
    for name, w in (("wmax", wm), ("w228", 228), ("csharp", cs), ("crude", crude)):
        nl = mpf(2) ** w - 2
        row[f"c_noroom_{name}"] = float(log(nl) / p)
        row[f"c_room_{name}"] = float((log(nl) - log(SLACK[p])) / p)
    lhs = (mpf(2) ** wm - 2) * exp(-mpf("0.058") * p)
    row["c0058_C1_lhs"] = float(lhs); row["c0058_C1_fits"] = bool(lhs < SLACK[p])
    row["c0058_max_C"] = float(SLACK[p] / lhs)
    assert row["c0058_C1_fits"]
    rows.append(row); print(json.dumps(row), flush=True)
assert [r["wmax"] for r in rows] == [112, 231]
OUT.write_text(json.dumps(dict(rows=rows), indent=1) + "\n")
