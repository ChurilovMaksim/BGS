#!/usr/bin/env python3
"""Exact controls for the beta-smoothed path-law criterion and its limits."""
from fractions import Fraction as F
from math import comb,factorial
import json,platform,sys


def main():
    cases=[]
    for K in range(1,101):
        target=[F(comb(K,k)*factorial(k)*factorial(K-k),factorial(K+1)) for k in range(K+1)]
        assert target==[F(1,K+1)]*(K+1)
        # Integrate the difference of the quantile functions on every grid-probability cell.
        exact=sum(((F(i,K)-F(i,K+1))**2+(F(i+1,K+1)-F(i,K))**2)/2 for i in range(K+1))
        assert exact==F(2*K+1,6*K*(K+1)) and exact<=F(1,2*K)
        # Beta-binomial composition: E[(Y-t)^2]=[2+2(K-3)t(1-t)]/((K+2)(K+3)).
        max_error=max(F(2,(K+2)*(K+3)),F(K+1,2*(K+2)*(K+3)))
        assert max_error<=F(1,2*(K+2))
        # Exact polynomial check that uniform Bernstein weights smooth to density one.
        coefficients=[0]*(K+1)
        for k in range(K+1):
            for j in range(K-k+1):coefficients[k+j]+=comb(K,k)*comb(K-k,j)*(-1)**j
        assert coefficients==[1]+[0]*K
        if K in (1,2,3,10,100):
            cases.append({'K':K,'uniform_grid_W1_exact':str(exact),
                          'max_beta_squared_displacement_exact':str(max_error)})
    out={'status':'passed','python':platform.python_version(),'K_range':[1,100],
         'uniform_target_weights_exact':True,'uniform_smoothed_density_exact':True,
         'cases':cases,
         'analytic_negative_controls':[
          {'pair':'Uniform[0,1] versus its discrete uniform K-grid','TV_exact':'1',
           'reason':'Mutually singular; an arbitrarily small W1 error does not imply TV error.'},
          {'pair':'delta_(1/2) versus its beta-binomial smoothing','TV_exact':'1',
           'reason':'The smoothing has a density; the AC-cluster assumption is necessary for the general TV approximation statement.'}
         ],
         'non_claims':['No rate of TV approximation for an unknown compact L1 family.',
                       'No estimate of the actual quantum path weights.']}
    with open(sys.argv[1],'w') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({'status':'passed','K_range':[1,100],'both_singular_TV_controls':'1'}))


if __name__=='__main__':main()
