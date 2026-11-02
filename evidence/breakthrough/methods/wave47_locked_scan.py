"""Wave 47, task 5: locked-candidate scan at m = 36, 72, 144.

For each prime-power component q | D_m (small q only): enumerate kernel
points (wave38 kernel_points), group by value-multiset (fiber), compute
the exact dihedral canonical form per point (Booth least rotation, both
orientations), and report split fibers with a rep period of v3 <= 1
(locked candidates) plus total split-fiber counts.
"""
import sys
from collections import defaultdict

exec(open("wave38_blind_explore.py").read().split("m = 60")[0])


def least_rotation(s):
    m = len(s)
    i, j, k = 0, 1, 0
    while i < m and j < m and k < m:
        a, b = s[(i + k) % m], s[(j + k) % m]
        if a == b:
            k += 1
        elif a < b:
            j = j + k + 1
            if i == j:
                i += 1
            k = 0
        else:
            i = i + k + 1
            if i == j:
                j += 1
            k = 0
    r = min(i, j)
    return tuple(s[(r + t) % m] for t in range(m))


def canon(s):
    return min(least_rotation(s), least_rotation(tuple(reversed(s))))


def v3(n):
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


def scan(m, qs):
    for q in qs:
        pts = kernel_points(m, q)
        fib = defaultdict(list)
        for p in pts:
            fib[tuple(sorted(p))].append(p)
        nsplit = 0
        cands = []
        for key, members in fib.items():
            orbs = {}
            for p in members:
                orbs.setdefault(canon(p), p)
            if len(orbs) > 1:
                nsplit += 1
                pers = sorted(set(period(r) for r in orbs.values()))
                if min(v3(p) for p in pers) <= 1:
                    cands.append((len(orbs), pers))
        print(f"m={m} q={q}: npts={len(pts)} split_fibers={nsplit} "
              f"locked_cands(orbits,periods)={cands}", flush=True)


if __name__ == "__main__":
    scan(36, [25, 49, 121, 128, 5329, 32041, 38809, 39601])
    scan(72, [25, 49, 121, 289, 512, 5329, 32041, 38809, 39601])
    scan(144, [25, 49, 121, 289, 2048, 9409, 5329, 32041, 38809, 39601])
