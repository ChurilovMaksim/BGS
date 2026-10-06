#!/usr/bin/env python3
"""Bounded float64 diagnostics for FM-019, not certified spectral bounds."""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse, json, time
from pathlib import Path
import numpy as np
from scipy.linalg import eigvalsh
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

def block(n, ka, kb):
    h=(n+1)//2
    sine=lambda x: np.sin(2*np.pi*((h*x)%n)/n)
    rows=[]; cols=[]; vals=[]
    for a in range(n):
        for b in range(n):
            i=a*n+b
            sa=sine(a); ta=sine(ka-a)
            sb=sine(b); tb=sine(kb-b)
            rows.append(i); cols.append(i)
            vals.append(2*n*n*(sa*sa+ta*ta+sb*sb+tb*tb))
            for aa,bb,val in [(a,(b+1)%n,2*n*n*sa*ta),
                              (a,(b-1)%n,2*n*n*sa*ta),
                              ((a+1)%n,b,2*n*n*sb*tb),
                              ((a-1)%n,b,2*n*n*sb*tb)]:
                rows.append(i); cols.append(aa*n+bb); vals.append(val)
    return coo_matrix((vals,(rows,cols)),shape=(n*n,n*n)).tocsr()

def gap(n,k):
    a=block(n,*k)
    if k==(0,0):
        a=a[1:,1:]
        vals=eigvalsh(a.toarray(),subset_by_index=[0,2]) if n<=21 else eigsh(a,k=3,which='SA',tol=1e-9,maxiter=10000,return_eigenvectors=False,v0=np.sin(np.arange(a.shape[0])+1)+np.cos(np.sqrt(2)*(np.arange(a.shape[0])+1)))
        vals=np.sort(vals)
        assert abs(vals[0])<1e-6, vals
        return float(vals[1])
    vals=eigvalsh(a.toarray(),subset_by_index=[0,0]) if n<=21 else eigsh(a,k=1,which='SA',tol=1e-9,maxiter=10000,return_eigenvectors=False,v0=np.sin(np.arange(a.shape[0])+1)+np.cos(np.sqrt(2)*(np.arange(a.shape[0])+1)))
    return float(vals[0])

def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',required=True); args=p.parse_args()
    result={'arithmetic':'IEEE float64; exploratory eigenvalues, no certified lower bound', 'full':[], 'selected':[]}
    start=time.monotonic()
    for n in [3,5,7,9,11,13]:
        values=[(gap(n,(a,b)),a,b) for a in range(n) for b in range(n)]
        best=min(values)
        row={'N':n,'blocks':n*n,'gap':best[0],'minimizer':list(best[1:]),'zero_block_gap':values[0][0]}
        result['full'].append(row); print(json.dumps(row),flush=True)
    for n in [17,21,33,65]:
        for k in [(0,0),(1,0),(1,1),(2,0),(2,2),(n//2,n//2)]:
            row={'N':n,'k':list(k),'gap':gap(n,k)}
            result['selected'].append(row); print(json.dumps(row),flush=True)
    result['elapsed_seconds']=time.monotonic()-start
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__': main()
