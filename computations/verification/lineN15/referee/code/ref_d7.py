"""Referee lineN15 (N17b spot-check): Dev_7(rho)/(phi m) for rho=(+-2,8) at m=15,21,33,39 via TRACE-204/212 (I2') member formula,
own code: own y' (h^2+1=2y'^2), own twists tau_i=Tr(beta lam^i)/7 for ALL 49 beta (no orbit/sign/Galois reduction), own member set
(nu = nu_rho + 2hj/7 unit mod 2h, j=1..6), own phi(2h).  Shared (refereed) pieces: N6 twb.Zbatch/TW transfer law (L=8,K=16) and nu_rho.
Also reports the max relative difference |Zhat(beta)-Zhat(beta')| and |Zhat(beta)-Zhat(-beta)| (symmetries used by N17b d_g3dev)."""
import os; os.environ.setdefault('OMP_NUM_THREADS','1')
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import Zbatch, TW, nu_rho
from sympy import totient
d=7; out={}
for m in [int(a) for a in sys.argv[1:]]:
    x,y=1,1
    for _ in range(m-1): x,y=x+2*y,x+y          # (1+sqrt2)^m = x + y sqrt2
    h=x; assert h*h+1==2*y*y and h%7==0; yp=y; M=2*h; phi=int(totient(M))
    for sg in (1,-1):
        h_,nu0=nu_rho(m,sg); assert h_==h; tw=TW(m,nu0,L=8,K=16)
        B=[(a,b) for a in range(d) for b in range(d)]; T=[]
        for (a,b) in B:
            ta=[]; u,v=a,b
            for i in range(m): ta.append(((2*u)%d)/d); u,v=(3*u+4*v)%d,(2*u+3*v)%d
            T.append(ta)
        Zh=Zbatch(tw,np.array(T)); Zd={B[i]:Zh[i] for i in range(len(B))}; Z0=Zd[(0,0)]; Z02=abs(Z0)**2
        gal=max(abs(Zd[(a,b)]-Zd[(a,(-b)%d)])/abs(Z0) for (a,b) in B); neg=max(abs(Zd[(a,b)]-Zd[((-a)%d,(-b)%d)])/abs(Z0) for (a,b) in B)
        S=0.0; n=0
        for j in range(1,d):
            nu=(nu0+(M//d)*j)%M
            if math.gcd(nu,M)!=1: continue
            t=(j*yp)%d; tb=pow(t,-1,d)
            z=abs(sum(np.exp(2j*np.pi*((tb*((a*a-2*b*b)%d))%d)/d)*Zd[(a,b)] for (a,b) in B))**2/d**2
            S+=z; n+=1
        dev=S-n*Z02/d/d
        r=dict(m=m,rho=[2*sg,8],n7=n,Dev_over_phim=dev/phi/m,Dev_rel_main=dev/(n*Z02/d/d),S_units=dev/(Z02/phi/(h if False else 1)),galois_sym_maxrel=gal,neg_sym_maxrel=neg)
        hp=None
        if m%3==0:
            pp=m//3; xx,yy=1,1
            for _ in range(pp-1): xx,yy=xx+2*yy,xx+yy
            hp=xx; Srho=Z02/phi/hp; r['Dev_over_Srho_over_m']=dev/phi/(Srho/m) if False else (dev/phi)/(Srho/m)
        r.pop('S_units'); out[f'{m}_{2*sg}']=r; print(json.dumps(r),flush=True)
json.dump(out,open('logs/ref_d7.json','w'),indent=1)
