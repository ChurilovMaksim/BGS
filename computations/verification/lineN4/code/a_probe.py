"""N4 (A) [N]: probe derivative norms for the 8V certificate (float), to design the [CA] cell scheme."""
import sys, numpy as np, json
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
K0,r,K,N0=4,1.2,55,60
R=np.load('/workspace/bgs-lineN/N3/logs/g_R_V_final.npy'); S=np.linalg.inv(R)
w0=wk1(2.0,0); C={}
for n in range(-N0,N0+1):
    V,E=ops(lambda m,n=n: 1.0 if m==n else 0.0, N0,K0,r,r,K,beta=0.0)
    if np.abs(V).max()==0: continue
    C[n]=R@(w0(n)*V)@S
ns=np.array(sorted(C)); Cst=np.stack([C[n] for n in ns])
nrm2={int(n):float(np.linalg.norm(C[n],2)) for n in ns}; nrmF={int(n):float(np.linalg.norm(C[n],'fro')) for n in ns}
print('Lip2',2*np.pi*sum(abs(n)*nrm2[n] for n in nrm2),'LipF',2*np.pi*sum(abs(n)*nrmF[n] for n in nrmF))
print('L2_2',sum((2*np.pi*n)**2*nrm2[n] for n in nrm2))
print('tail norms', {n:nrm2[n] for n in nrm2 if abs(n)>=14})
out=[]
for tau in np.linspace(0,1,41)[:-1]:
    ph=np.exp(2j*np.pi*ns*tau); Y=np.tensordot(ph,Cst,axes=1); Yp=np.tensordot(2j*np.pi*ns*ph,Cst,axes=1)
    out.append((tau,np.linalg.norm(Y,2),np.linalg.norm(Yp,2),np.linalg.norm(Yp,'fro')))
for o in out: print(['%.4f'%x for x in o])
