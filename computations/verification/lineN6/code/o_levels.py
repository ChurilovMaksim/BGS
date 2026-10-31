"""N6 (2) [N]: included levels d | h_m (m = 3p) with h_p | d (frozen TRACE-206 rule: d <= sqrt h, |Z_rho|^2/d^2 >= 4m), and the fully
isotropic linear sum at d = 7 h_p split by CRT into  (beta_7 = 0: inherited level-h_p family) + (beta_p = 0: level-7 iso) + (mixed).
usage: o_levels.py p"""
import sys, json, math, itertools, numpy as np
from sympy import factorint, divisors, sqrt_mod
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); m=3*p
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
q=hp(p); h,nu0=nu_rho(m,1); tw=TW(m,nu0,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]
fac=factorint(h); levels=[]
for d in divisors(h):
    if d>1 and d%q==0 and d*d<=h and abs(Z0)**2/d**2>=4*m: levels.append(d)
print('p',p,'h_m factors',fac,'included levels with h_p|d:',[(d,factorint(d)) for d in levels],flush=True)
d=7*q; assert h%d==0
def isoline(r):
    w=int(sqrt_mod(2,r)); pts=[(0,0)]
    for y in range(1,r): pts+= [((w*y)%r,y),((-w*y)%r,y)]
    return pts
P7=isoline(7); Pq=isoline(q) if q<10**5 else None
u7=q*pow(q,-1,7); uq=7*pow(7,-1,q)
pw=lam_pows(m,d)
def tw_of(b7,bq):
    bx=(b7[0]*u7+bq[0]*uq)%d; by=(b7[1]*u7+bq[1]*uq)%d
    return taus_of((bx,by),pw,d)
parts={'inherited':0j,'level7':0j,'mixed':0j}; cnt={'inherited':0,'level7':0,'mixed':0}
batch=[];lab=[]
for b7 in P7:
    for bq in Pq:
        if b7==(0,0) and bq==(0,0): continue
        k='inherited' if b7==(0,0) else ('level7' if bq==(0,0) else 'mixed')
        batch.append(tw_of(b7,bq)); lab.append(k)
Z=np.zeros(len(batch),complex)
for i in range(0,len(batch),64): Z[i:i+64]=Zbatch(tw,batch[i:i+64])
for k,z in zip(lab,Z): parts[k]+=z/Z0; cnt[k]+=1
res=dict(p=p,m=m,levels=[str(x) for x in levels],d=d,counts=cnt,parts={k:[v.real,v.imag] for k,v in parts.items()})
print(json.dumps(res)); json.dump(res,open(f'logs/o_levels_p{p}.json','w'),indent=1)
