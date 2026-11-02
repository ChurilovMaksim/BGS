"""Wave 36, task 5, fix-up: recompute test (a) with the corrected
signature encoding (unified ids range over [0, 2N), so the base
must be 2N, not N), and directly verify the two headline examples:
- m=30 (b) example pair (base pt 841, other pt 3364) has NO
  exactly-affine matching (all 240 affine maps tested directly);
- m=18 and m=30 (c) explicit non-class-affine sigmas are genuine
  matchings and are not class-affine.
Slice construction imported from wave36_sigma_structure.py, so the
point indexing is identical to the main run.
"""
import numpy as np
from wave36_sigma_structure import kernel_mod_np, kernel_mod_38809


def compute_a(m, K1, MOD2, K2, label):
    n1, n2 = len(K1), len(K2)
    N = n1 * n2
    P = (K1[:, None, :].astype(np.int64) * MOD2 +
         K2[None, :, :].astype(np.int64)).astype(np.int32)
    flat = P.reshape(N, m)
    srt = np.sort(flat, axis=1)
    _, inv, counts = np.unique(srt, axis=0, return_inverse=True,
                               return_counts=True)
    order = np.argsort(inv, kind="stable")
    bounds = np.concatenate([[0], np.cumsum(counts)])
    nfib = len(counts)
    ev = np.sort(flat[:, 0::2], axis=1)
    od = np.sort(flat[:, 1::2], axis=1)
    evod = np.concatenate([ev, od], axis=0)
    _, uids = np.unique(evod, axis=0, return_inverse=True)
    ev_id, od_id = uids[:N], uids[N:]
    B = 2 * N  # ids are in [0, 2N): base must exceed max id
    sig = ev_id.astype(np.int64) * B + od_id.astype(np.int64)
    fib_of_pt = np.empty(N, dtype=np.int64)
    for fi in range(nfib):
        fib_of_pt[order[bounds[fi]:bounds[fi + 1]]] = fi
    comp = fib_of_pt.astype(np.int64) * (B * B) + sig
    sidx = np.argsort(comp, kind="stable")
    scomp = comp[sidx]
    uniq_c, first = np.unique(scomp, return_index=True)
    cnts = np.diff(np.append(first, len(scomp)))
    gsig = uniq_c % (B * B)
    gfib = uniq_c // (B * B)
    d = {}
    for f_, s_, c_ in zip(gfib.tolist(), gsig.tolist(), cnts.tolist()):
        d[(f_, s_)] = c_
    pairs_with = 0
    for (f_, s_), c_ in d.items():
        e_, o_ = divmod(s_, B)
        s2 = o_ * B + e_
        if s2 == s_:
            pairs_with += c_ * (c_ - 1) // 2
        elif s2 > s_:
            pairs_with += c_ * d.get((f_, s2), 0)
    total_pairs = int((counts * (counts - 1) // 2).sum())
    # base-vs-other (a) failures (cross-check vs test (c))
    bo_fail = 0
    for fi in range(nfib):
        if counts[fi] < 2:
            continue
        idx = order[bounds[fi]:bounds[fi + 1]]
        b = idx[0]
        for o in idx[1:]:
            ok = ((ev_id[o] == ev_id[b] and od_id[o] == od_id[b]) or
                  (ev_id[o] == od_id[b] and od_id[o] == ev_id[b]))
            if not ok:
                bo_fail += 1
    print(f"== {label}: all pairs {total_pairs}, with class-affine "
          f"{pairs_with}, WITHOUT {total_pairs - pairs_with}; "
          f"base-vs-other (a) failures: {bo_fail}", flush=True)
    return flat


def main():
    m = 18
    k25 = kernel_mod_np(m, 25)
    k38809 = kernel_mod_38809(m)
    f18 = compute_a(m, k25, 38809, k38809, "m=18 slice (fixed)")
    # verify m=18 (c) example sigma directly
    sigma18 = [3, 5, 4, 0, 2, 1, 6, 11, 10, 9, 8, 7, 12, 17, 16, 15,
               14, 13]
    b18 = f18[38809]
    o18 = f18[155236]
    assert sorted(sigma18) == list(range(18))
    assert all(o18[i] == b18[sigma18[i]] for i in range(18)), \
        "m=18 sigma is not a matching"
    ev_imgs = {sigma18[i] & 1 for i in range(18) if i % 2 == 0}
    od_imgs = {sigma18[i] & 1 for i in range(18) if i % 2 == 1}
    assert len(ev_imgs) == 2 or len(od_imgs) == 2, \
        "m=18 sigma is class-affine after all"
    print("   m=18 (c) sigma verified: matching, not class-affine",
          flush=True)
    m = 30
    k625 = kernel_mod_np(m, 625)
    k841 = kernel_mod_np(m, 841)
    f30 = compute_a(m, k625, 841, k841, "m=30 slice (fixed)")
    # verify m=30 (b) example pair has NO affine matching, directly
    b30 = f30[841]
    o30 = f30[3364]
    units = [u for u in range(30) if np.gcd(u, 30) == 1]
    found = []
    for u in units:
        for c in range(30):
            perm = [(u * j + c) % 30 for j in range(30)]
            if (o30 == b30[perm]).all():
                found.append((u, c))
    assert not found, f"m=30 pair HAS affine matching {found}"
    print("   m=30 (b) example pair verified: no affine map works "
          f"(240 tested)", flush=True)
    # verify m=30 (c) example sigma directly
    sigma30 = [3, 5, 4, 0, 2, 1, 6, 11, 10, 9, 8, 7, 12, 17, 16, 15,
               14, 13, 18, 23, 22, 21, 20, 19, 24, 29, 28, 27, 26, 25]
    b30c = f30[4205]
    o30c = f30[16820]
    assert sorted(sigma30) == list(range(30))
    assert all(o30c[i] == b30c[sigma30[i]] for i in range(30)), \
        "m=30 sigma is not a matching"
    ev_imgs = {sigma30[i] & 1 for i in range(30) if i % 2 == 0}
    od_imgs = {sigma30[i] & 1 for i in range(30) if i % 2 == 1}
    assert len(ev_imgs) == 2 or len(od_imgs) == 2
    print("   m=30 (c) sigma verified: matching, not class-affine",
          flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
