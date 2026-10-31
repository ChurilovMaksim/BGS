"""N15b [N]: worst-case normalized orbit sums  max_{a != 0 mod q} |sum_{i<ord} e(a L^i / q)| / ord,  L = root of x^2-6x+1 mod q
(the image of lam in F_q, q prime factor of h_p), and the size ratio ord/log q.  BGK/Bourgain need ord >= q^delta /
log ord > C log q/loglog q; MVW conjecture needs ord/log q -> infinity.  Shows sums are NOT o(ord) at this scale."""
import json, math, numpy as np
from sympy import factorint, sqrt_mod, n_order
out=[]
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x,y
for p in [11,13,17,19,23,29,31]:
    h=xy(p)[0]
    for q in sorted(factorint(h)):
        if q>3_000_000: continue
        r=sqrt_mod(2,q); L=(3+2*r)%q; o=n_order(L,q)
        pw=np.array([pow(L,i,q) for i in range(o)],dtype=np.int64)
        best=0.0; besta=None
        for a0 in range(1,q,max(1,q//2_000_000+1)) if q<2_000_000 else []:
            pass
        A=np.arange(1,q,dtype=np.int64)
        S=np.zeros(q-1,dtype=complex)
        for v in pw: S+=np.exp(2j*np.pi*((A*v)%q)/q)
        m=np.abs(S)/o; k=int(m.argmax())
        out.append(dict(p=p,q=int(q),ord=int(o),ord_over_logq=o/math.log(q),log_ord_over_logq=math.log(o)/math.log(q),
                        max_norm_sum=float(m[k]),argmax_a=int(k+1),median_norm_sum=float(np.median(m))))
        print(out[-1],flush=True)
json.dump(out,open('logs/c_orbitsums.json','w'),indent=1)
