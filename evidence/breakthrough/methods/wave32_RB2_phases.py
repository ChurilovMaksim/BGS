"""Wave 32, task 2: are the new on-support splits phase-split?

Key identity (avoids the adjugate): for H = H_m, X = adj(H) = D*H^{-1},
a kernel point y mod q with H y = q*W (exact ints) satisfies
    W X W'^T = (D/q) * (W . y')          (exact integer identity)
since H^{-1} W' = y'/q.  Hence, with Q_i = (D/q)(W_i.y_i) mod q and
P_ij = (D/q)(W_i.y_j) mod q, the wave-20 S_q vector is
    S_q[j] = sum_i exp(2 pi i * (ci * T_ij mod q)/q),
    T_ij = (2 Q_i - P_ij) [* inv_u2 if correction mode], ci = (D/q)^{-1} mod q.
Correction mode is decided by the wave-16 test against global points
g (H g = D*w): Qr_i = (g_i.w_i) mod q, Pr_ij = (g_i.w_j) mod q.

Targets: (m,q) = (30,625) and (32,8192): for each on-support split
fiber, report |S| and phase per orbit.  Equal phases across orbits
=> phase-degenerate split (no Delta contribution from it).
"""
import sys
sys.path.insert(0, ".")
import numpy as np
import sympy as sp
from wave16_d1a_targeted import (Dm, snf_kernel, sample_kernel_points,
                                 torsion_data, comp_supported,
                                 gamma_perms, lex_canon, group_ids)

def H_np(v):
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)

def component_QP(K, q, D):
    """K: (n,m) kernel points mod q. Returns Q (n,), P (n,n) mod q."""
    HK = H_np(K)
    assert np.all(HK % q == 0)
    W = HK // q
    # only Q,P mod q are needed: reduce D/q mod q first (D/q exceeds int64)
    dqm = (D // q) % q
    Q = (dqm * np.einsum("ij,ij->i", W, K)) % q
    P = (dqm * (W @ K.T)) % q
    return Q, P, W

def global_QP(glob, q, D):
    """glob: (n,m) global points mod D. Returns Qr (n,), Pr (n,n) mod q."""
    Hg = 6 * glob - np.roll(glob, 1, axis=1) - np.roll(glob, -1, axis=1)
    assert np.all(Hg % D == 0), "global point not in kernel mod D"
    w = Hg // D
    Qr = np.array([int(sum(glob[i, j] * w[i, j] for j in range(glob.shape[1]))) % q
                   for i in range(glob.shape[0])], dtype=np.int64)
    Pr = np.array([[int(sum(glob[i, j] * w[k, j] for j in range(glob.shape[1]))) % q
                    for k in range(glob.shape[0])] for i in range(glob.shape[0])],
                  dtype=np.int64)
    return Qr, Pr

def crt_py(comp_pts, D):
    """Exact Python-int CRT; returns object array mod D (D may exceed int64)."""
    n = len(next(iter(comp_pts.values())))
    out = np.zeros((n, glob_m), dtype=object)
    for q, pts in comp_pts.items():
        dq = D // q
        Kk = (dq * pow(dq % q, -1, q)) % D
        out = out + Kk * pts.astype(object)
    return out % D

def analyze(m, qstar):
    global glob_m
    glob_m = m
    D = Dm(m)
    fac = sp.factorint(D)
    qs = sorted([p ** e for p, e in fac.items()])
    assert qstar in qs
    Z, Qmod = torsion_data(m, D)
    perms = gamma_perms(m)
    K = snf_kernel(m, qstar)
    assert len(K) == qstar
    Q, P, W = component_QP(K, qstar, D)
    fib = group_ids(np.sort(K, axis=1))
    canon = lex_canon(K, perms)
    gam = group_ids(canon)
    sup = comp_supported(K, Z, Qmod, qstar)
    gam_fiber = np.empty(int(gam.max()) + 1, dtype=np.int64)
    gam_fiber[gam] = fib
    opf = np.bincount(gam_fiber, minlength=int(fib.max()) + 1)
    split_fibs = np.where(opf > 1)[0]
    print(f"== m={m} q*={qstar} D={D}", flush=True)
    # correction mode test (wave-16): random global points
    rng = np.random.default_rng(3)
    comp_pts = {}
    for q in qs:
        if q == qstar:
            sel = rng.integers(0, len(K), size=400)
            comp_pts[q] = K[sel]
        elif q <= 400_000:
            Kq = snf_kernel(m, q)
            sel = rng.integers(0, len(Kq), size=400)
            comp_pts[q] = Kq[sel]
        else:
            comp_pts[q] = sample_kernel_points(m, q, 400, rng)
    glob = crt_py(comp_pts, D)
    Qr, Pr = global_QP(glob, qstar, D)
    u = (D // qstar) % qstar
    inv_u2 = pow((u * u) % qstar, -1, qstar)
    lookup = {tuple(int(x) for x in row): i for i, row in enumerate(K)}
    idx = np.array([lookup[tuple(int(x) % qstar for x in row)] for row in glob])
    raw_bad = corr_bad = 0
    for _ in range(300):
        i = int(rng.integers(0, len(glob))); j = int(rng.integers(0, len(glob)))
        tg = int((2 * Qr[i] - Pr[i, j]) % qstar)
        tc = int((2 * Q[idx[i]] - P[idx[i], idx[j]]) % qstar)
        if tc != tg: raw_bad += 1
        if (inv_u2 * tc) % qstar != tg: corr_bad += 1
    corr = (raw_bad > 0 and corr_bad == 0)
    print(f"   correction mode: raw_bad={raw_bad} corr_bad={corr_bad} -> corr={corr}",
          flush=True)
    assert not (raw_bad > 0 and corr_bad > 0), "no mode fits"
    # S_q values at split-fiber points only
    ci = pow(D // qstar, -1, qstar)
    T = (2 * Q[:, None] - P) % qstar
    if corr:
        T = (inv_u2 * T) % qstar
    for f in split_fibs:
        idxf = np.where(fib == f)[0]
        s = int(sup[idxf].sum())
        if s != len(idxf):
            continue
        print(f"   ON-SUPPORT split fiber {f}: size={len(idxf)} "
              f"orbits={len(set(gam[idxf].tolist()))}", flush=True)
        for g in sorted(set(gam[idxf].tolist())):
            oo = idxf[gam[idxf] == g]
            # S at points oo: sum over all i
            E = np.exp(2j * np.pi * ((ci * T[:, oo]) % qstar) / qstar)
            vals = E.sum(axis=0)
            ph = np.angle(vals)
            print(f"      orbit {g}: size={len(oo)} |S| mean={np.abs(vals).mean():.4f} "
                  f"phase spread={np.abs(vals - vals[0]).max():.2e} "
                  f"phase={ph[0]:.6f}", flush=True)
    print(flush=True)

analyze(30, 625)
analyze(32, 8192)
