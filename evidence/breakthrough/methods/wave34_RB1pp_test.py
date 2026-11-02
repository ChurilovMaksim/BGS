"""Wave 34, task 3: test RB1'' at m=60 via joint 81 x 625 fibers.

RB1'' (wave 33) claims every contributing global fiber is one split
fiber at q* x one supported 2-fiber x one companion (singleton, or twin
when q* = q3) x singletons. At m=60 both q=81 (split 36,3) and q=625
(split 150,5 x2) are on-support. A joint fiber from both splits, with
all other components fixed to supported singletons (zero where
supported), that has >=2 diagonal Gamma-orbits with distinct phases
is a contributing fiber with a split companion -> RB1'' is FALSE.

Global fiber = pairs (a,b) in F81 x F625 with the same joint multiset
of pairs (a_i, b_i) (CRT is injective on pairs; reductions to other
components force the fixed singletons). Diagonal Gamma-orbits are
computed on the encoded pair sequence v_i = a_i*625 + b_i.
Phases: wave-32 S_q method (adjugate-free, correction-mode tested).
"""
import sys, math
sys.path.insert(0, ".")
import numpy as np
import sympy as sp
from wave16_d1a_targeted import (Dm, snf_kernel, sample_kernel_points,
                                 torsion_data, comp_supported,
                                 gamma_perms, lex_canon, group_ids)

m = 60
D = Dm(m)
fac = sp.factorint(D)
qs = sorted([p ** e for p, e in fac.items()])
print(f"m={m} D={D} components={qs}", flush=True)
Z, Qmod = torsion_data(m, D)
perms = gamma_perms(m)

# 1. Zero support at every component (dot=0, need 2*Qmod == 0 mod q)
zero_ok = {}
for q in qs:
    Qm = np.array([qq % q for qq in Qmod], dtype=np.int64)
    zero_ok[q] = bool(np.all((2 * Qm) % q == 0))
print("zero supported per component:", zero_ok, flush=True)

def fixed_point(q):
    """A supported singleton-fiber point at q (zero if it qualifies)."""
    if zero_ok[q]:
        return np.zeros(m, dtype=np.int64)
    pts = snf_kernel(m, q)
    fib = group_ids(np.sort(pts, axis=1))
    sup = comp_supported(pts, Z, Qmod, q)
    for i in range(len(pts)):
        if sup[i] and int((fib == fib[i]).sum()) == 1:
            return pts[i]
    raise RuntimeError(f"no supported singleton at q={q}")

fixed = {q: fixed_point(q) for q in qs if q not in (81, 625)}
print("fixed other components to supported singletons:", flush=True)
for q, pt in fixed.items():
    print(f"   q={q}: nonzero={int(np.count_nonzero(pt))}", flush=True)

# 2. Component fibers / orbits / support at 81 and 625
def comp_data(q):
    pts = snf_kernel(m, q)
    assert len(pts) == q
    fib = group_ids(np.sort(pts, axis=1))
    canon = lex_canon(pts, perms)
    gam = group_ids(canon)
    sup = comp_supported(pts, Z, Qmod, q)
    gam_fiber = np.empty(int(gam.max()) + 1, dtype=np.int64)
    gam_fiber[gam] = fib
    opf = np.bincount(gam_fiber, minlength=int(fib.max()) + 1)
    splits = []
    for f in np.where(opf > 1)[0]:
        idx = np.where(fib == f)[0]
        if int(sup[idx].sum()) == len(idx):
            splits.append((int(f), idx))
    return pts, fib, gam, sup, splits

pts81, fib81, gam81, sup81, splits81 = comp_data(81)
pts625, fib625, gam625, sup625, splits625 = comp_data(625)
print(f"81: on-support split fibers: {[(f, len(idx), len(set(gam81[idx].tolist()))) for f, idx in splits81]}", flush=True)
print(f"625: on-support split fibers: {[(f, len(idx), len(set(gam625[idx].tolist()))) for f, idx in splits625]}", flush=True)

# 3. Component phases via wave-32 method (with correction-mode test)
def H_np(v):
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)

