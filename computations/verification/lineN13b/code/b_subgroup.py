"""N13b R2 [N]: unbiased random-sample averages of |r(beta)| = |Zhat(beta)/Z(0)| at level h_p over
  G   = all beta mod h (beta != 0),
  H_d = {beta : N beta = 0 mod d, N beta unit mod h/d}  (mixed: iso part d, unit part h/d), for each prime d | h,
plus E_U = unit-at-every-prime.  Twist law tau_i = Tr(lam^i beta)/h (N11b a_unit_types).  Reports c_est = log(E_H/E_G)/log d,
the needed c* = 0.387, and the implied Y_mixed bound  2^w (2d/h) |H_d| E_H.   usage: b_subgroup.py p NS"""
import sys, json, math, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import *
from sympy import factorint
p=int(sys.argv[1]); NSMP=int(sys.argv[2]); m=3*p
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
h=xy(p)[0]; fac=list(factorint(h).keys())
hh,nu=nu_rho(m,1); tw=TW(m,nu,L=8,K=16); Z0=Zbatch(tw,[[0.0]*m])[0]
L=[(1,0)]
for i in range(m-1):
    a,b=L[-1]; L.append(((3*a+4*b)%h,(2*a+3*b)%h))
LA=np.array([l[0] for l in L],dtype=object); LB=np.array([l[1] for l in L],dtype=object)
def taus(a,b): return [float((2*((a*int(LA[i])+2*b*int(LB[i]))%h))%h)/h for i in range(m)]
rng=np.random.default_rng(p)
def sample(cond,n):
    out=[]
    while len(out)<n:
        a=int(rng.integers(0,h)); b=int(rng.integers(0,h))
        if (a,b)==(0,0): continue
        N=(a*a-2*b*b)%h
        if cond(N): out.append((a,b))
    return out
def avg(bl):
    T=[taus(a,b) for a,b in bl]; Z=[]
    for i in range(0,len(T),32): Z+=list(Zbatch(tw,T[i:i+32]))
    r=np.abs(np.array(Z)/Z0); return float(r.mean()),float(r.max()),float(np.quantile(r,0.99))
res=dict(p=p,h=h,factors=fac,NS=NSMP,sets={}); t0=time.time()
res['sets']['G']=avg(sample(lambda N: True,NSMP)); print('G',res['sets']['G'],round(time.time()-t0),flush=True)
for d in fac:
    if len(fac)==1: break
    hd=h//d
    def cond(N,d=d,hd=hd): return N%d==0 and math.gcd(N,hd)==1
    # acceptance ~ 2/d: sample via ideal structure if d large: beta = x*pi with N(pi)=+-d ... keep rejection, cap work
    if d>20000:
        res['sets'][f'H_{d}']='skipped (rejection rate)'; continue
    res['sets'][f'H_{d}']=avg(sample(cond,NSMP)); print(d,res['sets'][f'H_{d}'],round(time.time()-t0),flush=True)
EG=res['sets']['G'][0]; lam=3+2*math.sqrt(2); rate=(1.2744/1.9154732)**(3*p)
for k,v in res['sets'].items():
    if k.startswith('H_') and not isinstance(v,str):
        d=int(k[2:]); EH=v[0]
        res[f'c_est_{d}']=math.log(EH/EG)/math.log(d)
        res[f'Ymixed_bound_{d}']=2*(2*d/h)*(2*h*h/d)*EH   # weight<=2*2d/h (|kappa|<=2 n_d), |H_d|~2h^2/d... upper estimate
res['Cprime_rate_3p']=rate; res['EG_over_Cprime']=EG/rate
print(json.dumps(res)); json.dump(res,open(f'logs/b_subgroup_p{p}.json','w'),indent=1)
