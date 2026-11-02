"""Wave 41: find constraining components (p, f) for even m.

(p, f) constraining iff alpha^u == -1 mod p^f in R = Z[sqrt(2)],
u = m/2 (then automatically alpha^m == 1, beta^u == 1).
p odd only (trace-signature injectivity needs p odd).
"""

def rmul(x, y, mod):
    a, b = x
    c, d = y
    return ((a * c + 2 * b * d) % mod, (a * d + b * c) % mod)


def rpow(x, n, mod):
    r = (1 % mod, 0)
    while n:
        if n & 1:
            r = rmul(r, x, mod)
        x = rmul(x, x, mod)
        n >>= 1
    return r


def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]


def constraining(m, pmax=2000, fmax=4):
    u = m // 2
    out = []
    for p in primes_upto(pmax):
        if p == 2:
            continue
        mod = p
        for f in range(1, fmax + 1):
            alpha = (3 % mod, 2 % mod)
            au = rpow(alpha, u, mod)
            if au == (mod - 1, 0):
                out.append((p, f))
            mod *= p
    return out


if __name__ == "__main__":
    import sys
    for m in [12, 18, 24, 30, 36, 42, 48, 60, 66, 72, 84, 90]:
        comps = constraining(m)
        desc = []
        for (p, f) in comps:
            q = p ** (2 * f)
            desc.append(f"{p}^{2 * f}={q}")
        print(f"m={m} u={m // 2}: {', '.join(desc)}", flush=True)
