#!/usr/bin/env python3
"""Bounded exact controls; not an asymptotic universality computation."""
import hashlib
import json
import platform
import sympy as s
from pathlib import Path

x,y,T,q,eps=s.symbols('x y T q eps', positive=True)
a,b,c,d,z=s.symbols('a b c d z')

# Exact U(1) ratio by residues at 0 and b (|a|,|b|<1).
integrand=(1-c*z)*(z-d)/((1-a*z)*(z-b)*z)
phase=s.factor(s.residue(integrand,z,0)+s.residue(integrand,z,b))
target=1+(a-c)*(b-d)/(1-a*b)
assert s.factor(phase-target)==0

# Normalization/top odd coefficient from the pinned (4.16); all integrals exact.
raw=(1-y)/(1+y)**3
primitive=s.factor(s.integrate(raw,(y,0,T)))
assert primitive==T/(T+1)**2
assert s.limit(primitive,T,s.oo)==0
surface=s.integrate((1+y)**-2,(y,0,T))
assert s.factor(surface-T/(T+1))==0
assert s.limit(surface,T,s.oo)==1

normalizations={}
for nc in range(1,7):
    density=nc*(1-x)**(nc-1)*(1-y)/(1+y)**(nc+2)
    if nc>1:
        density+=nc*(nc-1)*(1-x)**(nc-2)*(1+x*y)/(1+y)**(nc+2)
    value=s.integrate(s.integrate(density,(x,0,1)),(y,0,s.oo))
    assert value==(0 if nc==1 else 1)
    normalizations[str(nc)]=str(value)

# Weak boundary concentration missed by setting N_c=1 before integration.
concentration=[]
for k in range(7):
    moment=s.factor(s.prod(s.Rational(j,1)/(eps+j) for j in range(1,k+1)))
    # eps * Beta(k+1,eps) = k! / product_{j=1}^k(eps+j).
    assert s.limit(moment,eps,0,dir='+')==1
    concentration.append({'power':k,'exact_moment':str(moment),'limit':1})

# Polynomial identity for the requested pair rational function.
assert s.factor(phase-(1+c*d-b*c-a*d)/(1-a*b))==0

# Boson/fermion-opposite source insertion of the graph-type form.
# Sources a=A(1+j), c=A(1-j), b=B(1+k), d=B(1-k).
j,k,q0=s.symbols('j k q0')
qp=q0*(1+j)*(1+k);rp=q0*(1-j)*(1-k)
source_curvature=s.factor(s.diff(1+4*q0*j*k/(1-qp),j,k).subs({j:0,k:0}))
divergent_curvature=s.factor(s.diff(rp/(1-qp),j,k).subs({j:0,k:0}))
assert s.factor(source_curvature-4*q0/(1-q0))==0
assert s.factor(divergent_curvature-q0*(1-3*q0+4*q0**2)/(1-q0)**3)==0

# Fixed higher flavors: independent exact residue check on a cancellation family.
# The first pair is arbitrary rational; the remaining flavors cancel identically.
higher=[]
for k in range(1,5):
    av=[s.Rational(1,3)]+[s.Rational(j+1,2*j+7) for j in range(1,k)]
    bv=[s.Rational(1,5)]+[s.Rational(j+1,3*j+11) for j in range(1,k)]
    cv=[s.Rational(-1,7)]+av[1:]
    dv=[s.Rational(2,9)]+bv[1:]
    f=s.cancel(s.prod((1-C*z)/(1-A*z) for A,C in zip(av,cv))*
               s.prod((z-D)/(z-B) for B,D in zip(bv,dv))/z)
    val=s.factor(s.residue(f,z,0)+sum(s.residue(f,z,B) for B in set(bv)))
    want=s.factor(1+(av[0]-cv[0])*(bv[0]-dv[0])/(1-av[0]*bv[0]))
    assert val==want
    higher.append({'flavors':k,'exact_phase_ratio':str(val)})

out={
 'result':'all bounded exact controls passed',
 'arithmetic':'SymPy exact rational and symbolic integration/residues/limits',
 'python':platform.python_version(),'sympy':s.__version__,
 'one_site_ratio':str(phase),
 'bulk_y_cutoff':str(primitive),'surface_normalization_cutoff':str(surface),
 'standard_color_normalizations':normalizations,
 'boundary_concentration_moments':concentration,
 'higher_flavor_cancellation_controls':higher,
 'opposite_BF_source_curvature':str(source_curvature),
 'surface_logarithmic_source_curvature':str(divergent_curvature),
 'non_claims':['No asymptotic spectral assertion','No test of actual extremely-small-coupling U_N',
               'No general higher-flavor boundary supermeasure constructed',
               'No numerical quadrature or Monte Carlo evidence'],
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
print(json.dumps(out,indent=2))
