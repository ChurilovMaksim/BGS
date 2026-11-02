"""Wave 36, task 3: PAIR test at m=30, constraining pair (625, 841).
Points = ker_625 x ker_841; fibers = groups with equal sorted pair
multiset over 30 positions. For each fiber pair compute Pi_625, Pi_841
(id/swap from even/odd sorted multisets) and report common-pi failures.
Kernels by exact brute force (see verification in session log)."""
import numpy as np

def kernel_brute(m, mod):
    out = []
    for a in range(mod):
        for b in range(mod):
            seq = [a, b]
            for _ in range(m):
                seq.append((6*seq[-1] - seq[-2]) % mod)
            if seq[m] == a and seq[m+1] == b:
                out.append(tuple(seq[:m]))
    return np.array(out, dtype=np.int32)

def row_keys(arr):
    _, ids = np.unique(arr, axis=0, return_inverse=True)
    return ids

def test_pair(m, kA, qA, kB, qB):
    pk = (kA[:, None, :].astype(np.int64) * qB + kB[None, :, :].astype(np.int64)).astype(np.int32)
    pk_sorted = np.sort(pk, axis=2)
    flat = pk_sorted.reshape(-1, m)
    _, inv, counts = np.unique(flat, axis=0, return_inverse=True, return_counts=True)
    order = np.argsort(inv, kind="stable")
    bounds = np.concatenate([[0], np.cumsum(counts)])
    def class_keys(k, q):
        ke = row_keys(np.sort(k[:, 0::2] % q, axis=1))
        ko = row_keys(np.sort(k[:, 1::2] % q, axis=1))
        return ke, ko
    keA, koA = class_keys(kA, qA)
    keB, koB = class_keys(kB, qB)
    nB = len(kB)
    base_list, other_list = [], []
    for fi in range(len(counts)):
        if counts[fi] < 2:
            continue
        idx = order[bounds[fi]:bounds[fi + 1]]
        base_list.append(np.full(len(idx) - 1, idx[0]))
        other_list.append(idx[1:])
    base_idx = np.concatenate(base_list); other_idx = np.concatenate(other_list)
    nb = len(base_idx)
    bA, oA = base_idx // nB, other_idx // nB
    bB, oB = base_idx % nB, other_idx % nB
    idA = (keA[oA] == keA[bA]) & (koA[oA] == koA[bA])
    swA = (keA[oA] == koA[bA]) & (koA[oA] == keA[bA])
    idB = (keB[oB] == keB[bB]) & (koB[oB] == koB[bB])
    swB = (keB[oB] == koB[bB]) & (koB[oB] == keB[bB])
    fail = ((idA & ~swA) & (swB & ~idB)) | ((swA & ~idA) & (idB & ~swB))
    neither = (~(idA | swA)) | (~(idB | swB))
    print(f"pair ({qA},{qB}): points={len(flat)} fibers={len(counts)} "
          f"pairs={nb} PiA id={int(idA.sum())} sw={int(swA.sum())} "
          f"both={int((idA&swA).sum())} neither={int((~(idA|swA)).sum())} | "
          f"PiB id={int(idB.sum())} sw={int(swB.sum())} "
          f"both={int((idB&swB).sum())} neither={int((~(idB|swB)).sum())}")
    print(f"  COMMON-PI FAILURES: {int(fail.sum())}; pairs with empty Pi: {int(neither.sum())}")
    return int(fail.sum())

m = 30
k625 = kernel_brute(m, 625)
k841 = kernel_brute(m, 841)
print("kernels:", len(k625), len(k841))
test_pair(m, k625, 625, k841, 841)
