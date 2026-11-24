"""Direct, independent small-matrix checks; NumPy is needed only for this diagnostic."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from itertools import product
import json
from pathlib import Path
import numpy as np
from coefficients import pell

def test(k):
    N=pell(k); indices=np.arange(N)
    x,y=np.meshgrid(indices,indices,indexing="ij")
    e=lambda t: np.exp(2j*np.pi*(np.asarray(t)%N)/N)
    M=e(-pow(8,-1,N)*(3*x*x-2*x*y+3*y*y))/np.sqrt(N)
    eye=np.eye(N,dtype=complex)
    T=lambda a,b: e(b*(indices+pow(2,-1,N)*a))[:,None]*np.roll(eye,-a,axis=0)
    # Arbitrary nonsymmetric polynomial, supports exact cycle enumeration.
    D={(0,0):0.83+.01j,(0,1):.22-.11j,(1,-1):.12j,(-1,0):-.09j,(0,-1):.11}
    K=sum(z*T(*d) for d,z in D.items())
    Mk=np.linalg.matrix_power(M,k)
    val=np.trace(np.linalg.matrix_power(K@M,k))/np.trace(Mk)
    S=np.array([[3,4],[2,3]],dtype=int)
    entries=list(D.items()); signed=0j; arms=0j; count=0
    Sk=np.linalg.matrix_power(S,k)
    # adjugate of I-S^k recovers the unique real carry exactly.
    G=np.eye(2,dtype=int)-Sk
    det=int(G[0,0]*G[1,1]-G[0,1]*G[1,0])
    adj=np.array([[G[1,1],-G[0,1]],[-G[1,0],G[0,0]]])
    for seq in product(entries,repeat=k):
        A=B=phase=0; z=1
        for (a,b),coef in seq:
            A,B=3*A+4*B,2*A+3*B
            phase+=a*B-b*A
            A+=a;B+=b;z*=coef
        if A%N or B%N:continue
        count+=1
        signed+=z*e(pow(2,-1,N)*phase)
        t=2*adj@np.array([A,B]);assert np.all(t%det==0)
        X,Y=t//det;x0,y0=X,Y
        phase2=0
        for (a,b),coef in seq:
            X,Y=3*X+4*Y,2*X+3*Y
            phase2+=a*Y-b*X
            X+=2*a;Y+=2*b
        assert (X,Y)==(x0,y0) and (phase2-2*phase)%N==0
        arms+=z*e(pow(4,-1,N)*phase2)
    cov=np.max(abs(M@T(1,-1)@M.conj().T-T(-1,-1)))
    error=max(abs(val-arms),abs(val-signed),cov,np.max(abs(Mk-np.trace(Mk)/N*eye)))
    assert error<1e-12
    return dict(k=k,N=N,closed=count,error=float(error),trace=[float(val.real),float(val.imag)])
if __name__=="__main__":
    results=[test(k) for k in (3,5,7)]
    print(json.dumps(results,indent=2))
