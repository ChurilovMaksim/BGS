"""Wave 24, task 4 (follow-up): full product deficits for the (1,2) twin
identity at qt = 289 and 332929.

Finding: for orbit reps (a6, a7) of the 81-split fiber, the exact
identity sorted CRT(p0, a6, t) == sorted CRT(p0, a7, t) holds for ALL
supported p0 and ALL t at qt in {289, 332929} (verified exactly on
random samples; the mod-P sweep found literally every combo a
survivor: 11232/11232 at qt=289, 12984192/12984192 at qt=332929).
Hence EVERY product (f2048 x split81 x f_qt) at those qt contains
mixing fibers. This script computes every such product's deficit
exactly (same method as wave24_m48_fragments.py: mod-(P1,P2) grouping
+ 81-orbit-count deficit with exactly-120-degree phases).

Pairs: 39 supported 2048-fibers x (27 + 10693) qt-fibers = 418080.
Resumable: results append to JSONL; already-done pairs are skipped
on restart. Progress + running total rewritten to the summary file
every 1000 pairs. Repository untouched; no Lean build.
"""
import json, os, sys
import numpy as np
sys.path.insert(0, ".")
from wave16_d1a_targeted import Dm, snf_kernel, group_ids

m = 48
D = Dm(m)
P1, P2 = 1_000_000_007, 998244353
OUT = "wave24_m48_fragments12.jsonl"
SUM = "wave24_m48_fragments12_summary.json"

def KqP(q, P):
    dq = D // q
    return ((dq * pow(dq % q, -1, q)) % D) % P

d81 = np.load("wave24_comp_81.npz")
K81, fib81, gam81 = d81["K"], d81["fib"], d81["gam"]
d2048 = np.load("wave24_comp_2048.npz")
K2048, fib2048, sup2048 = d2048["K"], d2048["fib"], d2048["sup"]
gf = np.empty(int(gam81.max()) + 1, dtype=np.int64)
gf[gam81] = fib81
opf = np.bincount(gf, minlength=int(fib81.max()) + 1)
f81 = sorted(np.where(opf > 1)[0].tolist())[0]
idx81 = np.where(fib81 == f81)[0]
gam = gam81[idx81]
orbs81 = sorted(set(gam.tolist()))
a_orb = np.array([orbs81.index(int(gam[k])) for k in range(len(idx81))],
                 dtype=np.int64)
a_pts = K81[idx81]
sup2048_fibs = sorted(set(fib2048[sup2048].tolist()))

# Pair list (shuffled with fixed seed so early output is a fair sample).
rng = np.random.default_rng(12345)
pairs = []
for qt in (289, 332929):
    K = snf_kernel(m, qt)
    fib = group_ids(np.sort(K, axis=1))
    fqt_list = sorted(set(fib.tolist()))
    np.savez(f"wave24_qt_{qt}.npz", K=K, fib=fib)
    for f2048 in sup2048_fibs:
        for fqt in fqt_list:
            pairs.append((f2048, qt, fqt))
    del K, fib
rng.shuffle(pairs)
print(f"total pairs: {len(pairs)}", flush=True)

done = set()
if os.path.exists(OUT):
    with open(OUT) as fh:
        for line in fh:
            r = json.loads(line)
            done.add((r["f2048"], r["qt"], r["fqt"]))
print(f"already done: {len(done)}", flush=True)
tot_def = 0
tot_groups = 0
tot_mixing = 0
# Recompute running totals from existing JSONL.
if os.path.exists(OUT):
    with open(OUT) as fh:
        for line in fh:
            r = json.loads(line)
            tot_def += r["deficit"]
            tot_groups += r["groups"]
            tot_mixing += r["mixing"]
out_fh = open(OUT, "a")
n_done = len(done)
# Cache qt arrays ONCE (loading the 332929 npz per pair cost ~200 ms/pair).
qt_cache = {}
for qt in (289, 332929):
    d = np.load(f"wave24_qt_{qt}.npz")
    qt_cache[qt] = (d["K"], d["fib"])
for (f2048, qt, fqt) in pairs:
    if (f2048, qt, fqt) in done:
        continue
    Kqt, fibqt = qt_cache[qt]
    p_pts = K2048[np.where(fib2048 == f2048)[0]]
    s_pts = Kqt[np.where(fibqt == fqt)[0]]
    n_p, n_a, n_s = len(p_pts), len(a_pts), len(s_pts)
    V1 = (KqP(2048, P1) * p_pts[:, None, None, :]
          + KqP(81, P1) * a_pts[None, :, None, :]
          + KqP(qt, P1) * s_pts[None, None, :, :]) % P1
    V2 = (KqP(2048, P2) * p_pts[:, None, None, :]
          + KqP(81, P2) * a_pts[None, :, None, :]
          + KqP(qt, P2) * s_pts[None, None, :, :]) % P2
    S1 = np.sort(V1, axis=3).reshape(-1, m)
    S2 = np.sort(V2, axis=3).reshape(-1, m)
    joint = np.concatenate([S1, S2], axis=1)
    _, inv = np.unique(joint, axis=0, return_inverse=True)
    inv = inv.reshape(-1)
    a_grid = np.tile(a_orb[None, :, None], (n_p, 1, n_s)).reshape(-1)
    pair_def = 0
    pair_groups = int(inv.max()) + 1
    pair_mixing = 0
    for g in range(pair_groups):
        sel = (inv == g)
        cnt = np.bincount(a_grid[sel], minlength=3)
        if (cnt > 0).sum() >= 2:
            pair_def += int(3 * (cnt[0] * cnt[1] + cnt[0] * cnt[2]
                                + cnt[1] * cnt[2]))
            pair_mixing += 1
    out_fh.write(json.dumps({"f2048": int(f2048), "qt": int(qt), "fqt": int(fqt),
                             "n_p": n_p, "n_s": n_s, "groups": pair_groups,
                             "mixing": pair_mixing, "deficit": pair_def}) + "\n")
    tot_def += pair_def
    tot_groups += pair_groups
    tot_mixing += pair_mixing
    n_done += 1
    if n_done % 1000 == 0:
        out_fh.flush()
        with open(SUM, "w") as sf:
            json.dump({"done": n_done, "total_pairs": len(pairs),
                       "total_deficit": tot_def, "total_groups": tot_groups,
                       "total_mixing": tot_mixing}, sf)
        print(f"progress {n_done}/{len(pairs)} deficit={tot_def}", flush=True)
out_fh.flush()
with open(SUM, "w") as sf:
    json.dump({"done": n_done, "total_pairs": len(pairs),
               "total_deficit": tot_def, "total_groups": tot_groups,
               "total_mixing": tot_mixing}, sf)
print(f"DONE: {n_done}/{len(pairs)} deficit={tot_def} groups={tot_groups} "
      f"mixing={tot_mixing}", flush=True)
