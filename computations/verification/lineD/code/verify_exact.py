"""V1: pathwise identity  Tr U^m = Tr M^m * sum_n Ghat(n) e_p(Dbar * A(n)),  A(n) = 2 n^T X n  (Theorem D1).
V2: pathwise identity at rational points  sum_n Ghat(n) e(s A(n)/D) = sum_{xi in Fix} phihat_s(xi) G(xi)  (Prop. D2).
V3: |Tr M^m| = 1 for p not dividing D_m."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, itertools, sys
from dlib import *
rng = np.random.default_rng(20261029)
def ghat(modes, amps, th, eta, Ng=4096, L=40):
    q = np.arange(Ng)/Ng
    v = sum(a*np.cos(2*np.pi*k*q + t) for k, a, t in zip(modes, amps, th))
    c = np.fft.fft(np.exp(1j*eta*v))/Ng
    n = np.arange(-L, L+1); return n, c[n % Ng]
def nside(m, n, gh, tnum, tden):
    """sum_{n in [-L,L]^m} prod ghat(n_j) e(tnum*A(n)/tden), exact integer phases."""
    X, D = Xmat(m)
    grids = np.meshgrid(*([n]*m), indexing='ij')
    N = [g.reshape(-1).astype(object) for g in grids]
    W = np.ones(len(N[0]), complex)
    for j in range(m): W = W*gh[(grids[j].reshape(-1) + n[-1])]
    A = sum(2*X[i][j]*N[i]*N[j] for i in range(m) for j in range(m))
    ph = np.array([(tnum*int(a)) % tden for a in A], dtype=float)/tden
    return (W*np.exp(2j*np.pi*ph)).sum()
out = []
worst1 = worst2 = 0
for (m, p, L) in [(3, 101, 30), (3, 103, 30), (3, 211, 30), (4, 101, 18), (4, 107, 18), (3, 13, 30), (4, 19, 18)]:
    D = Dm(m); assert D % p and p > 2
    modes = [1, 2, 3]; amps = [0.6, 0.4, 0.3]; eta = 1.0
    th = 2*np.pi*rng.random(3)
    n, gh = ghat(modes, amps, th, eta, L=L)
    M = MN(p); x = np.arange(p)
    v = sum(a*np.cos(2*np.pi*k*x/p + t) for k, a, t in zip(modes, amps, th))
    U = np.exp(1j*eta*v)[:, None]*M
    trU = np.trace(np.linalg.matrix_power(U, m)); trM = np.trace(np.linalg.matrix_power(M, m))
    Dbar = pow(D, -1, p)
    rhs = trM*nside(m, n, gh, Dbar, p)
    err = abs(trU - rhs); worst1 = max(worst1, err)
    out.append(f"V1 m={m} p={p} L={L}: TrU^m={trU:.12f}  formula={rhs:.12f}  |diff|={err:.2e}  |TrM^m|={abs(trM):.15f}")
# V2: rational points
for m in (3, 4):
    o = Orbits(m); D = o.D
    for s in (1, 5, 77):
        if math.gcd(s, D) != 1: continue
        modes = [1, 3]; amps = [0.7, 0.5]; eta = 1.3; th = 2*np.pi*rng.random(2)
        n, gh = ghat(modes, amps, th, eta, L=30 if m == 3 else 18)
        lhs = nside(m, n, gh, s, D)
        G = np.exp(1j*eta*sum(a*np.real(np.exp(1j*t)*o.Sk(k)) for k, a, t in zip(modes, amps, th)))
        rhs = (o.phihat(s)*G).sum()
        worst2 = max(worst2, abs(lhs-rhs))
        out.append(f"V2 m={m} s={s}: n-side={lhs:.12f}  orbit-side={rhs:.12f}  |diff|={abs(lhs-rhs):.2e}")
out.append(f"max V1 diff {worst1:.2e}; max V2 diff {worst2:.2e}")
print('\n'.join(out)); open('../logs/verify_exact.log', 'w').write('\n'.join(out)+'\n')
