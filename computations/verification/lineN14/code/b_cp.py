"""N14 (A) core-rate certificate [CA-fp] + collision letter weights [N].
K_w(Y) = sum_n w_n M_n Y M_n^*  (completely positive).  i.i.d.-uniform second moment: w_n = |c_n|^2/|s|^2 (=K).
(1) Perron matrix Y* of K by power iteration; Y_c = Y* + eps*||Y*|| I (PD).
(2) Certificate:  K(Y_c) <= rho_bar Y_c  (Loewner)  => K^m(Y) <= rho_bar^m (sup_Y/Y_c) Y_c  for all m, all Y>=0.
    rigorous float: W = rho_bar Y_c - fl(K(Y_c)); lambda_min(W) - ||E_round||_F - ||E_input||_F - eig_err > 0,
    E_round <= gamma * sum_n w_n |M_n||Y_c||M_n|^T (gamma = 2.5e-13 >= gamma_{1100} with margin), E_input from RAD, |s| enclosure.
(3) Off-diagonal (carry) letters: K_v(Y) = sum_n |c_n c_{n-v}| M_n Y M_n^*/|s|^2 and the shifted variant (M_{n-v}); kappa_v = max of
    lambda_max(Y_c^{-1/2} K_v(Y_c) Y_c^{-1/2}) over both variants  [N float; feeds the carry automaton e_carry.py]."""
import sys, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); import fastops as F
A=F.A; D=F.D; K=F.K; NS=list(A.NS); MS=A.MS
s=F.s; c=A.COEF0
blocks={}   # n-index -> list of (ib,jb,B)
for k,ib,jb,B in zip(F.BK,F.BI,F.BJ,F.BB): blocks.setdefault(int(k),[]).append((int(ib),int(jb),B))
def MYMs(k,Y):   # M_k Y M_k^*  block-sparse
    T=np.zeros((D,D),complex)
    for ib,jb,B in blocks[k]: T[ib*K:(ib+1)*K,:]+=B@Y[jb*K:(jb+1)*K,:]
    Z=np.zeros((D,D),complex)
    for ib,jb,B in blocks[k]: Z[:,ib*K:(ib+1)*K]+=T[:,jb*K:(jb+1)*K]@B.conj().T
    return Z
def MYMs2(k1,k2,Y):  # M_k1 Y M_k2^*
    T=np.zeros((D,D),complex)
    for ib,jb,B in blocks[k1]: T[ib*K:(ib+1)*K,:]+=B@Y[jb*K:(jb+1)*K,:]
    Z=np.zeros((D,D),complex)
    for ib,jb,B in blocks[k2]: Z[:,ib*K:(ib+1)*K]+=T[:,jb*K:(jb+1)*K]@B.conj().T
    return Z
def Kw(w,Y): return sum(w[k]*MYMs(k,Y) for k in range(len(NS)) if w[k]!=0)
W2=np.abs(c)**2/abs(s)**2
t0=time.time()
Y=np.eye(D,dtype=complex)/D; rates=[]
for it in range(60):
    Y2=Kw(W2,Y); Y2=(Y2+Y2.conj().T)/2; r=np.trace(Y2).real/np.trace(Y).real; Y=Y2/np.trace(Y2).real; rates.append(r)
    if it%10==9: print('it',it,r,time.time()-t0,flush=True)
ev=np.linalg.eigvalsh(Y); print('Y* eig range',ev.min(),ev.max())
out=dict(rho_power=rates[-1],rates=rates[-10:])
best=None
for epsr in [1e-3,1e-4,1e-5,1e-6]:
    Yc=Y+epsr*ev.max()*np.eye(D); Z=Kw(W2,Yc); Z=(Z+Z.conj().T)/2
    L=np.linalg.cholesky(Yc); Li=np.linalg.inv(L); T=Li@Z@Li.conj().T; mu=np.linalg.eigvalsh((T+T.conj().T)/2).max()
    print('eps',epsr,'gen-eig max',mu,'cond(Yc)',np.linalg.cond(Yc),flush=True)
    if best is None or mu<best[1]: best=(epsr,mu,Yc,Z)
