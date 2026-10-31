"""N2 (B2) [N] exploration: the carry automaton projects to u = e_j - e_{j-1}/lam, u' = lam*u + v, weight rho(v).
Discretise (M x)(u) = sum_v rho(v) x(lam u + v) on [-U,U] (piecewise-linear interpolation, x=0 outside), get Perron value."""
import numpy as np, math
from scipy.special import jv
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import eigs
LAM=3+2*math.sqrt(2)
AM=60; J=np.abs(jv(np.arange(AM+1),1.8))
def rho(d,tau=0.0):
    s=0.0
    for a in range(-AM,AM+1):
        b=a-d
        if -AM<=b<=AM: s+=J[abs(a)]*J[abs(b)]*math.exp(tau*(abs(a)+abs(b)))
    return s
R={d:rho(d) for d in range(-30,31)}
for U,n in [(2,801),(3,1201),(4,2001),(4,4001)]:
    us=np.linspace(-U,U,n); h=us[1]-us[0]
    M=lil_matrix((n,n))
    for i,u in enumerate(us):
        for v,rv in R.items():
            t=LAM*u+v
            if abs(t)>U: continue
            j=(t+U)/h; j0=int(math.floor(j)); f=j-j0
            if j0>=n-1: j0,f=n-2,1.0
            M[i,j0]+=rv*(1-f); M[i,j0+1]+=rv*f
    val,vec=eigs(M.tocsr(),k=1,which='LM'); x=np.abs(vec[:,0]); x/=x.max()
    print(U,n,'perron',val[0].real, 'x(0)',x[n//2], 'x at u=+-1',x[np.argmin(abs(us-1))],x[np.argmin(abs(us+1))],'x(U-)',x[-5])
    np.save(f'logs/b2_perron_U{U}_n{n}.npy',np.vstack([us,x]))
