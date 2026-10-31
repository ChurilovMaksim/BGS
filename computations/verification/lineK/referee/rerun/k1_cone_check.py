"""K1 [P-check of the algebra]: for q prime, q=+-1 mod 8 (2 a square), arbitrary complex mass A on O/q = (Z/q)^2 (x = x1 + x2 sqrt2),
 Zhat(beta) = sum_x A(x) e(Tr(beta x)/q),  W_beta = q^-2 sum_{t in F_q^*, t != t_b} e(N(beta) t^-1 / q),
identity:  sum_{beta != 0} Zhat(beta) W_beta = D_iso - E_b/q,
 D_iso = A(N(x)=0) - (2q-1)/q^2 * A_tot,  E_b = sum_x A(x) e(-N(x) t_b/q) - A_tot/q.   Exact check in Q(zeta_q) via high-precision floats + random A."""
import numpy as np, json
from mpmath import mp, mpc, exp, pi
mp.dps=40
rng=np.random.default_rng(5); out=[]
for q in (7,17,23,31):
    e=lambda k: exp(2j*pi*mpc(k%q)/q)
    A={(a,b):mpc(*rng.normal(size=2)) for a in range(q) for b in range(q)}
    N=lambda a,b:(a*a-2*b*b)%q
    inv={t:pow(t,-1,q) for t in range(1,q)}
    for tb in (1,3):
        lhs=0
        Zh={}
        for b1 in range(q):
            for b2 in range(q):
                if b1==0 and b2==0: continue
                Z=sum(A[x]*e(2*(b1*x[0]+2*b2*x[1])) for x in A)
                W=sum(e(N(b1,b2)*inv[t]) for t in range(1,q) if t!=tb)/q**2
                lhs+=Z*W
        Atot=sum(A.values()); cone=sum(A[x] for x in A if N(*x)==0)
        Diso=cone-mpc(2*q-1)/q**2*Atot; Eb=sum(A[x]*e(-N(*x)*tb) for x in A)-Atot/q
        rhs=Diso-Eb/q; d=abs(lhs-rhs); out.append((q,tb,float(d))); print(q,tb,'|lhs-rhs|=',float(d),flush=True)
ok=all(d<1e-25 for _,_,d in out); print('K1 IDENTITY', 'VERIFIED' if ok else 'FAILED')
json.dump(dict(cases=out,ok=ok),open('logs/k1_cone_check.json','w'))
