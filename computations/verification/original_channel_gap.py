#!/usr/bin/env python3
"""Finite diagnostics, never an asymptotic proof. Python float64 trig checks.
Base BGS fa007c498fe116a814a90aa3215cfd65b1f2a154, D6 versus derived D8.
All odd N=3..65 for spectral multiset comparison; N below for full k count.
Exact rational arithmetic checks the counting combinatorics separately.
"""
import json, math, platform, time
from fractions import Fraction
import numpy as np
start=time.time()
Ns=list(range(3,66,2))+[97,129,193,257]
thresholds=[1e-4,1e-3,1e-2,.1,1.0]
worst_ratio=0.; worst_case=None; max_error=0.; cases=0; nonempty=0
for N in Ns:
 a=np.arange(N); j=np.arange(N); h=(N+1)//2
 # reduce phase to residues BEFORE evaluating trig
 s=np.sin(2*np.pi*((h*a)%N)/N)
 for k in range(-(N//2),N//2+1):
  z=s[(k-a)%N]
  raw=2*N*N*((s[:,None]+z[:,None])**2*np.cos(np.pi*j/N)[None,:]**2+(s[:,None]-z[:,None])**2*np.sin(np.pi*j/N)[None,:]**2)
  axis_kernel=np.zeros((N,N),bool)
  if k==0: axis_kernel[0,:]=True; axis_kernel[:,0]=True
  if N<=65:
   grid=np.arange(-N//2+1,N//2+1,dtype=float) if k%2==0 else np.arange(-N/2,N/2)
   assert len(grid)==N
   v=np.sin(np.pi*grid/N)**2; w=np.cos(np.pi*grid/N)**2; th=np.pi*k/(2*N)
   gauged=8*N*N*(np.cos(th)**2*v[:,None]*v[None,:]+np.sin(th)**2*w[:,None]*w[None,:])
   err=float(np.max(np.abs(np.sort(raw.ravel())-np.sort(gauged.ravel()))))/(1+8*N*N)
   max_error=max(max_error,err); assert err<2e-13,(N,k,err)
  for lam in thresholds:
   rank=int(np.count_nonzero((raw<=lam)&~axis_kernel))
   bound=4*N*math.sqrt(lam)*(1+math.log(N))
   ratio=rank/bound
   if ratio>worst_ratio: worst_ratio=ratio; worst_case=[N,k,lam,rank,bound]
   assert rank<=bound+1e-12,(N,k,lam,rank,bound)
   cases+=1; nonempty+=rank>0
# exact combinatorial bounds: grids doubled to integers, R rational
exact_cases=0
for N in range(3,66,2):
 for parity in [0,1]:
  grid=list(range(-(N-1),N,2)) if parity==0 else list(range(-N,N,2))
  for R in [Fraction(1,16),Fraction(1,4),Fraction(1),Fraction(N,8),Fraction(N),Fraction(N*N,4)]:
   for yy in grid:
    if yy==0:continue
    t=2*R/abs(yy)
    count=sum(zz!=0 and Fraction(abs(zz),2)<=t for zz in grid)
    assert count<=4*t
    exact_cases+=1
 for D in [Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1),Fraction(N,8),Fraction(N,2)]:
  count=sum(Fraction(N-abs(yy),2)<=D for yy in range(-(N-1),N,2))
  assert count<=4*D
  exact_cases+=1
out={'base':'fa007c498fe116a814a90aa3215cfd65b1f2a154','arithmetic':'float64 trig spectral/count diagnostics; Fraction exact combinatorics','N':Ns,'thresholds':thresholds,'count_cases':cases,'nonempty_count_cases':nonempty,'worst_count_ratio':worst_ratio,'worst_count_case':worst_case,'max_scaled_spectral_multiset_error':max_error,'exact_combinatorial_cases':exact_cases,'python':platform.python_version(),'numpy':np.__version__,'elapsed_seconds':time.time()-start,'non_claim':'Finite diagnostics do not establish the asymptotic theorem or deterministic BGS.'}
print(json.dumps(out,indent=2))
