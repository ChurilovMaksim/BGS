"""Separation candidates on the m=12 O* counterexample pair (exact integers).

y, y' from gluing_m12_counterexample.py (verified: H y = H y' = 0 mod D,
sorted(y) = sorted(y'), distinct affine canons, both outside supp phihat_12).
Candidates: w_sorted (w = H y / D), pair_sorted (z_gamma . y over V4),
pair_mod_sorted, support passcount, neighbour sums S1/S2/S3/S6,
adjacency pair multiset, adjacency difference multiset, w Gamma-canon.
Also the m=8 first bad pair is recomputed for comparison (values already in
sep_m8_result.json; here only m=12).
"""
import json
import numpy as np
import sympy as sp

m = 12
D = 1536796800
y = (1366041600, 1366041600, 683020800, 1195286400, 341510400, 853776000,
     170755200, 170755200, 853776000, 341510400, 1195286400, 683020800)
yp = (1366041600, 1195286400, 1195286400, 1366041600, 853776000, 683020800,
      170755200, 341510400, 341510400, 170755200, 683020800, 853776000)

def Hvec(v):
    return [6*v[i] - v[(i-1) % m] - v[(i+1) % m] for i in range(m)]

# V4 by recurrence (as in oprime_m12_counterexample_test.py)
V4 = []
for a in range(4):
    for b in range(4):
        seq = [a, b]
        for _ in range(10):
            seq.append((2*seq[-1] - seq[-2]) % 4)
        if (2*seq[11] - seq[10]) % 4 != seq[0]:
            continue
        if (2*seq[0] - seq[11]) % 4 != seq[1]:
            continue
        assert all(x % 4 == 0 for x in Hvec(seq))
        V4.append(tuple(seq))
assert len(V4) == 16
tors = []
for v in V4:
    hv = Hvec(v)
    assert all(x % 4 == 0 for x in hv)
    tors.append(tuple(x // 4 for x in hv))

Hsp = sp.zeros(m)
for i in range(m):
    Hsp[i, i] = 6; Hsp[i, (i-1) % m] -= 1; Hsp[i, (i+1) % m] -= 1
assert int(Hsp.det()) == D
Qnum = []
for z in tors:
    t = Hsp.LUsolve(sp.Matrix([D*zz for zz in z]))
    assert all(x.q == 1 for x in t)
    t = tuple(int(x) for x in t)
    Qnum.append(sum(zz*tt for zz, tt in zip(z, t)))
Qnum = np.array(Qnum, dtype=np.int64)

gam_perms = []
for k in range(m):
    gam_perms.append([(j + k) % m for j in range(m)])
    gam_perms.append([(k - j) % m for j in range(m)])
gam_perms = np.array(gam_perms, dtype=np.int64)

def canon(vec, perms):
    vec = np.array(vec, dtype=np.int64)
    cands = [tuple(vec[p].tolist()) for p in perms]
    return min(cands)

def cand(vec):
    v = np.array(vec, dtype=np.int64)
    hv = np.array(Hvec(vec), dtype=np.int64)
    assert np.all(hv % D == 0)
    w = hv // D
    pr = np.array([sum(zz*vv for zz, vv in zip(z, vec)) for z in tors], dtype=np.int64)
    return {
        "w": w.tolist(),
        "w_sorted": sorted(w.tolist()),
        "pair_sorted": [int(x) for x in sorted(pr.tolist())],
        "pair_mod_sorted": [int(x) for x in sorted((pr % D).tolist())],
        "support_passcount": int((((2*Qnum - pr) % D) == 0).sum()),
        "S1": int((v * np.roll(v, -1)).sum()),
        "S2": int((v * np.roll(v, -2)).sum()),
        "S3": int((v * np.roll(v, -3)).sum()),
        "S6": int((v * np.roll(v, -6)).sum()),
        "adj_pair": sorted(zip(v.tolist(), np.roll(v, -1).tolist())),
        "adj_diff": sorted(((np.roll(v, -1) - v) % D).tolist()),
        "w_gamma_canon": list(canon(w, gam_perms)),
        "y_gamma_canon": list(canon(v, gam_perms)),
    }

cy, cyp = cand(y), cand(yp)
out = {"y": cy, "y_prime": cyp,
       "separates": {k: cy[k] != cyp[k] for k in cy}}
for k in cy:
    print(f"{k}: separates={cy[k] != cyp[k]}")
    print("  y :", cy[k])
    print("  y':", cyp[k])
json.dump(out, open('/home/hatch/workspace/bgs-breakthrough/methods/sep_m12_pair_result.json', 'w'), indent=1, default=str)
print("written sep_m12_pair_result.json")
