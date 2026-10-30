"""Galerkin sections of the vector-valued IFS operators of the a^2-resonance law (float, exploration/verification).
 (L_b phi)(u, sig) = sum_n ghat(n) e( s c (x_n u + x_n^2/2) + b n/8 + gamma (n sig + n^2/2)/a^2 ) phi((u + x_n)/lam, lam_a^{-1}(sig + n)),
 x_n = n/a,  on H^2(D_rho) (x) l^2(Z/a^2).  Z_m(nu_res) = sum_b c_b (1 - lam^-m) Tr L_b^m  (b even)."""
import numpy as np, math
from scipy.special import gammaln
from lawlib import *
def MC(x, coef, rho, K):
    """matrix of phi -> e(coef*x*u) phi((u+x)/lam) in basis (u/rho)^k"""
    l = np.arange(K); d = l[:, None] - l[None, :]
    if x == 0:
        return np.diag(LAM**(-l.astype(float))).astype(complex)
    z = 2j*np.pi*coef*x*rho
    dd = np.where(d >= 0, d, 0)
    M = np.where(d >= 0, np.exp(dd*np.log(z + 0j) - gammaln(dd + 1)), 0)
    kk = l[None, :]; jj = l[:, None]; e = kk - jj; ee = np.where(e >= 0, e, 0)
    logb = gammaln(kk + 1) - gammaln(jj + 1) - gammaln(ee + 1)
    C = np.where(e >= 0, np.exp(logb - kk*np.log(LAM) + ee*np.log(abs(x)/rho))*np.sign(x)**ee, 0)
    return M @ C
def DP(n, P):
    A2 = P['a']**2; g = P['gamma']; li = P['lami']; inv2 = pow(2, -1, A2)
    Mx = np.zeros((A2, A2), complex)
    for sg in range(A2):
        tgt = (li*(sg + n)) % A2
        Mx[sg, tgt] = np.exp(2j*np.pi*((g*(n*sg + inv2*n*n)) % A2)/A2)
    return Mx   # (DP phi)(sig) = sum_tau Mx[sig,tau] phi(tau);  as operator on coefficient vectors use Mx^T
def build(ghat, m, a, s, b, rho, K, root=None, Nfin=None):
    P = law_params(m, a, s, root) if a > 1 else law_params(m, 1, s)
    A2 = a*a if a > 1 else 1
    Op = np.zeros((K*A2, K*A2), complex)
    for n, gn in ghat.items():
        if gn == 0: continue
        x = n/a
        cc = s*C0*(1 + s*4*a*a/Nfin) if Nfin else s*C0   # finite N (TRACE-163 Thm 1 factor e(2q/N)): c -> c(1 + s 4a^2/N)
        w = gn*np.exp(2j*np.pi*(cc*x*x/2 + b*n/8))
        R = MC(x, cc, rho, K)
        if a > 1:
            Op += w*np.kron(R, DP(n, P).T)
        else:
            Op += w*R
    return Op, P
def csec(kappa):
    return [np.mean([np.exp(2j*np.pi*(kappa*t*t - b*t)/8) for t in range(8)]) for b in range(8)]
def Z_TO(ghat, m, a, s, rho, K, root=None, return_eigs=False, Nfin=None):
    P = law_params(m, a, s, root) if a > 1 else law_params(m, 1, s)
    cs = csec(P['kappa']); Z = 0; eig = {}
    for b in range(8):
        if abs(cs[b]) < 1e-12: continue
        Op, _ = build(ghat, m, a, s, b, rho, K, root, Nfin)
        ev = np.linalg.eigvals(Op); eig[b] = ev
        Z += cs[b]*(1 - LAM**(-m))*np.sum(ev**m)
    return (Z, eig, P) if return_eigs else Z
