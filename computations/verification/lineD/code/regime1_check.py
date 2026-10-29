"""Check of Theorem D2 (fixed modes, p -> infinity): exact theta-average (trapezoid rule in theta, K=1, uniform phase)
of |Tr U^m|^2 at prime p, versus  Psi_m(s/D) + c_1(s)/p  with s = -p^{-1} mod D_m.
Usage: regime1_check.py k a eta Q p1 p2 ...   (single mode k, amplitude a)"""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import os, sys
os.environ['OMP_NUM_THREADS'] = '1'; os.environ['OPENBLAS_NUM_THREADS'] = '1'
import numpy as np, math, multiprocessing as mpc
from dlib import MN, Dm
from psi import Setup, psi_c1_quad
k, a, eta, Q = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
primes = list(map(int, sys.argv[5:])); MS = (3, 4, 5, 6)
def tr_node(args):
    p, th = args; M = MN(p); x = np.arange(p)
    ev = np.linalg.eigvals(np.exp(1j*eta*a*np.cos(2*np.pi*k*x/p + th))[:, None]*M)
    return np.array([abs(np.sum(ev**m))**2 for m in MS])
out = []
with mpc.Pool(8) as pool:
    for p in primes:
        vals = np.mean(pool.map(tr_node, [(p, 2*np.pi*q/Q) for q in range(Q)]), axis=0)
        for i, m in enumerate(MS):
            D = Dm(m)
            if D % p == 0: continue
            s = (-pow(p, -1, D)) % D
            st = Setup(m, s); ps, c1 = psi_c1_quad(st, [k], [a], eta)
            line = f"k={k} a={a} eta={eta} m={m} p={p} s={s}: exact E={vals[i]:.10f}  Psi={ps:.10f}  Psi+c1/p={ps+c1/p:.10f}  c1={c1:.4f}  p*(E-Psi)={p*(vals[i]-ps):.4f}  p^2*(E-Psi-c1/p)={p*p*(vals[i]-ps-c1/p):.3f}"
            print(line, flush=True); out.append(line)
open(f'../logs/regime1_k{k}_a{a}_eta{eta}.log', 'a').write('\n'.join(out)+'\n')
