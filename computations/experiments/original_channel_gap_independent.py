
# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import numpy as np,json,math
maxerr=0.; checks=0; maxratio=0.; worst=None
for N in range(3,66,2):
 h=(N+1)//2
 for k in range(-(N-1)//2,(N-1)//2+1):
  a=np.arange(N)[:,None]; j=np.arange(N)[None,:]
  s=lambda x:np.sin(2*np.pi*h*x/N)
  raw=2*N*N*(s(a)**2+s(k-a)**2+2*s(a)*s(k-a)*np.cos(2*np.pi*j/N))
  grid=np.arange(N)-N//2-(.5 if k%2 else 0)
  y=grid[:,None]; eta=grid[None,:]; theta=np.pi*k/(2*N)
  E=8*N*N*(np.cos(theta)**2*np.sin(np.pi*y/N)**2*np.sin(np.pi*eta/N)**2+np.sin(theta)**2*np.cos(np.pi*y/N)**2*np.cos(np.pi*eta/N)**2)
  err=np.max(np.abs(np.sort(E.flat)-np.sort(raw.flat)))/(1+N*N)
  maxerr=max(maxerr,float(err));checks+=1
  kernel=(y==0)|(eta==0) if k==0 else np.zeros_like(E,dtype=bool)
  for lam in np.logspace(-10,5,61):
   r=int(np.count_nonzero((E<=lam)&(~kernel)))
   bound=4*N*np.sqrt(lam)*(1+np.log(N))
   ratio=r/bound
   if ratio>maxratio:maxratio=ratio;worst=[N,k,float(lam),r,float(bound)]
   assert r<=bound+1e-9,(N,k,lam,r,bound)
  assert err<1e-11,(N,k,err)
print(json.dumps({'N':'all odd 3..65','k':'all centered labels','spectral_cases':checks,'count_thresholds':'61 logspace values 1e-10..1e5','maximum_scaled_spectral_error':maxerr,'max_count_ratio':maxratio,'max_count_ratio_case':worst,'arithmetic':'numpy float64, diagnostic only'},indent=2))
