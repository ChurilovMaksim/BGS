import numpy as np, math, scipy.sparse as sp, time
from collections import defaultdict
def coeff():
 r={0:1,7:-.5,-7:-.5}
 def prod(a,b):
  c=defaultdict(complex)
  for j,x in a.items():
   for k,y in b.items(): c[j+k]+=x*y
  return c
 r=prod(r,{0:1,1:.5,-1:.5})
 s=prod(r,{1:-.5j,-1:.5j})
 A=defaultdict(complex,{(0,7):.5,(0,-7):.5,(0,0):-.1})
 for k,v in r.items():
  A[0,k]+=v/10
  A[1,k]+=v*(-3-4j)/1000
  A[-1,k]+=v*(-3+4j)/1000
 for k,v in s.items(): A[0,k]+=v/100
 return {d:v for d,v in A.items() if v}
def kick(xi,L):
 # W=(-1)^ab T: ordinary Fourier convolution for the small-angle frozen twist
 from scipy.signal import convolve2d
 A=np.zeros((3,19),complex)
 for (a,b),v in coeff().items(): A[a+1,b+9]=v*(-1)**(a*b)
 mat=np.ones((1,1),complex)
 out=np.zeros((2*L+1,18*L+1),complex);out[L,9*L]=1
 for i in range(1,L+1):
  mat=convolve2d(mat,A)*(1j*xi/i)
  out[L-i:L+i+1,9*(L-i):9*(L+i)+1]+=mat
 return {(int(a-L),int(b-9*L)):out[a,b]*(1-2*((a-L)*(b-9*L)%2)) for a,b in zip(*np.nonzero(out))}
def pell(k):
 h,v=1,0
 for _ in range(k): h,v=h+2*v,h+v
 return h
def matrix(D,p,sector):
 # Coordinates doubled: X=2a,Y=2b, with residue sector
 # U=a+sqrt(2)b and V=a-sqrt(2)b. use integer exact enlarged domain in production.
 r=math.sqrt(2); lm=3+2*r
 u=max(abs(a+r*b) for a,b in D)/(lm-1);v=max(abs(a-r*b) for a,b in D)/(1-1/lm)
 R=math.ceil(u+v)+1
 states=[(X,Y) for X in range(-R,R+1) for Y in range(-R,R+1) if (X%2,Y%2)==sector and abs(X+r*Y)<=2*u+1e-8 and abs(X-r*Y)<=2*v+1e-8]
 di={x:i for i,x in enumerate(states)};rows=[];cols=[];data=[]
 for t,(X,Y) in enumerate(states):
  A,B=3*X+4*Y,2*X+3*Y
  for (a,b),z in D.items():
   j=di.get((A+2*a,B+2*b))
   if j is not None:
    rows.append(j);cols.append(t);data.append(z*1j**((p*(a*B-b*A))%4))
 return sp.csr_matrix((data,(rows,cols)),shape=(len(states),len(states)))
def power(H,k,cut):
 out=None
 while k:
  if k%2:
   out=H if out is None else out@H
   if out is not H:
    out.data[abs(out.data)<cut]=0;out.eliminate_zeros()
  k//=2
  if k:
   H=H@H
   H.data[abs(H.data)<cut]=0;H.eliminate_zeros()
 return out.diagonal().sum()
if __name__=='__main__':
 import sys
 k=int(sys.argv[1]);cut=float(sys.argv[2]);dc=float(sys.argv[3])
 N=pell(k);D0=kick(N/1e80,18);D={d:z for d,z in D0.items() if abs(z)>dc}
 print('xi',N/1e80,'sum excluded',sum(abs(z) for d,z in D0.items() if d not in D),'D',len(D),flush=True)
 total=0
 for i in range(2):
  for j in range(2):
   H=matrix(D,-N%4,(i,j)); t=time.time(); result=power(H,k,cut); total+=result
   print(H.shape,H.nnz,result,time.time()-t,flush=True)
 print('trace',total,abs(total))
