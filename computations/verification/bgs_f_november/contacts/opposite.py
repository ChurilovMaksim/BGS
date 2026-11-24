"""Independent finite tests for reversed paths, intersections, and complex transfer twists."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from itertools import product
import json
import numpy as np
from pathlib import Path
import sys
# Use common assembly without running its explicit word tests.
from paths import model

def check(n,m):
    U=model(n,.38)
    words=np.array(list(product(range(n),repeat=m)))
    amp=U[np.roll(words,-1,axis=1),words].prod(axis=1)
    threshold=2*m//3+1
    perm=np.array([(-j)%m for j in range(m)])
    reverse=words[:,perm]
    coef=np.zeros(m+1,complex); union=0j; sum_offsets=0j; duplicates=0j
    for x,a in zip(words,amp):
        val=a*amp.conj()
        rev_hits=np.stack([(np.roll(reverse,s,axis=1)==x).sum(axis=1) for s in range(m)])
        fwd_hits=np.stack([(np.roll(words,s,axis=1)==x).sum(axis=1) for s in range(m)])
        np.add.at(coef,rev_hits[0],val)
        count=(rev_hits>=threshold).sum(axis=0)+(fwd_hits>=threshold).sum(axis=0)
        union+=sum(val[count>0]);sum_offsets+=sum(count*val)
        duplicates+=sum(np.maximum(count-1,0)*val)
    V=np.kron(U,U.conj().T)
    ids=np.arange(n)*(n+1); is_diag=np.zeros(n*n,bool);is_diag[ids]=True
    error=abs(union-sum_offsets+duplicates)
    for j in (1,2,3):
        A=np.linalg.matrix_power(U,j)
        block=np.linalg.matrix_power(V,j)[np.ix_(ids,ids)]
        error=max(error,np.max(abs(block-A*A.T.conj())))
    for z in (-.3+.7j,1,1.2-.04j):
        mat=np.where(is_diag,z,1.)[:,None]*V
        error=max(error,abs(np.trace(np.linalg.matrix_power(mat,m))-sum(coef[i]*z**i for i in range(m+1))))
    assert error<2e-10
    return dict(N=n,m=m,max_error=float(error),dihedral_union=float(union.real),
                reversed_full_contact=float(coef[-1].real))
if __name__=='__main__':
    print(json.dumps([check(3,5),check(5,4),check(3,6)],indent=2))
