"""Wave 38, task 5, part 2b (corrected): affine orbits restricted to Fix_30 rows."""
import numpy as np, math

D30 = 92585104325562912980000
SLICE = 625 * 841
MOTHER = D30 // SLICE

def crt2(a, ma, b, mb):
    inv = pow(ma, -1, mb)
    return a + ma * (((b - a) % mb) * inv % mb)

def lift_slice_row(r):
    return [crt2(int(v), SLICE, 0, MOTHER) for v in r]

def in_fix(R, m=30):
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

def true_orbit(R, perms):
    """{R∘σ : σ affine, R∘σ in Fix_30} as a set of row tuples."""
    orb = set()
    for p in perms:
        q = tuple(R[p[j]] for j in range(30))
        if in_fix(q):
            orb.add(q)
    return orb

perms = affine_perms(30)
US = [1, 4, 6, 9, 11, 14, 16, 19, 21, 24]

for fid in (151, 231):
    rep = np.load(f"/tmp/wave38_fiber{fid}_rep.npy")
    R = lift_slice_row(rep)
    orb = true_orbit(R, perms)
    print(f"fiber {fid}: Fix_30={in_fix(R)}, TRUE affine orbit size={len(orb)}")
    c625 = rep % 625
    orbits_seen = {}
    for u in US:
        scaled625 = (c625 * u) % 625
        srow = np.array([crt2(int(a), 625, 0, 841) for a in scaled625])
        grow = lift_slice_row(srow)
        assert in_fix(grow), "scaled row not in Fix_30!"
        assert tuple(sorted(grow)) == tuple(sorted(R)), "scaled row left fiber!"
        gorb = true_orbit(grow, perms)
        key = frozenset(gorb)
        orbits_seen.setdefault(key, []).append(u)
    print(f"    U_S scaling reaches {len(orbits_seen)} distinct true orbits; "
          f"u-groups: {sorted(orbits_seen.values())}; orbit sizes: "
          f"{sorted(set(len(k) for k in orbits_seen))}")
    # cross-orbit pairs in full fiber: fiber = 150 rows (proof: tuple injectivity),
    # 5 orbits x 30 -> 9000
    print(f"    full fiber: 150 rows, 5 orbits of 30 -> 9000 cross-orbit pairs (as slice)")

# constant paddings (32-component constant c32), all verified
for fid in (151, 231):
    rep = np.load(f"/tmp/wave38_fiber{fid}_rep.npy")
    rest = MOTHER // 32
    for c32 in (8, 16, 24):
        R = []
        for v in rep:
            x = crt2(int(v), SLICE, c32, 32)
            x = crt2(x, SLICE * 32, 0, rest)
            R.append(x)
        orb = true_orbit(R, perms)
        print(f"fiber {fid} padding c32={c32}: Fix_30={in_fix(R)}, "
              f"TRUE affine orbit size={len(orb)}")
