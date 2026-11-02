# Wave 44, task 1 (recount) — classify ALL GPL-bad pairs at m=32, (8192,17):
# same (global, per-class marginals), different per-class joints.
# For each, find the joint pi-set relating the two joint tuples and check
# whether that pi stabilizes the marginal signature.
import math
from collections import Counter
ALPHA = (3, 2)
def mul(a, b, M):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % M, (a[0]*b[1] + a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    for _ in range(n):
        r = mul(r, a, M)
    return r
def genuine(M, m):
    d = pw(ALPHA, m, M); d = ((d[0]-1) % M, d[1]); d0, d1 = d; sols = []
    for x in range(M):
        rhs = (-d1*x) % M; g = math.gcd(d0, M)
        if rhs % g:
            continue
        d0p, Mp, rhsp = d0//g, M//g, rhs//g
        y0 = (rhsp * pow(d0p, -1, Mp)) % Mp
        for k in range(g):
            y = y0 + k*Mp
            if (d0*x + 2*d1*y) % M == 0 and (d1*x + d0*y) % M == 0:
                sols.append((x, y))
    return sols
m, q2, q = 32, 8192, 17
t = math.gcd(m, 4)
perms = [tuple((eps*r + b) % t for r in range(t)) for eps in (1, -1) for b in range(t)]
G2, Gq = genuine(q2, m), genuine(q, m)
def prep(G, M):
    ap = [pw(ALPHA, i, M) for i in range(m)]
    out = []
    for B in G:
        s = tuple((2*mul(B, a, M)[0]) % M for a in ap)
        marg = tuple(tuple(sorted(s[r::t])) for r in range(t))
        out.append((B, s, marg))
    return out
P2, Pq = prep(G2, q2), prep(Gq, q)
def joints_of(p, o):
    return tuple(tuple(sorted(zip(p[r::t], o[r::t]))) for r in range(t))
first = {}
bad_total = 0
pi_types = Counter()
marg_stab = Counter()
examples = []
for (B2, p, pm) in P2:
    for (Bq, o, om) in Pq:
        glob = tuple(sorted(zip(p, o)))
        j = joints_of(p, o)
        key = (glob, pm, om)
        prev = first.get(key)
        if prev is None:
            first[key] = (j, (B2, Bq), pm, om)
        elif prev[0] != j:
            bad_total += 1
            j0 = prev[0]
            pis = tuple(pp for pp in perms if all(j[r] == j0[pp[r]] for r in range(t)))
            pi_types[pis] += 1
            # does every such pi stabilize the marginal signature?
            pm0, om0 = prev[2], prev[3]
            stab = all(tuple(pm0[pp[r]] for r in range(t)) == pm0 and
                       tuple(om0[pp[r]] for r in range(t)) == om0 for pp in pis)
            marg_stab[stab] += 1
            if len(examples) < 3:
                examples.append(((B2, Bq), prev[1], pis))
print(f"GPL groups: {len(first)}, GPL-bad pairs (vs first-in-group): {bad_total}")
print("joint-pi types of bad pairs:", dict(pi_types))
print("bad pairs where every relating pi stabilizes marginals:", dict(marg_stab))
for e in examples:
    print("EXAMPLE bad pair:", e[0], "vs", e[1], "joint pis:", e[2])
