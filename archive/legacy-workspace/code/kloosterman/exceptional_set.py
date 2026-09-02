"""
Empirical determination of the exceptional set  B(k,s)
=====================================================

B(k,s) := { p prime, p = 1 mod k :  E_s(H_{k,p}) > CHAR0(s,k) }.

Theorem A gives  B(k,s) subset {p <= (2s)^{phi(k)}}, an astronomically weak
bound.  This script measures  P*(k,s) = max B(k,s)  by exhaustive scan over
primes p = 1 mod k up to a cap, using the meet-in-the-middle energy count.

Cost per prime is O(C(k+s-1,s) log p), independent of p, so thousands of
primes are cheap.
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subgroup_kloosterman_energy import (           # noqa: E402
    char0_count, energy_Fp, is_prime, lpf, pair_count,
)


def scan(k: int, s: int, pmax: int, verbose: bool = False):
    C0 = char0_count(s, k)
    P = pair_count(s, k)
    bad = []
    n = 0
    npr = 0
    t0 = time.time()
    while True:
        n += 1
        p = k * n + 1
        if p > pmax:
            break
        if not is_prime(p):
            continue
        npr += 1
        E = energy_Fp(p, k, s)
        if E is None:
            return None
        if E > C0:
            bad.append((p, E, E - C0))
        elif E < C0:
            raise AssertionError(f"E < CHAR0 at k={k},s={s},p={p}: {E} < {C0}")
    return {"k": k, "s": s, "lpf": lpf(k), "CHAR0": C0, "PAIR": P,
            "CHAR0_eq_PAIR": C0 == P, "pmax": pmax, "primes_scanned": npr,
            "n_bad": len(bad), "P_star": (max(b[0] for b in bad) if bad else None),
            "bad": bad[-25:], "secs": round(time.time() - t0, 1)}


def main():
    rows = []
    plan = []
    for k in [5, 7, 8, 9, 11, 12, 13, 15, 16, 17, 19, 20, 23, 25, 29, 31, 37, 41]:
        for s in [2, 3, 4, 5]:
            nm = math.comb(k + s - 1, s)
            if nm > 60_000:
                continue
            plan.append((k, s, nm))

    print(f"{'k':>4} {'s':>2} {'lpf':>4} {'CHAR0':>12} {'=PAIR':>6} "
          f"{'#bad':>5} {'P*':>8} {'P*/k':>7} {'log_k P*':>9} {'pmax':>7} {'s'}")
    for k, s, nm in plan:
        pmax = 60_000 if nm < 4000 else 20_000
        r = scan(k, s, pmax)
        if r is None:
            continue
        rows.append(r)
        Ps = r["P_star"]
        lk = (math.log(Ps) / math.log(k)) if Ps else float("nan")
        print(f"{k:>4} {s:>2} {r['lpf']:>4} {r['CHAR0']:>12} "
              f"{str(r['CHAR0_eq_PAIR']):>6} {r['n_bad']:>5} "
              f"{str(Ps):>8} {(Ps/k if Ps else 0):>7.1f} {lk:>9.3f} "
              f"{pmax:>7} {r['secs']}")
        sys.stdout.flush()

    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "rows": rows}
    # empirical law fit:  log P* vs log k  and vs s
    pts = [(r["k"], r["s"], r["P_star"]) for r in rows if r["P_star"]]
    out["fit_points"] = pts
    print("\nEMPIRICAL LAW  (k, s, P*)")
    for k, s, Ps in pts:
        print(f"   k={k:>3} s={s}  P*={Ps:>7}  P*/k^2={Ps/k**2:8.3f}  "
              f"P*/(k^2 s)={Ps/(k**2*s):8.3f}  log_k P* = {math.log(Ps)/math.log(k):.3f}")
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r71", "exceptional_set.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
