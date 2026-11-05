#!/usr/bin/env python3
"""Constant check for the conditional H5(b) cross-line sufficiency (BGS-TRACE-355) [CA].

(A) w_max(p) = max{w : (p-1)^w w! <= eps^p} (Lemma W, BGS-TRACE-342), exactly: eps^p = a_p + b_p sqrt2 and an integer
    X satisfies X <= a + b sqrt2 iff X - a <= 0 or (X - a)^2 <= 2 b^2; p = 1409 and 3307 (w_max = 112, 231; the source
    report's 228 at p = 3307 is wrong).
(B) rooms: the idealised additive slack of THEOREM_DRAFT_v5 / BGS-TRACE-333 on main, recomputed here (not copied from
    the unregistered grok47 note / PR #85). With R = Re Lambda_lo' = 6.234e-4, n/h_p := 1, Y = X_tail = eps_* = 0,
    M = 2 (1+R)^p e^{-p delta} - 1, robin = e^gamma log log K + 0.6483/log log K - 1 (K = 4 h_p^2 + 3),
    slack = M - sqrt(1+robin) - e^{-0.28 p}:
      slack(1409, delta = 7.4115e-6)  = 0.0201129655...   # robust C <= 8.8e-4 of TRACE-333
      slack(3307, delta = 3.4962e-4)  = 0.0033471847...   # fragile C <= 0.082 of TRACE-333
    (mpmath 80 digits; matches the previously copied grok47 Prop. 4 values to all printed digits).
(C) thresholds c*(p, C) = [ln(2^{w_max} - 2) + ln C - ln slack(p)] / p for C = 1 (and the variants with no room, the
    source's 228, c_sharp and the crude p/ln(p-1) cap); and the direct check that c = 0.058, C = 1 gives
    (2^{w_max} - 2) e^{-0.058 p} < slack at both primes (so C <= 1 is enough).
Output ../logs/h5b_const.json.  Usage: python code/h5b_const.py
"""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, math, pathlib
from mpmath import mp, mpf, log, exp, log1p, sqrt, euler

OUT = pathlib.Path(__file__).resolve().parents[1] / "logs" / "h5b_const.json"
mp.dps = 80
R = mpf("6.234e-4")
# TRACE-333 / V5 deltas at the two binding primes
DELTAS = {1409: mpf("7.4115e-6"), 3307: mpf("3.4962e-4")}


def ab(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = a + 2 * b, a + b
    return a, b


def h_nsw(p):
    a, b = 1, 7
    for _ in range((p - 1) // 2 - 1):
        a, b = b, 6 * b - a
    return b


def le_eps_pow(X, p):
    a, b = ab(p)
    d = X - a
    return d <= 0 or d * d <= 2 * b * b


def wmax(p):
    w, X = 0, 1
    while le_eps_pow(X * (p - 1) * (w + 1), p):
        X *= (p - 1) * (w + 1); w += 1
    return w


def idealised_slack(p, delta):
    """V5 / TRACE-333 idealised room for |X_cross| after putting e^{-0.28 p} back."""
    lnb = log1p(R) - delta
    M = 2 * exp(p * lnb) - 1
    K = 4 * h_nsw(p) ** 2 + 3
    L = log(K)
    robin = exp(euler) * log(L) + mpf("0.6483") / log(L) - 1
    slack_before = M - sqrt(1 + robin)
    tail = exp(-mpf("0.28") * p)
    return slack_before - tail, slack_before, tail


# Recompute rooms; assert they match the previously published digits
SLACK = {}
ROOM_META = {}
for p, delta in DELTAS.items():
    after, before, tail = idealised_slack(p, delta)
    SLACK[p] = after
    ROOM_META[p] = dict(delta=str(delta), slack_after_tail=str(after),
                        slack_before_tail=str(before), tail=str(tail))
assert str(SLACK[1409]).startswith("0.020112965592839825")
assert str(SLACK[3307]).startswith("0.003347184751707372")

rows = []
for p in (1409, 3307):
    wm = wmax(p)
    X = (p - 1) ** wm * math.factorial(wm)
    assert le_eps_pow(X, p) and not le_eps_pow(X * (p - 1) * (wm + 1), p)
    cs = int(math.floor(p * math.log(1 + 2 ** .5) / math.log(p - 1))); crude = p / math.log(p - 1)
    row = dict(p=p, wmax=wm, csharp=cs, p_over_ln=crude, slack=str(SLACK[p])[:24],
               room=ROOM_META[p])
    for name, w in (("wmax", wm), ("w228", 228), ("csharp", cs), ("crude", crude)):
        nl = mpf(2) ** w - 2
        row[f"c_noroom_{name}"] = float(log(nl) / p)
        row[f"c_room_{name}"] = float((log(nl) - log(SLACK[p])) / p)
    lhs = (mpf(2) ** wm - 2) * exp(-mpf("0.058") * p)
    row["c0058_C1_lhs"] = float(lhs); row["c0058_C1_fits"] = bool(lhs < SLACK[p])
    row["c0058_max_C"] = float(SLACK[p] / lhs)
    assert row["c0058_C1_fits"]
    rows.append(row); print(json.dumps({k: row[k] for k in row if k != "room"}), flush=True)

assert [r["wmax"] for r in rows] == [112, 231]
OUT.write_text(json.dumps(dict(
    room_source=("Recomputed from THEOREM_DRAFT_v5 / BGS-TRACE-333 on main: "
                 "R=6.234e-4, delta(1409)=7.4115e-6, delta(3307)=3.4962e-4, "
                 "slack=M-sqrt(1+robin)-e^{-0.28p} with n/h_p:=1 and Y=X_tail=eps=0"),
    rows=rows), indent=1) + "\n")
