#!/usr/bin/env python3
"""Exact bounded regression controls accompanying a separate analytic audit.

No tiny-coupling floating-point exponentials and no numerical asymptotic
extrapolation. Failure checks remain active under python -O.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parent

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

expected = {
    'growing_word_window.md': '4c497a406e51dd75cc0ca0b3b85100c3713c2013ae2d53b3d15e7ecceaf7222a',
    'strong_freeness_obstruction.md': '8eab771234f702cdf840497e49d7bf43c9fc1ab673818a75f31661bc99273729',
}
for name, sha in expected.items():
    require(hashlib.sha256((ROOT/'frozen'/name).read_bytes()).hexdigest() == sha,
            'Frozen candidate changed: '+name)

# Independent exact Laurent expansion of the displayed physical symbol.
x, y = s.symbols('x y', nonzero=True)
C = lambda n: (x**n+x**(-n))/2
r = (1-C(7))*(1+C(1))
g = C(7)+r/10+r*(x-x**-1)/(200*s.I)-s.Rational(1,10)
g += r.subs(x,-x)*((-3-4*s.I)*y+(-3+4*s.I)/y)/1000
coeffs={}
for term in s.Add.make_args(s.expand(g)):
    powers=term.as_powers_dict()
    k,l=int(powers.get(x,0)),int(powers.get(y,0))
    coeffs[k,l]=s.simplify(coeffs.get((k,l),0)+term/x**k/y**l)
coeffs={v:c for v,c in coeffs.items() if c != 0}
require(sum(coeffs.values()) == s.Rational(9,10), 'Incorrect equilibrium value')
require(all(sum(c*v[j] for v,c in coeffs.items()) == 0 for j in range(2)),
        'Nonzero equilibrium differential')
H=s.Matrix(2,2,lambda i,j:s.simplify(-4*sum(c*v[i]*v[j] for v,c in coeffs.items())))
require(H == s.diag(-s.Rational(19606,125),0), 'Incorrect equilibrium Hessian')
moment=s.simplify(sum((abs(s.re(c))+abs(s.im(c)))*(v[0]**2+v[1]**2) for v,c in coeffs.items()))
require(moment == s.Rational(51451,1000), 'Second-moment input mismatch')
require(max(abs(v[0])+abs(v[1]) for v in coeffs) <= 10, 'Support bound mismatch')

# Gaussian second-order differential identity, checked symbolically.
t,a,b=s.symbols('t a b', real=True)
f=s.exp(-s.pi*t*t)
L=lambda z:a*s.diff(z,t)+2*s.pi*s.I*b*t*z
z=-a+s.I*b
require(s.simplify(L(L(f))-(2*s.pi*a*z+4*s.pi**2*z*z*t*t)*f)==0,
        'Weyl Gaussian second-order identity failed')
moment4=s.simplify(s.integrate(s.sqrt(2)*t**4*s.exp(-2*s.pi*t*t),(t,-s.oo,s.oo)))
require(moment4 == 3/(16*s.pi**2), 'Gaussian fourth moment failed')

# Exact finite raw/midpoint identities, including aliases outside one cell.
checks=0
for N in (1,3,5,7,9,21,35):
    inv2=(N+1)//2
    labels=[(-N-1,3),(N+2,-2),(0,0),(1,0),(0,1),(-3,-2),(-1,2),(2,-1)]
    for aa,bb in labels:
        for j in range(N):
            require((N*aa*bb+2*bb*(j+inv2*aa)-bb*(2*j+aa))%(2*N)==0,
                    'Raw/midpoint phase mismatch')
            checks+=1

S=s.Matrix([[3,4],[2,3]])
require(S.det()==1 and max(sum(abs(S[i,j]) for j in range(2)) for i in range(2))==7,
        'Cat matrix bound failed')
require((S.T*S).charpoly().as_expr().subs(s.Symbol('lambda'),49)>0,
        'Unexpected characteristic polynomial evaluation')
B=[312*7**(2*j) for j in range(3)]
loss=Fraction((B[0]+B[1])**2+(B[1]+B[2])**2,4)
require(loss == 146137680000, 'Rayleigh constant mismatch')
require(loss<10**12, 'Claimed outlier margin failed')

# Tree-shell formulas for finitely many exact R, only as finite regression.
for R in range(1,20):
    norm=1+sum(Fraction(4*3**(r-1),3**r) for r in range(1,R+1))
    require(norm==1+Fraction(4*R,3),'Radial norm shell identity failed')
    scaled_edge=sum(Fraction(8*3**(r-1),3**(r-1)) for r in range(1,R+1))
    require(scaled_edge==8*R,'Radial adjacency shell identity failed')

print(json.dumps({
    'result':'PASS', 'scope':'Exact finite algebra regression only; analytic verdict is separate.',
    'candidate_sha256':expected,
    'fourier_terms':len(coeffs),'second_moment_re_im':str(moment),
    'hessian_over_pi_squared':str(H),
    'midpoint_phase_cases':checks,
    'cat_residual_constants':B,
    'outlier_loss':'146137680000 / 10^160',
    'gaussian_fourth_moment':'3/(16*pi^2)',
    'tree_shell_regression':'R=1,...,19'
},indent=2))
