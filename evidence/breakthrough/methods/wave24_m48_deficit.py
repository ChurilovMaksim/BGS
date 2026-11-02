"""Wave 24, task 4: cancellation deficit Delta at m=48.

Mirrors wave-22 task 2 (m=36) methodology. New facts at m=48 (from
wave24_comp_analysis): D = 2^11*3^4*5^2*7^2*11^2*17^2*97^2*577^2*1153^2*
13729^2, prime powers [25,49,81,121,289,2048,9409,332929,1329409,
188485441]; split component fibers ONLY at q=81 (36 pts, 3 orbits of
12, fully supported) among the 9 enumerable components; q=2048 has 10
split fibers, all off-support, and 39 supported single-orbit fibers
(sizes 1x4, 2x14, 4x18, 8x3; 128 points); no partial fibers anywhere
enumerated; the q=188485441 component is handled by the C++ streaming
enumerator (wave24_bigcomp.cpp), not here. Zero is supported at 2048.
D ~ 5.6e36 > 2^63, so global CRT values are Python object ints.
Repository untouched; no Lean build.
"""
import collections, json, sys
import numpy as np
sys.path.insert(0, ".")
from wave16_d1a_targeted import (Dm, snf_kernel, sample_kernel_points,
                                 torsion_data, comp_supported,
                                 gamma_perms, lex_canon, group_ids)

m = 48
D = Dm(m)
QS = [25, 49, 81, 121, 289, 2048, 9409, 332929, 1329409, 188485441]
assert D == 25 * 49 * 81 * 121 * 289 * 2048 * 9409 * 332929 * 1329409 * 188485441, D
Z, Qmod = torsion_data(m, D)
perms = gamma_perms(m)
print(f"m={m} D={D} |V4|={len(Z)} nperms={len(perms)}", flush=True)

# --- adjugate first row via recurrence solve (X circulant, X*H = D*I) ---
A = [(1, 0), (0, 1)]
for i in range(1, m - 1):
    (a0, b0), (a1, b1) = A[i - 1], A[i]
    A.append((6 * a1 - a0, 6 * b1 - b0))
A47, B47 = A[47]
A46, B46 = A[46]
c11 = 6 * A47 - A46 - 1
c12 = 6 * B47 - B46
c21 = 6 - A47
c22 = -1 - B47
det = c11 * c22 - c12 * c21
assert det != 0
assert (-c12 * D) % det == 0 and (c11 * D) % det == 0
x0 = (-c12 * D) // det
x1 = (c11 * D) // det
xrow = [a * x0 + b * x1 for (a, b) in A]
assert (6 * xrow[0] - xrow[1] - xrow[47]) == D
assert all((6 * xrow[i] - xrow[i - 1] - xrow[(i + 1) % m]) == 0
           for i in range(1, m))
np.save("wave24_Xrow48.npy", np.array(xrow, dtype=object), allow_pickle=True)
print(f"xrow solved; x0={x0} x1={x1}", flush=True)
Xq = {}
for q in QS:
    if q == 188485441:
        continue
    Xq[q] = np.array([[xrow[(j - i) % m] % q for j in range(m)]
                      for i in range(m)], dtype=np.int64)

def H_np(v):
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)

def H_py(v):
    v = np.asarray(v, dtype=object)
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)

def crt_py(comp_pts):
    n = len(next(iter(comp_pts.values())))
    out = np.zeros((n, m), dtype=object)
    for q, pts in comp_pts.items():
        dq = D // q
        K = (dq * pow(dq % q, -1, q)) % D
        out = out + K * np.asarray(pts, dtype=object)
    return out % D

# --- component data for 81 and 2048 (saved by census) ---
comp = {}
for q in (81, 2048):
    d = np.load(f"wave24_comp_{q}.npz")
    K = d["K"]
    HK = H_np(K)
    assert np.all(HK % q == 0)
    W = HK // q
    WX = (W @ Xq[q]) % q
    Qv = np.einsum("ij,ij->i", WX, W) % q
    Pv = (WX @ W.T) % q
    comp[q] = {"K": K, "W": W, "WX": WX, "Q": Qv, "P": Pv,
               "lookup": {tuple(int(v) for v in row): i for i, row in enumerate(K)},
               "fib": d["fib"], "gam": d["gam"], "sup": d["sup"]}
    print(f"q={q}: pts={len(K)} fibers={int(d['fib'].max())+1} "
          f"supp_pts={int(d['sup'].sum())}", flush=True)

