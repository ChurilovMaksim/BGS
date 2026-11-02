"""Wave 35, task 3, stage 1: direct census vs trace model for split fibers.

Direct: wave16 code (kernel mod q, fibers by sorted multiset, Gamma-orbits
by lex canon, support by torsion criterion). Trace model (odd p):
kernel rows mod p^(2f) are p^f * Tr(C alpha^j) mod p^(2f), C in R/p^f.
"""
import sys, math
sys.path.insert(0, ".")
import numpy as np, sympy as sp
from wave16_d1a_targeted import (Dm, snf_kernel, torsion_data,
                                 comp_supported, gamma_perms, lex_canon,
                                 group_ids)

def direct(m, q):
    D = Dm(m); Z, Qmod = torsion_data(m, D)
    pts = snf_kernel(m, q)
    fib = group_ids(np.sort(pts, axis=1))
    perms = gamma_perms(m)
    canon = lex_canon(pts, perms, chunk=500)
    gam = group_ids(canon)
    sup = comp_supported(pts, Z, Qmod, q)
    out = []
    for f in range(int(fib.max()) + 1):
        idx = np.where(fib == f)[0]
        opf = len(set(gam[idx].tolist()))
        if opf > 1:
            s = int(sup[idx].sum())
            out.append((int(len(idx)), opf, s, len(idx) == s, pts[idx[0]].tolist()))
    return out, pts, fib, gam, sup

def trace_model(m, p, f):
    """C in R/p^f; returns dict: fiber key -> list of (C, orbit id)."""
    mod = p ** f
    inv2 = pow(2, -1, mod); inv8 = pow(8, -1, mod)
    # alpha powers: A[j] = (a_j, b_j) for alpha^j in R/mod
    A = [(1, 0)]
    for _ in range(m):
        a, b = A[-1]
        A.append(((3 * a + 4 * b) % mod, (2 * a + 3 * b) % mod))
    # check alpha^m == 1
    assert A[m] == (1, 0), (m, p, f, A[m])
    # orbit of C: {C*alpha^j} U {conj(C)*alpha^j}, j < m
    def orbit_canon(a, b):
        best = None
        for j in range(m):
            aj, bj = A[j]
            # C * alpha^j
            x = (a * aj + 2 * b * bj) % mod
            y = (a * bj + b * aj) % mod
            if best is None or (x, y) < best: best = (x, y)
            # conj(C) * alpha^j
            x2 = (a * aj - 2 * b * bj) % mod
            y2 = (a * bj - b * aj) % mod
            if (x2, y2) < best: best = (x2, y2)
        return best
    fibers = {}
    for a in range(mod):
        for b in range(mod):
            # trace sequence
            tr = []
            for j in range(m):
                aj, bj = A[j]
                tr.append((2 * (a * aj + 2 * b * bj)) % mod)
            key = tuple(sorted(tr))
            fibers.setdefault(key, []).append(((a, b), orbit_canon(a, b)))
    return fibers

for (m, q) in [(12, 81), (21, 2401), (30, 625)]:
    fac = sp.factorint(q); p = list(fac)[0]; e = fac[p]; f = e // 2
    out, pts, fib, gam, sup = direct(m, q)
    onsup = [o for o in out if o[3]]
    print(f"== m={m} q={q} (p={p} f={f}): split fibers={len(out)} on-support={len(onsup)}")
    for (sz, opf, s, allsup, rep) in onsup:
        print(f"   size={sz} orbits={opf} supported={s} all={allsup}")
    # trace model
    fibers = trace_model(m, p, f)
    split_tm = {k: v for k, v in fibers.items() if len(set(o for _, o in v)) > 1}
    print(f"   trace model mod {p**f}: fibers={len(fibers)} split={len(split_tm)}")
    for k, v in split_tm.items():
        orbs = set(o for _, o in v)
        Cs = sorted(set(c for c, _ in v))
        print(f"   TM split: size={len(v)} orbits={len(orbs)} Cmod{p}={sorted(set((a % p, b % p) for a, b in Cs))}")
    # check kernel = p^f * trace model: every row divisible by p^f?
    print(f"   all rows divisible by {p**f}: {bool(np.all(pts % (p**f) == 0))}")
