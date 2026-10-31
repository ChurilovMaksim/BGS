"""Referee [N]: adjudicate 'fixed points 4 vs 8' and test whether the two genuine fixed points NOT used by N7/N8
(z = sqrt2/8 and z = 1/4 + sqrt2/8) carry shallow isotropic classes missing from N7's numerics / N8's certified list.
For h_p prime: x = z + e*gamma/(8q); keep e with x in (1/q)O^vee and N(q x 4/sqrt2) = 0 mod q (isotropic), e small.
Twists tau_i = Tr(lam^i u)/(8q) mod 1, u = 8q x in O (exact integers). |Zhat/Z| via N6 twb (L=8,K=16)."""
import os; os.environ.setdefault('OMP_NUM_THREADS','2'); os.environ.setdefault('OPENBLAS_NUM_THREADS','2')
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import Zbatch, nu_rho, TW
from fractions import Fraction as Fr
p=int(sys.argv[1]); R=int(sys.argv[2]); m=3*p; k=(p-1)//2
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
q=xy(p)[0]; g=(xy(k+1)[0],xy(k)[1])          # gamma = x_{k+1} + y_k sqrt2
def mul(a,b): return (a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
assert abs(g[0]**2-2*g[1]**2)==q
# fixed points: (lam-1) z in O^vee  <=> z in (1/2)O^vee = (sqrt2/8)O.  8z as element of O (scaled by 8): z=(a + b sqrt2)/8
# check which z in (1/8)O/O^vee are lam-fixed: lam z - z = 2 eps z must be in O^vee=(sqrt2/4)O
def in_Ovee_scaled(v,s):   # is v/s in (sqrt2/4)O ?  v/s = (sqrt2/4) w  <=> w = 4 v/(s sqrt2) = (4/s)(v1 + v0 sqrt2/2)... do exactly
    # v/s*(4/sqrt2) = (4/s)*(v0/sqrt2 + v1) = (4/s)*(v1 + (v0/2) sqrt2)
    a=Fr(4*v[1],s); b=Fr(4*v[0],2*s); return a.denominator==1 and b.denominator==1
Z8=[(a,b) for a in range(0,8) for b in range(0,8)]
reps=[]
for z in Z8:   # dedupe mod O^vee
    if not any(in_Ovee_scaled((z[0]-r[0],z[1]-r[1]),8) for r in reps): reps.append(z)
fixed=[z for z in reps if in_Ovee_scaled(mul((2,2),z),8)]      # 2 eps z, eps = 1+sqrt2 -> (2,2)
out=dict(p=p,q=q,n_reps_1_8O_mod_Ovee=len(reps),fixed=[list(z) for z in fixed],classes=[])
print('reps',len(reps),'fixed',fixed,flush=True)
h,nu=nu_rho(m,1); tw=TW(m,nu,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]
LAM=(3,2)
cand=[]
for z in fixed:
    for e1 in range(-R,R+1):
        for e2 in range(-R,R+1):
            if (e1,e2)==(0,0): continue
            ug=mul((e1,e2),g); u=(q*z[0]+ug[0], q*z[1]+ug[1])      # u = 8q x
            # x in (1/q)O^vee <=> q x = u/8 in (sqrt2/4)O
            if not in_Ovee_scaled(u,8): continue
            v=(Fr(4*u[1],8),Fr(4*u[0],16))   # v = q x * 4/sqrt2 in O
            v=(int(v[0]),int(v[1]))
            if (v[0]**2-2*v[1]**2)%q: continue
            if v[0]%q==0 and v[1]%q==0: continue
            cand.append((z,(e1,e2),abs(e1*e1-2*e2*e2)))
# dedupe by point mod O^vee: x = u/(8q); compare u mod 8q*O^vee
seen={}; pts=[]
for z,e,N in sorted(cand,key=lambda t:t[2]):
    ug=mul(e,g); u=(q*z[0]+ug[0], q*z[1]+ug[1])
    key=None
    # canonical: v mod q (v in O/qO)
    v=(int(Fr(4*u[1],8))%q,int(Fr(4*u[0],16))%q); key=v
    if key in seen: continue
    seen[key]=1; pts.append((z,e,N,u))
pts=[t for t in pts if t[2]<=60][:200]
T=[]
for z,e,N,u in pts:
    a=u; seq=[]
    for i in range(m):
        seq.append(((2*a[0])%(8*q))/(8*q)); a=mul(LAM,a); a=(a[0]%(8*q*4),a[1]%(8*q*4))
    T.append(seq)
Z=[]
for i in range(0,len(T),64): Z+=list(Zbatch(tw,T[i:i+64]))
for (z,e,N,u),zz,seq in zip(pts,Z,T):
    r=zz/Z0
    out['classes'].append(dict(z=list(z),e=list(e),N=N,r=[r.real,r.imag],absr=abs(r),window_twist=round(min(seq,key=lambda t:min(t,1-t)) ,6)))
for zc in fixed:
    cl=[c for c in out['classes'] if c['z']==list(zc)]
    cl.sort(key=lambda c:-c['absr'])
    print('z',zc,'n',len(cl),'top',[(c['e'],c['N'],'%.4g'%c['absr'],'%.3g'%c['r'][0]) for c in cl[:6]],flush=True)
json.dump(out,open(f'logs/ref_bases_p{p}.json','w'),indent=1)
