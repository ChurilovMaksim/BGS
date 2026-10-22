import numpy as np,sympy as s,json,time
from pathlib import Path
R=Path('/workspace/shared/bgs_seven_adic_independent_review');S=R/'actual_source';x=s.symbols('q');start=time.time()
def trim(a):
 a=np.array(a,dtype=np.int64)%5
 while len(a)>1 and a[-1]==0:a=a[:-1]
 return a

def rem(a,f):
 a=np.array(a,dtype=np.int64).copy()%5;f=trim(f);iv=pow(int(f[-1]),-1,5)
 for k in range(len(a)-len(f),-1,-1):
  c=int(a[k+len(f)-1])*iv%5
  if c:a[k:k+len(f)]=(a[k:k+len(f)]-c*f)%5
 return trim(a[:max(1,len(f)-1)])
def mul(a,b):return trim(np.convolve(a,b))
def gcd(a,b):
 a=trim(a);b=trim(b)
 while np.any(b):a,b=b,rem(a,b)
 return trim(a*pow(int(a[-1]),-1,5))
def subx(a):
 a=np.pad(a,(0,max(0,2-len(a))));a[1]-=1;return trim(a)
def rabin(f):
 f=trim(f);f=trim(f*pow(int(f[-1]),-1,5));d=len(f)-1
 h=np.array([0,1],dtype=np.int64);cuts={d//p for p in s.factorint(d)}
 for k in range(1,d+1):
  hh=np.zeros(5*(len(h)-1)+1,dtype=np.int64);hh[::5]=h;h=rem(hh,f)
  if k in cuts:assert len(gcd(f,subx(h)))==1,(d,k)
 assert not np.any(rem(subx(h),f)),d
 return {'degree':d,'rabin_cuts':sorted(cuts),'frobenius':True}
res=[]
yd=json.loads((S/'bounded_boundary_polynomials.json').read_text())
for j in range(1,7):
 P=s.Poly(s.sympify(yd['y_numerators'][j]),x,modulus=5);unit,fs=s.factor_list(P)
 prod=np.array([int(unit)],dtype=np.int64);cert=[]
 for f,e in fs:
  a=np.array(list(map(int,f.all_coeffs()))[::-1],dtype=np.int64)%5
  for k in range(e):prod=mul(prod,a)
  c=rabin(a);assert c['degree']%42;c['multiplicity']=e;cert.append(c)
 assert np.array_equal(trim(prod),trim(list(map(int,P.all_coeffs()))[::-1]))
 res.append({'name':'y'+str(j),'degree':P.degree(),'factors':cert});print('y',j,'passed',flush=True)
nd=json.loads((S/'bounded_boundary_norm.json').read_text());prod=np.array([1],dtype=np.int64);cert=[]
for f in nd['factors']:
 a=trim(f['coefficients'][::-1]);c=rabin(a);assert c['degree']%42;c['multiplicity']=f['multiplicity'];cert.append(c)
 for k in range(f['multiplicity']):prod=mul(prod,a)
 print('norm',c['degree'],'passed',flush=True)
pinned=trim(nd['norm_coefficients'][::-1]);assert np.array_equal(trim(prod*pow(int(prod[-1]),-1,5)),trim(pinned*pow(int(pinned[-1]),-1,5)))
res.append({'name':'norm','degree':len(pinned)-1,'factors':cert})
(R/'actual_factor_results.json').write_text(json.dumps({'results':res,'seconds':time.time()-start},indent=2));print('ALL PASSED',time.time()-start,flush=True)
