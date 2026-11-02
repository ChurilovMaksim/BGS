"""Wave 38, task 5, part 2: full Fix_30 lift of fibers 151/231 + constant paddings."""
import numpy as np, math
from collections import defaultdict

D30 = 92585104325562912980000
COMPS = [32, 625, 49, 841, 923521, 1681, 72361]
assert math.prod(COMPS) == D30
SLICE = 625 * 841
MOTHER = D30 // SLICE
assert math.prod([32, 49, 923521, 1681, 72361]) == MOTHER

def crt2(a, ma, b, mb):
    inv = pow(ma, -1, mb)
    t = ((b - a) % mb) * inv % mb
    return a + ma * t

def lift_slice_row(r):
    """r: length-30 array mod SLICE -> global row mod D30 with other comps 0."""
    return np.array([crt2(int(v), SLICE, 0, MOTHER) for v in r], dtype=object)

def check_fix(R, m=30):
    """Verify recurrence mod D30 with period m (Python ints)."""
    y = list(R) + [0, 0]
    for j in range(m):
        y[j + 2] = (6 * y[j + 1] - y[j]) % D30
    # need y[m]==y[0], y[m+1]==y[1]; recompute properly:
    seq = list(R)
    for _ in range(2):
        seq.append((6 * seq[-1] - seq[-2]) % D30)
    return seq[m] == R[0] and seq[m + 1] == R[1]

def affine_perms(m):
    perms = []
    for u in range(m):
        if math.gcd(u, m) != 1: continue
        for c in range(m):
            perms.append([(u * j + c) % m for j in range(m)])
    return perms

def orbit_ids(rows, perms):
    """Partition list of rows (tuples) into affine orbits; return orbit index per row."""
    rows = [tuple(r) for r in rows]
    idx = {r: i for i, r in enumerate(rows)}
    seen = {}
    out = []
    for r in rows:
        if r in seen: out.append(seen[r]); continue
        orb = set()
        for p in perms:
            q = tuple(r[p[j]] for j in range(len(r)))
            orb.add(q)
        oid = len(set(out)) if False else None
        # assign new orbit id
        newid = max(out) + 1 if out else 0
        for q in orb:
            if q in idx and q not in seen:
                seen[q] = newid
        out.append(seen[r])
    return out

perms = affine_perms(30)
US = [1, 4, 6, 9, 11, 14, 16, 19, 21, 24]  # units mod 25 with mod-5 in {1,4}

for fid in (151, 231):
    rep = np.load(f"/tmp/wave38_fiber{fid}_rep.npy")
    R = lift_slice_row(rep)
    print(f"--- fiber {fid}: Fix_30 check: {check_fix(R)}")
    # affine orbit of R in full space: apply perms, keep rows with same sorted multiset
    base_sorted = tuple(sorted(R.tolist()))
    orb_rows = set()
    for p in perms:
        q = tuple(R[p[j]] for j in range(30))
        if tuple(sorted(q)) == base_sorted:
            orb_rows.add(q)
    print(f"    affine orbit size in full space: {len(orb_rows)} (slice said 30)")
    # scaling: scale 625-component by u, other comps 0 -> global row; check fiber + orbit
    c625 = rep % 625
    orbit_of = {}
    for u in US:
        scaled625 = (c625 * u) % 625
        # rebuild slice row: CRT(625-comp, 841-comp=0)
        srow = np.array([crt2(int(a), 625, 0, 841) for a in scaled625])
        grow = lift_slice_row(srow)
        assert tuple(sorted(grow.tolist())) == base_sorted, "scaled row left the fiber!"
        # which affine orbit? compare against orb_rows via canonical: is grow in orb_rows?
        in_orbit = tuple(grow.tolist()) in orb_rows
        # orbit id: find rotation class: use sorted-adjacent-pair multiset as in wave37? use
        # membership in orbit sets: compute orbit of grow the same way
        gorb = set()
        for p in perms:
            q = tuple(grow[p[j]] for j in range(30))
            if tuple(sorted(q)) == base_sorted:
                gorb.add(q)
        orbit_of[u] = (len(gorb), in_orbit, len(gorb & orb_rows))
    print("    scaling action (u -> orbit size, in base orbit?, overlap):", orbit_of)
    # transitivity: distinct orbits hit by scaling
    # (orbit identity via a canonical invariant: frozenset of orbit rows)
    seen_orbits = set()
    for u in US:
        scaled625 = (c625 * u) % 625
        srow = np.array([crt2(int(a), 625, 0, 841) for a in scaled625])
        grow = lift_slice_row(srow)
        gorb = frozenset(tuple(grow[p[j]] for j in range(30))
                          for p in perms
                          if tuple(sorted(tuple(grow[p[j]] for j in range(30)))) == base_sorted)
        seen_orbits.add(gorb)
    print(f"    distinct affine orbits reached by U_S scaling: {len(seen_orbits)} (expect 5)")

# constant paddings: 32-component in {8,16,24} (0 = original)
for fid in (151, 231):
    rep = np.load(f"/tmp/wave38_fiber{fid}_rep.npy")
    # need all 150 slice rows of this fiber: recompute quickly from saved? We only saved rep.
    # Instead: verify padding claim on rep + scaling family: padded rep fiber membership is
    # by construction; check Fix_30 and affine orbit size of padded rep.
    for c32 in (8, 16, 24):
        # global row: CRT(slice value, 32-comp c32 constant, rest 0)
        # CRT in two steps: first combine slice with 32, then with rest (MOTHER/32)
        rest = MOTHER // 32
        R = []
        for v in rep:
            x = crt2(int(v), SLICE, c32, 32)
            x = crt2(x, SLICE * 32, 0, rest)
            R.append(x)
        R = np.array(R, dtype=object)
        ok = check_fix(R)
        base_sorted = tuple(sorted(R.tolist()))
        orb = set()
        for p in perms:
            q = tuple(R[p[j]] for j in range(30))
            if tuple(sorted(q)) == base_sorted:
                orb.add(q)
        print(f"fiber {fid} padding c32={c32}: Fix_30={ok}, affine orbit size={len(orb)}")
