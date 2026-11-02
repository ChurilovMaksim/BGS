"""O* at m=13, component level.
H = 6I - C - C^T on Z^m, m=13. Fix mod q = ker(H mod q).
Enumerate via recurrence: v0,v1 free, v_{i+1} = 6 v_i - v_{i-1} mod q,
closure v_13=v0, v_14=v1.
For large q (358801) enumerate by solving first closure equation over v0:
compute M^13 (M=[[6,-1],[1,0]]) over integers, then for each v0 solve
a*v0 + b*v1 = 0 mod q (linear congruence), test second equation.
Fibers = sorted(y); affine group p[j]=a*j+b mod 13, a in (Z/13)^x,
action y'_j = y_{p[j]}; canon = lexicographic min over group.
"""
import json, math
import numpy as np

m = 13
D = 8957108164
QS = [4, 6241, 358801]

def mat_pow(M, e):
    # 2x2 integer matrix power
    R = [[1, 0], [0, 1]]
    B = [row[:] for row in M]
    while e:
        if e & 1:
            R = [[R[0][0]*B[0][0]+R[0][1]*B[1][0], R[0][0]*B[0][1]+R[0][1]*B[1][1]],
                 [R[1][0]*B[0][0]+R[1][1]*B[1][0], R[1][0]*B[0][1]+R[1][1]*B[1][1]]]
        B = [[B[0][0]*B[0][0]+B[0][1]*B[1][0], B[0][0]*B[0][1]+B[0][1]*B[1][1]],
             [B[1][0]*B[0][0]+B[1][1]*B[1][0], B[1][0]*B[0][1]+B[1][1]*B[1][1]]]
        e >>= 1
    return R

M13 = mat_pow([[6, -1], [1, 0]], 13)
print("M^13 =", M13)
# K = M^13 - I
K = [[M13[0][0]-1, M13[0][1]], [M13[1][0], M13[1][1]-1]]
print("K =", K, "det K =", K[0][0]*K[1][1]-K[0][1]*K[1][0])

def solve_congruence(b, rhs, q):
    """all x in [0,q) with b*x = rhs mod q, or None if none"""
    g = math.gcd(b % q, q)
    if rhs % g != 0:
        return []
    b1, q1, rhs1 = (b % q)//g, q//g, (rhs % q)//g
    inv = pow(b1, -1, q1)
    x0 = (rhs1 * inv) % q1
    return [x0 + k*q1 for k in range(g)]

def enum_fix(q):
    a, b = K[0][0] % q, K[0][1] % q
    c, d = K[1][0] % q, K[1][1] % q
    vecs = []
    for v0 in range(q):
        rhs = (-a*v0) % q
        for v1 in solve_congruence(b, rhs, q):
            if (c*v0 + d*v1) % q != 0:
                continue
            seq = [v0, v1]
            for _ in range(m):
                seq.append((6*seq[-1] - seq[-2]) % q)
            if seq[m] == v0 and seq[m+1] == v1:
                vecs.append(seq[:m])
            else:
                raise RuntimeError("closure mismatch despite K equations")
    return np.array(vecs, dtype=np.int64)

def check_H(vecs, q):
    # Hv = 6v_i - v_{i-1} - v_{i+1} mod q == 0
    Hv = (6*vecs - np.roll(vecs, 1, axis=1) - np.roll(vecs, -1, axis=1)) % q
    assert np.all(Hv == 0), "Hv != 0"

perms_aff = []
for a in range(1, m):
    if math.gcd(a, m) != 1:
        continue
    for bb in range(m):
        perms_aff.append([(a*j + bb) % m for j in range(m)])
perms_aff = np.array(perms_aff, dtype=np.int64)
print("affine perms:", len(perms_aff))
perms_dih = []
for k in range(m):
    perms_dih.append([(j + k) % m for j in range(m)])
    perms_dih.append([(k - j) % m for j in range(m)])
perms_dih = np.array(sorted({tuple(p) for p in perms_dih}), dtype=np.int64)
print("dihedral perms:", len(perms_dih))

def canon_chunked(vecs, perms):
    """lexicographic min over perms, chunked, mask method"""
    out = np.empty_like(vecs)
    CH = 20000
    for s in range(0, len(vecs), CH):
        chunk = vecs[s:s+CH]
        permuted = np.stack([chunk[:, p] for p in perms], axis=1)  # (n,P,m)
        mask = np.ones((len(chunk), len(perms)), dtype=bool)
        for c in range(m):
            vals = np.where(mask, permuted[:, :, c], np.iinfo(np.int64).max)
            mask &= (permuted[:, :, c] == vals.min(axis=1, keepdims=True))
        chosen = mask.argmax(axis=1)
        out[s:s+CH] = permuted[np.arange(len(chunk)), chosen]
    return out

results = {}
for q in QS:
    vecs = enum_fix(q)
    check_H(vecs, q)
    print(f"q={q}: |Fix|={len(vecs)}", flush=True)
    sorted_keys = np.sort(vecs, axis=1)
    uniq_sorted, counts = np.unique(sorted_keys, axis=0, return_counts=True)
    print(f"  fibers={len(uniq_sorted)} sizes dist:", {int(k): int(v) for k, v in zip(*np.unique(counts, return_counts=True))}, flush=True)
    canon = canon_chunked(vecs, perms_aff)
    combo = np.concatenate([sorted_keys, canon], axis=1)
    uniq_combo = np.unique(combo, axis=0)
    # orbits per fiber: count distinct combo rows per sorted key
    from collections import Counter
    orbit_per_fiber = Counter()
    for row in uniq_combo:
        orbit_per_fiber[tuple(row[:m].tolist())] += 1
    bad = [k for k, c in orbit_per_fiber.items() if c > 1]
    print(f"  aff-bad fibers={len(bad)}", flush=True)
    # distinct-value counts and periods for structure
    distinct_counts = {}
    for row in uniq_sorted:
        distinct_counts[len(set(row.tolist()))] = distinct_counts.get(len(set(row.tolist())), 0) + 1
    print(f"  distinct-value counts per fiber: {distinct_counts}", flush=True)
    results[q] = {
        "n_fix": int(len(vecs)),
        "n_fibers": int(len(uniq_sorted)),
        "fiber_size_dist": {int(k): int(v) for k, v in zip(*np.unique(counts, return_counts=True))},
        "aff_bad": int(len(bad)),
        "bad_examples": [list(k) for k in bad[:5]],
        "distinct_value_counts_per_fiber": {str(k): v for k, v in distinct_counts.items()},
    }
    # save vectors for the small components for later gluing analysis
    if q <= 6241:
        np.save(f"/home/hatch/workspace/bgs-breakthrough/methods/ostar_m13_fix_{q}.npy", vecs)

json.dump(results, open("/home/hatch/workspace/bgs-breakthrough/methods/ostar_m13_components.json", "w"), indent=1)
print(json.dumps(results, indent=1))
