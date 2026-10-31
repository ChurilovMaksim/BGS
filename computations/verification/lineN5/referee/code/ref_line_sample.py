"""Referee [N]: random sample of points on the isotropic lines at q = h_p (prime), m = 3p: |Zhat/Z0| distribution and
the Monte-Carlo estimate of the generic part of X = sum_{both lines} Zhat/Z0 (size bound), for comparison with the depth-class sum.
usage: p nsamp"""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineL/L2/code'); sys.path.insert(0,'/workspace/bgs-lineI/code')
from law import mdata
from twlaw import TW, lam_pows, taus_of
from sympy import sqrt_mod
p=int(sys.argv[1]); ns=int(sys.argv[2])
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
q=hp(p); m=3*p; d=mdata(m); h=d['h']; M=2*h
x0=(pow(4,-1,M//2))%(M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1)
tw=TW(m,nu0,L=8,K=32); Z0=tw.Z([0.0]*m); pw=lam_pows(m,q)
roots=[int(r) for r in sqrt_mod(2,q,all_roots=True)]
rng=np.random.default_rng(7); vals=[]
for i in range(ns):
    r=roots[i%2]; t=int(rng.integers(1,q)); beta=((r*t)%q,t)
    vals.append(tw.Z(taus_of(beta,pw,q))/Z0)
v=np.array(vals); a=np.abs(v)
res=dict(p=p,q=str(q),n=ns,abs_quantiles=[float(x) for x in np.quantile(a,[0,.5,.9,.99,1])],mean=[float(v.mean().real),float(v.mean().imag)],
  sem=float(v.std()/math.sqrt(ns)),generic_X_bound_MC=float(2*(q-1)*(abs(v.mean())+3*v.std()/math.sqrt(ns))))
print(json.dumps(res)); json.dump(res,open(f'logs/ref_line_sample_p{p}.json','w'),indent=1)
