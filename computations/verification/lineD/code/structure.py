"""Structure of Fix_m and of the Gauss weights phihat_s: support, |phihat|^2, Gamma-classes, parity, multiset classes,
and K-resolution (which Fourier sets {1..K} separate multiset classes). Exact integer arithmetic for orbits;
power sums compared in floating point with a reported gap."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, math, sys
from dlib import *
out = []
def log(s): print(s); out.append(s)
for m in range(3, int(sys.argv[1]) + 1 if len(sys.argv) > 1 else 9):
    o = Orbits(m); D = o.D
    # residues s coprime to D (s = -pbar mod D); test a few
    ss = [s for s in range(1, 60) if math.gcd(s, D) == 1][:4]
    for s in ss:
        ph = o.phihat(s); a2 = np.abs(ph)**2
        supp = a2 > 0.5/D**1.0*1e-6
        vals = np.unique(np.round(a2[supp]*D, 6))
        log(f"m={m} D={D} s={s}: |supp|={supp.sum()}  D*|phihat|^2 values on supp={vals}  sum phihat={ph.sum():.12f}")
    s = ss[0]; ph = o.phihat(s); supp = np.abs(ph)**2 > 1e-6/D; Deff = supp.sum()
    lab, cnt = gamma_classes(o)
    mlab, mcnt = multiset_classes(o)
    sizes = cnt[lab]
    # invariance of phihat under Gamma / parity
    rot = np.roll(o.Xi, 1, axis=1); # check phihat constant on classes
    dev = 0.0
    for c in range(len(cnt)):
        pass
    # vectorised: compare phihat over class via sorting
    order = np.argsort(lab); pl = ph[order]; ll = lab[order]
    starts = np.r_[0, np.flatnonzero(np.diff(ll)) + 1]
    mx = np.maximum.reduceat(np.abs(pl - np.repeat(pl[starts], np.diff(np.r_[starts, len(ll)]))), starts).max()
    log(f"  Gamma-classes: {len(cnt)}, size histogram {dict(zip(*np.unique(cnt, return_counts=True)))}; max |phihat - phihat(rep)| on classes = {mx:.2e}")
    # parity: -xi
    negXi = (-o.Xi) % o.d2
    # find class of -xi via multiset key
    key = {tuple(r): i for i, r in enumerate(np.sort(o.Xi, axis=1).tolist())} if D < 300000 else None
    # Gamma classes vs multiset classes
    nm = len(mcnt)
    # each multiset class is a union of Gamma classes; count Gamma classes per multiset class
    pairs = np.unique(np.stack([mlab, lab], 1), axis=0)
    per = np.bincount(pairs[:, 0])
    extra = np.flatnonzero(per > 1)
    log(f"  multiset classes: {nm}; multiset classes containing >1 Gamma-class: {len(extra)}")
    for e in extra[:6]:
        idx = np.flatnonzero(mlab == e)
        reps = {}
        for i in idx: reps.setdefault(lab[i], i)
        log(f"    arithmetic coincidence: multiset {sorted(o.Xi[idx[0]].tolist())}/{o.d2}, Gamma-classes {[(int(c), int(cnt[c])) for c in reps]}, orbits {[o.Xi[i].tolist() for i in reps.values()]}, in support: {[bool(supp[i]) for i in reps.values()]}")
    # parity classes: is -xi in Gamma xi?
    nkey = np.sort(negXi, axis=1)
    same = np.all(nkey == np.sort(o.Xi, axis=1), axis=1)
    log(f"  orbits with -xi same multiset as xi: {same.sum()} (in support: {(same & supp).sum()})")
    # Gamma-diagonal value: (1/Deff) sum_{xi in supp} |Gamma xi|  and with multiset classes
    gd = (sizes[supp]).sum()/Deff
    msz = np.bincount(mlab, weights=supp.astype(float))
    # sum over multiset classes |sum phihat|^2
    cs = np.bincount(mlab, weights=ph.real) + 1j*np.bincount(mlab, weights=ph.imag)
    log(f"  Gamma-diagonal value (1/Deff) sum_supp |Gamma xi| = {gd:.6f}  (2m = {2*m});  sum_multiset-classes |sum phihat|^2 = {np.sum(np.abs(cs)**2):.6f}")
    # K-resolution: separate multiset classes with S_1..S_K
    reps = np.unique(mlab, return_index=True)[1]
    Sks = np.stack([o.Sk(k)[reps] for k in range(1, m+1)], 1)
    for K in range(1, m+1):
        F = Sks[:, :K]
        # sort by rounded key and check collisions; report min distance between distinct classes via grid hashing
        R = np.round(np.concatenate([F.real, F.imag], 1), 7)
        _, inv, c2 = np.unique(R, axis=0, return_inverse=True, return_counts=True)
        ncoll = int((c2 > 1).sum())
        # min nonzero distance (approx via nearest neighbours after sorting along random projection)
        Z = np.concatenate([F.real, F.imag], 1)
        best = np.inf
        for t in range(6):
            w = np.random.default_rng(t).normal(size=Z.shape[1]); pr = Z @ w; od = np.argsort(pr)
            for sh in range(1, 40):
                d = np.linalg.norm(Z[od[sh:]] - Z[od[:-sh]], axis=1)
                d = d[d > 1e-6]
                if len(d): best = min(best, d.min())
        log(f"  K={K}: collisions among {len(reps)} multiset classes (to 1e-7): {ncoll} groups; approx min nonzero |Delta P_K| = {best:.3e}")
        if ncoll == 0: break
open(f'../logs/structure.log', 'w').write('\n'.join(out) + '\n')
