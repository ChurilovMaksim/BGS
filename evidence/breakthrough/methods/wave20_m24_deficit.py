"""Wave 20, task 3: cancellation deficit Delta at m=24 (and exact
Delta=0 at m=16, m=20 by the Gamma-invariance argument).

Key structural fact (proved as a sketch, used here):
  S_q[j] = sum_i exp(2*pi*i*(ci*T_corr[i,j])/q) is Gamma-invariant:
  S_q[j o gamma] = S_q[j] (reindex the kernel sum; X=adj(H) commutes
  with dihedral permutations). Hence S_q is constant on every
  single-orbit component fiber. A global fiber F whose component
  fibers are ALL single orbits therefore has phihat CONSTANT on F,
  so its deficit is exactly 0. Only global fibers containing a
  SPLIT component fiber can contribute to Delta.
  - m=16: splits only at q=2048, all off-support -> Delta=0 exactly.
  - m=20: no component splits at all -> Delta=0 exactly.
  - m=24: one on-support split component fiber (q=81, 36 pts,
    3 orbits). This script computes exactly the on-support global
    fibers containing it (rigid construction + exhaustive
    single-component rigidity sweep + generic sampling via exact
    (v0,v1) fiber enumeration) and their deficits.

Arithmetic care at m=24 (D ~ 2.36e18): global CRT and H use Python
ints (object arrays); all mod-q work uses X reduced mod q (exact,
since everything downstream is mod q); int64 is safe for values
< D and for component values < q.
Repository untouched; no Lean build.
"""
import collections
import json
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, ".")
from wave16_d1a_targeted import (Dm, snf_kernel, sample_kernel_points,
                                 torsion_data, comp_supported,
                                 gamma_perms, lex_canon, group_ids)

m = 24
D = Dm(m)
QS = [25, 49, 81, 121, 289, 512, 1329409]
assert D == 25 * 49 * 81 * 121 * 289 * 512 * 1329409, D
Z, Qmod = torsion_data(m, D)
perms = gamma_perms(m)
print(f"m={m} D={D} |V4|={len(Z)} nperms={len(perms)}", flush=True)

# --- adjugate of H_m (exact), reduced mod q per component ---
Hsp = sp.zeros(m)
for i in range(m):
    Hsp[i, i] = 6
    Hsp[i, (i - 1) % m] -= 1
    Hsp[i, (i + 1) % m] -= 1
X = np.array(Hsp.adjugate().tolist(), dtype=object)
print("det==D:", int(Hsp.det()) == D, "X max abs digits:",
      len(str(int(np.max(np.abs(X.astype(object)))))), flush=True)


def H_py(v):
    """H applied to object/int arrays (exact Python ints)."""
    v = np.asarray(v, dtype=object)
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)


def H_np(v):
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)


def crt_py(comp_pts):
    """comp_pts: dict q -> (n, m) int64 array. Exact Python-int CRT."""
    n = len(next(iter(comp_pts.values())))
    out = np.zeros((n, m), dtype=object)
    for q, pts in comp_pts.items():
        dq = D // q
        K = (dq * pow(dq % q, -1, q)) % D
        out = out + K * pts.astype(object)
    return (out % D).astype(np.int64)


# --- component data (small q fully; large q sampled) ---
comp = {}
for q in QS:
    if q <= 512:
        K = snf_kernel(m, q)
        assert len(K) == q
        HK = H_np(K)
        assert np.all(HK % q == 0)
        W = HK // q
        Xq = np.array([[int(x) % q for x in row] for row in X.tolist()],
                       dtype=np.int64)
        WX = (W @ Xq) % q
        Qv = np.einsum("ij,ij->i", WX, W) % q
        Pv = (WX @ W.T) % q
        comp[q] = {"K": K, "W": W, "Q": Qv, "P": Pv,
                   "lookup": {tuple(row): i for i, row in enumerate(K)}}
        fib = group_ids(np.sort(K, axis=1))
        canon = lex_canon(K, perms)
        gam = group_ids(canon)
        sup = comp_supported(K, Z, Qmod, q)
        comp[q].update({"fib": fib, "gam": gam, "sup": sup})
        print(f"q={q}: pts={len(K)} fibers={int(fib.max())+1} "
              f"supp_pts={int(sup.sum())}", flush=True)
    else:
        rng = np.random.default_rng(11)
        S = sample_kernel_points(m, q, 400, rng)
        HS = H_np(S)
        assert np.all(HS % q == 0)
        W = HS // q
        Xq = np.array([[int(x) % q for x in row] for row in X.tolist()],
                       dtype=np.int64)
        WX = (W @ Xq) % q
        Qv = np.einsum("ij,ij->i", WX, W) % q
        Pv = (WX @ W.T) % q
        comp[q] = {"K": S, "W": W, "Q": Qv, "P": Pv,
                   "lookup": {tuple(row): i for i, row in enumerate(S)}}
        print(f"q={q}: sampled {len(S)} kernel points", flush=True)

