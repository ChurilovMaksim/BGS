"""Wave 39 task 4: structure of E_alt on split fibers.
Q1: is |E_alt| constant across the orbits of one split fiber?
Q2: nu distribution on split points (all supports)?
Q3: m=128 confirmation of max|E|=6 on split points?
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave36_2part import snf_kernel_i32, orbit_canon
from wave39_Ealt_check import min_period, ealt_of_period_block
from wave39_Ealt_scope import nu_of
from wave16_d1a_targeted import Dm, torsion_data, group_ids


def main():
    ms = [int(x) for x in sys.argv[1:]] or [32]
    for m in ms:
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
        # per-point |E|, per-fiber set of |E| over its orbits
        fib_E = defaultdict(set)
        orb_E = {}
        nu_split = Counter()
        maxE = 0
        for i in range(len(pts)):
            if fib[i] not in split_fib:
                continue
            p = min_period(pts[i])
            if p < 8:
                continue
            A, E, e = ealt_of_period_block(pts[i][:p], Q)
            maxE = max(maxE, abs(E))
            fib_E[fib[i]].add(abs(E))
            orb_E.setdefault(orb[i], abs(E))
            nu_split[nu_of(pts[i][:p], Q)] += 1
        multi = {f: v for f, v in fib_E.items() if len(v) > 1}
        print(f"m={m}: split fibers={len(split_fib)} max|E|={maxE} "
              f"fibers with non-constant |E|: {len(multi)}")
        print(f"  nu dist on split points (p>=8): {dict(nu_split)}")
        if multi:
            print(f"  examples: {list(multi.items())[:5]}")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
