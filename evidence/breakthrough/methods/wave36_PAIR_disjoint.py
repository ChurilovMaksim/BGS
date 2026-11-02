"""Wave 36, task 3: measure support-disjointness coverage at m=30 (625,841).
For each fiber pair, check whether supp(M_E) cap supp(M_O) is empty at
625 or at 841 (for base or other). The one-sided disjoint-supports
theorem (see note) then covers those pairs unconditionally."""
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

m = 30
kA = kernel_brute(m, 625); kB = kernel_brute(m, 841)
def disjoint_flags(k, q):
    # True if supp(sorted even multiset) cap supp(sorted odd multiset) empty
    se = [set(np.unique(row)) for row in k[:, 0::2]]
    so = [set(np.unique(row)) for row in k[:, 1::2]]
    return np.array([len(a & b) == 0 for a, b in zip(se, so)])
dA = disjoint_flags(kA, 625); dB = disjoint_flags(kB, 841)
print(f"points disjoint at 625: {dA.mean():.3f}; at 841: {dB.mean():.3f}")
pk = (kA[:, None, :].astype(np.int64) * 841 + kB[None, :, :].astype(np.int64)).astype(np.int32)
flat = np.sort(pk, axis=2).reshape(-1, m)
_, inv, counts = np.unique(flat, axis=0, return_inverse=True, return_counts=True)
order = np.argsort(inv, kind="stable")
bounds = np.concatenate([[0], np.cumsum(counts)])
keA, koA = row_keys(np.sort(kA[:, 0::2] % 625, axis=1)), row_keys(np.sort(kA[:, 1::2] % 625, axis=1))
keB, koB = row_keys(np.sort(kB[:, 0::2] % 841, axis=1)), row_keys(np.sort(kB[:, 1::2] % 841, axis=1))
nB = len(kB)
tot = cov = uncov = fails = fails_uncov = 0
for fi in range(len(counts)):
    if counts[fi] < 2:
        continue
    idx = order[bounds[fi]:bounds[fi + 1]]
    for other in idx[1:]:
        base = idx[0]
        bA, oA = base // nB, other // nB
        bB, oB = base % nB, other % nB
        idA = (keA[oA] == keA[bA]) and (koA[oA] == koA[bA])
        swA = (keA[oA] == koA[bA]) and (koA[oA] == keA[bA])
        idB = (keB[oB] == keB[bB]) and (koB[oB] == koB[bB])
        swB = (keB[oB] == koB[bB]) and (koB[oB] == keB[bB])
        fail = (idA and not swA and swB and not idB) or (swA and not idA and idB and not swB)
        covered = dA[bA] or dA[oA] or dB[bB] or dB[oB]
        tot += 1
        if covered: cov += 1
        else: uncov += 1
        if fail: fails += 1; fails_uncov += (0 if covered else 1)
print(f"pairs={tot} covered_by_disjoint_supports={cov} uncovered={uncov} "
      f"failures={fails} failures_among_uncovered={fails_uncov}")
