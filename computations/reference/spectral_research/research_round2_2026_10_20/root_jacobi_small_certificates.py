#!/usr/bin/env python3
"""Exact Jacobi characteristic-polynomial certificates, N = 21, 35, 49.

All arithmetic is in explicitly specified prime fields.  The output includes
Bezout polynomials U,V with U P + V P' = 1, not numerical eigenvalues.
Polynomial lists use ascending coefficients.
"""
import hashlib
import json
from math import isqrt
from pathlib import Path

CASES = ((21, 337, 13, 148), (35, 281, 98, 228), (49, 197, 16, 183))


def trim(a, p):
    a = [int(x) % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim(c, p)


def scale(a, c, p):
    return trim([c*x for x in a], p)


def mul(a, b, p):
    c = [0] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % p
    return trim(c, p)


def divmod_poly(a, b, p):
    a, b = trim(a, p), trim(b, p)
    if b == [0]:
        raise ZeroDivisionError
    q = [0] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        shift = len(a)-len(b)
        coefficient = a[-1] * pow(b[-1], -1, p) % p
        q[shift] = coefficient
        a = add(a, [0]*shift + scale(b, -coefficient, p), p)
    return trim(q, p), a


def xgcd(a, b, p):
    r0, r1, u0, u1, v0, v1 = a, b, [1], [0], [0], [1]
    while r1 != [0]:
        q, r2 = divmod_poly(r0, r1, p)
        r0, r1 = r1, r2
        u0, u1 = u1, add(u0, scale(mul(q, u1, p), -1, p), p)
        v0, v1 = v1, add(v0, scale(mul(q, v1, p), -1, p), p)
    c = pow(r0[-1], -1, p)
    return scale(r0, c, p), scale(u0, c, p), scale(v0, c, p)


def prime_factors(n):
    answer, d = [], 2
    while d*d <= n:
        if n % d == 0:
            answer.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        answer.append(n)
    return answer


def certify(n, p, zeta, imag):
    assert all(p % d for d in range(2, isqrt(p)+1))
    assert p not in (2, 5) and n % p
    assert pow(zeta, n, p) == 1
    assert all(pow(zeta, n//q, p) != 1 for q in prime_factors(n))
    assert imag*imag % p == p-1
    half, inv_2i = pow(2, -1, p), pow(2*imag, -1, p)
    roots = [pow(zeta, j, p) for j in range(n)]

    def cosine(j):
        return (roots[j % n]+roots[-j % n])*half % p

    def sine(j):
        return (roots[j % n]-roots[-j % n])*inv_2i % p

    rr = [(1-cosine(7*j))*(1+cosine(j)) % p for j in range(n)]
    h = (n+1)//2
    # L = 200 D^* P^* A_N P D, with x_j = h+j modulo N.
    diagonal = []
    hopping = []
    for j in range(n):
        x = (h+j) % n
        diagonal.append((200*cosine(7*x)+20*rr[x]+2*rr[x]*sine(x)-20) % p)
        hopping.append(rr[(x+h) % n])
    length = n//7
    assert [j for j, b in enumerate(hopping) if b == 0] == list(range(length-1, n, length))
    characteristic = [1]
    block_polynomials = []
    for block in range(7):
        p_old, p_cur = [0], [1]
        start = block*length
        for j in range(start, start+length):
            p_next = mul([-diagonal[j], 1], p_cur, p)
            if j > start:
                p_next = add(p_next, scale(p_old, -hopping[j-1]**2, p), p)
            p_old, p_cur = p_cur, p_next
        block_polynomials.append(p_cur)
        characteristic = mul(characteristic, p_cur, p)
    assert len(characteristic) == n+1 and characteristic[-1] == 1
    derivative = trim([j*characteristic[j] for j in range(1, n+1)], p)
    gcd, u, v = xgcd(characteristic, derivative, p)
    assert gcd == [1]
    assert add(mul(u, characteristic, p), mul(v, derivative, p), p) == [1]
    return {
        "N": n, "p": p, "zeta_N": zeta, "i": imag,
        "polynomial_convention": "ascending",
        "scaled_matrix": "200 D^* P^* A_N P D",
        "block_characteristic_polynomials": block_polynomials,
        "characteristic_polynomial": characteristic,
        "derivative": derivative, "bezout_U": u, "bezout_V": v,
        "bezout_identity": "U*P + V*P' = 1 modulo p",
        "verified": True,
    }


def main():
    result = {
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "cases": [certify(*case) for case in CASES],
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(out), "cases": [
        {"N": c["N"], "p": c["p"], "verified": c["verified"]}
        for c in result["cases"]]}, indent=2))


if __name__ == "__main__":
    main()

