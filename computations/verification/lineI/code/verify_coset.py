"""Exact check of the dilation-coset L^2 law (Line I, Prop I2), brute force over all words, random complex weights.
For d prime, d || h:  with w(n)=Phihat(n)e(-nu0 P(n)/2h), W(gamma)=sum_{alpha_n≡gamma (d)} w(n), W_u = sum_{Nm gamma≡u} W(gamma),
Z_t := sum_gamma W(gamma) e(-t Nm(gamma)/d)  [= Z(nu0+2hj/d), t=j y' mod d],  N(u)=#{gamma: Nm gamma≡u}, eps=(2|d),
delta_u = W_u - Z0 N(u)/d^2, Z0 = sum W:
 (a) Z(nu0+2hj/d) = Z_{j y'}                                     (direct, all j)
 (b) sum_{t mod d}|Z_t|^2 = d sum_u |W_u|^2                        (coset Parseval)
 (c) sum_{t != 0}|Z_t|^2 = |Z0|^2 (1/d-1/d^2) + 2 eps Re(conj(Z0) delta_0) + d sum_u|delta_u|^2
 (d) N(u)=d-eps (u!=0), N(0)=d+(d-1)eps."""
import numpy as np, itertools, math, sys
from law import mdata, pell
def run(m, L, d, seed):
    rng = np.random.default_rng(seed); D = mdata(m); h = D['h']; yp = D['yp']; assert h % d == 0 and (h//d) % d != 0
    vals = np.arange(-L, L+1); gh = rng.normal(size=2*L+1)+1j*rng.normal(size=2*L+1)
    grid = np.array(list(itertools.product(range(2*L+1), repeat=m)), dtype=np.int64); n = vals[grid]
    MOD = 2*h
    psi = np.array([[(yp*pell(abs(i-j))[0]-2*h*pell(abs(i-j))[1]) % MOD for j in range(m)] for i in range(m)], dtype=np.int64)
    Pm = np.zeros(len(n), dtype=np.int64)
    for i in range(m):
        for j in range(m): Pm = (Pm+psi[i, j]*((n[:, i]*n[:, j]) % MOD)) % MOD
    W0 = np.prod(gh[grid], axis=1)
    units = [x for x in range(1, 2*h, 2) if math.gcd(x, 2*h) == 1]; nu0 = units[rng.integers(len(units))]
    w = W0*np.exp(-2j*np.pi*((nu0*Pm) % MOD)/MOD)
    # alpha_n mod d
    x = np.zeros(len(n), np.int64); y = np.zeros(len(n), np.int64); lx, ly = 1, 0
    for i in range(m): x = (x+n[:, i]*lx) % d; y = (y+n[:, i]*ly) % d; lx, ly = (3*lx+4*ly) % d, (2*lx+3*ly) % d
    Wg = np.zeros((d, d), complex); np.add.at(Wg, (x, y), w)
    X, Y = np.meshgrid(np.arange(d), np.arange(d), indexing='ij'); Nmg = (X*X-2*Y*Y) % d
    Wu = np.zeros(d, complex); np.add.at(Wu, Nmg.ravel(), Wg.ravel()); Nu = np.bincount(Nmg.ravel(), minlength=d)
    eps = 1 if pow(2, (d-1)//2, d) == 1 else -1
    okd = all(Nu[u] == d-eps for u in range(1, d)) and Nu[0] == d+(d-1)*eps
    Z0 = w.sum(); Zt = np.array([np.sum(Wu*np.exp(-2j*np.pi*t*np.arange(d)/d)) for t in range(d)])
    ea = 0
    for j in range(d):
        nu = nu0+(2*h//d)*j; Zd = np.sum(W0*np.exp(-2j*np.pi*((nu*Pm) % MOD)/MOD))
        ea = max(ea, abs(Zd-Zt[(j*yp) % d])/max(1, abs(Zd)))
    lhs = np.sum(abs(Zt)**2); rhs = d*np.sum(abs(Wu)**2); eb = abs(lhs-rhs)/rhs
    dl = Wu-Z0*Nu/d**2
    rc = abs(Z0)**2*(1/d-1/d**2)+2*eps*np.real(np.conj(Z0)*dl[0])+d*np.sum(abs(dl)**2)
    ec = abs(np.sum(abs(Zt[1:])**2)-rc)/rc
    print(f'm={m} d={d} eps={eps:+d} nu0={nu0} words={len(n)}: (a) {ea:.1e} (b) {eb:.1e} (c) {ec:.1e} (d) {okd}  '
          f'[cross={2*eps*np.real(np.conj(Z0)*dl[0]):.3g}, square={d*np.sum(abs(dl)**2):.3g}, main={abs(Z0)**2*(1/d-1/d**2):.3g}]', flush=True)
    return max(ea, eb, ec), okd
r = [run(5, 2, 41, s) for s in range(3)]+[run(9, 1, 7, s) for s in range(3)]+[run(11, 1, 23, s) for s in range(2)]+[run(7,1,239,0)]
print('MAXERR', max(e for e, _ in r), 'N(u) law all', all(o for _, o in r))
