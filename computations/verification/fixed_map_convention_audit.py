#!/usr/bin/env python3
"""Audit the uploaded fixed-map proposal; finite tests are not BGS evidence.

Run from the repository root with numpy and sympy installed.
The modular Weyl law and classical identities are also derived in the report.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import json
import numpy as np
import sympy as s


def weyl(N, a, b, ordinary=False):
    x = np.arange(N)
    A = np.zeros((N, N), complex)
    A[x, (x+a) % N] = np.exp(2j*np.pi*((b*(x+a*pow(2, -1, N))) % N)/N)
    return (-1 if a*b % 2 else 1)*A if ordinary else A


def convention_checks():
    rows = []
    for N in [5, 7, 9, 11, 21]:
        T = lambda a, b: weyl(N, a, b)
        W = lambda a, b: weyl(N, a, b, True)
        comm = T(1, 0)@T(0, 1)-T(0, 1)@T(1, 0)
        claimed = 2j*np.sin(np.pi/N)*T(1, 1)
        corrected_error = np.linalg.norm(comm+claimed, 2)
        assert corrected_error < 2e-13
        assert np.linalg.norm(comm-claimed, 2) > .1
        x = np.arange(N); X = x[:, None]; Y = x[None, :]
        U = np.exp(2j*np.pi*((-pow(8, -1, N)*(3*X*X-2*X*Y+3*Y*Y)) % N)/N)/np.sqrt(N)
        covariance_error = max(np.linalg.norm(U@T(a,b)@U.conj().T-T(3*a+4*b,2*a+3*b), 2)
                               for a,b in [(1,0),(0,1),(1,1)])
        assert covariance_error < 2e-13
        # Ordinary midpoint gauge has the ordinary sine, for integer labels.
        for a,b,c,d in [(1,0,0,1),(1,1,2,-1),(-2,3,1,2)]:
            error = np.linalg.norm(W(a,b)@W(c,d)-np.exp(1j*np.pi*(a*d-b*c)/N)*W(a+c,b+d),2)
            assert error < 2e-13
        # Compute hopping directly from Fourier coefficients of r, not midpoints.
        rc = {0:1,1:.5,-1:.5,7:-.5,-7:-.5,6:-.25,-6:-.25,8:-.25,-8:-.25}
        raw = sum(value*T(1,k) for k,value in rc.items())
        ordinary = sum(value*W(1,k) for k,value in rc.items())
        r = lambda q:(1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))
        assert np.max(abs(ordinary[x,(x+1)%N]-r((x+.5)/N))) < 5e-14
        rz = np.where(abs(raw[x,(x+1)%N]) < 1e-12)[0].tolist()
        oz = np.where(abs(ordinary[x,(x+1)%N]) < 1e-12)[0].tolist()
        assert len(rz) == (7 if N % 7 == 0 else 1)
        assert oz == [(N-1)//2]
        if N == 7:
            assert np.linalg.norm(raw,2) < 2e-13
            assert np.max(abs(r(x/N))) < 2e-13
            assert np.max(abs(np.cos(14*np.pi*x/N)-1)) < 2e-13
        rows.append(dict(N=N,correct_commutator_error=float(corrected_error),
                         covariance_error=float(covariance_error),raw_zero_edges=rz,
                         ordinary_zero_edges=oz))
    return rows


def classical_checks():
    q,p = s.symbols('q p',real=True)
    r = (1-s.cos(14*s.pi*q))*(1+s.cos(2*s.pi*q))
    f = s.cos(14*s.pi*q)+r/10+r*s.sin(2*s.pi*q)/100+r*(-3*s.cos(2*s.pi*p)+4*s.sin(2*s.pi*p))/500
    H=s.hessian(f,(q,p)); grad=s.Matrix([s.diff(f,x) for x in (q,p)])
    points=[(0,0),(0,s.Rational(1,2)),(s.Rational(1,2),0),(s.Rational(1,2),s.Rational(1,2))]
    coeffs=[s.Rational(n,125) for n in [-19894,-19306,24594,24606]]
    for point,coeff in zip(points,coeffs):
        sub=dict(zip((q,p),point))
        assert grad.subs(sub).applyfunc(s.simplify)==s.zeros(2,1)
        assert (H.subs(sub)/s.pi**2).applyfunc(s.simplify)==s.diag(coeff,0)
    x,y,z=s.symbols('x y z'); S=s.Matrix([[3,4],[2,3]])
    M=lambda t:S*s.Matrix([[1,0],[t,1]])
    assert s.expand(s.trace(M(z)*M(y)*M(x))-(198+140*(x+y+z)+96*(x*y+x*z+y*z)+64*x*y*z))==0
    # At zero kick the claimed local curvature 3/2 fails for period one.
    W=(3*q*q-2*q*p+3*p*p)/8
    assert s.diff(W.subs(p,q),q,2)==1
    return dict(fixed_hessian_coefficients=[str(c) for c in coeffs],period_three_polynomial=True,
                period_one_curvature=1)


def spacing_checks():
    a=.2
    def bump(x):
        y=(x-1)/a; result=np.zeros_like(y)
        inside=abs(y)<1
        result[inside]=np.exp(1-1/(1-y[inside]**2))
        return result
    def pair(phases):
        N=len(phases); d=N*(phases[:,None]-phases[None,:]); mask=~np.eye(N,dtype=bool)
        return sum(float(bump(d+N*n)[mask].sum()) for n in [-1,0,1])/N
    rows=[]
    for N in [8,16,32,64]:
        clock=np.arange(N)/N
        changed=clock+(-1.)**np.arange(N)*a/N
        cv,cu=pair(clock),pair(changed)
        assert abs(cv-1)<1e-12 and abs(cu)<1e-12
        eps=np.max(abs(np.exp(2j*np.pi*clock)-np.exp(2j*np.pi*changed)))
        assert abs(eps-2*np.sin(np.pi*a/N))<2e-14
        rows.append(dict(N=N,clock_pair=cv,perturbed_pair=cu,N_operator_error=float(N*eps)))
    return rows


if __name__=='__main__':
    print(json.dumps(dict(conventions=convention_checks(),classical=classical_checks(),
                          sharpness=spacing_checks()),indent=2))
