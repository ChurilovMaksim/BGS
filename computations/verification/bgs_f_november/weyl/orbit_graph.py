"""Certify two Fourier coefficients of every orbit sum at every odd modulus."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import json
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "research"))
from coefficients import raw_symbol

symbol = raw_symbol()
directions = [(1, 0), (0, 1)]
def norm(v):
    a, b = v
    return a*a - 2*b*b

norm_range = [min(map(norm, symbol)), max(map(norm, symbol))]
isolated = {str(d): [v for v in symbol if norm(v) == norm(d)] for d in directions}
assert all(set(isolated[str(d)]) == {d, (-d[0], -d[1])} for d in directions)
assert norm_range[1] - norm_range[0] < 165

def certified(n, d):
    reduced = {}
    for (a, b), (x, y) in symbol.items():
        k = (a % n, b % n)
        i, j = reduced.get(k, (0, 0))
        reduced[k] = (i+x, j+y)
    orbit = []
    v = d
    while True:
        orbit.append(reduced.get(v, (0, 0)))
        a, b = v
        v = ((3*a-4*b) % n, (-2*a+3*b) % n)
        if v == d:
            break
    total = tuple(map(sum, zip(*orbit)))
    prefix = (0, 0)
    for r, term in enumerate(orbit, 1):
        prefix = (prefix[0]+term[0], prefix[1]+term[1])
        if total == (0, 0):
            assert prefix != (0, 0), (n, d, r)
            continue
        x = next(i for i in range(2) if total[i])
        k = Fraction(-prefix[x], total[x])
        assert (k < 0 or k.denominator != 1 or
                any(prefix[i]+k*total[i] for i in range(2))), (n, d, r, k)
    return len(orbit)

tests = []
for n in range(3, 165, 2):
    if n == 7:
        continue
    basis = [(1, 1), (0, 1)] if n == 49 else directions
    assert abs(basis[0][0]*basis[1][1] - basis[0][1]*basis[1][0]) == 1
    tests.append((n, *(certified(n, d) for d in basis)))
alias7 = {}
for (a, b), (x, y) in symbol.items():
    u, v = alias7.get((a % 7, b % 7), (0, 0))
    alias7[a % 7, b % 7] = u+x, v+y
assert {d: z for d,z in alias7.items() if z!=(0,0)} == {(0,0): (3600,0)}
print(json.dumps(dict(norm_range=norm_range, isolated=isolated, small_moduli=tests,
                      prefixes_checked=sum(x+y for n, x, y in tests)), indent=1))
