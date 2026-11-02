"""Wave 27, task 5, checks 4: equivalence + refined cross-tab.

(a) Validate S^(d) = sum_e x_{e-d} W_e exactly on census data
    (x = adjugate row of H_12), for a failing pair.
(b) Cross-tab over all 762 split groups, per group:
      S0_const  = S^(0) constant across orbits?
      Sall_const = all S^(d) constant across orbits?
      W_const   = all W_d constant across orbits?
    Theorem (proved in the note): Sall_const <=> W_const, via the
    invertible circulant X_circ with eigenvalues D/lambda_j != 0.
    Also report: W_const groups vs S0_const groups.

Exact integers throughout. Repository untouched; no Lean build.
"""
import json
from collections import defaultdict

M = 12
D = 1536796800
XROW = [271669860, 46611180, 7997220, 1372140, 235620, 41580,
        13860, 41580, 235620, 1372140, 7997220, 46611180]


def Hvec(y):
    return [6 * y[i] - y[(i - 1) % M] - y[(i + 1) % M] for i in range(M)]


def Wd(w, d):
    return sum(w[i] * w[(i + d) % M] for i in range(M))


def Sd(y, w, d):
    return sum(y[i] * w[(i + d) % M] for i in range(M))


def main():
    with open("wave18_Pw_m12_census.json") as fh:
        cen = json.load(fh)
    groups = cen["split_groups"]
    assert len(groups) == 762

    # (a) formula validation on the first failing class
    for g in groups:
        if g["pw_ok"]:
            continue
        by_sw = defaultdict(list)
        for o in g["orbits"]:
            by_sw[tuple(o["sorted_w"])].append(o["rep"])
        done = False
        for sw, rr in by_sw.items():
            if len(rr) >= 2:
                for r in rr[:1]:
                    w = [v // D for v in Hvec(r)]
                    W = [Wd(w, d) for d in range(M)]
                    for d in range(M):
                        lhs = Sd(r, w, d)
                        rhs = sum(XROW[(e - d) % M] * W[e]
                                  for e in range(M))
                        assert lhs == rhs, (d, lhs, rhs)
                print(f"(a) S^(d) = sum_e x_{{e-d}} W_e verified exactly "
                      f"for a failing rep, all d", flush=True)
                done = True
                break
        if done:
            break

    # (b) cross-tab
    tab = defaultdict(int)
    for g in groups:
        ws = []
        ys = []
        for o in g["orbits"]:
            r = o["rep"]
            ys.append(r)
            ws.append([v // D for v in Hvec(r)])
        S0_vals = {Sd(ys[k], ws[k], 0) for k in range(len(ys))}
        Sall_vals = {tuple(Sd(ys[k], ws[k], d) for d in range(M))
                     for k in range(len(ys))}
        W_vals = {tuple(Wd(ws[k], d) for d in range(M))
                  for k in range(len(ys))}
        s0 = len(S0_vals) == 1
        sall = len(Sall_vals) == 1
        wcon = len(W_vals) == 1
        tab[(s0, sall, wcon)] += 1
    print("(b) cross-tab (S0_const, Sall_const, W_const) -> #groups:",
          flush=True)
    for k in sorted(tab):
        print(f"    {k} -> {tab[k]}", flush=True)
    # theorem check: Sall == W_const in every group?
    bad = sum(v for (s0, sall, wcon), v in tab.items()
              if sall != wcon)
    print(f"(b) groups violating Sall <=> W_const: {bad}", flush=True)


if __name__ == "__main__":
    main()
