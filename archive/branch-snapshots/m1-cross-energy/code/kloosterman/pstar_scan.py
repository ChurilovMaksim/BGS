"""
Fast, honest determination of  P*(k,s) = max { p = 1 mod k prime :
                                              E_s(H_{k,p}) > PAIR(s,k) }
for k PRIME (where char-0 rigidity gives CHAR0 = PAIR for every s, so every
excess is a genuine mod-p sporadic coincidence).

Vectorised: the multiset index table is built once, independent of p.
"""

from __future__ import annotations

import json
import math
import os
import sys
import time
from itertools import combinations_with_replacement

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subgroup_kloosterman_energy import is_prime, pair_count   # noqa: E402


def multiset_table(k: int, s: int):
    """(idx array of shape (M,s), multiplicity weights of shape (M,))."""
    rows = list(combinations_with_replacement(range(k), s))
    idx = np.array(rows, dtype=np.int64)
    # multiplicity = s! / prod(counts!)
    w = np.empty(len(rows), dtype=np.int64)
    fs = math.factorial(s)
    for r, tup in enumerate(rows):
        m = fs
        cnt = {}
        for t in tup:
            cnt[t] = cnt.get(t, 0) + 1
        for c in cnt.values():
            m //= math.factorial(c)
        w[r] = m
    return idx, w


def order_k_element(p: int, k: int) -> int:
    """Some element of exact order k in F_p^* (k | p-1, k prime)."""
    g = 2
    while True:
        x = pow(g, (p - 1) // k, p)
        if x != 1:
            return x
        g += 1


def energy(p: int, k: int, s: int, idx, w) -> int:
    a = order_k_element(p, k)
    H = np.empty(k, dtype=np.int64)
    v = 1
    for j in range(k):
        H[j] = v
        v = v * a % p
    Hi = np.array([pow(int(h), p - 2, p) for h in H], dtype=np.int64)
    X = H[idx].sum(axis=1) % p
    Y = Hi[idx].sum(axis=1) % p
    key = X * p + Y
    o = np.argsort(key, kind="stable")
    key = key[o]
    ww = w[o]
    # group sums of weights per distinct key, then sum of squares
    bnd = np.flatnonzero(np.diff(key)) + 1
    starts = np.concatenate(([0], bnd))
    ends = np.concatenate((bnd, [len(key)]))
    cs = np.concatenate(([0], np.cumsum(ww.astype(object))))
    tot = 0
    for st, en in zip(starts, ends):
        g = cs[en] - cs[st]
        tot += g * g
    return int(tot)


def scan(k: int, s: int, pmax: int):
    idx, w = multiset_table(k, s)
    P = pair_count(s, k)
    bad = []
    t0 = time.time()
    n = 0
    npr = 0
    while True:
        n += 1
        p = k * n + 1
        if p > pmax:
            break
        if not is_prime(p):
            continue
        npr += 1
        E = energy(p, k, s, idx, w)
        if E > P:
            bad.append((p, E - P))
        elif E < P:
            raise AssertionError(f"E<PAIR k={k} s={s} p={p}")
    return {"k": k, "s": s, "PAIR": P, "pmax": pmax, "primes": npr,
            "n_bad": len(bad), "P_star": (max(b[0] for b in bad) if bad else None),
            "bad_tail": bad[-15:], "secs": round(time.time() - t0, 1),
            "censored": bool(bad) and max(b[0] for b in bad) > 0.6 * pmax,
            "table_rows": int(len(w))}


def main():
    jobs = [(11, 3, 3_000_000), (11, 4, 2_000_000), (11, 5, 1_000_000),
            (11, 6, 400_000), (11, 7, 200_000),
            (13, 3, 3_000_000), (13, 4, 2_000_000), (13, 5, 600_000),
            (13, 6, 300_000),
            (17, 3, 2_000_000), (17, 4, 500_000),
            (19, 3, 2_000_000), (19, 4, 400_000),
            (23, 3, 1_000_000), (23, 4, 200_000),
            (29, 3, 600_000), (31, 3, 600_000), (37, 3, 400_000),
            (41, 3, 400_000), (43, 3, 300_000), (47, 3, 300_000),
            (53, 3, 200_000), (59, 3, 200_000), (61, 3, 200_000)]
    rows = []
    print(f"{'k':>4} {'s':>2} {'rows':>7} {'#bad':>5} {'P*':>9} "
          f"{'log_k P*':>9} {'cens':>5} {'pmax':>9} {'secs':>7}")
    for k, s, pmax in jobs:
        r = scan(k, s, pmax)
        rows.append(r)
        Ps = r["P_star"]
        lk = math.log(Ps) / math.log(k) if Ps else float("nan")
        r["log_k_Pstar"] = lk
        print(f"{k:>4} {s:>2} {r['table_rows']:>7} {r['n_bad']:>5} "
              f"{str(Ps):>9} {lk:>9.3f} {str(r['censored']):>5} "
              f"{pmax:>9} {r['secs']:>7}")
        sys.stdout.flush()
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r71", "Pstar_prime_k.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump({"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
                   "rows": rows}, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    print("\nsummary: log_k P* by (k,s)")
    for r in rows:
        print(f"  k={r['k']:>3} s={r['s']}: P*={str(r['P_star']):>9} "
              f"log_k P*={r['log_k_Pstar']:.3f} censored={r['censored']} "
              f"bad_tail={r['bad_tail'][-4:]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
