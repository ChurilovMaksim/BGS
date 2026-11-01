"""Auditor: Prop. G (orbit/Gauss-completed form) vs brute-force n-sum Z_m(nu) = sum_n Phihat(n) e(-nu y' Nm(alpha_n)/g')
for a generic NON-even complex-coefficient real kick (so sign/conjugation errors in Prop G would show), all units nu."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import numpy as np, itertools, math, sys
def pell(d):
    x, y = 1, 0
    for _ in range(d): x, y = 3*x + 8*y, x + 3*y
    return x, y
def f(q): return 0.35*np.cos(2*np.pi*q) + 0.2*np.sin(4*np.pi*q) + 0.15*np.cos(6*np.pi*q + 0.4) + 0.1*np.sin(2*np.pi*q - 1.1)
def run(m, eta, L):
    xm, ym = pell(m); h = int(round(math.sqrt((xm - 1)//2))); assert 2*h*h == xm - 1; yp = ym//h; gp = 2*h
    M = 1 << 14; qq = np.arange(M)/M; ghat = np.fft.fft(np.exp(1j*eta*f(qq)))/M   # ghat[n] = int g e(-nq)
    ns = np.arange(-L, L+1); w = ghat[ns % M]
    X = np.array([[pell(abs(i-j))[0] for j in range(m)] for i in range(m)], dtype=np.int64)
    grid = np.array(np.meshgrid(*([ns]*m), indexing='ij')).reshape(m, -1).T.astype(np.int64)
    Nm = np.einsum('ki,ij,kj->k', grid, X, grid)
    W = np.prod(w[grid + L], axis=1)
    a, b = [1, 0], [0, 1]
    for j in range(2, m): a.append(6*a[-1] - a[-2]); b.append(6*b[-1] - b[-2])
    worst = 0; out = []
    for nu in range(1, gp, 2):
        if math.gcd(nu, gp) != 1: continue
        ph = (-nu*yp*Nm) % gp
        Zn = np.sum(W*np.exp(2j*np.pi*ph/gp))
        t = pow(16*nu % h, -1, h); S = 0
        for z0 in range(h):
            for z1 in range(h):
                z = [(a[j]*z0 + b[j]*z1) for j in range(m)]
                Hz = [6*z[j] - z[(j+1) % m] - z[(j-1) % m] for j in range(m)]
                R = (2*sum(z[j]*Hz[j] for j in range(m))//h) % h
                S += np.exp(2j*np.pi*t*R/h)*np.prod(np.exp(1j*eta*f(0.5 + np.array(z) % h/h)))
        ZG = abs(S)/h
        rel = abs(abs(Zn) - ZG)/abs(Zn); worst = max(worst, rel); out.append((nu, abs(Zn), ZG, rel))
    return worst, out
if __name__ == '__main__':
    for m, eta, L in ((3, 0.8, 14), (5, 0.8, 9), (5, 1.6, 10)):
        worst, out = run(m, eta, L)
        print(f'm={m} eta={eta} L={L} units={len(out)} worst rel |Z| diff = {worst:.2e}')
        for r in out[:4]: print('   nu=%d |Z|nsum=%.12f |Z|propG=%.12f rel=%.1e' % r)
