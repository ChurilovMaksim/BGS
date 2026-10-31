"""N15 REPORT_N14_v2 / F14.1: c2_mid.py with DERIVED rounding constants.  [CA-fp: IEEE std model + libm <=1 ulp]  (rig.py header).
Same objects, job list and order as N14 c2_mid / N13 c_replay.  Changes vs c2_mid:
 (i)  per-op constant: |fl(X^ v) - X^ v|_i <= kap (Xabs|v^|)_i with kap = max(1e-13, 1.25*kap_derived),
      kap_derived = (1+eps_c)(1+cgam(55))(1+sqrt2 gam(2))(1+gam(M)) - 1,  M = max #blocks summed into one output block (np.add.at),
      eps_c = 4u*2pi*30*0.5 + 16u  (phase arg 2pi n d: 4 roundings; cos/sin 1 ulp; C_n=fl(COEF0/s) complex division; C*e product).
      Xabs|v^| evaluated in float, divided by (1-gam(57+M+4)) to make it an upper bound.
 (ii) data: |M^-M| <= RAD entrywise (arb radius) + u|M^| (mid rounding), COEF0 mid rounding 2u: + 2u||Xabs|v^|| + RAD*D*sum|C_n| ||v^||.
      twist: Lip2 = 2pi sum|n||C_n| ||M_n||_F (Frobenius: no SVD) times |d-d^| <= 2.3e-16|d|.
 (iii) ||T||_2 <= ||T||_F (rigorous); eta_T >= ||T Ti - I||_2 via Frobenius + matmul error (rig); ||psi T^-1|| <= (||fl(psi Ti)||+cgam(D)|| |psi||Ti| ||)/(1-eta_T).
 (iv) N_H(d): |d|<=1/256 [CA] 1+1.01e-12+4260 d^2;  else SVD-free table nh_table_rig_2048.json (cell containing d, both cells at a boundary).
 (v)  final r^ = fl(psi.v^)/fl(psi.Phi): numerator error npsi*e + cgam(D) |psi|.|v^|; denominator error eps_p = cgam(D)|psi|.|Phi|;
      |r - r^| <= E_a/(|p^|-eps_p) + |a^| eps_p/(|p^|(|p^|-eps_p)) + 1e-15|r^|."""
import sys, os, json, time, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); sys.path.insert(0,'/workspace/bgs-lineN/N15/code')
import a_ops as A, digits as Dg, rig
from rig import u, gam, cgam
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz')
T=z['T']; s=complex(z['s']); Phi=z['Phi'].astype(complex); psi=z['psi'].astype(complex); Ti=np.linalg.inv(T)
D=A.D; K=55; NB=D//K; NS=A.NS.astype(float); C=A.COEF0/s
P,eP=rig.matmul_err(T,Ti); etaT=rig.fro(P-np.eye(D))+eP; nT=rig.fro(T)
pTi=psi@Ti; npsi=(rig.fro(pTi)+cgam(D)*rig.fro(np.abs(psi)@np.abs(Ti)))/(1-etaT)*(1+1e-15)
psiPhi=psi@Phi; eps_p=cgam(D)*float(np.abs(psi)@np.abs(Phi))*1.01
bl=[]
for k in range(len(A.NS)):
    for ib in range(NB):
        for jb in range(NB):
            B=A.MS[k][ib*K:(ib+1)*K, jb*K:(jb+1)*K]
            if np.abs(B).max()>0: bl.append((k,ib,jb,B))
