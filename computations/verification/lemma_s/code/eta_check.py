#!/usr/bin/env python3
"""Checks for the Binet lattice generator (BGS-TRACE-354).

omega = zeta^{(p+1)/2} (so omega^2 = zeta), eta_s = omega^2 - 2 s omega - 1 = zeta - 1 - 2 s zeta^{(p+1)/2}, s = +-1.
(A) exact resultants (sympy, Phi_p monic, so Res(Phi_p, g) = prod over the primitive p-th roots of g):
    N(eta_+) = N(eta_-) = h_p and N(zeta^2 - 6 zeta + 1) = h_p^2 for every prime 3 <= p <= 73;
(B) exact integers in Z[sqrt2]: Phi_p(s eps) Phi_p(s epsbar) = h_p (p odd prime <= 1500), the closed form behind (A);
(C) on every line abar of h_p (sqrt2 -> r mod h, zeta -> lambda = (1 + r)^2) for p <= 43: on a Binet line with sign s,
    eta_s -> 0, eta_{-s} -/-> 0 and zeta^2 - 6 zeta + 1 -> 0; on a cross line neither eta_s vanishes, the kernel element does;
(D) word lattice caveat: |Res(x^p - 1, eta_s)| = |eta_s(1)| h_p = 2 h_p for every prime 5 <= p <= 43, i.e. in
    Z[x]/(x^p - 1) the ideal (eta_s) has index 2h, and the line lattice is (eta_s) + (Phi_p).
Output ../logs/eta_check.json.  Usage: python code/eta_check.py
"""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import itertools, json, pathlib, time
from sympy import factorint, sqrt_mod, symbols, resultant, cyclotomic_poly, primerange

OUT = pathlib.Path(__file__).resolve().parents[1] / "logs" / "eta_check.json"
x = symbols("x")


def h_of(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = a + 2 * b, a + b
    return a


def zmul(u, v):  # (a + b sqrt2)(c + d sqrt2)
    return (u[0] * v[0] + 2 * u[1] * v[1], u[0] * v[1] + u[1] * v[0])


def phi_at(p, z):  # sum_{k<p} z^k in Z[sqrt2]
    acc, pw = (0, 0), (1, 0)
    for _ in range(p):
        acc = (acc[0] + pw[0], acc[1] + pw[1]); pw = zmul(pw, z)
    return acc


t0 = time.time()
A = []
for p in primerange(3, 74):
    h = h_of(p); Phi = cyclotomic_poly(p, x); row = dict(p=p, h=h)
    for s in (1, -1):
        eta = x - 1 - 2 * s * x ** ((p + 1) // 2)
        row[f"N_{s:+d}"] = int(resultant(Phi, eta, x))
    row["N_kernel"] = int(resultant(Phi, x ** 2 - 6 * x + 1, x))
    row["ok"] = row["N_+1"] == h and row["N_-1"] == h and row["N_kernel"] == h * h
    assert row["ok"], row
    A.append(row)
B_bad = []
for p in primerange(3, 1501):
    h = h_of(p)
    for s in (1, -1):
        u = phi_at(p, (s, s)); v = phi_at(p, (s, -s))
        n = zmul(u, v)
        if n != (h, 0):
            B_bad.append((p, s))
assert not B_bad
C = []
for p in primerange(3, 44):
    h = h_of(p); qs = sorted(factorint(h)); oks = []; kinds = []
    for ch in itertools.product(*[[int(sqrt_mod(2, q)), q - int(sqrt_mod(2, q))] for q in qs]):
        r, M = 0, 1
        for q, rq in zip(qs, ch):
            r = r + M * (((rq - r) * pow(M, -1, q)) % q); M *= q
        e = (1 + r) % h; lam = e * e % h; ep = pow(e, p, h); om = pow(lam, (p + 1) // 2, h)
        sig = [1 if ep % q == 1 else -1 for q in qs]
        assert all((ep - s) % q == 0 for q, s in zip(qs, sig))
        ev = {s: (lam - 1 - 2 * s * om) % h for s in (1, -1)}
        ker = (lam * lam - 6 * lam + 1) % h
        kind = "binet" if len(set(sig)) == 1 else "cross"; kinds.append(kind)
        if kind == "binet":
            oks.append(ev[sig[0]] == 0 and ev[-sig[0]] != 0 and ker == 0)
        else:
            oks.append(ev[1] != 0 and ev[-1] != 0 and ker == 0)
    C.append(dict(p=p, omega=len(qs), lines=len(oks), cross=kinds.count("cross"), ok=all(oks)))
    assert all(oks), p
D = []
for p in primerange(5, 44):
    h = h_of(p)
    for s in (1, -1):
        eta = x - 1 - 2 * s * x ** ((p + 1) // 2)
        R = abs(int(resultant(x ** p - 1, eta, x)))
        D.append(dict(p=p, s=s, index=R, two_h=2 * h, ok=R == 2 * h))
        assert R == 2 * h
res = dict(A_resultants=A, B_closed_form=dict(odd_primes_upto=1500, bad=B_bad),
           C_lines=C, D_word_index=D, seconds=round(time.time() - t0, 1))
OUT.write_text(json.dumps(res, indent=1) + "\n")
print(json.dumps(dict(A=len(A), A_ok=all(r["ok"] for r in A), B_bad=len(B_bad), C=[(r["p"], r["lines"], r["ok"]) for r in C],
                      D_ok=all(r["ok"] for r in D), seconds=res["seconds"])))
