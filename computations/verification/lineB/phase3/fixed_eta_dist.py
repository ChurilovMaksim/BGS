"""Fixed-eta distribution of Z_m(nu) over nu from norm-class sums: |Z(nu)|^2 = |sum_r A_r e(u r/h)|^2 / h^2, u = unit mod h
(u = c*nu^{-1}; as nu runs over units mod g'=2h, u runs uniformly over units mod h).  Moments M4, M6, |E Z^2|/E|Z|^2, KS vs Exp(1)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fast_classes import *
ms=[int(x) for x in sys.argv[1].split(',')]; etas=[float(x) for x in sys.argv[2].split(',')]
for m in ms:
    h,A,P=class_sums(m,etas); u=np.array([v for v in range(1,h) if math.gcd(v,h)==1])
    for i,eta in enumerate(etas):
        Z=np.fft.ifft(A[i])*h/h   # sum_r A_r e(+u r/h)/h
        Z=Z[u]; I=np.abs(Z)**2; F=I.mean()
        x=np.sort(I/F); ks=np.max(np.abs(np.arange(1,len(x)+1)/len(x)-(1-np.exp(-x))))
        print(f'm={m} h={h} #u={len(u)} eta={eta:g} F/2m={F/(2*m):.4f} M4={np.mean(I**2)/F**2:.3f} M6={np.mean(I**3)/F**3:.3f} |EZ^2|/F={abs(np.mean(Z**2))/F:.3f} KS={ks:.4f} (5% crit {1.36/np.sqrt(len(u)):.4f})',flush=True)
