"""W_m(eta) = F_m(eta) - B_sym_m (xi-picture off-diagonal), fixed eta, nu-average over units mod g'. Scan eta, m."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase2'))
from p2lib import *
import time
ms=[int(x) for x in sys.argv[1].split(',')]
etas=[0.1,0.25,0.5,1,2,3,5,7,10,15,25,50,100,200,400]
for m in ms:
    t0=time.time(); O,supp=support_data(m); u=O.units()
    # B_sym from orbits: sum |o|^2/D_eff ; orbits = S-classes under Gamma: use exact cluster via theta-sequence canonical form is costly; use B_sym from REPORT (phase2 deficit) instead
    Deff=supp.sum()
    print(f'm={m} D={O.D} g\'={O.gp} #units={len(u)} D_eff={Deff}',flush=True)
    for eta in etas:
        Z=O.Z_all(eta)[u]; F=np.mean(np.abs(Z)**2)
        print(f'  eta={eta:7g} F={F:9.4f} F/2m={F/(2*m):.4f}',flush=True)
    print(f'  time {time.time()-t0:.1f}s',flush=True)
