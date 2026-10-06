"""Exact rational certificate; no floating-point numbers enter assertions."""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

def main():
    from fractions import Fraction as F
    from math import factorial
    import sys,json
    from pathlib import Path
    from functools import lru_cache
    sys.path.insert(0,str(Path(__file__).resolve().parent))
    from frozen_full_lag_gap import plus,scale,product,cosine,sine,ONE

    def add(x,y):return x[0]+y[0],x[1]+y[1]
    def mul(x,y):
     v=[a*b for a in x for b in y];return min(v),max(v)
    def sc(x,a):return mul(x,(a,a))
    def atan_inv(n):
     s=sum((F((-1)**j,(2*j+1)*n**(2*j+1)) for j in range(90)),F(0))
     return s,s+F(1,181*n**181)
    pi=add(sc(atan_inv(5),16),sc(atan_inv(239),-4))
    assert F(314159265358979323846,10**20)<pi[0]<pi[1]<F(314159265358979323847,10**20)
    pi=(F(314159265358979323846,10**20),F(314159265358979323847,10**20))
    @lru_cache(None)
    def trig(frac,sin=False):
     frac=frac-F((frac+F(1,2)).numerator//(frac+F(1,2)).denominator)
     x=sc(pi,2*frac); xx=mul(x,x); out=(F(0),F(0))
     for j in reversed(range(21)):
      out=add(mul(out,xx),(F((-1)**j,factorial(2*j+int(sin))),)*2)
     if sin:out=mul(out,x)
     # Taylor's theorem at degree 40/41, |x|<4, all derivatives <=1.
     err=F(4**41,factorial(41)) if not sin else F(4**42,factorial(42))
     return out[0]-err,out[1]+err
    u={(0,0):ONE}; r=product(plus(u,scale(cosine(7),(F(-1),F(0)))),plus(u,cosine(1)))
    rs={k:tuple((1 if k[0]%2==0 else -1)*v for v in a) for k,a in r.items()}
    pc={(0,1):(F(-3,10),F(-2,5)),(0,-1):(F(-3,10),F(2,5))}
    g=plus(cosine(7),scale(r,(F(1,10),F(0))),scale(product(r,sine(1)),(F(1,100),F(0))),scale(product(rs,pc),(F(1,100),F(0))),{(0,0):(F(-1,10),F(0))})
    def coeff(orbit):
     out=(F(0),F(0))
     for a,b in orbit:
      for (k,l),(re,im) in g.items():
       z=add(sc(trig(F(k*a+l*b,7)),re),sc(trig(F(k*a+l*b,7),True),-im))
       out=add(out,sc(z,4*(140*k*k-70*l*l)))
     return out
    O=[(1,2),(4,1),(2,4)]
    Cs={name:coeff([(sq*a,sp*b) for a,b in O]) for name,sq,sp in [('I',1,1),('-I',-1,-1),('R0',1,-1),('-R0',-1,1)]}
    # Human-readable decimal enclosures derived by outward integer rounding.
    def dec(x):
     d=10**9
     return [str(F(x[0].numerator*d//x[0].denominator,d)),str(F(-((-x[1].numerator*d)//x[1].denominator),d))]
    res={}
    for n in ['-I','R0','-R0']:
     diff=add(Cs['I'],sc(Cs[n],-1)); assert diff[0]>500 or diff[1]<-500
     res[n]={'signed_difference_over_pi_squared':dec(diff)}
    t=F(1,10**12); e=1800000000; L=3000
    remainder=4*7**3*(3*e+3*(L+e*t)**2+(L+e*t)**3*t)
    assert remainder<8*10**12
    print(json.dumps({'arithmetic':'exact rational interval Taylor bounds; Machin formula for pi','coefficients_over_pi_squared':{k:dec(v) for k,v in Cs.items()},'differences':res,'pair_remainder_constant_upper':str(remainder),'nonclaim':'This certificate checks finite coefficients and constants; the maintained proof supplies all-kappa and centralizer implications.'},indent=2))
    # Exact Fourier checks at the four fixed points, independent of trig intervals.
    for (a,b),expected in zip([(0,0),(0,1),(1,0),(1,1)],[-19606,-19594,24306,24894]):
     grad=[(F(0),F(0)),(F(0),F(0))]; hess=[[F(0),F(0)],[F(0),F(0)]]
     for (k,l),(re,im) in g.items():
      sign=1 if (k*a+l*b)%2==0 else -1
      for j,v in enumerate([k,l]):
       grad[j]=(grad[j][0]-sign*im*v,grad[j][1]+sign*re*v)
       for m,w in enumerate([k,l]):hess[j][m] += -4*sign*re*v*w
     assert grad==[(0,0),(0,0)]
     assert hess==[[F(expected,125),0],[0,0]]
    assert sum((abs(re)+abs(im))*(k*k+l*l) for (k,l),(re,im) in g.items())==F(51451,1000)

if __name__ == "__main__":
    main()
