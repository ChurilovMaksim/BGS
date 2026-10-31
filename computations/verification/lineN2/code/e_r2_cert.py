"""N2 (E) [CA]: rigorous upper bound for the block exact-collision rate r_2(k) (Theorem C input), via
 (1) Fourier majorant  rho_hat_i(t) = |u_hat_i(t)|^2 <= g_i(t) := sum_{|d|<=V} rho_i(d) e(dt) + eps_i,
     eps_i >= sum_{|d|>V} rho_i(d)   (pointwise, since |sum_{|d|>V} rho_i(d)e(dt)| <= eps_i);
 (2) exact collisions with all letters |v|<=V have all carries |e_j| <= floor(V/4)
     (Green kernel e = G*v, G(n)=lam^{-|n|}/(lam-1/lam), sum_n G(n) = 1/4 exactly), so the finite box automaton
     with E0=floor(V/4) is EXACT for the majorant -- no tail;
 (3) Collatz-Wielandt on the finite nonnegative block matrix B = a*Z^k + C_pair * M_0 M_1 ... M_{k-1}:
     B x <= R x (x>0)  =>  <0|B^Q|0> <= R^Q ;  r_2(k) <= R^{1/k}.
 Weights rho_i(d) = sum_a u_i(a) u_i(a-d), u_i(a) = |J_a(1.8)| e^{tau_i |a|}; tau-profile, C_pair: Line L Lemma O1
 (as in b_r2_float.py).  Monotonicity of rho in tau lets middle letters use one upper tau_mid.
 usage: e_r2_cert.py FAM k V J1 [a]"""
import sys, math, json, time, numpy as np
from flint import arb, arb_mat, ctx
ctx.prec=128
fam=sys.argv[1]; k=int(sys.argv[2]); V=int(sys.argv[3]); J1=int(sys.argv[4]); aclamp=arb(sys.argv[5] if len(sys.argv)>5 else 1)
FAM={'8V':(1,'0.75','0.25','V',1),'8E':(1,'0.2','0.3','E',1),'16V':(64,'0.9','0.3','V',2),'16E':(64,'0.2','0.3','E',2)}
NS,rho_s,beta_s,typ,cdiv=FAM[fam]
LAM=3+2*arb(2).sqrt(); C0=1/(LAM-1/LAM)/cdiv; rho=arb(rho_s); beta=arb(beta_s); X=arb('1.8'); AM=60
E0=V//4; es=list(range(-E0,E0+1)); st=[(p,q) for p in es for q in es]; idx={s:i for i,s in enumerate(st)}; n=len(st)
J=[abs(X.bessel_j(a)) for a in range(AM+1)]
def fact(m): return arb(math.factorial(m))
def weights(tau):
    et=tau.exp(); u=[J[abs(a)]*(et**abs(a)) for a in range(-AM,AM+1)]   # index a+AM
    # tail sum_{|a|>AM} u(a) <= 2 * 2*(X e^tau/2)^{AM+1}/(AM+1)!   (ratio of successive terms < 1/2)
    tail=4*((X*et/2)**(AM+1))/fact(AM+1)
    Usum=sum(u,arb(0))+tail
    h=V//2+1; tailV=sum((u[a+AM] for a in range(-AM,AM+1) if abs(a)>=h),arb(0))+tail
    eps=2*tailV*Usum
    g={}
    for d in range(-V,V+1):
        s=arb(0)
        for a in range(-AM,AM+1):
            b=a-d
            if -AM<=b<=AM: s+=u[a+AM]*u[b+AM]
        g[d]=s+2*tail*Usum
    g[0]=g[0]+eps
    return {d:arb(g[d].upper()) for d in g}, float(eps.upper())
def taus():
    out=[]
    for j in range(k): out.append(2*arb.pi()*C0*rho*LAM**(-j)+beta*LAM**(-(k-j)))
    return out
T=taus(); tmid=2*arb.pi()*C0*rho*LAM**(-J1)+beta*LAM**(-(J1+1))
plan=[]  # list of (key) per position
keys={}
for j in range(k):
    if J1<=j<k-J1: key='mid'; tau=tmid
    else: key=j; tau=T[j]
    if key not in keys: keys[key]=weights(arb(tau.upper()))
    plan.append(key)
def fmat(g):
    M=np.zeros((n,n))
    for (p,q) in st:
        for e in es:
            d=e-6*q+p
            if d in g: M[idx[(p,q)],idx[(q,e)]]+=float(g[d].mid())   # transition weight, NB g is upper already
    return M
def amat(g):
    rows=[[0]*n for _ in range(n)]
    for (p,q) in st:
        for e in es:
            d=e-6*q+p
            if d in g: rows[idx[(p,q)]][idx[(q,e)]]=g[d]
    return arb_mat(rows)
Fm={key:fmat(keys[key][0]) for key in keys}; Z=fmat({0:arb(1)})
# C_pair (Line L O1)
dev=LAM/(2*(LAM-1)) if typ=='V' else 1/(2*(LAM-1))
theta=(rho*LAM**(-k)+dev)/rho
bb=beta*(1-LAM**(-k)); tanh=(bb.exp()-(-bb).exp())/(bb.exp()+(-bb).exp())
Cpair=arb((NS/tanh*(2*beta*(dev+1)).exp()/(1-theta**2)).upper())
a_f=float(aclamp.mid()); Cf=float(Cpair.mid())
def Bf(x):
    y=x.copy()
    for j in reversed(range(k)): y=Fm[plan[j]]@y
    z=x.copy()
    for j in range(k): z=Z@z
    return Cf*y+a_f*z
x=np.ones(n); lam_est=None
t0=time.time()
for it in range(60):
    y=Bf(x); lam_est=y.max()/x.max(); x=y/y.max()
x=np.maximum(x,1e-200)
ratio_f=float(np.max(Bf(x)/x))
# rigorous
Am={key:amat(keys[key][0]) for key in keys}; Za=amat({0:arb(1)})
xa=arb_mat([[arb(float(v))] for v in x])
y=xa
for j in reversed(range(k)): y=Am[plan[j]]*y
z=xa
for j in range(k): z=Za*z
y=Cpair*y+aclamp*z
R=max(float((y[i,0]/xa[i,0]).upper()) for i in range(n))
Rarb=arb(R)*(1+arb(2)**-40)   # absorb float rounding of the upper endpoint
r2=float((Rarb.log()/k).exp().upper())*(1+2.0**-40)
res=dict(fam=fam,k=k,V=V,E0=E0,J1=J1,a=a_f,states=n,Cpair=float(Cpair.mid()),eps_max=max(v[1] for v in keys.values()),
         float_rate=ratio_f**(1/k),R_upper=R,r2_upper=r2,minx=float(x.min()),sec=round(time.time()-t0,1))
print(json.dumps(res),flush=True)
with open('logs/e_r2_cert.jsonl','a') as f: f.write(json.dumps(res)+'\n')
