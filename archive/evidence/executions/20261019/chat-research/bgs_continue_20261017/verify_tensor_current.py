#!/usr/bin/env python3
"""Infinite Taylor sums evaluated exactly; no truncation or Monte Carlo."""
import json
from pathlib import Path
import platform
import sys
from math import comb
import sympy as S

z,n=S.symbols('z n')
a=S.Rational(1,3)
b=(z-a)/(1-a*z)
tau=(1-a*a)/((1-a*z)*(1-a/z))
left=S.Matrix([[S.Rational(3,5),-S.Rational(4,5)],
               [S.Rational(4,5),S.Rational(3,5)]])
right=S.Matrix([[S.Rational(5,13),-S.Rational(12,13)],
                [S.Rational(12,13),S.Rational(5,13)]])
mat=left*S.diag(b,1)*right
assert S.simplify(mat*mat.subs(z,1/z).T-S.eye(2))==S.zeros(2)

def integrate(expr):
    expr=S.cancel(expr/z)
    # The only possible inside-circle poles are 0 and a; real rational data.
    return S.simplify(S.residue(expr,z,0)+S.residue(expr,z,a))


# Exact sums sum_(n>=0) n^d t^n by Euler differentiation. Cached as rationals.
t=S.symbols('t')
euler=[1/(1-t)]
def full_geom(d):
    while len(euler)<=d:
        euler.append(S.cancel(t*S.diff(euler[-1],t)))
    return euler[d].subs(t,a*a)


def coefficient_moments(num,den_power):
    """Sum n^p |[z^n]num/(1-a*z)^K|^2 for p=0,1,2, exactly."""
    num=S.Poly(S.expand(num),z)
    deg=num.degree()
    coeffs=[num.nth(j) for j in range(deg+1)]
    k=den_power
    # For n>=deg the coefficient equals a^n times this polynomial in n.
    pol=0
    for j,c in enumerate(coeffs):
        if c:
            rising=S.prod(n-j+h for h in range(1,k)) / S.factorial(k-1)
            pol += c*a**(-j)*rising
    pol=S.Poly(S.expand(pol*pol),n)
    totals=[]
    for p in (0,1,2):
        tail=0
        for (degree,),c in pol.terms():
            d=degree+p
            early=sum(S.Integer(v)**d*a**(2*v) for v in range(deg))
            tail += c*(full_geom(d)-early)
        early_mass=0
        for v in range(deg):
            cv=sum(coeffs[j]*S.binomial(k+v-j-1,k-1)*a**(v-j)
                   for j in range(min(v,deg)+1))
            early_mass += S.Integer(v)**p*cv*cv
        totals.append(S.factor(tail+early_mass))
    return totals


references=[]
for source in (0,1):
    target=1-source
    x=mat[:,source]
    dx=S.simplify(z*x.diff(z))
    transmission=S.cancel(mat[target,source]*mat[target,source].subs(z,1/z))
    w=right[0,source]**2
    current=w*tau
    normdx=sum(dx[j]*dx[j].subs(z,1/z) for j in (0,1))
    equal_slot=S.cancel(x[target].subs(z,1/z)*dx[target])
    refs={
       'T':integrate(transmission),
       'T2':integrate(transmission**2),
       'A':integrate(current),
       'A2':integrate(current**2),
       'normD2':integrate(normdx),
       'TA':integrate(transmission*current),
       'equal':integrate(equal_slot),
    }
    assert refs['A']==w
    assert refs['A2']==w*w*(1+a*a)/(1-a*a)
    assert refs['normD2']==w*(1+a*a)/(1-a*a)
    references.append(refs)

all_cases=[]
for k_tensor in range(1,7):
    for source in (0,1):
        target=1-source
        f=S.cancel(mat[target,source])
        g=S.cancel(mat[source,source])
        fn=S.cancel(f*(1-a*z))
        gn=S.cancel(g*(1-a*z))
        observed={'mass':0,'L':0,'L2':0,'B':0,'B2':0,'BL':0}
        for count in range(k_tensor+1):
            q=coefficient_moments(S.expand(fn**count*gn**(k_tensor-count)),k_tensor)
            mult=S.binomial(k_tensor,count)
            observed['mass']+=mult*q[0]
            observed['L']+=mult*q[1]
            observed['L2']+=mult*q[2]
            observed['B']+=mult*count*q[0]
            observed['B2']+=mult*count*count*q[0]
            observed['BL']+=mult*count*q[1]
        ref=references[source]
        expected={
            'mass':1,
            'L':k_tensor*ref['A'],
            'L2':k_tensor*(k_tensor-1)*ref['A2']+k_tensor*ref['normD2'],
            'B':k_tensor*ref['T'],
            'B2':k_tensor*(k_tensor-1)*ref['T2']+k_tensor*ref['T'],
            'BL':k_tensor*(k_tensor-1)*ref['TA']+k_tensor*ref['equal'],
        }
        assert all(S.simplify(observed[key]-expected[key])==0 for key in observed), (k_tensor,source)
        all_cases.append({'K':k_tensor,'source':source+1,'identities':len(observed)})

# Polynomial inner example: F=diag(z,1)R, T=16/25 constant.
# Source 1 has L=K-B, source 2 has L=B; this tests the source average and
# the zero-current summands without poles or a geometric-tail calculation.
tt=S.Rational(16,25)
for kk in range(1,101):
    for source in (0,1):
        weights=[S.Integer(comb(kk,j))*tt**j*(1-tt)**(kk-j) for j in range(kk+1)]
        assert sum(weights)==1
        expected_a=1-tt if source==0 else tt
        assert sum(w*((kk-j) if source==0 else j) for j,w in enumerate(weights))==kk*expected_a
        assert sum(w*j for j,w in enumerate(weights))==kk*tt

output={
 'status':'passed','arithmetic':'exact rational polynomials, residues and infinite geometric sums',
 'python':platform.python_version(),'sympy':S.__version__,
 'rational_inner_cases':all_cases,
 'reference_integrals':[{key:str(v) for key,v in ref.items()} for ref in references],
 'polynomial_cases':200,
 'non_claims':['No N-uniform K limit','No Haar/current-isotropy conclusion',
               'No formal proof certificate']
}
Path(sys.argv[1]).write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'status':'passed','rational_cases':len(all_cases),
                  'rational_identities':sum(c['identities'] for c in all_cases),
                  'polynomial_cases':200}))
