"""Exact integer checks of branch/winding quotient and cat action pairing."""
from itertools import product
from collections import Counter
import json
import numpy as np
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
from sympy.polys.domains import ZZ
S=s.Matrix([[3,4],[2,3]])
def need(v,msg):
 if not v:raise RuntimeError(msg)
def run():
 rows=[]
 for m in range(1,5):
  B=6*s.eye(m)
  for j in range(m):B[j,(j+1)%m]-=1;B[j,(j-1)%m]-=1
  D=int(B.det());adj=np.array(B.adjugate().tolist(),dtype=np.int64);H=hermite_normal_form(B)
  nu=np.array(list(product(*[range(int(H[j,j])) for j in range(m)])),dtype=np.int64)
  L=np.array((S**m-s.eye(2)).tolist(),dtype=np.int64)
  counts=Counter(); qtable={};total=0
  for rt in product(range(4),repeat=m):
   r=np.array(rt,dtype=np.int64);t=r-3*np.roll(r,1);v=t+4*nu;xnum=v@adj
   pnum4=xnum[:,1%m]+int(r[0])*D-3*xnum[:,0]
   need(np.all(pnum4%4==0),('p denominator',m,rt))
   xy=np.stack((xnum[:,0]%D,(pnum4//4)%D),axis=1)
   nnum=xy@L.T;need(np.all(nnum%D==0),('fixed point',m,rt));n=nnum//D
   qnum=(xy[:,0]*n[:,1]-xy[:,1]*n[:,0]-D*n[:,0]*n[:,1])%(2*D)
   rawnum=(np.sum(xnum*v,axis=1)-3*D*np.sum(r*r))%(8*D)
   need(np.all((rawnum-4*qnum)%(8*D)==0),('action quotient',m,rt))
   for pt,q in zip(xy,qnum):
    key=tuple(map(int,pt));counts[key]+=1
    if key in qtable:need(qtable[key]==int(q),('q consistency',m))
    qtable[key]=int(q)
   total+=len(nu)
  need(len(counts)==D and set(counts.values())=={4**m},('free quotient count',m))
  pts=np.array(sorted(counts),dtype=np.int64);n=(pts@L.T)//D
  lookup={tuple(p):i for i,p in enumerate(pts)};q=np.array([qtable[tuple(p)] for p in pts],dtype=np.int64)
  # Check perfect polarization and exact arbitrary-amplitude paired phase equality.
  tested=0;kernel_b=0
  for j,d in enumerate(pts):
   idx=np.array([lookup[tuple(p)] for p in (pts+d)%D],dtype=np.int64)
   bnum=(pts[:,0]*n[j,1]-pts[:,1]*n[j,0])%D
   need(np.all((q[idx]-q-q[j]-2*bnum)%(2*D)==0),('polarization',m,j))
   if np.all(bnum==0):kernel_b+=1
   tested+=D
  need(kernel_b==1,('nondegenerate character pairing',m))
  calibrations=[]
  for N in [3,5,7,9]:
   ker=np.all((N*pts)%D==0,axis=1);nk=int(ker.sum())
   need(np.all((N*q[ker])%(2*D)==0),('odd torsion refinement',m,N))
   # Exact coefficient histograms of |Gauss sum|².
   hist=np.zeros(2*D,dtype=np.int64)
   for qq in q:hist+=np.bincount((N*(qq-q))%(2*D),minlength=2*D)
   hist[0]-=D*nk
   xx=s.Symbol('x');poly=s.Poly.from_dict({(i,):int(c) for i,c in enumerate(hist) if c},xx,domain=s.QQ)
   phi=s.Poly(s.cyclotomic_poly(2*D,xx),xx,domain=s.QQ)
   need(poly.rem(phi).is_zero,('exact Gauss norm',m,N))
   calibrations.append({'N':N,'kernel_size':nk})
  rows.append({'m':m,'D':D,'listed_classes':total,'physical_classes':len(counts),'copies_per_class':4**m,'polarization_pairs':tested,'smith_B':[abs(int(v)) for v in smith_normal_form(B,domain=ZZ).diagonal() if abs(int(v))>1],'smith_Sm_I':[abs(int(v)) for v in smith_normal_form(s.Matrix(L),domain=ZZ).diagonal() if abs(int(v))>1],'Gauss_calibrations':calibrations})
 return {'arithmetic':'exact integer histograms and rational cyclotomic remainder; no floating point','rows':rows,'boundary':'Checks coordinate/phase algebra only; no fixed-tau CUE comparison.'}
def main():
    print(json.dumps(run(),indent=2))

if __name__=='__main__':
    main()
