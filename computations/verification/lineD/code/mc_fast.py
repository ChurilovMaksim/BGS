"""Fast Monte Carlo of E|Tr U^m|^2 for m = 1..8 only, U = exp(i eta V_theta) M_p, using M_p = Delta F_{1/4} Delta
(Line C Theorem 1 factorisation) and batched FFTs.  Same ensembles/seeding conventions as mc_band.py.
Usage: mc_fast.py ens p K eta a samples seed nproc"""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import os, sys
os.environ['OMP_NUM_THREADS'] = '1'; os.environ['OPENBLAS_NUM_THREADS'] = '1'
import numpy as np, multiprocessing as mpc
from scipy import fft as sfft
from dlib import MN
from mc_band import modes_amps
MMAX = 8
def make_apply(p):
    x = np.arange(p); inv8 = pow(8, -1, p); c = pow(4, -1, p)
    Dl = np.exp(-2j*np.pi*((3*inv8*x*x) % p)/p)
    perm = (c*x) % p
    def applyM(V):                     # M V for V of shape (p, ncols)
        W = Dl[:, None]*V
        W = sfft.ifft(W, axis=0)[perm]*np.sqrt(p)
        return Dl[:, None]*W
    return applyM
def traces(d, applyM, p):
    U1 = d[:, None]*applyM(np.eye(p, dtype=complex))
    U2 = d[:, None]*applyM(U1); U3 = d[:, None]*applyM(U2); U4 = d[:, None]*applyM(U3)
    t = np.empty(MMAX, complex)
    t[0] = np.trace(U1); t[1] = np.trace(U2); t[2] = np.trace(U3); t[3] = np.trace(U4)
    t[4] = np.sum(U4*U1.T); t[5] = np.sum(U4*U2.T); t[6] = np.sum(U4*U3.T); t[7] = np.sum(U4*U4.T)
    return t
def worker(args):
    ens, p, K, eta, a, S, seed = args
    rng = np.random.default_rng(seed); applyM = make_apply(p); x = np.arange(p)
    modes, amps = modes_amps(ens, K, a)
    C = np.array([np.exp(2j*np.pi*k*x/p) for k in modes])
    s1 = np.zeros(MMAX); s2 = np.zeros(MMAX)
    for _ in range(S):
        th = 2*np.pi*rng.random(len(modes))
        r = np.sqrt(rng.exponential(1.0, len(modes))) if ens == 'flatG' else np.ones(len(modes))
        v = np.real((np.array(amps)*r*np.exp(1j*th)) @ C)
        tr = np.abs(traces(np.exp(1j*eta*v), applyM, p))**2
        s1 += tr; s2 += tr*tr
    return s1, s2
if __name__ == '__main__':
    if sys.argv[1] == 'selftest':
        p = 37; M = MN(p); applyM = make_apply(p); rng = np.random.default_rng(1)
        d = np.exp(2j*np.pi*rng.random(p)); U = d[:, None]*M
        ref = np.array([np.trace(np.linalg.matrix_power(U, m)) for m in range(1, MMAX+1)])
        print('selftest max |diff| =', np.abs(traces(d, applyM, p) - ref).max(), ' |M - Delta F Delta| =', np.abs(applyM(np.eye(p, dtype=complex)) - M).max()); sys.exit()
    ens, p, K, eta, a, S, seed, npr = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8])
    with mpc.Pool(npr) as pool:
        res = pool.map(worker, [(ens, p, K, eta, a, S//npr, seed*1000+k) for k in range(npr)])
    s1 = sum(r[0] for r in res); s2 = sum(r[1] for r in res); n = (S//npr)*npr
    mean = s1/n; se = np.sqrt((s2/n - mean**2)/n)
    os.makedirs('../logs/mcfast', exist_ok=True)
    tag = f'{ens}_p{p}_K{K}_eta{eta}_a{a}_S{n}_seed{seed}'
    np.save(f'../logs/mcfast/{tag}.npy', np.vstack([mean, se]))
    with open(f'../logs/mcfast/{tag}.txt', 'w') as f:
        f.write(f'# {tag}\n'); [f.write(f'{m} {mean[m-1]:.6f} {se[m-1]:.6f}\n') for m in range(1, MMAX+1)]
    print('done', tag, flush=True)
