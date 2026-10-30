"""Fixed-eta law over nu (average over N only): moments of Z_m(nu) over units nu mod g' for fixed eta.
Gaussian (circular complex normal) predictions: M4=E|Z|^4/(E|Z|^2)^2=2, M6=6, |E Z^2|/E|Z|^2=0, |Z|^2/E|Z|^2 ~ Exp(1).
Also F/B_m and the KS distance of |Z|^2/F to Exp(1)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from p2lib import *
import sys
B={3:4.795918,4:5.083333,5:9.399762,6:11.118367,7:13.795609,8:15.298683,9:17.941811}
etas=[float(x) for x in sys.argv[2].split(',')]
for m in [int(x) for x in sys.argv[1].split(',')]:
    O=Orbits(m); u=O.units()
    for eta in etas:
        Z=O.Z_all(eta)[u]; A=np.abs(Z)**2; F=A.mean()
        M4=np.mean(A**2)/F**2; M6=np.mean(A**3)/F**3; rel=abs(np.mean(Z**2))/F
        x=np.sort(A/F); ecdf=np.arange(1,len(x)+1)/len(x); ks=np.max(np.abs(ecdf-(1-np.exp(-x))))
        print(f'm={m} #nu={len(u)} eta={eta:g} F/B={F/B[m]:.3f} M4={M4:.3f} M6={M6:.3f} |E Z^2|/E|Z|^2={rel:.3f} KS(|Z|^2/F vs Exp1)={ks:.3f} (1.36/sqrt(n)={1.36/np.sqrt(len(u)):.3f})',flush=True)
