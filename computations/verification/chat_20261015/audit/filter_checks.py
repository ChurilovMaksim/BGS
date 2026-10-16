#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json
from pathlib import Path
import sympy as s
D=Path(__file__).parent
spec=importlib.util.spec_from_file_location('audit',D/'independent_audit.py');a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
z,w,x=s.symbols('z w x')
Pq=z*(z-s.I)*s.prod(1+z*z/s.Integer(n*n) for n in (2,5,6,7,8,9))*(1+w*w)
Pp=s.prod(1+z*z/s.Integer(n*n) for n in (1,2,5,6,7,8,9))*w*(w-s.I)
qs=(0,1,-1,2,-2,5,-5,6,-6,7,-7,8,-8,9,-9)
selected=[[],[]]
for j,P in enumerate((Pq,Pp)):
    for k in qs:
        for l in (-1,0,1):
            v=s.simplify(P.subs({z:s.I*k,w:s.I*l}))
            if v!=0:selected[j].append([k,l,str(v)])
a.need(selected==[[[-1,0,'-4/3']],[[0,-1,'-2']]],'isolating filters')

def mod13(c):
    ar,ai=c
    v=(ar+5*ai)
    return (v.numerator*pow(v.denominator,-1,13))%13
# Since each original leading coefficient remains nonzero after this good reduction,
# coprime reductions prove no common root over Q(i).
g0={k:v for (k,l),v in a.g.items() if l==0}
b={k:a.cs(v,a.F(1,100)*(1 if k%2==0 else -1)) for (k,l),v in a.rpoly.items()}
A2=sum(mod13(a.cs(v,k*k))*x**(k+9) for k,v in g0.items())
B1=sum(mod13(a.cm(a.I,a.cs(v,k)))*x**(k+8) for k,v in b.items())
pa=s.Poly(A2,x,modulus=13);pb=s.Poly(B1,x,modulus=13);gcd=s.gcd(pa,pb)
a.need(gcd.degree()==0,'Hessian common-zero exclusion')
a.need(pa.degree()==18 and pb.degree()==16,'reduction preserves degrees')
slopes=[a.F(i,125) for i in (39212,39188,-48612,-49788)]
branch=[-a.F(j,1)/u for u in slopes for j in (4,8)]
a.need(len(set(branch))==8,'disjoint branch points')
report={'filters':selected,'hessian_gcd_mod13':str(gcd.as_expr()),'degrees':[pa.degree(),pb.degree()],
 'multiplier_branch_points':[str(v) for v in branch],
 'scope':'exact finite algebra; analytic continuations have separate proofs'}
(D/'filter_checks.json').write_text(json.dumps(report,indent=2)+'\n')
print('EXTRA_CHECKS',json.dumps(report,indent=2))
