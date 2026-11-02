"""Wave 39 task 4: find the exact scope where |E_alt| < 8 holds.

Intersect: on-support split fibers, nu = (1,1), minimal period p >= 8.
Also report the same for broader scopes to see which hypothesis is load-bearing.
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave36_2part import snf_kernel_i32, orbit_canon
from wave39_Ealt_check import min_period, ealt_of_period_block
from wave16_d1a_targeted import Dm, torsion_data, group_ids


def nu_of(block, Q):
    """Half-period defect nu in (Z/2)^2 for a minimal-period block."""
    p = len(block)
    assert p % 2 == 0
    h = p // 2
    d0 = int(block[h]) - int(block[0])
    d1 = int(block[h + 1]) - int(block[1])
    half = Q // 2
    assert d0 % half == 0 and d1 % half == 0, (d0, d1, half)
    return ((d0 // half) % 2, (d1 // half) % 2)


def main():
    for m in (32, 64):
        k = m.bit_length() - 1
        Q = 2 ** (2 * k + 3)
        D = Dm(m)
        Z, Qmod = torsion_data(m, D)
        pts = snf_kernel_i32(m, Q)
        n = len(pts)
        # support
        Qm = np.array([qq % Q for qq in Qmod], dtype=np.int64)
        Z64 = Z.astype(np.int64)
        sup = np.empty(n, dtype=bool)
        for s in range(0, n, 65536):
            dot = pts[s:s + 65536].astype(np.int64) @ Z64.T
            sup[s:s + 65536] = ((2 * Qm[None, :] - dot) % Q == 0).all(axis=1)
        fib = group_ids(np.sort(pts, axis=1))
        seeds = pts[:, :2].astype(np.int64)
        ca, cb = orbit_canon(seeds, m, Q)
        orb = group_ids(np.stack([ca, cb], axis=1))
        # fiber -> set of orbits
        fib_orbits = defaultdict(set)
        for f, o in zip(fib, orb):
            fib_orbits[f].add(o)
        split_fib = {f for f, os_ in fib_orbits.items() if len(os_) >= 2}
        print(f"=== m={m} Q={Q} points={n} fibers={len(fib_orbits)} "
              f"split_fibers={len(split_fib)}")
        scopes = {
            "all": np.ones(n, dtype=bool),
            "split": np.array([f in split_fib for f in fib]),
            "on-support": sup,
            "split+support": np.array([f in split_fib for f in fib]) & sup,
        }
        for name, mask in scopes.items():
            maxE, cnt, bad = 0, 0, 0
            dist = Counter()
            for i in np.where(mask)[0]:
                p = min_period(pts[i])
                if p < 8:
                    continue
                A, E, e = ealt_of_period_block(pts[i][:p], Q)
                nu = nu_of(pts[i][:p], Q)
                cnt += 1
                dist[E] += 1
                maxE = max(maxE, abs(E))
                if abs(E) >= 8:
                    bad += 1
            print(f"  {name}: p>=8 points={cnt} max|E|={maxE} |E|>=8: {bad}")
            if name in ("split+support",):
                print(f"    E dist: {dict(sorted(dist.items()))}")
        # nu=(1,1) within split+support
        for name, mask in [("split+support+nu11", None)]:
            cnt, bad, maxE = 0, 0, 0
            dist = Counter()
            for i in range(n):
                if fib[i] not in split_fib or not sup[i]:
                    continue
                p = min_period(pts[i])
                if p < 8:
                    continue
                nu = nu_of(pts[i][:p], Q)
                if nu != (1, 1):
                    continue
                A, E, e = ealt_of_period_block(pts[i][:p], Q)
                cnt += 1
                dist[E] += 1
                maxE = max(maxE, abs(E))
                if abs(E) >= 8:
                    bad += 1
            print(f"  {name}: points={cnt} max|E|={maxE} |E|>=8: {bad}")
            print(f"    E dist: {dict(sorted(dist.items()))}")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
