#!/usr/bin/env python3
"""Exact checks for the H5 structural-ceiling arithmetic (BGS-TRACE-348..351).

Convention (BGS-TRACE-342, Bgs.H6LemmaW): eps = 1 + sqrt2, epsbar = 1 - sqrt2, lambda = eps^2 = 3 + 2 sqrt2,
h_n = (eps^n + epsbar^n)/2 (h_0 = h_1 = 1, h_{n+2} = 2 h_{n+1} + h_n), so h_3 = 7, h_5 = 41, h_7 = 239, h_11 = 8119;
for odd p, h_p = u_{(p-1)/2} with u_0 = 1, u_1 = 7, u_{n+1} = 6 u_n - u_{n-1} (BGS-TRACE-344).  Checked here.

(A) [TRACE-348] every odd prime p <= P and EVERY prime q < B1 (no residue-class presieve): q | h_p  =>  q = 1 (mod 2p)
    and q = +-1 (mod 8).  h_p mod q is the rational part of (1 + sqrt2)^p mod q (int64, vectorised); each hit is
    re-confirmed with the exact big integer h_p.  Complete factorisations (sympy factorint) for odd primes p <= PF.
(B) [TRACE-349] gcd(h_p, h_p') = 1 for all odd primes p < p' <= P (exact big-integer gcd), and no prime q < B1 is hit
    by two different p in (A).
(C) [TRACE-350] for odd primes p <= P: (2p+1) | h_p  <=>  (p = 3 mod 4 and 2p+1 prime); for every p, no prime q <= 2p+1
    other than 2p+1 itself divides h_p (exact trial division by all primes q <= 2p+1, no presieve), so the least prime
    factor of h_p equals 2p+1 exactly on that set; count over 5 <= p <= 1500.
(D) [TRACE-351] h_n = prod_{k=1}^{(n-1)/2} (6 - 2 cos(2 pi k/n)) in mpmath at 80 digits for every odd n, 3 <= n <= ND.
Output: ../logs/h5_arith.json.  Usage: python code/h5_arith.py (any working directory).
"""
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")
import json, math, pathlib, sys, time
import numpy as np
import mpmath
import sympy
from sympy import factorint, isprime, primerange

OUT = pathlib.Path(__file__).resolve().parents[1] / "logs" / "h5_arith.json"
P, B1, PF, ND = 1500, 10**7, 61, 301


def h_pair(n):
    """Exact (h_n, y_n) with eps^n = h_n + y_n sqrt2."""
    x, y = 1, 0
    for _ in range(n):
        x, y = x + 2 * y, x + y
    return x, y


