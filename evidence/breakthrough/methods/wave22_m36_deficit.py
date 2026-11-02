"""Wave 22, task 2: cancellation deficit Delta at m=36.

Mirrors wave-20 task 3 (m=24) methodology. New facts at m=36 (from
wave22_comp_analysis): D=3629521257408972904004611200, prime powers
[25,49,121,128,729,5329,32041,38809,39601] (all enumerable), split
component fibers ONLY at q=729 (fiber 14: 324 pts, 9 orbits of 36;
fiber 15: 36 pts, 3 orbits of 12), both FULLY supported; zero
supported at every component except q=128; supported 128-fibers:
[1,13,21,28,37] sizes [2,2,1,2,1]; no partial fibers anywhere.

D ~ 3.6e27 > 2^63, so global CRT values are Python object ints
(int64 only for mod-q work). lex_canon is int64-only, so global
canonicalisation uses exact tuple min over dihedral perms.
Repository untouched; no Lean build.
"""
import collections, json, sys
import numpy as np
sys.path.insert(0, ".")
from wave16_d1a_targeted import (Dm, snf_kernel, sample_kernel_points,
                                 torsion_data, comp_supported,
                                 gamma_perms, lex_canon, group_ids)

m = 36
D = Dm(m)
QS = [25, 49, 121, 128, 729, 5329, 32041, 38809, 39601]
assert D == 25 * 49 * 121 * 128 * 729 * 5329 * 32041 * 38809 * 39601, D
Z, Qmod = torsion_data(m, D)
perms = gamma_perms(m)
print(f"m={m} D={D} |V4|={len(Z)} nperms={len(perms)}", flush=True)

xrow = np.load("wave22_Xrow36.npy", allow_pickle=True)
xrow = [int(v) for v in xrow]
Xq = {}
for q in QS:
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

# --- component data ---
comp = {}
for q in QS:
    K = snf_kernel(m, q)
    assert len(K) == q
    HK = H_np(K)
    assert np.all(HK % q == 0)
    W = HK // q
    WX = (W @ Xq[q]) % q
    Qv = np.einsum("ij,ij->i", WX, W) % q
    Pv = (WX @ W.T) % q if q <= 2000 else None  # full P is 8GB+ at q>=32041
    comp[q] = {"K": K, "W": W, "WX": WX, "Q": Qv, "P": Pv,
               "lookup": {tuple(int(v) for v in row): i for i, row in enumerate(K)}}
    fib = group_ids(np.sort(K, axis=1))
    canon = lex_canon(K, perms)
    gam = group_ids(canon)
    sup = comp_supported(K, Z, Qmod, q)
    comp[q].update({"fib": fib, "gam": gam, "sup": sup})
    print(f"q={q}: pts={len(K)} fibers={int(fib.max())+1} supp_pts={int(sup.sum())}", flush=True)

# --- correction modes (wave-16 test) ---
rng = np.random.default_rng(3)
rand_pts = {}
for q in QS:
    sel = rng.integers(0, len(comp[q]["K"]), size=400)
    rand_pts[q] = comp[q]["K"][sel]
rand_glob = crt_py(rand_pts)
wrand = H_py(rand_glob) // D
assert np.all(H_py(rand_glob) % D == 0)
for q in QS:
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

