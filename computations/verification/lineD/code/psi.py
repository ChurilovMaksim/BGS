"""Leading term Psi_m(s/D) and 1/p coefficient c_1 of E_theta|Tr U^m|^2 in the fixed-mode-set limit (Theorem D2/D3).
Psi(s/D) = sum_{xi,xi' in Fix} phihat_s(xi) conj(phihat_s(xi')) prod_k omega_k(eta (S_k(xi)-S_k(xi'))),
omega = J_0(a|z|) (uniform phases) or exp(-a^2|z|^2/4) (circular Gaussian coefficient, E|c|^2 = a^2).
c_1 = (2/pi) Im E[ conj(Z) * sum_xi phihat(xi) br(xi) G(xi) ],  br = i eta h0 sum_i v''(xi_i) - eta^2 v'(xi)^T H^{-1} v'(xi).
Computation is reduced to Gamma-classes inside the support of phihat (phihat is Gamma- and parity-invariant)."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, math
from scipy.special import j0
from dlib import *

class Setup:
    def __init__(self, m, s):
        o = Orbits(m); self.o = o; self.m = m; self.s = s; self.D = o.D
        ph = o.phihat(s); supp = np.abs(ph)**2 > 1e-6/o.D
        lab_s, cnt = gamma_classes(o, o.Xi[supp]); ph_s = ph[supp]
        u, first, inv, c = np.unique(lab_s, return_index=True, return_inverse=True, return_counts=True)
        idx = np.flatnonzero(supp)[first]
        self.rep = o.Xi[idx]                      # representative orbits (integers mod d2)
        self.w = c*ph_s[first]                    # class weight |O| phihat_O
        self.size = c
        self.Deff = supp.sum()
        # parity partner class index
        key = {tuple(sorted(r)): i for i, r in enumerate(self.rep.tolist())}
        self.par = np.array([key.get(tuple(sorted(((-np.array(r)) % o.d2).tolist())), -1) for r in self.rep.tolist()])
        X, D = Xmat(m); self.Hinv = np.array(X, float)/D
        self.q = self.rep/o.d2                    # points in [0,1)
    def Sk(self, k):
        return np.exp(2j*np.pi*k*self.q).sum(axis=1)
    def gamma_diag(self):
        return float(np.sum(np.abs(self.w)**2))

def psi_exact(st, modes, amps, eta, ens='J0', decompose=False):
    S = [st.Sk(k) for k in modes]; w = st.w; n = len(w)
    tot = 0.0; diag = 0.0; par = 0.0
    B = 2000
    for i0 in range(0, n, B):
        sl = slice(i0, min(n, i0+B))
        Wm = np.ones((sl.stop-sl.start, n))
        for Sk_, a in zip(S, amps):
            z = np.abs(Sk_[sl, None] - Sk_[None, :])*eta*a
            Wm *= j0(z) if ens == 'J0' else np.exp(-z*z/4)
        T = (w[sl, None]*np.conj(w)[None, :])*Wm
        tot += T.sum().real
        if decompose:
            ii = np.arange(sl.start, sl.stop)
            diag += T[ii-sl.start, ii].sum().real
            pj = st.par[ii]; ok = (pj >= 0) & (pj != ii)
            par += T[(ii-sl.start)[ok], pj[ok]].sum().real
    return (tot, diag, par, tot-diag-par) if decompose else tot

def sample_theta(rng, K, ens, nsamp):
    th = 2*np.pi*rng.random((nsamp, K))
    if ens == 'J0': r = np.ones((nsamp, K))
    else: r = np.sqrt(rng.exponential(1.0, (nsamp, K)))   # |c| Rayleigh with E|c|^2 = a^2  (a multiplies)
    return th, r

def psi_c1_mc(st, modes, amps, eta, nsamp, seed, ens='J0', batch=200):
    """Monte Carlo over theta of |Z|^2 and (2/pi) Im conj(Z) Y.  Returns means and standard errors."""
    rng = np.random.default_rng(seed)
    m = st.m; q = st.q; w = st.w
    E = [np.exp(2j*np.pi*k*q) for k in modes]        # (nclass, m)
    h0 = st.Hinv[0, 0]
    acc = []; acc1 = []
    done = 0
    while done < nsamp:
        b = min(batch, nsamp-done)
        th, r = sample_theta(rng, len(modes), ens, b)
        for t in range(b):
            c = [amps[i]*r[t, i]*np.exp(1j*th[t, i]) for i in range(len(modes))]
            v = sum(np.real(ci*Ei) for ci, Ei in zip(c, E))
            vp = sum(np.real(2j*np.pi*k*ci*Ei) for k, ci, Ei in zip(modes, c, E))
            vpp = sum(np.real(-(2*np.pi*k)**2*ci*Ei) for k, ci, Ei in zip(modes, c, E))
            G = np.exp(1j*eta*v.sum(axis=1))
            br = 1j*eta*h0*vpp.sum(axis=1) - eta**2*np.einsum('ni,ij,nj->n', vp, st.Hinv, vp)
            Z = (w*G).sum(); Y = (w*br*G).sum()
            acc.append(abs(Z)**2); acc1.append((2/np.pi)*(np.conj(Z)*Y).imag)
        done += b
    a = np.array(acc); a1 = np.array(acc1)
    return a.mean(), a.std()/math.sqrt(len(a)), a1.mean(), a1.std()/math.sqrt(len(a1))

def psi_c1_quad(st, modes, amps, eta, Q=None):
    """exact theta-average for uniform phases via product trapezoid rule (exact up to aliasing; K <= 2)."""
    K = len(modes); m = st.m
    if Q is None: Q = int(2*(eta*max(amps)*m + 40))
    grids = np.meshgrid(*([2*np.pi*np.arange(Q)/Q]*K), indexing='ij')
    ths = np.stack([g.reshape(-1) for g in grids], 1)
    q = st.q; w = st.w; E = [np.exp(2j*np.pi*k*q) for k in modes]; h0 = st.Hinv[0, 0]
    a = 0.0; a1 = 0.0
    for th in ths:
        c = [amps[i]*np.exp(1j*th[i]) for i in range(K)]
        v = sum(np.real(ci*Ei) for ci, Ei in zip(c, E))
        vp = sum(np.real(2j*np.pi*k*ci*Ei) for k, ci, Ei in zip(modes, c, E))
        vpp = sum(np.real(-(2*np.pi*k)**2*ci*Ei) for k, ci, Ei in zip(modes, c, E))
        G = np.exp(1j*eta*v.sum(axis=1))
        br = 1j*eta*h0*vpp.sum(axis=1) - eta**2*np.einsum('ni,ij,nj->n', vp, st.Hinv, vp)
        Z = (w*G).sum(); Y = (w*br*G).sum()
        a += abs(Z)**2; a1 += (2/np.pi)*(np.conj(Z)*Y).imag
    return a/len(ths), a1/len(ths)

def class_weights(st, s):
    """class weights w_O(s) = |O| phihat_s(O) in the class order of st (support is s-independent, checked)."""
    o = st.o; ph = o.phihat(s)
    if not hasattr(st, '_first'):
        supp = np.abs(o.phihat(st.s))**2 > 1e-6/o.D
        lab_s, cnt = gamma_classes(o, o.Xi[supp])
        u, first, c = np.unique(lab_s, return_index=True, return_counts=True)
        st._first = np.flatnonzero(supp)[first]; st._supp = supp
    assert np.array_equal(np.abs(ph)**2 > 1e-6/o.D, st._supp)
    return st.size*ph[st._first]

def residues(m):
    """units r mod g'_m up to sign, each lifted to a unit s mod D_m."""
    from dlib import pell
    xs, ys = pell(m); D = 2*(xs[m]-1); g = (xs[m]-1)//math.gcd(ys[m], xs[m]-1)
    out = []; seen = set()
    for r in range(1, g):
        if math.gcd(r, g) != 1 or r in seen: continue
        seen.add(r); seen.add((-r) % g)
        s = r
        while math.gcd(s, D) != 1: s += g
        out.append((r, s))
    return g, out

