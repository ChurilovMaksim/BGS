"""Wave 10, task 2, experiment C: Pcarry exact search at m=36, other
components zero.
Enumerate Fix mod 128 and Fix mod 729 (m=36), lift by CRT with other
components 0 to global vectors y in Fix_36 (D = 3629521257408972904004611200),
group by sorted multiset, and check exact Lemma Y: all Y vectors in a
group lie in a single D4 orbit (not just mod D). Report groups, pairs,
exact failures.
"""
import numpy as np
from collections import defaultdict
import sys, time

m = 36
t = 4
# D_36 and factorisation (verified by sympy in analysis): 2^7 * 3^6 * ...
s0, s1 = 2, 6
for _ in range(2, m+1):
    s0, s1 = s1, 6*s1 - s0
D = s1 - 2
print(f"m={m} D={D}", flush=True)
q2, q3 = 128, 729
assert D % q2 == 0 and D % q3 == 0

def fix_mod_q(q):
    vecs = []
    y1_all = np.arange(q, dtype=np.int64)
    for y0 in range(q):
        a = np.full(q, y0, dtype=np.int64)
        b = y1_all.copy()
        seq = [a.copy(), b.copy()]
        for _ in range(m):
            c = (6*b - a) % q
            a, b = b, c
            seq.append(b.copy())
        ok = (seq[m] == y0) & (seq[m+1] == y1_all)
        idx = np.where(ok)[0]
        for j in idx:
            vecs.append(tuple(int(seq[k][j]) for k in range(m)))
    return vecs

t0 = time.time()
v2 = fix_mod_q(q2)
print(f"Fix mod {q2}: {len(v2)} (expect {q2})  [{time.time()-t0:.1f}s]", flush=True)
v3 = fix_mod_q(q3)
print(f"Fix mod {q3}: {len(v3)} (expect {q3})  [{time.time()-t0:.1f}s]", flush=True)
assert len(v2) == q2 and len(v3) == q3

def crt_coeff(q):
    Dj = D // q
    return (Dj * pow(Dj, -1, q)) % D

c2, c3 = crt_coeff(q2), crt_coeff(q3)
print(f"c2={c2} c3={c3}", flush=True)

def d4_orbit(v):
    out = set()
    for b in range(4):
        out.add(tuple(v[(i+b) % 4] for i in range(4)))
        out.add(tuple(v[(-i+b) % 4] for i in range(4)))
    return out

def Yvec(y):
    Y = [0]*4
    for i, val in enumerate(y):
        Y[i % 4] += val
    return tuple(Y)

groups = defaultdict(list)
for z2 in v2:
    for z3 in v3:
        y = tuple((c2*z2[i] + c3*z3[i]) % D for i in range(m))
        groups[tuple(sorted(y))].append(y)
print(f"lifts: {len(v2)*len(v3)}  groups: {len(groups)}  [{time.time()-t0:.1f}s]", flush=True)
multi = sum(1 for vs in groups.values() if len(vs) > 1)
print(f"groups with >1 vector: {multi}", flush=True)
fails = 0
fail_examples = []
pairs_checked = 0
for ms, vs in groups.items():
    if len(vs) < 2:
        continue
    Y0 = Yvec(vs[0])
    orb = d4_orbit(Y0)
    for y in vs[1:]:
        pairs_checked += 1
        Yp = Yvec(y)
        if Yp not in orb:
            fails += 1
            if len(fail_examples) < 5:
                fail_examples.append((vs[0], y, Y0, Yp))
print(f"pairs checked (vs first): {pairs_checked}  EXACT FAILURES: {fails}", flush=True)
for y, yp, Y, Yp in fail_examples:
    print(f"  FAIL y={y} yp={yp} Y={Y} Yp={Yp}")
# also verify mod-D agreement holds for all groups (sanity): Y mod D in single orbit
mod_fails = 0
for ms, vs in groups.items():
    if len(vs) < 2:
        continue
    Y0 = tuple(v % D for v in Yvec(vs[0]))
    orb = d4_orbit(Y0)
    for y in vs[1:]:
        if tuple(v % D for v in Yvec(y)) not in orb:
            mod_fails += 1
print(f"mod-D failures (sanity, expect 0): {mod_fails}", flush=True)
