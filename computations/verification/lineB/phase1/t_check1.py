if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import dlib, numpy as np, math, itertools, time
eta=1.7
n, gh = dlib.ghat(eta)
sel = np.abs(gh)>1e-17; n=n[sel]; gh=gh[sel]
print('ghat support', n.min(), n.max(), 's0=',np.abs(gh).sum())
# m=2 fourier truncation
def Z2(nu):
    gp,yp = dlib.gprime(2)
    tot=0
    for a,ca in zip(n,gh):
        tot += ca*np.sum(gh*dlib.e(-nu*yp*(a*a+6*a*n+n*n)/gp))
    return tot
O2 = dlib.Orbits(2)
Z = O2.Z_all(eta)
for nu in [1,3,5,7]: print('m=2 nu',nu, Z2(nu), Z[nu])
# m=3 fourier truncated small support check
m=3; O3=dlib.Orbits(3); Z3=O3.Z_all(eta); gp,yp=dlib.gprime(3)
idx = np.abs(gh)>1e-9; nn=n[idx]; gg=gh[idx]; print('trunc support',len(nn))
for nu in [1,3,5]:
    tot=0
    for a,ca in zip(nn,gg):
        for b,cb in zip(nn,gg):
            al = (a,b); # alpha = a + b*lam + c*lam^2 = a + b lam + c(6lam-1) = (a-c) + (b+6c) lam
            A_=a-nn; B_=b+6*nn
            tot += ca*cb*np.sum(gg*dlib.e(-nu*yp*(A_*A_+6*A_*B_+B_*B_)/gp))
    print('m=3 nu',nu,tot,Z3[nu])
