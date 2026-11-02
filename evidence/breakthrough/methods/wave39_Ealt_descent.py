"""Wave 39 task 4: does the half-shift property propagate down the
mod-(Q/2) descent? For each split point, iterate:
  (y mod Q*, period p*) -> (y mod Q*/2, period p*/2)
and check at every step: y_{i+p*/2} == y_i + Q*/2 (mod Q*) for all i.
Also record the base period-4 data (r0, r1, Q_t, E).
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave36_2part import snf_kernel_i32, orbit_canon
from wave39_Ealt_check import min_period, ealt_of_period_block
from wave16_d1a_targeted import group_ids


def check_half_shift(block, Q):
    """block: minimal-period block (list), Q: modulus. Returns True iff
    y_{i+p/2} == y_i + Q/2 (mod Q) for all i, where the block is extended
    p-periodically (here block length = p, so indices mod p)."""
    p = len(block)
    assert p % 2 == 0
    h = p // 2
    b = np.array(block, dtype=np.int64)
    return bool(np.all((b[(np.arange(p) + h) % p] - b) % Q == Q // 2))


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
        nsteps_fail = Counter()
        base = Counter()
        Epres = 0
        Etot = 0
        for i in range(len(pts)):
            if fib[i] not in split_fib:
                continue
            p = min_period(pts[i])
            if p < 8:
                continue
            block = [int(v) for v in pts[i][:p]]
            Qs = Q
            # step 0: half-shift at top level is nu=(1,1), already known
            assert check_half_shift(block, Qs)
            Etop = ealt_of_period_block(np.array(block), Qs)[1]
            # descend
            cur, Qc = block, Qs
            ok = True
            while len(cur) > 4:
                Qc = Qc // 2
                r = [v % Qc for v in cur]
                # minimal period of r (should be len(cur)/2)
                rr = np.array(r)
                pp = None
                for d in range(1, len(r) + 1):
                    if len(r) % d == 0 and np.array_equal(
                            rr, np.tile(rr[:d], len(r) // d)):
                        pp = d
                        break
                r = r[:pp]
                if not check_half_shift(r, Qc):
                    ok = False
                    nsteps_fail[(len(cur), pp)] += 1
                    break
                cur, Qc2 = r, Qc
                Qc = Qc2
            if ok:
                # base: period-4 block cur mod Qc; E preserved?
                Eb = ealt_of_period_block(np.array(cur), Qc)[1]
                Etot += 1
                if Eb == Etop:
                    Epres += 1
                # base data: r0, r1 with s2 = s0 + Qt/2 wrap etc.
                s = cur
                Qt = Qc
                r0 = s[0] % (Qt // 2)
                r1 = s[1] % (Qt // 2)
                base[(Qt, r0, r1, Eb)] += 1
        print(f"m={m}: descent half-shift failures: {dict(nsteps_fail)}")
        print(f"  E preserved top->base: {Epres}/{Etot}")
        # summarize base E values and (r0-r1)/Qt ratio
        bE = Counter()
        for (Qt, r0, r1, Eb), c in base.items():
            bE[Eb] += c
        print(f"  base E dist: {dict(sorted(bE.items()))}")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
