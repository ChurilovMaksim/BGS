"""N14 (A) core-rate certificate, v2 [CA-fp].  N_n := c_n M_n / s (balanced letters; ||N_3|| = 2.43, ||N_0|| = 0.40).
K(Y) = sum_n N_n Y N_n^* = E_{d uniform} X(d) Y X(d)^*  (CP).  rho(K) = 0.27255 (power) but its Perron matrix Y* is SINGULAR,
so Y* + eps I only certifies 0.62 (b_cp.py).  Here: Neumann certificate  Y_c = sum_{k=0}^{m} rb^{-k} K^k(Y0), Y0 = Y* + eps||Y*|| I:
  K(Y_c) - rb Y_c = rb^{-m} K^{m+1}(Y0) - rb Y0  <= 0  iff  lambda_max(Y0^{-1/2} K^{m+1}(Y0) Y0^{-1/2}) <= rb^{m+1}.
Verified directly: W = rb Y_c - fl(K(Y_c)) >= 0 with rounding/input error bounds (Weyl).  usage: b_cp2.py rb eps m"""
import sys, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); import fastops as F
A=F.A; D=F.D; K=F.K; NS=list(A.NS); s=F.s; c=A.COEF0
rb=float(sys.argv[1]); epsr=float(sys.argv[2]); m=int(sys.argv[3])
blocks={}
for k,ib,jb,B in zip(F.BK,F.BI,F.BJ,F.BB): blocks.setdefault(int(k),[]).append((int(ib),int(jb),c[k]/s*B))   # N_n blocks
def NYN(k,Y,absv=False):
    T=np.zeros((D,D),float if absv else complex)
    for ib,jb,B in blocks[k]:
        Bb=np.abs(B) if absv else B; T[ib*K:(ib+1)*K,:]+=Bb@Y[jb*K:(jb+1)*K,:]
    Z=np.zeros((D,D),float if absv else complex)
    for ib,jb,B in blocks[k]:
        Bb=np.abs(B) if absv else B; Z[:,ib*K:(ib+1)*K]+=T[:,jb*K:(jb+1)*K]@(Bb.conj().T)
    return Z
def Kw(w,Y): Z=sum(w[k]*NYN(k,Y) for k in range(len(NS)) if w[k]!=0); return (Z+Z.conj().T)/2
one=np.ones(len(NS))
Y=np.eye(D,dtype=complex)/D
for it in range(60):
    Y2=Kw(one,Y); r=np.trace(Y2).real/np.trace(Y).real; Y=Y2/np.trace(Y2).real
rho=r; print('rho power',rho,flush=True)
Y0=Y+epsr*np.linalg.eigvalsh(Y).max()*np.eye(D)
Yc=np.zeros((D,D),complex); Kk=Y0.copy(); t0=time.time()
for k in range(m+1):
    Yc+=Kk*rb**(-k); Kk=Kw(one,Kk)
L0=np.linalg.cholesky(Y0); L0i=np.linalg.inv(L0); T=L0i@Kk@L0i.conj().T
g=np.linalg.eigvalsh((T+T.conj().T)/2).max(); print('Neumann test g_m',g,'rb^(m+1)',rb**(m+1),time.time()-t0,flush=True)
Yc=(Yc+Yc.conj().T)/2
Z=Kw(one,Yc)
Wm=rb*Yc-Z; Wm=(Wm+Wm.conj().T)/2; lmin=np.linalg.eigvalsh(Wm).min()
P=sum(NYN(k,np.abs(Yc),True) for k in range(len(NS)))
E_round=2.5e-13*np.linalg.norm(P)+1e-16*rb*np.linalg.norm(Yc)
# input errors: |Delta M_n| <= RAD entrywise -> ||Delta N_n||_F <= |c_n|/|s| RAD D ; coefficient/s relative error <= 1e-15
NnF=[np.sqrt(sum(np.linalg.norm(B)**2 for _,_,B in blocks[k])) for k in range(len(NS))]
dN=[abs(c[k]/s)*A.RAD*D for k in range(len(NS))]
E_input=sum(2*dN[k]*NnF[k]+dN[k]**2 for k in range(len(NS)))*np.linalg.norm(Yc,2)+3e-15*np.linalg.norm(P)
eig_err=1e-13*np.linalg.norm(Wm,2)
margin=lmin-E_round-E_input-eig_err
ev=np.linalg.eigvalsh(Yc); condY=ev.max()/ev.min(); pt=A.PERT/abs(s); tt=1e-3
rho_true=(1+tt)*rb+(1+1/tt)*pt**2*condY*1.0   # core->true:  ||Delta X||_2 <= Pert/|s|
out=dict(rho_power=rho,rb=rb,eps=epsr,m=m,g_m=float(g),lmin_W=float(lmin),E_round=float(E_round),E_input=float(E_input),eig_err=float(eig_err),
         margin=float(margin),certified=bool(margin>0),cond_Yc=float(condY),rho_true_bar=float(rho_true),
         Phi_c=float(np.real(F.Phi.conj()@np.linalg.solve(Yc,F.Phi))),psi_Yc=float(np.real(F.psi.conj()@Yc@F.psi)))
print(json.dumps(out),flush=True)
np.savez(f'/workspace/bgs-lineN/N14/logs/b_cp2_Yc_{rb}.npz',Yc=Yc)
# balanced off-diagonal letter weights:  K_v^(1)(Y)=sum_n (|N_{n-v}|/|N_n|) N_n Y N_n^*, K_v^(2)(Y)=sum_n (|N_n|/|N_{n-v}|) N_{n-v} Y N_{n-v}^*
nrm=[np.linalg.norm(np.block([[np.zeros((0,0))]]) ) for _ in NS]
nrm=[max(np.linalg.norm(B,2) for _,_,B in blocks[k]) for k in range(len(NS))]
Li=np.linalg.inv(np.linalg.cholesky(Yc)); kap={}
for v in range(1,25):
    w1=np.zeros(len(NS)); w2=np.zeros(len(NS))
    for k,n in enumerate(NS):
        if (n-v) in NS:
            j=NS.index(n-v); w1[k]+=nrm[j]/nrm[k]; w2[j]+=nrm[k]/nrm[j]
    mx=0
    for w in (w1,w2):
        Zv=Kw(w,Yc); T=Li@Zv@Li.conj().T; mx=max(mx,float(np.linalg.eigvalsh((T+T.conj().T)/2).max()))
    kap[v]=mx; print('kappa',v,mx,flush=True)
out['kappa']=kap
json.dump(out,open(f'/workspace/bgs-lineN/N14/logs/b_cp2_{rb}.json','w'),indent=1)
