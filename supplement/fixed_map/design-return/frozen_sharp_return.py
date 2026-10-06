"""Rational certificates for the prescribed finite Fourier kick.

Position convention is explicit: exp(2*pi*i*(k*q+l*p)) maps to T(l,k).
Raw modular coefficients are used. The squared average is also computed
after multiplying by (-1)**(k*l); the finite certificate checks equality.
This does not assert that the spectra of the two quantizations agree.

All certificate inequalities use integers/Fraction, including bounds on
square roots and sines. Decimal conversion is only for display.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
from fractions import Fraction as F
from math import isqrt, lcm
from decimal import Decimal, localcontext
from collections import defaultdict
import json
from sparse_orbit_checks import pell, power, act


def coefficients():
    c=defaultdict(lambda:[F(0),F(0)])
    r={0:F(1),1:F(1,2),-1:F(1,2),7:F(-1,2),-7:F(-1,2),
       6:F(-1,4),-6:F(-1,4),8:F(-1,4),-8:F(-1,4)}
    c[(7,0)][0]+=F(1,2);c[(-7,0)][0]+=F(1,2)
    for k,z in r.items():
        c[(k,0)][0]+=z/10
        c[(k+1,0)][1]-=z/200
        c[(k-1,0)][1]+=z/200
        c[(k,1)][0]-=3*z/1000;c[(k,1)][1]-=4*z/1000
        c[(k,-1)][0]-=3*z/1000;c[(k,-1)][1]+=4*z/1000
    assert c.pop((0,0))==[F(1,10),F(0)]
    c={v:z for v,z in c.items() if any(z)}
    den=lcm(*(t.denominator for z in c.values() for t in z))
    out={(l,k):tuple(int(t*den) for t in z) for (k,l),z in c.items()}
    assert max(abs(a)+abs(b) for a,b in out)==9
    for (a,b),(re,im) in out.items():assert out[(-a,-b)]==(re,-im)
    return den,out


def sqrt_bounds(x,scale=10**18):
    assert x>=0
    lo=isqrt(x.numerator*scale*scale//x.denominator)
    assert F(lo,scale)**2<=x<F(lo+1,scale)**2
    return F(lo,scale),F(lo+1,scale)


def dec(x):
    with localcontext() as ctx:
        ctx.prec=40
        return str(Decimal(x.numerator)/Decimal(x.denominator))


def certificate(k):
    assert k>=39 and k%2==1
    n,_=pell(k);den,coeff=coefficients()
    scale=10**12
    upper={v:isqrt((a*a+b*b)*scale*scale//(den*den))+1
           for v,(a,b) in coeff.items()}
    for v,(a,b) in coeff.items():
        assert F(upper[v],scale)**2>=F(a*a+b*b,den*den)

    collected=defaultdict(lambda:[0,0])
    gauge_collected=defaultdict(lambda:[0,0])
    c0num=0;c1num=0
    for d in range(k):
        sd=power(d,n)
        sw={v:act(sd,v,n) for v in coeff}
        for v,(a,b) in coeff.items():
            collected[sw[v]][0]+=a;collected[sw[v]][1]+=b
            sign=-1 if (v[0]*v[1])%2 else 1
            gauge_collected[sw[v]][0]+=sign*a
            gauge_collected[sw[v]][1]+=sign*b
        for v,uv in upper.items():
            for w,uw in upper.items():
                a,b=sw[w]
                det=(v[0]*b-v[1]*a)%n
                distance=min(det,n-det)
                gnum=min(14*n,44*distance)
                z=uv*uw*gnum
                c0num+=z
                c1num+=abs(k-1-2*d)*z
    assert (0,0) not in collected
    avg_sq=F(sum(a*a+b*b for a,b in collected.values()),k*k*den*den)
    gauge_avg_sq=F(sum(a*a+b*b for a,b in gauge_collected.values()),k*k*den*den)
    assert avg_sq==gauge_avg_sq
    common=7*n*scale*scale
    c0=F(c0num,common)
    kc1=F(c1num,2*common)
    avg_hi=sqrt_bounds(avg_sq)[1]
    cs_hi=sqrt_bounds(F(k*k-1,12*k))[1]
    eps=F(n,10**80)
    linear=eps*k*avg_hi
    nonlinear=eps*eps*(kc1+c0*(1+cs_hi))/2
    b=linear+nonlinear
    t=F(9,4)*b
    assert b<t<2
    root_lo=sqrt_bounds(1-t*t/4)[0]
    assert root_lo>0
    mass=1-b*b/(t*t)
    arc_budget=t/(F(157,50)*root_lo)
    lower=mass*mass/(F(k,n)+arc_budget)-1
    assert lower>F(7,2)
    # This proves a >1 discrepancy for any smooth 0<=h<=1 that is 1
    # on [-1,1] and supported in [-5/4,5/4]: its CUE integral is <=5/2.
    return dict(K=k,N=str(n),epsilon=dec(eps),fourier_denominator=den,
                nonconstant_modes=len(coeff),
                raw_and_midpoint_average_norms_equal=True,
                K_times_average_HS_squared=str(k*avg_sq),
                commutator_C0_upper=dec(c0),K_commutator_C1_upper=dec(kc1),
                linear_return_bound=dec(linear),nonlinear_return_bound=dec(nonlinear),
                normalized_HS_return_bound=dec(b),pair_mass_lower=dec(lower),
                strict_smooth_pair_discrepancy_lower=dec(lower-F(5,2)),
                quantization='Position symbol e(k q+l p) -> T(l,k); bounds also hold with ordinary-midpoint gauge',
                scope='Finite N, fixed tau=10^-80; not an asymptotic BGS counterexample')


if __name__=='__main__':
    print(json.dumps(dict(certificates=[certificate(k) for k in (199,201,203,205)],
                         arithmetic='Exact integers and fractions; decimal strings rounded only for display'),indent=2))
