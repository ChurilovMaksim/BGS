"""Check Prop. R: |k_nu(xi)|^2 in {0, |V[4]|/D} with support independent of nu, for ALL units nu mod g' (m<=7)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import dlib, numpy as np, math
for m in range(1,8):
    O=dlib.Orbits(m); u=O.units(); rad=math.gcd(4,O.d1)*math.gcd(4,O.d2)
    v0=None; worst=0; lev=set()
    for nu in u:
        k=np.fft.fft2(dlib.e(-nu*O.cls/O.gp))/O.D; a=np.abs(k)**2
        lev|=set(np.round(a.ravel()*O.D,8)); 
        if v0 is None: v0=a
        worst=max(worst,np.abs(a-v0).max())
    print(f'm={m} D={O.D} (d1,d2)=({O.d1},{O.d2}) |V[4]|={rad} levels of D|k|^2={sorted(lev)} #units={len(u)} max_nu|dk^2|={worst:.1e}',flush=True)
