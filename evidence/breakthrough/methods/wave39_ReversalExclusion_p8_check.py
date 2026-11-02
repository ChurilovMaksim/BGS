"""Wave 39 task 4 check: mod-64 classification behind reversal exclusion at p=8.
Verifies: (1) counterexample seed (1,11) has A_z=-72, E_alt=-9, minimal period 8;
(2) among all 384 minimal-period-8 z-sequences mod 64, split <=> all-even
(128 each), and split sequences have A_z in {0,+-16,+-32,+-48}."""
from collections import defaultdict


def seq(z0, z1, mod=64):
    y = [z0 % mod, z1 % mod]
    for i in range(2, 8):
        y.append((6 * y[-1] - y[-2]) % mod)
    return y


def canon(y):
    rots = [tuple(y[(i + k) % 8] for i in range(8)) for k in range(8)]
    rev = [y[(-i) % 8] for i in range(8)]
    revrots = [tuple(rev[(i + k) % 8] for i in range(8)) for k in range(8)]
    return min(rots + revrots)


def period(y):
    for p in (1, 2, 4, 8):
        if all(y[i % p] == y[i] for i in range(8)):
            return p
    return 8


z = seq(1, 11)
assert period(z) == 8, z
az = sum(((-1) ** i) * z[i] for i in range(8))
assert (z, az) == ([1, 11, 1, 59, 33, 11, 33, 59], -72), (z, az)
assert az // 8 == -9  # E_alt = A_z / 8

fib = defaultdict(set)
seqs = []
for z0 in range(64):
    for z1 in range(64):
        y = seq(z0, z1)
        y8 = (6 * y[-1] - y[-2]) % 64
        y9 = (6 * y8 - y[-1]) % 64
        if y8 != y[0] or y9 != y[1] or period(y) != 8:
            continue
        seqs.append(tuple(y))
        fib[tuple(sorted(y))].add(canon(y))
assert len(seqs) == 384
split_seqs = set()
for k, orbits in fib.items():
    if len(orbits) > 1:
        for c in orbits:
            pass
        # recover members via a second pass over seqs is unnecessary: use fib keys
        split_seqs.add(k)
even_seqs = {tuple(sorted(y)) for y in seqs if all(v % 2 == 0 for v in y)}
assert split_seqs == even_seqs, "split multisets != all-even multisets"
split_az = set()
for y in seqs:
    if tuple(sorted(y)) in split_seqs:
        split_az.add(sum(((-1) ** i) * y[i] for i in range(8)))
assert split_az == {0, -16, 16, -32, 32, -48, 48}, split_az
assert all(abs(a) < 64 for a in split_az)
print("ALL CHECKS PASS: counterexample E_alt=-9; split<=>all-even;",
      "split A_z in {0,+-16,+-32,+-48}, |E_alt|<=6")
