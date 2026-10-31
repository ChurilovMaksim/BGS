"""N9: near-collision transfer matrices (referee route for A-infinity, 'r2(eta)').
Letters v (pair differences) with weight g(v) = rho(v) = sum_a u(a)u(a-v), u(a)=|J_a(1.8)| e^{tau|a|} (Line L O1 weights, 8V tau_mid),
|v|<=V, tail mass folded into g(0) (Prop E device; nonneg coefficients).
Horner state S in Z[sqrt2]:  S -> beta*S + v.  1-D near-collision (one embedding small at the end, tolerance eta) forces every
intermediate state into the finite box |S| <= B1 = (V+eta)/(beta-1), |S'| <= B2 = V/(1-1/|beta'|) (backward/forward recursion).
 beta = lam : a single core (letters at lam-spacing)            -> rate per letter  (referee's r2(eta))
 beta = eps : A- and B-cores of the SAME class interleaved (zeta_B = -eps^{-1} zeta_A, Lemma P') -> rate per letter
Spectral radius by power iteration [N]; Collatz-Wielandt upper bound with float x>0, nonnegative matrix, weights rounded up in arb,
relative float error margin 1e-10 [CA*].  usage: b_automaton.py beta(lam|eps) V eta"""
import sys, json, math, numpy as np
from flint import arb, ctx
ctx.prec=128
base=sys.argv[1]; V=int(sys.argv[2]); eta=float(sys.argv[3]) if len(sys.argv)>3 else 1.0
LAM=3+2*arb(2).sqrt(); C0=1/(LAM-1/LAM); rho_=arb('0.75'); beta_=arb('0.25'); J1=14; X=arb('1.8'); AM=60
tau=2*arb.pi()*C0*rho_*LAM**(-J1)+beta_*LAM**(-(J1+1))
J=[abs(X.bessel_j(a)) for a in range(AM+1)]
et=tau.exp(); u=[J[abs(a)]*et**abs(a) for a in range(-AM,AM+1)]
tail=4*((X*et/2)**(AM+1))/arb(math.factorial(AM+1)); Usum=sum(u,arb(0))+tail
g={}
for d in range(-V,V+1):
    s=arb(0)
    for a in range(-AM,AM+1):
        b=a-d
        if -AM<=b<=AM: s+=u[a+AM]*u[b+AM]
    g[d]=s+2*tail*Usum
h=V//2+1; tailV=sum((u[a+AM] for a in range(-AM,AM+1) if abs(a)>=h),arb(0))+tail
g[0]+=2*tailV*Usum
gf={d:float(g[d].upper()) for d in g}
A2=float((Usum**2).upper())
S2=math.sqrt(2)
if base=='lam': bu,bv=3,2; bnum=3+2*S2; bconj=3-2*S2
else: bu,bv=1,1; bnum=1+S2; bconj=1-S2
B1=(V+eta)/(bnum-1)+1e-9; B2=V/(1-abs(bconj))+1e-9
st=[]
R=int(B1+B2)+3
for a in range(-4*R,4*R+1):
    for b in range(-3*R,3*R+1):
        if abs(a+b*S2)<=B1 and abs(a-b*S2)<=B2: st.append((a,b))
idx={s:i for i,s in enumerate(st)}; n=len(st)
rows=[];cols=[];vals=[]
for (a,b) in st:
    na=bu*a+2*bv*b; nb=bv*a+bu*b       # beta*S
    for v,w in gf.items():
        t=(na+v,nb)
        if t in idx: rows.append(idx[t]); cols.append(idx[(a,b)]); vals.append(w)
import scipy.sparse as sp
F=sp.csr_matrix((vals,(rows,cols)),shape=(n,n))
x=np.ones(n)
for it in range(3000):
    y=F@x; lamb=y.max()/x.max(); x=y/y.max()
x=np.maximum(x,1e-300)
y=F@x; ratio=np.max(y/x)*(1+1e-10)
res=dict(base=base,V=V,eta=eta,states=n,nnz=int(F.nnz),power_iter=float(lamb),CW_upper=float(ratio),
         free_mass_A2=A2,minx=float(x.min()),tau_mid=float(tau.upper()))
print(json.dumps(res)); open('/workspace/audit/lineN10/logs/rerun_b_automaton.jsonl','a').write(json.dumps(res)+'\n')
