"""N5 (A) [N]: model check.  For an isotropic point beta=(bx,by) at level q (y=(bx+by sqrt2)/q), twists tau_i = Tr(lam^i y) mod 1 (exact rationals),
Zmodel = Tr prod_{i<m} L^V_{tau_i} - Tr prod L^E_{tau_i}  (Line F lift, eta=2, sector a=0 weights times e(n tau_i)).  Compare with N2 TRACE-206 |Zhat|."""
import sys, numpy as np, math
sys.path.insert(0,'/workspace/bgs-lineF/code')
from lift import ops, wk1
def twists(bx,by,q,m):
    # lam^i (bx + by sqrt2) = A + B sqrt2 ; Tr = 2A ; tau = 2A/q mod 1
    A,B=bx,by; out=[]
    for i in range(m):
        out.append(((2*A)%q)/q); A,B=(3*A+4*B)%q,(2*A+3*B)%q
    return out
def zmodel(tw,K0=4,r=1.2,rE=0.8,K=30,N0=60):
    w0=wk1(2,0); cache={}; PV=None; PE=None
    for t in tw:
        if t not in cache:
            cache[t]=ops(lambda n,t=t: w0(n)*np.exp(2j*np.pi*n*t),N0,K0,r,rE,K,beta=0.0)
        V,E=cache[t]
        PV=V if PV is None else V@PV; PE=E if PE is None else E@PE
    return np.trace(PV)-np.trace(PE)
if __name__=='__main__':
    m,q=int(sys.argv[1]),int(sys.argv[2]); pts=[tuple(map(int,s.split(','))) for s in sys.argv[3:]]
    Zh=np.load(f'/workspace/bgs-lineN/N2/logs/d_Zh_m{m}_q{q}_s1.npy')
    for (bx,by) in pts:
        z=zmodel(twists(bx,by,q,m)); print((bx,by),'model',abs(z),'TRACE206',abs(Zh[bx,by]),flush=True)
