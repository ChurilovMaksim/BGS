"""N13 (A) [N]: second-moment (HS^2-type) rate for i.i.d. uniform twists: K(Y) = E_d[X(d) Y X(d)^*] = sum_n |w_4(n)|^2 M_n Y M_n^* / |s|^2
(cross terms n != n' vanish under uniform d).  rho(K) = growth rate of E||prod X(d_t) Phi||^2 and of E|psi prod X Phi|^2.
Also the cut-off version K_b: d uniform on [-1/2,1/2] minus the slow box |d|<theta (excursion steps), computed by quadrature."""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
A0,s,Phi,psi=A.spectral(); W2=np.abs(A.COEF0)**2/abs(s)**2
def K(Y): return sum(w*(M@Y@M.conj().T) for w,M in zip(W2,A.MS))
Y=np.outer(Phi,Phi.conj()); rates=[]
for it in range(40):
    Y2=K(Y); r=np.trace(Y2).real/np.trace(Y).real; Y=Y2/np.trace(Y2).real; rates.append(r)
    print(it,r,flush=True)
# second moment of the scalar psi prod X Phi along the iteration
out=dict(rho_K=rates[-1],rates=rates,lam_m_half=float((3+2*2**0.5)**-0.5),lam_inv=float(1/(3+2*2**0.5)))
json.dump(out,open('/workspace/bgs-lineN/N13/logs/g_K.json','w'),indent=1); print(out['rho_K'])
