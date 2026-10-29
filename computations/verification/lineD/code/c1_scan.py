"""1/p coefficient c_1(s) of Theorem D2 in the fixed-mode limit, by Monte Carlo over theta (Gaussian and uniform-phase
ensembles), flat modes 1..K, a=1.  Also Psi from the same samples (checked against the exact pair sum)."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, numpy as np
from psi import *
m = int(sys.argv[1]); out = []
g, res = residues(m); r, s = res[1]
st = Setup(m, s)
for ens in ('G', 'J0'):
    for K in map(int, sys.argv[2].split(',')):
        for eta in map(float, sys.argv[3].split(',')):
            ps, pse, c1, c1se = psi_c1_mc(st, list(range(1, K+1)), [1.0]*K, eta, int(sys.argv[4]), 7, ens=ens)
            ex = psi_exact(st, list(range(1, K+1)), [1.0]*K, eta, ens=ens)
            line = f"m={m} s={s} {ens:2s} K={K} eta={eta:5.1f}: Psi_MC={ps:.4f}+-{pse:.4f} (exact {ex:.4f})  c1={c1:+10.3f} +- {c1se:.3f}"
            print(line, flush=True); out.append(line)
open(f'../logs/c1_scan_m{m}.log', 'w').write('\n'.join(out)+'\n')
