#!/usr/bin/env python3
"""Finite regression for exact history normalization and reconnection tensors.

Checks only finite-dimensional identities. It does not prove semiclassical
partner-orbit localization or BGS.
"""
from __future__ import annotations
import itertools, json
import numpy as np

rng=np.random.default_rng(20260921)

def haar(n):
    z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    q,r=np.linalg.qr(z); d=np.diag(r)
    return q*(d/np.abs(d)).conj()

def projective_history_error(D,M):
    V=haar(D)
    Pis=[]
    for a in range(D):
        P=np.zeros((D,D),complex); P[a,a]=1; Pis.append(P)
    total=0.0
    for hist in itertools.product(range(D), repeat=M+1):
        H=Pis[hist[0]]
        for j in range(1,M+1): H=Pis[hist[j]]@V@H
        total+=np.linalg.norm(H,'fro')**2
    return abs(total-D)

def smooth_history_errors(D,M,J=3):
    V=haar(D)
    raw=rng.uniform(.2,1.0,size=(J,D))
    raw/=np.sqrt((raw**2).sum(axis=0,keepdims=True))
    Ms=[np.diag(raw[j]) for j in range(J)]
    completeness=np.linalg.norm(sum(M.conj().T@M for M in Ms)-np.eye(D))
    total=0.0
    for hist in itertools.product(range(J),repeat=M+1):
        H=Ms[hist[0]]
        for j in range(1,M+1): H=Ms[hist[j]]@V@H
        total+=np.linalg.norm(H,'fro')**2
    return completeness,abs(total-D)

def cycles_cinv_pi(L,pi):
    f=[(pi[i]-1)%L for i in range(L)]
    seen=set(); cyc=0
    for i in range(L):
        if i in seen: continue
        cyc+=1; j=i
        while j not in seen:
            seen.add(j); j=f[j]
    return cyc

def recon_tensor(V,pi,r,powers=None):
    N=V.shape[0]; L=len(pi); P=np.abs(V)**2
    if powers is None: powers=[np.linalg.matrix_power(P,rr) for rr in r]
    c=[(i+1)%L for i in range(L)]
    z=0j
    for aa in itertools.product(range(N),repeat=L):
      for bb in itertools.product(range(N),repeat=L):
        term=1+0j
        for i in range(L):
          term*=powers[i][bb[i],aa[i]]*V[aa[c[i]],bb[i]]*np.conj(V[aa[pi[i]],bb[i]])
        z+=term
    return z

def reconnection_checks():
    rows=[]
    for N in (3,4):
      V=haar(N)
      for L in (2,3):
        perms=list(itertools.permutations(range(L)))[:4]
        for pi in perms:
          r=[i+1 for i in range(L)]
          _=recon_tensor(V,pi,r)
          J=np.ones((N,N))/N
          z0=recon_tensor(V,pi,r,powers=[J]*L)
          cyc=cycles_cinv_pi(L,pi); target=N**(cyc-L)
          err=abs(z0-target); assert err<3e-12
          rows.append({'N':N,'L':L,'pi':pi,'cycles':cyc,'flat_error':err})
    return rows

def main():
    hist=[]
    for D in (2,3,4):
      for M in (1,2,3):
        if D**(M+1)<=5000:
          e=projective_history_error(D,M); assert e<3e-12
          hist.append({'kind':'projective','D':D,'M':M,'error':e})
    for D in (2,3,4):
      for M in (1,2,3):
        ce,e=smooth_history_errors(D,M); assert ce<3e-12 and e<6e-12
        hist.append({'kind':'smooth','D':D,'M':M,'completeness_error':ce,'error':e})
    rec=reconnection_checks()
    print(json.dumps({'status':'PASS','scope':'Exact finite-dimensional history/reconnection identities only; no semiclassical partner localization or BGS.',
      'history_fixtures':len(hist),'max_history_error':max(x['error'] for x in hist),
      'reconnection_flat_fixtures':len(rec),'max_flat_error':max(x['flat_error'] for x in rec)},indent=2))
if __name__=='__main__':main()
