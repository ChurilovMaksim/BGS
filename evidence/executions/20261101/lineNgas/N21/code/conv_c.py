"""N21 (A): Lemma C (two-sided vector-form core->true conversion), REPORT_N21 sec. 2.  Self-contained (no c2_mid import).
For one window (twists d_1..d_n = digits.core(zeta,18), tails from N15 conv.tails):
  core chain   r^ = fl(psi.v^_n)/fl(psi.Phi), rounding radius rad  (N15 c3_mid recursion, pure rounding, [CA-fp])
  forward      F_k >= ||A_{<=k} Phi||_2   (k=0..n),  backward  B_k >= ||psi A_{>k}||_2  (k=0..n)   (c3 / N16 dual recursions, NO pert term)
  GA = (c_hi/c_lo) prod max(1,N_H(d_k))  >= every contiguous core sub-product 2-norm   (c_hi/c_lo = 21.103 [CA]; NOT sqrt -- N21 finding F21-1)
  Lemma C:  |r_true - r^| <= rad + err_proj + err_pert + err_dPi + |Tr(Pi P)| scale + (1+scale) err_tail
  with every term as in REPORT_N21 sec. 2 (eqs. C1-C6).  Label: numbers [CA-fp: IEEE std model + libm <= 1 ulp]; lemma [P].
usage: conv_c.py replay part nparts | ext Glo Ghi part nparts | test"""
import os
os.environ.setdefault('OMP_NUM_THREADS','1'); os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import sys, json, math, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); sys.path.insert(0,'/workspace/bgs-lineN/N15/code')
import a_ops as A, digits as Dg, rig
from rig import u, gam, cgam
import mpmath as mp
# N21 finding F21-2: digits.py runs at mp.dps=34, which corrupts the twists for G >= 22 (|e| ~ lambda^G); raise precision
mp.mp.dps=160; Dg.S2=mp.sqrt(2); Dg.LAM=3+2*Dg.S2
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz')
T=z['T']; s=complex(z['s']); Phi=z['Phi'].astype(complex); psi=z['psi'].astype(complex); Ti=np.linalg.inv(T)
D=A.D; K=55; NB=D//K; NS=A.NS.astype(float); C=A.COEF0/s
# ---- c3_mid constants (verbatim formulas, N15 c3_mid.py)
P_,eP=rig.matmul_err(T,Ti); etaT=rig.fro(P_-np.eye(D))+eP; nT=rig.fro(T); nTi=rig.fro(Ti)/(1-etaT)
pTi=psi@Ti; npsi=(rig.fro(pTi)+cgam(D)*rig.fro(np.abs(psi)@np.abs(Ti)))/(1-etaT)*(1+1e-15)
psiPhi=psi@Phi; eps_p=cgam(D)*float(np.abs(psi)@np.abs(Phi))*1.01
bl=[]
for k in range(len(A.NS)):
    for ib in range(NB):
        for jb in range(NB):
            Bk=A.MS[k][ib*K:(ib+1)*K, jb*K:(jb+1)*K]
            if np.abs(Bk).max()>0: bl.append((k,ib,jb,Bk))
BK=np.array([b[0] for b in bl]); BI=np.array([b[1] for b in bl]); BJ=np.array([b[2] for b in bl]); BB=np.array([b[3] for b in bl]); BA=np.abs(BB)
CA=np.abs(C)*(1+8*u)
M_=int(max(np.bincount(BI).max(),np.bincount(BJ).max()))
eps_c=4*u*2*math.pi*30*0.5+16*u
kap_der=(1+eps_c)*(1+cgam(K))*(1+math.sqrt(2)*gam(2))*(1+gam(M_))-1
KAP=max(1e-13,1.25*kap_der)+2*u
ABSDIV=1/(1-gam(K+M_+6))
RADT=A.RAD*D*float(np.abs(C).sum())*1.01
Lip2=2*math.pi*sum(abs(n)*CA[k]*rig.fro(A.MS[k]) for k,n in enumerate(NS))*1.01
def stp(v,d):
    c=C*np.exp(2j*np.pi*NS*d); vb=v.reshape(NB,K)
    y=np.einsum('bij,bj->bi',BB,vb[BJ])*c[BK][:,None]; out=np.zeros((NB,K),complex); np.add.at(out,BI,y); return out.reshape(D)
