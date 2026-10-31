"""N5 (D) [N]: factorisation of the dominant-family sum into excursion factors (gauge lemma + sector-4 rank-one).
Period of the 16D=1 family (p large): window at 1/2 (sector 4), excursion A (deviations +-(2-sqrt2)/4 lam^-k, antisymmetric),
window, excursion B (deviations sqrt2/4 lam^-|k|, symmetric).  Checks Zhat(family) = (rA rB)^3 Zhat(all 1/2) and Zhat(all 1/2)/Zhat(0)."""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineL/L2/code'); from twlaw import *
src=open('/workspace/bgs-lineN/N5/code/b_family.py').read().split("P=[int(t)")[0]; exec(src)
p=int(sys.argv[1]); m=3*p; q=hp(p); d=mdata(m); h=d['h']; M=2*h
x0=(pow(4,-1,M//2))%(M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1)
tw=TW(m,nu0,L=8,K=32)
c=gen(q); eps=(1,1)
for j in range(2*p):
    if ok(q,c): break
    if ok(q,(-c[0],-c[1])): c=(-c[0],-c[1]); break
    c=mul(c,eps)
A,B=q+c[0],c[1]; taus=[]
for i in range(m):
    taus.append(((2*A)%(4*q))/(4*q)); A,B=(3*A+4*B)%(4*q),(2*A+3*B)%(4*q)
dev=[((t-0.5+0.5)%1)-0.5 for t in taus]
big=[i for i in range(p) if abs(dev[i])>0.1]
print('excursion peaks in first period at',big,[round(dev[i],6) for i in big])
half=[0.5]*m
Zh=tw.Z(half); Z0=tw.Z([0.0]*m); Zf=tw.Z(taus)
def only(center,width=12):
    t=list(half)
    for i in range(center-width,center+width+1): t[i%m]=taus[i%m]
    return tw.Z(t)/Zh
peaksA=[i for i in big if abs(abs(dev[i])-(2-math.sqrt(2))/4)<1e-3]; peaksB=[i for i in big if abs(abs(dev[i])-math.sqrt(2)/4)<1e-3]
rA=only(peaksA[0]); rB=only(peaksB[0])
res=dict(p=p,peaksA=peaksA,peaksB=peaksB,Zhalf_over_Z0=complex(Zh/Z0).__abs__(),rA=[rA.real,rA.imag],rB=[rB.real,rB.imag],absrA=abs(rA),absrB=abs(rB),
  pred_ratio=abs((rA*rB)**3*Zh/Z0),true_ratio=abs(Zf/Z0),twosided_dev_A=[round(dev[(peaksA[0]+k)%m],8) for k in range(-4,5)],twosided_dev_B=[round(dev[(peaksB[0]+k)%m],8) for k in range(-4,5)])
print(json.dumps(res,indent=1)); json.dump(res,open(f'logs/d_excursion_p{p}.json','w'),indent=1)
