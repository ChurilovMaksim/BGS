if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np
from numpy.polynomial.laguerre import laggauss
from d4_d6 import *
from psi_check import psi_nsum
from d1_check import Aform
m = 3; dat, W, B = setup(m); D = dat['D']; Nt = 40; NA = Aform(dat, Nt)
u, wu = laggauss(80)
def psiG(t, eta, a=1.0):
    return sum(wi*psi_nsum(dat, t, eta*a*np.sqrt(ui), Nt, NA) for ui, wi in zip(u, wu) if eta*a*np.sqrt(ui) < 25)
for eta in (0.5, 1.0, 2.0):
    for s in units_lifts(dat)[:3]:
        ph, Ws = supp_data(dat, s, W, B)
        t = s/D; h = 1e-5
        num = (psiG(t+h, eta) - psiG(t-h, eta))/(2*h)/D
        orb = psi(ph, Ws, D, [1], [1.0], eta, 'G'); ns = psiG(t, eta)
        tot, diag, bmax = c1_gauss(dat, ph, Ws, [1], [1.0], eta, split=True)
        print(f"eta={eta} s={s}: Psi_G orbit {orb:.10f} nsum {ns:.10f} | c1 closed-form {tot:.6f} vs numeric d/dt {num:.6f} | Gamma-diag part {diag:.1e}", flush=True)
