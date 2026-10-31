"""N9b [N] (referee N8b-F7): evidence for G / G* on UNIT and MIXED (partially isotropic) points at larger p.
Point beta in Z[sqrt2]/h_p, twists tau_i = 2 Re-part(lambda^i beta mod d)/d (as N7 f_mixed.py), r = Z(beta)/Z(0) via N6 twb.Zbatch
(L2 TW law, L=8,K=16).  Classes: U = unit at every prime of h_p (random), US = small beta = a+b sqrt2 (|a|,|b|<=3, unit) [long slow windows], UM = |a|,|b| <= d^{1/4} (medium windows),
M = iso-or-0 mod q1 and unit mod the cofactor (random), for every prime q1 | h_p.
Reports Gamma_raw = mu* |r|^{1/m} (G with A=1, s=0) and Gamma_eff(theta) = mu* |r|^{1/(m-s)}, s = #{i : (tau_i,tau_{i+1}) within sup-dist
theta of (0,0) or (1/2,1/2)} (G*: all slow time).  usage: g_unitmix.py p N"""
import sys, json, random, math, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
from sympy import factorint, sqrt_mod
p=int(sys.argv[1]); N=int(sys.argv[2]); m=3*p; random.seed(1000+p); MU=1.9154732
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
d=xy(p)[0]; fac=factorint(d); primes=sorted(fac)
assert all(v==1 for v in fac.values())
def tw_seq(b):
    L=(1,0); out=[]
    for i in range(m):
        v=((L[0]*b[0]+2*L[1]*b[1])%d,(L[0]*b[1]+L[1]*b[0])%d); out.append((2*v[0]%d)/d); L=((3*L[0]+4*L[1])%d,(2*L[0]+3*L[1])%d)
    return out
def is_unit(b): return all((b[0]*b[0]-2*b[1]*b[1])%q for q in primes)
def rand_unit():
    while True:
        b=(random.randrange(d),random.randrange(d))
        if is_unit(b): return b
def crt(rs):  # rs: list of (q, (a,b) mod q)
    a=b=0
    for q,(x,y) in rs:
        u=(d//q)*pow(d//q,-1,q); a+=x*u; b+=y*u
    return (a%d,b%d)
def rand_iso_or0(q):
    if random.random()<1.0/q: return (0,0)
    w=int(sqrt_mod(2,q)); y=random.randrange(1,q); return ((random.choice((w,-w))*y)%q,y)
def rand_unit_q(q):
    while True:
        a,b=random.randrange(q),random.randrange(q)
        if (a*a-2*b*b)%q: return (a,b)
def tdist(x): x=x%1.0; return min(x,1-x)
def slow(tw_,th):
    s=0
    for i in range(m):
        a,b=tw_[i],tw_[(i+1)%m]
        if max(tdist(a),tdist(b))<th or max(tdist(a-.5),tdist(b-.5))<th: s+=1
    return s
pts={'U':[rand_unit() for _ in range(N)]}
pts['US']=[(a%d,b%d) for a in range(-3,4) for b in range(-3,4) if (a,b)!=(0,0) and is_unit((a%d,b%d))]
R=max(4,int(round(d**0.25)))
def rand_med():
    while True:
        b=(random.randint(-R,R)%d,random.randint(-R,R)%d)
        if is_unit(b): return b
pts['UM']=[rand_med() for _ in range(N)]
if len(primes)>=2:
    for q1 in primes:
        pts[f'M{q1}']=[crt([(q1,rand_iso_or0(q1))]+[(q,rand_unit_q(q)) for q in primes if q!=q1]) for _ in range(N)]
h,nu=nu_rho(m,1); tw=TW(m,nu,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]; t0=time.time(); out=dict(p=p,m=m,d=str(d),primes=[str(q) for q in primes],cls={})
for c,P in pts.items():
    T=[tw_seq(b) for b in P]; Z=[]
    for i in range(0,len(T),64): Z+=list(Zbatch(tw,T[i:i+64]))
    a=np.abs(np.array(Z))/abs(Z0)
    rec=dict(n=len(P),max_abs=float(a.max()),mean_abs=float(a.mean()),Gamma_raw_max=float(MU*a.max()**(1/m)),
             Gamma_raw_med=float(MU*np.median(a)**(1/m)))
    for th in (1/16,1/8):
        S=np.array([slow(t,th) for t in T]); ge=MU*a**(1/np.maximum(1,m-S))
        k=int(np.argmax(ge)); rec[f'th{th:.4f}']=dict(Gamma_eff_max=float(ge.max()),s_at_max=int(S[k]),abs_at_max=float(a[k]),s_max=int(S.max()),s_mean=float(S.mean()))
    out['cls'][c]=rec
    print(p,c,json.dumps(rec),round(time.time()-t0,1),flush=True)
open('logs/g_unitmix.jsonl','a').write(json.dumps(out)+'\n')
