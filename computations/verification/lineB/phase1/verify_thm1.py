"""Verify Theorem 1: Tr U_N^m/Tr M_N^m = Z_m(N^{-1} mod g'_m) + O(1/N), |Tr M_N^m|=1 for gcd(N,D_m)=1. Diagonal kick, fixed phases."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import dlib, numpy as np, math, sys, time
etas=[0.5,1.0,2.0,4.0]; ms=list(range(1,8))
Os={m:dlib.Orbits(m) for m in ms}
Ns=[101,151,201,203,205,251,301,401,501,601,801,1001,1201,1601]
print('# N m eta |TrM^m|  Z_quantum  Z_limit  |diff|  N*|diff|  bound')
for eta in etas:
    n,gh=dlib.ghat(eta); a=np.abs(gh); s0=a.sum(); s2=(a*n.astype(float)**2).sum()
    Zl={m:Os[m].Z_all(eta) for m in ms}
    for N in Ns:
        res=dlib.trace_ratio_quantum(N,ms,eta)
        for m in ms:
            D=dlib.Dm(m)
            if math.gcd(N,D)!=1: continue
            gp,yp=dlib.gprime(m); nu=pow(N,-1,gp)
            tU,tM=res[m]; zq=tU/tM; zl=Zl[m][nu]; d=abs(zq-zl)
            bound=math.pi*m*s2*s0**(m-1)/N
            print(f'{N} {m} {eta} {abs(tM):.12f} {zq.real:+.6f}{zq.imag:+.6f}j {zl.real:+.6f}{zl.imag:+.6f}j {d:.3e} {N*d:.3f} {bound:.3e}', flush=True)
