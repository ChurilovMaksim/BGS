#!/usr/bin/env python3
"""Debug: find a pair with no transform to A''==A mod p^2 at (36,3),
and check whether S*!=0 pairs all have empty v=2 low-groups."""
from collections import defaultdict
import math

p, m = 3, 36
P = 27
def mul(x, y):
    return ((x[0]*y[0] + 2*x[1]*y[1]) % P, (x[0]*y[1] + x[1]*y[0]) % P)
def conj(x): return (x[0], (-x[1]) % P)
def tr(x): return (2*x[0]) % P
def inv(x):
    n = (x[0]*x[0] - 2*x[1]*x[1]) % P
    ni = pow(n, -1, P)
    c = conj(x)
    return ((c[0]*ni) % P, (c[1]*ni) % P)

alpha = (3, 2)
pw = [(1, 0)]
for i in range(1, m):
    pw.append(mul(pw[-1], alpha))
groups = defaultdict(list)
for a in range(P):
    for b in range(P):
        A = (a, b)
        vals = tuple(sorted(tr(mul(A, pw[i])) for i in range(m)))
        groups[vals].append(A)

n_notrans = 0
examples = []
sstar_nonzero_with_singletons = []
for vals, members in groups.items():
    base = members[0]
    if base[0] % p == 0 and base[1] % p == 0:
        continue
    # low-groups of base
    g = (1, 0)
    for _ in range(4):
        g = mul(g, alpha)
    gamma = g
    u = ((gamma[0]-1)//p % 9, gamma[1]//p % 9)
    lg = defaultdict(list)
    for r in range(4):
        C = mul(base, pw[r])
        Cu = ((C[0]*u[0] + 2*C[1]*u[1]) % 9, (C[0]*u[1] + C[1]*u[0]) % 9)
        if (2*Cu[0]) % 9 == 0:
            lg[tr(C) % 9].append((tr(C)//9) % 3)
    for A2 in members[1:]:
        found = set()
        for j in range(m):
            for refl in (False, True):
                App = mul(conj(A2) if refl else A2, pw[j])
                if (App[0]-base[0]) % 9 == 0 and (App[1]-base[1]) % 9 == 0:
                    D = mul(App, inv(base))
                    eta1 = ((D[0]-1)//9 % 3, D[1]//9 % 3)
                    found.add((2*eta1[0]) % 3)
        if not found:
            n_notrans += 1
            if len(examples) < 3:
                examples.append((base, A2, dict(lg)))
        elif found != {0} and lg:
            sstar_nonzero_with_singletons.append((base, A2, found, dict(lg)))
print("no-transform pairs:", n_notrans)
for base, A2, lg in examples:
    print("example base", base, "A2", A2, "lowgroups", lg)
    # what transforms come closest? print (A''-A) mod 9 for all transforms
    dists = defaultdict(int)
    for j in range(m):
        for refl in (False, True):
            App = mul(conj(A2) if refl else A2, pw[j])
            dists[((App[0]-base[0]) % 9, (App[1]-base[1]) % 9)] += 1
    print("  distinct (A''-A) mod 9 values:", len(dists), sorted(dists.items())[:12])
print("S*!=0 pairs WITH nonempty low-groups:", len(sstar_nonzero_with_singletons))
for row in sstar_nonzero_with_singletons[:5]:
    print("  ", row)