def component_QP(K, q):
    HK = H_np(K)
    assert np.all(HK % q == 0)
    W = HK // q
    dqm = (D // q) % q
    Q = (dqm * np.einsum("ij,ij->i", W, K)) % q
    P = (dqm * (W @ K.T)) % q
    return Q, P

def crt_py(comp_pts):
    n = len(next(iter(comp_pts.values())))
    out = np.zeros((n, m), dtype=object)
    for q, pts in comp_pts.items():
        dq = D // q
        Kk = (dq * pow(dq % q, -1, q)) % D
        out = out + Kk * pts.astype(object)
    return out % D

def global_QP(glob, q):
    Hg = 6 * glob - np.roll(glob, 1, axis=1) - np.roll(glob, -1, axis=1)
    assert np.all(Hg % D == 0)
    w = Hg // D
    Qr = np.array([int(sum(glob[i, j] * w[i, j] for j in range(m))) % q
                   for i in range(len(glob))], dtype=np.int64)
    Pr = np.array([[int(sum(glob[i, j] * w[k, j] for j in range(m))) % q
                    for k in range(len(glob))] for i in range(len(glob))],
                  dtype=np.int64)
    return Qr, Pr

def orbit_phases(K, q, fib, gam, splits):
    Q, P = component_QP(K, q)
    # correction-mode test with random global points
    rng = np.random.default_rng(3)
    comp_pts = {}
    for qq in qs:
        if qq == q:
            sel = rng.integers(0, len(K), size=200)
            comp_pts[qq] = K[sel]
        elif qq <= 400_000:
            Kq = snf_kernel(m, qq)
            sel = rng.integers(0, len(Kq), size=200)
            comp_pts[qq] = Kq[sel]
        else:
            comp_pts[qq] = sample_kernel_points(m, qq, 200, rng)
    glob = crt_py(comp_pts)
    Qr, Pr = global_QP(glob, q)
    u = (D // q) % q
    inv_u2 = pow((u * u) % q, -1, q)
    lookup = {tuple(int(x) for x in row): i for i, row in enumerate(K)}
    idx = np.array([lookup[tuple(int(x) % q for x in row)] for row in glob])
    raw_bad = corr_bad = 0
    for _ in range(200):
        i = int(rng.integers(0, len(glob))); j = int(rng.integers(0, len(glob)))
        tg = int((2 * Qr[i] - Pr[i, j]) % q)
        tc = int((2 * Q[idx[i]] - P[idx[i], idx[j]]) % q)
        if tc != tg: raw_bad += 1
        if (inv_u2 * tc) % q != tg: corr_bad += 1
    corr = (raw_bad > 0 and corr_bad == 0)
    print(f"   q={q} correction: raw_bad={raw_bad} corr_bad={corr_bad} -> corr={corr}", flush=True)
    assert not (raw_bad > 0 and corr_bad > 0)
    ci = pow(D // q, -1, q)
    T = (2 * Q[:, None] - P) % q
    if corr:
        T = (inv_u2 * T) % q
    ph = {}
    for f, idxf in splits:
        for g in sorted(set(gam[idxf].tolist())):
            oo = idxf[gam[idxf] == g]
            E = np.exp(2j * np.pi * ((ci * T[:, oo]) % q) / q)
            vals = E.sum(axis=0)
            ph[g] = float(np.angle(vals[0]))
            print(f"   q={q} fiber {f} orbit {g}: size={len(oo)} phase={ph[g]:.6f} "
                  f"spread={np.abs(vals - vals[0]).max():.2e}", flush=True)
    return ph

print("phases at 81:", flush=True)
ph81 = orbit_phases(pts81, 81, fib81, gam81, splits81)
print("phases at 625:", flush=True)
ph625 = orbit_phases(pts625, 625, fib625, gam625, splits625)

# 4. Twin status of 625 at m=60: ord of beta = 17+12*sqrt(2) in R_q
def beta_order(q):
    def mul(a, b):
        return ((a[0]*b[0] + 2*a[1]*b[1]) % q, (a[0]*b[1] + a[1]*b[0]) % q)
    cur, beta, n = (1, 0), (17 % q, 12 % q), 0
    while True:
        cur = mul(cur, beta); n += 1
        if cur == (1, 0):
            return n
        assert n < 10 * q * q
print(f"ord_81(beta)={beta_order(81)} ord_625(beta)={beta_order(625)}", flush=True)

# 5. Joint fibers: pairs (a in F81, b in F625) grouped by joint multiset
def joint_test(f81, idx81, f625, idx625):
    A = pts81[idx81]
    B = pts625[idx625]
    pairs = []
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            v = a.astype(np.int64) * 625 + b.astype(np.int64)
            key = tuple(sorted(v.tolist()))
            pairs.append((key, i, j))
    from collections import defaultdict
    fibers = defaultdict(list)
    for key, i, j in pairs:
        fibers[key].append((i, j))
    n_multi_orbit = 0
    contributing = []
    for key, members in fibers.items():
        if len(members) < 2:
            continue
        # diagonal orbits: canon of pair-sequence under simultaneous perms
        V = np.array([[int(A[i][t]) * 625 + int(B[j][t]) for t in range(m)]
                      for i, j in members], dtype=np.int64)
        canon = lex_canon(V, perms)
        og = group_ids(canon)
        orbits = {}
        for k, (i, j) in enumerate(members):
            orbits.setdefault(int(og[k]), []).append((i, j))
        if len(orbits) < 2:
            continue
        n_multi_orbit += 1
        # phase of each diagonal orbit = ph81[o81] + ph625[o625]
        ths = []
        for k, mem in orbits.items():
            i0, j0 = mem[0]
            o81 = int(gam81[idx81[i0]])
            o625 = int(gam625[idx625[j0]])
            ths.append((ph81[o81] + ph625[o625]) % (2 * np.pi))
        # deficit > 0 iff phases not all equal (mod 2pi)
        dmax = 0.0
        for x in range(len(ths)):
            for y in range(x + 1, len(ths)):
                d = abs((ths[x] - ths[y] + np.pi) % (2 * np.pi) - np.pi)
                dmax = max(dmax, d)
        if dmax > 1e-6:
            sizes = [len(mem) for mem in orbits.values()]
            dF = 0.0
            for x in range(len(ths)):
                for y in range(x + 1, len(ths)):
                    dF += 2 * sizes[x] * sizes[y] * (1 - math.cos(ths[x] - ths[y]))
            contributing.append((len(members), len(orbits), sizes, ths, dF))
    print(f"joint F81={f81} x F625={f625}: pairs={len(pairs)} joint fibers={len(fibers)} "
          f"multi-orbit fibers={n_multi_orbit} CONTRIBUTING={len(contributing)}", flush=True)
    for c in contributing[:10]:
        print(f"   CONTRIBUTING fiber: size={c[0]} orbits={c[1]} orbit_sizes={c[2]} "
              f"phases={[round(t, 4) for t in c[3]]} Delta_F={c[4]:.1f}", flush=True)
    return contributing

all_contrib = []
for f81, idx81 in splits81:
    for f625, idx625 in splits625:
        all_contrib += joint_test(f81, idx81, f625, idx625)
print("TOTAL CONTRIBUTING joint fibers:", len(all_contrib), flush=True)