def absstp(va):
    vb=va.reshape(NB,K); y=np.einsum('bij,bj->bi',BA,vb[BJ])*CA[BK][:,None]; out=np.zeros((NB,K)); np.add.at(out,BI,y); return out.reshape(D)
def stpT(w,d):
    c=C*np.exp(2j*np.pi*NS*d); ub=w.reshape(NB,K)
    y=np.einsum('bij,bi->bj',BB,ub[BI])*c[BK][:,None]; out=np.zeros((NB,K),complex); np.add.at(out,BJ,y); return out.reshape(D)
def absstpT(wa):
    ub=wa.reshape(NB,K); y=np.einsum('bij,bi->bj',BA,ub[BI])*CA[BK][:,None]; out=np.zeros((NB,K)); np.add.at(out,BJ,y); return out.reshape(D)
TAB=json.load(open('/workspace/bgs-lineN/N15/logs/nh_table_rig_2048.json')); TB=TAB['bound']; TH=TAB['h']
def NH(d):
    if abs(d)<=1/256: return 1+1.01e-12+4260*d*d
    x=(d+0.5)/TH; k=int(math.floor(x)); k=min(max(k,0),len(TB)-1); b=TB[k]
    if x-k<1e-9 and k>0: b=max(b,TB[k-1])
    if k+1-x<1e-9 and k+1<len(TB): b=max(b,TB[k+1])
    return b
def loc(xa_norm,xn,d,nPre): return nPre*(KAP*xa_norm*ABSDIV+RADT*xn+Lip2*abs(d)*2.3e-16*xn)*(1+1e-14)
# ---- certified constants: N8 (Line F / N6), N13 adapted norm
N8=json.load(open('/workspace/bgs-lineN/N8/logs/n8_cert_fam.json'))
RA=N8['RA_Gamma']; dPi=N8['dPi']; Pert=N8['Pert']; Xn=N8['Xn']; N1=N8['N1']; Cpow=N8['Cpow']; mus=N8['mu_minus_s']
B13=json.load(open('/workspace/bgs-lineN/N13/logs/b_arb.json')); CONDH=B13['V1']['c_hi']/B13['V1']['c_lo']*(1+1e-12)
Fs=Pert/abs(s)*(1+1e-12); xs=Xn/abs(s)*(1+1e-12); g=1+xs
# er, el: residual bounds of the float Perron vectors (N15 conv.py formulas, unit-normalised vectors)
A0=A.Amat(0.0); gm=1.05*(D+4)*2*u*math.sqrt(2); dA0=float(np.sum(np.abs(A.COEF0)))*A.RAD*D
psiN=psi/np.linalg.norm(psi); PhiN=Phi/np.linalg.norm(Phi)
def res(Mm,v,l): return np.linalg.norm(Mm@v-l*v)*1.01+gm*np.linalg.norm(np.abs(Mm)@np.abs(v))*1.01+dA0*np.linalg.norm(v)+u*abs(l)*2*np.linalg.norm(v)
er=RA*res(A0,PhiN,s); el=RA*res(A0.T,psiN,s)
npsi2=float(np.linalg.norm(psi))*(1+1e-14); nPhi2=float(np.linalg.norm(Phi))*(1+1e-14)
ER=er*nPhi2; EL=el*npsi2                       # ||Phi~ - Pi_A Phi~||, ||psi~ - psi~ Pi_A||
den1=abs(psiPhi)-eps_p-npsi2*ER                 # <= |psi_A Phi_A| = |psi~ Pi_A Phi~|
nPsiT=npsi2+EL; nPhiT=math.sqrt(1+xs*xs)*(nPhi2+ER)   # ||psi_T||, ||Phi_T||
tau=dPi*nPsiT*nPhiT
mu_lo=abs(s)-mus
def tails(zz,KK=18):
    e1=zz[0]+zz[1]*Dg.S2; e2=zz[0]-zz[1]*Dg.S2
    L1=max(0,int(mp.ceil(mp.log(abs(e1)+1)/mp.log(Dg.LAM)))); L2=max(0,int(mp.ceil(mp.log(abs(e2)+1)/mp.log(Dg.LAM))))
    return float(abs(e1)*Dg.LAM**(-(KK+L1+1))/(1-1/Dg.LAM)+abs(e2)*Dg.LAM**(-(KK+L2+1))/(1-1/Dg.LAM))*(1+1e-12)
