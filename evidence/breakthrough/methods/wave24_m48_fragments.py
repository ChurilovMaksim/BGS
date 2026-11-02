"""Wave 24, task 4 (follow-up): exact fragment deficits for sweep survivors.

Background: the multiset-mod-P sweep in wave24_m48_deficit.py found
42048 slice survivors (qt=289: 576, qt=332929: 41472) where the two
orbit reps (p0, a0, t) and (p0, a1, t) share one EXACT global multiset,
but no slice forms a single rigid fiber. A slice survivor witnesses a
mixing global fiber inside the FULL product (f2048 x split81 x f_qt),
because a global fiber's component fibers are fixed (global multiset
determines component multisets). This script enumerates those full
products for every DISTINCT survivor pair (f2048, fiber(t)) and sums
their exact deficits.

Deficit per global fiber via 81-orbit counts only: within a product,
S_2048 is constant on the single-orbit f2048, S_qt constant on the
single-orbit f_qt (0 splits at qt=289/332929), other components are
zero (common factors), so a point's relative phase depends only on
its 81-orbit; S_81 phases are exactly 120 degrees apart, hence
deficit = 3*(n0*n1 + n0*n2 + n1*n2) with nO = #points in 81-orbit O.

Grouping is by sorted multiset mod P1 AND P2 (two independent ~1e9
primes, as in prior waves); grouping mod P never splits an exact
fiber, and a mod-(P1,P2) collision merging distinct exact fibers is
negligible for structured data. Repository untouched; no Lean build.
"""
import json, sys
import numpy as np
sys.path.insert(0, ".")
from wave16_d1a_targeted import Dm, snf_kernel, group_ids

m = 48
D = Dm(m)
P1, P2 = 1_000_000_007, 998244353

def KqP(q, P):
    dq = D // q
    return ((dq * pow(dq % q, -1, q)) % D) % P

# --- S_81 phases (corr=True verified in wave24_m48_deficit run) ---
d81 = np.load("wave24_comp_81.npz")
K81, fib81, gam81 = d81["K"], d81["fib"], d81["gam"]
d2048 = np.load("wave24_comp_2048.npz")
K2048, fib2048 = d2048["K"], d2048["fib"]
# Xq for 81 from wave24_Xrow48.npy
xrow = np.load("wave24_Xrow48.npy", allow_pickle=True)
xrow = [int(v) for v in xrow]
X81 = np.array([[xrow[(j - i) % m] % 81 for j in range(m)]
                for i in range(m)], dtype=np.int64)
