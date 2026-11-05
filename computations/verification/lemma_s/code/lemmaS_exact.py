#!/usr/bin/env python3
"""Exhaustive check of Lemma S (BGS-TRACE-352) on every line of h_p for p = 11, 13, 17 (all semiprime, omega = 2).

Convention (BGS-TRACE-342/348): eps = 1 + sqrt2, h_p = (eps^p + epsbar^p)/2 (h_11 = 23*353, h_13 = 79*599,
h_17 = 103*15607).  A line is an ideal abar of O = Z[sqrt2] of norm h_p containing one prime above each q | h_p; it is
the kernel of O -> Z/h, a + b sqrt2 -> a + b r (r^2 = 2 mod h, r fixed by a choice of sqrt2 mod each q; CRT).
eps^p = s_q = +-1 mod the prime of abar above q; abar_+ / abar_- = product over s_q = +1 / -1, d_+- = N(abar_+-),
d_+ d_- = h (h_p squarefree here).  Cross line: d_+, d_- > 1.  Height G(x) = min{|a| + sqrt2 |b| : a + b r = x mod h}
(= min max(|rho|, |rho'|) over the coset, BGS-TRACE-352 / Lean ht_eq_max).

G is computed exactly as an exhaustive minimum: G(x) = min_b (sqrt2 |b| + min(t, h - t)), t = (x - b r) mod h, with b
running until sqrt2 |b| exceeds max_x G (a representative with larger |b| cannot be minimal).  Heights are evaluated in
float64; every inequality is checked with relative tolerance 1e-12 and the reported margins are >= 3%.
Checked per cross line (sigma = side with d_sigma = max(d_+, d_-), x -> x e, e = (1 + r)^p mod h):
  (i)   (G(x) + G(x e))^2 >= d_sigma for every class x not in abar_{-sigma} (x != 0 mod d_{-sigma});
  (ii)  (G(x) + G(x e))^2 >= d_+ gcd(x, d_-) whenever x != 0 mod d_-, and >= d_- gcd(x, d_+) whenever x != 0 mod d_+;
  (iii) on the axis sub-line 0 != x in abar_{-sigma}: G(x e) = G(x), G(x)^2 >= min(d_+, d_-), exact minimum reported;
  (iv)  Q = min over primitive x of max(G(x), G(x e)) and Q / sqrt(d_sigma) (report's 0.811 / 0.891 / 0.544),
        min over primitive x of (G(x) + G(x e)) / sqrt(d_sigma).
On Binet lines (one sign) Q = 1 (x = 1).  Output ../logs/lemmaS_exact.json.  Usage: python code/lemmaS_exact.py
Non-claims: finite check at three semiprime h_p; it does not test omega >= 3 (first case p = 37, h ~ 7e13).
"""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import itertools, json, math, pathlib, time
import numpy as np
from sympy import factorint, sqrt_mod

OUT = pathlib.Path(__file__).resolve().parents[1] / "logs" / "lemmaS_exact.json"
S2 = math.sqrt(2.0)
TOL = 1e-12


def h_of(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = a + 2 * b, a + b
    return a


def heights(h, r):
    x = np.arange(h, dtype=np.int64)
    G = np.minimum(x, h - x).astype(float)
    b = 0
    while S2 * (b + 1) < G.max() + 1e-9:
        b += 1
        for sb in (b, -b):
            t = (x - sb * r) % h
            G = np.minimum(G, S2 * b + np.minimum(t, h - t))
    return x, G, b


def run(p):
    h = h_of(p)
    f = factorint(h)
    qs = sorted(f)
    assert all(v == 1 for v in f.values())
    rows = []
    for ch in itertools.product(*[[int(sqrt_mod(2, q)), q - int(sqrt_mod(2, q))] for q in qs]):
        r, M = 0, 1
        for q, rq in zip(qs, ch):
            r = r + M * (((rq - r) * pow(M, -1, q)) % q)
            M *= q
        assert (r * r - 2) % h == 0
        e = pow(1 + r, p, h)
        sig = [1 if e % q == 1 else (-1 if e % q == q - 1 else 0) for q in qs]
        assert 0 not in sig
        dp = math.prod(q for q, s in zip(qs, sig) if s == 1)
        dm = h // dp
        assert dp * dm == h
        x, G, bmax = heights(h, r)
        Ge = G[(x * e) % h]
        S = G + Ge
        prim = np.ones(h, bool)
        for q in qs:
            prim &= (x % q != 0)
        row = dict(p=p, h=h, qs=qs, r=int(r), signs=sig, dplus=dp, dminus=dm, Bmax=bmax, maxG=float(G.max()))
        if dp == 1 or dm == 1:
            row.update(kind="binet", Q=float(np.maximum(G, Ge)[prim].min()))
            assert row["Q"] == 1.0 and G[1] == 1.0
            rows.append(row); print(json.dumps(row), flush=True); continue
        D = max(dp, dm)
        dsig, dother = (dp, dm) if dp >= dm else (dm, dp)
        outside = (x % dother != 0)                         # classes not in abar_{-sigma}
        ok_i = bool((S[outside] ** 2 >= dsig * (1 - TOL)).all())
        nzm = (x % dm != 0); nzp = (x % dp != 0)
        g_m = np.gcd(x, dm); g_p = np.gcd(x, dp)
        ok_ii = bool((S[nzm] ** 2 >= dp * g_m[nzm] * (1 - TOL)).all() and (S[nzp] ** 2 >= dm * g_p[nzp] * (1 - TOL)).all())
        axis = (x % dother == 0) & (x != 0)
        ok_iii_sym = bool(np.allclose(G[axis], Ge[axis], rtol=0, atol=1e-9))
        ok_iii_bd = bool((G[axis] ** 2 >= min(dp, dm) * (1 - TOL)).all())
        pm = np.maximum(G, Ge)
        row.update(kind="cross", D=D, d_sigma=dsig, d_minus_sigma=dother,
                   ok_i_all_outside_axis=ok_i, min_ratio_i=float((S[outside] / math.sqrt(dsig)).min()),
                   ok_ii_general_form=ok_ii,
                   axis_classes=int(axis.sum()), ok_iii_axis_symmetric=ok_iii_sym, ok_iii_axis_ge_sqrt_min=ok_iii_bd,
                   axis_min_G=float(G[axis].min()), sqrt_min=math.sqrt(min(dp, dm)),
                   Q=float(pm[prim].min()), Q_over_sqrtD=float(pm[prim].min() / math.sqrt(D)),
                   minsum_prim_over_sqrtD=float(S[prim].min() / math.sqrt(D)))
        assert ok_i and ok_ii and ok_iii_sym and ok_iii_bd
        rows.append(row); print(json.dumps(row), flush=True)
    return rows


if __name__ == "__main__":
    t0 = time.time()
    out = []
    for p in (11, 13, 17):
        out += run(p)
    res = dict(rows=out, all_cross_ok=all(r["ok_i_all_outside_axis"] and r["ok_ii_general_form"] for r in out if r["kind"] == "cross"),
               seconds=round(time.time() - t0, 1))
    OUT.write_text(json.dumps(res, indent=1) + "\n")
    print(json.dumps({k: v for k, v in res.items() if k != "rows"}))
