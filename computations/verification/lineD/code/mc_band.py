"""Monte Carlo E|Tr U^m|^2, m = 1..2p, for U = exp(i eta V_theta) M_p, band-limited kick
V_theta(x) = sum_{k in modes} a_k |c_k| cos(2 pi k x/p + theta_k)   (theta_k iid uniform; |c_k| = 1 ('J0') or Rayleigh with E|c|^2=1 ('G')).
Usage: mc_band.py ens p K eta a samples seed nproc     ens in {flat, flatG, diag7}
Deterministic seeds: worker k uses seed*1000+k. Output: ../logs/mc/<tag>.npy (mean, se) and a text log."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import os, sys
os.environ.setdefault('OMP_NUM_THREADS', '1'); os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import numpy as np, multiprocessing as mpc
from dlib import MN
DIAG7 = [(9, 0.0025), (8, 2*abs(-0.025-0.0025j)), (7, 0.9), (6, 2*abs(-0.025+0.0025j)), (5, 0.0025), (2, 0.005), (1, 2*abs(0.05+0.005j))]
def modes_amps(ens, K, a):
    if ens == 'diag7': return [k for k, _ in DIAG7], [c for _, c in DIAG7]
    if ens == 'k7only': return [7], [0.9]          # dominant mode of diag7 alone
    return list(range(1, K+1)), [a]*K
def worker(args):
    ens, p, K, eta, a, S, seed, mmax = args
    rng = np.random.default_rng(seed); M = MN(p); x = np.arange(p)
    modes, amps = modes_amps(ens, K, a)
    C = np.array([np.exp(2j*np.pi*k*x/p) for k in modes])     # (K, p)
    s1 = np.zeros(mmax); s2 = np.zeros(mmax); ms = np.arange(1, mmax+1)
    for _ in range(S):
        th = 2*np.pi*rng.random(len(modes))
        r = np.sqrt(rng.exponential(1.0, len(modes))) if ens == 'flatG' else np.ones(len(modes))
        v = np.real((np.array(amps)*r*np.exp(1j*th)) @ C)
        ev = np.linalg.eigvals(np.exp(1j*eta*v)[:, None]*M)
        tr = np.abs(np.power.outer(ev, ms).sum(axis=0))**2
        s1 += tr; s2 += tr*tr
    return s1, s2
if __name__ == '__main__':
    ens, p, K, eta, a, S, seed, npr = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8])
    mmax = 2*p
    with mpc.Pool(npr) as pool:
        res = pool.map(worker, [(ens, p, K, eta, a, S//npr, seed*1000+k, mmax) for k in range(npr)])
    s1 = sum(r[0] for r in res); s2 = sum(r[1] for r in res); n = (S//npr)*npr
    mean = s1/n; se = np.sqrt((s2/n - mean**2)/n)
    os.makedirs('../logs/mc', exist_ok=True)
    tag = f'{ens}_p{p}_K{K}_eta{eta}_a{a}_S{n}_seed{seed}'
    np.save(f'../logs/mc/{tag}.npy', np.vstack([mean, se]))
    with open(f'../logs/mc/{tag}.txt', 'w') as f:
        f.write(f'# {tag}\n')
        for m in range(1, mmax+1): f.write(f'{m} {mean[m-1]:.6f} {se[m-1]:.6f}\n')
    print('done', tag)
