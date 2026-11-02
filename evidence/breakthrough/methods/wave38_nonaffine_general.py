"""Wave 38, task 5, part 1: m=30 slice reproduction + full Fix_30 lift + paddings."""
import numpy as np
from collections import defaultdict

def kernel_rows(m, q):
    """All kernel rows mod q: rows y_0..y_{m-1} with recurrence y_{j+2}=6y_{j+1}-y_j
    and y_m=y_0, y_{m+1}=y_1. Vectorized over (a,b) in (Z/q)^2."""
    a, b = np.meshgrid(np.arange(q), np.arange(q), indexing="ij")
    a = a.ravel().astype(np.int64); b = b.ravel().astype(np.int64)
    prev, cur = a, b
    seqs = [a, b]
    for _ in range(m - 1):
        nxt = (6 * cur - prev) % q
        seqs.append(nxt); prev, cur = cur, nxt
    # seqs[j] = y_j for j=0..m ; need y_m==a and y_{m+1}==b ; seqs[m]=y_m, need one more
    nxt = (6 * cur - prev) % q
    ok = (seqs[m] == a) & (nxt == b)
    rows = np.stack([s[ok] for s in seqs[:m]], axis=1)
    return rows

def crt_pair(A, qa, B, qb):
    """Combine row sets: A (n1,m) mod qa, B (n2,m) mod qb -> (n1*n2,m) mod qa*qb."""
    inv = pow(int(qa), -1, int(qb))
    # broadcast: (n1,1,m) vs (1,n2,m)
    A3 = A[:, None, :]; B3 = B[None, :, :]
    t = (((B3 - A3) % qb) * inv) % qb
    pts = A3 + qa * t
    return pts.reshape(-1, A.shape[1])

def fibers_of(pts):
    srt = np.sort(pts, axis=1)
    _, inv, counts = np.unique(srt, axis=0, return_inverse=True, return_counts=True)
    return inv, counts

def affine_perms(m):
    import math
    perms = []
    for u in range(m):
        if math.gcd(u, m) != 1: continue
        for c in range(m):
            perms.append([(u * j + c) % m for j in range(m)])
    return np.array(perms, dtype=np.int64)

def orbit_partition(fiber_rows, perms):
    """Partition fiber_rows (array) into affine orbits. Returns list of orbit sizes."""
    remaining = set(map(bytes, fiber_rows))
    orbits = []
    while remaining:
        base = np.frombuffer(next(iter(remaining)), dtype=np.int64)
        orb = set(map(bytes, base[perms]))
        in_fiber = orb & remaining
        orbits.append(len(in_fiber))
        remaining -= in_fiber
    return orbits

m = 30
K625 = kernel_rows(m, 625)
K841 = kernel_rows(m, 841)
print("ker625:", len(K625), "ker841:", len(K841))
pts = crt_pair(K625, 625, K841, 841)
print("slice points:", pts.shape)
inv, counts = fibers_of(pts)
print("num fibers:", len(counts), "max size:", counts.max())
big = np.where(counts == 150)[0]
print("size-150 fibers:", len(big))
perms = affine_perms(m)
print("affine maps:", len(perms))
for fid in big:
    rows = pts[inv == fid]
    # 841-component and 625-component of members
    c841 = rows % 841
    c625 = rows % 625
    print(f"fiber id {fid}: size {len(rows)}, 841 all zero: {bool((c841==0).all())}, "
          f"625 all div by 25: {bool((c625 % 25 == 0).all())}")
    vals = np.unique((c625 // 25) % 25)
    red5 = sorted(set((vals % 5).tolist()))
    print("   (625/25) value set size:", len(vals), "mod-5 reductions:", red5)
    orbs = orbit_partition(rows, perms)
    print("   affine orbit sizes:", orbs, "cross-orbit pairs:",
          (len(rows)**2 - sum(o*o for o in orbs)) // 2)
    # save a rep row for part 2
    np.save(f"/tmp/wave38_fiber{fid}_rep.npy", rows[0])
