"""Collect CORRECTED sol_6 for ODD k to fit its closed form."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys
sys.path.insert(0, _BGS_ROOT + r"\src")
from phase3_r6_families import enumerate_sols
from sympy import primitive_root

pts = []
for (p, k) in [(211, 15), (211, 21), (211, 35), (101, 25),
               (401, 25), (307, 21)]:
    if (p - 1) % k != 0:
        continue
    g = int(primitive_root(p))
    alpha = pow(g, (p - 1) // k, p)
    H = set(); x = 1
    for _ in range(k):
        H.add(x); x = x * alpha % p
    n = len(enumerate_sols(p, H))
    pts.append((k, n))
    print(f"odd k={k} (p={p}): sol6={n}")

print("\nfit cubic through first three points:")
(k1, n1), (k2, n2), (k3, n3) = pts[0], pts[1], pts[2]
import numpy as np
A = np.array([[k**3, k*k, k, 1] for k, _ in pts[:3]])
b = np.array([n for _, n in pts[:3]])
a3, a2, a1_, a0 = np.linalg.solve(A, b)
print(f"T_odd = {a3:.0f}k^3 + {a2:.0f}k^2 + {a1_:.0f}k + {a0:.0f}")
for k, n in pts:
    pred = a3*k**3 + a2*k*k + a1_*k + a0
    print(f"  k={k}: actual={n} pred={pred:.0f} "
          f"{'OK' if abs(pred-n)<0.5 else 'FAIL'}")
