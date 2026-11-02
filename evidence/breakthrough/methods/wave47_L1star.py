#!/usr/bin/env python3
"""Wave 47, task 3 (PURE COMPUTATION): L1* unit case at NEW prime powers
289, 361, 529, 343. Same convention as wave46_L1_units.check_units:
units C in R/p^f grouped by cycle multiset M(C) over one period T;
violations = C outside dihedral orbit of group rep; scaling-explained =
C in {lam * o : lam unit, o in orbit} (then lam in Stab(M) automatically).
Also checks Stab(M) == {lam unit : lam = +-1 mod p^(f-e)}, e = v_p(2T),
for every group. No proof, no Lean."""
import math, sys, time
from collections import defaultdict

def check(p, f):
    m = p ** f
    beta = (17 % m, 12 % m)
    # order of beta mod m
    x = (1, 0)
    T = None
    for k in range(1, 10000):
        x = ((x[0]*beta[0] + 2*x[1]*beta[1]) % m,
             (x[0]*beta[1] + x[1]*beta[0]) % m)
        if x == (1, 0):
            T = k
            break
    assert T is not None
    # beta powers
    xs, ys = [1], [0]
    for _ in range(T - 1):
        xs.append((xs[-1]*beta[0] + 2*ys[-1]*beta[1]) % m)
        ys.append((xs[-2]*beta[1] + ys[-1]*beta[0]) % m)
    units = [u for u in range(m) if math.gcd(u, m) == 1]
    unitset = set(units)
    groups = defaultdict(list)
    n_units = 0
    for a in range(m):
        for b in range(m):
            if math.gcd((a*a - 2*b*b) % m, m) != 1:
                continue
            n_units += 1
            B = (2 * b) % m
            vals = sorted((2 * (a * xs[k] + B * ys[k])) % m for k in range(T))
            groups[tuple(vals)].append((a, b))
    # e = v_p(2T), predicted Stab modulus
    e = 0
    t = 2 * T
    while t % p == 0:
        e += 1
        t //= p
    pe = p ** (f - e)
    pred_stab = {u for u in units if u % pe in (1, pe - 1)}
    nviol = nscal = 0
    unexplained = []
    stab_bad = 0
    stab_bad_ex = None
    stab_dir = {"subset": 0, "superset": 0, "incomparable": 0}
    for M, cs in groups.items():
        a0, b0 = cs[0]
        orb = set()
        for r in range(T):
            orb.add(((a0*xs[r] + 2*b0*ys[r]) % m,
                     (a0*ys[r] + b0*xs[r]) % m))
            orb.add(((a0*xs[r] - 2*b0*ys[r]) % m,
                     (a0*ys[r] - b0*xs[r]) % m))
        scal = set()
        for lam in units:
            for (u, v) in orb:
                scal.add(((lam*u) % m, (lam*v) % m))
        for C in cs:
            if C not in orb:
                nviol += 1
                if C in scal:
                    nscal += 1
                elif len(unexplained) < 5:
                    unexplained.append((C, cs[0], M))
        stab = {lam for lam in units
                if tuple(sorted((lam*v) % m for v in M)) == M}
        if stab != pred_stab:
            stab_bad += 1
            if stab <= pred_stab:
                stab_dir["subset"] += 1
            elif stab >= pred_stab:
                stab_dir["superset"] += 1
            else:
                stab_dir["incomparable"] += 1
            if stab_bad_ex is None:
                stab_bad_ex = (cs[0], sorted(stab)[:10], len(stab))
    print(f"mod {m}: T={T} e={e} units={n_units} groups={len(groups)} "
          f"violations={nviol} explained={nscal} unexplained={nviol-nscal} "
          f"StabMismatches={stab_bad} {stab_dir} |Stab_pred|={len(pred_stab)}",
          flush=True)
    for C, c0, M in unexplained:
        print(f"  UNEXPLAINED C={C} rep={c0} M={M}", flush=True)
    if stab_bad_ex:
        print(f"  STAB-MISMATCH rep={stab_bad_ex[0]} stab_head={stab_bad_ex[1]} "
              f"|stab|={stab_bad_ex[2]}", flush=True)

if __name__ == "__main__":
    for p, f in [(17, 2), (19, 2), (23, 2), (7, 3)]:
        t0 = time.time()
        check(p, f)
        print(f"  ({time.time()-t0:.1f}s)", flush=True)
