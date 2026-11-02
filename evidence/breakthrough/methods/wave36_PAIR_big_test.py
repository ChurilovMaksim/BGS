"""Wave 36, task 3: PAIR test at m=30 for large constraining pairs.
Chunked hashing: points processed in blocks over ker_A; per point a
64-bit FNV-style hash of its sorted pair multiset is stored; groups
with equal hash are then verified exactly (recomputed sorted keys)
before Pi computation. Kernels: brute force (625, 841); param
B = 269*C for 72361 (verified: alpha^30 = 1 + 269*265*sqrt2 mod 269^2)."""
import numpy as np, sys

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

def alpha_powers(m, mod):
    X = [1 % mod, 3 % mod]; Y = [0, 2 % mod]
    for _ in range(2, m):
        x0, y0 = X[-1], Y[-1]
        X.append((3*x0 + 4*y0) % mod); Y.append((2*x0 + 3*y0) % mod)
    return np.array(X[:m], dtype=np.int64), np.array(Y[:m], dtype=np.int64)

def kernel_72361(m):
    p, q = 269, 269*269
    Xq, Yq = alpha_powers(m, q)
    x, y = np.meshgrid(np.arange(p, dtype=np.int64), np.arange(p, dtype=np.int64), indexing="ij")
    x = x.ravel(); y = y.ravel()
    seqs = (2*(x[:, None]*(Xq % p)[None, :] + 2*y[:, None]*(Yq % p)[None, :])) % p
    return (seqs * p).astype(np.int32)

def row_keys(arr):
    _, ids = np.unique(arr, axis=0, return_inverse=True)
    return ids

def test_pair_chunked(m, kA, qA, kB, qB, chunk=25):
    nA, nB = len(kA), len(kB)
    total = nA * nB
    hashes = np.empty(total, dtype=np.uint64)
    FNV = np.uint64(0x100000001b3); OFF = np.uint64(0xcbf29ce484222325)
    pos = 0
    for s in range(0, nA, chunk):
        kAc = kA[s:s+chunk]
        pk = (kAc[:, None, :].astype(np.int64) * qB + kB[None, :, :].astype(np.int64)).astype(np.int32)
        pk_sorted = np.sort(pk, axis=2)
        flat = pk_sorted.reshape(-1, m).astype(np.uint64)
        h = np.full(flat.shape[0], OFF, dtype=np.uint64)
        for j in range(m):
            h = (h ^ flat[:, j]) * FNV
        hashes[pos:pos+len(h)] = h
        pos += len(h)
        print(f"  hashed {pos}/{total}", flush=True)
    order = np.argsort(hashes, kind="stable")
    hs = hashes[order]
    # group boundaries on equal hash
    eq = np.flatnonzero(np.diff(hs)) + 1
    bounds = np.concatenate([[0], eq, [len(hs)]])
    def class_keys(k, q):
        ke = row_keys(np.sort(k[:, 0::2] % q, axis=1))
        ko = row_keys(np.sort(k[:, 1::2] % q, axis=1))
        return ke, ko
    keA, koA = class_keys(kA, qA)
    keB, koB = class_keys(kB, qB)
    def pair_key(pid):
        ia, ib = pid // nB, pid % nB
        pairs = sorted(int(kA[ia, i]) * qB + int(kB[ib, i]) for i in range(m))
        return tuple(pairs)
    fails = 0; pairs = 0; verified_groups = 0; hash_only_groups = 0
    for gi in range(len(bounds) - 1):
        grp = order[bounds[gi]:bounds[gi+1]]
        if len(grp) < 2:
            continue
        # exact verification by recomputed keys
        by_key = {}
        for pid in grp:
            by_key.setdefault(pair_key(int(pid)), []).append(int(pid))
        for key, members in by_key.items():
            if len(members) < 2:
                continue
            verified_groups += 1
            base = members[0]
            for other in members[1:]:
                pairs += 1
                bA, oA = base // nB, other // nB
                bB, oB = base % nB, other % nB
                idA = (keA[oA] == keA[bA]) and (koA[oA] == koA[bA])
                swA = (keA[oA] == koA[bA]) and (koA[oA] == keA[bA])
                idB = (keB[oB] == keB[bB]) and (koB[oB] == koB[bB])
                swB = (keB[oB] == koB[bB]) and (koB[oB] == keB[bB])
                if (idA and not swA and swB and not idB) or (swA and not idA and idB and not swB):
                    fails += 1
                    print("  FAIL pair:", base, other)
    print(f"pair ({qA},{qB}): points={total} verified_fiber_groups={verified_groups} "
          f"pairs={pairs} COMMON-PI FAILURES: {fails}", flush=True)
    return fails

m = 30
which = sys.argv[1]
if which == "625-72361":
    kA = kernel_brute(m, 625); kB = kernel_72361(m)
    test_pair_chunked(m, kA, 625, kB, 72361)
elif which == "841-72361":
    kA = kernel_brute(m, 841); kB = kernel_72361(m)
    test_pair_chunked(m, kA, 841, kB, 72361)
