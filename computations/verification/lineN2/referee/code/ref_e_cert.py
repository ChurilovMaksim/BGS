"""Referee: independent certificate for N2 Prop E (r_2(k) upper bounds).
Independent choices vs author: LEFT Collatz-Wielandt vector, AM=50 with own Bessel tail, J1=20 exact boundary letters,
weights/C_pair rebuilt from the TRACE-249/250 statements. usage: FAM k V J1"""
import sys, math, json, time, numpy as np
from flint import arb, arb_mat, ctx
ctx.prec=160
fam=sys.argv[1]; k=int(sys.argv[2]); V=int(sys.argv[3]); J1=int(sys.argv[4]); E0=int(sys.argv[5]) if len(sys.argv)>5 else V//4
NS,rho,beta,typ,kdiv={'8V':(1,'0.75','0.25','V',1),'8E':(1,'0.2','0.3','E',1),'16V':(64,'0.9','0.3','V',2),'16E':(64,'0.2','0.3','E',2)}[fam]
rho=arb(rho); beta=arb(beta); L=3+2*arb(2).sqrt(); kap=1/(L-1/L)/kdiv; X=arb('1.8'); AM=50
Jv=[X.bessel_j(a).__abs__() for a in range(AM+1)]
def wts(tau):
    y=X*tau.exp()/2
    tail=2*y**(AM+1)/arb(math.factorial(AM+1))/(1-y/(AM+2))     # sum_{|a|>AM} u(a)
    u={a:Jv[abs(a)]*(tau*abs(a)).exp() for a in range(-AM,AM+1)}
    U=sum(u.values(),arb(0))+tail
    tV=sum((u[a] for a in u if 2*abs(a)>V),arb(0))+tail
    g={}
    for d in range(-V,V+1):
        g[d]=sum((u[a]*u[a-d] for a in u if (a-d) in u),arb(0))+2*tail*U
    g[0]+=2*tV*U
    return g
es=range(-E0,E0+1); st=[(p,q) for p in es for q in es]; ix={s:i for i,s in enumerate(st)}; n=len(st)
def mats(g):
    A=np.zeros((n,n)); R=[[arb(0)]*n for _ in range(n)]
    for (p,q) in st:
        for e in es:
            d=e-6*q+p
            if d in g: A[ix[(p,q)],ix[(q,e)]]=float(g[d].mid()); R[ix[(p,q)]][ix[(q,e)]]=g[d]
    return A, arb_mat(R)
tauj=lambda j: 2*arb.pi()*kap*rho*L**(-j)+beta*L**(-(k-j))
tmid=2*arb.pi()*kap*rho*L**(-J1)+beta*L**(-(J1+1))
plan=[]; cache={}
for j in range(k):
    key='mid' if J1<=j<k-J1 else j
    if key not in cache: cache[key]=mats(wts(arb((tauj(j) if key!='mid' else tmid).upper())))
    plan.append(key)
Zf,Za=mats({0:arb(1)})
dev=L/(2*(L-1)) if typ=='V' else 1/(2*(L-1))
th=(rho*L**(-k)+dev)/rho; b=beta*(1-L**(-k))
C=NS*(b.exp()+(-b).exp())/(b.exp()-(-b).exp())*(2*beta*(dev+1)).exp()/(1-th**2)
Cf=float(C.mid()); t0=time.time()
def leftB(w):   # w^T B
    y=w.copy()
    for j in range(k): y=y@cache[plan[j]][0]
    z=w.copy()
    for j in range(k): z=z@Zf
    return Cf*y+z
w=np.ones(n)
for it in range(80):
    w2=leftB(w); w=w2/w2.max()
w=np.maximum(w,1e-250)
wa=arb_mat([[arb(float(v)) for v in w]])
y=wa
for j in range(k): y=y*cache[plan[j]][1]
z=wa
for j in range(k): z=z*Za
y=C*y+z
Rub=max((y[0,i]/wa[0,i]).upper() for i in range(n))
r2=(arb(Rub).log()/k).exp()
out=dict(fam=fam,k=k,V=V,J1=J1,E0=E0,states=n,Cpair=float(C.mid()),R_upper=float(Rub),r2_upper=float(r2.upper()),sec=round(time.time()-t0,1))
print(json.dumps(out),flush=True)
