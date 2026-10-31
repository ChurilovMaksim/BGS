"""N6 (2) [N]: screened isotropic sum at prime level q = h_p.  X = 2 * sum_{s != 0} Zhat(s(w,1))/Z_rho (the conjugate line is equal by
Galois symmetry, checked in t_sym.py).  Orbits of <lam, -1> on the line (size 2p); keep orbits whose period-p twist sequence has >= thr
steps within 0.05 of {0, 1/2}; evaluate those with the true TW law (K=16).  usage: i_screen.py p thr [maxeval]"""
import sys, json, time, numpy as np
from sympy import sqrt_mod, isprime
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
p=int(sys.argv[1]); thr=int(sys.argv[2]); maxev=int(sys.argv[3]) if len(sys.argv)>3 else 4000
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
q=hp(p); assert isprime(q); m=3*p; w=int(sqrt_mod(2,q))
pw=lam_pows(p,q); lx=np.array([a for a,b in pw],dtype=np.int64); ly=np.array([b for a,b in pw],dtype=np.int64)
# point s(w,1): Tr(beta lam^i) = 2(bx x + 2 by y) = 2 s (w x + 2 y) ;  c_i = 2(w x_i + 2 y_i) mod q
c=(2*((w*lx)%q+2*ly))%q
# lam acts on the line by multiplication with r = eigenvalue: lam*(w,1) = (3w+4, 2w+3) = r (w,1) with r = 2w+3
r=(2*w+3)%q
t0=time.time(); cand=[]; CH=1<<20
for s0 in range(1,q,CH):
    s=np.arange(s0,min(q,s0+CH),dtype=np.int64)
    # canonical: s minimal in orbit {+-s r^k}; cheap filter: compute slow count for all s, keep those passing, canonicalise later
    tau=((s[:,None]*c[None,:])%q)/q
    dd=np.minimum(np.abs(((tau+0.5)%1)-0.5),np.abs(tau-0.5))
    sl=(dd<0.05).sum(1)
    keep=s[sl>=thr]; cand.extend(keep.tolist())
cand=set(cand); reps={}
for s in cand:
    orb=[]; x=s
    for k in range(p): orb.append(x); orb.append(q-x); x=(x*r)%q
    reps[min(orb)]=len(set(orb))
reps=sorted(reps.items())
print('p',p,'q',q,'candidates',len(cand),'orbits',len(reps),'screen sec',round(time.time()-t0,1),flush=True)
assert len(reps)<=maxev
h,nu0=nu_rho(m,1); tw=TW(m,nu0,L=8,K=16); pwm=lam_pows(m,q)
z0=Zbatch(tw,[[0.0]*m])[0]
T=np.array([taus_of(((s*w)%q,s),pwm,q) for s,_ in reps]); Z=np.zeros(len(reps),complex)
for i in range(0,len(reps),32): Z[i:i+32]=Zbatch(tw,T[i:i+32])
sz=np.array([n for _,n in reps]); ratio=Z/z0
X=2*(sz*ratio).sum()
dd=np.minimum(np.abs(((T+0.5)%1)-0.5),np.abs(T-0.5)); sl=(dd<0.05).sum(1)
o=np.argsort(-np.abs(sz*ratio))
top=[dict(s=int(reps[j][0]),size=int(sz[j]),ratio=[ratio[j].real,ratio[j].imag],slow=int(sl[j])) for j in o[:15]]
res=dict(p=p,q=q,thr=thr,norbits=len(reps),X=[X.real,X.imag],twoReX=2*X.real,sec=round(time.time()-t0,1),top=top)
json.dump(res,open(f'logs/i_screen_p{p}_thr{thr}.json','w'),indent=1); print(json.dumps(res)[:1500])