BK=np.array([b[0] for b in bl]); BI=np.array([b[1] for b in bl]); BJ=np.array([b[2] for b in bl]); BB=np.array([b[3] for b in bl]); BA=np.abs(BB)
CA=np.abs(C)*(1+8*u)
M=int(np.bincount(BI).max())
eps_c=4*u*2*math.pi*30*0.5+16*u
kap_der=(1+eps_c)*(1+cgam(K))*(1+math.sqrt(2)*gam(2))*(1+gam(M))-1
KAP=max(1e-13,1.25*kap_der)+2*u        # + COEF0/M mid rounding
ABSDIV=1/(1-gam(K+M+6))
RADT=A.RAD*D*float(np.abs(C).sum())*1.01
Lip2=2*math.pi*sum(abs(n)*CA[k]*rig.fro(A.MS[k]) for k,n in enumerate(NS))*1.01
def stp(v,d):
    c=C*np.exp(2j*np.pi*NS*d); vb=v.reshape(NB,K)
    y=np.einsum('bij,bj->bi',BB,vb[BJ])*c[BK][:,None]; out=np.zeros((NB,K),complex); np.add.at(out,BI,y); return out.reshape(D)
def absstp(va):
    vb=va.reshape(NB,K); y=np.einsum('bij,bj->bi',BA,vb[BJ])*CA[BK][:,None]; out=np.zeros((NB,K)); np.add.at(out,BI,y); return out.reshape(D)
TAB=json.load(open('/workspace/bgs-lineN/N15/logs/nh_table_rig_2048.json')); TB=TAB['bound']; TH=TAB['h']
def NH(d):
    if abs(d)<=1/256: return 1+1.01e-12+4260*d*d
    x=(d+0.5)/TH; k=int(math.floor(x)); k=min(max(k,0),len(TB)-1)
    b=TB[k]
    if x-k<1e-9 and k>0: b=max(b,TB[k-1])
    if k+1-x<1e-9 and k+1<len(TB): b=max(b,TB[k+1])
    return b
def chain(ds):
    v=Phi.copy(); e=0.0
    for d in ds:
        va=absstp(np.abs(v)); nva=rig.fro(va)*ABSDIV; nv=rig.fro(v)
        loc=nT*(KAP*nva+RADT*nv+Lip2*abs(d)*2.3e-16*nv)*(1+1e-14)
        e=(NH(d)*e+loc)*(1+4*u); v=stp(v,d)
    a=psi@v; Ea=npsi*e+cgam(D)*float(np.abs(psi)@np.abs(v))*1.01
    r=a/psiPhi; P=abs(psiPhi)
    rad=(Ea/(P-eps_p)+abs(a)*eps_p/(P*(P-eps_p))+1e-15*abs(r))*(1+1e-14)
    return r,rad
def window(ea,eb):
    out=[]
    for zz in Dg.seeds(ea,eb):
        ds=Dg.core(zz,18); r,rad=chain(ds)
        out.append(dict(re=[r.real-rad,r.real+rad],im=[r.imag-rad,r.imag+rad],abs_up=abs(r)+rad,rad=rad,n=len(ds)))
    return out
sys.argv_save=sys.argv; sys.argv=[sys.argv[0]]
import c2_mid as OLD
sys.argv=sys.argv_save; jobs=OLD.jobs
if __name__=='__main__':
    OUT='/workspace/bgs-lineN/N15/logs/c3_mid.jsonl'; done=set()
    if os.path.exists(OUT):
        for l in open(OUT): done.add(json.loads(l)['k'])
    print('jobs',len(jobs),'M',M,'eps_c',eps_c,'kap_der',kap_der,'KAP',KAP,'etaT',etaT,'|T|_F',nT,'npsi',npsi,'eps_p',eps_p,'RADT',RADT,'Lip2',Lip2,flush=True)
    with open(OUT,'a') as f:
        for k in range(len(jobs)):
            if k in done: continue
            kind,name,h,sg,G,e=jobs[k]; t0=time.time(); w=window(*e)
            f.write(json.dumps(dict(k=k,kind=kind,name=name,h=h,s=sg,G=G,e=list(e),A=w[0],B=w[1],secs=round(time.time()-t0,2)))+'\n'); f.flush()
            if k%100==0: print(k,kind,name,G,'%.3g %.3g'%(w[0]['rad'],w[1]['rad']),round(time.time()-t0,2),flush=True)
