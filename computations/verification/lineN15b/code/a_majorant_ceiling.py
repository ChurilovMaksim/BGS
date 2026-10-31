"""N15b pre-flight [N]: ceiling of ANY equidistribution/exponential-sum route that passes through the C' collision majorant.
F(beta) = prod_{i<p} g(tau_i), g(t) = |sum_a |J_a(1.8)| e(a t)|^2 (Prop-E majorant, mid letters, tau=0; sup g = g(0) = 5.614, mean 1),
tau_i = Tr(lam^i beta)/h (twist law of N11b/N13b). Compares
  E_G F (beta mod h), E_{H_d} F (mixed classes, iso part d), and the 'Lebesgue' value int F (beta mod h*M, M large prime).
Perfect-equidistribution prediction: E_{H_d} F ~ int F + (mass/N_b) ~ int F * (1 + C d kappa^p), kappa = 0.915.
usage: a_majorant_ceiling.py p NS"""
import sys, json, math, numpy as np, mpmath as mp
from sympy import factorint
p=int(sys.argv[1]); NS=int(sys.argv[2]); rng=np.random.default_rng(1000+p)
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
h=xy(p)[0]; fac=sorted(factorint(h))
u=np.array([float(abs(mp.besselj(a,1.8))) for a in range(-40,41)]); A=np.arange(-40,41)
GR=1<<16; tg=np.arange(GR)/GR; gg=np.abs(np.exp(2j*np.pi*np.outer(tg,A))@u)**2; lg=np.log(gg)
def lam_pows(mod):
    LA=[1];LB=[0]
    for i in range(p-1): a,b=LA[-1],LB[-1]; LA.append((3*a+4*b)%mod); LB.append((2*a+3*b)%mod)
    return np.array(LA,dtype=object),np.array(LB,dtype=object)
def logF(a,b,mod):
    LA,LB=lam_pows(mod); s=np.zeros(len(a))
    a=a.astype(object); b=b.astype(object)
    for i in range(p):
        t=((2*(a*LA[i]+2*b*LB[i]))%mod).astype(np.float64)/mod
        s+=lg[(np.floor(t*GR).astype(np.int64))%GR]
    return s
def mean_exp(s): m=s.max(); return float(np.log(np.mean(np.exp(s-m)))+m)
res=dict(p=p,h=h,factors=[int(q) for q in fac],NS=NS)
a=rng.integers(0,h,NS); b=rng.integers(0,h,NS); res['logE_G']=mean_exp(logF(a,b,h))
M=1000003; a=rng.integers(0,h*M,NS); b=rng.integers(0,h*M,NS); res['logInt']=mean_exp(logF(a,b,h*M))
for d in fac:
    if len(fac)==1: break
    hd=h//d; got_a=[];got_b=[];n=0
    while n<NS:
        a=rng.integers(0,h,2_000_000).astype(np.int64); b=rng.integers(0,h,2_000_000).astype(np.int64)
        N=(a*a-2*b*b)%h; ok=(N%d==0)&(N%hd!=0) if all(hd%q for q in [d]) else (N%d==0)
        got_a.append(a[ok]); got_b.append(b[ok]); n+=int(ok.sum())
        if d>5000 and n<NS and len(got_a)>40: break
    a=np.concatenate(got_a)[:NS]; b=np.concatenate(got_b)[:NS]
    res[f'logE_H{d}']=mean_exp(logF(a,b,h)); res[f'n_H{d}']=int(len(a))
    res[f'c_maj_{d}']=(res[f'logE_H{d}']-res['logE_G'])/math.log(d)
print(json.dumps(res)); json.dump(res,open(f'logs/a_majorant_p{p}.json','w'),indent=1)
