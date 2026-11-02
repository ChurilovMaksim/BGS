#!/usr/bin/env python3
"""Wave 47x, task A, part 2: (7,2) with u=ord(beta), (5,3),
mod-p L3 tests, (11,2) genericity."""
from collections import Counter
from wave47x_L3_pT_survey import rmul, rpow, build, l3_census, find_u


def build_u(p, f, u):
    mod = p ** f
    beta = rmul((3 % mod, 2 % mod), (3 % mod, 2 % mod), mod)
    bp = [(1, 0)]
    for _ in range(1, u):
        bp.append(rmul(bp[-1], beta, mod))
    cyc, per, per0 = [], [], []
    for a in range(mod):
        for b in range(mod):
            cy = [(2 * rmul((a, b), bp[k], mod)[0]) % mod for k in range(u)]
            T = u
            for d in range(1, u + 1):
                if u % d == 0 and all(cy[k] == cy[k % d] for k in range(u)):
                    T = d
                    break
            cy0 = [v % p for v in cy]
            T0 = u
            for d in range(1, u + 1):
                if u % d == 0 and all(cy0[k] == cy0[k % d] for k in range(u)):
                    T0 = d
                    break
            cyc.append(tuple(cy))
            per.append(T)
            per0.append(T0)
    return mod, cyc, per, per0


def modp_l3(p):
    u = find_u(p, 1)
    mod, beta, cyc, per, per0 = build(p, 1, u)
    viol, mset = l3_census(mod, cyc, f"mod-p p={p} u={u}")
    return viol


if __name__ == "__main__":
    # (7,2): alpha has odd order 21, so no u with alpha^u=-1; use u=ord(beta)=21
    print("== (7,2) with u=21 (ord beta) ==")
    mod, cyc, per, per0 = build_u(7, 2, 21)
    dist = Counter(zip(per, per0))
    print(f"  params={len(cyc)} (T,T0) dist={sorted(dist.items())}")
    viol, _ = l3_census(mod, cyc, "(7,2) u=21")
    # (5,3)
    u53 = find_u(5, 3)
    print(f"== (5,3): u={u53} ==")
    if u53:
        mod, beta, cyc, per, per0 = build(5, 3, u53)
        dist = Counter(zip(per, per0))
        pt = sorted([(T, T0, n) for (T, T0), n in dist.items() if T % 5 == 0])
        print(f"  params={len(cyc)} p|T (T,T0,count)={pt}")
        viol, _ = l3_census(mod, cyc, "(5,3)")
    # mod-p L3 tests
    print("== mod-p L3 tests (regime-B validation) ==")
    for p in [5, 11, 13]:
        modp_l3(p)
    # (11,2) genericity: distinct mod-p values / zeros among T0=6 cycles
    print("== (11,2) genericity ==")
    mod, beta, cyc, per, per0 = build(11, 2, 66)
    gen = Counter()
    for cy, T, T0 in zip(cyc, per, per0):
        if T0 == 6:
            vals = cy[:6]
            vals0 = [v % 11 for v in vals]
            gen[(len(set(vals0)), 0 in vals0)] += 1
    print(f"  (distinct-mod-11-values, has-zero) counts: {sorted(gen.items())}")
