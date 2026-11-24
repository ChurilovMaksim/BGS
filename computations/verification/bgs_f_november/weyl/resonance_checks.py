"""Independent integer checks on the order, the orbit counts and the arithmetic bound."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import Counter
from fractions import Fraction
from math import lcm
import json

def factors(n):
    d = 2
    while d*d <= n:
        k = 0
        while n % d == 0:
            k += 1
            n //= d
        if k:
            yield d, k
        d += 1
    if n > 1:
        yield n, 1

records = []
peak = Fraction(0)
for n in range(3, 2002, 2):
    bound = 1
    fac = list(factors(n))
    for p,k in fac:
        character = 1 if pow(2, (p-1)//2, p) == 1 else -1
        bound = lcm(bound, p**(k-1)*(p-character))
    assert bound <= n*2*Fraction(2,3)**len(fac)
    # S^j corresponds to multiplication by a+b sqrt(2).
    a, b = 3 % n, 2 % n
    order = 1
    while (a,b) != (1,0):
        a,b = (3*a+4*b) % n, (2*a+3*b) % n
        order += 1
        assert order <= bound
    assert bound % order == 0
    peak = max(peak, Fraction(order,n))
    if n <= 79:
        remaining = {(i,j) for i in range(n) for j in range(n)}
        cycles = Counter()
        while remaining:
            v = next(iter(remaining))
            h = 0
            while v in remaining:
                remaining.remove(v)
                a,b = v
                v = (3*a+4*b) % n, (2*a+3*b) % n
                h += 1
            cycles[h] += 1
        assert lcm(*cycles.keys()) == order
        assert sum(h*c for h,c in cycles.items()) == n*n
        records.append(dict(N=n, order=order, cycles=sum(cycles.values())))
assert peak == Fraction(4,3)
print(json.dumps(dict(last_N=2001, maximal_order_over_N=str(peak), small_cycles=records), indent=1))
