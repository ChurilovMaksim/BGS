#!/usr/bin/env python3
"""Exact coefficient checks and finite numerical echo comparisons.

These tests distinguish intermediate times, negative times and repeated
cycles. Finite traces are recorded without asserting they equal their limits.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from pell_floquet_regression import design, weyl, hermitian_exponential as expi


def odd_basis(n: int) -> np.ndarray:
    """Orthonormal parity-odd basis in the full position space."""
    d = (n-1)//2
    q = np.zeros((n, d))
    j = np.arange(1, d+1)
    q[j, j-1] = 1/math.sqrt(2)
    q[n-j, j-1] = -1/math.sqrt(2)
    assert np.max(abs(q.T@q-np.eye(d))) < 1e-14
    return q


def hs(a: np.ndarray) -> float:
    """Normalized Hilbert--Schmidt norm on the spectral block."""
    return float(np.linalg.norm(a, 'fro')/math.sqrt(a.shape[0]))


def weights(k: int, t: int) -> list[int]:
    m,s=divmod(t,k)
    return [m+int(j<s) for j in range(k)]


def covariance(k: int, t: int, u: int) -> Q:
    m,s=divmod(t,k)
    n,r=divmod(u,k)
    return Q(m*n)+m*Q(r,k)+n*Q(s,k)+Q(min(s,r),k)


def exact_checks() -> dict:
    coefficients=0
    covariances=0
    for k in (3,5,7,11,13,17,23,47,101):
        c=[Q(k-1-2*j,2*k) for j in range(k)]
        times=sorted(set((-2*k-1,-k,-k+1,-1,0,1,k//2,k-1,k,k+1,3*k//2,2*k+1)))
        for t in times:
            w=weights(k,t)
            assert all(c[j]+Q(t,k)-c[(j-t)%k]==w[j] for j in range(k))
            coefficients+=k
            for u in times:
                z=weights(k,u)
                assert sum(Q(x*y,k) for x,y in zip(w,z))==covariance(k,t,u)
                covariances+=1
        # Recurrence cycles repeat the same noise: 3/2 has variance 5/2.
        # Use even denominator for this auxiliary coefficient identity only;
        # no even-period quantum theorem is claimed.
    assert covariance(2,3,3)==Q(5,2)
    assert covariance(2,1,1)==Q(1,2)
    assert covariance(2,-3,-3)==Q(5,2)
    return {'coefficient_identities':coefficients,'gram_identities':covariances,
            'half_period_variance':'1/2','three_half_period_variance':'5/2',
            'arithmetic':'exact rational','passed':True}


def dense_checks() -> list[dict]:
    rows=[]
    for k in (3,5,7):
        n,f,h=design(k)
        q=odd_basis(n)
        d=q.shape[1]
        full_u=np.eye(n,dtype=complex)[(h*np.arange(n))%n]
        u=q.conj().T@full_u@q
        w=weyl(n,(-f)%n,1)
        b=q.conj().T@(w+w.conj().T)@q
        orbit=[]
        bj=b.copy()
        for _ in range(k):
            orbit.append(bj)
            bj=u@bj@u.conj().T
        c=np.asarray([(k-1-2*j)/(2*k) for j in range(k)])
        avg=sum(orbit)/k
        g=sum(c[j]*orbit[j] for j in range(k))
        xc=g/math.sqrt(2*k)
        xone=sum(orbit)/math.sqrt(2*k)
        for tau in (.5,1.0):
            epsilon=tau/math.sqrt(2*k)
            kicked=expi(b,epsilon)@u
            v=expi(g,-epsilon)
            normal_step=hs(v@kicked@v.conj().T-expi(avg,epsilon)@u)
            for t in sorted(set((-k-1,-1,0,k//2,k-1,k,k+1,3*k//2,2*k))):
                alpha=t/k
                shifted=sum(c[(j-t)%k]*orbit[j] for j in range(k))/math.sqrt(2*k)
                xw=sum(weight*bj for weight,bj in zip(weights(k,t),orbit))/math.sqrt(2*k)
                assert hs(xc+alpha*xone-shifted-xw)<2e-11
                echo=np.linalg.matrix_power(kicked,t)@np.linalg.matrix_power(u,-t)
                triple=expi(xc,tau)@expi(xone,tau*alpha)@expi(shifted,-tau)
                single=expi(xw,tau)
                first_error=hs(echo-triple)
                second_error=hs(triple-single)
                comm1=xc@(alpha*xone)-(alpha*xone)@xc
                combined=xc+alpha*xone
                comm2=combined@shifted-shifted@combined
                second_bound=tau*tau*.5*(hs(comm1)+hs(comm2))
                assert first_error<=abs(t)*normal_step+2e-10
                assert second_error<=second_bound+2e-10
                assert hs(echo-single)<=abs(t)*normal_step+second_bound+3e-10
                variance=float(covariance(k,t,t))
                trace=complex(np.trace(echo)/d)
                trace2=complex(np.trace(echo@echo)/d)
                rows.append({'K':k,'N':n,'dimension':d,'tau':tau,'time':t,
                    'alpha':alpha,'variance':variance,'normal_step_error':normal_step,
                    'echo_to_triple_error':first_error,
                    'triple_to_single_error':second_error,
                    'generic_duhamel_bound':second_bound,
                    'echo_trace':[trace.real,trace.imag],
                    'echo_second_trace':[trace2.real,trace2.imag],
                    'limiting_trace_prediction':math.exp(-tau*tau*variance/2),
                    'limiting_second_trace_prediction':math.exp(-2*tau*tau*variance),
                    'scope':'finite numerical mechanism check below K=11; does not assert the uniform arithmetic constant or asymptotic equality here'})
    return rows


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--exact-only',action='store_true')
    args=parser.parse_args()
    data={'producer':'computations/verification/pell_weighted_echo_regression.py',
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'scope':'Exact finite coefficient/covariance identities and numerical operator comparisons, not a formal proof or priority certificate.',
          'exact':exact_checks(),'passed':True}
    if not args.exact_only:
        data['dense']=dense_checks()
    text=json.dumps(data,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    else:
        print(text,end='')


if __name__=='__main__':
    main()
