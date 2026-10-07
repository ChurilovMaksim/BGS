#!/usr/bin/env python3
"""Independent finite-dimensional floating controls, not an asymptotic proof."""
import itertools, json
from pathlib import Path
import numpy as np
rng=np.random.default_rng(742198)
checks=0; worst=0.0

def check(ok,label):
 global checks
 if not ok: raise AssertionError(label)
 checks+=1

def close(a,b,label,tol=2e-9):
 global worst
 err=float(np.max(np.abs(a-b))); worst=max(worst,err)
 check(err<tol,label)

def adj(U): return np.kron(U.conj(),U)
for N in range(2,6):
 X=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N))
 U=np.linalg.qr(X)[0]
 slices=[np.array([[U[x,y] if (x-y)%N==c else 0 for y in range(N)] for x in range(N)]) for c in range(N)]
 C=np.column_stack([A.conj().T.reshape(-1,order='F') for A in slices])
 C0=max(np.vdot(A,A).real for A in slices)
 T=adj(U); R=np.kron(U.T,np.eye(N))
 D=sum(adj(A) for A in slices)
 Dtw=np.zeros_like(D)
 Vs=[]
 for b in range(N):
  Z=np.diag(np.exp(2j*np.pi*b*np.arange(N)/N)); V=Z@U@Z.conj().T
  Vs.append(V); Dtw+=adj(V)/N
 close(D,Dtw,'slice/twirl equality')
 for n in range(7):
  B=np.linalg.qr(rng.normal(size=(N,N))+1j*rng.normal(size=(N,N)))[0]
  v=(B@np.linalg.matrix_power(U,n)).reshape(-1,order='F')
  f=sum(abs(np.trace(np.linalg.matrix_power(U,n)@A@B))**2 for A in slices)
  close(f,np.linalg.norm(C.conj().T@v)**2,'right-frame arbitrary B identity')
  Bn=np.linalg.matrix_power(U.conj().T,n+1)
  close(sum(abs(np.trace(np.linalg.matrix_power(U,n)@A@Bn))**2 for A in slices),sum(np.vdot(A,A).real**2 for A in slices),'changing B counterexample')
 for wordlen in range(1,6):
  for word in itertools.product((0,1),repeat=wordlen):
   P=np.eye(N*N,dtype=complex)
   for digit in word: P=P@(D if digit else T)
   check(np.trace(P).real>=-2e-9 and abs(np.trace(P).imag)<2e-9,'full CP-word positivity')
 for z in (0.,.2,.5,.99,1.):
  d=1-z; Tz=z*T+d*D
  F=np.array([np.trace(np.linalg.matrix_power(Tz,m))-z**m*abs(np.trace(np.linalg.matrix_power(U,m)))**2 for m in range(1,10)]).real
  check(np.min(F)>-2e-9,'complete positivity')
  for m in range(1,10):
   rhs=d*sum(z**n*np.trace(np.linalg.matrix_power(T,n)@D@np.linalg.matrix_power(Tz,m-1-n)) for n in range(m))
   close(F[m-1],rhs,'first-pinch identity')
  for L in range(1,6):
   eps=max([0.]+[np.linalg.norm(C.conj().T@np.linalg.matrix_power(R,r)@C,2) for r in range(1,L)])
   delta=min(C0,C0/L+(1-1/L)*eps); rem=(C0-delta)*(L-1)
   S=np.column_stack([np.linalg.matrix_power(R.conj().T,j)@C for j in range(L)])
   check(np.linalg.norm(S,2)**2/L <=delta+2e-9,'block Gram estimate')
   for A in range(1,10):
    for M in range(A,10):
     lhs=sum(F[A-1:M])/N**2
     rhs=delta/N*sum(1-z**m for m in range(A,M+1))+rem/N*d*(M-A+1+sum(z**r for r in range(1,A)))
     check(lhs <= rhs+2e-9,'finite undamped band estimate')
     if z>0:
      lhs=sum(z**(-m)*F[m-1] for m in range(A,M+1))/N**2
      rhs=delta/N*sum(z**(-m)-1 for m in range(A,M+1))+rem/N*(z**(-M)-1)
      check(lhs<=rhs+2e-8*max(1.,abs(rhs)),'finite deconvolved band estimate')
report={'seed':742198,'dimensions':[2,3,4,5],'z':[0,.2,.5,.99,1],'max_m':9,'max_word_length':5,'max_L':5,'checks_passed':checks,'largest_equalities_absolute_residual':worst,'nonclaims':['No actual U_N computation','No asymptotic frame proof','Floating controls only; universal assertions established by audit proof']}
Path(__file__).with_name('independent_bounded_controls_result.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
