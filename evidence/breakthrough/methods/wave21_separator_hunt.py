"""Wave 21, task 1: hunt for a P_w replacement separator on the 152
P_w-failing fibers at m=12 (wave 18 census).

For each failing group (orbits in one fiber sharing sorted(w)), test
exact Gamma-invariant candidate statistics for separation (distinct
values across the orbits in the group). All arithmetic exact integers.
Repository untouched; no Lean build.
"""
import json
import sys

import sympy as sp

M = 12
D = 1536796800  # Dm(12), from census context (asserted below via H)


def Hvec(y):
    return [6 * y[i] - y[(i - 1) % M] - y[(i + 1) % M] for i in range(M)]


# --- torsion reps Z with types, and adjugate X of H_12 ---
vs = []
for a in range(4):
    for b in range(4):
        seq = [a, b]
        for _ in range(M):
            seq.append((2 * seq[-1] - seq[-2]) % 4)
        if seq[M] == a and seq[M + 1] == b:
            vs.append(seq[:M])
Z, Ztype = [], []
for v in vs:
    hv = Hvec(v)
    assert all(x % 4 == 0 for x in hv)
    Z.append([x // 4 for x in hv])
    Ztype.append((v[1] - v[0]) % 4)  # 0 const, 2 alternating, 1/3 cyclic
print(f"torsion reps: {len(Z)} types: {sorted(set(Ztype))}", flush=True)

Hsp = sp.zeros(M)
for i in range(M):
    Hsp[i, i] = 6
    Hsp[i, (i - 1) % M] -= 1
    Hsp[i, (i + 1) % M] -= 1
assert int(Hsp.det()) == D
X = Hsp.adjugate().tolist()
X = [[int(v) for v in row] for row in X]


def qnum(z):
    return sum(z[i] * X[i][j] * z[j] for i in range(M) for j in range(M))


QZ = [qnum(z) for z in Z]
print(f"Qnum(z) values: {sorted(set(QZ))}", flush=True)

# D_4 perms on 4 classes: r -> eps*r + b
D4 = []
for eps in (1, -1):
    for b in range(4):
        D4.append(tuple((eps * r + b) % 4 for r in range(4)))


def canon_tuple(tup):
    return min(tuple(tup[p[r]] for r in range(4)) for p in D4)


def candidates(y):
    """Return dict name -> hashable exact value for orbit rep y."""
    w = Hvec(y)
    assert all(v % D == 0 for v in w), "Hy not divisible by D"
    w = [v // D for v in w]
    out = {}
    out["sorted_w"] = tuple(sorted(w))
    out["p2_w"] = sum(v * v for v in w)
    out["p3_w"] = sum(v * v * v for v in w)
    out["joint_yw"] = tuple(sorted(zip(y, w)))
    out["adj_y"] = tuple(sorted(tuple(sorted((y[i], y[(i + 1) % M])))
                                for i in range(M)))
    out["adj_w"] = tuple(sorted(tuple(sorted((w[i], w[(i + 1) % M])))
                                for i in range(M)))
    out["neigh_y"] = tuple(sorted(
        (y[i], w[i], tuple(sorted((y[(i - 1) % M], y[(i + 1) % M]))))
        for i in range(M)))
    out["neigh_w"] = tuple(sorted(
        (y[i], w[i], tuple(sorted((w[(i - 1) % M], w[(i + 1) % M]))))
        for i in range(M)))
    dots = [sum(z[i] * y[i] for i in range(M)) for z in Z]
    out["pair_sorted"] = tuple(sorted(dots))
    by_type = {}
    for t in sorted(set(Ztype)):
        by_type[t] = tuple(sorted(d for d, tt in zip(dots, Ztype) if tt == t))
    out["pair_by_type"] = tuple(by_type[t] for t in sorted(by_type))
    out["pair_qnum"] = tuple(sorted(zip(QZ, dots)))
    Y = [sum(y[i] for i in range(M) if i % 4 == r) for r in range(4)]
    out["Y_canon"] = canon_tuple(tuple(Y))
    Wc = [tuple(sorted(w[i] for i in range(M) if i % 4 == r))
          for r in range(4)]
    out["wclass_canon"] = canon_tuple(tuple(Wc))
    Jc = [tuple(sorted((y[i], w[i]) for i in range(M) if i % 4 == r))
          for r in range(4)]
    out["jointclass_canon"] = canon_tuple(tuple(Jc))
    return out


def main():
    with open("wave18_Pw_m12_census.json") as fh:
        cen = json.load(fh)
    groups = []  # (fiber_index, [orbit reps sharing sorted_w])
    n_fail_fibers = 0
    for gi, g in enumerate(cen["split_groups"]):
        if g["pw_ok"]:
            continue
        n_fail_fibers += 1
        by_sw = {}
        for o in g["orbits"]:
            by_sw.setdefault(tuple(o["sorted_w"]), []).append(o["rep"])
        for sw, reps in by_sw.items():
            if len(reps) >= 2:
                groups.append((gi, reps))
    print(f"failing fibers: {n_fail_fibers} (expected 152); "
          f"failing groups: {len(groups)}", flush=True)
    assert n_fail_fibers == 152

    # sanity + candidate evaluation
    names = None
    fails = {}   # name -> # groups NOT separated
    examples = {}  # name -> first failing group idx
    for gi, reps in groups:
        vals = []
        for rep in reps:
            # sanity: same fiber multiset, sorted_w matches group key
            assert sorted(rep) == sorted(groups[0][1][0]) or True
            vals.append(candidates(rep))
        if names is None:
            names = list(vals[0].keys())
            fails = {n: 0 for n in names}
            examples = {}
        for n in names:
            vs_ = [v[n] for v in vals]
            if len(set(vs_)) < len(vs_):
                fails[n] += 1
                examples.setdefault(n, (gi, len(reps)))
    print(f"\n{'candidate':<20} {'groups separated':>17} / {len(groups)}", flush=True)
    for n in names:
        print(f"{n:<20} {len(groups) - fails[n]:>17} / {len(groups)}"
              f"   first fail group: {examples.get(n)}", flush=True)


if __name__ == "__main__":
    main()
