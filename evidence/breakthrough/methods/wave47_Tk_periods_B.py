"""Wave 47, task 10, script B: periods of on-support split fibers in the
wave-36 censuses (m = 32, 64, 128, 256), from the JSON orbit canons.

Seed convention (wave36_2part.orbit_canon): canon (a, b) = (y_0, y_1);
sequence y_{i+1} = 6 y_i - y_{i-1} mod q2, length m. Period = smallest
p | m with the sequence p-periodic (m is a power of 2).
"""
import json


def seq_from_seed(a, b, m, q):
    y = [a % q, b % q]
    for i in range(1, m - 1):
        y.append((6*y[i] - y[i-1]) % q)
    return y


def period_of_seq(y, m):
    p = 1
    while p <= m:
        if all(y[i] == y[i % p] for i in range(m)):
            return p
        p *= 2
    return None


for m in [32, 64, 128, 256]:
    d = json.load(open(f"wave36_2part_m{m}.json"))
    q = d["q2"]
    rows = []
    for f in d["fibers"]:
        pers = sorted({period_of_seq(seq_from_seed(a, b, m, q), m)
                       for (a, b) in f["own_orbit_canons"]})
        rows.append((f["kind"], f["n_orbits"], f["size"],
                     tuple(f["orbit_sizes"]), tuple(pers)))
    print(f"== m={m} (N={m}, N/4={m//4}): {len(rows)} on-support split fibers")
    for kind in ["NEW", "OLD"]:
        sub = [r for r in rows if r[0] == kind]
        if not sub:
            continue
        print(f"   {kind}: {len(sub)} fibers")
        for r in sorted(set(sub)):
            o, s, osz, pers = r[1], r[2], r[3], r[4]
            ratio = [p // o for p in pers]
            print(f"     o={o} size={s} orbit_sizes={osz} periods={pers} "
                  f"p/o={ratio}")
    allp = sorted({p for r in rows for p in r[4]})
    maxp = max(allp)
    print(f"   periods present: {allp}; max={maxp} (N/4={m//4}); "
          f"p=4o everywhere: {all(r[4] == (4*r[1],) for r in rows)}; "
          f"p<=4o everywhere: {all(all(p <= 4*r[1] for p in r[4]) for r in rows)}")
