"""N9 [N]: isotropic classes at ALL FOUR lambda-fixed points z in (sqrt2/8)O/O^vee = {0, 1/4, sqrt2/8, 1/4+sqrt2/8}
(N8b erratum to N7 Lemma P'(i): 4 fixed points, not 8). Point x = z + e*gamma/(8q), e in -8 z gammabar + 2sqrt2 O (coset),
twist tau_i = Tr(lam^i x) mod 1 computed EXACTLY from w8 = 8qz + e*gamma in O:  tau_i = Tr(lam^i w8)/(8q).
Representatives e: |N(e)| <= K, balanced mod lam (|e1/e2| in [1/lam, lam)), +-e identified (Zhat(-x)=Zhat(x)).
usage: a_bases.py p K"""
import sys, json, math
from fractions import Fraction as Fr
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); K=int(sys.argv[2]); m=3*p; k=(p-1)//2
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
q=xy(p)[0]; g=(xy(k+1)[0],xy(k)[1]); assert g[0]**2-2*g[1]**2==q
gb=(g[0],-g[1]); S2=math.sqrt(2); LAM=3+2*S2
# z as (8z) in O: 0, 2, sqrt2, 2+sqrt2
Z8={'0':(0,0),'q':(2,0),'s':(0,1),'qs':(2,1)}
def in2s2O(u):  # u in 2sqrt2 O  <=>  u = 2sqrt2(a+b sqrt2) = 4b + 2a sqrt2 : u0 % 4 == 0 and u1 % 2 == 0
    return u[0]%4==0 and u[1]%2==0
reps={}
B=int(3*math.sqrt(K))+6
for zt,z8 in Z8.items():
    sh=mul(z8,gb)
    for a in range(-B,B+1):
        for b in range(-B,B+1):
            n=a*a-2*b*b
            if n==0 or abs(n)>K: continue
            if not in2s2O((a+sh[0],b+sh[1])): continue
            e1=a+b*S2; e2=a-b*S2; r=abs(e1/e2)
            if not (1/LAM-1e-12<=r<LAM-1e-12): continue
            key=(zt,)+tuple(max((a,b),(-a,-b)))
            reps[key]=n
items=sorted(reps.items(),key=lambda t:(abs(t[1]),t[0]))
def twist(z8,e):
    w=mul(g,e); w=(q*z8[0]+w[0],q*z8[1]+w[1]); out=[]; L=(1,0)
    for i in range(m):
        v=mul(L,w); out.append(float(Fr(2*v[0],8*q)%1)); L=mul(L,(3,2))
    return out
pts=[twist(Z8[key[0]],(key[1],key[2])) for key,n in items]
res=[]
for sg in (1,-1):
    h,nu=nu_rho(m,sg); tw=TW(m,nu,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]; Zs=[]
    for i in range(0,len(pts),32): Zs+=list(Zbatch(tw,pts[i:i+32]))
    for (key,n),zz in zip(items,Zs): res.append(dict(sg=sg,z=key[0],e=[key[1],key[2]],N=n,r=[(zz/Z0).real,(zz/Z0).imag]))
json.dump(dict(p=p,K=K,q=str(q),gamma=list(g),res=res),open(f'/workspace/bgs-lineN/N9/logs/a_bases_p{p}_K{K}.json','w'),indent=1)
for r in sorted([r for r in res if r['sg']==1],key=lambda r:-abs(complex(*r['r']))):
    print(r['z'],r['e'],r['N'],'%.4e %+.4e |%.3e|'%(r['r'][0],r['r'][1],abs(complex(*r['r']))))
