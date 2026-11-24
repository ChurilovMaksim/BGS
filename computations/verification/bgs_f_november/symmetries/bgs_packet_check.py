"""Exact coefficient and affine-normalizer checks for the fixed BGS map."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"research"))
from coefficients import raw_symbol

IDENTITY=(1,0,0,1)
LINEAR=(3,-4,-2,3)
ROOT=(1,-2,-1,1)
REVERSE=(1,0,0,-1)

def mult(A,B):
    a,b,c,d=A
    e,f,g,h=B
    return (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)

def inverse(A):
    a,b,c,d=A
    determinant=a*d-b*c
    assert abs(determinant)==1
    return tuple(x*determinant for x in (d,-b,-c,a))

def apply(A,v):
    a,b,c,d=A
    x,y=v
    return a*x+b*y,c*x+d*y

def transpose(A):
    a,b,c,d=A
    return a,c,b,d

def fixed_tables(g):
    values=[]
    for q,p in product(range(2),repeat=2):
        monomials=[(a,b,(-1)**((a*q+b*p)%2)*r,(-1)**((a*q+b*p)%2)*i)
                   for (a,b),(r,i) in g.items()]
        assert all(sum((a if component==0 else b)*value for a,b,re,im in monomials
                       for value in [re if part==0 else im])==0
                   for component,part in product(range(2),repeat=2))
        for mode in (lambda a,b:a*b,lambda a,b:b*b):
            assert all(sum(mode(a,b)*value for a,b,re,im in monomials
                           for value in [re if part==0 else im])==0 for part in range(2))
        assert sum(im for _,_,_,im in monomials)==0
        numerator=sum(-4*a*a*re for a,_,re,_ in monomials)
        values.append(dict(q_twice=q,p_twice=p,gqq_over_pi_squared=str(F(numerator,4000))))
    assert [row["gqq_over_pi_squared"] for row in values]==[
        "-19606/125","-19594/125","24306/125","24894/125"]
    return values

def affine_check():
    assert mult(ROOT,ROOT)==LINEAR
    assert mult(REVERSE,mult(LINEAR,REVERSE))==inverse(LINEAR)
    fixed=list(product(range(2),repeat=2))
    winners=[]
    seen=Counter()
    for s,reversal,sign in product(range(2),range(2),(1,-1)):
        C=mult(ROOT if s else IDENTITY,REVERSE if reversal else IDENTITY)
        C=tuple(sign*x for x in C)
        for t in fixed:
            signature=tuple(tuple((r+w)%2 for r,w in zip(apply(C,u),t)) for u in fixed)
            seen[signature]+=1
            if signature==tuple(fixed):
                winners.append(dict(s=s,reversal=reversal,sign=sign,
                                    t_twice=list(t),matrix=list(C)))
    assert len(winners)==4
    assert set(tuple(x["matrix"]) for x in winners)=={IDENTITY,REVERSE,
        tuple(-x for x in IDENTITY),tuple(-x for x in REVERSE)}
    return dict(representatives=32,distinct_actions=len(seen),fixed_point_preservers=winners)

def orbit_check(g):
    P=transpose(LINEAR)
    answer=[]
    for e,minimum in [((1,0),4),((0,1),3)]:
        assert g[e] in {(200,-20),(-12,-16)}
        for sign in (1,-1):
            Q=P if sign==1 else inverse(P)
            v=e
            for j in range(1,33):
                v=apply(Q,v)
                assert abs(v[1])>=minimum and v not in g
                assert 2*max(map(abs,v))>=5**j
        a,b=e
        factor=F(a*a)-F(b*b,2)
        r,i=g[e]
        imm=F(i,4000)*factor
        error_over_tau=20*F(10**45,10**80)
        assert abs(imm)*3-error_over_tau>F(1,1000)
        answer.append(dict(e=list(e),reduced_real=str(F(r,4000)*factor),
                           reduced_imag=str(imm),finite_orbit_checks=64))
    return answer

def main():
    g={(b,a):(r*(-1)**(a*b%2),i*(-1)**(a*b%2))
       for (a,b),(r,i) in raw_symbol().items()}
    assert all(abs(a)+abs(b)<=10 and abs(b)<=1 for a,b in g)
    assert sum(abs(r)+abs(i) for r,i in g.values())==4744
    assert 12*(F(440,7))**4<10**10
    assert F(7)<2**4
    assert 2*(1+F(2,5))/(1-F(2,5))<10
    assert 2*F(1,5)**2<F(1,10)
    # For beta=1/4, using Lambda>5 and 5^(1/4)>7/5:
    assert F(7,5)**4<5
    assert 2*(1+2*F(5,7)/(1-F(5,7)))<20
    data=dict(physical_modes=len(g),l1_upper=str(F(4744,4000)),
              fixed_points=fixed_tables(g),dual_orbits=orbit_check(g),
              affine=affine_check(),relative_fourier_remainder=str(20*F(10**45,10**80)))
    if "--verify" in sys.argv:
        expected=json.loads((Path(__file__).resolve().parent/'data/checks.json').read_text())
        assert data==expected
        print("Fixed points, Fourier invariants and affine exclusions verified.")
    else:
        print(json.dumps(data,indent=2))

if __name__=="__main__":
    main()
