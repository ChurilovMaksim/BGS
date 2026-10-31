"""N13 (C) [CA for the core functional]: arb replay of the two-bump interaction windows (coded types: eps-gap n=2G+h>=5, G<=15)
and of the single windows.  For each window: d_t enclosures from exact seeds (N8 core(), KK=18), arb chain
v <- A(d_t) v / s over the N6 cert_core blocks (radii included), r~ = psi~ v / (psi~ Phi~)  (Phi~, psi~, s~ = stored binary64 data).
Stores |r~| enclosure + per-step |d_t| upper bounds (for the core->true conversion in d_post.py).  Sequential, resumable (jsonl).
usage: c_replay.py [start] [stop]"""
import sys, json, time, math, os, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code')
import cert_core as C
from flint import arb, acb, acb_mat, ctx
ctx.prec=96
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz')
sf=complex(z['s']); Phif=z['Phi']; psif=z['psi']
K=C.K; lam=C.lam; r2=arb(2).sqrt()
s=acb(sf.real,sf.imag); sinv=1/s
cores=sorted(C.idx,key=lambda c:C.idx[c])
def vecblocks(x): return {c2:acb_mat(K,1,[acb(complex(x[C.idx[c2]*K+i]).real,complex(x[C.idx[c2]*K+i]).imag) for i in range(K)]) for c2 in cores}
PHI=vecblocks(Phif); PSI=vecblocks(psif)
ns=sorted(set(n for (c2,n) in C.blocks)); W4={n:C.wa(4,n)*sinv for n in ns}
BL=[(c2,n,j2,Mx) for (c2,n),(j2,Mx) in C.blocks.items()]
def step(v,d):
    co={n:W4[n]*C.e(arb(n)*d) for n in ns}
    out={c2:acb_mat(K,1) for c2 in cores}
    for c2,n,j2,Mx in BL:
        out[c2]=out[c2]+(Mx*v[j2])*co[n]
    return out
def dot(u,v):
    t=acb(0)
    for c2 in cores:
        for i in range(K): t+=u[c2][i,0]*v[c2][i,0]
    return t
PSIPHI=dot(PSI,PHI)
KK=18
def red(x): n=(x+arb(1)/2).floor(); return x-n
def core(zu,zv):
    e1=zu+zv*r2; e2=zu-zv*r2
    L1=max(0,math.ceil(float((abs(e1)+1).log()/lam.log()))); L2=max(0,math.ceil(float((abs(e2)+1).log()/lam.log())))
    ds=[red(e1*lam**j) if j<=0 else red(-e2*lam**(-j)) for j in range(-(KK+L1),KK+L2+1)]
    tail=abs(e1)*lam**(-(KK+L1+1))/(1-1/lam)+abs(e2)*lam**(-(KK+L2+1))/(1-1/lam)
    return ds,tail
def seeds(ea,eb):   # k even convention (N8): zeta_A = e sqrt2/8, zeta_B = -e eps^{-1} sqrt2/8
    zA=(arb(2*eb)/8,arb(ea)/8); fu=-ea+2*eb; fv=ea-eb; zB=(-arb(2*fv)/8,-arb(fu)/8); return zA,zB
def window(ea,eb):
    out=[]
    for zz in seeds(ea,eb):
        ds,tail=core(*zz); v=PHI
        for d in ds: v=step(v,d)
        r=dot(PSI,v)/PSIPHI
        out.append(dict(re=[float(r.real.lower()),float(r.real.upper())],im=[float(r.imag.lower()),float(r.imag.upper())],
                        abs_up=float(abs(r).upper()),rad=float(max(r.real.rad(),r.imag.rad())),
                        d_up=[float(abs(d).upper()) for d in ds],tail=float(tail.upper()),n=len(ds)))
    return out
def mulq(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def lamp(G):
    r=(1,0)
    for _ in range(G): r=mulq(r,(3,2))
    return r
TYPES={'odd':(2,0),'sq2':(0,2),'two':(4,0),'2sq2':(0,4),'four':(8,0)}; EPS=(1,1)
jobs=[('single',t,0,0,0,TYPES[t]) for t in TYPES]+[('single_eps',t,1,0,0,mulq(TYPES[t],EPS)) for t in TYPES]
for ti in TYPES:
    for tj in TYPES:
        for h in (0,1):
            for sg in (1,-1):
                for G in range(0,16):
                    if 2*G+h<5: continue
                    ej=mulq(TYPES[tj],lamp(G))
                    if h: ej=mulq(ej,EPS)
                    jobs.append(('pair',f'{ti}+{tj}',h,sg,G,(TYPES[ti][0]+sg*ej[0],TYPES[ti][1]+sg*ej[1])))
# N12-referee F1: the n=2G+h<5 'pairs' (200 types) appended at the END (indices of coded jobs unchanged): short clusters / relabellings
for ti in TYPES:
    for tj in TYPES:
        for h in (0,1):
            for sg in (1,-1):
                for G in range(0,16):
                    if 2*G+h>=5 or (G==0 and h==0): continue
                    ej=mulq(TYPES[tj],lamp(G))
                    if h: ej=mulq(ej,EPS)
                    jobs.append(('short',f'{ti}+{tj}',h,sg,G,(TYPES[ti][0]+sg*ej[0],TYPES[ti][1]+sg*ej[1])))
OUT='/workspace/bgs-lineN/N13/logs/c_replay.jsonl'
done=set()
if os.path.exists(OUT):
    for l in open(OUT): done.add(json.loads(l)['k'])
a=int(sys.argv[1]) if len(sys.argv)>1 else 0; b=int(sys.argv[2]) if len(sys.argv)>2 else len(jobs)
print('jobs',len(jobs),'done',len(done),flush=True)
with open(OUT,'a') as f:
    for k in range(a,min(b,len(jobs))):
        if k in done: continue
        kind,name,h,sg,G,e=jobs[k]; t0=time.time()
        w=window(*e)
        f.write(json.dumps(dict(k=k,kind=kind,name=name,h=h,s=sg,G=G,e=list(e),A=w[0],B=w[1],secs=round(time.time()-t0,1)))+'\n'); f.flush()
        print(k,kind,name,h,sg,G,'|rA|<=%.6g |rB|<=%.6g rad %.2g'%(w[0]['abs_up'],w[1]['abs_up'],max(w[0]['rad'],w[1]['rad'])),round(time.time()-t0,1),flush=True)
