"""Independent one-step stationary-phase diagnostic at a visible test strength."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import json
import math
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

def compare(n, strength):
    idx=np.arange(n); q=idx/n; nxt=(idx+1)%n
    r=lambda x:(1-np.cos(14*np.pi*x))*(1+np.cos(2*np.pi*x))
    diag=np.cos(14*np.pi*q)-.1+r(q)*(.1+.01*np.sin(2*np.pi*q))
    off=(-3-4j)*r(((idx+pow(2,-1,n))%n)/n)/1000
    A=coo_matrix((np.r_[diag,off,off.conj()],(np.r_[idx,idx,nxt],np.r_[idx,nxt,idx])),shape=(n,n)).tocsr()
    x,y=np.ogrid[:n,:n]
    angle=(-pow(8,-1,n)*(3*x*x-2*x*y+3*y*y))%n
    M=np.exp((2j*math.pi/n)*angle)/math.sqrt(n)
    observed=np.trace(expm_multiply((1j*strength*n)*A,M))/np.trace(M)
    curv=np.array([-19606,-19594,24306,24894])/125
    a=(4-2*math.pi*strength*curv)**(-.5)
    main=1j**(n%4)*(a[0]-a[1])*np.exp(.9j*strength*n)+(a[2]+a[3])*np.exp(-1.1j*strength*n)
    return dict(N=n, auxiliary_strength=strength, absolute_error=abs(observed-main))

rows=[compare(n, .0001) for n in (151,301,601,1101)]
assert all(r['absolute_error']<1.5/r['N'] for r in rows)
print(json.dumps(rows,indent=2))
