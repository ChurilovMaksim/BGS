"""Large-prime symbolic expansion of E_theta|Tr U^m|^2:
E = sum_e p^{e} * [ sum_D A_{e,D} (D/p) + eps_p * sum_D B_{e,D} (D/p) ],  e in (1/2)Z, e<=0.
(D/p) Legendre (Jacobi for squarefree D, (1/p)=1); eps_p = 1 (p=1 mod 4), i (p=3 mod 4).
Valid for primes p not dividing the 'bad' product of pivots (printed)."""
import sys, math
from fractions import Fraction
from gauss_exact import terms

def sqf(x):
    s = -1 if x < 0 else 1; x = abs(x); out = 1; d = 2
    while d*d <= x:
        while x % (d*d) == 0: x //= d*d
        if x % d == 0: out *= d; x //= d
        d += 1
    return s*out*x

def expansion(m):
    T, cache = terms(m, 'Q')
    bad = 1
    for v in cache.values(): bad = math.lcm(bad, v[2]) if v[2] else bad
    E = {}
    for (k, r, D), co in T.items():
        n2 = k  # 2n - r
        e = Fraction(n2, 2) - m
        Dp = sqf(((-1)**(r//2))*(2**r)*D) if r > 0 else 1
        key = (e, r % 2, Dp)
        E[key] = E.get(key, Fraction(0)) + co
    E = {k: v for k, v in E.items() if v != 0}
    badp = sorted({q for q in range(2, 200) if all(q % d for d in range(2, int(q**.5)+1)) and bad % q == 0})
    return E, badp

if __name__ == '__main__':
    for m in range(int(sys.argv[1]), int(sys.argv[2])+1):
        E, badp = expansion(m)
        print(f'm={m}  bad primes(<200)={badp}')
        for key in sorted(E, key=lambda k: (-k[0], k[1], k[2])):
            e, odd, D = key
            print(f'   p^{str(e):>6}  {"eps*" if odd else "    "}({D:>4}/p) : {E[key]}')
        sys.stdout.flush()
