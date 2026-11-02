# Wave 40, task 4 — exact verifier for e(p) candidates.
# Usage: python3 wave40_W2_verify.py p d
# Computes d' = ord_p(alpha) independently and the exact e = v_p(alpha^d - 1)
# in R = Z[sqrt(2)], alpha = 3+2*sqrt(2), with Python big integers.
import sys


def mul(x, y, m):
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % m,
            (x[0] * y[1] + x[1] * y[0]) % m)


def pw(base, e, m):
    r = (1 % m, 0)
    while e:
        if e & 1:
            r = mul(r, base, m)
        base = mul(base, base, m)
        e >>= 1
    return r


def factorize(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


p, d_given = int(sys.argv[1]), int(sys.argv[2])
N = p - 1 if p % 8 in (1, 7) else p + 1
d = N
for q in factorize(N):
    while d % q == 0 and pw((3 % p, 2 % p), d // q, p) == (1 % p, 0):
        d //= q
print(f"p={p} N={N} d_computed={d} d_given={d_given} match={d == d_given}")
e, mod = 0, 1
while True:
    mod *= p
    ok = pw((3 % mod, 2 % mod), d, mod) == (1 % mod, 0)
    print(f"  alpha^d == 1 mod p^{e + 1}: {ok}")
    if ok:
        e += 1
    else:
        break
    if e > 6:
        break
print(f"exact e = {e}")
