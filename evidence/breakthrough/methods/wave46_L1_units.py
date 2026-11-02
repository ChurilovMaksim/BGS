#!/usr/bin/env python3
"""Wave 46, task 1 (part 2): unit-restricted L1-corrected check at p^f,
mod-49 degenerate counterexample (1,2) vs (1,5), Stab(M) example at 49."""
import math
from collections import defaultdict
from wave46_L1_checks import mul, conj, tr, order, cycle_multiset, dihedral_orbit, pw

def check_units(p, f):
    m = p**f; beta = (17 % m, 12 % m); T = order(beta, m)
    units = [u for u in range(m) if math.gcd(u, m) == 1]
    groups = defaultdict(list)
    for a in range(m):
        for b in range(m):
            C = (a, b)
            if math.gcd((a*a - 2*b*b) % m, m) != 1: continue
            groups[cycle_multiset(C, beta, T, m)].append(C)
    nviol = nscal = 0
    for M, cs in groups.items():
        c0 = cs[0]; orb = dihedral_orbit(c0, beta, T, m)
        scal = {mul((lam, 0), o, m) for lam in units for o in orb}
        for C in cs:
            if C not in orb:
                nviol += 1
                if C in scal: nscal += 1
    print(f"mod {m} units-only: T={T} groups={len(groups)} "
          f"violations={nviol} scaling-explained={nscal} unexplained={nviol-nscal}")

def cyc(C, beta, T, m):
    x = C; out = []
    for _ in range(T): out.append(tr(x, m)); x = mul(x, beta, m)
    return out

m = 49; beta = (17, 12); T = order(beta, m)
print("== mod-49 degenerate counterexample ==")
t1, t2 = cyc((1, 2), beta, T, m), cyc((1, 5), beta, T, m)
print("N(1,2) =", (1 - 8) % m, " N(1,5) =", (1 - 50) % m)
print("cycle(1,2) =", t1)
print("cycle(1,5) =", t2)
print("same multiset:", sorted(t1) == sorted(t2), "| all 21 values distinct:",
      len(set(t1)) == 21)
orb = dihedral_orbit((1, 2), beta, T, m)
units = [u for u in range(m) if math.gcd(u, m) == 1]
scal = {mul((lam, 0), o, m) for lam in units for o in orb}
print("(1,5) in dihedral orbit:", (1, 5) in orb,
      "| in scaling closure:", (1, 5) in scal)
print()
print("== Stab(M) example at 49: C = sqrt2, outsider 6*sqrt2 = 43*conj ==")
M = cycle_multiset((0, 1), beta, T, m)
stab = [lam for lam in units if tuple(sorted((lam*v) % m for v in M)) == M]
print("Stab(M) =", stab)
print("Stab == {lam : lam = +-1 mod 7}:",
      stab == [u for u in units if u % 7 in (1, 6)])
print()
for p, f in [(5, 2), (7, 2), (11, 2), (5, 3), (13, 2)]:
    check_units(p, f)
