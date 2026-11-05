"""Truncation check: Zhat(beta)/Z_rho at K=12,16,24 (L=8) and L=10 for sample betas at m=33, level h_11=8119."""
import sys, numpy as np, json
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
m=33; h,nu0=nu_rho(m,1); D=8119; pw=lam_pows(m,D)
rng=np.random.default_rng(5)
betas=[(0,0)]
# isotropic: Nm = 0 mod 8119
iso=[(a,b) for a in range(0,400) for b in range(0,400) if (a*a-2*b*b)%D==0 and (a,b)!=(0,0)][:4]
betas+=iso+[tuple(map(int,rng.integers(0,D,2))) for _ in range(4)]
T=np.array([taus_of(b,pw,D) for b in betas])
out={}
for (L,K) in [(8,12),(8,16),(8,24),(10,16)]:
    tw=TW(m,nu0,L=L,K=K); Z=Zbatch(tw,T); out[(L,K)]=Z/Z[0]
    print(L,K,'Z0=%.6e'%abs(Z[0]),' '.join('%.3e'%abs(z) for z in (Z/Z[0])[1:]),flush=True)
ref=out[(8,24)]
for k,v in out.items(): print(k,'max abs diff vs (8,24):', '%.2e'%np.max(np.abs(v[1:]-ref[1:])), 'max rel', '%.2e'%np.max(np.abs(v[1:]-ref[1:])/np.abs(ref[1:])))
print('betas',betas)
