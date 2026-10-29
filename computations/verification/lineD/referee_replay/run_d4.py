if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, sys
from d4_d6 import *
for m in (3, 4, 5):
    dat, W, B = setup(m); D = dat['D']
    ss = units_lifts(dat)
    print(f"== m={m}: {len(ss)} residues mod g'={dat['gp']}", flush=True)
    for Ks in ([1], [1, 2], list(range(1, m+1))):
        lims = []; vals = {}
        for s in ss:
            ph, Ws = supp_data(dat, s, W, B)
            lims.append(psi_inf(ph, Ws, D, Ks))
            for eta in (2, 8, 32, 128):
                vals.setdefault(eta, []).append(psi(ph, Ws, D, Ks, [1.0]*len(Ks), eta, 'G'))
        print(f"  K={Ks}: Psi_inf over residues: min {min(lims):.6f} max {max(lims):.6f}", flush=True)
        for eta in vals: print(f"     G eta={eta}: Psi range [{min(vals[eta]):.4f}, {max(vals[eta]):.4f}]", flush=True)
