"""N15 REPORT_N14_v2: eigen-solver-free re-verification of the N14 rho_bar=0.28 certificate (b_cp2), [CA-fp: IEEE std model + libm<=1ulp].
Loads the stored Y_c (N14/logs/b_cp2_Yc_0.28.npz, binary64, used as an exact matrix).  Checks
  (a) Y_c > 0:  rig.psd_lower(Y_c) > 0   (residual bound W = V Lam V^* + R, lam_min >= min Lam (1-||V^*V-I||) - ||R||; no eigen-solver accuracy assumed)
  (b) W = 0.28 Y_c - K(Y_c) >= 0: psd_lower(fl W) - E_round - E_input > 0 with
      E_round <= (2 cgam(L) + 16u + gam(61) + 3u) ||P||_F / (1-gam(L+70)),  L = max inner length (<= 55 * max #blocks per (n,row block)), P = sum|N_n||Y_c||N_n|^T
      E_input as in b_cp2 with ||Y_c||_2 <= ||Y_c||_F.
  (c) rho_true <= (1+t) rb + (1+1/t) (Pert/|s|)^2 cond(Y_c), cond(Y_c) <= ||Y_c||_F / psd_lower(Y_c).
Together: K(Y_c) <= rb Y_c with Y_c > 0  =>  rho(K) <= rb (Krein-Rutman / CP Perron-Frobenius)."""
import sys, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); sys.path.insert(0,'/workspace/bgs-lineN/N15/code')
import fastops as F, rig
from rig import u, gam, cgam
A=F.A; D=F.D; K=F.K; NS=list(A.NS); s=F.s; c=A.COEF0; rb=0.28
blocks={}
for k,ib,jb,B in zip(F.BK,F.BI,F.BJ,F.BB): blocks.setdefault(int(k),[]).append((int(ib),int(jb),c[k]/s*B))
Lmax=0
for k,bl in blocks.items():
    cnt={}
    for ib,jb,B in bl: cnt[ib]=cnt.get(ib,0)+1
    Lmax=max(Lmax,K*max(cnt.values()))
def NYN(k,Y,absv=False):
    T=np.zeros((D,D),float if absv else complex)
    for ib,jb,B in blocks[k]:
        Bb=np.abs(B) if absv else B; T[ib*K:(ib+1)*K,:]+=Bb@Y[jb*K:(jb+1)*K,:]
    Z=np.zeros((D,D),float if absv else complex)
    for ib,jb,B in blocks[k]:
        Bb=np.abs(B) if absv else B; Z[:,ib*K:(ib+1)*K]+=T[:,jb*K:(jb+1)*K]@(Bb.conj().T)
    return Z
t0=time.time()
Yc=np.load('/workspace/bgs-lineN/N14/logs/b_cp2_Yc_0.28.npz')['Yc']; Yc=(Yc+Yc.conj().T)/2
ylo,yinfo=rig.psd_lower(Yc); nY=rig.fro(Yc); print('Yc lower',ylo,yinfo,'|Yc|_F',nY,time.time()-t0,flush=True)
Z=sum(NYN(k,Yc) for k in range(len(NS))); Z=(Z+Z.conj().T)/2
W=rb*Yc-Z; W=(W+W.conj().T)/2
P=sum(NYN(k,np.abs(Yc),True) for k in range(len(NS)))
kround=(2*cgam(Lmax)+16*u+gam(61)+3*u)/(1-gam(Lmax+70))
E_round=kround*rig.fro(P)+4*u*rig.fro(np.abs(rb*Yc))+4*u*rig.fro(Z)
NnF=[np.sqrt(sum(np.linalg.norm(B)**2 for _,_,B in blocks[k]))*1.01 for k in range(len(NS))]
dN=[abs(c[k]/s)*A.RAD*D*1.01 for k in range(len(NS))]
E_input=sum(2*dN[k]*NnF[k]+dN[k]**2 for k in range(len(NS)))*nY+3e-15*rig.fro(P)
wlo,winfo=rig.psd_lower(W)
margin=wlo-E_round-E_input
cond=nY/ylo; pt=A.PERT/abs(s); tt=1e-3; rho_true=(1+tt)*rb+(1+1/tt)*pt**2*cond
out=dict(rb=rb,Lmax=Lmax,kround=kround,Yc_lower=ylo,Yc_info=yinfo,W_lower=wlo,W_info=winfo,E_round=E_round,E_input=E_input,margin=margin,
         certified=bool(margin>0 and ylo>0),cond_upper=cond,rho_true_bar=rho_true,secs=time.time()-t0,label='CA-fp (IEEE std model + libm<=1ulp), eigen-solver-free')
print(json.dumps(out)); json.dump(out,open('/workspace/bgs-lineN/N15/logs/b_cp3_0.28.json','w'),indent=1)
