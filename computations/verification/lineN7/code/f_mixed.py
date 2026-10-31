"""N7 F7 [N, Monte Carlo]: mixed isotropic/unit classes at composite level d = h_p = q1*q2 (p = 11: 23*353; p = 13: 79*599).
Class A: beta iso-or-0 mod q1, unit mod q2;  class B: unit mod q1, iso-or-0 mod q2.  Lin weight |kappa_d| = |kappa_q1|*|kappa_q2| with
|kappa_q(0)| = q-2 and |kappa_q(u)| <= 2 for u != 0 (J3 sec 3).  Estimate S_class = sum_{beta in class} |kappa||Zhat_beta| / |Z_rho| by sampling,
and compare with the family term 4p*n_d*Re w* (same normalisation (2/d^2)|Z|).  usage: f_mixed.py p N"""
import sys, json, random, numpy as np
from sympy import factorint, sqrt_mod
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); N=int(sys.argv[2]); m=3*p; random.seed(12345)
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
d=xy(p)[0]; f=factorint(d); assert len(f)==2 and all(v==1 for v in f.values()); q1,q2=sorted(f)
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
def kap(q,isz): return (q-2) if isz else 2
res={}
h,nu=nu_rho(m,1); tw=TW(m,nu,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]
for cls in ('A','B'):
    pts=[]; wts=[]
    for _ in range(N):
        if cls=='A': b1=random.choice(I1); b2=rand_unit(q2); w=kap(q1,True)*2
        else: b1=rand_unit(q1); b2=random.choice(I2); w=2*kap(q2,True)
        pts.append(tw_seq(crt(b1,b2))); wts.append(w)
    Z=[]
    for i in range(0,N,64): Z+=list(Zbatch(tw,pts[i:i+64]))
    a=np.abs(np.array(Z))/abs(Z0)
    size=(len(I1)*(q2*q2-len(I2))) if cls=='A' else ((q1*q1-len(I1))*len(I2))
    S=size*np.mean(a*np.array(wts)); se=size*np.std(a*np.array(wts))/np.sqrt(N)
    res[cls]=dict(size=size,mean_abs=float(a.mean()),max_abs=float(a.max()),S=float(S),S_se=float(se))
nd=(q1-2)*(q2-2); fam=4*p*nd*3.43578e-4
out=dict(p=p,m=m,d=d,q1=q1,q2=q2,N=N,classes=res,family_term=fam,ratio_A=res['A']['S']/fam,ratio_B=res['B']['S']/fam)
print(json.dumps(out,indent=1)); json.dump(out,open(f'/workspace/bgs-lineN/N7/logs/f_mixed_p{p}.json','w'),indent=1)
