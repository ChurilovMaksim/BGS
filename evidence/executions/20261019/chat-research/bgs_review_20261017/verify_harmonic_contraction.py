#!/usr/bin/env python3
"""Independent branching-rule controls of the appendix's harmonic bounds."""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from math import comb
import json, platform, sys


def dimension(weight):
    ans=F(1)
    for i in range(len(weight)):
        for j in range(i+1,len(weight)):
            ans*=F(weight[i]-weight[j]+j-i,j-i)
    assert ans.denominator==1
    return ans.numerator


def circle_weights(lam):
    """U(m)->U(m-1) branching; circle exponent |lam|-|mu|."""
    d=dimension(lam); probs={}
    for mu in product(*(range(lam[i+1],lam[i]+1) for i in range(len(lam)-1))):
        assert all(mu[i]>=mu[i+1] for i in range(len(mu)-1))
        exponent=sum(lam)-sum(mu)
        probs[exponent]=probs.get(exponent,F(0))+F(dimension(mu),d)
    assert sum(probs.values())==1
    return probs


def test(lam):
    m=len(lam);r=sum(max(x,0) for x in lam)
    p=circle_weights(lam)
    rho=[F(m+1-2*(i+1),2) for i in range(m)]
    ell=[x+y for x,y in zip(lam,rho)]
    C=sum(x*x-y*y for x,y in zip(ell,rho))
    delta4=sum(x**4-y**4 for x,y in zip(ell,rho))
    D=m*(m+1)*(m+2)*(m+3)
    second=sum(prob*j*j for j,prob in p.items())
    fourth=sum(prob*j**4 for j,prob in p.items())
    assert second==C/F(m*(m+1))
    assert fourth==(6*delta4-(2*m+3)*(m-1)*C+3*C*C)/D
    a=sum(prob/F(comb(m+abs(j),abs(j))) for j,prob in p.items())
    if r:
        assert p.get(0,F(0))<=F(m-1,m+1)
        assert fourth<=12*second+21*second*second
        assert 1-a>=F(m,m+1)*F(r,12*(m+1)+21*r)
        small=F(2*r,m+1)-F(2*r*r,(m+1)**2)-F(6*r*(r-1)*(m+r)*(m+r-1),(m+1)**2*(m+2)*(m+3))
        assert 1-a>=small
        assert fourth-second<=F(24*r*(r-1)*(m+r)*(m+r-1),D)
    else:assert a==1
    if r and lam==(r,)+(0,)*(m-2)+(-r,):
        assert a==1-F(2*r*(m+r-1),(m+r)*(m+2*r-1))
    return a,p


def main():
    counts=[]
    for m in range(2,7):
        n=0
        for ascending in combinations_with_replacement(range(-5,6),m):
            lam=tuple(reversed(ascending))
            if sum(lam) or sum(max(x,0) for x in lam)>6:continue
            test(lam);n+=1
        counts.append({'m':m,'balanced_weights_tested':n})
    a,p=test((2,2,-2,-2))
    b,_=test((4,0,0,-4))
    assert a==F(193,525) and b==F(4,11) and a>b
    out={'status':'passed','python':platform.python_version(),
         'method':'Exact Weyl dimensions and the interlacing branching rule; no simulation.',
         'cases':counts,'total_weights':sum(row['balanced_weights_tested'] for row in counts),
         'counterexample':{'lambda':[2,2,-2,-2],'a_exact':str(a),
                           'sphere_a_exact':str(b),'circle_probabilities_exact':{str(j):str(v) for j,v in p.items()}},
         'non_claims':['Finite branching controls do not prove all highest-weight inequalities.',
                       'No bound on an unknown coherent density or its harmonic remainder.']}
    with open(sys.argv[1],'w') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({'status':'passed','total_weights':out['total_weights'],'counterexample_a':str(a)}))


if __name__=='__main__':main()
