#!/usr/bin/env python3
"""Wave 15: for (150,5), count S*!=0 pairs in fibres WITH v=2 singletons,
and verify the 0-or-2 collapsed-pairs lemma per A."""
from collections import defaultdict
import math, sys

m, p = 150, 5
P = p**3
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
assert mul(pw[-1], alpha) == (1, 0)
# L0
x = (1, 0); L0 = 0
while True:
    x = ((x[0]*3 + 2*x[1]*2) % p, (x[0]*2 + x[1]*3) % p); L0 += 1
    if x == (1, 0): break
print("L0 =", L0)
g = (1, 0)
for _ in range(L0):
    g = mul(g, alpha)
gamma = g
u = ((gamma[0]-1)//p % (p*p), gamma[1]//p % (p*p))
t = math.gcd(m, 4); gg = math.gcd(L0, t)
print("t =", t, "g =", gg, "u =", u)
step = (t * p * p) % m
H0 = []
z = (1, 0)
while True:
    H0.append(z)
    z = mul(z, pw[step])
    if z == (1, 0): break
print("|H0| =", len(H0))

groups = defaultdict(list)
for a in range(P):
    for b in range(P):
        A = (a, b)
        vals = tuple(sorted(tr(mul(A, pw[i])) for i in range(m)))
        groups[vals].append(A)
print("groups:", len(groups))

def lowgroups_of(base):
    lg = defaultdict(list)
    for r in range(gg):
        for z in H0:
            C = mul(mul(base, pw[r]), z)
            Cu = ((C[0]*u[0] + 2*C[1]*u[1]) % (p*p),
                  (C[0]*u[1] + C[1]*u[0]) % (p*p))
            if (2*Cu[0]) % (p*p) == 0:
                lg[tr(C) % (p*p)].append((tr(C)//(p*p)) % p)
    return lg

def collapsed_count(base):
    # (r,z) pairs with Tr(C u) == 0 mod p
    n = 0
    for r in range(gg):
        for z in H0:
            C = mul(mul(base, pw[r]), z)
            # C mod p, u mod p
            c0 = (C[0] % p, C[1] % p); u0 = (u[0] % p, u[1] % p)
            cu = (c0[0]*u0[0] + 2*c0[1]*u0[1]) % p
            if (2*cu) % p == 0:
                n += 1
    return n

# 0-or-2 lemma check on a sample of unit bases (all group bases + random)
import random
random.seed(1)
bases = [v[0] for v in groups.values()]
units = [b for b in bases if not (b[0] % p == 0 and b[1] % p == 0)]
print("unit group bases:", len(units))
bad02 = [(b, collapsed_count(b)) for b in units if collapsed_count(b) not in (0, 2)]
print("0-or-2 violations among unit group bases:", len(bad02), bad02[:5])
# also random unit A's
viol = 0
for _ in range(300):
    A = (random.randrange(P), random.randrange(P))
    if A[0] % p == 0 and A[1] % p == 0:
        continue
    if collapsed_count(A) not in (0, 2):
        viol += 1
        print("random violation:", A, collapsed_count(A))
print("random 0-or-2 violations:", viol)

# S* in singleton fibres only
nonzero_with_singletons = 0
pairs_in_singleton_fibres = 0
for vals, members in groups.items():
    base = members[0]
    if base[0] % p == 0 and base[1] % p == 0:
        continue
    lg = lowgroups_of(base)
    if not lg:
        continue
    for A2 in members[1:]:
        found = set()
        for j in range(m):
            for refl in (False, True):
                App = mul(conj(A2) if refl else A2, pw[j])
                if (App[0]-base[0]) % (p*p) == 0 and (App[1]-base[1]) % (p*p) == 0:
                    D = mul(App, inv(base))
                    eta1 = ((D[0]-1)//(p*p) % p, D[1]//(p*p) % p)
                    found.add((2*eta1[0]) % p)
        pairs_in_singleton_fibres += 1
        if found - {0}:
            nonzero_with_singletons += 1
            print("NONZERO with singletons:", base, A2, found, dict(lg))
print("pairs in singleton fibres:", pairs_in_singleton_fibres,
      "with S*!=0:", nonzero_with_singletons)
