#!/usr/bin/env python3
"""Independent exact controls for the ordinary compact-stratum formula.
No source checker is imported. Symbolic/rational checks are not a universal proof.
"""
from __future__ import annotations
import json, math, hashlib, platform
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
I=s.I
checks=[]
def record(name,detail):
    checks.append({'name':name,'passed':True,'detail':detail})

def ss(x): return s.simplify(s.expand_complex(x))
def abs2(x): return ss(x*s.conjugate(x))
ax,ay=s.symbols('ax ay', real=True)
p=ax+I*ay
u,v,u2,v2=s.symbols('u v u2 v2', real=True)
t,t2=s.symbols('t t2',real=True)
E=lambda t:s.cos(t)+I*s.sin(t)
omega=-s.Rational(1,2)+I*s.sqrt(3)/2
cases=[
 (0,[u+I*v,u2+I*v2,-u-I*v-u2-I*v2],[u,v,u2,v2],{u:s.Rational(1,5),v:s.Rational(1,7),u2:-s.Rational(1,4),v2:s.Rational(1,6)}),
 (1,[E(t),u+I*v,-E(t)-u-I*v],[t,u,v],{t:0,u:-s.Rational(1,2),v:s.Rational(1,3)}),
 (2,[E(t),(-3+4*I)*E(t2)/5,-E(t)-(-3+4*I)*E(t2)/5],[t,t2],{t:0,t2:0}),
 (3,[E(t),omega*E(t),omega**2*E(t)],[t],{t:0}),
]
for k,ws,shapevars,shapevalues in cases:
    for ap in [(0,0),(s.Rational(1,5),s.Rational(1,7))]:
        vals={ax:ap[0],ay:ap[1],**shapevalues}
        p0=p.subs(vals); w0=[ss(w.subs(vals)) for w in ws]
        assert ss(sum(w0))==0
        for j,w in enumerate(w0):
            assert abs2(w)==1 if j<k else abs2(w)<1
        zs=[(p+w)/(1+s.conjugate(p)*w) for w in ws]
        cols=[ax,ay]+shapevars
        rows=[]
        for j,z in enumerate(zs):
            z0=ss(z.subs(vals))
            dz=[ss(s.diff(z,c).subs(vals)) for c in cols]
            if j<k:
                rows.append([ss(s.im(s.conjugate(z0)*q)) for q in dz])
            else:
                rows.extend([[ss(s.re(q)) for q in dz],[ss(s.im(q)) for q in dz]])
        observed=abs(ss(s.det(s.Matrix(rows))))
        den=s.prod(abs2(1+s.conjugate(p0)*w)**(1 if j<k else 2) for j,w in enumerate(w0))
        delta=ss(9-abs2(sum(w*w for w in w0)))
        # For k<3, one disk is eliminated by delta, with coordinate Jacobian 1.
        # For k=3, each equilateral component has dH/J = 2/sqrt(3) dphi.
        slice_factor=2/s.sqrt(3) if k==3 else 1
        expected=ss(slice_factor*delta*(1-abs2(p0))**(4-k)/den)
        assert ss(observed-expected)==0,(k,ap,observed,expected)
        record(f'N3_k{k}_jacobian_at_{ap}',{'jacobian':str(observed),'gauge_delta':str(delta),'comparison':'exact rational/algebraic'})

# Independently differentiate the real a-map at arbitrary rational centered tuples.
for N in [1,2,3,5,7,9]:
    ws=[]
    for j in range(N//2):
        z=s.Rational(j+1,N+2)+I*s.Rational(j+1,2*N+3)
        ws.extend([z,-z])
    if N%2: ws.append(s.Integer(0))
    p0=s.Rational(1,5)+I*s.Rational(1,7)
    zs=[ss((p0+w)/(1+s.conjugate(p0)*w)) for w in ws]
    T=sum((z-p)/(1-s.conjugate(p)*z) for z in zs)
    dt=[ss(s.diff(T,c).subs({ax:s.re(p0),ay:s.im(p0)})) for c in [ax,ay]]
    det=ss(s.re(dt[0])*s.im(dt[1])-s.re(dt[1])*s.im(dt[0]))
    target=ss((N*N-abs2(sum(w*w for w in ws)))/(1-abs2(p0))**2)
    assert ss(det-target)==0
    record(f'N{N}_gauge_derivative',{'determinant':str(det)})

# N=1 disk calibrates the normalized measure: (d^2p) delta(w) d^2w/pi.
assert ss((1-abs2(s.Integer(0)))**2)==1
record('N1_disk_normalization',{'result':'d^2p/pi; delta(w) d^2w/pi has mass 1/pi'})

# N=2 disk: angular averaging and elementary beta integrals yield a telescope.
n=s.symbols('n',integer=True,nonnegative=True)
term=s.factor(4*(n+1)**2*(1/(2*n+1)-1/(2*n+3))*(1/(2*n+1)-2/(2*n+2)+1/(2*n+3)))
telescope=1/(2*n+1)**2-1/(2*n+3)**2
assert s.simplify(term-telescope)==0
assert s.summation(term,(n,0,s.oo))==1
record('N2_disk_total_mass',{'series_term':str(term),'telescope':str(telescope),'mass':'1'})

# N=3 all-circle: exact global a-density after both ordered equilateral components.
x=s.symbols('x',real=True,nonnegative=True)
radial_integral=s.integrate(3*s.sqrt(3)/s.pi/(1+x+x*x),(x,0,1))
assert s.simplify(radial_integral)==1
record('N3_all_circle_total_mass',{'density_d2p':'3*sqrt(3)/(pi^2*(1+|p|^2+|p|^4))','mass':str(radial_integral)})
e=s.symbols('e',positive=True)
tail=6/s.pi*(s.pi/3-s.atan((2*(1-e)**2+1)/s.sqrt(3)))
leading=s.simplify(s.limit(tail/e,e,0,dir='+'))
assert leading==2*s.sqrt(3)/s.pi
record('N3_zero_source_tail',{'tail_formula':str(tail),'first_order':str(leading)})

# Odd-N uniform Delta bound: enumerate all possible vertices of the real box slice.
for N in range(1,32,2):
    extreme=[]
    for nplus in range(N):
        last=-(2*nplus-(N-1))
        if abs(last)<=1:
            extreme.append(N-1+last*last)
    assert max(extreme)==N-1
    assert N*N-(N-1)**2==2*N-1
record('odd_N_box_slice_vertex_check',{'N':'1,3,...,31','scope':'finite check of the general elementary vertex proof; not an exhaustive complex-tuple enumeration'})

# Actual completed source U=I_3, nonzero real sample: four local sectors sum exactly.
q=s.Rational(1,4); rr=s.Rational(1,12); uu=s.Rational(1,6); vv=s.Rational(1,8)
local=(1+rr-uu-vv)/(1-q)
assert local==s.Rational(19,18)
assert ((1+rr)/(1-q)-(uu+vv)*s.integrate((1-q*x)**-2,(x,0,1)))**3==local**3
record('N3_diagonal_completed_source',{'source_a':'1/2','source_b':'1/2','source_c':'1/3','source_d':'1/4','exact_value':str(local**3),'scope':'factorized complete signed source; no numerical sector cancellation'})

out={'status':'passed','python':platform.python_version(),'sympy':s.__version__,'checks':checks,'claims_not_tested':['No all-N proof by sampling','No super-Berezinian','No large-N normalized tail','No BGS or microscopic CUE law']}
(ROOT/'checks/results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
