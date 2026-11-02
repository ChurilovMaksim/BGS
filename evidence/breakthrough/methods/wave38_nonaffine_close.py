"""Wave 38, task 5, part 6: mechanism at m=48 + remaining 2-part slices at m=6,18."""
import numpy as np, math
from collections import defaultdict

def kernel_rows(m, q):
    a, b = np.meshgrid(np.arange(q), np.arange(q), indexing="ij")
    a = a.ravel().astype(np.int64); b = b.ravel().astype(np.int64)
    prev, cur = a, b
    seqs = [a, b]
    for _ in range(m - 1):
        nxt = (6 * cur - prev) % q
        seqs.append(nxt); prev, cur = cur, nxt
    nxt = (6 * cur - prev) % q
    ok = (seqs[m] == a) & (nxt == b)
    return np.stack([s[ok] for s in seqs[:m]], axis=1)

def crt_pair(A, qa, B, qb):
    inv = pow(int(qa), -1, int(qb))
    A3 = A[:, None, :]; B3 = B[None, :, :]
    t = (((B3 - A3) % qb) * inv) % qb
    return (A3 + qa * t).reshape(-1, A.shape[1])

def affine_perms(m):
    perms = []
    for u in range(m):
        if math.gcd(u, m) != 1: continue
        for c in range(m):
            perms.append([(u * j + c) % m for j in range(m)])
    return np.array(perms, dtype=np.int64)

def orbit_partition(rows, perms):
    members = set(map(bytes, rows))
    remaining = set(members); orbits = []
    while remaining:
        base = np.frombuffer(next(iter(remaining)), dtype=np.int64)
        orb = set(map(bytes, base[perms])) & remaining
        orbits.append(orb); remaining -= orb
    return orbits

def analyze_slice(m, q1, q2, mech=False):
    K1 = kernel_rows(m, q1); K2 = kernel_rows(m, q2)
    pts = crt_pair(K1, q1, K2, q2)
    srt = np.sort(pts, axis=1)
    _, inv, counts = np.unique(srt, axis=0, return_inverse=True, return_counts=True)
    perms = affine_perms(m)
    multi = []
    best = None
    for fid in range(len(counts)):
        rows = pts[inv == fid]
        orbs = orbit_partition(rows, perms)
        if len(orbs) > 1:
            multi.append((int(counts[fid]), [len(o) for o in orbs]))
            if best is None or len(rows) > len(best[0]):
                best = (rows, orbs)
    print(f"m={m} ker({q1})xker({q2}): pts={len(pts)} fibers={len(counts)} "
          f"maxsize={counts.max()} multi={len(multi)}")
    for size, orbs in sorted(multi, reverse=True)[:3]:
        print(f"    size {size} orbits {orbs}")
    if mech and best is not None:
        rows, orbs = best
        row2orb = {}
        for i, o in enumerate(orbs):
            for r in o: row2orb[r] = i
        base = np.frombuffer(next(iter(orbs[0])), dtype=np.int64)
        for ci, q, other in ((1, q1, q2), (2, q2, q1)):
            reached = defaultdict(set)
            for u in range(1, q):
                if math.gcd(u, q) != 1: continue
                if ci == 1:
                    new = (base % q1) * u % q1
                    iv = pow(q1, -1, q2)
                    t = (((base % q2) - new) % q2) * iv % q2
                    srow = new + q1 * t
                else:
                    new = (base % q2) * u % q2
                    iv = pow(q2, -1, q1)
                    t = (((base % q1) - new) % q1) * iv % q1
                    srow = new + q2 * t
                if tuple(sorted(srow.tolist())) != tuple(sorted(base.tolist())): continue
                if srow.tobytes() in row2orb:
                    reached[row2orb[srow.tobytes()]].add(u)
            print(f"    mechanism: scaling q={q}: orbits reached "
                  f"{ {k: len(v) for k, v in sorted(reached.items())} } of {len(orbs)}")

analyze_slice(48, 2048, 81, mech=True)
analyze_slice(18, 32, 49)
analyze_slice(18, 32, 38809)
analyze_slice(6, 32, 49)