def chain(ds,tail,keep=None):
    n=len(ds)
    # forward core chain (c3 rounding recursion)
    v=Phi.copy(); e=0.0; F=[nPhi2]
    for d in ds:
        e=(NH(d)*e+loc(rig.fro(absstp(np.abs(v))),rig.fro(v),d,nT))*(1+4*u); v=stp(v,d)
        F.append((rig.fro(v)+nTi*e)*(1+1e-14))
    a=psi@v; Ea=npsi*e+cgam(D)*float(np.abs(psi)@np.abs(v))*1.01
    r=a/psiPhi; Pp=abs(psiPhi)
    rad=(Ea/(Pp-eps_p)+abs(a)*eps_p/(Pp*(Pp-eps_p))+1e-15*abs(r))*(1+1e-14)
    # backward core chain (dual-norm recursion), B[k] >= ||psi A_{>k}||, k=n..0
    w=psi.copy(); eb=0.0; B=[0.0]*(n+1); B[n]=npsi2
    for k in range(n,0,-1):
        d=ds[k-1]
        eb=(NH(d)*eb+loc(rig.fro(absstpT(np.abs(w))),rig.fro(w),d,nTi))*(1+4*u); w=stpT(w,d)
        B[k-1]=(rig.fro(w)+nT*eb)*(1+1e-14)
    GA=CONDH
    for d in ds: GA*=max(1.0,NH(d))
    GA*=1+1e-12
    GT=g*GA; q=1+Fs*GT; GL=GT*q**n
    # C1 projection
    err_proj=((EL*F[n]+B[0]*ER+EL*ER*GA)/den1+(abs(r)+rad)*npsi2*ER/den1)*(1+1e-12)
    # C2 perturbation, two-sided
    uu=[F[j]+GA*ER for j in range(n+1)]
    phi=[0.0]*(n+2); phi[1]=uu[0]*math.sqrt(1+xs*xs)
    for k in range(2,n+2): phi[k]=math.sqrt(uu[k-1]**2+(xs*uu[k-2])**2)
    b=[B[k]+EL*GA for k in range(n+1)]; bmax=max(b)
    beta=[b[k]+bmax*(q**(n-k)-1) for k in range(n+1)]
    err_pert=Fs/den1*sum(beta[k]*phi[k] for k in range(1,n+1))*(1+1e-12)
    TP=abs(r)+rad+err_proj+err_pert                               # >= |Tr(Pi_T P)|
    # C3 projector mismatch (with the second-order dPi^2 ||P|| term)
    VPf=phi[n+1]+Fs*GL*sum(phi[1:n+1]); VPb=beta[0]
    err_dPi=(dPi*nPsiT*VPf+dPi*nPhiT*VPb+dPi*dPi*nPsiT*nPhiT*GL+tau*TP)/(den1-tau)*(1+1e-12)
    TrPi=TP+err_dPi
    # C4 scale, C5 tails
    scale=(1+mus/(abs(s)-mus))**n-1
    sig=2*math.pi*N1*tail/mu_lo; eta=math.expm1(Cpow*sig)
    nPsiMu=nPsiT*(1+dPi)/(den1-tau); nPhiMu=nPhiT*(1+dPi)
    PPhiMu=VPf+GL*dPi*nPhiT; PsiMuP=(VPb+GL*dPi*nPsiT)/(den1-tau)
    err_tail=(eta*nPsiMu*PPhiMu+eta*PsiMuP*nPhiMu+eta*eta*nPsiMu*nPhiMu*GL)*(1+1e-12)
    E=(rad+err_proj+err_pert+err_dPi+TrPi*scale+(1+scale)*err_tail)*(1+1e-12)
    if keep is not None: keep.update(F=F,B=B,phi=phi,beta=beta,GL=GL,GA=GA,scale=scale,eta=eta,sig=sig,nPsiMu=nPsiMu,nPhiMu=nPhiMu,n=n)
    return r,E,dict(n=n,rad=rad,err_proj=err_proj,err_pert=err_pert,err_dPi=err_dPi,scale=scale,err_tail=err_tail,GA=GA,F_end=F[n],B0=B[0],
                    Fmax=max(F),Bmax=max(B),VPf=VPf,VPb=VPb)
