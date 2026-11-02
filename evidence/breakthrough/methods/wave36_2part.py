"""Wave 36, task 4: 2-part census + reduction (tower) analysis at m = 2^k.

Census: kernel points mod q2 = 2^(2k+3) (SNF seeds), sorted-multiset
fibers, seed-space Gamma orbits (S: (a,b)->(b,6b-a), R: (a,b)->(a,6a-b)),
wave-16 support criterion (chunked, int64-safe).

Reduction analysis: level-k sequences are 2^(k-1)-periodic mod 2^(2k+1)
(proved: (M^(2^(k-1))+I) has det 4*odd, so (M^(2^(k-1))-I)seed = 0 mod
2^(2k+1)); hence reduction mod 2^(2k+1) maps level-k kernel points to
level-(k-1) kernel points, Gamma-equivariantly, 4-to-1. A level-k split
fiber is NEW if all its orbits reduce to a single level-(k-1) orbit,
and OLD (a lift) otherwise. For old fibers we record which reduced
orbit-set they map to, i.e. lift multiplicities.
"""
import sys, json
sys.path.insert(0, ".")
import numpy as np, sympy as sp
from collections import defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids, smith_normal_decomp
import math


def snf_kernel_i32(m, q):
    M = sp.Matrix([[6, -1], [1, 0]])
    A = M**m - sp.eye(2)
    S, U, V = smith_normal_decomp(A, domain=sp.ZZ)
    assert U * A * V == S
    d1, d2 = abs(int(S[0, 0])), abs(int(S[1, 1]))
    g1, g2 = math.gcd(d1, q), math.gcd(d2, q)
    assert g1 * g2 == q, (m, q, d1, d2, g1, g2)
    y0s = np.arange(0, q, q // g1, dtype=np.int64)
    y1s = np.arange(0, q, q // g2, dtype=np.int64)
    Y0, Y1 = np.meshgrid(y0s, y1s, indexing="ij")
    y0, y1 = Y0.ravel(), Y1.ravel()
    Vn = np.array(V.tolist(), dtype=np.int64) % q
    k0 = (Vn[0, 0] * y0 + Vn[0, 1] * y1) % q
    k1 = (Vn[1, 0] * y0 + Vn[1, 1] * y1) % q
    seqs = np.empty((len(k0), m), dtype=np.int32)
    seqs[:, 0] = k1.astype(np.int32)
    if m >= 2:
        seqs[:, 1] = k0.astype(np.int32)
        for i in range(1, m - 1):
            seqs[:, i + 1] = (6 * seqs[:, i] - seqs[:, i - 1]) % q
    return seqs


def orbit_canon(seeds, m, q):
    """Canonical seed of the Gamma orbit for each seed row (int64)."""
    ca, cb = seeds[:, 0].copy(), seeds[:, 1].copy()
    ba, bb = ca.copy(), cb.copy()
    for _ in range(m):
        y2 = (6 * ca - cb) % q
        upd = (ca < ba) | ((ca == ba) & (cb < bb))
        ba = np.where(upd, ca, ba); bb = np.where(upd, cb, bb)
        upd2 = (ca < ba) | ((ca == ba) & (y2 < bb))
        ba = np.where(upd2, ca, ba); bb = np.where(upd2, y2, bb)
        ca, cb = cb, (6 * cb - ca) % q
    return ba, bb


def main():
    m = int(sys.argv[1])
    k = m.bit_length() - 1
    assert m == 2 ** k and k >= 5, "m must be 2^k, k>=5"
    D = Dm(m)
    q2 = 2 ** sp.factorint(D)[2]
    print(f"m={m} k={k} q2={q2}", flush=True)
    Z, Qmod = torsion_data(m, D)
    pts = snf_kernel_i32(m, q2)
    assert len(pts) == q2
    print(f"points={len(pts)}", flush=True)
    fib = group_ids(np.sort(pts, axis=1))
    # support, chunked int64 matmul
    Qm = np.array([qq % q2 for qq in Qmod], dtype=np.int64)
    Z64 = Z.astype(np.int64)
    sup = np.empty(len(pts), dtype=bool)
    for s in range(0, len(pts), 65536):
        dot = pts[s:s + 65536].astype(np.int64) @ Z64.T
        sup[s:s + 65536] = ((2 * Qm[None, :] - dot) % q2 == 0).all(axis=1)
    seeds = pts[:, :2].astype(np.int64)
    ba, bb = orbit_canon(seeds, m, q2)
    gam = group_ids(np.stack([ba, bb], axis=1))
    fib_orbits = defaultdict(set)
    fib_sup = defaultdict(lambda: [0, 0])
    fib_idx = defaultdict(list)
    for i in range(len(pts)):
        f = int(fib[i])
        fib_orbits[f].add(int(gam[i]))
        fib_sup[f][0] += int(sup[i]); fib_sup[f][1] += 1
        fib_idx[f].append(i)
    split = [(f, fib_orbits[f], fib_sup[f]) for f in fib_orbits if len(fib_orbits[f]) > 1]
    onsup = [(f, o, s) for (f, o, s) in split if s[0] == s[1]]
    mixed = [(f, o, s) for (f, o, s) in split if 0 < s[0] < s[1]]
    print(f"split={len(split)} on-support={len(onsup)} mixed={len(mixed)}", flush=True)
    # reduction analysis on on-support split fibers
    qred = q2 // 4  # 2^(2k+1) = q2(m/2)
    half = m // 2
    # level-(k-1) support criterion, for reduced representatives
    Dhalf = Dm(half)
    assert 2 ** sp.factorint(Dhalf)[2] == qred
    Zh, Qmodh = torsion_data(half, Dhalf)
    Qmh = np.array([qq % qred for qq in Qmodh], dtype=np.int64)
    Zh64 = Zh.astype(np.int64)
    out = {"m": m, "k": k, "q2": int(q2), "split": len(split),
           "on_support": len(onsup), "mixed": len(mixed), "fibers": []}
    for (f, o, s) in sorted(onsup, key=lambda t: -fib_sup[t[0]][1]):
        idx = fib_idx[f]
        sub = pts[idx]
        sz = len(idx)
        # periodicity of reduction mod qred
        red = sub[:, :half] % qred
        per_ok = bool(np.all((sub % qred)[:, half:] == red))
        # reduced orbits: seeds of reduced sequences
        rseeds = red[:, :2].astype(np.int64)
        rba, rbb = orbit_canon(rseeds, half, qred)
        rgam = group_ids(np.stack([rba, rbb], axis=1))
        # reduced multiset id per point (first half sorted)
        rmult = group_ids(np.sort(red, axis=1))
        # orbit sizes at level k
        orb_sizes = defaultdict(int)
        for i in idx:
            orb_sizes[int(gam[i])] += 1
        # map: level-k orbit -> reduced orbit
        orb_to_red = {}
        for j, i in enumerate(idx):
            orb_to_red.setdefault(int(gam[i]), set()).add(int(rgam[j]))
        red_orbits = set().union(*orb_to_red.values()) if orb_to_red else set()
        kind = "NEW" if len(red_orbits) == 1 else "OLD"
        # reduced multiset consistency: all points same reduced multiset?
        rmult_consistent = bool(len(set(rmult.tolist())) == 1)
        # own orbit canons (representative seed canon per orbit)
        own_canons = sorted({(int(ba[i]), int(bb[i])) for i in idx})
        # distinct reduced orbit canons across the fiber's points
        red_canons = sorted({(int(rba[j]), int(rbb[j])) for j in range(len(idx))})
        # support of reduced representatives under level-(k-1) criterion
        reps = []
        seen_red = set()
        for j in range(len(idx)):
            key = (int(rba[j]), int(rbb[j]))
            if key not in seen_red:
                seen_red.add(key)
                reps.append(red[j])
        reps = np.array(reps, dtype=np.int64)
        dot = reps @ Zh64.T
        red_sup = bool(((2 * Qmh[None, :] - dot) % qred == 0).all(axis=1).all())
        rec = {"size": sz, "n_orbits": len(o), "orbit_sizes": sorted(orb_sizes.values()),
               "supported": f"{s[0]}/{s[1]}", "kind": kind,
               "n_reduced_orbits": len(red_orbits),
               "periodicity_ok": per_ok, "reduced_multiset_consistent": rmult_consistent,
               "reduced_orbit_canons": [[a, b] for (a, b) in red_canons],
               "own_orbit_canons": [[a, b] for (a, b) in own_canons],
               "reduced_supported": red_sup}
        out["fibers"].append(rec)
        print(f"  size={sz} orbits={len(o)} orbit_sizes={sorted(orb_sizes.values())} "
              f"sup={s[0]}/{s[1]} kind={kind} red_orbits={len(red_orbits)} "
              f"per_ok={per_ok} rmult_ok={rmult_consistent} red_sup={red_sup}", flush=True)
    with open(f"wave36_2part_m{m}.json", "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", f"wave36_2part_m{m}.json", flush=True)


if __name__ == "__main__":
    main()
