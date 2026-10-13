"""Finite TRACE-078 controls: exact rational Schur expansion and bounded
complex128 diagnostics. Dimensions 4 and 64; one BLAS thread, timeout 90 s,
memory below 1 GiB. These checks do not prove concentration or BGS."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from pathlib import Path
import json
import numpy as np
import sympy as sp

def exact():
    h=sp.Matrix([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]])/2
    p=h.applyfunc(lambda z:sp.simplify(z*sp.conjugate(z))); k=p*p; p3=k*p
    rows=[]
    for i,j in [(0,1),(1,3)]:
        for w in [sp.Integer(1),sp.Integer(-1),sp.I,-sp.I]:
            ss=0
            for e in range(4):
                if e in (i,j):continue
                keep=[l for l in range(4) if l!=e];q=w/(1-h[e,e]*w)
                sn=h.extract(keep,keep)+h.extract(keep,[e])*h.extract([e],keep)*q
                pn=sn.applyfunc(lambda z:sp.simplify(z*sp.conjugate(z)))
                change=sp.simplify((pn*pn)[keep.index(i),keep.index(j)]-k[i,j])
                aa=bb=cc=dd=ff=0
                for l in keep:
                    x,y=p[i,l],p[l,j];a=h[i,e]*h[e,l]*sp.conjugate(h[i,l]);b=h[l,e]*h[e,j]*sp.conjugate(h[l,j]);v=p[i,e]*p[e,l];d=p[l,e]*p[e,j]
                    aa+=y*a+x*b;bb+=x*d+y*v+a*sp.conjugate(b)+sp.conjugate(a)*b;cc+=a*b;dd+=a*d+b*v;ff+=v*d
                formula=-p[i,e]*p[e,j]+q*aa+sp.conjugate(q*aa)+q*sp.conjugate(q)*bb+q*q*cc+sp.conjugate(q*q*cc)+q*q*sp.conjugate(q)*dd+sp.conjugate(q*q*sp.conjugate(q)*dd)+(q*sp.conjugate(q))**2*ff
                assert sp.simplify(formula-change)==0
                ss+=change**2
            assert ss<=sp.Rational(2600,16)*(k[i,j]+p3[i,j])
            rows.append({'pair':[i,j],'phase':str(w),'sum_increment_squares':str(sp.simplify(ss))})
    return rows

def diagnostics():
    n=64;ii=np.arange(n);s=np.exp(2j*np.pi*np.outer(ii,ii)/n)/np.sqrt(n)
    r=np.eye(n);a=.21
    for l in range(0,n,2):r[l:l+2,l:l+2]=[[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]]
    s=s@r;p=abs(s)**2;k=p@p;p3=k@p;delta=float(p.max());assert delta<=.25
    results=[]
    for i,j in [(0,1),(3,17),(12,45)]:
        sums=[]
        for theta in [.17,1.23,3.61]:
            total=0
            for e in range(n):
                if e in [i,j]:continue
                keep=[v for v in range(n) if v!=e];w=np.exp(1j*(theta+e*.11));q=w/(1-s[e,e]*w)
                # Independent row/column feedback computation, no candidate coefficients.
                row=s[i,keep]+s[i,e]*s[e,keep]*q
                col=s[keep,j]+s[keep,e]*s[e,j]*q
                change=float(np.dot(abs(row)**2,abs(col)**2)-k[i,j]);total+=change**2
            rhs=2600*delta**2*(k[i,j]+p3[i,j]);assert total<=rhs
            sums.append(total/rhs)
        results.append({'pair':[i,j],'sum_to_bound_ratios':sums})
    return {'n':n,'delta':delta,'cases':results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result={'claim':'BGS-TRACE-078','exact_expansions':exact(),'floating_diagnostics':diagnostics(),'non_claim':'Finite controls; no concentration theorem or BGS proof.'}
    encoded = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
