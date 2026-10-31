"""N5 (C) [N]: TRUE TRACE-206 twisted sums (L2 twlaw transfer law, L=8, K=32, exactly as N2 d_level_split) at the dominant isotropic family
(16D = 1) of q = h_p, for p with h_p prime.  beta = (q+gamma)/4 mod q (checked: its twists equal Tr(lam^i (q+gamma))/(4q) mod 1 for all i).
Reports |Zhat|, |Zhat|^{1/m}, |Z_rho| = |Zhat(0)|, and the family's iso cross rate (4p (q-2)/q^2 |Zhat|)^{1/m} vs T = 1.28359.
usage: c_true.py p[,p...] [sign]"""
import sys, json, math, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineL/L2/code'); sys.path.insert(0,'/workspace/bgs-lineN/N5/code')
from twlaw import *
src=open('/workspace/bgs-lineN/N5/code/b_family.py').read().split("P=[int(t)")[0]; exec(src)
sg=int(sys.argv[2]) if len(sys.argv)>2 else 1; out=[]
for p in [int(t) for t in sys.argv[1].split(',')]:
    m=3*p; q=hp(p); t0=time.time()
    d=mdata(m); h=d['h']; M=2*h; assert h%q==0, (h%q)
    x0=(sg*pow(4,-1,M//2))%(M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1); assert (8*nu0-2*sg)%M==0
    tw=TW(m,nu0,L=8,K=32); pw=lam_pows(m,q)
    g=gen(q); eps=(1,1); found=None; gg=g
    for j in range(2*p):
        for s in (1,-1):
            c=(s*gg[0],s*gg[1])
            if not ok(q,c): continue
            i4=pow(4,-1,q); beta=(((q+c[0])*i4)%q,(c[1]*i4)%q)
            mine=[]; A,B=q+c[0],c[1]
            for i in range(m):
                mine.append(((2*A)%(4*q))/(4*q)); A,B=(3*A+4*B)%(4*q),(2*A+3*B)%(4*q)
            theirs=taus_of(beta,pw,q)
            if max(min(abs(a-b),1-abs(a-b)) for a,b in zip(mine,theirs))<1e-9: found=(beta,theirs); break
        if found: break
        gg=mul(gg,eps)
    assert found, 'no matching beta'
    beta,taus=found
    z=tw.Z(taus); z0=tw.Z([0.0]*m)
    rec=dict(p=p,m=m,q=q,beta=[int(beta[0]),int(beta[1])] if q<2**62 else [str(beta[0]),str(beta[1])],absZhat=float(abs(z)),root=float(abs(z))**(1/m),
             absZrho=float(abs(z0)),Zrho_root=float(abs(z0))**(1/m),family_iso_rate=float(4*p*(q-2)/q**2*abs(z))**(1/m),T=1.28359,sec=round(time.time()-t0,1))
    out.append(rec); print(json.dumps(rec),flush=True)
json.dump(out,open(f'logs/c_true_s{sg}.json','w'),indent=1)
