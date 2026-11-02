"""Wave 38, task 5, part 4: mechanism of multi-orbit fibers at other m.
For one large multi-orbit fiber per slice: does unit scaling of a component
move between orbits, and is it transitive? Also component multisets per orbit."""
import numpy as np, math

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

def units(q):
    return [u for u in range(1, q) if math.gcd(u, q) == 1]

def investigate(m, q1, q2):
    K1 = kernel_rows(m, q1); K2 = kernel_rows(m, q2)
    pts = crt_pair(K1, q1, K2, q2)
    srt = np.sort(pts, axis=1)
    _, inv, counts = np.unique(srt, axis=0, return_inverse=True, return_counts=True)
    perms = affine_perms(m)
    # largest multi-orbit fiber
    best = None
    for fid in range(len(counts)):
        rows = pts[inv == fid]
        if len(rows) < 2: continue
        orbs = orbit_partition(rows, perms)
        if len(orbs) > 1 and (best is None or len(rows) > len(best[0])):
            best = (rows, orbs)
    rows, orbs = best
    print(f"=== m={m} ker({q1})xker({q2}): fiber size {len(rows)}, orbits {[len(o) for o in orbs]}")
    # orbit id per row
    row2orb = {}
    for i, o in enumerate(orbs):
        for r in o: row2orb[r] = i
    # component multisets per orbit: are they identical across orbits?
    for ci, q in ((0, q1), (1, q2)):
        pass
    # component multisets: for orbit 0 vs orbit 1, compare multiset of component rows
    for i, o in enumerate(orbs[:3]):
        comp1 = sorted(tuple(np.frombuffer(r, dtype=np.int64) % q1) for r in o)
        comp2 = sorted(tuple(np.frombuffer(r, dtype=np.int64) % q2) for r in o)
        print(f"    orbit {i}: distinct {q1}-comp rows: {len(set(comp1))}, "
              f"distinct {q2}-comp rows: {len(set(comp2))}")
    # scaling tests: base row from orbit 0
    base = np.frombuffer(next(iter(orbs[0])), dtype=np.int64)
    for ci, q in ((1, q1), (2, q2)):
        other = q2 if ci == 1 else q1
        reached = defaultdict(set)
        for u in units(q):
            if ci == 1:
                new = (base % q1) * u % q1
                # recombine: CRT(new, q1, base%q2, q2)
                inv12 = pow(q1, -1, q2)
                t = (((base % q2) - new) % q2) * inv12 % q2
                srow = new + q1 * t
            else:
                new = (base % q2) * u % q2
                inv21 = pow(q2, -1, q1)
                t = (((base % q1) - new) % q1) * inv21 % q1
                srow = new + q2 * t
            # in fiber? sorted multiset equal to base's
            if tuple(sorted(srow.tolist())) != tuple(sorted(base.tolist())):
                continue
            key = srow.tobytes()
            if key in row2orb:
                reached[row2orb[key]].add(u)
        print(f"    scaling comp q={q}: orbits reached: "
              f"{ {k: len(v) for k, v in sorted(reached.items())} } "
              f"(total orbits {len(orbs)})")

from collections import defaultdict
investigate(12, 128, 81)
investigate(36, 128, 729)
investigate(60, 625, 81)
investigate(42, 2401, 25)