# --- correction modes (wave-16 test) for 81, 2048 ---
rng = np.random.default_rng(3)
rand_pts = {}
for q in QS:
    if q in comp:
        sel = rng.integers(0, len(comp[q]["K"]), size=400)
        rand_pts[q] = comp[q]["K"][sel]
    else:
        rand_pts[q] = sample_kernel_points(m, q, 400, rng)
rand_glob = crt_py(rand_pts)
wrand = H_py(rand_glob) // D
assert np.all(H_py(rand_glob) % D == 0)
for q in (81, 2048):
    c = comp[q]
    wr = np.asarray(wrand % q, dtype=np.int64)
    Wr = (wr @ Xq[q]) % q
    Qr = np.einsum("ij,ij->i", Wr, wr) % q
    u = (D // q) % q
    inv_u2 = pow((u * u) % q, -1, q)
    idx = np.array([c["lookup"][tuple(int(v) for v in row)] for row in (rand_glob % q)])
    raw_bad = corr_bad = 0
    for _ in range(300):
        i = int(rng.integers(0, len(rand_glob))); j = int(rng.integers(0, len(rand_glob)))
        tg = int((2 * Qr[i] - int(Wr[i] @ wr[j])) % q)
        tc = int((2 * c["Q"][idx[i]] - int(c["WX"][idx[i]] @ c["W"][idx[j]])) % q)
        if tc != tg: raw_bad += 1
        if (inv_u2 * tc) % q != tg: corr_bad += 1
    c["corr"] = (raw_bad > 0 and corr_bad == 0)
    print(f"  corr q={q}: raw_bad={raw_bad} corr_bad={corr_bad} -> corr={c['corr']}", flush=True)
    assert not (raw_bad > 0 and corr_bad > 0), "no mode fits"

def S_vec(q):
    c = comp[q]
    ci = pow(D // q, -1, q)
    u = (D // q) % q
    inv_u2 = pow((u * u) % q, -1, q)
    T = (2 * c["Q"][:, None] - c["P"]) % q
    if c["corr"]:
        T = (inv_u2 * T) % q
    E = np.exp(2j * np.pi * ((ci * T) % q) / q)
    return E.sum(axis=0)

S81 = S_vec(81)
S2048 = S_vec(2048)
print("S81/S2048 computed", flush=True)

# --- 81 split fiber: phases and |S| on orbits ---
c81 = comp[81]
gf = np.empty(int(c81["gam"].max()) + 1, dtype=np.int64)
gf[c81["gam"]] = c81["fib"]
opf = np.bincount(gf, minlength=int(c81["fib"].max()) + 1)
split81 = sorted(np.where(opf > 1)[0].tolist())
print(f"81 split fibers: {split81}", flush=True)
split_idx = {}
for f in split81:
    idx = np.where(c81["fib"] == f)[0]
    split_idx[f] = idx
    assert int(c81["sup"][idx].sum()) == len(idx), "split fiber not fully supported"
    for g in sorted(set(c81["gam"][idx].tolist())):
        oo = idx[c81["gam"][idx] == g]
        vals = S81[oo]
        print(f"  81 fiber {f} orbit {g}: size={len(oo)} |S|={np.abs(vals[0]):.6f} "
              f"phase={np.angle(vals[0]):.6f} spread={np.abs(vals-vals[0]).max():.2e}", flush=True)

# --- supported 2048 fibers ---
c2048 = comp[2048]
sup2048_fibs = sorted(set(c2048["fib"][c2048["sup"]].tolist()))
print(f"supported 2048-fibers: {len(sup2048_fibs)} sizes="
      f"{[int((c2048['fib']==f).sum()) for f in sup2048_fibs]}", flush=True)
for f in sup2048_fibs:
    idx = np.where(c2048["fib"] == f)[0]
    assert len(set(c2048["gam"][idx].tolist())) == 1, "supported 2048-fiber not single orbit"
    vals = S2048[idx]
    print(f"  2048 fiber {f}: size={len(idx)} |S2048|={np.abs(vals[0]):.6f} "
          f"phase={np.angle(vals[0]):.6f} spread={np.abs(vals-vals[0]).max():.2e}", flush=True)

zero = {}
for q in QS:
    if q in comp:
        zidx = comp[q]["lookup"][(0,) * m]
        zero[q] = comp[q]["K"][zidx]
    else:
        zero[q] = np.zeros(m, dtype=np.int64)
    print(f"  zero q={q} (kernel point by construction)", flush=True)

# --- global helpers (object ints) ---
def canon_py(rows, perms):
    out = []
    for row in rows:
        best = None
        for p in perms:
            cand = tuple(row[p[j]] for j in range(m))
            if best is None or cand < best:
                best = cand
        out.append(best)
    return out

def fiber_deficit(glob_rows):
    can = canon_py(glob_rows, [tuple(p) for p in perms])
    gam_ids = {}
    for i, c in enumerate(can):
        gam_ids.setdefault(c, []).append(i)
    i81 = [comp[81]["lookup"][tuple(int(v) % 81 for v in row)] for row in glob_rows]
    i2048 = [comp[2048]["lookup"][tuple(int(v) % 2048 for v in row)] for row in glob_rows]
    rel = np.array([S81[a] * S2048[b] for a, b in zip(i81, i2048)])
    orbits = []
    for g, oo in gam_ids.items():
        vals = rel[oo]
        dev = float(np.abs(vals - vals[0]).max())
        assert dev < 1e-9, f"rel not constant on orbit! dev={dev}"
        orbits.append({"size": len(oo), "phase": float(np.angle(vals[0])),
                       "abs": float(np.abs(vals[0]))})
    F = len(glob_rows)
    coh = abs(sum(o["size"] * np.exp(1j * o["phase"]) for o in orbits)) ** 2
    return {"size": F, "n_orbits": len(orbits), "orbits": orbits,
            "coherent": float(coh), "deficit": float(F * F - coh)}

# --- (a) rigid combos: supported 2048-fiber x 81-split x zeros ---
rigid = []
for f2048 in sup2048_fibs:
    idx2048 = np.where(c2048["fib"] == f2048)[0]
    for f81 in split81:
        idx81 = split_idx[f81]
        combos = {}
        for p in idx2048:
            for a in idx81:
                cp = {}
                for q in QS:
                    if q == 2048: cp[q] = c2048["K"][p:p+1]
                    elif q == 81: cp[q] = c81["K"][a:a+1]
                    else: cp[q] = zero[q][None, :]
                combos[tuple(int(v) for v in crt_py(cp)[0].tolist())] = None
        pts = list(combos.keys())
        groups = collections.defaultdict(list)
        for row in pts:
            groups[tuple(sorted(row))].append(row)
        for key, sub in groups.items():
            fd = fiber_deficit(sub)
            fd["f2048"] = int(f2048); fd["f81"] = int(f81)
            fd["n2048"] = int(len(idx2048))
            rigid.append(fd)
            print(f"  rigid f2048={f2048} (n2048={len(idx2048)}) f81={f81}: "
                  f"global fiber size={fd['size']} orbits={fd['n_orbits']} "
                  f"orbit_sizes={[o['size'] for o in fd['orbits']]} "
                  f"phases={[round(o['phase'],4) for o in fd['orbits']]} "
                  f"deficit={fd['deficit']:.6f}", flush=True)
tot_rigid_def = sum(r["deficit"] for r in rigid)
print(f"(a) rigid global fibers: {len(rigid)} total deficit={tot_rigid_def:.6f}", flush=True)

# --- (b) multiset-mod-P filter rigidity sweep (t != 0 at one other component) ---
# qt OUTER so each component kernel array is built once. Big component:
# one fixed 200k sample, saved for exact rechecks.
P1, P2 = 1_000_000_007, 998244353
KqP = {}
for q in QS:
    dq = D // q
    KqP[q] = (((dq * pow(dq % q, -1, q)) % D) % P1,
              ((dq * pow(dq % q, -1, q)) % D) % P2)
other_qs = [q for q in QS if q not in (2048, 81)]
big_sample = sample_kernel_points(m, 188485441, 200000, np.random.default_rng(11))
np.savez("wave24_bigcomp_sample.npz", T=big_sample)
print(f"  big-component sweep sample: {len(big_sample)} pts", flush=True)
survivors = []
for qt in other_qs:
    if qt == 188485441:
        T = big_sample
    else:
        T = snf_kernel(m, qt)
    nz = ~np.all(T == 0, axis=1)
    Tnz = T[nz]
    nz_idx = np.where(nz)[0]
    print(f"  sweep qt={qt}: {len(Tnz)} nonzero pts", flush=True)
    for f2048 in sup2048_fibs:
        p0 = c2048["K"][np.where(c2048["fib"] == f2048)[0][0]]
        for f81 in split81:
            idx81 = split_idx[f81]
            gam81 = c81["gam"][idx81]
            orbs = sorted(set(gam81.tolist()))
            a0 = c81["K"][idx81[gam81 == orbs[0]][0]]
            a1 = c81["K"][idx81[gam81 == orbs[1]][0]]
            for st in range(0, len(Tnz), 20000):
                ch = Tnz[st:st+20000]
                hit = np.ones(len(ch), dtype=bool)
                for pi, P in enumerate((P1, P2)):
                    if not hit.any():
                        break
                    base = (KqP[2048][pi] * (p0 % P)) % P
                    A0 = (KqP[81][pi] * (a0 % P)) % P
                    A1 = (KqP[81][pi] * (a1 % P)) % P
                    V0 = (base[None, :] + A0[None, :] + (KqP[qt][pi] * (ch % P)) % P) % P
                    V1 = (base[None, :] + A1[None, :] + (KqP[qt][pi] * (ch % P)) % P) % P
                    hit &= np.all(np.sort(V0, axis=1) == np.sort(V1, axis=1), axis=1)
                for h in np.where(hit)[0]:
                    survivors.append({"f2048": int(f2048), "f81": int(f81),
                                      "qt": int(qt), "t_idx": int(nz_idx[st + h])})
    if qt != 188485441:
        del T
    print(f"  sweep done qt={qt} survivors so far={len(survivors)}", flush=True)
print(f"(b) multiset-mod-P sweep survivors={len(survivors)}", flush=True)
with open("wave24_sweep_survivors.json", "w") as fh:
    json.dump(survivors, fh)

# Exact recheck. Cheap exact 2-rep pre-check first: the two orbit reps
# combined with (p0, t) must share one EXACT multiset; only survivors of
# that get the full combo recheck (and a deficit computation if rigid).
exact_extra = []
extra_deficits = []
n_killed = 0
n_2rep_killed = 0
# Cache kernel arrays for qts that actually have survivors (289, 332929).
Tcache = {}
for qt_needed in sorted(set(sv["qt"] for sv in survivors)):
    if qt_needed != 188485441:
        Tcache[qt_needed] = snf_kernel(m, qt_needed)
        print(f"  recheck cache qt={qt_needed}: {len(Tcache[qt_needed])} pts", flush=True)
for si, sv in enumerate(survivors):
    qt, ti = sv["qt"], sv["t_idx"]
    if qt == 188485441:
        t = big_sample[ti]
    else:
        t = Tcache[qt][ti]
    f2048, f81 = sv["f2048"], sv["f81"]
    idx2048 = np.where(c2048["fib"] == f2048)[0]
    idx81 = split_idx[f81]
    gam81 = c81["gam"][idx81]
    orbs = sorted(set(gam81.tolist()))
    a0 = c81["K"][idx81[gam81 == orbs[0]][0]]
    a1 = c81["K"][idx81[gam81 == orbs[1]][0]]
    p0 = c2048["K"][idx2048[0]]
    cp0 = {q: (c2048["K"][idx2048[0]][None, :] if q == 2048 else
               c81["K"][idx81[gam81 == orbs[0]][0]][None, :] if q == 81 else
               t[None, :] if q == qt else zero[q][None, :]) for q in QS}
    cp1 = {q: (c2048["K"][idx2048[0]][None, :] if q == 2048 else
               c81["K"][idx81[gam81 == orbs[1]][0]][None, :] if q == 81 else
               t[None, :] if q == qt else zero[q][None, :]) for q in QS}
    v0 = tuple(int(v) for v in crt_py(cp0)[0].tolist())
    v1 = tuple(int(v) for v in crt_py(cp1)[0].tolist())
    if tuple(sorted(v0)) != tuple(sorted(v1)):
        n_2rep_killed += 1
        n_killed += 1
        if (si + 1) % 10000 == 0:
            print(f"  recheck {si+1}/{len(survivors)}: 2rep-killed={n_2rep_killed} "
                  f"extra={len(exact_extra)}", flush=True)
        continue
    combos = {}
    for p in idx2048:
        for a in idx81:
            cp = {}
            for q in QS:
                if q == 2048: cp[q] = c2048["K"][p:p+1]
                elif q == 81: cp[q] = c81["K"][a:a+1]
                elif q == qt: cp[q] = t[None, :]
                else: cp[q] = zero[q][None, :]
            combos[tuple(int(v) for v in crt_py(cp)[0].tolist())] = None
    ms = set(tuple(sorted(row)) for row in combos.keys())
    if len(ms) == 1:
        fd = fiber_deficit(list(combos.keys()))
        fd.update(sv)
        extra_deficits.append(fd)
        print(f"  !! EXACT RIGID EXTRA: {sv} size={fd['size']} orbits={fd['n_orbits']} "
              f"deficit={fd['deficit']:.6f}", flush=True)
        exact_extra.append(sv)
    else:
        n_killed += 1
    if (si + 1) % 10000 == 0:
        print(f"  recheck {si+1}/{len(survivors)}: 2rep-killed={n_2rep_killed} "
              f"extra={len(exact_extra)}", flush=True)
print(f"(b) exact extra rigid families: {len(exact_extra)} (2rep-killed: {n_2rep_killed}, "
      f"total killed: {n_killed})", flush=True)

# --- (c) generic sampling via exact (v0,v1) fiber enumeration ---
def enumerate_fiber(xi):
    Mx = collections.Counter(int(v) for v in xi)
    fcomp = {}
    for q in QS:
        fcomp[q] = collections.Counter(int(v) % q for v in xi)
    out = []
    for v0 in list(Mx.keys()):
        M1 = Mx.copy(); M1[v0] -= 1
        if M1[v0] == 0: del M1[v0]
        for v1 in list(M1.keys()):
            seqs = {}; ok = True
            for q in QS:
                y = [v0 % q, v1 % q]
                for i in range(1, m - 1):
                    y.append((6 * y[i] - y[i - 1]) % q)
                ym = (6 * y[m - 1] - y[m - 2]) % q
                ym1 = (6 * ym - y[m - 1]) % q
                if ym != y[0] or ym1 != y[1]:
                    ok = False; break
                seqs[q] = y[:m]
                if collections.Counter(y[:m]) != fcomp[q]:
                    ok = False; break
            if not ok: continue
            cp = {q: np.array(seqs[q], dtype=np.int64)[None, :] for q in QS}
            g = crt_py(cp)[0]
            if collections.Counter(int(v) for v in g) != Mx: continue
            out.append(tuple(int(v) for v in g))
    return out

rng3 = np.random.default_rng(9)
gen_results = []
for trial in range(20):
    cp = {}
    for q in QS:
        if q == 81:
            f81 = split81[rng3.integers(0, len(split81))]
            idx = split_idx[f81]
            cp[q] = c81["K"][idx[rng3.integers(0, len(idx))]][None, :]
        elif q == 2048:
            f2048 = sup2048_fibs[rng3.integers(0, len(sup2048_fibs))]
            idx = np.where(c2048["fib"] == f2048)[0]
            cp[q] = c2048["K"][idx[rng3.integers(0, len(idx))]][None, :]
        else:
            # all points supported at every other (odd) component per census
            cp[q] = sample_kernel_points(m, q, 1, rng3)
    xi = crt_py(cp)[0]
    fib = enumerate_fiber(xi)
    assert len(fib) >= 1
    fd = fiber_deficit(fib)
    g81 = set(c81["gam"][[c81["lookup"][tuple(int(v) % 81 for v in row)] for row in fib]].tolist())
    gen_results.append({"size": fd["size"], "n_orbits": fd["n_orbits"],
                        "deficit": fd["deficit"], "n_81orbits": len(g81)})
    print(f"  generic trial {trial}: fiber size={fd['size']} orbits={fd['n_orbits']} "
          f"81-orbits spanned={len(g81)} deficit={fd['deficit']:.6f}", flush=True)

# --- cross-check: (v0,v1) enumeration of one rigid fiber point ---
if rigid:
    f2048_0, f81_0 = rigid[0]["f2048"], rigid[0]["f81"]
    idx2048 = np.where(c2048["fib"] == f2048_0)[0]
    idx81 = split_idx[f81_0]
    cp = {}
    for q in QS:
        if q == 2048: cp[q] = c2048["K"][idx2048[0]][None, :]
        elif q == 81: cp[q] = c81["K"][idx81[0]][None, :]
        else: cp[q] = zero[q][None, :]
    xi = crt_py(cp)[0]
    fib = enumerate_fiber(xi)
    print(f"cross-check rigid fiber (f2048={f2048_0}, f81={f81_0}): enumerated size="
          f"{len(fib)} vs rigid size={rigid[0]['size']}", flush=True)

tot_extra_def = sum(fd["deficit"] for fd in extra_deficits)
tot_def = tot_rigid_def + tot_extra_def
supp48 = D // 16
out = {"m": m, "D": D, "supp": supp48,
       "rigid_fibers": rigid, "total_rigid_deficit": float(tot_rigid_def),
       "extra_rigid_fibers": extra_deficits, "total_extra_deficit": float(tot_extra_def),
       "total_deficit": float(tot_def),
       "Delta48": float(tot_def / supp48),
       "sweep_survivors": survivors, "exact_extra_rigid": exact_extra,
       "generic": gen_results}
with open("wave24_m48_deficit.json", "w") as fh:
    json.dump(out, fh, indent=1, default=str)
print(f"TOTAL: rigid deficit={tot_rigid_def:.6f} extra deficit={tot_extra_def:.6f} "
      f"Delta(48)={tot_def / supp48:.6e}", flush=True)
