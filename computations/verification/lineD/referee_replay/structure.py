if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, numpy as np
from fractions import Fraction
from math import gcd
from collections import defaultdict
import core

def units_mod(g):
    return [u for u in range(1, g) if gcd(u, g) == 1]

def rad_elems(dat, B):
    D = dat['D']; Xi = np.array(dat['X'], dtype=np.int64)
    keys = (B @ Xi.T) % D
    sel = np.all((4*keys) % D == 0, axis=1)
    return B[sel]

def supp_via_rad(dat, s, W, R):
    """|phihat_s(xi)|^2 = D^{-1} sum_{gamma in V[4]} e(2 s Q(gamma) - gamma.xi)  (own derivation)"""
    D = dat['D']; Xi = np.array(dat['X'], dtype=np.int64)
    q = (2*s*np.einsum('bi,ij,bj->b', R, Xi, R)) % D
    ph = (q[None, :] - (W @ R.T) % D) % D
    return np.real(np.exp(2j*np.pi*ph/D).sum(axis=1))/D

def main(m, direct=True, nS=4):
    dat = core.data(m); D = dat['D']; gp = dat['gp']
    W = core.enum_fix(dat); B = core.enum_V(dat)
    R = rad_elems(dat, B)
    print(f"m={m} D={D} g'={gp} |Fix|={len(W)} |V[4]|={len(R)}")
    us = units_mod(gp)
    # s ranges over units mod D; pick lifts of several residues mod g'
    svals = []
    for u in us[:nS] + us[-2:]:
        s = u
        while gcd(s, D) != 1: s += gp
        svals.append(s)
    canon, osz = core.gamma_canon(W, D)
    idx = {tuple(w): i for i, w in enumerate(W)}
    supports = []
    for s in svals:
        a2 = supp_via_rad(dat, s, W, R)
        supp = a2 > 1e-9
        lev = np.unique(np.round(a2[supp]*D, 6))
        line = f"  s={s} (s mod g'={s%gp}): rad-formula levels D|phi|^2 on supp = {lev}, |supp|={supp.sum()}"
        if direct:
            ph = core.phihat(dat, s, W, B)
            err = np.abs(np.abs(ph)**2 - a2).max()
            # Gamma invariance and parity invariance of phihat (phase included)
            errG = 0.0
            for r in range(m):
                for rev in (False, True):
                    W2 = np.roll(W, r, axis=1)
                    if rev: W2 = W2[:, ::-1]
                    j = np.array([idx[tuple(w)] for w in W2])
                    errG = max(errG, np.abs(ph[j]-ph).max())
            jpar = np.array([idx[tuple((-w) % D)] for w in W])
            errP = np.abs(ph[jpar]-ph).max()
            line += f" | direct-vs-rad {err:.1e} | Gamma-inv {errG:.1e} | parity-inv {errP:.1e} | sum phihat = {ph.sum():.12f}"
        print(line)
        supports.append(supp)
    same = all((sp == supports[0]).all() for sp in supports)
    supp = supports[0]
    Deff = int(supp.sum())
    print(f"  support s-independent over tested s: {same}; D_eff={Deff}; D/D_eff={D/Deff}")
    # Gamma-invariance of the support
    Bsym = Fraction(int(osz[supp].sum()), Deff)
    print(f"  B_sym = {Bsym} = {float(Bsym):.6f}; 2m - B_sym = {2*m - float(Bsym):.6f}")
    print(f"  #support points with |Gamma xi|<2m: {(osz[supp] < 2*m).sum()};  D_eff odd: {Deff%2==1}; 2m | D_eff: {Deff % (2*m) == 0}")
    # multiset => Gamma on the support (exact, integer)
    ms = defaultdict(set)
    for i in np.where(supp)[0]:
        ms[tuple(sorted(W[i]))].add(canon[i])
    bad = [k for k, v in ms.items() if len(v) > 1]
    print(f"  multiset classes on supp: {len(ms)}; Gamma classes on supp: {len(set(canon[i] for i in np.where(supp)[0]))}; multisets containing >1 Gamma class: {len(bad)}")
    # same on full Fix
    msF = defaultdict(set)
    for i in range(len(W)): msF[tuple(sorted(W[i]))].add(canon[i])
    print(f"  (full Fix_m) multisets containing >1 Gamma class: {sum(1 for v in msF.values() if len(v)>1)}")
    # K=1 and K={1,2} separation (floats; report min gaps)
    sidx = np.where(supp)[0]
    reps = {}
    for i in sidx: reps.setdefault(canon[i], i)
    ri = np.array(list(reps.values()))
    for Ks in ([1], [1, 2], [1,2,3]):
        P = np.stack([core.Sk(W[ri], D, k) for k in Ks], axis=1)
        # pairwise distances over Gamma-class representatives
        n = len(ri); mind = np.inf; ncoll = 0; collset = set()
        for a in range(0, n, 500):
            d = np.sqrt((np.abs(P[a:a+500, None, :] - P[None, :, :])**2).sum(axis=2))
            for i in range(d.shape[0]): d[i, a+i] = np.inf
            c = np.argwhere(d < 1e-9)
            for (i, j) in c: collset.add(a+i); collset.add(j)
            mind = min(mind, d[d >= 1e-9].min())
        print(f"  K={Ks}: Gamma-class reps in collisions (tol 1e-9): {len(collset)}; min nonzero gap = {mind:.3e}")
        if Ks == [1] and collset:
            cl = sorted(collset)
            hti = [all(((W[ri[c]] + D//2) % D).tolist().count(x) == W[ri[c]].tolist().count(x) for x in W[ri[c]]) for c in cl]
            S1 = np.abs(P[cl, 0]).max()
            print(f"    collision reps all half-turn-invariant multisets: {all(hti)}; max |S_1| among them: {S1:.2e}")
    return dat, W, supp

if __name__ == '__main__':
    m = int(sys.argv[1]); direct = (sys.argv[2] == '1') if len(sys.argv) > 2 else True
    main(m, direct)
