#!/usr/bin/env python3
"""Wave 47x, task A, part 3: tower uniformity + (7,2) coverage.

Tower of cycle C over mod-p class ybar: {Tr(C beta^j) : Tr(C beta^j) = ybar
mod p}. Uniform tower: every lift of ybar mod p^f appears equally often.
If all towers of C are uniform, M(C) = c * Lift(M(Cbar)) with
c = u / (T0 * p^(f-1)), so M(C) is determined by M(Cbar).
"""
from collections import Counter
from wave47x_L3_pT_survey import build
from wave47x_L3_pT_survey2 import build_u


def tower_uniform(cy, T0, p, f, u):
    """cy: length-u value tuple. Returns (uniform?, detail)."""
    mod = p ** f
    lifts_per_class = p ** (f - 1)
    # positions grouped by mod-p class
    by_class = {}
    for k, v in enumerate(cy):
        by_class.setdefault(v % p, []).append(v)
    for ybar, vals in by_class.items():
        # each lift ybar + p*t (t in Z/p^(f-1)) must appear equally often
        cnt = Counter((v - ybar) // p for v in vals)
        if len(cnt) != lifts_per_class:
            return False, (ybar, "missing lifts", len(cnt))
        if len(set(cnt.values())) != 1:
            return False, (ybar, "uneven", sorted(cnt.values())[:5])
    return True, None


def check_component(p, f, u, builder):
    mod, *rest = builder(p, f, u)
    if len(rest) == 4:
        beta, cyc, per, per0 = rest
    else:
        cyc, per, per0 = rest
    tot = uni = 0
    nonuni_examples = []
    for cy, T, T0 in zip(cyc, per, per0):
        if T % p != 0:
            continue
        tot += 1
        ok, det = tower_uniform(cy, T0, p, f, u)
        uni += ok
        if not ok and len(nonuni_examples) < 3:
            nonuni_examples.append((cy[:T], T, T0, det))
    print(f"p={p} f={f}: p|T cycles={tot} uniform-tower={uni} "
          f"nonuniform={tot - uni}")
    for ex in nonuni_examples:
        print(f"   nonuni: period-vals={ex[0]} T={ex[1]} T0={ex[2]} det={ex[3]}")
    return tot, uni


def coverage(p, f, u, builder):
    mod, *rest = builder(p, f, u)
    if len(rest) == 4:
        beta, cyc, per, per0 = rest
    else:
        cyc, per, per0 = rest
    tot = good = df = nf = 0
    for cy, T, T0 in zip(cyc, per, per0):
        if T % p != 0:
            continue
        tot += 1
        vals = [v % p for v in cy[:T0]]
        if len(set(vals)) != T0:
            df += 1
            continue
        if any((-v) % p in set(vals) for v in vals):
            nf += 1
            continue
        good += 1
    print(f"p={p} f={f} coverage: p|T={tot} satisfy distinct+negfree={good} "
          f"distinct-fail={df} negfree-fail={nf}")


if __name__ == "__main__":
    coverage(5, 2, 15, build)
    coverage(7, 2, 21, build_u)
    check_component(5, 2, 15, build)
    check_component(7, 2, 21, build_u)
    check_component(11, 2, 66, build)
    check_component(5, 3, 75, build)
