"""N11b [N]: exact-twist unit-point weights r(beta) = Z(beta)/Z(0) at level h_p (twlaw: tau_i = Tr(lam^i beta)/h_p), for small beta
(single-bump unit types) and two-bump configurations beta = u1 + s*u2*lam^g (gas test).  usage: a_unit_types.py p"""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); m=3*p
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
h=xy(p)[0]
def mul(u,v): return ((u[0]*v[0]+2*u[1]*v[1])%h,(u[0]*v[1]+u[1]*v[0])%h)
def taus(b):
    L=(1,0); out=[]
    for i in range(m):
        v=mul(L,b); out.append((2*v[0]%h)/h); L=mul(L,(3,2))
    return out
hh,nu=nu_rho(m,1); tw=TW(m,nu,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]
def r_of(bl):
    T=[taus((a%h,b%h)) for a,b in bl]; Z=[]
    for i in range(0,len(T),32): Z+=list(Zbatch(tw,T[i:i+32]))
    return [z/Z0 for z in Z]
mode=sys.argv[2] if len(sys.argv)>2 else 'single'
out=dict(p=p,mode=mode,rows=[])
if mode=='single':
    bl=[(a,b) for a in range(-6,7) for b in range(-5,6) if (a,b)!=(0,0) and math.gcd(abs(a*a-2*b*b),h)==1]
    rs=r_of(bl)
    for (a,b),r in zip(bl,rs): out['rows'].append(dict(beta=[a,b],N=a*a-2*b*b,r=[r.real,r.imag],absr=abs(r)))
else:  # two-bump: u1=1 or eps, u2 in small list, gap g
    U=[(1,0),(1,1),(-1,1),(0,1),(2,1)]
    bl=[];meta=[]
    for u1 in [(1,0),(1,1)]:
        for u2 in U:
            for s in (1,-1):
                for g in (3,5,7,9,11):
                    L=(1,0)
                    for _ in range(g): L=((3*L[0]+4*L[1]),(2*L[0]+3*L[1]))
                    v=(u2[0]*L[0]+2*u2[1]*L[1],u2[0]*L[1]+u2[1]*L[0])
                    b=(u1[0]+s*v[0],u1[1]+s*v[1])
                    if math.gcd(abs(b[0]**2-2*b[1]**2)%h or h,h)!=1: continue
                    bl.append(b); meta.append((u1,u2,s,g))
    rs=r_of(bl)
    for (u1,u2,s,g),b,r in zip(meta,bl,rs): out['rows'].append(dict(u1=u1,u2=u2,s=s,g=g,r=[r.real,r.imag],absr=abs(r)))
json.dump(out,open(f'logs/a_unit_{mode}_p{p}.json','w'),indent=1)
rows=sorted(out['rows'],key=lambda x:-x['absr'])
for x in rows[:25]: print(x,flush=True)