def kernel(st, modes, amps, eta, ens):
    S = [st.Sk(k) for k in modes]; n = len(st.w)
    Wm = np.ones((n, n))
    for Sk_, a in zip(S, amps):
        z = np.abs(Sk_[:, None] - Sk_[None, :])*eta*a
        Wm *= j0(z) if ens == 'J0' else np.exp(-z*z/4)
    return Wm

def psi_infinity(st, K, ws, tol=1e-9):
    """eta -> infinity limit: sum over P_K-equality classes of |sum w|^2 (classes found by exact-to-tol clustering)."""
    F = np.stack([st.Sk(k) for k in range(1, K+1)], 1)
    R = np.round(np.concatenate([F.real, F.imag], 1)/tol).astype(np.int64)
    _, inv = np.unique(R, axis=0, return_inverse=True); inv = inv.reshape(-1)
    return [float(np.sum(np.abs(np.bincount(inv, weights=w.real) + 1j*np.bincount(inv, weights=w.imag))**2)) for w in ws], int(inv.max()+1)

def c1_gauss_exact(st, modes, amps, eta, w=None, B=400):
    """Exact 1/p coefficient c_1 for the circular-Gaussian ensemble (E|c_k|^2 = a_k^2), by the Gaussian tilting formula:
    E[G(xi)conj G(xi') beta(xi)] = f * b,  f = prod_k exp(-a_k^2 eta^2 |Delta_k|^2/4),
    b = -eta h0 sum_i r2_i - eta^2 (H^{-1}:C - r^T H^{-1} r)  (real),
    r_i = (eta/2) sum_k a_k^2 Re(2 pi i k u_k(i) conj Delta_k),  r2_i = (eta/2) sum_k a_k^2 Re(-(2 pi k)^2 u_k(i) conj Delta_k),
    C_ij = sum_k 2 pi^2 k^2 a_k^2 cos(2 pi k (xi_i - xi_j)).   c_1 = (2/pi) sum Im(w_O conj w_O') f b."""
    w = st.w if w is None else w
    q = st.q; n, m = q.shape; Hinv = st.Hinv; h0 = Hinv[0, 0]
    S = np.stack([st.Sk(k) for k in modes], 1)                       # (n, K)
    u = np.stack([np.exp(2j*np.pi*k*q) for k in modes], 2)          # (n, m, K)
    kk = np.array(modes, float); a2 = np.array(amps, float)**2
    dq = q[:, :, None] - q[:, None, :]
    C = np.einsum('k,nijk->nij', 2*np.pi**2*kk**2*a2, np.cos(2*np.pi*dq[..., None]*kk))
    HC = np.einsum('ij,nij->n', Hinv, C)                               # (n,)
    U1 = 2j*np.pi*kk*u; U2 = -(2*np.pi*kk)**2*u
    tot = 0.0
    for i0 in range(0, n, B):
        sl = slice(i0, min(n, i0+B))
        Dl = S[sl, None, :] - S[None, :, :]                              # (b, n, K)
        f = np.exp(-(eta**2/4)*np.sum(a2*np.abs(Dl)**2, axis=2))
        r = (eta/2)*np.einsum('k,bik,bjk->bji', a2, U1[sl].real, Dl.real) + (eta/2)*np.einsum('k,bik,bjk->bji', a2, U1[sl].imag, Dl.imag)
        r2 = (eta/2)*np.einsum('k,bik,bjk->bj', a2, U2[sl].real, Dl.real) + (eta/2)*np.einsum('k,bik,bjk->bj', a2, U2[sl].imag, Dl.imag)
        rHr = np.einsum('bji,ik,bjk->bj', r, Hinv, r)
        b = -eta*h0*r2 - eta**2*(HC[sl, None] - rHr)
        tot += np.sum(np.imag(w[sl, None]*np.conj(w)[None, :])*f*b)
    return (2/np.pi)*tot
