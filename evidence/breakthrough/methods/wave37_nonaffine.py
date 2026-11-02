"""Wave 37, task 5: characterize the 18,000 non-affine pairs at m=30.

Reproduces the wave-36 slice exactly: K1 = kernel mod 625, K2 = kernel
mod 841, slice point (i1, i2) has row K1[i1]*841 + K2[i2], flat index
i1*841 + i2. Fibers = groups by sorted row. Affine maps: sigma(i) =
u*i + c mod 30, gcd(u,30)=1 (240 maps). A pair has an exactly-affine
matching iff its two points lie in the same orbit of the diagonal
affine action on the slice (canonical rep = min image index).
Repository untouched, no Lean build.
"""
import numpy as np
from collections import Counter

M = 30
N1, N2 = 625, 841


def kernel_mod_np(m, mod):
    a, b = np.meshgrid(np.arange(mod), np.arange(mod), indexing="ij")
    a = a.ravel().astype(np.int64)
    b = b.ravel().astype(np.int64)
    seqs = [a, b]
    for _ in range(m):
        seqs.append((6 * seqs[-1] - seqs[-2]) % mod)
    ok = (seqs[m] == a) & (seqs[m + 1] == b)
    out = np.stack([s[ok] for s in seqs[:m]], axis=1)
    assert len(out) == mod, (m, mod, len(out))
    return out.astype(np.int32)


def row_index_map(K):
    d = {}
    for i, row in enumerate(K):
        d[row.tobytes()] = i
    return d


def main():
    K1 = kernel_mod_np(M, N1)
    K2 = kernel_mod_np(M, N2)
    print(f"K1 {K1.shape}, K2 {K2.shape}", flush=True)
    N = N1 * N2
    # component fibers (sorted component multisets)
    s1 = np.sort(K1, axis=1)
    _, f1id = np.unique(s1, axis=0, return_inverse=True)
    s2 = np.sort(K2, axis=1)
    _, f2id = np.unique(s2, axis=0, return_inverse=True)
    print(f"component fibers: F1={f1id.max()+1}, F2={f2id.max()+1}",
          flush=True)
    # global fibers = groups by sorted row (equivalently by the sorted
    # multiset of pairs (a_j, b_j), since (a,b) -> a*841+b is injective).
    # NOTE: the pair of marginal component multisets does NOT determine
    # the fiber -- the joint pairing matters -- so no product shortcut.
    i1_all = np.repeat(np.arange(N1), N2)
    i2_all = np.tile(np.arange(N2), N1)
    P = (K1[:, None, :].astype(np.int64) * N2 +
         K2[None, :, :].astype(np.int64)).astype(np.int32)
    flat = P.reshape(N, M)
    srt = np.sort(flat, axis=1)
    _, gfib, counts = np.unique(srt, axis=0, return_inverse=True,
                                return_counts=True)
    gcounts = counts
    print(f"global fibers (sorted rows): {len(counts)}, max size "
          f"{counts.max()}, total pairs "
          f"{int((counts * (counts - 1) // 2).sum())}", flush=True)
    assert len(counts) == 9061
    assert counts.max() == 150
    # affine maps PA/PB
    d1, d2 = row_index_map(K1), row_index_map(K2)
    units = [u for u in range(M) if np.gcd(u, M) == 1]
    PA, PB = [], []
    for u in units:
        for c in range(M):
            perm = [(u * j + c) % M for j in range(M)]
            PA.append(np.array([d1.get(K1[i, perm].tobytes(), -1)
                                for i in range(N1)], dtype=np.int64))
            PB.append(np.array([d2.get(K2[i, perm].tobytes(), -1)
                                for i in range(N2)], dtype=np.int64))
    PA = np.array(PA)
    PB = np.array(PB)
    print(f"affine maps: {len(PA)}", flush=True)
    # canonical orbit rep per point: min over valid affine images
    BIG = N + 1
    canon = np.full(N, BIG, dtype=np.int64)
    for pa, pb in zip(PA, PB):
        p1 = pa[i1_all]
        p2 = pb[i2_all]
        valid = (p1 >= 0) & (p2 >= 0)
        pidx = np.where(valid, p1 * N2 + p2, BIG)
        np.minimum(canon, pidx, out=canon)
    assert (canon < BIG).all()
    # component canonical reps
    BIG1, BIG2 = N1 + 1, N2 + 1
    can1 = np.full(N1, BIG1, dtype=np.int64)
    can2 = np.full(N2, BIG2, dtype=np.int64)
    for pa, pb in zip(PA, PB):
        np.minimum(can1, np.where(pa >= 0, pa, BIG1), out=can1)
        np.minimum(can2, np.where(pb >= 0, pb, BIG2), out=can2)
    # orbit partition within fibers
    okey = gfib.astype(np.int64) * N + canon
    _, osizes = np.unique(okey, return_counts=True)
    within = int((osizes * (osizes - 1) // 2).sum())
    total = int((gcounts * (gcounts - 1) // 2).sum())
    print(f"within-orbit pairs: {within}, NON-AFFINE pairs: "
          f"{total - within} (target 18000)", flush=True)
    # save intermediates for the analysis stage
    np.savez("/tmp/w37_stage1.npz", gfib=gfib, canon=canon, can1=can1,
             can2=can2, f1id=f1id, f2id=f2id, gcounts=gcounts,
             i1_all=i1_all, i2_all=i2_all)
    # fiber-size distribution of non-affine pairs
    order = np.argsort(okey, kind="stable")
    # per-fiber: orbit sizes
    fib_of_orbit = okey[order][np.searchsorted(
        okey[order], np.unique(okey), side="left")] // N
    # simpler: recompute per fiber via pandas-free loop over fibers
    # (9061 fibers; use np.unique on (gfib, canon) pairs)
    uk, uk_counts = np.unique(
        np.stack([gfib, canon], axis=1), axis=0, return_counts=True)
    # uk rows: (fiber, orbit-rep), counts = orbit size
    from collections import defaultdict
    fib_orbits = defaultdict(list)
    for (f_, _), s_ in zip(uk.tolist(), uk_counts.tolist()):
        fib_orbits[f_].append(s_)
    nonaff_by_fibsize = Counter()
    norbit_dist = Counter()
    min_fib_with_nonaff = None
    for f_, sizes in fib_orbits.items():
        k = sum(sizes)
        cross = k * (k - 1) // 2 - sum(s * (s - 1) // 2 for s in sizes)
        norbit_dist[len(sizes)] += 1
        if cross > 0:
            nonaff_by_fibsize[k] += cross
            if min_fib_with_nonaff is None or k < min_fib_with_nonaff:
                min_fib_with_nonaff = k
    print("non-affine pairs by fiber size:", dict(sorted(
        nonaff_by_fibsize.items())), flush=True)
    print("min fiber size with non-affine pair:", min_fib_with_nonaff,
          flush=True)
    print("fibers by #orbits:", dict(sorted(norbit_dist.items())), flush=True)
    # explicit counterexample check: base pt 841 (1,0), other 3364 (4,0)
    print("canon[841] =", canon[841], "canon[3364] =", canon[3364],
          "same fiber:", gfib[841] == gfib[3364], flush=True)


if __name__ == "__main__":
    main()
