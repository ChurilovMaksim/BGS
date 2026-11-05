#!/usr/bin/env python3
"""Exact integer checks for BGS-TRACE-344 and BGS-TRACE-345 (H7* scope integration).

u_0 = 1, u_1 = 7, u_{n+1} = 6 u_n - u_{n-1};  h_p = u_{(p-1)/2};  K_p = 4 h_p^2 + 3;
h_{3p} = u_{(3p-1)/2} = h_p K_p;  lambda = 3 + 2 sqrt2 acting on (x, y) = x + y sqrt2.

(a) every prime 5 <= p < 2000: 7 | K_p, 7 does not divide h_p, 3 does not divide h_p,
    K_p odd, gcd(h_p, K_p) = 1 and u_{(3p-1)/2} = h_p K_p (Python integers, exact).
(b) 5 <= p <= 31: complete factorisation of K_p (sympy factorint; every factor is
    < 2^64, where sympy.isprime (BPSW) is deterministic); every factor = 1 (mod 3),
    every factor other than 7 = 1 (mod 6p); the included K_p-divisors other than 7
    (d | K_p, 1 < d, d^2 <= h_p K_p); the three crossing conductors (d | K_p,
    gcd(d, h_p) = 1, floor(h_{3p}/d^2) = 278, 5, 133, gcd(beta, d) = 1); and
    ord_d(lambda) = 3p for every included conductor at p = 5, 7, 19, 29.
Output: ../logs/kp_arith.json.  Usage: python code/kp_arith.py (any working directory).
"""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json
import math
import pathlib
import time

from sympy import divisors, factorint, isprime, primerange

OUT = pathlib.Path(__file__).resolve().parents[1] / "logs" / "kp_arith.json"


def u(n: int) -> int:
    a, b = 1, 7
    for _ in range(n):
        a, b = b, 6 * b - a
    return a


def hK(p: int) -> tuple[int, int]:
    h = u((p - 1) // 2)
    return h, 4 * h * h + 3


def lam_pow(d: int, e: int) -> tuple[int, int]:
    r, b = (1, 0), (3, 2)
    while e:
        if e & 1:
            r = ((r[0] * b[0] + 2 * r[1] * b[1]) % d, (r[0] * b[1] + r[1] * b[0]) % d)
        b = ((b[0] * b[0] + 2 * b[1] * b[1]) % d, (2 * b[0] * b[1]) % d)
        e >>= 1
    return r


def order(d: int, p: int) -> int:
    """Exact order of lambda mod d, given that it divides 3p (checked)."""
    one = (1 % d, 0)
    assert lam_pow(d, 3 * p) == one
    divs = [k for k in (1, 3, p, 3 * p) if (3 * p) % k == 0]
    return min(k for k in divs if lam_pow(d, k) == one)


def main() -> None:
    t0 = time.time()
    # (a) all primes 5 <= p < 2000
    count = 0
    for p in primerange(5, 2000):
        h, K = hK(p)
        assert K % 7 == 0 and h % 7 != 0, p
        assert h % 3 != 0 and K % 2 == 1, p
        assert math.gcd(h, K) == 1, p
        assert u((3 * p - 1) // 2) == h * K, p
        count += 1
    h3, K3 = hK(3)
    assert (h3, K3, K3 % 7) == (7, 199, 3)
    # (b) factorisations and included divisors
    rows = []
    for p in primerange(5, 32):
        h, K = hK(p)
        f = factorint(K)
        assert math.prod(q ** e for q, e in f.items()) == K
        assert all(q < 2 ** 64 and isprime(q) for q in f)
        assert all(q % 3 == 1 for q in f)
        assert all((q - 1) % (6 * p) == 0 for q in f if q != 7)
        hm = h * K
        inc = [d for d in divisors(K) if d > 1 and d != 7 and d * d <= hm]
        rows.append({"p": p, "h_p": str(h), "h_p_prime": bool(isprime(h)), "K_p": str(K),
                     "factorisation": {str(q): e for q, e in sorted(f.items())},
                     "included_other_than_7": [str(d) for d in inc]})
    by = {r["p"]: r for r in rows}
    assert by[5]["factorisation"] == {"7": 1, "31": 2} and by[5]["included_other_than_7"] == ["31", "217"]
    assert by[7]["factorisation"] == {"7": 2, "4663": 1} and by[7]["included_other_than_7"] == ["49", "4663"]
    assert len(by[19]["included_other_than_7"]) == 10 and len(by[29]["included_other_than_7"]) == 10
    assert len(by[31]["included_other_than_7"]) == 12
    assert by[23]["factorisation"] == {"7": 1, "57887325592525441": 1}
    # 31^2 = 961 is above sqrt(h_15): 525^2 < h_15 = 275807 < 526^2
    assert hK(5)[0] * hK(5)[1] == 275807 and 525 ** 2 < 275807 < 526 ** 2
    # 4663 at p = 7
    h7, K7 = hK(7)
    assert K7 == 228487 and K7 % 4663 == 0 and 4663 ** 2 <= h7 * K7 == u(10)
    # orders of all included conductors at the NSW primes 5, 7, 19, 29
    orders = {}
    for p in (5, 7, 19, 29):
        for d in map(int, by[p]["included_other_than_7"]):
            o = order(d, p)
            assert o == 3 * p, (p, d, o)
            orders[str(d)] = o
    assert len(orders) == 24
    # the three crossings
    cross = []
    for p, d, beta, fl in ((19, 3437426497, (-208, 0), 278), (19, 24061985479, (227, 227), 5),
                           (29, 2735635252619983, (-89, 0), 133)):
        h, K = hK(p)
        hm = h * K
        assert K % d == 0 and math.gcd(d, h) == 1 and d * d <= hm and hm // (d * d) == fl
        assert math.gcd(math.gcd(abs(beta[0]), abs(beta[1])), d) == 1
        cross.append({"p": p, "d": str(d), "factorisation": {str(q): e for q, e in sorted(factorint(d).items())},
                      "beta": list(beta), "floor_hm_over_d2": fl, "order": order(d, p)})
    assert hK(19)[0] == 9369319 and hK(29)[0] == 63018038201
    out = {"schema": "bgs-h7-scope-kp-arith-v1", "lemma_check_primes_5_to_1999": count,
           "lemma_check": "7 | K_p, 7 !| h_p, 3 !| h_p, K_p odd, gcd(h_p, K_p) = 1, u_{(3p-1)/2} = h_p K_p",
           "factorisations": rows, "orders_included_conductors": orders, "crossings": cross,
           "unsearched_included": ["4663"], "seconds": round(time.time() - t0, 2)}
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print("ok", count, "primes;", len(orders), "orders = 3p;", out["seconds"], "s")


if __name__ == "__main__":
    main()
