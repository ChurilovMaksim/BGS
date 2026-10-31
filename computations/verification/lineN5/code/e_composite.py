"""N5 (E) [N]: same as c_true.py but at the full level d = h_p for COMPOSITE squarefree h_p (all prime factors split).
For each square root r of 2 mod d (up to sign: one ideal of norm d per choice), gamma = Gauss-reduced generator (|N gamma| = d),
y = (d+gamma)/(4d) realised as beta = (d+gamma)/4 mod d (twists checked exactly).  Weight of a beta that is isotropic at every prime of d:
prod_q (q-2)/q^2 (J3 prime-level weights, CRT; squarefree).  Family size 2p per ideal choice; the ideal choices give the same |Zhat| up to conjugation
(checked on two choices).  Rate = (2^omega * 2p * prod (q-2)/q^2 * |Zhat|)^{1/m}."""
import sys, json, math, numpy as np
from sympy import factorint, sqrt_mod
sys.path.insert(0,'/workspace/bgs-lineL/L2/code'); from twlaw import *
src=open('/workspace/bgs-lineN/N5/code/b_family.py').read().split("P=[int(t)")[0]; exec(src)
def gen_r(d,r):
    u=(d,0); v=(r,1); f=lambda w: w[0]*w[0]+2*w[1]*w[1]; dot=lambda w,z: w[0]*z[0]+2*w[1]*z[1]
    if f(u)<f(v): u,v=v,u
    while True:
        k=(2*dot(u,v)+f(v))//(2*f(v)); u=(u[0]-k*v[0],u[1]-k*v[1])
        if f(u)>=f(v): break
        u,v=v,u
    for w in (v,u):
        if abs(w[0]**2-2*w[1]**2)==d: return w
    return None
out=[]
for p in [int(t) for t in sys.argv[1].split(',')]:
    m=3*p; dd=hp(p); fac=factorint(dd); assert all(e==1 for e in fac.values()), fac
    D=mdata(m); h=D['h']; M=2*h; assert h%dd==0
    x0=(pow(4,-1,M//2))%(M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1)
    tw=TW(m,nu0,L=8,K=32); pw=lam_pows(m,dd); Z0=tw.Z([0.0]*m)
    roots=sorted(set(min(r,dd-r) for r in sqrt_mod(2,dd,all_roots=True)))
    vals=[]
    for r in roots:
        g=gen_r(dd,r)
        if g is None: continue
        found=None; gg=g
        for j in range(2*p):
            for s in (1,-1):
                c=(s*gg[0],s*gg[1])
                if not ok(dd,c): continue
                i4=pow(4,-1,dd); beta=(((dd+c[0])*i4)%dd,(c[1]*i4)%dd)
                A,B=dd+c[0],c[1]; mine=[]
                for i in range(m):
                    mine.append(((2*A)%(4*dd))/(4*dd)); A,B=(3*A+4*B)%(4*dd),(2*A+3*B)%(4*dd)
                th=taus_of(beta,pw,dd)
                if max(min(abs(a-b),1-abs(a-b)) for a,b in zip(mine,th))<1e-9: found=th; break
            if found: break
            gg=mul(gg,eps:=(1,1))
        if found: vals.append(abs(tw.Z(found)))
    wt=1.0
    for q in fac: wt*=(q-2)/q**2
    om=len(fac); z=max(vals)
    rec=dict(p=p,m=m,d=dd,factors=list(map(int,fac)),absZhat=[float(v) for v in vals],ratio_to_Zrho=float(z/abs(Z0)),
             family_rate=float(2**om*2*p*wt*z)**(1/m),T=1.28359)
    out.append(rec); print(json.dumps(rec),flush=True)
json.dump(out,open('logs/e_composite.json','w'),indent=1)
