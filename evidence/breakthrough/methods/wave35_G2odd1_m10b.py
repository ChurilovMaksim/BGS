"""Wave 35, task 5: m=10 a=b subcase, fully vectorized.

For each constant mod-32 component a in {0,8,16,24}: enumerate
K_841 x K_1681 (1,413,721 points), group by sorted multiset, and for
each fiber pair compute, vectorized:
  - Pi_841, Pi_1681, common pi,
  - dihedral relation (other in D_10-orbit of base),
  - odd-part unordered splitting: {M_E, M_O} mod D_odd=1413721 for base
    vs other: 'straight', 'swapped', or 'neither'.
"""
import numpy as np
from collections import Counter


def kernel_mod_np(m, mod):
    a, b = np.meshgrid(np.arange(mod, dtype=np.int64),
                       np.arange(mod, dtype=np.int64), indexing="ij")
    a = a.ravel()
    b = b.ravel()
    seqs = [a, b]
    for _ in range(m):
        seqs.append((6 * seqs[-1] - seqs[-2]) % mod)
    ok = (seqs[m] == a) & (seqs[m + 1] == b)
    return np.stack([s[ok] for s in seqs[:m]], axis=1).astype(np.int32)


def crt_combine_np(A, mod_a, B, mod_b):
    A = A.astype(np.int64)
    B = B.astype(np.int64)
    inv = pow(int(mod_a), -1, int(mod_b))
    diff = (B[None, :, :] - A[:, None, :]) % mod_b
    t = (diff * inv) % mod_b
    out = (A[:, None, :] + mod_a * t).reshape(-1, A.shape[1])
    return out.astype(np.int32)


def row_keys(arr):
    """Map each row of a 2D int array to a unique integer id."""
    _, ids = np.unique(arr, axis=0, return_inverse=True)
    return ids


def main():
    m = 10
    Dodd = 841 * 1681
    k841 = kernel_mod_np(m, 841)
    k1681 = kernel_mod_np(m, 1681)
    print("kernels ok", len(k841), len(k1681), flush=True)

    tot = Counter()
    pat = Counter()
    split_pat = Counter()
    nondih_nonsplit = []
    for a in (0, 8, 16, 24):
        const = np.full((1, m), a, dtype=np.int32)
        pts = crt_combine_np(const, 32, k841, 841)
        pts = crt_combine_np(pts, 32 * 841, k1681, 1681)
        srt = np.sort(pts, axis=1)
        _, inv, counts = np.unique(srt, axis=0, return_inverse=True,
                                   return_counts=True)
        order = np.argsort(inv, kind="stable")
        bounds = np.concatenate([[0], np.cumsum(counts)])
        # pair arrays (base, other)
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
        print(f"a={a}: pairs {nb}", flush=True)
        tot['pairs'] += nb
        B = pts[base_idx]
        O = pts[other_idx]
        # per-q class keys
        pi = {}
        for q in (841, 1681):
            kE = row_keys(np.sort(B[:, 0::2] % q, axis=1))
            kO = row_keys(np.sort(B[:, 1::2] % q, axis=1))
            # keys must be comparable across B and O: recompute jointly
            jE = row_keys(np.sort(
                np.concatenate([B[:, 0::2], O[:, 0::2]], axis=0) % q, axis=1))
            jO = row_keys(np.sort(
                np.concatenate([B[:, 1::2], O[:, 1::2]], axis=0) % q, axis=1))
            bE, oE = jE[:nb], jE[nb:]
            bO, oO = jO[:nb], jO[nb:]
            is_id = (oE == bE) & (oO == bO)
            is_swap = (oE == bO) & (oO == bE)
            pi[q] = (is_id, is_swap)
        common = ((pi[841][0] | pi[841][1]) & (pi[1681][0] | pi[1681][1]))
        # common pi exists iff not (841 forces id-only and 1681 swap-only
        # or vice versa); compute directly:
        id841_only = pi[841][0] & ~pi[841][1]
        sw841_only = pi[841][1] & ~pi[841][0]
        id1681_only = pi[1681][0] & ~pi[1681][1]
        sw1681_only = pi[1681][1] & ~pi[1681][0]
        common_pi = ~((id841_only & sw1681_only) |
                      (sw841_only & id1681_only))
        tot['common_pi_fail'] += int((~common_pi).sum())
        # dihedral relation, vectorized over 20 maps
        dih = np.zeros(nb, dtype=bool)
        for eps in (1, -1):
            for k in range(m):
                perm = [(eps * i + k) % m for i in range(m)]
                dih |= (B[:, perm] == O).all(axis=1)
        tot['dihedral'] += int(dih.sum())
        # odd-part unordered splitting mod Dodd
        jE = row_keys(np.sort(
            np.concatenate([B[:, 0::2], O[:, 0::2]], axis=0) % Dodd, axis=1))
        jO = row_keys(np.sort(
            np.concatenate([B[:, 1::2], O[:, 1::2]], axis=0) % Dodd, axis=1))
        bE, oE = jE[:nb], jE[nb:]
        bO, oO = jO[:nb], jO[nb:]
        straight = (oE == bE) & (oO == bO)
        swapped = (oE == bO) & (oO == bE)
        neither = ~(straight | swapped)
        split_pat['straight'] += int(straight.sum())
        split_pat['swapped'] += int(swapped.sum())
        split_pat['neither'] += int(neither.sum())
        # pi patterns
        for name, arr in (('id841', pi[841][0]), ('sw841', pi[841][1]),
                          ('id1681', pi[1681][0]), ('sw1681', pi[1681][1])):
            tot[name] += int(arr.sum())
        # record non-dihedral + neither examples
        bad = np.where(neither & ~dih)[0]
        for j in bad[:5]:
            nondih_nonsplit.append((a, B[j].tolist(), O[j].tolist()))
        print(f"  a={a}: common_pi_fail={int((~common_pi).sum())} "
              f"dihedral={int(dih.sum())} straight={int(straight.sum())} "
              f"swapped={int(swapped.sum())} neither={int(neither.sum())}",
              flush=True)
    print("TOTAL:", dict(tot))
    print("splitting:", dict(split_pat))
    for e in nondih_nonsplit[:5]:
        print("NONDIH+NEITHER example:", e)


if __name__ == "__main__":
    main()
