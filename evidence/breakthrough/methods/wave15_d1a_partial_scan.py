"""Wave 15, task 3: scan m for a SPLIT fiber PARTIALLY in supp(phihat).

Definitions (as in wave 14, task 3):
  D_m = det H_m = s_m - 2, s_0=2, s_1=6, s_{n+1}=6 s_n - s_{n-1}.
  Fix_m = length-m sequences mod D_m with y_{i+1} = 6 y_i - y_{i-1}
          (mod D_m) and m-periodic  <=>  (y_1, y_0) in ker(M^m - I).
  Fiber = same sorted multiset of entries.
  Gamma-orbit = dihedral action on positions (shifts + reflections).
  Split fiber = fiber with > 1 Gamma-orbit.
  Support (s=1): y in supp iff for every torsion representative
  z = (H v)/4, v in ker(H mod 4): (2*Qnum(z) - z.y) == 0 mod D,
  where Qnum(z) = z^T adj(H) z.
  Partial fiber = 0 < #(fiber cap supp) < |fiber|.
  (phihat is Gamma-invariant, so partial <=> mixed support across
  the fiber's orbits.)

Enumeration via SNF of A = M^m - I (2x2): U A V = diag(d1, d2),
kernel vectors x = V y with d_i y_i == 0 mod D.  Count = D.
"""
import json
import sys

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp


def Dm(m):
    s0, s1 = 2, 6
    if m == 0:
        return s0 - 2
    if m == 1:
        return s1 - 2
    for _ in range(2, m + 1):
        s0, s1 = s1, 6 * s1 - s0
    return s1 - 2


