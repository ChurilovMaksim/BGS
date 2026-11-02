"""Wave 45 exploration: find constraining components and trace-period
structures, hunting for a pair with gcd of generic periods >= 3."""
import sys
from collections import Counter


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


def tr(x, mod):
    return (2 * x[0]) % mod


def primes_upto(n):
    sieve = [True] * (n + 1)
    out = []
    for i in range(2, n + 1):
        if sieve[i]:
            out.append(i)
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return out


def period_of(seq, u):
    for d in sorted(d for d in range(1, u + 1) if u % d == 0):
        if all(seq[k] == seq[k % d] for k in range(u)):
            return d
    return u


def component_periods(p, f, m):
    mod = p ** f
    u = m // 2
    alpha = (3 % mod, 2 % mod)
    if rpow(alpha, u, mod) != (mod - 1, 0):
        return None
    beta = rmul(alpha, alpha, mod)
    bpow = [(1 % mod, 0)]
    for _ in range(1, u):
        bpow.append(rmul(bpow[-1], beta, mod))
    periods = Counter()
    generic_periods = Counter()  # distinct values, negation-free, nonzero
    for a in range(mod):
        for b in range(mod):
            C = (a, b)
            seq = tuple(tr(rmul(C, bpow[k], mod), mod) for k in range(u))
            T = period_of(seq, u)
            periods[T] += 1
            vals = seq[:T]
            vset = set(vals)
            if len(vset) == T and all(((-v) % mod) not in vset for v in vset) and 0 not in vset:
                generic_periods[T] += 1
    return periods, generic_periods


def main():
    for m in [2 * u for u in range(3, 130, 2)]:
        u = m // 2
        comps = []
        for p in primes_upto(400):
            if p == 2:
                continue
            for f in (1, 2):
                mod = p ** f
                if mod > 900:
                    continue
                res = component_periods(p, f, m)
                if res:
                    periods, generic = res
                    comps.append((p, f, dict(periods), dict(generic)))
        # pairs with gcd of generic periods >= 3
        hits = []
        for i in range(len(comps)):
            for j in range(i + 1, len(comps)):
                pa, fa, _, ga = comps[i]
                pb, fb, _, gb = comps[j]
                size = (pa ** (2 * fa)) * (pb ** (2 * fb))
                for Ta in ga:
                    for Tb in gb:
                        import math
                        g = math.gcd(Ta, Tb)
                        if g >= 3 and ga[Ta] > 0 and gb[Tb] > 0:
                            hits.append((g, pa, fa, Ta, ga[Ta], pb, fb, Tb, gb[Tb], size))
        if hits:
            hits.sort(reverse=True)
            print(f"m={m} comps={[(c[0], c[1]) for c in comps]}")
            for h in hits[:6]:
                print("   gcd=%d (%d,%d) T=%d n=%d  x  (%d,%d) T=%d n=%d  pairsize=%d" % h)


if __name__ == "__main__":
    main()
