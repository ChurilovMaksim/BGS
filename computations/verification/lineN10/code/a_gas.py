"""N10 [N]: finite-p test of the multi-bump (polymer/gas) picture on the line (gamma) at q = h_p, background z = 1/4.
Classes alpha (odd), x = 1/4 + gamma*alpha/(4q) (e = 2alpha), exact twists tau_i = Tr(lam^i x) mod 1 (as N7 e_isodepth), Zhat/Z_rho for sg=+1.
 fam: alpha = 1
 2-bump: alpha = 1 + s*beta*lam^g, beta in even seeds, s = +-1, g = 1..G
 3-bump: alpha = 1 + lam^g1 + lam^g2
usage: a_gas.py p G"""
import sys, json, math
from fractions import Fraction as Fr
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); G=int(sys.argv[2]); m=3*p; k=(p-1)//2
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def add(u,v): return (u[0]+v[0],u[1]+v[1])
def sc(s,u): return (s*u[0],s*u[1])
q=xy(p)[0]; g=(xy(k+1)[0],xy(k)[1]); assert g[0]**2-2*g[1]**2==q
lp=[(1,0)]
for i in range(60): lp.append(mul(lp[-1],(3,2)))
BETA={'r2':(0,1),'2':(2,0),'2+r2':(2,1),'2-r2':(2,-1),'2r2':(0,2),'4':(4,0)}
cls=[('fam',0,0,(1,0))]
for bn,b in BETA.items():
    for s in (1,-1):
        for gg in range(1,G+1): cls.append((f'{bn}',s,gg,add((1,0),sc(s,mul(b,lp[gg])))))
for g1,g2 in [(2,5),(3,7),(4,9),(3,12),(5,15),(2,18)]:
    if g2<=G: cls.append(('tri',g1,g2,add((1,0),add(lp[g1],lp[g2]))))
def twist(al):
    w=mul(g,al); w=(q+w[0],w[1]); out=[]; L=(1,0)
    for i in range(m):
        v=mul(L,w); out.append(float(Fr(2*v[0],4*q)%1)); L=mul(L,(3,2))
    return out
pts=[twist(c[3]) for c in cls]
h,nu=nu_rho(m,1); tw=TW(m,nu,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]; Zs=[]
for i in range(0,len(pts),32): Zs+=list(Zbatch(tw,pts[i:i+32])); print('batch',i,flush=True)
res=[dict(type=c[0],s=c[1],g=c[2],alpha=list(c[3]),r=[(z/Z0).real,(z/Z0).imag]) for c,z in zip(cls,Zs)]
json.dump(dict(p=p,G=G,res=res),open(f'/workspace/bgs-lineN/N10/logs/a_gas_p{p}_G{G}.json','w'),indent=1)
for r in res: print(r['type'],r['s'],r['g'],'%.4e %+.4e'%tuple(r['r']))
