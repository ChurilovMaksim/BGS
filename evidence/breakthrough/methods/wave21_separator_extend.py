"""Wave 21 extension: (a) empirical Gamma-invariance of adj_y;
(b) adj_y / neigh_y / neigh_w separation on ALL 762 split fibers
on support at m=12 (not just the 152 P_w-failing ones).
Exact integers. Repository untouched; no Lean build.
"""
import json

M = 12
D = 1536796800


def Hvec(y):
    return [6 * y[i] - y[(i - 1) % M] - y[(i + 1) % M] for i in range(M)]


def adj_y(y):
    return tuple(sorted(tuple(sorted((y[i], y[(i + 1) % M])))
                        for i in range(M)))


def neigh_y(y):
    w = [v // D for v in Hvec(y)]
    return tuple(sorted(
        (y[i], w[i], tuple(sorted((y[(i - 1) % M], y[(i + 1) % M]))))
        for i in range(M)))


def neigh_w(y):
    w = [v // D for v in Hvec(y)]
    return tuple(sorted(
        (y[i], w[i], tuple(sorted((w[(i - 1) % M], w[(i + 1) % M]))))
        for i in range(M)))


# dihedral perms on 12 positions: i -> eps*i + b
PERMS = []
for eps in (1, -1):
    for b in range(M):
        PERMS.append(tuple((eps * i + b) % M for i in range(M)))


def main():
    with open("wave18_Pw_m12_census.json") as fh:
        cen = json.load(fh)
    groups = cen["split_groups"]
    print(f"split groups: {len(groups)} (expected 762)", flush=True)

    # (a) invariance: adj_y constant on each orbit (apply all 24 perms)
    bad = 0
    checked = 0
    for g in groups[:50]:
        for o in g["orbits"]:
            rep = o["rep"]
            base = adj_y(rep)
            for p in PERMS:
                permuted = [rep[p[i]] for i in range(M)]
                if adj_y(permuted) != base:
                    bad += 1
            checked += 1
    print(f"invariance check: {checked} reps x 24 perms, violations: {bad}",
          flush=True)

    # (b) separation on all split groups
    for name, fn in (("adj_y", adj_y), ("neigh_y", neigh_y),
                     ("neigh_w", neigh_w)):
        nsep = 0
        nfail = 0
        fail_ex = None
        for gi, g in enumerate(groups):
            vals = [fn(o["rep"]) for o in g["orbits"]]
            if len(set(vals)) == len(vals):
                nsep += 1
            else:
                nfail += 1
                fail_ex = fail_ex or (gi, len(vals),
                                      [o["orbit_size"] for o in g["orbits"]])
        print(f"{name}: separates {nsep}/{len(groups)} split groups; "
              f"fails {nfail}, first fail: {fail_ex}", flush=True)

    # failing-group orbit-count distribution (from hunt)
    from collections import Counter
    c = Counter()
    for g in groups:
        if not g["pw_ok"]:
            by_sw = {}
            for o in g["orbits"]:
                by_sw.setdefault(tuple(o["sorted_w"]), []).append(o)
            for reps in by_sw.values():
                if len(reps) >= 2:
                    c[len(reps)] += 1
    print(f"P_w-failing group orbit counts: {dict(c)}", flush=True)


if __name__ == "__main__":
    main()