def window(ea,eb):
    return [chain(Dg.core(zz,18),tails(zz)) for zz in Dg.seeds(ea,eb)]
def mulq(x,y): return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def lamp(G):
    r=(1,0)
    for _ in range(G): r=mulq(r,(3,2))
    return r
TYPES={'odd':(2,0),'sq2':(0,2),'two':(4,0),'2sq2':(0,4),'four':(8,0)}; EPS=(1,1)
CONST=dict(etaT=etaT,nT=nT,nTi=nTi,npsi=npsi,eps_p=eps_p,KAP=KAP,RADT=RADT,Lip2=Lip2,CONDH=CONDH,Fs=Fs,xs=xs,g=g,er=er,el=el,ER=ER,EL=EL,den1=den1,
           nPsiT=nPsiT,nPhiT=nPhiT,tau=tau,dPi=dPi,Pert=Pert,Xn=Xn,N1=N1,Cpow=Cpow,mus=mus,M=M_)
def run(jobs,out,part,nparts):
    done=set()
    if os.path.exists(out):
        for l in open(out): done.add(json.loads(l)['k'])
    t0=time.time()
    with open(out,'a') as f:
        for k,(kind,name,h,sg,G,e) in enumerate(jobs):
            if k%nparts!=part or k in done: continue
            w=window(*e); rw=dict(k=k,kind=kind,name=name,h=h,s=sg,G=G,e=list(e))
            for W,(r,E,inf) in zip('AB',w):
                rw[W]=dict(re=[r.real-E,r.real+E],im=[r.imag-E,r.imag+E],mid=[r.real,r.imag],abs_up=abs(r)+E,rad=E,conv=inf)
            f.write(json.dumps(rw)+'\n'); f.flush()
            if (k//nparts)%25==0: print(k,kind,name,G,'E/|r| %.3g %.3g'%(w[0][1]/abs(w[0][0]),w[1][1]/abs(w[1][0])),round(time.time()-t0),flush=True)
    print('done',round(time.time()-t0),flush=True)
if __name__=='__main__':
    mode=sys.argv[1]
    print(json.dumps(CONST),flush=True)
    if mode=='test':
        for e in ((2,0),(0,2),(8,0)):
            for r,E,inf in window(*e): print(e,abs(r),E,E/abs(r),json.dumps(inf),flush=True)
    elif mode=='replay':
        rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N15/logs/c3_mid.jsonl')]
        jobs=[(r['kind'],r['name'],r['h'],r['s'],r['G'],tuple(r['e'])) for r in sorted(rows,key=lambda r:r['k'])]
        part,nparts=int(sys.argv[2]),int(sys.argv[3])
        run(jobs,f'/workspace/bgs-lineN/N21/logs/convC_replay_p{part}.jsonl',part,nparts)
    elif mode=='ext':
        Glo,Ghi,part,nparts=map(int,sys.argv[2:6]); jobs=[]
        for G in range(Glo,Ghi+1):
          for ti in TYPES:
            for tj in TYPES:
              for h in (0,1):
                for sg in (1,-1):
                  ej=mulq(TYPES[tj],lamp(G))
                  if h: ej=mulq(ej,EPS)
                  jobs.append(('pair',f'{ti}+{tj}',h,sg,G,(TYPES[ti][0]+sg*ej[0],TYPES[ti][1]+sg*ej[1])))
        run(jobs,f'/workspace/bgs-lineN/N21/logs/convC_ext_{Glo}_{Ghi}_p{part}.jsonl',part,nparts)
