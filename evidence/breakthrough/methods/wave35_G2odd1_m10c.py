"""Wave 35, task 5: m=10 a=b subcase, a=0 only, optimized.

The four constant mod-32 components give identical fiber combinatorics
(the mod-32 part is constant, so fibers are determined by odd parts
alone); a=0 suffices. Keys are computed once per point set.
"""
import numpy as np
from collections import Counter
import sys
sys.path.insert(0, '.')
from wave35_G2odd1_m10b import kernel_mod_np, crt_combine_np, row_keys


def main():
    m = 10
    Dodd = 841 * 1681
    k841 = kernel_mod_np(m, 841)
    k1681 = kernel_mod_np(m, 1681)
    const = np.zeros((1, m), dtype=np.int32)
    pts = crt_combine_np(const, 32, k841, 841)
    pts = crt_combine_np(pts, 32 * 841, k1681, 1681)
    print("points:", len(pts), flush=True)
    srt = np.sort(pts, axis=1)
    _, inv, counts = np.unique(srt, axis=0, return_inverse=True,
                               return_counts=True)
    order = np.argsort(inv, kind="stable")
    bounds = np.concatenate([[0], np.cumsum(counts)])
    base_list, other_list = [], []
    for fi in range(len(counts)):
        if counts[fi] < 2:
            continue
        idx = order[bounds[fi]:bounds[fi + 1]]
        base_list.append(np.full(len(idx) - 1, idx[0]))
        other_list.append(idx[1:])
    base_idx = np.concatenate(base_list)
    other_idx = np.concatenate(other_list)
    nb = len(base_idx)
    print("pairs:", nb, flush=True)
    # keys once per point set
    keys = {}
    for q in (841, 1681, Dodd):
        keys[(q, 'E')] = row_keys(np.sort(pts[:, 0::2] % q, axis=1))
        keys[(q, 'O')] = row_keys(np.sort(pts[:, 1::2] % q, axis=1))
    print("keys done", flush=True)
    for q in (841, 1681):
        bE, oE = keys[(q, 'E')][base_idx], keys[(q, 'E')][other_idx]
        bO, oO = keys[(q, 'O')][base_idx], keys[(q, 'O')][other_idx]
        is_id = (oE == bE) & (oO == bO)
        is_sw = (oE == bO) & (oO == bE)
        print(f"q={q}: id={int(is_id.sum())} swap={int(is_sw.sum())} "
              f"both={int((is_id & is_sw).sum())} "
              f"neither={int((~(is_id | is_sw)).sum())}", flush=True)
        if q == 841:
            id841, sw841 = is_id, is_sw
        else:
            id1681, sw1681 = is_id, is_sw
    common_fail = ((id841 & ~sw841) & (sw1681 & ~id1681)) | \
                  ((sw841 & ~id841) & (id1681 & ~sw1681))
    print("common-pi failures:", int(common_fail.sum()), flush=True)
    # dihedral, vectorized
    B, O = pts[base_idx], pts[other_idx]
    dih = np.zeros(nb, dtype=bool)
    for eps in (1, -1):
        for k in range(m):
            perm = [(eps * i + k) % m for i in range(m)]
            dih |= (B[:, perm] == O).all(axis=1)
    print("dihedral:", int(dih.sum()), "of", nb, flush=True)
    # odd-part splitting
    bE, oE = keys[(Dodd, 'E')][base_idx], keys[(Dodd, 'E')][other_idx]
    bO, oO = keys[(Dodd, 'O')][base_idx], keys[(Dodd, 'O')][other_idx]
    straight = (oE == bE) & (oO == bO)
    swapped = (oE == bO) & (oO == bE)
    neither = ~(straight | swapped)
    print(f"splitting: straight={int(straight.sum())} "
          f"swapped={int(swapped.sum())} neither={int(neither.sum())}",
          flush=True)
    bad = np.where(neither)[0][:5]
    for j in bad:
        print("NEITHER example: base=", B[j].tolist(),
              "other=", O[j].tolist(), flush=True)
    bad2 = np.where(neither & ~dih)[0][:5]
    for j in bad2:
        print("NEITHER+NONDIH example: base=", B[j].tolist(),
              "other=", O[j].tolist(), flush=True)
    # cross-tab: splitting vs dihedral
    print("dihedral & straight:", int((dih & straight).sum()),
          "dihedral & swapped:", int((dih & swapped).sum()),
          "nondih & straight:", int(((~dih) & straight).sum()),
          "nondih & swapped:", int(((~dih) & swapped).sum()),
          "nondih & neither:", int(((~dih) & neither).sum()), flush=True)


if __name__ == "__main__":
    main()
