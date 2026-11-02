#!/usr/bin/env python3
"""Wave 47x, task A: L3 at p|T — survey + census.

Setup (wave 46): R = Z[sqrt2] mod p^f, alpha=(3,2), beta=alpha^2,
cycle[k] = Tr(C beta^k) = 2a_k, k in Z/u, alpha^u = -1 mod p^f.
per(C) = exact period of the value sequence (divisor of u).
T0(C) = period of the value sequence reduced mod p.
"""
from collections import Counter
from math import gcd


def rmul(x, y, mod):
    return ((x[0]*y[0] + 2*x[1]*y[1]) % mod, (x[0]*y[1] + x[1]*y[0]) % mod)


def rpow(x, n, mod):
    r = (1 % mod, 0)
    while n:
        if n & 1:
            r = rmul(r, x, mod)
        x = rmul(x, x, mod)
        n >>= 1
    return r


def order(x, mod, cap):
    # order of x in R^×, assuming it divides cap
    for d in range(1, cap + 1):
        if cap % d == 0 and rpow(x, d, mod) == (1 % mod, 0):
            return d
    return None


def find_u(p, f):
    """u with alpha^u = -1 mod p^f, if it exists (u = ord(alpha)/2)."""
    mod = p ** f
    alpha = (3 % mod, 2 % mod)
    # order of alpha divides phi-ish; brute force up to 4*mod for small cases
    cur = (1 % mod, 0)
    for k in range(1, 8 * mod + 1):
        cur = rmul(cur, alpha, mod)
        if cur == (mod - 1, 0):
            return k
    return None


def build(p, f, u):
    mod = p ** f
    alpha = (3 % mod, 2 % mod)
    assert rpow(alpha, u, mod) == (mod - 1, 0), "u not constraining"
    beta = rmul(alpha, alpha, mod)
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
    return mod, beta, cyc, per, per0


def l3_census(mod, cyc, label, want_t_periods=None):
    """Exact L3 test as in wave 46. If want_t_periods given, only report
    violations where t's exact period is in that set (for p|T focus);
    still count all violations."""
    mset = {}
    for i in range(len(cyc)):
        mset.setdefault(tuple(sorted(cyc[i])), []).append(i)
    keys = list(mset.keys())
    cnt = {k: Counter(k) for k in keys}
    neg = {k: tuple(sorted(((-v) % mod) for v in k)) for k in keys}
    keyset = set(keys)
    # map multiset -> periods of its params
    per_of = {}
    viol_all, viol_want = [], []
    for t in keys:
        S = cnt[t] + cnt[neg[t]]
        for x in keys:
            if any(cnt[x][v] > S[v] for v in cnt[x]):
                continue
            rem = S - cnt[x]
            remkey = tuple(sorted(rem.elements()))
            if remkey in keyset and {x, remkey} != {t, neg[t]}:
                viol_all.append((t, x, remkey))
    print(f"  [{label}] params={len(cyc)} distinct multisets={len(keys)} "
          f"L3 violations={len(viol_all)}")
    for v in viol_all[:5]:
        print(f"    VIOL t={v[0]} x={v[1]} x'={v[2]}")
    return viol_all, mset


def survey_component(p, f):
    u = find_u(p, f)
    print(f"== p={p} f={f}: u={u}")
    if u is None:
        print("  no u with alpha^u = -1; skip")
        return
    mod, beta, cyc, per, per0 = build(p, f, u)
    ob = order(beta, mod, u)
    # beta order mod p
    modp = p
    betap = (beta[0] % p, beta[1] % p)
    obp = None
    cur = (1 % p, 0)
    for k in range(1, 4 * p * p + 1):
        cur = rmul(cur, betap, p)
        if cur == (1 % p, 0):
            obp = k
            break
    print(f"  mod={mod} ord(beta mod p^f)={ob} ord(beta mod p)={obp}")
    # period distribution
    dist = Counter(zip(per, per0))
    pt = [(T, T0) for (T, T0) in dist if T % p == 0]
    print(f"  distinct (T,T0) pairs: {len(dist)}; with p|T: {sorted(pt)}")
    for (T, T0) in sorted(pt):
        n = dist[(T, T0)]
        ratio = T // T0 if T0 and T % T0 == 0 else None
        print(f"    T={T} T0={T0} count={n} T/T0={ratio} "
              f"p-power={ratio is not None and ratio & (ratio - 1) == 0}")
    # lift-tower check for one p|T example: defect sequence
    for i, (T, T0) in enumerate(zip(per, per0)):
        if T % p == 0 and T0 > 0 and T % T0 == 0:
            cy = cyc[i]
            defect = [(cy[k + T0] - cy[k]) % mod for k in range(T0)]
            vp = [min([e for e in range(f + 1) if d % (p ** e) == 0
                       or e == 0] + [99]) for d in defect]
            # simpler: exact p-adic valuation of each defect
            def val(d):
                e = 0
                while e < f and d % (p ** (e + 1)) == 0:
                    e += 1
                return e
            print(f"    example param {i}: T={T} T0={T0} defect valuations "
                  f"{[val(d) for d in defect]} distinct-vals-mod-p="
                  f"{len(set(v % p for v in cy[:T0]))}")
            break
    return mod, cyc, per, per0


def both_double_search(p):
    """Mod p (f=1): search for x with per(x)=2*per(t) and
    values(x) = values(t) union values(-t) for some t (the configuration
    that would break mod-p Step 1)."""
    u = find_u(p, 1)
    if u is None:
        print(f"  mod-p p={p}: no u; skip")
        return
    mod, beta, cyc, per, per0 = build(p, 1, u)
    # here per == per0 since f=1
    valsets = {}
    for i in range(len(cyc)):
        valsets.setdefault(tuple(sorted(set(cyc[i][:per[i]]))), []).append(i)
    found = []
    for i in range(len(cyc)):
        Ti = per[i]
        if Ti % 2 == 1:
            continue
        vi = set(cyc[i][:Ti])
        for j in range(len(cyc)):
            Tj = per[j]
            if Ti != 2 * Tj:
                continue
            vj = set(cyc[j][:Tj])
            if vi == vj | set((-v) % p for v in vj):
                found.append((i, Ti, j, Tj))
                break
        if found and len(found) >= 3:
            break
    print(f"  mod-p p={p}: u={u} both-double configurations found: "
          f"{len(found)} (showing <=3)")
    for (i, Ti, j, Tj) in found[:3]:
        print(f"    x param {i} per {Ti} = 2 x t param {j} per {Tj}")
    return found


if __name__ == "__main__":
    import sys
    # survey f=2 components
    for (p, f) in [(5, 2), (7, 2), (11, 2), (13, 2)]:
        out = survey_component(p, f)
        if out:
            mod, cyc, per, per0 = out
            u = find_u(p, f)
            viol, mset = l3_census(mod, cyc, f"p={p} f={f}")
    print("== mod-p both-double search ==")
    for p in [5, 7, 11, 13]:
        both_double_search(p)
