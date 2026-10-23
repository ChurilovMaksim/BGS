#!/usr/bin/env python3
"""Exact symbolic audit of the rational Wick collision mean; no physical limit."""
import hashlib
import json
from pathlib import Path
import sympy as z

n,m=z.symbols('N m',positive=True)
hp=(m+1)/(m*(n+m))
hk=(m+1)/((m-1)*(n+m)*(n+m-1))
energy=m*(m-1)
swap=m*(m-1-2*(n-1)/(m+2))
tn=m*m*(m-1)*hp
sn=m*(n+m-1-2*(n-1)/(m+2)-(m+1)/(n+m))
cross=m*(m-1)
joint=tn+sn+2*cross
mu=(n-1)/m
second=mu+2*(n-1)*(n-2)/(m*(m+1))
v=n+m-2
scalar=4*m*m*hk*(v*v-2*v*mu+second)
derived=(2*(n*n+4*n+2)*(energy+swap)-4*joint+(n+2)*scalar)/(2*n*(n+1)*(n+2)*(n+3))
target=2*m*((n+5)*m*(m+1)-(n+2)*(n+3))/((n+1)*(n+2)*(n+3)*(m+2))
residual=z.factor(derived-target)
if residual != 0:
    raise RuntimeError(('rational identity failed',residual))
a,t=z.symbols('alpha t',positive=True)
constant=z.limit(target.subs({m:a/t,n:1/t}),t,0,dir='+')
linear=z.limit(z.diff(target.subs({m:a/t,n:1/t}),t),t,0,dir='+')
if z.simplify(constant-2*a*a)!=0 or z.simplify(linear+2*(a*a+a+1))!=0:
    raise RuntimeError('large-N coefficient identity failed')
print(json.dumps({'status':'PASS','arithmetic':'exact SymPy rational functions',
                  'sympy_version':z.__version__,'rational_residual':str(residual),
                  'constant_term':str(constant),'inverse_N_coefficient':str(linear),
                  'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'nonclaims':['The stars-and-bars applicability and tail estimates require the written proof.',
                               'No collision distribution or physical BGS theorem is computed.']},indent=2))
