import numpy as np
import json
rng=np.random.default_rng(8102026)
errors=[]
cube_errors=[]
delay_errors=[]
for n in [2,3,5,9]:
 for trial in range(8):
  z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
  S,R=np.linalg.qr(z); S=S@np.diag(np.diag(R)/abs(np.diag(R)))
  z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); T=np.eye(n)+z.conj().T@z/n
  Q=S@T@S.conj().T
  a=S[0,0]; b=S[0,1:]; c=S[1:,0]; d=1-abs(a)**2
  theta=2*np.pi*np.arange(4096)/4096; w=np.exp(1j*theta); q=w/(1-a*w)
  H=T[1:,1:]; h=T[1:,0]; t=T[0,0].real;s=Q[0,0].real
  tp=H[None,:,:]+q[:,None,None]*np.outer(h,b)+q.conj()[:,None,None]*np.outer(b.conj(),h.conj())+t*abs(q[:,None,None])**2*np.outer(b.conj(),b)
  exact=(np.trace(T@T)+2*t*s/d).real
  avg=np.einsum('aij,aji->a',tp,tp).real.mean()
  errors.append(abs(avg-exact)/max(1,abs(exact)))
  gamma=(S@T)[0,0]
  exact3=(np.trace(T@T@T)+3/d*(t*(Q@Q)[0,0]+s*(T@T)[0,0])+6*t*s*np.real(a.conjugate()*gamma)/d**2).real
  avg3=np.einsum('aij,ajk,aki->a',tp,tp,tp).real.mean()
  cube_errors.append(abs(avg3-exact3)/max(1,abs(exact3)))
  w0=w[371];q0=q[371];K=np.vstack((q0*b,np.eye(n-1)))
  sp=S[1:,1:]+np.outer(c,b)*q0
  J=np.vstack((q0.conjugate()*c.conjugate(),np.eye(n-1)))
  delay_errors.append(float(np.linalg.norm(sp@(K.conj().T@T@K)@sp.conj().T-J.conj().T@Q@J)))
  vals,V=np.linalg.eigh(T)
  def curve(th):
   Ft=S@(V@np.diag(np.exp(1j*th*vals))@V.conj().T)
   return Ft[1:,1:]+np.outer(Ft[1:,0],Ft[0,1:])*w0/(1-w0*Ft[0,0])
  eps=1e-6; deriv=(curve(eps)-curve(-eps))/(2*eps)
  delay_errors.append(float(np.linalg.norm(-1j*sp.conj().T@deriv-K.conj().T@T@K)))
print(json.dumps({'cases':len(errors),'phase_grid':4096,'max_relative_second':max(errors),'max_relative_third':max(cube_errors),'max_output_or_derivative_error':max(delay_errors)},indent=2))
# Probe the strong arbitrary-source covariance claim with independent random contractions.
checks=[]
for n in [2,3,4]:
 for trial in range(6):
  z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); U,_=np.linalg.qr(z)
  z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); V,_=np.linalg.qr(z)
  singular=np.linspace(.1,.9,n) if trial<3 else np.repeat(.9,n)
  F=U@np.diag(singular)@V.conj().T
  H=np.eye(n)-F.conj().T@F;ev,E=np.linalg.eigh(H); hs=E@np.diag(np.sqrt(ev))@E.conj().T
  count=24**n
  grid=np.indices((24,)*n).reshape(n,-1).T
  D=np.exp(2j*np.pi*grid/24)
  mat=np.eye(n)[None,:,:]-D[:,:,None]*F[None,:,:]
  K=np.linalg.solve(mat,np.eye(n)[None,:,:]*D[:,:,None])
  L=np.einsum('ij,ajk->aik',hs,K).reshape(count,n*n)
  cov=L.T@L.conj()/count
  checks.append((n,trial,float(np.linalg.eigvalsh(cov)[-1])))
print(json.dumps({'covariance_probes':checks},indent=2))