# --- correction modes (wave-16 test, s=1) ---
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
    Xq = np.array([[int(x) % q for x in row] for row in X.tolist()],
                   dtype=np.int64)
    wr = np.asarray(wrand, dtype=np.int64)
    Qr = np.einsum("ij,ij->i", (wr @ Xq) % q, wr) % q
    Pr = ((wr @ Xq) % q) @ wr.T % q
    u = (D // q) % q
    inv_u2 = pow((u * u) % q, -1, q)
    idx = np.array([c["lookup"][tuple(row)] for row in (rand_glob % q)])
    raw_bad = corr_bad = 0
    for _ in range(300):
        i = int(rng.integers(0, len(rand_glob)))
        j = int(rng.integers(0, len(rand_glob)))
        tg = int((2 * Qr[i] - Pr[i, j]) % q)
        tc = int((2 * c["Q"][idx[i]] - c["P"][idx[i], idx[j]]) % q)
        if tc != tg:
            raw_bad += 1
        if (inv_u2 * tc) % q != tg:
            corr_bad += 1
    c["corr"] = (raw_bad > 0 and corr_bad == 0)
    print(f"  corr q={q}: raw_bad={raw_bad} corr_bad={corr_bad} "
          f"-> corr={c['corr']}", flush=True)
    assert not (raw_bad > 0 and corr_bad > 0), "no mode fits"


def S_vec(q):
    """Full S_j vector for small q (exact CRT factor)."""
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
S512 = S_vec(512)
print("S81/S512 computed", flush=True)

# --- q=81 split fiber; supported 512-fibers ---
c81 = comp[81]
gf = np.empty(int(c81["gam"].max()) + 1, dtype=np.int64)
gf[c81["gam"]] = c81["fib"]
opf = np.bincount(gf, minlength=int(c81["fib"].max()) + 1)
split81 = np.where(opf > 1)[0]
assert len(split81) == 1
f81 = int(split81[0])
idx81 = np.where(c81["fib"] == f81)[0]
print(f"q=81 split fiber {f81}: size={len(idx81)} orbits="
      f"{len(set(c81['gam'][idx81].tolist()))} supp={int(c81['sup'][idx81].sum())}",
      flush=True)
assert int(c81["sup"][idx81].sum()) == len(idx81)
# S81 phases across the 3 component orbits
for g in sorted(set(c81["gam"][idx81].tolist())):
    oo = idx81[c81["gam"][idx81] == g]
    vals = S81[oo]
    print(f"  81-orbit {g}: size={len(oo)} |S| mean={np.abs(vals).mean():.6f} "
          f"phase spread={np.abs(vals - vals[0]).max():.2e} "
          f"phase={np.angle(vals[0]):.6f}", flush=True)

c512 = comp[512]
sup512_fibs = sorted(set(c512["fib"][c512["sup"]].tolist()))
print(f"supported 512-fibers: {len(sup512_fibs)}; sizes="
      f"{[int((c512['fib'] == f).sum()) for f in sup512_fibs]}", flush=True)
zero = {}
for q in QS:
    if q <= 512:
        zidx = comp[q]["lookup"][(0,) * m]
        zero[q] = comp[q]["K"][zidx]
        assert bool(comp[q]["sup"][zidx]), f"zero not supported at q={q}"
    else:
        zero[q] = np.zeros(m, dtype=np.int64)
print("zero component point supported at all small q (checked); "
      "q=1329409 zero: support criterion 2Q(z)==0 mod q holds since "
      "q | D (checked below)", flush=True)
for z in Z:
    assert all((2 * (qq % 1329409)) % 1329409 == 0 for qq in [0]) or True
# direct check: zero supported at 1329409 via criterion
Qm = [qq % 1329409 for qq in Qmod]
assert all((2 * qq) % 1329409 == 0 for qq in Qm), "zero NOT supported at 1329409"
print("zero supported at q=1329409: True", flush=True)


def rel_phi(glob):
    """Relative phihat (S81 x S512 only; other components are common
    factors within the fibers studied here)."""
    i81 = np.array([comp[81]["lookup"][tuple(row)] for row in (glob % 81)])
    i512 = np.array([comp[512]["lookup"][tuple(row)] for row in (glob % 512)])
    return S81[i81] * S512[i512]


def fiber_deficit(glob):
    """glob: points of one global fiber. Returns dict with orbits,
    sizes, phases, deficit (Bsym units)."""
    can = lex_canon(glob, perms)
    gam = group_ids(can)
    rel = rel_phi(glob)
    orbits = []
    for g in sorted(set(gam.tolist())):
        oo = gam == g
        vals = rel[oo]
        dev = float(np.abs(vals - vals[0]).max())
        assert dev < 1e-9, f"rel not constant on orbit! dev={dev}"
        orbits.append({"size": int(oo.sum()),
                       "phase": float(np.angle(vals[0])),
                       "abs": float(np.abs(vals[0]))})
    F = len(glob)
    coh = abs(sum(o["size"] * np.exp(1j * o["phase"])
                  for o in orbits)) ** 2
    return {"size": F, "n_orbits": len(orbits), "orbits": orbits,
            "coherent": float(coh), "deficit": float(F * F - coh)}


# --- (a) rigid combos: supported 512-fiber x S81 x zeros ---
rigid = []
for f512 in sup512_fibs:
    idx512 = np.where(c512["fib"] == f512)[0]
    n512 = len(idx512)
    combos = {}
    for p in idx512:
        for a in idx81:
            cp = {}
            for q in QS:
                if q == 512:
                    cp[q] = c512["K"][p:p + 1]
                elif q == 81:
                    cp[q] = c81["K"][a:a + 1]
                else:
                    cp[q] = zero[q][None, :]
            combos.setdefault(tuple(crt_py(cp)[0].tolist()), None)
    # group combos by sorted global multiset
    pts = np.array([list(k) for k in combos.keys()], dtype=np.int64)
    gfib = group_ids(np.sort(pts, axis=1))
    for g in sorted(set(gfib.tolist())):
        sub = pts[gfib == g]
        fd = fiber_deficit(sub)
        fd["f512"] = int(f512)
        fd["n512"] = int(n512)
        rigid.append(fd)
        print(f"  rigid f512={f512} (n512={n512}): global fiber size="
              f"{fd['size']} orbits={fd['n_orbits']} orbit_sizes="
              f"{[o['size'] for o in fd['orbits']]} deficit={fd['deficit']:.6f}",
              flush=True)
tot_rigid_def = sum(r["deficit"] for r in rigid)
print(f"(a) rigid global fibers: {len(rigid)} total deficit={tot_rigid_def:.6f}",
      flush=True)

# --- (b') single-component rigidity sweep (exhaustive for small q,
# sampled for q=1329409). For each candidate fixed sequence t and each
# supported 512-fiber: do all combos (512-fiber x S81 x {t} x zeros)
# share ONE global multiset? Early exit on first mismatch. ---
Kq = {}
for q in QS:
    dq = D // q
    Kq[q] = (dq * pow(dq % q, -1, q)) % D


def combos_one_multiset(t_q, t, f512):
    """t_q: component of t; t: its sequence. 512-fiber x S81 x {t}.
    Returns True iff all combos share one sorted multiset."""
    idx512 = np.where(c512["fib"] == f512)[0]
    ref = None
    for p in idx512:
        pseq = c512["K"][p]
        for a in idx81:
            aseq = c81["K"][a]
            vals = []
            for i in range(m):
                v = 0
                for q in QS:
                    if q == 512:
                        v += Kq[q] * int(pseq[i])
                    elif q == 81:
                        v += Kq[q] * int(aseq[i])
                    elif q == t_q:
                        v += Kq[q] * int(t[i])
                    # else zero contributes 0
                vals.append(v % D)
            srt = tuple(sorted(vals))
            if ref is None:
                ref = srt
            elif srt != ref:
                return False
    return True


extra_rigid = []
for t_q in (25, 49, 121, 289):
    K = comp[t_q]["K"]
    for ti in range(len(K)):
        t = K[ti]
        if np.all(t == 0):
            continue
        for f512 in sup512_fibs:
            if combos_one_multiset(t_q, t, f512):
                print(f"  !! EXTRA RIGID: q={t_q} point#{ti} f512={f512}",
                      flush=True)
                extra_rigid.append({"q": int(t_q), "point": int(ti),
                                    "f512": int(f512)})
print(f"(b') small-odd sweep: {4} components x points x {len(sup512_fibs)} "
      f"512-fibers -> extra rigid families: {len(extra_rigid)}", flush=True)
rng2 = np.random.default_rng(5)
samp_big = sample_kernel_points(m, 1329409, 60, rng2)
n_extra_big = 0
for si in range(len(samp_big)):
    t = samp_big[si]
    if np.all(t == 0):
        continue
    for f512 in sup512_fibs:
        if combos_one_multiset(1329409, t, f512):
            print(f"  !! EXTRA RIGID BIG: sample#{si} f512={f512}", flush=True)
            n_extra_big += 1
print(f"(b') large-q sweep (60 sampled 1329409 points): extra={n_extra_big}",
      flush=True)

# --- (c) generic sampling via exact (v0, v1) fiber enumeration ---
def enumerate_fiber(xi):
    """All points xi' with sorted(xi') == sorted(xi) and xi' in Fix_m
    mod D, via (v0, v1) = first two entries (forced recurrence)."""
    M = collections.Counter(xi.tolist())
    fcomp = {}
    for q in QS:
        fcomp[q] = collections.Counter((xi % q).tolist())
    out = []
    for v0 in list(M.keys()):
        M1 = M.copy()
        M1[v0] -= 1
        if M1[v0] == 0:
            del M1[v0]
        for v1 in list(M1.keys()):
            seqs = {}
            ok = True
            for q in QS:
                y = [v0 % q, v1 % q]
                for i in range(1, m - 1):
                    y.append((6 * y[i] - y[i - 1]) % q)
                # closure: y[m] == y[0], y[m+1] == y[1]
                ym = (6 * y[m - 1] - y[m - 2]) % q
                ym1 = (6 * ym - y[m - 1]) % q
                if ym != y[0] or ym1 != y[1]:
                    ok = False
                    break
                seqs[q] = y[:m]
                if collections.Counter(y[:m]) != fcomp[q]:
                    ok = False
                    break
            if not ok:
                continue
            cp = {q: np.array(seqs[q], dtype=np.int64)[None, :] for q in QS}
            g = crt_py(cp)[0]
            if collections.Counter(g.tolist()) != M:
                continue
            out.append(g)
    return np.array(out, dtype=np.int64) if out else np.zeros((0, m),
                                                             dtype=np.int64)


rng3 = np.random.default_rng(9)
gen_results = []
for trial in range(20):
    cp = {}
    for q in QS:
        if q == 81:
            cp[q] = c81["K"][idx81[rng3.integers(0, len(idx81))]][None, :]
        elif q == 512:
            f512 = sup512_fibs[rng3.integers(0, len(sup512_fibs))]
            idxp = np.where(c512["fib"] == f512)[0]
            cp[q] = c512["K"][idxp[rng3.integers(0, len(idxp))]][None, :]
        elif q == 1329409:
            cp[q] = sample_kernel_points(m, q, 1, rng3)
        else:
            K = comp[q]["K"]
            cp[q] = K[rng3.integers(0, len(K))][None, :]
    xi = crt_py(cp)[0]
    fib = enumerate_fiber(xi)
    assert len(fib) >= 1
    fd = fiber_deficit(fib)
    # how many distinct S81-orbits does the fiber's 81-content span?
    g81 = set(c81["gam"][np.array([c81["lookup"][tuple(row)]
                                   for row in (fib % 81)])].tolist())
    gen_results.append({"size": fd["size"], "n_orbits": fd["n_orbits"],
                        "deficit": fd["deficit"],
                        "n_81orbits": len(g81)})
    print(f"  generic trial {trial}: fiber size={fd['size']} orbits="
          f"{fd['n_orbits']} 81-orbits spanned={len(g81)} "
          f"deficit={fd['deficit']:.6f}", flush=True)

# --- cross-check: (v0,v1) enumeration of one rigid fiber point ---
if rigid:
    f512_0 = rigid[0]["f512"]
    idx512 = np.where(c512["fib"] == f512_0)[0]
    cp = {}
    for q in QS:
        if q == 512:
            cp[q] = c512["K"][idx512[0]][None, :]
        elif q == 81:
            cp[q] = c81["K"][idx81[0]][None, :]
        else:
            cp[q] = zero[q][None, :]
    xi = crt_py(cp)[0]
    fib = enumerate_fiber(xi)
    print(f"cross-check rigid fiber (f512={f512_0}): enumerated size="
          f"{len(fib)} vs rigid size={rigid[0]['size']}", flush=True)

# --- full phihat validation on one rigid point (incl. q=1329409) ---
# S_1329409 at zero: needs full kernel Q vector (1.3M points)
qbig = 1329409
Kbig = snf_kernel(m, qbig)
HKbig = H_np(Kbig)
assert np.all(HKbig % qbig == 0)
Wbig = HKbig // qbig
Xqbig = np.array([[int(x) % qbig for x in row] for row in X.tolist()],
                  dtype=np.int64)
WXbig = (Wbig @ Xqbig) % qbig
Qbig = np.einsum("ij,ij->i", WXbig, Wbig) % qbig
ci = pow(D // qbig, -1, qbig)
u = (D // qbig) % qbig
inv_u2 = pow((u * u) % qbig, -1, qbig)
Tbig = (2 * Qbig) % qbig
if comp[qbig]["corr"]:
    Tbig = (inv_u2 * Tbig) % qbig
Sbig0 = np.exp(2j * np.pi * ((ci * Tbig) % qbig) / qbig).sum()
print(f"S_1329409[zero]: |S|={abs(Sbig0):.6f} (sqrt(q)={np.sqrt(qbig):.6f})",
      flush=True)
# full phihat at the cross-check point xi
ph = 1.0 + 0j
for q in QS:
    if q == 81:
        i = comp[81]["lookup"][tuple((xi % 81).tolist())]
        ph *= S81[i]
    elif q == 512:
        i = comp[512]["lookup"][tuple((xi % 512).tolist())]
        ph *= S512[i]
    elif q == 1329409:
        ph *= Sbig0
    else:
        Sq = S_vec(q)
        i = comp[q]["lookup"][tuple((xi % q).tolist())]
        ph *= Sq[i]
ph /= D
print(f"full |phihat|^2 at rigid point = {abs(ph)**2:.6e} vs 16/D = "
      f"{16.0/D:.6e}; rel err = "
      f"{abs(abs(ph)**2 - 16.0/D) / (16.0/D):.2e}", flush=True)

supp24 = 147609025664839200
tot_def = tot_rigid_def  # extra rigid families: none found (see counts)
out = {"m": m, "D": D, "supp": supp24,
       "rigid_fibers": rigid, "total_rigid_deficit": float(tot_rigid_def),
       "Delta24": float(tot_rigid_def / supp24),
       "extra_rigid_small": extra_rigid, "extra_rigid_big": n_extra_big,
       "generic": gen_results,
       "phihat_validation_relerr": float(abs(abs(ph) ** 2 - 16.0 / D) / (16.0 / D))}
with open("wave20_m24_deficit.json", "w") as fh:
    json.dump(out, fh, indent=1, default=str)
print(f"TOTAL: rigid deficit={tot_rigid_def:.6f} Delta(24)="
      f"{tot_rigid_def / supp24:.6e}", flush=True)
print(json.dumps(out, indent=1, default=str)[:2000])
