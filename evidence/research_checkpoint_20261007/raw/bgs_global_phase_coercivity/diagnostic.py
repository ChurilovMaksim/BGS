import numpy as np
from scipy.optimize import root
rng=np.random.default_rng(1871)

def center(z):
 def fun(a):
  c=a[0]+1j*a[1]
  q=((z-c)/(1-c.conjugate()*z)).sum()
  return [q.real,q.imag]
 r=root(fun,[0.,0.])
 c=r.x[0]+1j*r.x[1]
 if not r.success or abs(c)>=1 or np.linalg.norm(fun(r.x))>1e-7: return None
 return (z-c)/(1-c.conjugate()*z)

def calc(U,z):
 d=1-abs(z)**2; H=-np.log(d).sum()
 A=U@np.diag(z)@U.conj().T
 S=np.linalg.slogdet(np.eye(len(z))-A@np.diag(z.conj()))[1]+H
 g=np.log1p(abs(z[:,None]-z[None,:])**2/(d[:,None]*d[None,:]))
 E=(abs(U)**2*g).sum()/2
 return S,H,E
out=[]
for n in [2,3,4,5,7,8,16,32]:
 F=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n)/np.sqrt(n)
 best=[9,None]; gap=[9,None]
 for k in range(1500):
  z=(1-np.exp(-rng.uniform(.0001,12,n)))*np.exp(2j*np.pi*rng.random(n))
  z=center(z)
  if z is None:continue
  S,H,E=calc(F,z)
  if S/H<best[0]:best=[S/H,z.tolist()]
  if E and S/E<gap[0]:gap=[S/E,z.tolist()]
 out.append({'n':n,'min_S_H':best,'min_S_E':gap})
 print(n,best[0],gap[0],flush=True)
import json
with open('/workspace/shared/bgs_global_phase_coercivity/diagnostic.json','w') as f:json.dump(out,f,indent=2,default=lambda z:[z.real,z.imag])
