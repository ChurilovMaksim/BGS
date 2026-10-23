import json
from pathlib import Path
import sys
import sympy as sp
import numpy as np


def main(target):
    a,b=sp.symbols('a b', real=True)
    S=sp.Matrix([[0,1],[1,0]])
    H=S-sp.diag(a,b)
    X=H.inv()
    assert S*S==sp.eye(2)
    assert X==sp.Matrix([[-b,-1],[-1,-a]])/(a*b-1)
    A0=sp.diag(1,-1)
    assert sp.simplify(sp.trace(A0*X)-(a-b)/(a*b-1))==0
    alpha,beta=sp.symbols('alpha beta', real=True)
    trig=(sp.sin(alpha)*sp.cos(beta)-sp.sin(beta)*sp.cos(alpha))/(sp.sin(alpha)*sp.sin(beta)-sp.cos(alpha)*sp.cos(beta))
    assert sp.trigsimp(trig+sp.sin(alpha-beta)/sp.cos(alpha+beta))==0
    q,w=sp.symbols('q w', positive=True)
    F1=sp.asinh(q*w/sp.sqrt(1-q*q))/q
    assert sp.simplify(sp.diff(F1,w)-1/sp.sqrt(1-q*q+q*q*w*w))==0
    F2=sp.asinh(w/sp.sqrt(q*q-1))/q
    assert sp.simplify(sp.diff(F2,w)-1/(q*sp.sqrt(q*q-1+w*w)))==0
    assert sp.limit(sp.atanh(q)/q,q,0)==1
    pi=sp.pi
    assert sp.simplify(2/pi**2-1/pi)!=0
    assert sp.simplify(4/pi**2-2/pi)!=0
    checks=[]
    matrices=[sp.diag(1,0),sp.eye(2),sp.ones(2),sp.Matrix([[1,sp.I],[-sp.I,1]])]
    for A in matrices:
        assert A==A.H and all(ev>=0 for ev in A.eigenvals())
        qc=sp.simplify(sp.trace(A*(S+sp.I*sp.eye(2)).inv()))
        assert sp.simplify(qc-sp.trace(A*S)/2+sp.I*sp.trace(A)/2)==0
        checks.append({'A':str(A),'cauchy_parameter':str(qc)})
    diagnostic=[]
    for L in (256,512):
        u=np.pi*((np.arange(L)+1/3)/L-1/2)
        v=np.pi*((np.arange(L)+1/7)/L-1/2)
        t=np.tan(u)[:,None];r=np.tan(v)[None,:]
        det=t*r-1
        for j,A in enumerate(matrices):
            # trace(A X) = [-A00*r-A11*t-A01-A10]/det.
            numer=-complex(A[0,0])*r-complex(A[1,1])*t-complex(A[0,1]+A[1,0])
            z=0.3+1.2j
            value=np.mean(det/(numer-z*det))
            qc=complex(sp.trace(A*S)/2-sp.I*sp.trace(A)/2)
            expected=1/(qc-z)
            error=abs(value-expected)
            assert error<0.005,(L,j,error)
            diagnostic.append({'grid':L,'A_index':j,'observed':[value.real,value.imag],
                               'formula':[expected.real,expected.imag],'absolute_error':error})
    out={'status':'passed_exact_algebra_and_bounded_quadrature_diagnostics',
         'exact_checks':['2x2 involution and inverse','signed projection','torus identity',
                         'two density antiderivative derivatives','density at zero',
                         'distinct signed density and tail constants','four positive-source parameters'],
         'positive_source_cases':checks,'quadrature':diagnostic,
         'scope':'Exact finite algebra; quadrature is deterministic floating diagnostic with tolerance 0.005, not a proof of the all-dimension contour theorem.',
         'signed_density_zero':'2/pi^2','signed_tail_constant':'4/pi^2',
         'surrogate_signed_density_zero':'1/pi','surrogate_signed_tail_constant':'2/pi'}
    Path(target).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'max_quadrature_error':max(x['absolute_error'] for x in diagnostic)}))


if __name__=='__main__':main(sys.argv[1])
