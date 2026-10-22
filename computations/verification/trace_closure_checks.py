#!/usr/bin/env python3
"""Exact finite checks for TRACE-109/112/113 closure, not asymptotic certificates.

Standard-library rational arithmetic checks the four discrete stationary
classes, symbol values/Hessians, canonical determinant and error exponents.
No proxy coupling or finite spectrum is substituted for tau=10^-80.
Assertions are explicit and remain active with python -O.
"""
from fractions import Fraction as F
import json
from physical_kick_trace_checks import polyadd,polymul,scaled,cosine,add,scale

def require(ok,label):
    if not ok:raise RuntimeError(label)

def symbol():
    one={(0,0):(F(1),F(0))}
    r=polymul(polyadd(one,scaled(cosine(7),-1)),polyadd(one,cosine(1)))
    sinq={(1,0):(F(0),F(-1,2)),(-1,0):(F(0),F(1,2))}
    cosp={(0,1):(F(-3,10),F(-2,5)),(0,-1):(F(-3,10),F(2,5))}
    native=polyadd(cosine(7),scaled(r,F(1,10)),scaled(polymul(r,sinq),F(1,100)),
                   scaled(polymul(r,cosp),F(1,100)),scaled(one,F(-1,10)))
    return {v:scale(z,-1 if (v[0]*v[1])%2 else 1) for v,z in native.items()}

def evaluate(poly,q,p,dk=0,dl=0):
    # Returns the derivative divided by (2*pi*i)^(dk+dl).
    z=(F(0),F(0))
    for (k,l),c in poly.items():
        exponent=2*(k*q+l*p)
        require(exponent.denominator==1,'non-sign evaluation point')
        z=add(z,scale(c,(-1 if int(exponent)%2 else 1)*k**dk*l**dl))
    return z

def main():
    poly=symbol();rows=[]
    specs=[(F(0),0,0,F(0),F(0),F(9,10),F(-19606,125)),
           (F(0),2,-1,F(1,2),F(1,2),F(9,10),F(-19594,125)),
           (F(1,2),1,-1,F(0),F(3,4),F(-11,10),F(24306,125)),
           (F(1,2),3,-2,F(1,2),F(3,4),F(-11,10),F(24894,125))]
    for q,m,n,p,phase,value,hess in specs:
        s=q+m;F0=-(3*q*q-2*q*s+3*s*s)/8
        FQ=(-3*q+s)/4;Fs=(q-3*s)/4
        require(FQ+Fs==n,'stationary alias')
        require((-Fs)%1==p,'initial momentum')
        require((F0-n*q)%1==phase,'critical phase')
        require(evaluate(poly,q,p)==(value,0),'symbol value')
        require(evaluate(poly,q,p,1)==(0,0) and evaluate(poly,q,p,0,1)==(0,0),'equilibrium')
        require(scale(evaluate(poly,q,p,2),-4)==(hess,0),'Hessian/pi^2')
        require(evaluate(poly,q,p,0,2)==(0,0) and evaluate(poly,q,p,1,1)==(0,0),'rank-one Hamiltonian Hessian')
        trace_tau_pi=-2*hess
        expected=[F(39212,125),F(39188,125),F(-48612,125),F(-49788,125)][len(rows)]
        require(trace_tau_pi==expected,'monodromy trace coefficient')
        rows.append({'q':str(q),'sheet':m,'alias':n,'p_mod1':str(p),
                     'phase_mod1':str(phase),'a':str(value),'a_qq_over_pi2':str(hess)})
    # A nontrivial family of generating-function Hessians, including unequal
    # diagonal entries; no eigenphase differentiation or symmetry is assumed.
    cases=0
    for i in range(-3,4):
        for j in range(-3,4):
            aa=F(-3,4)+F(i,100);bb=F(1,4);cc=F(-3,4)+F(j,100)
            D=[[-cc/bb,-1/bb],[(bb*bb-aa*cc)/bb,-aa/bb]]
            require(D[0][0]*D[1][1]-D[0][1]*D[1][0]==1,'canonical determinant')
            require(aa+2*bb+cc==bb*(2-D[0][0]-D[1][1]),'stationary Jacobian normalization');cases+=1
    # Compare the four ordinary Gauss sheets to the native modular matrix
    # exactly in Q(sqrt(2),i), including negative/lifted indices and wraps.
    roots=[(F(1),F(0),F(0),F(0)),(F(0),F(1,2),F(0),F(1,2)),
           (F(0),F(0),F(1),F(0)),(F(0),F(-1,2),F(0),F(1,2)),
           (F(-1),F(0),F(0),F(0)),(F(0),F(-1,2),F(0),F(-1,2)),
           (F(0),F(0),F(-1),F(0)),(F(0),F(1,2),F(0),F(-1,2))]
    gauss_cases=0
    for n in range(3,100,2):
        labels=range(n) if n<=15 else [-1,0,1,n//2,n-1,n,n+1]
        for x in labels:
            for y in labels:
                native=F(-pow(8,-1,n)*(3*x*x-2*x*y+3*y*y),n)
                total=[F(0)]*4
                for sheet in range(4):
                    yy=y+n*sheet
                    phase=F(3*n,8)-F(3*x*x-2*x*yy+3*yy*yy,8*n)
                    relative=8*(phase-native)
                    require(relative.denominator==1,'Gauss sheet relative eighth root')
                    total=[a+b for a,b in zip(total,roots[int(relative)%8])]
                require(total==[2,0,0,0],'native odd Gauss identity with wrap')
                gauss_cases+=1
    # Symbolic powers of N in the Hilbert--Schmidt and cutoff error budgets.
    entry=F(-5,2);hs=entry+1;trace=hs+F(1,2)
    require(hs==F(-3,2) and trace==-1,'one-step trace error scale')
    alpha=F(1,5)
    require(-alpha==-1+4*alpha and -2+8*alpha==F(-2,5),'localization exponent')
    theta=F(7999,8000)
    # Exact verification of the telescoping bound's geometric inequality.
    for m in [1,2,3,20,100]:
        require(m*theta**(m-1)<=sum(theta**j for j in range(m))<=8000,'uniform displacement budget')
    require(F(24,16)==F(3,2),'protected A bound')
    require(F(48612+49788,16)==6150,'protected B bound')
    require(F(11,10)*6150-F(9,10)*F(3,2)==F(135273,20),'inserted lower coefficient')
    print(json.dumps({'result':'PASS','arithmetic':'exact rational and complex-rational Fourier algebra',
          'stationary_classes':rows,'canonical_Hessian_cases':cases,'odd_dimensions':49,'exact_Gauss_matrix_entries':gauss_cases,
          'matrix_error':'HS O(N^-3/2), trace O(N^-1)',
          'displacement_uniform_coarse_bound':'8e-53 (analytic trace-norm input is not certified by this check)',
          'asymptotic_theorem_established_by_finite_checks':False},indent=2))

if __name__=='__main__':main()
