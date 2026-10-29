if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, core
from d4_d6 import *
from psi_check import brute
# (a) eta-threshold spot checks (1% of 2m), G ensemble a_k=1
for m, Ks, etas in [(3, [1], [4, 8]), (4, [1, 2], [2, 4]), (5, [1, 2], [8, 16]), (5, [1, 2, 3, 4], [2, 4])]:
    dat, W, B = setup(m); D = dat['D']; sd = [supp_data(dat, s, W, B) for s in units_lifts(dat)]
    Bs = {3: 235/49, 4: 61/12, 5: 15801/1681}[m]
    for eta in etas:
        dev = max(abs(psi(ph, Ws, D, Ks, [1.0]*len(Ks), eta, 'G') - Bs) for ph, Ws in sd)
        print(f"m={m} K={Ks} G eta={eta}: max_s|Psi-B_sym|={dev:.4f}  (<= 0.02m*... threshold {0.01*2*m:.2f}: {dev <= 0.01*2*m})", flush=True)
# (b) non-commuting limits: fixed p=101, m=3, single mode J0, eta -> large
m = 3; dat, W, B = setup(m); D = dat['D']; p = 101
s = (-pow(p, -1, D)) % D; ph, Ws = supp_data(dat, s, W, B)
for eta in (1, 4, 16, 64):
    Q = int(max(128, 16*eta*m))
    e = brute(m, p, float(eta), Q=Q); ps = psi(ph, Ws, D, [1], [1.0], eta, 'J0')
    print(f"p={p} m=3 K=1 J0 eta={eta}: exact E={e:.4f}  Psi(t*)={ps:.4f}  p*(E-Psi*)={p*(e-ps):.2f}   B_3^sym={235/49:.4f}  E_LineC={6-9/p+4/p**2:.4f}", flush=True)
