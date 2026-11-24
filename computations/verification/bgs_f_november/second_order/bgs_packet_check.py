"""Exact checks of two-orbit collision bounds and fixed-kick certificates."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))
sys.path.insert(0, str(ROOT))
from coefficients import raw_symbol
from zero_mode.weights import GRID, bump, convolution

P = 7

def valuation(value, cap):
    v=0
    while v<cap and value%P==0:
        value//=P
        v+=1
    return v

def split_root(k):
    rho=3
    modulus=P
    for _ in range(1,k):
        rho=next(rho+u*modulus for u in range(P)
                 if ((rho+u*modulus)**2-2)%(P*modulus)==0)
        modulus*=P
    return rho

def orbit_points(d,K,ell,rho):
    n=P**K
    gamma=(3+2*rho)%n
    inverse=pow(gamma,-1,n)
    x=(d[0]+rho*d[1])%n
    y=(d[0]-rho*d[1])%n
    points=[]
    for _ in range(ell):
        points.append((x,y))
        x,y=x*gamma%n,y*inverse%n
    return points

def collision_check(k,ell,labels,short):
    N=P**k
    rho=split_root(k)
    cases=0
    max_energy=F(0)
    for d,e in product(labels,repeat=2):
        alpha=min(min(valuation(x,k) for x in d),min(valuation(x,k) for x in e))
        K=k-alpha
        n=P**K
        p1=tuple(x//P**alpha for x in d)
        p2=tuple(x//P**alpha for x in e)
        delta=max(min(valuation(x,K) for x in p1),min(valuation(x,K) for x in p2))
        assert delta<=1
        u=orbit_points(p1,K,ell,rho)
        v=orbit_points(p2,K,ell,rho)
        pairs=[]
        histogram=Counter()
        for i,(x,y) in enumerate(u):
            profile=Counter()
            for j,(X,Y) in enumerate(v):
                index=valuation(x*Y-X*y,K)
                profile[index]+=1
                if i<=j:
                    s=((x+X)%n,(y+Y)%n)
                    histogram[s]+=1
                    pairs.append((s,index))
            total=0
            for b in range(K,delta,-1):
                total+=profile[b]
                period=3*P**(b-delta-1)
                assert (total-1)*period<=ell-1
        multiple=1 if short else P
        for s,v7 in pairs:
            assert 3*n*histogram[s]<=multiple*(6*n+14*ell*P**v7)
        energy=F(sum(value**2 for value in histogram.values()),ell*ell)
        if short:
            assert energy<=F(12,5)
        else:
            assert energy<=1000*(1+F(k*ell,N))
        max_energy=max(max_energy,energy)
        cases+=1
    return dict(k=k,length=ell,short=short,cases=cases,max_energy_over_length_squared=str(max_energy))

def weight_bounds():
    nodes=[bump(i) for i in range(GRID+1)]
    lo,hi=map(list,zip(*[(min(nodes[abs(i)][0],nodes[abs(i+1)][0]),
                         max(nodes[abs(i)][1],nodes[abs(i+1)][1]))
                        for i in range(-GRID,GRID)]))
    cl=convolution(lo)
    norm=4*sum(hi)**4
    low6=F(GRID**2*cl[6*GRID//7]**2,norm)
    low0=F(GRID**2*cl[1]**2,norm)
    assert low6>F(1599,100000) and low0>F(1138,10000)
    return dict(at_six_sevenths=str(low6),at_first_grid_node=str(low0))

def finite_certificates():
    old=F(204,1000)
    old_lb=F(6854,10**5)*(1-old**2/2)**2+F(1599,10**5)*(1-2*old**2)**2-F(2067,10**5)-2*F(1141,10**4)/49
    assert old_lb>F(53,1000)
    cases=[]
    for k,x,cap in ((57,10**21,F(1,10**5)),(58,3*10**20,F(17,10**4)),
                     (59,78*10**18,F(291,1000))):
        n=P**k
        m=3*n//7
        t=F(n,10**80)
        L=x*x
        assert L*1000*k<=n
        D=F(2,3)*t*(F(m,x)+x)+F(9,4)*t*t*m+F(27,20)*t**3*m*(L+1)
        assert D<cap
        trace=1-cap**2/2
        cue_upper=F(2067,10**5)+2*F(1141,10**4)/n
        pair=F(6854,10**5)*trace**2+F(1599,10**5)*(1-2*cap**2)**2-cue_upper
        assert pair>F(53,1000) and trace>F(957,1000)
        assert F(98,1000)**2>F(1,105)
        gap=1-F(196,1000)-cap**2/2
        assert gap>F(76,100)
        if k<59:
            assert trace>F(99999,100000)
        cases.append(dict(k=k,N=str(n),m=str(m),length=str(L),D_upper=str(D),
                          D_upper_decimal=float(D),trace_lower=str(trace),
                          pair_lower=str(pair),bounded_gap_lower=str(gap)))
    return cases

def composite_certificates():
    h,v=1,0
    values={}
    for j in range(1,148):
        h,v=h+2*v,h+v
        if j in (21,147):
            values[j]=h
    output=[]
    for j,k,x,cap in ((21,54,47*10**17,F(19,1000)),(147,19,774000,F(13,100))):
        h=values[j]
        d=h
        while d%7==0:
            d//=7
        assert d%7!=0
        n7=7**k
        n=n7*d
        m=3*n7//7
        assert m%j==0 and x*x*1000*k<=n7
        t=F(n,10**80)
        D=F(2,3)*t*(F(m,x)+x)+F(9,4)*m*t*t+F(27,20)*m*t**3*(x*x+1)
        assert D<cap
        trace=1-cap**2/2
        terms=50 if j==21 else 10
        assert GRID*terms*m<=n and (terms*cap)**2<2
        pair=F(1138,10000)*sum((1-(h*cap)**2/2)**2 for h in range(1,terms+1))-F(2067,10**5)-2*F(1141,10**4)/n
        assert pair>(F(4149,1000) if j==21 else F(582,1000))
        if j==21:
            assert n>4*10**51 and m>10**45 and trace>F(9998,10000)
        else:
            assert n>3*10**69 and m==4885240793731347 and trace>F(9915,10000)
        output.append(dict(Pell_exponent=j,seven_exponent=k,coprime_factor=str(d),N=str(n),
                           m=str(m),D_upper=str(D),D_upper_decimal=float(D),
                           trace_lower=str(trace),pair_lower=str(pair)))
    return output

def main():
    coeff=raw_symbol()
    q=Counter()
    for (a,b),(r,i) in coeff.items():
        val=min(valuation(a,6),valuation(b,6))
        assert val<=1
        norm=(a*a-2*b*b)//P**(2*val)
        assert norm%P!=0
        q[a*a-2*b*b]+=abs(r)+abs(i)
    assert sum(q.values())==4744
    assert {d for d in coeff if (d[0]*d[0]-2*d[1]*d[1])==-98}=={(0,7),(0,-7)}
    bound=F(sum(value**2 for norm,value in q.items() if norm!=-98)+2*1800**2,4000**2)
    assert bound==F(847747,2000000)<F(4,9)
    assert F(6,5)**4*F(12,5)<F(9,4)**2
    close=[(0,-7),(0,7),(1,0),(-1,0),(0,1),(0,-1),(1,7)]
    checks=[collision_check(6,19,list(coeff),True),collision_check(7,117,close,True),
            collision_check(3,147,close,False),collision_check(4,401,close,False)]
    output=dict(first_order_coefficient_squared=str(bound),
                support_norm_classes=dict(sorted(q.items())),
                collision_checks=checks,fixed_kick=finite_certificates(),
                composite_kick=composite_certificates(),weight_lower_bounds=weight_bounds())
    if '--verify' in sys.argv:
        check=json.loads((Path(__file__).resolve().parent/'data/checks.json').read_text())
        assert json.loads(json.dumps(output))==check
        print('Exact orbit-collision counts and fixed-kick bounds verified.')
    else:
        print(json.dumps(output,indent=2))
if __name__=='__main__':
    main()
