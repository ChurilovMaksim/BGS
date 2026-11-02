"""Structure verification for O* at m=13, needed for the gluing argument.
For each component q in {4, 6241, 358801}, for each v in Fix mod q:
- distinct-value count and multiplicity pattern
- fiber size (from sorted key)
- number of reflections (of 13) fixing v, number of nontrivial rotations fixing v
Expected: constant -> distinct 1, fiber 1, refl 13, rot-fix 12 (all);
distinct -> distinct 13, fiber 26, refl 0, rot-fix 0;
reflection type -> distinct 7, multiplicities 1x1+6x2, fiber 13, refl exactly 1, rot-fix 0.
Dihedral orbit size then = 26/(stabiliser size) = fiber size, so dihedral
orbit = fiber, i.e. A(v)=D(v) in effect (with aff-bad=0 from components run).
"""
import json, math
import numpy as np
from collections import Counter

m = 13
# reuse enumeration from components script by importing its functions inline
import importlib.util, sys
# Instead of importing (which runs the whole script), copy the enumerator:
def mat_pow(M, e):
    R = [[1, 0], [0, 1]]; B = [row[:] for row in M]
    while e:
        if e & 1:
            R = [[R[0][0]*B[0][0]+R[0][1]*B[1][0], R[0][0]*B[0][1]+R[0][1]*B[1][1]],
                 [R[1][0]*B[0][0]+R[1][1]*B[1][0], R[1][0]*B[0][1]+R[1][1]*B[1][1]]]
        B = [[B[0][0]*B[0][0]+B[0][1]*B[1][0], B[0][0]*B[0][1]+B[0][1]*B[1][1]],
             [B[1][0]*B[0][0]+B[1][1]*B[1][0], B[1][0]*B[0][1]+B[1][1]*B[1][1]]]
        e >>= 1
    return R
M13 = mat_pow([[6, -1], [1, 0]], 13)
K = [[M13[0][0]-1, M13[0][1]], [M13[1][0], M13[1][1]-1]]

def solve_congruence(b, rhs, q):
    g = math.gcd(b % q, q)
    if rhs % g != 0: return []
    b1, q1, rhs1 = (b % q)//g, q//g, (rhs % q)//g
    return [(rhs1 * pow(b1, -1, q1)) % q1 + k*q1 for k in range(g)]

def enum_fix(q):
    a, b = K[0][0] % q, K[0][1] % q
    c, d = K[1][0] % q, K[1][1] % q
    vecs = []
    for v0 in range(q):
        for v1 in solve_congruence(b, (-a*v0) % q, q):
            if (c*v0 + d*v1) % q != 0: continue
            seq = [v0, v1]
            for _ in range(m): seq.append((6*seq[-1] - seq[-2]) % q)
            assert seq[m] == v0 and seq[m+1] == v1
            vecs.append(seq[:m])
    return np.array(vecs, dtype=np.int64)

refl_perms = np.array([[(c - j) % m for j in range(m)] for c in range(m)], dtype=np.int64)
rot_perms = np.array([[(j + k) % m for j in range(m)] for k in range(1, m)], dtype=np.int64)

out = {}
for q in [4, 6241, 358801]:
    vecs = enum_fix(q)
    print(f"q={q} n={len(vecs)}", flush=True)
    sorted_keys = np.sort(vecs, axis=1)
    _, inv, counts = np.unique(sorted_keys, axis=0, return_inverse=True, return_counts=True)
    fiber_size = counts[inv]
    # reflection fix counts, chunked
    refl_fix = np.zeros(len(vecs), dtype=np.int64)
    rot_fix = np.zeros(len(vecs), dtype=np.int64)
    CH = 20000
    for s in range(0, len(vecs), CH):
        chunk = vecs[s:s+CH]
        for p in refl_perms:
            refl_fix[s:s+CH] += np.all(chunk[:, p] == chunk, axis=1)
        for p in rot_perms:
            rot_fix[s:s+CH] += np.all(chunk[:, p] == chunk, axis=1)
    # distinct counts + multiplicity patterns (chunked via sorted rows: multiplicities from run lengths)
    distinct = np.empty(len(vecs), dtype=np.int64)
    patterns = Counter()
    joint = Counter()
    for s in range(0, len(vecs), CH):
        sk = sorted_keys[s:s+CH]
        # run lengths per row
        diff = np.ones((len(sk), m), dtype=bool)
        diff[:, 1:] = sk[:, 1:] != sk[:, :-1]
        # distinct = sum diff
        distinct[s:s+CH] = diff.sum(axis=1)
        # multiplicities: need per-row run lengths; do in python for chunk rows (chunk <=20000, ok)
        for i, row in enumerate(sk):
            runs = []
            cur = 1
            for t in range(1, m):
                if row[t] == row[t-1]: cur += 1
                else: runs.append(cur); cur = 1
            runs.append(cur)
            pat = tuple(sorted(runs))
            patterns[pat] += 1
            joint[(int(distinct[s+i]), pat, int(fiber_size[s+i]), int(refl_fix[s+i]), int(rot_fix[s+i]))] += 1
    print(f"  patterns: {dict(patterns)}", flush=True)
    print(f"  joint (distinct, pattern, fiber, refl_fix, rot_fix): count", flush=True)
    for k, v in sorted(joint.items()):
        print(f"    {k}: {v}", flush=True)
    out[q] = {
        "n": int(len(vecs)),
        "patterns": {str(k): v for k, v in patterns.items()},
        "joint": {str(k): v for k, v in joint.items()},
    }
json.dump(out, open("/home/hatch/workspace/bgs-breakthrough/methods/ostar_m13_structure.json", "w"), indent=1)
print("DONE")
