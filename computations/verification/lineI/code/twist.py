"""Twisted G2 operators for dilation analysis.  L(tau) = sum_n ghat(n) e(n tau) e(coef n^2/2) MC_n (x) P_n  on H^2(D_rho) (x) C^{b^2}.
Untwisted = Line G law (Z_rho).  Twisted by tau_i = Tr(beta lam^i)/d  gives Zhat(beta) = sum_n w(n) e(Tr(beta alpha_n)/d)."""
import numpy as np, math, sys, json
from law import mdata, MC, kick_ghat, LAM
def build(m, a, b, gh, rho, K):
    D = mdata(m); h = D['h']; yp = D['yp']; M = 2*h
    nu = next(x for x in [((a//2)*pow(b//2, -1, h)) % h + s*h for s in (0, 1)] if x % 2 == 1)
    assert (b*nu-a) % M == 0
    k = (b*nu-a)//M
    coef = -4*a*(1/(LAM-1/LAM))/b
    psi0 = yp % b; psi1 = (3*yp-2*h) % b; S = b*b
    us = np.arange(S)//b; ws = np.arange(S) % b
    parts = {}
    for n, gn in gh.items():
        if abs(gn) == 0: continue
        Mn = gn*np.exp(2j*np.pi*coef*n*n/2)*MC(n, coef, rho, K)
        ph = np.exp(-2j*np.pi*((k*((psi0*n*n+2*n*us) % b)) % b)/b)
        tgt = (((6*us-ws+n*psi1) % b)*b+((us+n*psi0) % b))
        P = np.zeros((S, S), complex); P[tgt, np.arange(S)] = ph
        parts[n] = (Mn, P)
    return parts, nu, S
def op(parts, tau=0.0):
    return sum(np.exp(2j*np.pi*n*tau)*np.kron(Mn, P) for n, (Mn, P) in parts.items())
def Zfrom(Lprod_list, m, S, K):
    """Z = (1-lam^-m) sum_s Tr_H[(L_{m-1}...L_0)_{(.,s),(.,0)}]; Lprod_list = list of m operators (applied in order)."""
    X = np.zeros((K*S, K), complex)
    for j in range(K): X[j*S+0, j] = 1
    for L in Lprod_list: X = L@X
    X = X.reshape(K, S, K)
    return (1-LAM**(-m))*np.einsum('isi->', X)
if __name__ == '__main__':
    gh = kick_ghat('k1', 2.0, 10)
    for m in (9, 15):
        parts, nu, S = build(m, 2, 8, gh, 2.6, 40); L = op(parts); K = 40
        ev = np.linalg.eigvals(L); ev = ev[np.argsort(-abs(ev))]
        Z = Zfrom([L]*m, m, S, K)
        print(f'm={m} nu={nu} top |eig|: {np.round(abs(ev[:6]),6)}  |Z|^2 law={abs(Z)**2:.6g}', flush=True)
