# Wave 44, task 1 — Global Pairing Lemma test at m=32, (8192,17).
# GPL: genuine A, A' with equal GLOBAL multisets and equal per-class
# marginals (class-by-class, i.e. after transport to pi=id) have equal
# per-class joints. By the wave-40 transport lemma this implies the
# untransported statement (joints agree under the marginal pi).
# Also runs the plain two-component JBL test (group by global only,
# check joints agree under SOME pi in D_t).
# Genuine params are solved exactly (linear equations), not brute-forced.
import math, sys
from collections import defaultdict
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
print(f"|G2|={len(G2)} |Gq|={len(Gq)} pairs={len(G2)*len(Gq)}", flush=True)

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

gpl_bad = []   # (global, pm, om) group with differing joints
jbl_bad = []   # global group with no joint pi
first_gpl = {}
first_jbl = {}
n = 0
for (B2, p, pm) in P2:
    for (Bq, o, om) in Pq:
        glob = tuple(sorted(zip(p, o)))
        j = joints_of(p, o)
        key = (glob, pm, om)
        prev = first_gpl.get(key)
        if prev is None:
            first_gpl[key] = (j, (B2, Bq))
        elif prev[0] != j and len(gpl_bad) < 5:
            gpl_bad.append((key, prev[1], (B2, Bq), prev[0], j))
        prevj = first_jbl.get(glob)
        if prevj is None:
            first_jbl[glob] = (j, (B2, Bq))
        else:
            j0 = prevj[0]
            if not any(all(j[r] == j0[pp[r]] for r in range(t)) for pp in perms):
                if len(jbl_bad) < 5:
                    jbl_bad.append((glob, prevj[1], (B2, Bq)))
        n += 1
        if n % 500000 == 0:
            print(f"  ...{n} pairs, gpl_keys={len(first_gpl)} jbl_keys={len(first_jbl)}",
                  flush=True)
print(f"pairs processed: {n}")
print(f"GPL groups: {len(first_gpl)}, GPL counterexamples: {len(gpl_bad)}")
for b in gpl_bad:
    print("GPL-BAD:", b[1], b[2], "class joints differ")
    print("   first:", b[3])
    print("   other:", b[4])
print(f"JBL global groups: {len(first_jbl)}, JBL-bad pairs (first 5 shown): {len(jbl_bad)}")
for b in jbl_bad:
    print("JBL-BAD:", b[1], b[2])
print("GPL HOLDS" if not gpl_bad else "GPL REFUTED")
print("JBL HOLDS (this pair)" if not jbl_bad else "JBL-BAD FOUND")
