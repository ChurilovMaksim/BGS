"""Wave 39 task 4: is split <=> nu=(1,1) for p>=8? And the mod-(Q/2)
recursion for E_alt on split points.
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave36_2part import snf_kernel_i32, orbit_canon
from wave39_Ealt_check import min_period, ealt_of_period_block
from wave39_Ealt_scope import nu_of
from wave16_d1a_targeted import group_ids


def min_period_arr(seq):
    m = len(seq)
    for p in range(1, m + 1):
        if m % p == 0 and np.array_equal(seq, np.tile(seq[:p], m // p)):
            return p
    return m


def main():
    for m in (32, 64):
        k = m.bit_length() - 1
        Q = 2 ** (2 * k + 3)
        pts = snf_kernel_i32(m, Q)
        fib = group_ids(np.sort(pts, axis=1))
        seeds = pts[:, :2].astype(np.int64)
        ca, cb = orbit_canon(seeds, m, Q)
        orb = group_ids(np.stack([ca, cb], axis=1))
        fib_orbits = defaultdict(set)
        for f, o in zip(fib, orb):
            fib_orbits[f].add(o)
        split_fib = {f for f, os_ in fib_orbits.items() if len(os_) >= 2}
        # nu distribution split vs nonsplit (p>=8), and divisibility check
        tab = Counter()
        nodiv = 0
        rec = Counter()  # (p, p', E_alt) for split points
        for i in range(len(pts)):
            p = min_period(pts[i])
            if p < 8:
                continue
            block = pts[i][:p]
            h = p // 2
            d0 = int(block[h]) - int(block[0])
            d1 = int(block[h + 1]) - int(block[1])
            if d0 % (Q // 2) != 0 or d1 % (Q // 2) != 0:
                nodiv += 1
                continue
            nu = ((d0 // (Q // 2)) % 2, (d1 // (Q // 2)) % 2)
            tab[(fib[i] in split_fib, nu)] += 1
            if fib[i] in split_fib:
                # mod-(Q/2) sequence minimal period
                rseq = (block % (Q // 2))
                pp = min_period_arr(rseq)
                A, E, e = ealt_of_period_block(block, Q)
                rec[(p, pp, E)] += 1
        print(f"m={m}: nodiv={nodiv}")
        for key in sorted(tab):
            print(f"  split={key[0]} nu={key[1]}: {tab[key]}")
        print(f"  split-point (p, p', E_alt) table:")
        for key in sorted(rec):
            print(f"    p={key[0]} p'={key[1]} E={key[2]}: {rec[key]}")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
