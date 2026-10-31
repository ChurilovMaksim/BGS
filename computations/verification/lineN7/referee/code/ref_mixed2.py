"""Referee [N]: independent Monte Carlo of N7 F7 mixed classes at composite h_p (different seed), with a K=16 vs K=32 truncation
check on the same samples, and identification of the outliers (is b1 = 0, i.e. a proper-divisor-level point?).
usage: ref_mixed2.py p N seed"""
import sys, json, random, numpy as np, time
from sympy import factorint, sqrt_mod
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import Zbatch, nu_rho, TW
p,N,seed=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]); m=3*p; random.seed(seed)
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
d=xy(p)[0]; q1,q2=sorted(factorint(d))
def iso_set(q):
    w=int(sqrt_mod(2,q)); s={(0,0)}
    for y in range(1,q): s.add(((w*y)%q,y)); s.add(((-w*y)%q,y))
    return sorted(s)
def rand_unit(q):
    while True:
        a,b=random.randrange(q),random.randrange(q)
        if (a*a-2*b*b)%q: return (a,b)
def crt(b1,b2):
    u1=q2*pow(q2,-1,q1); u2=q1*pow(q1,-1,q2)
    return ((b1[0]*u1+b2[0]*u2)%d,(b1[1]*u1+b2[1]*u2)%d)
def tw_seq(b):
    L=(1,0); out=[]
    for i in range(m):
        v=((L[0]*b[0]+2*L[1]*b[1])%d,(L[0]*b[1]+L[1]*b[0])%d); out.append((2*v[0]%d)/d); L=((3*L[0]+4*L[1])%d,(2*L[0]+3*L[1])%d)
    return out
I1,I2=iso_set(q1),iso_set(q2)
h,nu=nu_rho(m,1); out=dict(p=p,d=d,q1=q1,q2=q2,N=N,seed=seed)
tws={K:TW(m,nu,L=8,K=K) for K in (16,32)}
KCHK=int(sys.argv[4]) if len(sys.argv)>4 else 60
Z0={K:Zbatch(tws[K],[[0.0]*m])[0] for K in tws}
nd=(q1-2)*(q2-2); fam=4*p*nd*3.43578e-4
for cls in ('A','B'):
    meta=[]; pts=[]
    for _ in range(N):
        if cls=='A': b1=random.choice(I1); b2=rand_unit(q2); meta.append(b1==(0,0))
        else: b1=rand_unit(q1); b2=random.choice(I2); meta.append(b2==(0,0))
        pts.append(tw_seq(crt(b1,b2)))
    A={}; t=time.time(); Z=[]
    for i in range(0,N,64): Z+=list(Zbatch(tws[16],pts[i:i+64]))
    A[16]=np.abs(np.array(Z))/abs(Z0[16]); out[f'time_K16_{cls}']=time.time()-t
    idx=list(np.argsort(-A[16])[:KCHK//2])+random.sample(range(N),KCHK//2)
    t=time.time(); Z32=[]
    for i in range(0,len(idx),32): Z32+=list(Zbatch(tws[32],[pts[j] for j in idx[i:i+32]]))
    a32=np.abs(np.array(Z32))/abs(Z0[32]); out[f'time_K32_{cls}']=time.time()-t
    A[32]=A[16].copy(); A[32][idx]=a32
    out[f'K16_vs_K32_{cls}']=[[float(A[16][j]),float(v)] for j,v in zip(idx,a32)][:12]
    size=(len(I1)*(q2*q2-len(I2))) if cls=='A' else ((q1*q1-len(I1))*len(I2))
    meta=np.array(meta); a=A[32]
    S=size*np.mean(a*2*((q1 if cls=='A' else q2)-2)); se=size*np.std(a*2*((q1 if cls=='A' else q2)-2))/np.sqrt(N)
    top=np.argsort(-a)[:5]
    out[cls]=dict(size=size,mean_K16=float(A[16].mean()),mean_K32=float(a.mean()),max_K32=float(a.max()),
        max_rel_diff_K16_K32_checked=float(np.max(np.abs(A[16][idx]-a32)/(a32+1e-300))),
        top5=[dict(abs=float(a[i]),zero_component=bool(meta[i])) for i in top],
        frac_zero_component=float(meta.mean()),mean_zero_comp=float(a[meta].mean()) if meta.any() else None,
        mean_nonzero=float(a[~meta].mean()),ratio=float(S/fam),ratio_se=float(se/fam),
        ratio_without_zero_comp=float(size*np.mean(np.where(meta,0,a)*2*((q1 if cls=='A' else q2)-2))/fam))
    print(cls,json.dumps(out[cls]),flush=True)
json.dump(out,open(f'logs/ref_mixed2_p{p}_s{seed}.json','w'),indent=1)
