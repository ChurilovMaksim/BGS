"""Referee [N]: mixed classes at composite levels d = e*h_p containing the 16D=1 family (p = 19, q = h_p prime):
beta = CRT(beta_e, beta_fam), twists tau_i = Tr(lam^i beta_fam)/q + Tr(lam^i beta_e)/e (mod 1).  Reports |Zhat/Z0| and arg for
all unit beta_e mod 7 (e = 7) and a sample of beta_e mod 457 (e = 457, rank-3p prime), versus the family value c* e^{0.518 i}."""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineL/L2/code'); sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import mdata
from twlaw import TW, lam_pows, taus_of
p=19; m=3*p
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
q=hp(p); d=mdata(m); h=d['h']; M=2*h
x0=(pow(4,-1,M//2))%(M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1)
tw=TW(m,nu0,L=8,K=32); Z0=tw.Z([0.0]*m)
fam=json.load(open('/workspace/bgs-lineN/N5/logs/c_true_s1.json'))
b=[r for r in fam if r['p']==p][0]['beta']; bfam=(int(b[0]),int(b[1])); tf=taus_of(bfam,lam_pows(m,q),q)
zf=tw.Z(tf)/Z0
out=dict(p=p,q=q,family=[abs(zf),math.atan2(zf.imag,zf.real)],e7=[],e457=[])
pw7=lam_pows(m,7)
seen=set()
for bx in range(7):
    for by in range(7):
        if (bx*bx-2*by*by)%7==0: continue
        t7=taus_of((bx,by),pw7,7); key=tuple(sorted(set(t7)))
        z=tw.Z([(a+c)%1 for a,c in zip(tf,t7)])/Z0
        out['e7'].append(dict(beta7=[bx,by],abs=abs(z),arg=math.atan2(z.imag,z.real)))
rng=np.random.default_rng(3); pw=lam_pows(m,457)
for _ in range(12):
    be=(int(rng.integers(0,457)),int(rng.integers(1,457))); te=taus_of(be,pw,457)
    z=tw.Z([(a+c)%1 for a,c in zip(tf,te)])/Z0; out['e457'].append(dict(beta_e=list(be),abs=abs(z)))
a7=[r['abs'] for r in out['e7']]; out['e7_max_abs']=max(a7); out['e7_sum_abs']=sum(a7); out['e457_max_abs']=max(r['abs'] for r in out['e457'])
print(json.dumps({k:v for k,v in out.items() if k not in('e7','e457')})); json.dump(out,open('logs/ref_mixed_p19.json','w'),indent=1)
