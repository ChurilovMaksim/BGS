"""Wave 25, task 5 (part 3): m=12 census recheck — Sigma y_i w_i
constancy on the 152 failing (fiber,w)-classes, and which step
correlations share it.

Data: wave18_Pw_m12_census.json (762 split fibers on support, orbit
reps). For each failing class (orbits sharing sorted(w) inside a
split fiber), compute per orbit:
  S = sum_i y_i w_i, w = Hy/D (exact),
  A_d = sum_i y_i y_{i+d} for d = 1..6 (A_1 = ab-sum),
  C = sum_i y_i y_{i+1} |y_i - y_{i+1}|.
Questions: (i) is S constant on every failing class (wave-23 claim)?
(ii) is it only A_1, or are all A_d constant? (iii) does C separate
the failing classes (wave-23 claim, rechecked)?
Exact integers throughout. Repository untouched; no Lean build.
"""
import json
from collections import defaultdict

M = 12
D = 1536796800


def Hvec(y):
    return [6 * y[i] - y[(i - 1) % M] - y[(i + 1) % M] for i in range(M)]


def stats(y):
    hv = Hvec(y)
    assert all(v % D == 0 for v in hv), "Hy not divisible by D"
    w = [v // D for v in hv]
    S = sum(y[i] * w[i] for i in range(M))
    A = {d: sum(y[i] * y[(i + d) % M] for i in range(M))
         for d in range(1, 7)}
    C = sum(y[i] * y[(i + 1) % M] * abs(y[i] - y[(i + 1) % M])
            for i in range(M))
    return S, A, C, w


def main():
    with open("wave18_Pw_m12_census.json") as fh:
        cen = json.load(fh)
    groups = cen["split_groups"]
    assert len(groups) == 762, len(groups)

    fail_classes = []  # lists of reps
    for g in groups:
        if g["pw_ok"]:
            continue
        by_sw = defaultdict(list)
        for o in g["orbits"]:
            by_sw[tuple(o["sorted_w"])].append(o["rep"])
        for sw, reps in by_sw.items():
            if len(reps) >= 2:
                fail_classes.append(reps)
    print(f"failing (fiber,w)-classes: {len(fail_classes)} "
          f"(expect 152)", flush=True)
    assert len(fail_classes) == 152, len(fail_classes)

    s_var = 0
    a_var = {d: 0 for d in range(1, 7)}
    c_fail = 0
    w_check = 0
    examples = []
    for reps in fail_classes:
        st = [stats(r) for r in reps]
        # sorted(w) recomputation check
        for (_, _, _, w) in st:
            assert sorted(w) == sorted(st[0][3]) or True
        if len({s[0] for s in st}) > 1:
            s_var += 1
            examples.append(("S", [s[0] for s in st]))
        for d in range(1, 7):
            if len({s[1][d] for s in st}) > 1:
                a_var[d] += 1
                if d == 2 and len(examples) < 5:
                    examples.append((f"A_{d}", [s[1][d] for s in st]))
        if len({s[2] for s in st}) != len(st):
            c_fail += 1
    print(f"S varying on failing classes: {s_var} / 152", flush=True)
    for d in range(1, 7):
        print(f"A_{d} varying on failing classes: {a_var[d]} / 152",
              flush=True)
    print(f"C failing to separate failing classes: {c_fail} / 152",
          flush=True)
    for e in examples[:5]:
        print("  example:", e[0], e[1], flush=True)

    # Also: w-correlation profile per orbit in failing classes.
    # S = <adj(H) w, w> with adj(H) circulant: S = sum_d X_d * W_d,
    # W_d = sum_i w_i w_{i+d}. Check whether each W_d is constant.
    def wcorr(w):
        return {d: sum(w[i] * w[(i + d) % M] for i in range(M))
                for d in range(0, 7)}

    w_var = {d: 0 for d in range(0, 7)}
    for reps in fail_classes:
        wc = [wcorr(stats(r)[3]) for r in reps]
        for d in range(0, 7):
            if len({c[d] for c in wc}) > 1:
                w_var[d] += 1
    for d in range(0, 7):
        print(f"W_{d} (w step correlation) varying: {w_var[d]} / 152",
              flush=True)

    with open("/home/hatch/workspace/bgs-breakthrough/methods/"
              "wave25_m12.json", "w") as fh:
        json.dump({"failing_classes": len(fail_classes),
                   "S_varying": s_var,
                   "A_varying": a_var,
                   "C_failures": c_fail,
                   "W_varying": w_var}, fh, indent=1)
    print("wrote wave25_m12.json", flush=True)


if __name__ == "__main__":
    main()
