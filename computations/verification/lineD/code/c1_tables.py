"""Exact 1/p coefficient c_1(s) (circular-Gaussian ensemble, modes 1..K, a_k=1) for all residues s, by c1_gauss_exact.
E_theta|Tr U^m|^2 = Psi_m(t*) + c_1/p + O(p^-2)   (Cor. D2).  Prints min/max over residues of c_1 and of c_1+2m^2 (COE needs c_1=-2m^2)."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, numpy as np, time
from psi import *
m = int(sys.argv[1]); Ks = list(map(int, sys.argv[2].split(','))); etas = list(map(float, sys.argv[3].split(',')))
g, res = residues(m)
st = Setup(m, res[0][1]); ws = [class_weights(st, s) for r, s in res]
out = [f"# m={m} D={st.D} classes={len(st.w)} residues={len(res)}  COE target c_1=-2m^2={-2*m*m}"]
for K in Ks:
    for eta in etas:
        t0 = time.time()
        c = np.array([c1_gauss_exact(st, list(range(1, K+1)), [1.0]*K, eta, w=w) for w in ws])
        out.append(f"m={m} K={K} G eta={eta:6.2f}: c1 over residues min={c.min():+11.4f} max={c.max():+11.4f} max|c1|={np.abs(c).max():10.4f}   ({time.time()-t0:.1f}s)")
        print(out[-1], flush=True)
open(f'../logs/c1_exact_m{m}.log', 'w').write('\n'.join(out)+'\n')
