"""N6 [N]: complex ratios. Zhat(all 1/2)/Zhat(0); the 16D=1 (sector-1/2) family and the sector-0 depth-1 family (beta = gamma, |N gamma| = q) at q = h_p prime."""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
src=open('/workspace/bgs-lineN/N5/code/b_family.py').read().split("P=[int(t)")[0]; exec(src)
sg=int(sys.argv[2]) if len(sys.argv)>2 else 1; out=[]
for p in [int(t) for t in sys.argv[1].split(',')]:
    m=3*p; q=hp(p); h,nu0=nu_rho(m,sg); tw=TW(m,nu0,L=8,K=32); pw=lam_pows(m,q)
    g=gen(q); i4=pow(4,-1,q)
    # sector-1/2 family: beta=(q+c)/4 with c ~ unit multiples of g satisfying ok(); sector-0: beta=c mod q
    T=[[0.0]*m,[0.5]*m]; lab=['zero','half']; gg=g
    for j in range(2):
        for s in (1,-1):
            c=(s*gg[0],s*gg[1])
            T.append(taus_of(((c[0])%q,(c[1])%q),pw,q)); lab.append(f'sec0_j{j}_s{s}')
            if ok(q,c): T.append(taus_of((((q+c[0])*i4)%q,(c[1]*i4)%q),pw,q)); lab.append(f'sec4_j{j}_s{s}')
        gg=mul(gg,(1,1))
    Z=Zbatch(tw,T); r=Z/Z[0]
    rec=dict(p=p,sg=sg,ratios={l:[float(x.real),float(x.imag)] for l,x in zip(lab,r)})
    print(json.dumps(rec),flush=True); out.append(rec)
json.dump(out,open(f'logs/g_sign_s{sg}.json','w'),indent=1)
