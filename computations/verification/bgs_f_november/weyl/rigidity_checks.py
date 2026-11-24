"""Verify the two physical Fourier modes and every finite-iteration cutoff."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fractions import Fraction as F
from pathlib import Path
import sys
import json

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'research'))
from coefficients import raw_symbol

# Coefficients of the midpoint symbol in q,p frequency order.
physical = {(b, a): tuple(((-1)**(a*b % 2))*i for i in c)
            for (a, b), c in raw_symbol().items()}
transpose = ((3, -2), (-4, 3))
B = ((3, -4), (-2, 3))

def act(mat, v):
    return tuple(row[0]*v[0]+row[1]*v[1] for row in mat)

supports = []
for e in [(1, 0), (0, 1)]:
    target = act(transpose, e)
    for length in range(1, 11):
        hits = []
        for d in physical:
            z = d
            for i in range(1, length+1):
                z = act(transpose, z)
                if z == target:
                    hits.append((i, d))
        assert hits == [(1, e)]
        x, y = physical[e]
        direction = (-e[1], e[0])
        for _ in range(length-1):
            direction = act(B, direction)
        square = F((x*x+y*y)*sum(v*v for v in direction), 4000**2)
        assert square > F(1, 10**22)
        supports.append([list(e), length, str(square)])
    x, y = physical[e]
    projection = F(1, 2) if e[0] else F(1, 4)
    # lambda < 6; the inverse-conjugacy error divided by tau is < 10^-30.
    assert F(x*x+y*y, 4000**2)*projection/36 > (F(1,10**4)+F(1,10**30))**2
assert F(58,10)**11 > 4*10**7
assert F(10**8,10**80) + F(10**5,10**40) < F(1,10**30)
err = 0
for j in range(1, 11):
    err = 8*err + 10**4 + 8000*20*(8**(j-1)-1)//7
assert err < 10**20
print(json.dumps(dict(first_order_mode_checks=supports, last_error_constant=err), indent=1))
