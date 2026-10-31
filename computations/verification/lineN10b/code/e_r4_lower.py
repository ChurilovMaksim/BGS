"""N10b [CA]: arb Collatz-Wielandt LOWER bound for the 4-fold collision automaton letter matrix at tau=0 (and the 2-fold one, sanity).
Letter weights: rho(d) = sum_a |J_a(1.8)||J_{a-d}(1.8)| (|a|<=AM: truncation only lowers -> valid lower bound), rho2 = rho*rho.
Carry automaton (a,b)->(b,e), letter d = e - 6b + a, carries |.|<=E (restricting states only lowers the spectral radius of a
nonnegative matrix: principal submatrix).  rho(M) >= min_i (Mx)_i/x_i for any x>0."""
import numpy as np, flint, json
from flint import arb
flint.ctx.prec=128
AM=40; E=6
J=[abs(arb('1.8').bessel_j(a)) for a in range(AM+1)]
Jf=lambda a: J[abs(a)] if abs(a)<=AM else arb(0)
rho={d:sum((Jf(a)*Jf(a-d) for a in range(-AM,AM+1) if abs(a-d)<=AM),arb(0)) for d in range(-2*AM,2*AM+1)}
rho2={}
for d in range(-60,61):
    s=arb(0)
    for x in range(-60,61):
        if x in rho and (d-x) in rho: s+=rho[x]*rho[d-x]
    rho2[d]=s
def build(R):
    es=range(-E,E+1); st=[(a,b) for a in es for b in es]; idx={s:i for i,s in enumerate(st)}; n=len(st)
    M=[[arb(0)]*n for _ in range(n)]
    for (a,b) in st:
        for e in es:
            d=e-6*b+a
            if d in R: M[idx[(a,b)]][idx[(b,e)]]=M[idx[(a,b)]][idx[(b,e)]]+R[d]
    return M
out={}
for name,R in (('s2',rho),('s4',rho2)):
    M=build(R); n=len(M)
    Mf=np.array([[float(M[i][j].mid()) for j in range(n)] for i in range(n)])
    keep=list(range(n))
    for it in range(6):   # shrink to a principal submatrix (lowers rho, still valid) where the CW ratio is uniform
        Ms=Mf[np.ix_(keep,keep)]; w,V=np.linalg.eig(Ms); k=int(np.argmax(w.real)); x=np.abs(V[:,k].real); x/=x.max()
        r=(Ms@x)/np.maximum(x,1e-300); bad=[keep[i] for i in range(len(keep)) if x[i]<1e-6 or r[i]<0.999*w.real[k]]
        if not bad: break
        keep=[i for i in keep if i not in bad]
    xa={keep[i]:arb(float(x[i])) for i in range(len(keep))}
    lb=None
    for i in keep:
        s=sum((M[i][j]*xa[j] for j in keep if Mf[i,j]!=0),arb(0))/xa[i]
        lb=s if lb is None else (s if s.lower()<lb.lower() else lb)
    out[name]=dict(states=len(keep),float_rho=float(w.real[k]),CW_lower=str(lb),CW_lower_float=float(lb.lower()))
    print(name,out[name],flush=True)
json.dump(out,open('logs/e_r4_lower.json','w'),indent=1)
