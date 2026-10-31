"""N14 (C') N13-F3 fix: mid-point replay with RIGOROUS a-posteriori error propagation in the adapted norm H (no ball-radius compounding).
Same objects as N13 c_replay (cert_core operator, stored npz s~, Phi~, psi~, exact seeds, KK=18, same job list & order).
Chain v^_k = fl(X^(d^_k) v^_{k-1}),  X = A(d)/s~.  Error e_k = v_k - v^_k (H-norm):
   ||e_k||_H <= N_H(d_k) ||e_{k-1}||_H + ||T||_2 ( ||delta_k||_2 + ||(X(d_k)-X^(d^_k)) v^_{k-1}||_2 )
 rounding  ||delta_k||_2 <= 2e-14 || Xabs |v^| ||_2   (Xabs = sum_n |c_n/s||M_n|; einsum/add.at/exp error, gamma_~150 with margin)
 data+twist ||dX v^||_2 <= 2e-14 || Xabs |v^| ||_2 + Lip_2 |d - d^| ||v^||_2   (|d-d^| <= 2^-52|d|; RAD entry radii 8e-20 included)
 N_H(d): |d|<=1/256: 1 + 1.01e-12 + 4260 d^2  [CA, N13 b2 + referee partition];  |d|>1/256: cell bound (width h)
         n_H(center) [float SVD of sum c_n e(n c) T M_n T^-1 / s, + formation error, /(1-||T Ti - I||)] + Lip_H h/2 (Lip_H=167.214 [CA]).
 Final: r = psi~ v / (psi~ Phi~),  |psi~ e| <= ||psi~ T^-1||_2 ||e||_H.   Output jsonl like c_replay (A/B: re, im, rad).
 Label [CA-fp]: IEEE binary64 with explicit a-priori rounding bounds (not interval arithmetic)."""
import sys, os, json, time, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); sys.path.insert(0,'/workspace/bgs-lineN/N12/code')
import a_ops as A, digits as Dg
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz')
T=z['T']; s=complex(z['s']); Phi=z['Phi'].astype(complex); psi=z['psi'].astype(complex); Ti=np.linalg.inv(T)
D=A.D; K=55; NB=D//K; NS=A.NS.astype(float); C=A.COEF0/s; LIP_H=167.21344682844932
etaT=np.linalg.norm(T@Ti-np.eye(D),2)*1.01; nT=np.linalg.norm(T,2)*(1+1e-12); npsi=np.linalg.norm(psi@Ti,2)*(1+1e-12)/(1-etaT)
psiPhi=psi@Phi
bl=[]
for k in range(len(A.NS)):
    for ib in range(NB):
        for jb in range(NB):
            B=A.MS[k][ib*K:(ib+1)*K, jb*K:(jb+1)*K]
            if np.abs(B).max()>0: bl.append((k,ib,jb,B))
BK=np.array([b[0] for b in bl]); BI=np.array([b[1] for b in bl]); BJ=np.array([b[2] for b in bl]); BB=np.array([b[3] for b in bl]); BA=np.abs(BB)
CA=np.abs(C)
def stp(v,d):
    c=C*np.exp(2j*np.pi*NS*d); vb=v.reshape(NB,K)
    y=np.einsum('bij,bj->bi',BB,vb[BJ])*c[BK][:,None]; out=np.zeros((NB,K),complex); np.add.at(out,BI,y); return out.reshape(D)
def absstp(va):
    vb=va.reshape(NB,K); y=np.einsum('bij,bj->bi',BA,vb[BJ])*CA[BK][:,None]; out=np.zeros((NB,K)); np.add.at(out,BI,y); return out.reshape(D)
