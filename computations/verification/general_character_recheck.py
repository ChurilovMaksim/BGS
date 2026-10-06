#!/usr/bin/env python3
"""Independent exact signed-trace arithmetic and finite character controls."""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse,hashlib,json,math
from pathlib import Path
import numpy as np

def mul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2))for i in range(2))
def power(a,k):
 b=((1,0),(0,1))
 for _ in range(k):b=mul(b,a)
 return b

def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def modulus(t,k):
 a=abs(t);s=1 if t>0 else -1;u=[0,1]
 for _ in range((k-1)//2):u.append(a*u[-1]-u[-2])
 return u[-1]+s*u[-2]
def spectral(t,k):
 s=1 if t>0 else -1
 if (abs(t)-2*s)%k==0:
  raise ValueError('Excluded ramified prime period: A-I is not a unit')
 n=modulus(t,k);x=np.arange(n,dtype=np.int64)
 phase=((t*x[:,None]**2-2*x[:,None]*x[None,:])*pow(2,-1,n))%n
 u=np.exp(2j*np.pi*phase/n)/np.sqrt(n);r=np.eye(n)[(-x)%n]
 scalar=np.trace(r@u);u/=scalar/abs(scalar)
 assert np.max(abs(u@u.conj().T-np.eye(n)))<1e-11
 assert np.max(abs(np.linalg.matrix_power(u,k)-np.eye(n)))<3e-10
 c=1 if n%k==1 else -1
 basis=[]
 if c==-1:
  v=np.zeros(n);v[0]=1;basis.append(v)
 for j in range(1,(n+1)//2):
  v=np.zeros(n);v[j]=1/math.sqrt(2);v[n-j]=-c/math.sqrt(2);basis.append(v)
 q=np.stack(basis,axis=1);v=q.T@u@q;ev=np.linalg.eigvals(v)
 labels=np.rint(k*np.angle(ev)/(2*np.pi)).astype(int)%k
 counts=np.bincount(labels,minlength=k)
 assert all(counts==(n-c)//(2*k))
 err=max(abs(np.trace(np.linalg.matrix_power(u,j))-c)for j in range(1,k))
 assert err<2e-10
 return {'trace':t,'K':k,'N':n,'uniform_parity':'odd'if c==1 else'even','dimension':q.shape[1],'root_counts':counts.tolist(),'maximum_full_trace_error':float(err)}

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args();rows=[]
 for t in list(range(-16,-2))+list(range(3,17)):
  a=abs(t);s=1 if t>0 else -1;A=((t,-1),(1,0))
  for k in (5,7,11,13,17,19):
   if (a-2*s)%k==0:continue
   n=modulus(t,k);m=(k-1)//2;lhs=power(A,k);am=power(A,m);aminus=((t-1,-1),(1,-1));rhs=mul(am,aminus)
   assert n%2==1 and math.gcd(n,a-2*s)==1
   assert all(lhs[i][j]-(i==j)==s**m*n*rhs[i][j]for i in range(2)for j in range(2))
   c=pow(a-2*s,(k-1)//2,k);c=1 if c==1 else -1
   assert n%k==c%k and (n-c)%(2*k)==0
   for j in range(1,k):
    b=power(A,j);b=((b[0][0]-1,b[0][1]),(b[1][0],b[1][1]-1));assert math.gcd(det(b),n)==1
   rows.append({'trace':t,'K':k,'N':str(n),'parity_sign':c,'multiplicity':str((n-c)//(2*k))})
 spectra=[spectral(t,k) for t,k in ((3,5),(3,7),(4,5),(4,7),(5,5),(6,5),(-3,7),(-4,5),(-6,7))]
 bad_n=modulus(-3,5)
 assert math.gcd(bad_n,5)==5
 try:spectral(-3,5)
 except ValueError:pass
 else:raise AssertionError('ramified negative control was accepted')
 result={'excluded_prime_negative_control':{'trace':-3,'K':5,'N':bad_n,'gcd':5},'status':'PASS','scope':'Exact recurrence/unit conditions plus independent small dense Weyl-character spectra. No asymptotic BGS assertion.','producer':'computations/verification/general_character_recheck.py','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'exact_cases':rows,'spectral_cases':spectra}
 text=json.dumps(result,indent=2)+'\n'
 if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(text)
 else:print(text)
if __name__=='__main__':main()
