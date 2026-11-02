#!/usr/bin/env python3
"""Wave 41, task 3 (part 4): verify the induction step and valuations.

1. Induction step: for nu=(1,1) z mod 2^(k+3), period 2^k, let
   z' = z mod 2^(k+2). Check: z' has minimal period exactly 2^(k-1),
   nu'=(1,1), and A(z)/2^k == A(z')/2^(k-1).
2. Valuations: v2(gcd of entries of M^p - I) = k and v2(det) = 2k+3
   for p = 2^k, k = 3..8.
"""
from math import gcd
from wave41_reversal_census import kernel_seeds, build_seq, min_period
from wave41_reversal_nu import nu_of, mat_int_pow


def v2(n):
    n = abs(n)
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


print("valuations:")
for k in range(3, 9):
    p = 2 ** k
    a, b, c, d = mat_int_pow((6, -1, 1, 0), p)
    a1, b1, c1, d1 = a - 1, b, c, d - 1
    g = gcd(gcd(a1, b1), gcd(c1, d1))
    det = a1 * d1 - b1 * c1
    print(f"  k={k} p={p}: v2(gcd)={v2(g)} (want {k}), "
          f"v2(det)={v2(det)} (want {2*k+3})")
    assert v2(g) == k and v2(det) == 2 * k + 3

print("induction step:")
for (j, p_target) in ((6, 16), (7, 32)):
    m = 2 ** j
    N = m
    Q = 2 ** (2 * j + 3)
    k = p_target.bit_length() - 1
    R = 2 ** (k + 3)
    scale = Q // R
    n_checked = 0
    for (y0, y1) in kernel_seeds(N, Q):
        s = build_seq(y0, y1, N, Q)
        if min_period(s, N) != p_target:
            continue
        if nu_of(s, p_target, Q) != (1, 1):
            continue
        z = tuple(v // scale for v in s[:p_target])
        R2 = R // 2
        zp = tuple(v % R2 for v in z)
        # minimal period of zp (as a 2^(k-1)-periodic sequence)
        pp = min_period(zp + zp, 2 * p_target // 2) if False else None
        # compute minimal period of zp over its natural length p_target
        # (zp has period dividing 2^(k-1); find smallest 2^r period)
        per = None
        for r in range(0, k):
            cand = 2 ** r
            if all(zp[i] == zp[i % cand] for i in range(p_target)):
                per = cand
                break
        assert per == 2 ** (k - 1), (per, k)
        # nu' of zp at period 2^(k-1), modulus R2
        half = R2 // 2
        nu_p = tuple(
            0 if (zp[r + 2 ** (k - 2)] - zp[r]) % R2 == 0
            else 1 if (zp[r + 2 ** (k - 2)] - zp[r]) % R2 == half
            else -1
            for r in (0, 1))
        assert nu_p == (1, 1), nu_p
        Az = sum((-1) ** i * z[i] for i in range(p_target))
        Azp = sum((-1) ** i * zp[i] for i in range(2 ** (k - 1)))
        assert Az // p_target == Azp // 2 ** (k - 1), (Az, Azp)
        assert Az % p_target == 0 and Azp % 2 ** (k - 1) == 0
        n_checked += 1
    print(f"  p={p_target}: induction step verified on {n_checked} points")
print("ALL CHECKS PASS")