HK = (6 * K81 - np.roll(K81, 1, axis=1) - np.roll(K81, -1, axis=1))
assert np.all(HK % 81 == 0)
W = HK // 81
WX = (W @ X81) % 81
Qv = np.einsum("ij,ij->i", WX, W) % 81
Pv = (WX @ W.T) % 81
ci = pow(D // 81, -1, 81)
u = (D // 81) % 81
inv_u2 = pow((u * u) % 81, -1, 81)
T = (inv_u2 * ((2 * Qv[:, None] - Pv) % 81)) % 81
E = np.exp(2j * np.pi * ((ci * T) % 81) / 81)
S81 = E.sum(axis=0)
gf = np.empty(int(gam81.max()) + 1, dtype=np.int64)
gf[gam81] = fib81
opf = np.bincount(gf, minlength=int(fib81.max()) + 1)
split81 = sorted(np.where(opf > 1)[0].tolist())
assert len(split81) == 1
f81 = split81[0]
idx81 = np.where(fib81 == f81)[0]
orbs81 = sorted(set(gam81[idx81].tolist()))
assert len(orbs81) == 3
phases = {}
for g in orbs81:
    oo = idx81[gam81[idx81] == g]
    vals = S81[oo]
    assert np.abs(vals - vals[0]).max() < 1e-9
    assert abs(np.abs(vals[0]) - 9) < 1e-9
    phases[g] = float(np.angle(vals[0]))
ph = sorted(phases.values())
d01 = (ph[1] - ph[0]) % (2 * np.pi)
d12 = (ph[2] - ph[1]) % (2 * np.pi)
print(f"S81 phases: {phases} diffs: {d01:.6f} {d12:.6f} (2pi/3 = {2*np.pi/3:.6f})",
      flush=True)
assert abs(d01 - 2 * np.pi / 3) < 1e-6 and abs(d12 - 2 * np.pi / 3) < 1e-6
a_orbit = {int(idx81[k]): orbs81.index(int(gam81[idx81[k]]))
           for k in range(len(idx81))}
a_pts = K81[idx81]
print(f"split81 fiber {f81}: {len(idx81)} pts, orbits {orbs81}", flush=True)

# --- distinct survivor pairs ---
sv = json.load(open("wave24_sweep_survivors.json"))
pairs = {}
for qt in (289, 332929):
    K = snf_kernel(m, qt)
    fib = group_ids(np.sort(K, axis=1))
    for s in sv:
        if s["qt"] == qt:
            pairs.setdefault((s["f2048"], qt, int(fib[s["t_idx"]])), None)
    pairs_qt = [(f, ff) for (f, q, ff) in pairs if q == qt]
    print(f"qt={qt}: {len(pairs_qt)} distinct pairs", flush=True)
    # store K/fib for the fragment loop
    if qt == 289:
        K289, fib289 = K, fib
    else:
        K332, fib332 = K, fib
print(f"total distinct pairs: {len(pairs)}", flush=True)

tot_frag_def = 0
tot_groups = 0
tot_mixing = 0
tot_points = 0
details = []
for (f2048, qt, fqt) in sorted(pairs.keys()):
    p_idx = np.where(fib2048 == f2048)[0]
    p_pts = K2048[p_idx]
    if qt == 289:
        s_idx = np.where(fib289 == fqt)[0]
        s_pts = K289[s_idx]
    else:
        s_idx = np.where(fib332 == fqt)[0]
        s_pts = K332[s_idx]
    n_p, n_a, n_s = len(p_pts), len(a_pts), len(s_pts)
    pair_def = 0
    pair_groups = 0
    pair_mixing = 0
    for P in (P1, P2):
        pass  # grouping uses both primes jointly below
    # Joint grouping key: sorted rows mod P1 and mod P2.
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
    # a-orbit index per combo, in the same flattened order (p, a, s)
    a_orb = np.array([a_orbit[int(idx81[k])] for k in range(n_a)], dtype=np.int64)
    a_grid = np.tile(a_orb[None, :, None], (n_p, 1, n_s)).reshape(-1)
    pair_groups = int(inv.max()) + 1
    for g in range(pair_groups):
        sel = (inv == g)
        n = int(sel.sum())
        cnt = np.bincount(a_grid[sel], minlength=3)
        if (cnt > 0).sum() >= 2:
            df = int(3 * (cnt[0] * cnt[1] + cnt[0] * cnt[2] + cnt[1] * cnt[2]))
            pair_def += df
            pair_mixing += 1
            details.append({"f2048": int(f2048), "qt": int(qt), "fqt": int(fqt),
                            "size": n, "orbit_counts": [int(c) for c in cnt],
                            "deficit": df})
    tot_frag_def += pair_def
    tot_groups += pair_groups
    tot_mixing += pair_mixing
    tot_points += n_p * n_a * n_s
    if (len(details) % 500 == 0) or pair_mixing > 0:
        pass
    print(f"  pair f2048={f2048} qt={qt} fqt={fqt}: pts={n_p*n_a*n_s} "
          f"groups={pair_groups} mixing={pair_mixing} deficit={pair_def}",
          flush=True) if pair_mixing > 0 else None
print(f"TOTAL: pairs={len(pairs)} product_points={tot_points} groups={tot_groups} "
      f"mixing_groups={tot_mixing} fragment_deficit={tot_frag_def}", flush=True)
with open("wave24_m48_fragments.json", "w") as fh:
    json.dump({"total_fragment_deficit": tot_frag_def, "total_groups": tot_groups,
               "total_mixing_groups": tot_mixing, "total_product_points": tot_points,
               "n_pairs": len(pairs), "mixing_details": details}, fh, indent=1)
print("WROTE wave24_m48_fragments.json", flush=True)
