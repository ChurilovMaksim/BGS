if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np
from d4_d6 import *
cases = [(3, [1], [1, 2, 4, 8, 16]), (3, [1, 2], [1, 2]), (4, [1], [1, 16, 32, 64]), (4, [1, 2], [2, 4]), (5, [1, 2], [2]), (5, [1, 2, 3, 4], [4])]
cache = {}
for m, Ks, etas in cases:
    if m not in cache:
        dat, W, B = setup(m); cache[m] = (dat, [supp_data(dat, s, W, B) for s in units_lifts(dat)])
    dat, sd = cache[m]
    for eta in etas:
        vals = []; bm = 0; dg = 0
        for ph, Ws in sd:
            tot, diag, bmax = c1_gauss(dat, ph, Ws, Ks, [1.0]*len(Ks), eta, split=True)
            vals.append(tot); bm = max(bm, bmax); dg = max(dg, abs(diag))
        vals = np.array(vals)
        print(f"m={m} K={Ks} eta={eta}: max|c1|={np.abs(vals).max():.4g}  sum over residues={vals.sum():.1e}  max|Gamma-diag part|={dg:.1e}  max|b| off-Gamma={bm:.4g}  max|b|/eta^4={bm/eta**4:.4g}", flush=True)
