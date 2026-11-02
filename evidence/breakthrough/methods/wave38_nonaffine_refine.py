"""Wave 38, task 5, part 5: full unit group at m=30 + 2-part slices at m=6,18,48."""
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

def analyze_slice(m, q1, q2):
    K1 = kernel_rows(m, q1); K2 = kernel_rows(m, q2)
    pts = crt_pair(K1, q1, K2, q2)
    srt = np.sort(pts, axis=1)
    _, inv, counts = np.unique(srt, axis=0, return_inverse=True, return_counts=True)
    perms = affine_perms(m)
    multi = []
    for fid in range(len(counts)):
        rows = pts[inv == fid]
        orbs = orbit_partition(rows, perms)
        if len(orbs) > 1:
            multi.append((int(counts[fid]), [len(o) for o in orbs]))
    print(f"m={m} ker({q1})xker({q2}): pts={len(pts)} fibers={len(counts)} "
          f"maxsize={counts.max()} multi={len(multi)}")
    for size, orbs in sorted(multi, reverse=True)[:5]:
        print(f"    size {size} orbits {orbs}")

# m=30 full unit group on fiber 151
m = 30
K625 = kernel_rows(m, 625); K841 = kernel_rows(m, 841)
pts = crt_pair(K625, 625, K841, 841)
srt = np.sort(pts, axis=1)
_, inv, counts = np.unique(srt, axis=0, return_inverse=True, return_counts=True)
perms = affine_perms(m)
rows = pts[inv == 151]
orbs = orbit_partition(rows, perms)
row2orb = {}
for i, o in enumerate(orbs):
    for r in o: row2orb[r] = i
base = np.frombuffer(next(iter(orbs[0])), dtype=np.int64)
reached = defaultdict(set)
for u in range(1, 625):
    if math.gcd(u, 625) != 1: continue
    new = (base % 625) * u % 625
    inv12 = pow(625, -1, 841)
    t = (((base % 841) - new) % 841) * inv12 % 841
    srow = new + 625 * t
    if tuple(sorted(srow.tolist())) != tuple(sorted(base.tolist())): continue
    if srow.tobytes() in row2orb:
        reached[row2orb[srow.tobytes()]].add(u)
print(f"m=30 fiber 151: full 625-unit scaling: orbits reached "
      f"{ {k: len(v) for k, v in sorted(reached.items())} }; "
      f"total fiber-preserving units={sum(len(v) for v in reached.values())} of 500")
# which residues mod 5 do the preserving units have?
allu = set().union(*reached.values())
print(f"    preserving units mod 5: {sorted(set(u % 5 for u in allu))}; "
      f"mod 25 classes: {sorted(set(u % 25 for u in allu))[:10]}... "
      f"count mod-25 classes: {len(set(u % 25 for u in allu))}")

analyze_slice(6, 32, 25)
analyze_slice(18, 32, 25)
analyze_slice(48, 2048, 81)