def S_point(q, j):
    """S_q at kernel point index j (no full P matrix needed)."""
    c = comp[q]
    ci = pow(D // q, -1, q)
    u = (D // q) % q
    inv_u2 = pow((u * u) % q, -1, q)
    Tcol = (2 * c["Q"] - c["WX"] @ c["W"][j]) % q
    if c["corr"]:
        Tcol = (inv_u2 * Tcol) % q
    return np.exp(2j * np.pi * ((ci * Tcol) % q) / q).sum()

S729 = S_vec(729)
S128 = S_vec(128)
print("S729/S128 computed", flush=True)

# --- 729 split fibers: phases and |S| on orbits ---
c729 = comp[729]
gf = np.empty(int(c729["gam"].max()) + 1, dtype=np.int64)
gf[c729["gam"]] = c729["fib"]
opf = np.bincount(gf, minlength=int(c729["fib"].max()) + 1)
split729 = sorted(np.where(opf > 1)[0].tolist())
print(f"729 split fibers: {split729}", flush=True)
split_idx = {}
for f in split729:
    idx = np.where(c729["fib"] == f)[0]
    split_idx[f] = idx
    assert int(c729["sup"][idx].sum()) == len(idx), "split fiber not fully supported"
    for g in sorted(set(c729["gam"][idx].tolist())):
        oo = idx[c729["gam"][idx] == g]
        vals = S729[oo]
        print(f"  729 fiber {f} orbit {g}: size={len(oo)} |S|={np.abs(vals[0]):.6f} "
              f"phase={np.angle(vals[0]):.6f} spread={np.abs(vals-vals[0]).max():.2e}", flush=True)

# --- supported 128 fibers ---
c128 = comp[128]
sup128_fibs = sorted(set(c128["fib"][c128["sup"]].tolist()))
print(f"supported 128-fibers: {sup128_fibs} sizes="
      f"{[int((c128['fib']==f).sum()) for f in sup128_fibs]}", flush=True)
for f in sup128_fibs:
    idx = np.where(c128["fib"] == f)[0]
    assert len(set(c128["gam"][idx].tolist())) == 1, "supported 128-fiber not single orbit"
    print(f"  128 fiber {f}: size={len(idx)} |S128|={np.abs(S128[idx[0]]):.6f} "
          f"phase={np.angle(S128[idx[0]]):.6f}", flush=True)

zero = {}
for q in QS:
    zidx = comp[q]["lookup"][(0,) * m]
    zero[q] = comp[q]["K"][zidx]
    print(f"  zero q={q} supported={bool(comp[q]['sup'][zidx])}", flush=True)
assert all(bool(comp[q]["sup"][comp[q]["lookup"][(0,)*m]]) for q in QS if q != 128)

# --- global helpers (object ints) ---
def canon_py(rows, perms):
    """rows: list of tuples (Python ints). Exact dihedral canonical form."""
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
    """glob_rows: list of tuples (global points of one fiber).
    rel = S729 * S128 (other components fixed within the fibers studied)."""
    can = canon_py(glob_rows, [tuple(p) for p in perms])
    gam_ids = {}
    for i, c in enumerate(can):
        gam_ids.setdefault(c, []).append(i)
    i729 = [comp[729]["lookup"][tuple(int(v) % 729 for v in row)] for row in glob_rows]
    i128 = [comp[128]["lookup"][tuple(int(v) % 128 for v in row)] for row in glob_rows]
    rel = np.array([S729[a] * S128[b] for a, b in zip(i729, i128)])
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

# --- (a) rigid combos: supported 128-fiber x 729-split x zeros ---
rigid = []
for f128 in sup128_fibs:
    idx128 = np.where(c128["fib"] == f128)[0]
    for f729 in split729:
        idx729 = split_idx[f729]
        combos = {}
        for p in idx128:
            for a in idx729:
                cp = {}
                for q in QS:
                    if q == 128: cp[q] = c128["K"][p:p+1]
                    elif q == 729: cp[q] = c729["K"][a:a+1]
                    else: cp[q] = zero[q][None, :]
                combos[tuple(int(v) for v in crt_py(cp)[0].tolist())] = None
        pts = list(combos.keys())
        groups = collections.defaultdict(list)
        for row in pts:
            groups[tuple(sorted(row))].append(row)
        for key, sub in groups.items():
            fd = fiber_deficit(sub)
            fd["f128"] = int(f128); fd["f729"] = int(f729)
            fd["n128"] = int(len(idx128))
            rigid.append(fd)
            print(f"  rigid f128={f128} (n128={len(idx128)}) f729={f729}: "
                  f"global fiber size={fd['size']} orbits={fd['n_orbits']} "
                  f"orbit_sizes={[o['size'] for o in fd['orbits']]} "
                  f"phases={[round(o['phase'],4) for o in fd['orbits']]} "
                  f"deficit={fd['deficit']:.6f}", flush=True)
tot_rigid_def = sum(r["deficit"] for r in rigid)
print(f"(a) rigid global fibers: {len(rigid)} total deficit={tot_rigid_def:.6f}", flush=True)

# --- (b) multiset-mod-P filter rigidity sweep (t != 0 at one other component) ---
# S2 alone is vacuous here (class-sum preservation makes S2 agree for ~69%
# of t); the sorted multiset mod P is the sound necessary condition.
P1, P2 = 1_000_000_007, 998244353
KqP = {}
for q in QS:
    dq = D // q
    KqP[q] = (((dq * pow(dq % q, -1, q)) % D) % P1,
              ((dq * pow(dq % q, -1, q)) % D) % P2)
other_qs = [q for q in QS if q not in (128, 729)]
survivors = []
for f128 in sup128_fibs:
    p0 = c128["K"][np.where(c128["fib"] == f128)[0][0]]
    for f729 in split729:
        idx729 = split_idx[f729]
        gam729 = c729["gam"][idx729]
        orbs = sorted(set(gam729.tolist()))
        a0 = c729["K"][idx729[gam729 == orbs[0]][0]]
        a1 = c729["K"][idx729[gam729 == orbs[1]][0]]
        for qt in other_qs:
            T = comp[qt]["K"]
            nz = ~np.all(T == 0, axis=1)
            Tnz = T[nz]
            nz_idx = np.where(nz)[0]
            for st in range(0, len(Tnz), 20000):
                ch = Tnz[st:st+20000]
                hit = np.ones(len(ch), dtype=bool)
                for pi, P in enumerate((P1, P2)):
                    if not hit.any():
                        break
                    base = (KqP[128][pi] * (p0 % P)) % P
                    A0 = (KqP[729][pi] * (a0 % P)) % P
                    A1 = (KqP[729][pi] * (a1 % P)) % P
                    V0 = (base[None, :] + A0[None, :] + (KqP[qt][pi] * (ch % P)) % P) % P
                    V1 = (base[None, :] + A1[None, :] + (KqP[qt][pi] * (ch % P)) % P) % P
                    hit &= np.all(np.sort(V0, axis=1) == np.sort(V1, axis=1), axis=1)
                for h in np.where(hit)[0]:
                    survivors.append({"f128": int(f128), "f729": int(f729),
                                      "qt": int(qt), "t_idx": int(nz_idx[st + h])})
print(f"(b) multiset-mod-P sweep over {sum(len(comp[q]['K']) for q in other_qs)} other-component "
      f"points x {len(sup128_fibs)} 128-fibers x {len(split729)} splits: "
      f"survivors={len(survivors)}", flush=True)

# exact check on survivors (quiet unless a genuine extra family appears)
exact_extra = []
n_killed = 0
for sv in survivors:
    qt, ti = sv["qt"], sv["t_idx"]
    t = comp[qt]["K"][ti]
    f128, f729 = sv["f128"], sv["f729"]
    idx128 = np.where(c128["fib"] == f128)[0]
    idx729 = split_idx[f729]
    combos = {}
    for p in idx128:
        for a in idx729:
            cp = {}
            for q in QS:
                if q == 128: cp[q] = c128["K"][p:p+1]
                elif q == 729: cp[q] = c729["K"][a:a+1]
                elif q == qt: cp[q] = t[None, :]
                else: cp[q] = zero[q][None, :]
            combos[tuple(int(v) for v in crt_py(cp)[0].tolist())] = None
    ms = set(tuple(sorted(row)) for row in combos.keys())
    if len(ms) == 1:
        print(f"  !! EXACT RIGID EXTRA: {sv}", flush=True)
        exact_extra.append(sv)
    else:
        n_killed += 1
print(f"(b) exact extra rigid families: {len(exact_extra)} (survivors killed: {n_killed})", flush=True)

# --- (c) generic sampling via exact (v0,v1) fiber enumeration ---
def enumerate_fiber(xi):
    M = collections.Counter(int(v) for v in xi)
    fcomp = {}
    for q in QS:
        fcomp[q] = collections.Counter(int(v) % q for v in xi)
    out = []
    for v0 in list(M.keys()):
        M1 = M.copy(); M1[v0] -= 1
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
            if collections.Counter(int(v) for v in g) != M: continue
            out.append(tuple(int(v) for v in g))
    return out

rng3 = np.random.default_rng(9)
gen_results = []
for trial in range(20):
    cp = {}
    for q in QS:
        if q == 729:
            f729 = split729[rng3.integers(0, len(split729))]
            idx = split_idx[f729]
            cp[q] = c729["K"][idx[rng3.integers(0, len(idx))]][None, :]
        elif q == 128:
            f128 = sup128_fibs[rng3.integers(0, len(sup128_fibs))]
            idx = np.where(c128["fib"] == f128)[0]
            cp[q] = c128["K"][idx[rng3.integers(0, len(idx))]][None, :]
        else:
            K = comp[q]["K"]
            sup = comp[q]["sup"]
            sidx = np.where(sup)[0]
            cp[q] = K[sidx[rng3.integers(0, len(sidx))]][None, :]
    xi = crt_py(cp)[0]
    fib = enumerate_fiber(xi)
    assert len(fib) >= 1
    fd = fiber_deficit(fib)
    g729 = set(c729["gam"][[c729["lookup"][tuple(int(v) % 729 for v in row)] for row in fib]].tolist())
    gen_results.append({"size": fd["size"], "n_orbits": fd["n_orbits"],
                        "deficit": fd["deficit"], "n_729orbits": len(g729)})
    print(f"  generic trial {trial}: fiber size={fd['size']} orbits={fd['n_orbits']} "
          f"729-orbits spanned={len(g729)} deficit={fd['deficit']:.6f}", flush=True)

# --- cross-check: (v0,v1) enumeration of one rigid fiber point ---
if rigid:
    f128_0, f729_0 = rigid[0]["f128"], rigid[0]["f729"]
    idx128 = np.where(c128["fib"] == f128_0)[0]
    idx729 = split_idx[f729_0]
    cp = {}
    for q in QS:
        if q == 128: cp[q] = c128["K"][idx128[0]][None, :]
        elif q == 729: cp[q] = c729["K"][idx729[0]][None, :]
        else: cp[q] = zero[q][None, :]
    xi = crt_py(cp)[0]
    fib = enumerate_fiber(xi)
    print(f"cross-check rigid fiber (f128={f128_0}, f729={f729_0}): enumerated size="
          f"{len(fib)} vs rigid size={rigid[0]['size']}", flush=True)

# --- full phihat validation at the cross-check point ---
ph = 1.0 + 0j
for q in QS:
    if q == 729:
        i = comp[729]["lookup"][tuple(int(v) % 729 for v in xi)]
        ph *= S729[i]
    elif q == 128:
        i = comp[128]["lookup"][tuple(int(v) % 128 for v in xi)]
        ph *= S128[i]
    else:
        i = comp[q]["lookup"][tuple(int(v) % q for v in xi)]
        ph *= S_point(q, i)
ph /= D
print(f"full |phihat|^2 at rigid point = {abs(ph)**2:.6e} vs 16/D = {16.0/D:.6e}; "
      f"rel err = {abs(abs(ph)**2 - 16.0/D) / (16.0/D):.2e}", flush=True)

supp36 = D // 16
tot_def = tot_rigid_def  # extra rigid families: none (see counts)
out = {"m": m, "D": D, "supp": supp36,
       "rigid_fibers": rigid, "total_rigid_deficit": float(tot_rigid_def),
       "Delta36": float(tot_rigid_def / supp36),
       "s2_survivors": survivors, "exact_extra_rigid": exact_extra,
       "generic": gen_results,
       "phihat_validation_relerr": float(abs(abs(ph) ** 2 - 16.0 / D) / (16.0 / D))}
with open("wave22_m36_deficit.json", "w") as fh:
    json.dump(out, fh, indent=1, default=str)
print(f"TOTAL: rigid deficit={tot_rigid_def:.6f} Delta(36)={tot_rigid_def / supp36:.6e}", flush=True)
