import json
from fractions import Fraction as F
from pathlib import Path
import sys
import numpy as np


def main(target):
    cases=0
    for a in [F(j,3) for j in range(-12,13)]:
        for b in [F(j,5) for j in range(-12,13)]:
            d=a*b-1
            if not d:continue
            X=[[-b/d,-1/d],[-1/d,-a/d]]
            H=[[-a,F(1)],[F(1),-b]]
            product=[[sum(H[i][k]*X[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
            assert product==[[1,0],[0,1]]
            assert X[0][0]-X[1][1]==(a-b)/d
            cases+=1
    # Each of the first three real sources is PSD, as a sum of u u^T.
    sources=[[[1,0],[0,0]],[[1,0],[0,1]],[[1,1],[1,1]]]
    source_parameters=[]
    for A in sources:
        center=F(A[0][1]+A[1][0],2)
        scale=F(A[0][0]+A[1][1],2)
        assert scale>0
        source_parameters.append((center,scale))
    assert source_parameters==[(F(0),F(1,2)),(F(0),F(1)),(F(1),F(1))]
    # Exact rational squared-derivative reductions used by the two density
    # antiderivatives; positivity selects the square-root signs in the proof.
    derivative_cases=0
    for q in [F(j,17) for j in range(1,17)]:
        for w in [F(j,19) for j in range(1,19)]:
            left=F(1,1)/(1-q*q)/(1+q*q*w*w/(1-q*q))
            assert left==1/(1-q*q+q*q*w*w)
            derivative_cases+=1
    for q in [1+F(j,17) for j in range(1,17)]:
        for w in [F(j,19) for j in range(1,19)]:
            left=1/(q*q*(q*q-1))/(1+w*w/(q*q-1))
            assert left==1/(q*q*(q*q-1+w*w))
            derivative_cases+=1
    diagnostics=[]
    for L in (256,512):
        t=np.tan(np.pi*((np.arange(L)+1/3)/L-1/2))[:,None]
        r=np.tan(np.pi*((np.arange(L)+1/7)/L-1/2))[None,:]
        det=t*r-1
        for j,A in enumerate(sources):
            numer=-A[0][0]*r-A[1][1]*t-A[0][1]-A[1][0]
            z=0.3+1.2j
            value=np.mean(det/(numer-z*det))
            a,b=source_parameters[j];expected=1/(complex(float(a),-float(b))-z)
            error=abs(value-expected)
            assert error<0.005,(L,j,error)
            diagnostics.append({'grid':L,'source_index':j,'observed':[value.real,value.imag],
                                'formula':[expected.real,expected.imag],'absolute_error':error})
    out={'status':'passed_rational_finite_algebra_and_bounded_quadrature_diagnostics',
         'exact_inverse_cases':cases,'exact_antiderivative_reduction_cases':derivative_cases,
         'positive_sources':3,'quadrature':diagnostics,
         'max_quadrature_error':max(x['absolute_error'] for x in diagnostics),
         'scope':'Finite exact Q algebra. NumPy float64 quadrature is diagnostic, not a certificate of the all-dimensional analytic theorem.',
         'signed_density_zero':'2/pi^2','signed_tail_constant':'4/pi^2',
         'surrogate_signed_density_zero':'1/pi','surrogate_signed_tail_constant':'2/pi'}
    Path(target).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'max_quadrature_error':out['max_quadrature_error']}))


if __name__=='__main__':main(sys.argv[1])