def fix_points(m, D):
    M = sp.Matrix([[6, -1], [1, 0]])
    A = M**m - sp.eye(2)
    S, U, V = smith_normal_decomp(A, domain=sp.ZZ)
    assert U * A * V == S
    d1, d2 = int(S[0, 0]), int(S[1, 1])
    assert d1 * d2 == D or d1 * d2 == -D, (d1, d2, D)
    import math
    g1, g2 = math.gcd(abs(d1), D), math.gcd(abs(d2), D)
    assert g1 * g2 == D, (g1, g2, D)
    y0s = np.arange(0, D, D // g1, dtype=np.int64)
    y1s = np.arange(0, D, D // g2, dtype=np.int64)
    Y0, Y1 = np.meshgrid(y0s, y1s, indexing="ij")
    y0 = Y0.ravel()
    y1 = Y1.ravel()
    Vnp = np.array(V.tolist(), dtype=np.int64)
    k0 = (Vnp[0, 0] * y0 + Vnp[0, 1] * y1) % D
    k1 = (Vnp[1, 0] * y0 + Vnp[1, 1] * y1) % D
    # kernel check: A @ (k0, k1) == 0 mod D
    Anp = np.array(A.tolist(), dtype=np.int64)
    assert np.all((Anp[0, 0] * k0 + Anp[0, 1] * k1) % D == 0)
    assert np.all((Anp[1, 0] * k0 + Anp[1, 1] * k1) % D == 0)
    # seed (y0_seq, y1_seq) = (k1, k0) since kernel vector is (y1, y0)
    seqs = np.empty((D, m), dtype=np.int32)
    seqs[:, 0] = k1.astype(np.int32)
    if m >= 2:
        seqs[:, 1] = k0.astype(np.int32)
        for i in range(1, m - 1):
            seqs[:, i + 1] = (6 * seqs[:, i].astype(np.int64)
                              - seqs[:, i - 1]) % D
        seqs = seqs.astype(np.int32)
    # sanity: H y == 0 mod D
    Hy = (6 * seqs.astype(np.int64)
          - np.roll(seqs, 1, axis=1) - np.roll(seqs, -1, axis=1)) % D
    assert np.all(Hy == 0), "H y != 0 mod D"
    return seqs


def torsion_data(m, D):
    # V4: v in (Z/4)^m from seeds (v0, v1), m-periodic mod 4
    vs = []
    for a in range(4):
        for b in range(4):
            seq = [a, b]
            for _ in range(m):
                seq.append((2 * seq[-1] - seq[-2]) % 4)
            if seq[m] == a and seq[m + 1] == b:
                vs.append(seq[:m])
    Hsp = sp.zeros(m)
    for i in range(m):
        Hsp[i, i] = 6
        Hsp[i, (i - 1) % m] -= 1
        Hsp[i, (i + 1) % m] -= 1
    X = np.array(Hsp.adjugate().tolist(), dtype=np.int64)
    zs, qs = [], []
    for v in vs:
        hv = np.array([6 * v[i] - v[(i - 1) % m] - v[(i + 1) % m]
                       for i in range(m)], dtype=np.int64)
        assert np.all(hv % 4 == 0)
        z = hv // 4
        zs.append(z)
        qs.append(int((z @ X @ z) % D))
    return np.array(zs, dtype=np.int64), np.array(qs, dtype=np.int64)


def support_mask(pts, Z, Q, D, chunk=200000):
    out = np.empty(len(pts), dtype=bool)
    for st in range(0, len(pts), chunk):
        ch = pts[st:st + chunk].astype(np.int64)
        dot = ch @ Z.T  # (chunk, n_z)
        ok = ((2 * Q[None, :] - dot) % D == 0).all(axis=1)
        out[st:st + chunk] = ok
    return out


def gamma_perms(m):
    perms = []
    seen = set()
    for k in range(m):
        for p in (tuple((j + k) % m for j in range(m)),
                  tuple((k - j) % m for j in range(m))):
            if p not in seen:
                seen.add(p)
                perms.append(p)
    return np.array(perms, dtype=np.int64)


def lex_canon(arr, perms, chunk=100000):
    out = np.empty_like(arr)
    for st in range(0, len(arr), chunk):
        ch = arr[st:st + chunk]
        permuted = np.stack([ch[:, p] for p in perms], axis=1)
        mask = np.ones((len(ch), len(perms)), dtype=bool)
        for cc in range(arr.shape[1]):
            vals = np.where(mask, permuted[:, :, cc],
                            np.iinfo(arr.dtype).max)
            mask &= (permuted[:, :, cc] == vals.min(axis=1, keepdims=True))
        chosen = mask.argmax(axis=1)
        out[st:st + chunk] = permuted[np.arange(len(ch)), chosen]
    return out


def phihat_direct(pts, m, D, idxs):
    """Direct phihat_s=1 for selected points (small D only)."""
    Hsp = sp.zeros(m)
    for i in range(m):
        Hsp[i, i] = 6
        Hsp[i, (i - 1) % m] -= 1
        Hsp[i, (i + 1) % m] -= 1
    X = np.array(Hsp.adjugate().tolist(), dtype=np.int64)
    Hg = (6 * pts.astype(np.int64) - np.roll(pts, 1, axis=1)
          - np.roll(pts, -1, axis=1))
    assert np.all(Hg % D == 0)
    W = (Hg // D).astype(np.int64)
    Qw = np.einsum("ij,ij->i", W @ X, W)
    XW = W @ X
    res = {}
    for i in idxs:
        P = XW @ W[i]
        ex = (2 * Qw - P) % D
        val = np.exp(2j * np.pi * ex / D).sum() / D
        res[int(i)] = complex(val)
    return res


def scan(m, direct_check=False):
    D = Dm(m)
    pts = fix_points(m, D)
    assert len(pts) == D
    Z, Q = torsion_data(m, D)
    supp = support_mask(pts, Z, Q, D)
    n_supp = int(supp.sum())
    v4size = len(Z)
    supp_ok = (D % v4size == 0 and n_supp == D // v4size)
    sorted_keys = np.sort(pts, axis=1)
    _, fib_id = np.unique(sorted_keys, axis=0, return_inverse=True)
    fib_id = np.asarray(fib_id).reshape(-1)
    n_fib = int(fib_id.max()) + 1
    fib_size = np.bincount(fib_id, minlength=n_fib)
    perms = gamma_perms(m)
    canon = lex_canon(pts, perms)
    _, gam_id = np.unique(canon, axis=0, return_inverse=True)
    gam_id = np.asarray(gam_id).reshape(-1)
    n_gam = int(gam_id.max()) + 1
    gam_fiber = np.empty(n_gam, dtype=np.int64)
    gam_fiber[gam_id] = fib_id
    orbits_per_fiber = np.bincount(gam_fiber, minlength=n_fib)
    bad = np.where(orbits_per_fiber > 1)[0]
    in_supp = np.bincount(fib_id[supp], minlength=n_fib)
    full = np.where(in_supp == fib_size)[0]
    empty = np.where(in_supp == 0)[0]
    partial = np.where((in_supp > 0) & (in_supp < fib_size))[0]
    rep = {"m": m, "D": D, "n_points": int(len(pts)), "V4_size": v4size,
           "support_size": n_supp, "support_eq_D_over_V4": bool(supp_ok),
           "n_fibers": n_fib, "n_gamma_orbits": n_gam,
           "n_split_fibers": int(len(bad)),
           "fibers_full_in_supp": int(len(full)),
           "fibers_empty": int(len(empty)),
           "fibers_partial": int(len(partial)),
           "split_fibers_meeting_supp": int(len(np.intersect1d(bad, full))),
           "split_fibers_partial": int(len(np.intersect1d(bad, partial)))}
    print(json.dumps(rep), flush=True)
    detail = None
    if len(partial):
        f0 = int(partial[0])
        sub = np.where(fib_id == f0)[0]
        orbits = {}
        for g in sorted(set(gam_id[sub].tolist())):
            oo = sub[gam_id[sub] == g]
            orbits[int(g)] = {"size": int(len(oo)),
                              "n_in_supp": int(supp[oo].sum())}
        detail = {"first_partial_fiber": f0, "fiber_size": int(len(sub)),
                  "n_orbits": len(orbits), "orbits": orbits,
                  "example_point": pts[sub[0]].tolist()}
        print("PARTIAL DETAIL:", json.dumps(detail), flush=True)
    if direct_check:
        rng = np.random.default_rng(1)
        idxs = rng.choice(len(pts), size=min(8, len(pts)), replace=False)
        ph = phihat_direct(pts, m, D, idxs)
        target = v4size / D
        for i, val in ph.items():
            in_s = bool(supp[i])
            agree = (abs(val) ** 2 > target / 2) == in_s
            on = abs(abs(val) ** 2 - target) < 1e-9 if in_s else abs(val) < 1e-9
            print(f"  direct-check pt {i}: supp={in_s} |phi|^2={abs(val)**2:.3e} "
                  f"target={target:.3e} agree={agree} modulus_ok={on}", flush=True)
            assert agree and on
    return rep, detail


if __name__ == "__main__":
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    results = {}
    for m in range(lo, hi + 1):
        rep, detail = scan(m, direct_check=(m <= 6))
        results[m] = rep
        if detail:
            results[m]["detail"] = detail
    with open(f"/tmp/wave15_scan_{lo}_{hi}.json", "w") as fh:
        json.dump(results, fh, indent=1)
