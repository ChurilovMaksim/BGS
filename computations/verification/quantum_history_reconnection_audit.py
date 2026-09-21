#!/usr/bin/env python3
"""Finite regression for exact history normalization and reconnection tensors."""
from __future__ import annotations
import itertools, json
import numpy as np
rng=np.random.default_rng(20260921)
def haar(n):
    z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    q,r=np.linalg.qr(z);d=np.diag(r)
    return q*(d/np.abs(d)).conj()
def projective_history_error(D,M):
    V=haar(D);Ps=[]
    for a in range(D):
        P=np.zeros((D,D),complex);P[a,a]=1;Ps.append(P)
    total=0.0
    for h in itertools.product(range(D),repeat=M+1):
        H=Ps[h[0]]
        for j in range(1,M+1):H=Ps[h[j]]@V@H
        total+=np.linalg.norm(H,'fro')**2
    return abs(total-D)
def smooth_history_errors(D,M,J=3):
    V=haar(D);raw=rng.uniform(.2,1.0,size=(J,D));raw/=np.sqrt((raw**2).sum(axis=0,keepdims=True))
    Ms=[np.diag(raw[j]) for j in range(J)]
    ce=np.linalg.norm(sum(M.conj().T@M for M in Ms)-np.eye(D));total=0.0
    for h in itertools.product(range(J),repeat=M+1):
        H=Ms[h[0]]
        for j in range(1,M+1):H=Ms[h[j]]@V@H
        total+=np.linalg.norm(H,'fro')**2
    return ce,abs(total-D)
def cycles(L,pi):
    f=[(pi[i]-1)%L for i in range(L)];seen=set();c=0
    for i in range(L):
        if i in seen:continue
        c+=1;j=i
        while j not in seen:seen.add(j);j=f[j]
    return c
def tensor(V,pi,r,powers=None):
    N=len(V);L=len(pi);P=np.abs(V)**2
    if powers is None:powers=[np.linalg.matrix_power(P,x) for x in r]
    cyc=[(i+1)%L for i in range(L)];z=0j
    for aa in itertools.product(range(N),repeat=L):
      for bb in itertools.product(range(N),repeat=L):
        t=1+0j
        for i in range(L):t*=powers[i][bb[i],aa[i]]*V[aa[cyc[i]],bb[i]]*np.conj(V[aa[pi[i]],bb[i]])
        z+=t
    return z
def main():
    hs=[]
    for D in (2,3,4):
      for M in (1,2,3):
        if D**(M+1)<=5000:
          e=projective_history_error(D,M);assert e<3e-12;hs.append(e)
    for D in (2,3,4):
      for M in (1,2,3):
        ce,e=smooth_history_errors(D,M);assert ce<3e-12 and e<6e-12;hs.append(e)
    fs=[]
    for N in (3,4):
      V=haar(N)
      for L in (2,3):
        for pi in list(itertools.permutations(range(L)))[:4]:
          J=np.ones((N,N))/N;z=tensor(V,pi,[i+1 for i in range(L)],powers=[J]*L)
          target=N**(cycles(L,pi)-L);e=abs(z-target);assert e<3e-12;fs.append(e)
    print(json.dumps({"status":"PASS","scope":"Exact finite history/reconnection identities only; no partner-tube localization or BGS.","history_fixtures":len(hs),"max_history_error":max(hs),"flat_reconnection_fixtures":len(fs),"max_flat_error":max(fs)},indent=2))
if __name__=="__main__":main()
