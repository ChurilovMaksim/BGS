"""Rigorous-form (float) QUADRATIC single-step bound near a slow twist: N_H(t) <= sigma_max([[sqrt(1+t^2 eps0^2)+..., t c1],[t b1, kap + t b2]]) + t^2 L2/2,
from v = a Phi + q (H-orthogonal), C(t) = M + t E1 + R(t), E1 = 2 pi i sum n w_n M_n / s, ||R(t)||_H <= t^2 L2/2, L2 = (2pi)^2 sum n^2|w_n| ||M_n||_H/|s|.
Requires Re(psi^T E1 Phi) = 0 (|mu(t)| stationary at t=0; checked, printed)."""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
f='/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'; z=np.load(f)
T=z['T']; Ti=np.linalg.inv(T); s=complex(z['s']); Phi=z['Phi']; psi=z['psi']; Qt=z['Qt']; kap=float(z['kap'])
nH=lambda v: np.linalg.norm(T@v); nHs=lambda w: np.linalg.norm(w@Ti); nHM=lambda M: np.linalg.norm(T@M@Ti,2)
E1=2j*np.pi*np.tensordot(A.COEF0*A.NS,A.MS,1)/s
eps0=complex(psi@E1@Phi); b1=nH(Qt@E1@Phi); c1=nHs(psi@E1@Qt); b2=nHM(Qt@E1@Qt)
MnH=np.array([nHM(Mk) for Mk in A.MS]); L2=float((2*np.pi)**2*np.sum(A.NS**2*np.abs(A.COEF0)*MnH)/abs(s))
L3=float((2*np.pi)**3*np.sum(np.abs(A.NS)**3*np.abs(A.COEF0)*MnH)/abs(s))
# with Re eps0 ~ 0: |a(1+t eps0)| <= |a| sqrt((1+t Re eps0)^2 + t^2 Im eps0^2)
def bound(t):
    m=np.array([[np.sqrt((1+t*eps0.real)**2+(t*eps0.imag)**2), t*c1],[t*b1, kap+t*b2]])
    return float(np.linalg.norm(m,2)+t*t*L2/2)
out=dict(eps0=[eps0.real,eps0.imag],b1=b1,c1=c1,b2=b2,L2=L2,L3=L3,kap=kap)
tab=json.load(open(f.replace('.npz','_stepnorm_NG4096.json')))['N_H']
rows=[]
for t in [1/4096,1/2048,1/1024,1/512,1/256,1/128,1/64]:
    j=int(round(t*4096)); B=bound(t); rows.append(dict(t=t,bound=B,coef=(B-1)/t**2,measured=tab[j],meas_coef=(tab[j]-1)/t**2))
    print(rows[-1])
out['rows']=rows; print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
json.dump(out,open('/workspace/bgs-lineN/N12/logs/quad_stepbound.json','w'),indent=1)
