"""Wave 39, task 3: census for the Split Bit Lemma at m=32 (and 64 if cheap).

For each kernel point: minimal period p, nu = (nu0,nu1) from the
half-period defect, fiber id (sorted multiset), Gamma-orbit id, support.
Checks:
  (1) split <=> nu=(1,1)  (all fibers; and restricted to on-support)
  (2) nonsplit p>=8 => nu in {(1,0),(0,1)}
  (3) fibers mix nu types? (which nu values occur inside one fiber)
  (4) for nu=(1,0): odd sub-multiset O never Q/2-symmetric?
      for nu=(0,1): even sub-multiset E never Q/2-symmetric?
  (5) distribution of nu by period.
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon


def period_of_row(y):
    m = len(y)
    for p in range(1, m + 1):
        if m % p == 0 and np.array_equal(y[:p], y[p:2 * p] if 2 * p <= m else y[:p]):
            # need full check: y is p-periodic
            if all(y[i] == y[i % p] for i in range(m)):
                return p
    return m


def main():
    for m, q in [(32, 8192)]:
        pts = snf_kernel_i32(m, q)
        D = Dm(m)
        Z, Qmod = torsion_data(m, D)
        Qm = np.array([qq % q for qq in Qmod], dtype=np.int64)
        sup = ((2 * Qm[None, :] - pts.astype(np.int64) @ Z.astype(np.int64).T) % q == 0).all(axis=1)
        fib = group_ids(np.sort(pts, axis=1))
        ba, bb = orbit_canon(pts[:, :2].astype(np.int64), m, q)
        gam = group_ids(np.stack([ba, bb], axis=1))
        fib_orbits = defaultdict(set)
        fib_nus = defaultdict(set)
        fib_sup = defaultdict(lambda: [0, 0])
        for i in range(len(pts)):
            fib_orbits[int(fib[i])].add(int(gam[i]))
            fib_sup[int(fib[i])][0] += int(sup[i])
            fib_sup[int(fib[i])][1] += 1
        split_ids = {f for f in fib_orbits if len(fib_orbits[f]) > 1}
        onsup_split = {f for f in split_ids if fib_sup[f][0] == fib_sup[f][1]}
        onsup_all = {f for f in fib_sup if fib_sup[f][0] == fib_sup[f][1]}
        print(f"== m={m} q={q}: points={len(pts)} fibers={len(fib_orbits)} "
              f"split={len(split_ids)} onsup_split={len(onsup_split)}")
        # per-point nu
        nu_of = {}
        per_of = {}
        bad_div = 0
        for i in range(len(pts)):
            y = pts[i].astype(np.int64)
            p = period_of_row(y)
            per_of[i] = p
            if p % 2 == 1 or p < 2:
                nu_of[i] = None
                continue
            d0 = int(y[p // 2] - y[0]) % q
            d1 = int(y[p // 2 + 1] - y[1]) % q
            if d0 % (q // 2) != 0 or d1 % (q // 2) != 0:
                bad_div += 1
                nu_of[i] = "BAD"
            else:
                nu_of[i] = ((d0 // (q // 2)) % 2, (d1 // (q // 2)) % 2)
        print("bad_divisibility:", bad_div)
        # (1),(2)
        nu_by_period = Counter()
        viol_split = []   # split fiber with a point nu != (1,1)
        viol_nonsplit = []  # nonsplit p>=8 with nu not in {(1,0),(0,1)}
        for i in range(len(pts)):
            nu_by_period[(per_of[i], nu_of[i])] += 1
            f = int(fib[i])
            if f in split_ids and nu_of[i] != (1, 1):
                viol_split.append((i, per_of[i], nu_of[i], bool(sup[i])))
            if f not in split_ids and per_of[i] >= 8 and nu_of[i] not in ((1, 0), (0, 1)):
                viol_nonsplit.append((i, per_of[i], nu_of[i], bool(sup[i])))
        print("nu by (period,nu):", dict(sorted(nu_by_period.items(), key=str)))
        print("split-fiber points with nu!=(1,1):", len(viol_split), viol_split[:10])
        print("nonsplit p>=8 points with nu not in {(1,0),(0,1)}:",
              len(viol_nonsplit), viol_nonsplit[:10])
        # on-support restriction
        viol_split_os = [v for v in viol_split if v[3]]
        viol_nonsplit_os = [v for v in viol_nonsplit if v[3]]
        print("  of those, on-support:", len(viol_split_os), len(viol_nonsplit_os))
        # (3) nu types per fiber
        for i in range(len(pts)):
            fib_nus[int(fib[i])].add(nu_of[i])
        mixed = {f: s for f, s in fib_nus.items() if len(s) > 1}
        print("fibers with >1 nu value:", len(mixed))
        for f, s in list(mixed.items())[:10]:
            print("   fiber", f, "nus", s, "split" if f in split_ids else "nonsplit",
                  "onsup" if f in onsup_all else "offsup")
        # (4) Q/2-symmetry of odd/even sub-multisets
        half = q // 2
        def q2sym(multi):
            c = Counter(int(v) for v in multi)
            return all(c[v] == c[(v + half) % q] for v in c)
        sym_viol_10 = 0  # nu=(1,0) but odd sub-multiset IS Q/2-symmetric
        sym_viol_01 = 0
        tot10 = tot01 = 0
        for i in range(len(pts)):
            y = pts[i].astype(np.int64)
            p = per_of[i]
            if nu_of[i] == (1, 0):
                tot10 += 1
                odd = [int(y[t]) for t in range(p) if t % 2 == 1]
                if q2sym(odd):
                    sym_viol_10 += 1
            elif nu_of[i] == (0, 1):
                tot01 += 1
                even = [int(y[t]) for t in range(p) if t % 2 == 0]
                if q2sym(even):
                    sym_viol_01 += 1
        print(f"nu=(1,0) points: {tot10}, odd sub-multiset Q/2-symmetric: {sym_viol_10}")
        print(f"nu=(0,1) points: {tot01}, even sub-multiset Q/2-symmetric: {sym_viol_01}")


if __name__ == "__main__":
    main()