Lip2=2*math.pi*sum(abs(n)*CA[k]*np.linalg.norm(A.MS[k],2) for k,n in enumerate(NS))*1.01
# cell cache for N_H
TMf='/workspace/bgs-lineN/N14/logs/c2_TM.npy'
TM=None; aF=None
CACHE='/workspace/bgs-lineN/N14/logs/c2_NH_cache.json'; H_CELL=2e-4
cache=json.load(open(CACHE)) if os.path.exists(CACHE) else {}
def NH(d):
    global TM,aF
    if abs(d)<=1/256: return 1+1.01e-12+4260*d*d
    key=str(round(d/H_CELL))
    if key not in cache:
        if TM is None:
            TM=np.array([T@Mk@Ti for Mk in A.MS]); aF=np.array([np.linalg.norm(np.abs(T)@np.abs(Mk)@np.abs(Ti)) for Mk in A.MS])
        cc=round(d/H_CELL)*H_CELL
        S=np.tensordot(C*np.exp(2j*np.pi*NS*cc),TM,1)
        n=np.linalg.norm(S,2); err=2.5e-13*float(CA@aF)+1e-13*n
        cache[key]=(n*(1+1e-12)+err)/(1-etaT)+LIP_H*H_CELL/2*1.0000001
        json.dump(cache,open(CACHE,'w'))
    return cache[key]
def chain(ds):
    v=Phi.copy(); e=0.0; ints=0
    for d in ds:
        va=absstp(np.abs(v)); nv=np.linalg.norm(v)
        loc=nT*(4e-14*np.linalg.norm(va)+Lip2*abs(d)*2.3e-16*nv)
        e=NH(d)*e+loc; v=stp(v,d)
    r=psi@v/psiPhi; rad=npsi*e/abs(psiPhi)*(1+1e-15)+1e-16*abs(r)
    return r,rad
def window(ea,eb):
    out=[]
    for zz in Dg.seeds(ea,eb):
        ds=Dg.core(zz,18); r,rad=chain(ds)
        out.append(dict(re=[r.real-rad,r.real+rad],im=[r.imag-rad,r.imag+rad],abs_up=abs(r)+rad,rad=rad,n=len(ds)))
    return out
# job list identical to N13 c_replay
def mulq(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def lamp(G):
    r=(1,0)
    for _ in range(G): r=mulq(r,(3,2))
    return r
TYPES={'odd':(2,0),'sq2':(0,2),'two':(4,0),'2sq2':(0,4),'four':(8,0)}; EPS=(1,1)
jobs=[('single',t,0,0,0,TYPES[t]) for t in TYPES]+[('single_eps',t,1,0,0,mulq(TYPES[t],EPS)) for t in TYPES]
for short in (False,True):
  for ti in TYPES:
    for tj in TYPES:
        for h in (0,1):
            for sg in (1,-1):
                for G in range(0,16):
                    n=2*G+h
                    if (not short and n<5) or (short and (n>=5 or (G==0 and h==0))): continue
                    ej=mulq(TYPES[tj],lamp(G))
                    if h: ej=mulq(ej,EPS)
                    jobs.append(('short' if short else 'pair',f'{ti}+{tj}',h,sg,G,(TYPES[ti][0]+sg*ej[0],TYPES[ti][1]+sg*ej[1])))
if __name__=='__main__':
    OUT='/workspace/bgs-lineN/N14/logs/c2_mid.jsonl'; done=set()
    if os.path.exists(OUT):
        for l in open(OUT): done.add(json.loads(l)['k'])
    a=int(sys.argv[1]) if len(sys.argv)>1 else 0; b=int(sys.argv[2]) if len(sys.argv)>2 else len(jobs)
    print('jobs',len(jobs),'etaT',etaT,'|T|',nT,'|psi|_H*',npsi,'Lip2',Lip2,flush=True)
    with open(OUT,'a') as f:
        for k in range(a,min(b,len(jobs))):
            if k in done: continue
            kind,name,h,sg,G,e=jobs[k]; t0=time.time(); w=window(*e)
            f.write(json.dumps(dict(k=k,kind=kind,name=name,h=h,s=sg,G=G,e=list(e),A=w[0],B=w[1],secs=round(time.time()-t0,2)))+'\n'); f.flush()
            if k%20==0: print(k,kind,name,h,sg,G,'rad/|r| %.2g %.2g'%(w[0]['rad']/abs(complex(sum(w[0]['re'])/2,sum(w[0]['im'])/2)),w[1]['rad']/abs(complex(sum(w[1]['re'])/2,sum(w[1]['im'])/2))),len(cache),round(time.time()-t0,2),flush=True)