def h_rec(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, 2 * b + a
    return a


def u(n):
    a, b = 1, 7
    for _ in range(n):
        a, b = b, 6 * b - a
    return a


def hp_mod(p, Q):
    """Rational part of (1 + sqrt2)^p modulo each q in Q (int64; q < 2^31 keeps products < 2^63)."""
    rx = np.ones_like(Q); ry = np.zeros_like(Q); bx = np.ones_like(Q); by = np.ones_like(Q); e = p
    while e:
        if e & 1:
            rx, ry = (rx * bx % Q + 2 * (ry * by % Q)) % Q, (rx * by % Q + ry * bx % Q) % Q
        bx, by = (bx * bx % Q + 2 * (by * by % Q)) % Q, (2 * (bx * by % Q)) % Q
        e >>= 1
    return rx


def main():
    t0 = time.time()
    odd_primes = list(primerange(3, P + 1))
    H = {p: h_pair(p) for p in odd_primes}
    # convention checks
    conv = dict(h_small={n: h_rec(n) for n in (3, 5, 7, 11, 13)})
    assert conv['h_small'] == {3: 7, 5: 41, 7: 239, 11: 8119, 13: 47321}
    for p in odd_primes:
        h, y = H[p]
        assert h == h_rec(p) == u((p - 1) // 2)
        assert h * h - 2 * y * y == -1          # N(eps^p) = -1
        assert h % 2 == 1
    conv['pell_norm_and_u_recurrence_all_p'] = True
    # (A) no-presieve scan
    sieve = np.ones(B1, dtype=bool); sieve[:2] = False
    for i in range(2, int(B1 ** .5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    Q = np.nonzero(sieve)[0].astype(np.int64)
    hits, viol_2p, viol_8, owner = {}, [], [], {}
    for p in odd_primes:
        r = hp_mod(p, Q)
        hq = [int(q) for q in Q[r == 0]]
        hq = [q for q in hq if H[p][0] % q == 0]
        assert all(H[p][0] % q == 0 for q in hq)
        hits[p] = hq
        for q in hq:
            if q % (2 * p) != 1: viol_2p.append((p, q))
            if q % 8 not in (1, 7): viol_8.append((p, q))
            owner.setdefault(q, []).append(p)
    # exact cross-check of the vectorised residue for a sample
    for p in odd_primes[:40]:
        for q in (3, 5, 7, 23, 9999991):
            assert int(hp_mod(p, np.array([q], dtype=np.int64))[0]) == H[p][0] % q
    shared = {q: ps for q, ps in owner.items() if len(ps) > 1}
    A = dict(B1=B1, P=P, primes_q_tested=int(len(Q)), odd_primes_p=len(odd_primes), total_hits=sum(map(len, hits.values())),
             p_with_hit=sum(1 for v in hits.values() if v), violations_mod_2p=viol_2p, violations_mod_8=viol_8,
             hits_le_200={p: hits[p] for p in odd_primes if p <= 200})
    fac = {}
    for p in primerange(3, PF + 1):
        f = factorint(H[p][0])
        for q in f:
            assert isprime(q) and q % (2 * p) == 1 and q % 8 in (1, 7), (p, q)
        fac[p] = {str(q): e for q, e in sorted(f.items())}
    A['factorisations_p_le_%d' % PF] = fac
    A['factorisations_all_factors_1_mod_2p_and_pm1_mod_8'] = True
    A['factorisations_squarefree'] = all(all(e == 1 for e in v.values()) for v in fac.values())
    A['factorisation_note'] = 'sympy factorint/isprime; factors above 2^64 are BPSW probable primes (not certified)'
    # (B) pairwise gcd
    ng, bad = 0, []
    for i, p in enumerate(odd_primes):
        for p2 in odd_primes[i + 1:]:
            ng += 1
            if math.gcd(H[p][0], H[p2][0]) != 1: bad.append((p, p2))
    Bres = dict(pairs_checked=ng, pairs_with_gcd_gt_1=bad, primes_q_lt_B1_hit_by_two_p=shared)
    # (C) Sophie Germain family and least prime factor 2p+1
    sg, lpf_2p1, mismatch = [], [], []
    for p in odd_primes:
        h = H[p][0]; q = 2 * p + 1
        pred = (p % 4 == 3) and isprime(q)
        div = (h % q == 0)
        if pred != div: mismatch.append(p)
        if pred: sg.append(p)
        small = [r for r in primerange(2, q + 1) if h % r == 0]
        if small == [q]: lpf_2p1.append(p)
        assert all(r == q for r in small), (p, small)
    sg5 = [p for p in sg if p >= 5]
    assert all(H[p][0] > 2 * p + 1 for p in sg5)
    Cres = dict(P=P, mismatches=mismatch, p_3mod4_2p1_prime=sg, count_5_to_1500=len(sg5),
                p_with_least_prime_factor_2p_plus_1=lpf_2p1, sets_equal=(sg == lpf_2p1),
                h_p_composite_for_p_ge_5_in_family=True, no_prime_below_2p_plus_1_divides_h_p=True)
    # (D) product formula
    mpmath.mp.dps = 80
    worst = mpmath.mpf(0)
    for n in range(3, ND + 1, 2):
        pr = mpmath.mpf(1)
        for k in range(1, (n - 1) // 2 + 1):
            pr *= 6 - 2 * mpmath.cos(2 * mpmath.pi * k / n)
        rel = abs(pr - h_rec(n)) / h_rec(n)
        worst = max(worst, rel)
    assert worst < mpmath.mpf(10) ** -60
    Dres = dict(odd_n_from=3, odd_n_to=ND, dps=80, max_relative_error=mpmath.nstr(worst, 5))
    res = dict(schema='bgs-h5-ceiling-arith-v1', convention=conv, A_congruences=A, B_coprime=Bres, C_sophie_germain=Cres,
               D_product_formula=Dres, versions=dict(python=sys.version.split()[0], numpy=np.__version__, sympy=sympy.__version__,
               mpmath=mpmath.__version__), seconds=round(time.time() - t0, 1),
               non_claims='finite checks of statements proved on paper (TRACE-348..351); no asymptotic statement is established by them')
    assert not viol_2p and not viol_8 and not bad and not shared and not mismatch and sg == lpf_2p1
    OUT.write_text(json.dumps(res, indent=1) + "\n")
    print(json.dumps(dict(A=dict((k, A[k]) for k in ('primes_q_tested', 'total_hits', 'violations_mod_2p', 'violations_mod_8')),
                          B=dict(pairs=ng, bad=len(bad), shared=len(shared)), C=dict(count=len(sg5), first=sg5[:8], equal=sg == lpf_2p1),
                          D=Dres, sec=res['seconds'])))


if __name__ == "__main__":
    main()
