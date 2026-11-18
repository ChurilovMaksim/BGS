#!/usr/bin/env python3
"""Exact arithmetic for the fixed-coupling Pell witnesses.

All bounds use integers and fractions. The commutator certificate covers
the fixed Weyl support and index 207, without forming an N-by-N matrix.
"""
from collections import defaultdict
from fractions import Fraction as Q
from math import factorial, isqrt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from orbit_orthogonal_spike import f_coeff


def multiply_pell(a, b):
    x, y = a
    z, w = b
    return x*z + 2*y*w, x*w + y*z


def power(base, exponent, identity, multiply):
    result = identity
    while exponent:
        if exponent % 2:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent //= 2
    return result


def pell(k):
    return power((1, 1), k, (1, 0), multiply_pell)


def require(condition, name):
    if not condition:
        raise ArithmeticError(name)


def window_checks():
    identity = ((1, 0), (0, 1))
    cat = ((3, 4), (2, 3))
    for k in (5, 197, 203, 207):
        n, v = pell(k)
        require(n*n - 2*v*v == -1 and n % 2 == 1, f"Pell norm, k={k}")

        def matmul(a, b):
            return tuple(tuple(sum(a[i][r]*b[r][j] for r in range(2)) % n
                               for j in range(2)) for i in range(2))

        require(power(cat, k, identity, matmul) == identity, f"cat return, k={k}")
        if k == 5:
            require(n == 41 and all(n % (d*d) for d in range(2, isqrt(n)+1)),
                    "h_5=41 squarefree")
        if k in (197, 203):
            width = Q(2000*k, n) + Q(8*k*n, 15*10**80)
            target = Q(1, 700) if k == 197 else Q(7, 25)
            require(width < target, f"arc cover width, k={k}")
            lower = Q(1, 8)*(Q(1, 4)*(Q(99, 100)**2/target-1)-Q(51, 100))
            require(lower > (21 if k == 197 else Q(1, 100)), f"pair defect, k={k}")
            print(f"PASS K={k}, N={n}, width<{target}, defect>{lower}")


def norm_buckets(k, n):
    # Round each coefficient magnitude upward on a rational grid.
    scale = 100_000
    coeff = {}
    majorant = {}
    for x in range(-9, 10):
        for y in range(-1, 2):
            a, b = f_coeff(x, y)
            squared = a*a + b*b
            if squared:
                coeff[x, y] = (a, b)
                majorant[x, y] = 1 + isqrt((squared*scale**2).__floor__())
    require(len(coeff) == 32, "support cardinality")
    variance = sum(a*a+b*b for a, b in coeff.values())
    flat, linear, invariant = defaultdict(int), defaultdict(int), defaultdict(int)
    modular_coeff = {(x % n, y % n): value for (x, y), value in coeff.items()}
    for d in range(1, k):
        u, v = pell(2*d)
        images = {(x, y): ((u*x+v*y) % n, (2*v*x+u*y) % n) for x, y in coeff}
        for key, (p, q) in images.items():
            a, b = coeff[key]
            c, e = modular_coeff.get((-p % n, -q % n), (0, 0))
            variance += a*c-b*e
        for (x, y), left in majorant.items():
            for key, (p, q) in images.items():
                residue = (x*q-y*p) % n
                # 2*pi < 44/7. All bucket weights share this denominator.
                weight = left*majorant[key]*min(14*n, 44*min(residue, n-residue))
                if weight:
                    a, b = (x+p) % n, (y+q) % n
                    flat[a, b] += weight
                    linear[a, b] += abs(k-1-2*d)*weight
                    invariant[(2*a*a-b*b) % n] += weight
    den = 7*n*scale**2
    for name, buckets, divisor, cap in (
            ("K[A,Abar]", flat, den, Q(7, 5)),
            ("K[G,A]", linear, 2*den, Q(13, 5)),
            ("invariant buckets", invariant, den, Q(14, 5))):
        squared_sum = sum(weight**2 for weight in buckets.values())
        require(squared_sum * cap.denominator**2 < (divisor*cap.numerator)**2, name)
        print(f"PASS {name}: bound {cap}, {len(buckets)} buckets")
    require(variance == Q(1650797, 4000000), "effective Weyl mass")
    eps = Q(n, 10**80)
    u = eps**2*k*variance/2
    omega = eps**2*(Q(7, 5)+Q(13, 5)+Q(17, 4)*Q(14, 5))/2
    require(Q(k,12) < Q(17,4)**2 and u+omega < Q(38,100), "trace lower bound")
    print(f"PASS normalized real return > 31/50 at K={k}")


def bump_reference(k, n):
    # Integral majorant: x=s^2/(1-s^2/4); bound (1+x/4)^(-2)
    # on left endpoints (mesh 1/16) against exp(-x) dx up to x=8.
    mesh = Q(1, 16)
    lo = sum((-mesh)**j/Q(factorial(j)) for j in range(4))
    hi = lo+mesh**4/24
    decay_sum = sum(hi**r/(1 + r*mesh/4)**2 for r in range(128))
    area = ((1-lo)*decay_sum + hi**128)/2
    require(area < Q(9,25), "reference integral")
    require((1-4*Q(k,n))**2 > Q(99,100), "first weight")
    lower = (Q(99,100)*Q(31,50)**2-Q(9,25)-Q(2,n))/16
    require(lower > Q(1,1000), "final pair gap")
    print("PASS CUE subtraction < (9/25 + 2/N) H^2 and defect > 1/1000")


if __name__ == "__main__":
    window_checks()
    n, _ = pell(207)
    norm_buckets(207, n)
    bump_reference(207, n)
