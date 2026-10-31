"""N11 [N]: single-class (single-bump-type) weights over ALL classes alpha mod +-eps^j with |N(alpha)| <= Nmax, both backgrounds:
 bg 1/4: x = 1/4 + 2 alpha gamma/(8q), N(alpha) odd;  bg 0: x = 2sqrt2 alpha' gamma/(8q), alpha' != 0.
Twists exact (Fractions), Zhat/Z from TW (L=8,K=16), sg=+1.  usage: t_classes.py p Nmax"""
import sys, json, math
from fractions import Fraction as Fr
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); Nmax=int(sys.argv[2]); m=3*p; k=(p-1)//2
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
q=xy(p)[0]; g=(xy(k+1)[0],xy(k)[1]); assert g[0]**2-2*g[1]**2==q
EPS=(1,1); EPSI=(-1,1)
def canon(a):
    best=None; u=a
    reps=[]
    for _ in range(40): u=mul(u,EPSI)
    for j in range(80):
        reps.append(u); reps.append((-u[0],-u[1])); u=mul(u,EPS)
    mn=min(r[0]**2+2*r[1]**2 for r in reps)
    return max(r for r in reps if r[0]**2+2*r[1]**2==mn)
B=int(math.sqrt(3*Nmax))+2
cls={'q':set(),'0':set()}
for a in range(-B,B+1):
    for b in range(-B,B+1):
        if (a,b)==(0,0) or a*a+2*b*b>3*Nmax: continue
        N=a*a-2*b*b
        if abs(N)>Nmax: continue
        c=canon((a,b))
        if N%2: cls['q'].add(c)
        cls['0'].add(c)
items=[('q',c) for c in sorted(cls['q'])]+[('0',c) for c in sorted(cls['0'])]
def twist(bg,al):
    if bg=='q': e=(2*al[0],2*al[1]); z8=(2,0)
    else: e=(4*al[1],2*al[0]); z8=(0,0)          # e = 2 sqrt2 alpha'
    w=mul(g,e); w=(q*z8[0]+w[0], q*z8[1]+w[1]); out=[]; L=(1,0)
    for i in range(m):
        v=mul(L,w); out.append(float(Fr(2*v[0],8*q)%1)); L=mul(L,(3,2))
    return out
pts=[twist(bg,c) for bg,c in items]
h,nu=nu_rho(m,1); tw=TW(m,nu,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]; Zs=[]
for i in range(0,len(pts),32): Zs+=list(Zbatch(tw,pts[i:i+32])); print('batch',i,len(pts),flush=True)
res=[dict(bg=bg,alpha=list(c),N=c[0]**2-2*c[1]**2,r=[(z/Z0).real,(z/Z0).imag]) for (bg,c),z in zip(items,Zs)]
json.dump(dict(p=p,Nmax=Nmax,res=res),open(f'/workspace/bgs-lineN/N11/logs/t_classes_p{p}_N{Nmax}.json','w'),indent=1)
print('done',len(res))
