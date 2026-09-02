"""
THEOREM E (run 72): every real-symbol single-orbit compression carries a real
structure, hence lies in the beta = 1 (orthogonal) class.
===========================================================================

Setup.  R is the reversing involution (R A R^{-1} = A^{-1}, det R = -1, R^2 = I),
M = S R, Theta = U_M o conj, and rho := M^T S = R^T.  From Egorov,
        Theta T(u) Theta^{-1} = T(rho u) = T(R^T u),
so Theta maps the real-symbol observable  V_u = T(u) + T(-u)  to  V_{R^T u}.
Generically R^T u is NOT in the A^T-orbit of +-u, so Theta alone does not commute
with the compression M_u = P_lam V_u P_lam and one would predict beta = 2.

The point of Theorem E: the Hecke torus repairs this.  Let
        C(A) = { x I + y A : x^2 + x y t + y^2 = 1 },   t = tr A,
be the centraliser torus of A mod p (order p -+ 1).  Its quantisation commutes
with U_A, hence acts on H_lam, and Egorov gives U_tau T(u) U_tau^* = T(tau^T u).
Therefore, if there exists tau in C(A) with

        tau^T R^T u  ==  +- u   (mod p)                                    (E)

then Theta_u := U_tau Theta is an antiunitary with Theta_u M_u Theta_u^{-1} = M_u,
i.e. M_u carries a real structure and its local statistics are beta = 1.

Why (E) should hold: in the eigenbasis of A the torus is the diagonal group
{diag(z, z^{-1})}, whose orbits on (Z/p)^2 minus 0 are the level sets of the
invariant q(u) = u_1 u_2 (split case).  R^T conjugates A^T to its inverse, so in
the same eigenbasis it interchanges the two eigendirections and therefore
PRESERVES q.  Hence R^T u lies on the same torus orbit as u, and (E) is solvable
whenever that orbit is a full torus orbit.

This script checks (E) exhaustively by integer arithmetic: for many (A, p) and
many u it searches the whole torus for tau satisfying (E), and reports the
fraction of u for which (E) is solvable, split by the value of the invariant.
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np


def torus_elements(A, p):
    """{x I + y A} with det = 1, as 2x2 matrices mod p."""
    a, b, c, d = A[0][0] % p, A[0][1] % p, A[1][0] % p, A[1][1] % p
    t = (a + d) % p
    out = []
    for x in range(p):
        for y in range(p):
            if (x * x + x * y * t + y * y) % p != 1 % p:
                continue
            M = ((x + y * a) % p, (y * b) % p, (y * c) % p, (x + y * d) % p)
            out.append(M)
    return out


def reversing_involution(A, box=12):
    (a, b), (c, d) = A
    Am = np.array(A, dtype=np.int64)
    Ainv = np.array([[d, -b], [-c, a]], dtype=np.int64)
    for p_ in range(-box, box + 1):
        for q_ in range(-box, box + 1):
            for r_ in range(-box, box + 1):
                if p_ * p_ + q_ * r_ != 1:
                    continue
                R = np.array([[p_, q_], [r_, -p_]], dtype=np.int64)
                if round(np.linalg.det(R)) != -1:
                    continue
                if np.array_equal(R @ Am, Ainv @ R):
                    return R
    return None


def main():
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "rows": []}
    maps = [[[2, 1], [1, 1]], [[5, 2], [2, 1]], [[3, 1], [2, 1]]]
    primes = [41, 71, 101, 151, 199, 311, 401]
    print(f"{'A':>18} {'p':>5} {'|C(A)|':>7} {'split?':>7} "
          f"{'#u tested':>10} {'(E) solvable':>13} {'via -u only':>12}")
    for A in maps:
        R = reversing_involution(A)
        if R is None:
            print(f"  no reversing involution found for {A}")
            continue
        RT = R.T % 1  # placeholder to keep numpy int
        RT = R.T
        for p in primes:
            if math.gcd(int(A[1][0]) % p, p) != 1:
                continue
            t = (A[0][0] + A[1][1]) % p
            disc = (t * t - 4) % p
            split = pow(disc, (p - 1) // 2, p) == 1 if disc % p else None
            T = torus_elements(A, p)
            nsolv = nminus = ntest = 0
            fails = []
            for u1 in range(0, p, max(1, p // 23)):
                for u2 in range(0, p, max(1, p // 23)):
                    if u1 % p == 0 and u2 % p == 0:
                        continue
                    ntest += 1
                    u = np.array([u1, u2], dtype=np.int64) % p
                    w = (RT @ u) % p                      # R^T u
                    hit = 0
                    for (m11, m12, m21, m22) in T:
                        # tau^T w
                        v0 = (m11 * w[0] + m21 * w[1]) % p
                        v1 = (m12 * w[0] + m22 * w[1]) % p
                        if v0 == u[0] % p and v1 == u[1] % p:
                            hit = 1
                            break
                        if v0 == (-u[0]) % p and v1 == (-u[1]) % p:
                            hit = 2
                            break
                    if hit:
                        nsolv += 1
                        nminus += (hit == 2)
                    else:
                        fails.append([int(u1), int(u2)])
            row = {"A": A, "p": p, "torus_order": len(T),
                   "split": split, "u_tested": ntest, "E_solvable": nsolv,
                   "solved_only_via_minus_u": nminus,
                   "fraction": nsolv / max(1, ntest),
                   "failures": fails[:10]}
            out["rows"].append(row)
            print(f"{str(A):>18} {p:>5} {len(T):>7} {str(split):>7} "
                  f"{ntest:>10} {nsolv:>6}/{ntest:<6} {nminus:>12}")
            sys.stdout.flush()

    frac = [r["fraction"] for r in out["rows"]]
    out["verdict"] = {"min_fraction": min(frac), "mean_fraction":
                      float(np.mean(frac)),
                      "E_always_solvable": bool(min(frac) == 1.0)}
    print()
    print("VERDICT:", out["verdict"])
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r72", "theoremE_torus_repair.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