epsr,mu,Yc,Z=best
rho_bar=float(mu)*(1+1e-6)+1e-9
# rigorous float check
absP=sum(W2[k]*MYMs(k,np.abs(Yc)).__abs__() for k in range(len(NS)))   # crude: |M||Y||M|^T approximated via |.| of product? use exact abs-matmul below
def absK(Yabs):
    S=np.zeros((D,D))
    for k in range(len(NS)):
        T=np.zeros((D,D))
        for ib,jb,B in blocks[k]: T[ib*K:(ib+1)*K,:]+=np.abs(B)@Yabs[jb*K:(jb+1)*K,:]
        Zk=np.zeros((D,D))
        for ib,jb,B in blocks[k]: Zk[:,ib*K:(ib+1)*K]+=T[:,jb*K:(jb+1)*K]@np.abs(B).T
        S+=W2[k]*Zk
    return S
P=absK(np.abs(Yc))
E_round=2.5e-13*np.linalg.norm(P)            # Frobenius bound on |fl(K(Yc)) - K(Yc)|  (gamma_1100 ~ 1.2e-13, x2 margin)
# input: entry radius RAD on M_n (=> |Delta M| <= RAD entrywise, D x D), coefficient rel err 1e-15, |s| rel err 1e-15
nMF=max(np.linalg.norm(MS[k]) for k in range(len(NS))); YF=np.linalg.norm(Yc)
E_input=sum(W2)*(2*A.RAD*D*YF*nMF+(A.RAD*D)**2*YF) + 6e-15*np.linalg.norm(Z)
Wm=rho_bar*Yc-Z; Wm=(Wm+Wm.conj().T)/2
lmin=np.linalg.eigvalsh(Wm).min(); eig_err=1e-13*np.linalg.norm(Wm,2)
margin=lmin-E_round-E_input-eig_err
# perturbation core->true operator: ||Delta X|| <= Pert/|s| (Euclid op); (1+t)K + (1+1/t)(Pert/|s|)^2 ||Yc|| I  <= rho_true Yc
condY=np.linalg.cond(Yc); pt=A.PERT/abs(s); tt=1e-4
rho_true=(1+tt)*rho_bar+(1+1/tt)*pt**2*condY
out.update(eps_reg=epsr,gen_eig_max=float(mu),rho_bar=rho_bar,lmin_W=float(lmin),E_round=float(E_round),E_input=float(E_input),
           eig_err=float(eig_err),margin=float(margin),certified=bool(margin>0),cond_Yc=float(condY),rho_true_bar=float(rho_true))
print(json.dumps(out),flush=True)
np.savez('/workspace/bgs-lineN/N14/logs/b_cp_Yc.npz',Yc=Yc)
# (3) letter weights kappa_v
Li=np.linalg.inv(np.linalg.cholesky(Yc)); kap={}
for v in range(1,31):
    w1=np.zeros(len(NS)); w2=np.zeros(len(NS))
    for k,n in enumerate(NS):
        if (n-v) in NS: w1[k]=abs(c[k]*c[NS.index(n-v)])/abs(s)**2
        if (n+v) in NS: w2[k]=abs(c[k]*c[NS.index(n+v)])/abs(s)**2   # M_{n} with partner n+v  (second variant after reindexing)
    m=0
    for w in (w1,w2):
        if w.max()==0: continue
        Zv=Kw(w,Yc); T=Li@Zv@Li.conj().T; m=max(m,float(np.linalg.eigvalsh((T+T.conj().T)/2).max()))
    kap[v]=m; print('kappa',v,m,flush=True)
out['kappa']=kap; out['kappa0']=rho_bar
json.dump(out,open('/workspace/bgs-lineN/N14/logs/b_cp.json','w'),indent=1)
