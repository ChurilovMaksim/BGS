"""Theorem D (odd m): 2m - B_m^sym = h_m^{-2} * sum_{d|m} [ 2(m-d) a(d) + d^2 b(d) ],
a(d)=sum_{e|d} mu(d/e) h_e^2, b(d)=sum_{e|d} mu(d/e) h_e, h_d = Q_d/2 (NSW numbers; D_d = 4 h_d^2).
(1) exact check against direct orbit counting on the support (m<=9, from Orbits);  (2) table for odd m<=41 (exact rationals)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from p2lib import *
from fractions import Fraction as Fr
def hQ(d):
    Q=[2,2]
    for _ in range(d): Q.append(2*Q[-1]+Q[-2])
    return Q[d]//2
def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def formula(m):
    a=lambda d: sum(mobius(d//e)*hQ(e)**2 for e in divisors(d))
    b=lambda d: sum(mobius(d//e)*hQ(e) for e in divisors(d))
    num=sum(2*(m-d)*a(d)+d*d*b(d) for d in divisors(m)); return num, hQ(m)**2
print('== direct counting on the support vs closed form (odd m) ==')
for m in [1,3,5,7,9]:
    O,supp=support_data(m); d1,d2=O.d1,O.d2
    X1=O.T[0]; X2=O.T[1] if m>1 else O.T[0]
    a,b=X1.copy(),X2.copy(); ra,rb=X1.copy(),(6*X1-X2)%d2; stab=np.zeros(X1.shape,np.int64)
    for j in range(m):
        stab+=((a==X1)&(b==X2)); stab+=((ra==X1)&(rb==X2)); a,b=b,(6*b-a)%d2; ra,rb=rb,(6*rb-ra)%d2
    orb=2*m//stab
    direct=int((2*m-orb[supp]).sum()); Deff=int(supp.sum())
    num,den=formula(m)
    # structure checks: support = s + odd part, s a fixed point of S (constant q-sequence, 4*theta=0)
    consts=[(int(O.T[0].ravel()[i]),) for i in np.flatnonzero(supp) if all(O.T[j].ravel()[i]==O.T[0].ravel()[i] for j in range(m))]
    print(f'm={m} D_eff={Deff} h_m^2={den} direct sum(2m-|Gamma xi|)={direct} closed form={num} match={direct==num and Deff==den} '
          f'deficit={direct/Deff:.6f}  #S-fixed points in support={len(consts)}',flush=True)
print('== exact deficit 2m - B_sym for odd m (closed form) and leading term m^2/h_m ==')
for m in range(1,42,2):
    num,den=formula(m); h=hQ(m)
    print(f'm={m:2d} h_m={h} deficit={num/den:.6e} m^2/h_m={m*m/h:.6e} ratio={num/den/(m*m/h):.6f} B_sym/2m={1-num/den/(2*m):.12f}')
