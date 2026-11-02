"""Wave 11, task 2, search C: joint (2,3)-component exact per-class multisets.

For each m with 2|D_m and 3|D_m, enumerate Fix mod q2 and Fix mod q3,
form joint vectors (other components zero). Exact CRT values are a bijection
phi of joint tuples (z2[i], z3[i]), so exact per-class multisets are D_t-related
iff joint-tuple per-class multisets are. Group joint vectors by sorted joint
codes (z2*q3+z3); within each group check that the D_t-canonical form of the
per-class tuple is constant. A non-constant group is an exact per-class
failure in this subclass (verified directly by CRT lift for the example).
Also: triple joint (128,81,25) at m=12.
Reuses fix_mod_q from wave11_perclass_component (SNF-free congruence solver).
"""
import math, sys, time
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/bgs-breakthrough/methods')
from wave11_perclass_component import fix_mod_q, d_t_perms

def canon_and_groups(codes, m):
    """codes: (N,m) int64 joint codes. Returns (groups, bad list).
    groups: dict sorted-key bytes -> (canon bytes, example row index)."""
    t = math.gcd(m, 4)
    perms = d_t_perms(t)
    cls_idx = [[i for i in range(m) if i % t == r] for r in range(t)]
    srt = np.sort(codes, axis=1).astype(np.int64)
    pc = np.empty((len(codes), t, m//t), dtype=np.int64)
    for r, idx in enumerate(cls_idx):
        pc[:, r, :] = np.sort(codes[:, idx], axis=1)
    best = None
    for pi in perms:
        cand = pc[:, list(pi), :].reshape(len(codes), m)
        if best is None:
            best = cand.copy(); continue
        lt = np.zeros(len(codes), dtype=bool); eq = np.ones(len(codes), dtype=bool)
        for c in range(m):
            lt |= eq & (cand[:, c] < best[:, c])
            eq &= (cand[:, c] == best[:, c])
        best[lt] = cand[lt]
    groups = {}
    bad = []
    for j in range(len(codes)):
        key = srt[j].tobytes(); can = best[j].tobytes()
        ent = groups.get(key)
        if ent is None:
            groups[key] = (can, j)
        elif ent[0] != can:
            bad.append((ent[1], j))
            # keep first bad per group only by marking: store a sentinel
            groups[key] = (can, ent[1])  # keep reporting? avoid duplicate flood: use set below
    return groups, bad, best, srt

def check_pair(m, q2, q3, extra=None):
    t0 = time.time()
    v2 = fix_mod_q(m, q2)
    v3 = fix_mod_q(m, q3)
    codes = (v2[:, None, :] * q3 + v3[None, :, :]).reshape(-1, m)
    label = f"m={m} q2={q2} q3={q3}"
    if extra is not None:
        qx, vx = extra
        codes = (codes[:, None, :] * qx + vx[None, :, :]).reshape(-1, m)
        label += f" qx={qx}"
    # group + canon, tracking bad groups properly (recompute with dict of sets)
    t = math.gcd(m, 4)
    perms = d_t_perms(t)
    cls_idx = [[i for i in range(m) if i % t == r] for r in range(t)]
    srt = np.sort(codes, axis=1)
    pc = np.empty((len(codes), t, m//t), dtype=np.int64)
    for r, idx in enumerate(cls_idx):
        pc[:, r, :] = np.sort(codes[:, idx], axis=1)
    best = None
    for pi in perms:
        cand = pc[:, list(pi), :].reshape(len(codes), m)
        if best is None:
            best = cand.copy(); continue
        lt = np.zeros(len(codes), dtype=bool); eq = np.ones(len(codes), dtype=bool)
        for c in range(m):
            lt |= eq & (cand[:, c] < best[:, c])
            eq &= (cand[:, c] == best[:, c])
        best[lt] = cand[lt]
    groups = {}
    bad_groups = []
    for j in range(len(codes)):
        key = srt[j].tobytes(); can = best[j].tobytes()
        ent = groups.get(key)
        if ent is None:
            groups[key] = (can, j, {can})
        else:
            if can not in ent[2]:
                if len(ent[2]) == 1:
                    bad_groups.append((ent[1], j))
                ent[2].add(can)
    print(f"{label} N={len(codes)} groups={len(groups)} BAD_GROUPS={len(bad_groups)} time={time.time()-t0:.1f}s", flush=True)
    for a, b in bad_groups[:3]:
        print(f"  BAD pair rows {a} vs {b}", flush=True)
        print(f"    codes_a={tuple(codes[a])}", flush=True)
        print(f"    codes_b={tuple(codes[b])}", flush=True)
    return len(bad_groups)

def main():
    import sympy as sp
    total = 0
    for m in [4, 8, 12, 16, 20, 24, 28, 32, 36]:
        x, y = 1, 0
        for _ in range(m):
            x, y = 3*x+8*y, x+3*y
        D = 2*(x-1)
        fac = sp.factorint(D)
        if 2 not in fac or 3 not in fac:
            print(f"m={m} skip (no 2- and 3-part)", flush=True); continue
        q2 = 2**fac[2]; q3 = 3**fac[3]
        total += check_pair(m, q2, q3)
    # triple at m=12
    m = 12
    v25 = fix_mod_q(m, 25)
    # check_pair with extra needs v2/v3 inside; emulate by calling with extra=(25, v25)
    # but check_pair regenerates v2/v3; fine.
    total += check_pair(m, 128, 81, extra=(25, v25))
    print(f"TOTAL_BAD_GROUPS={total}", flush=True)

if __name__ == "__main__":
    main()
