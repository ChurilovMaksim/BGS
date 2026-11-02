"""Wave 31 exploration 2: structure of d1 and of (V0,V1)-collisions.

d1(xi) = p-digit of Tr(T_xi), T_xi = Teichmuller lift of xi mod p^3.
Question: is d1(x, y) independent of y? What formula?
Also: on orbits S = tau_bar * <beta_bar>, what do (V0,V1)-colliding
pairs look like?
"""
from collections import defaultdict


def mul(u, v, M):
    return ((u[0] * v[0] + 2 * u[1] * v[1]) % M,
            (u[0] * v[1] + u[1] * v[0]) % M)


def pw(u, e, M):
    r = (1, 0)
    while e:
        if e & 1:
            r = mul(r, u, M)
        u = mul(u, u, M)
        e >>= 1
    return r


def teich(A, p):
    M = p ** 3
    leg = pow(2, (p - 1) // 2, p)
    m = (p - 1) ** 2 if leg == 1 else p ** 2 - 1
    d = pow(p * p, -1, m)
    return pw(pw(A, p * p, M), d, M)


for p in (5, 7):
    M = p ** 3
    print(f"== p={p}: d1 table (rows x, cols y), xi = x + y sqrt2, units only ==")
    d1 = {}
    for x in range(p):
        row = []
        for y in range(p):
            if (x * x - 2 * y * y) % p == 0:
                row.append(" .")
                continue
            T = teich((x, y), p)
            tr = (2 * T[0]) % M
            d = (tr // p) % p
            d1[(x, y)] = d
            row.append(f"{d:2d}")
        print(f"x={x}: " + " ".join(row))
    # is d1 independent of y on each row?
    for x in range(p):
        vals = {d1[(x, y)] for y in range(p) if (x, y) in d1}
        print(f"  row x={x}: distinct d1 values: {sorted(vals)}")
    # check formula candidates: d1 vs Tr(xi)=2x, vs N(xi), vs xi^p digit?
    print("  d1 vs (x, N): ", end="")
    byN = defaultdict(set)
    for (x, y), d in d1.items():
        byN[(x, (x * x - 2 * y * y) % p)].add(d)
    print("all singletons:", all(len(v) == 1 for v in byN.values()))
print("DONE")
