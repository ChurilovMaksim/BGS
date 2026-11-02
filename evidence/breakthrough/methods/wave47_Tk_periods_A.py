"""Wave 47, task 10, script A: fibers of period-dividing-4 points, mod 32.

Reduction (proved in the note): at any level j >= 5, a period-dividing-4
point is y = (Q/32) * r with r a mod-32 sequence, and every seed
(x', y') in {r_0..r_3}^2 is a kernel point, because M^32 == I mod 32
(checked below). Hence the whole fiber of a period-4 point is computed
from the 16 seeds, exactly and level-independently.

Fiber condition: point S with period L_S and period-multiset M_S lies
in the fiber of P (period 4, multiset M_P over 4 values) iff
4 * count_S(v) == L_S * count_P(v) for every value v (N cancels).
Gamma-orbits: 32-tuples, rotations + reversal.
"""
from collections import Counter
from math import gcd

MOD = 32


def mat_mult(A, B):
    return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
             (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
            [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
             (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]]


def mat_pow(M, e):
    R = [[1, 0], [0, 1]]
    while e:
        if e & 1:
            R = mat_mult(R, M)
        M = mat_mult(M, M)
        e >>= 1
    return R


M = [[6, MOD - 1], [1, 0]]
print("M^4  mod 32 =", mat_pow(M, 4))
print("M^8  mod 32 =", mat_pow(M, 8))
print("M^16 mod 32 =", mat_pow(M, 16))
print("M^32 mod 32 =", mat_pow(M, 32))
assert mat_pow(M, 32) == [[1, 0], [0, 1]], "M^32 != I mod 32"

# 1. Period-dividing-4 seeds: (M^4 - I) s == 0 mod 32.
M4 = mat_pow(M, 4)
A = [[(M4[0][0] - 1) % MOD, M4[0][1]],
     [M4[1][0], (M4[1][1] - 1) % MOD]]
seeds4 = []
for x in range(MOD):
    for y in range(MOD):
        if (A[0][0]*x + A[0][1]*y) % MOD == 0 and \
           (A[1][0]*x + A[1][1]*y) % MOD == 0:
            seeds4.append((x, y))
print("period-dividing-4 seeds:", len(seeds4))
assert len(seeds4) == 128


def gen_seq(seed, n):
    """First n terms of the mod-32 recurrence from seed (r0, r1)."""
    r = [seed[0], seed[1]]
    for i in range(1, n - 1):
        r.append((6*r[i] - r[i-1]) % MOD)
    return r


def period_of(seed):
    """Period of the mod-32 sequence from seed (state-repeat search)."""
    r = gen_seq(seed, 200)
    for L in range(1, 129):
        if r[L] == seed[0] and r[L+1] == seed[1]:
            return L
    return None


def tup32(seed):
    return tuple(gen_seq(seed, 32))


def gamma_canon(t):
    """Canonical form of a 32-tuple under rotations and reversal."""
    rots = [tuple(t[k:] + t[:k]) for k in range(32)]
    rev = (t[0],) + tuple(reversed(t[1:]))
    rots += [tuple(rev[k:] + rev[:k]) for k in range(32)]
    return min(rots)


# 2. For each period-4 point, compute its full fiber via the 16 seeds.
fibers = {}  # frozenset of 32-tuples -> dict
bad_period = []
for s in seeds4:
    seq4 = gen_seq(s, 4)
    vals = list(seq4)
    cntP = Counter(vals)
    members = {}  # 32-tuple -> period
    for x in vals:
        for y in vals:
            seed = (x, y)
            L = period_of(seed)
            if L is None or 32 % L != 0:
                bad_period.append((s, seed, L))
                continue
            per = gen_seq(seed, max(L, 2))[:L]
            cntS = Counter(per)
            ok = all(4*cntS.get(v, 0) == L*cntP.get(v, 0)
                     for v in set(list(cntS) + list(cntP)))
            if ok:
                members[tup32(seed)] = L
    key = frozenset(members.keys())
    if key not in fibers:
        fibers[key] = {"periods": set(), "members": members,
                       "base": s, "vals": tuple(vals)}
    fibers[key]["periods"] |= set(members.values())

print("seeds with period not dividing 32:", len(bad_period), bad_period[:5])
print("distinct fibers containing a period-4 point:", len(fibers))

split_fibers = []
mixed = []
for key, f in fibers.items():
    orbits = {gamma_canon(t) for t in key}
    f["n_orbits"] = len(orbits)
    if len(orbits) >= 2:
        split_fibers.append(f)
    if len(f["periods"]) > 1:
        mixed.append(f)

print("split fibers among them:", len(split_fibers))
for f in split_fibers[:10]:
    print("  SPLIT base=", f["base"], "vals=", f["vals"],
          "orbits=", f["n_orbits"], "periods=", sorted(f["periods"]),
          "members=", len(f["members"]))
print("mixed-period fibers:", len(mixed))
for f in mixed[:10]:
    print("  MIXED base=", f["base"], "vals=", f["vals"],
          "orbits=", f["n_orbits"], "periods=", sorted(f["periods"]))

# 3. Orbit census of the 128 points themselves (for reference).
pt_orbits = {gamma_canon(tup32(s)) for s in seeds4}
print("Gamma-orbits among the 128 period<=4 points:", len(pt_orbits))
per_dist = Counter(period_of(s) for s in seeds4)
print("period distribution of the 128 points:", dict(sorted(per_dist.items())))
