"""Fixed-eta limit F_m(eta) (N-averaged form factor) vs eta, and its Cesaro mean, showing approach to Bohr mean B_m (2m - short-orbit deficit).
Also 4th moment ratio of Z_m(nu) over nu (complex Gaussian -> 2)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import dlib, numpy as np
etas=[0.5,1,2,4,8,16,32,64,128,256,512,1024]
for m in [3,4,5,6,7,8]:
    O=dlib.Orbits(m)
    row=[]
    for eta in etas:
        F,Z=O.F(eta); u=O.units(); z=Z[u]; row.append((eta,F,np.mean(np.abs(z)**4)/F**2))
    # Cesaro means over eta windows [E,2E] (200 pts each)
    ces=[]
    for E in [8,64,512]:
        xs=np.linspace(E,2*E,201); ces.append((E,np.mean([O.F(x)[0] for x in xs])))
    print(f'm={m} 2m={2*m}  ' + '  '.join(f'F({e:g})={F:.2f}[M4={r:.2f}]' for e,F,r in row))
    print(f'      Cesaro means over [E,2E]: ' + '  '.join(f'E={E}: {c:.3f}' for E,c in ces), flush=True)
