"""N7b [N]: exact isotropic-line sums at prime conductors Q | h_m, Q not in {7, h_p} (gap (b) fully-isotropic pattern).
Line 1 = {s*(w,1)}: orbit-reduced under s -> s*ell (lam), s -> -s; line 2 = conjugate line (Zhat(conj beta) = Zhat(beta), N6 t_sym).
X_Q = sum_{iso beta != 0} Zhat/Z_rho;  rel_signed = ((Q-2)/Q^2)/((h_p-2)/h_p^2) * Re X_Q / Re X_fam  (iso Lin at Q over family Lin at h_p);
rel_abs same with sum|Zhat/Z|.  usage: e_iso.py p Q1 [Q2 ...]"""
import sys, json, math, numpy as np
from sympy import sqrt_mod
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); Qs=[int(a) for a in sys.argv[2:]]; m=3*p
def hpf(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
hp=hpf(p); h,nu0=nu_rho(m,1); tw=TW(m,nu0,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]
XH={5:0.003533,7:0.010724,11:0.016493,13:0.019429,19:0.028554}; ReX=XH.get(p,4*p*3.4358e-4*1.08)
for Q in Qs:
    assert h%Q==0
    w=int(sqrt_mod(2,Q)); pw=lam_pows(m,Q)
    # ell = lam acting on line 1: lam*(w,1) = (3w+4, 2w+3) = ell*(w,1) -> ell = 2w+3 mod Q
    ell=(2*w+3)%Q; assert (ell*w-(3*w+4))%Q==0
    seen=np.zeros(Q,bool); reps=[]; sizes=[]
    for s in range(1,Q):
        if seen[s]: continue
        orb=set(); t=s
        while t not in orb: orb.add(t); orb.add((-t)%Q); t=(t*ell)%Q
        for t in orb: seen[t]=True
        reps.append(s); sizes.append(len(orb))
    T=[taus_of(((s*w)%Q,s),pw,Q) for s in reps]; z=np.zeros(len(T),complex)
    for i in range(0,len(T),64): z[i:i+64]=Zbatch(tw,T[i:i+64])
    z/=Z0; sizes=np.array(sizes)
    X=2*complex(np.sum(sizes*z)); A=2*float(np.sum(sizes*np.abs(z)))
    fac=((Q-2)/Q**2)/((hp-2)/hp**2)
    rec=dict(p=p,m=m,Q=Q,orbits=len(reps),X=[X.real,X.imag],sum_abs=A,max_abs=float(np.abs(z).max()),
             rate_max=float((np.abs(z).max()*abs(Z0))**(1/m)),rel_signed=fac*X.real/ReX,rel_abs=fac*A/ReX)
    print(json.dumps(rec),flush=True)
    open('/workspace/bgs-lineN/N7b/logs/e_iso.jsonl','a').write(json.dumps(rec)+'\n')
