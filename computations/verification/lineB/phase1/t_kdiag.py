if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import dlib, numpy as np, math
for m in range(1,8):
    O=dlib.Orbits(m); u=O.units()
    vals=[]
    for nu in u[:6]:
        E=dlib.e(-nu*O.cls/O.gp); k=np.fft.fft2(E)/O.D; vals.append(np.abs(k)**2)
    v0=vals[0]; same=max(np.abs(v-v0).max() for v in vals)
    supp=v0>1e-12; levels=np.unique(np.round(v0[supp]*O.D,6))
    print(m,O.D,(O.d1,O.d2),'g\'=',O.gp,'max|dK| over nu',f'{same:.1e}','support',supp.sum(),'levels D|k|^2',levels[:6])
