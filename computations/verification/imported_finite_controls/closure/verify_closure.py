#!/usr/bin/env python3
"""Finite checks of the BGS hierarchy-to-Laplace bridge.

These tests verify algebraic identities and finite inequalities only.
They do not prove the signed hierarchy for the frozen BGS operator.
Run: python -O verify_closure.py --output verification.json
Dependencies: Python 3, NumPy. No network access or repository writes.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def elementary(values):
    zero = values[0] * 0 if len(values) else 0
    out = [zero + 1] + [zero] * len(values)
    for i, value in enumerate(values):
        for k in range(i + 1, 0, -1):
            out[k] += value * out[k - 1]
    return out


def coefficient(e, k):
    return e[k] if k < len(e) else 0


def partitions(n):
    if n == 0:
        return [()]
    ans = []
    for part in partitions(n - 1):
        ans.append(part + ((n - 1,),))
        for i in range(len(part)):
            ans.append(part[:i] + (part[i] + (n - 1,),) + part[i+1:])
    return ans


def mobius_trace(modes, traces, parts):
    result = 0j
    for part in parts:
        term = 1 + 0j
        for block in part:
            size = len(block)
            term *= ((-1) ** (size - 1)) * math.factorial(size - 1)
            term *= traces[sum(modes[i] for i in block)]
        result += term
    return result


def test_exact_bonferroni():
    count = 0
    for n in range(7):
        for xs in itertools.product((Fraction(0), Fraction(1,3), Fraction(3,4), Fraction(1)), repeat=n):
            e = elementary(xs)
            product = math.prod(1-x for x in xs)
            for order in (1,3,5,7):
                upper = sum((-1)**k * coefficient(e,k) for k in range(order))
                lower = upper - coefficient(e,order)
                require(lower <= product <= upper, 'Bonferroni bracket failed')
                count += 1
    rng = np.random.default_rng(145025)
    for _ in range(500):
        xs = [Fraction(int(v),20) for v in rng.integers(0,21,size=8)]
        ys = [Fraction(int(v),20) for v in rng.integers(0,21,size=8)]
        e,f = elementary(xs),elementary(ys)
        px,py = math.prod(1-x for x in xs),math.prod(1-y for y in ys)
        for order in (1,3,5,7,9):
            bound = sum(abs(coefficient(e,k)-coefficient(f,k)) for k in range(1,order+1)) + coefficient(f,order)
            require(abs(px-py) <= bound, 'Finite comparison certificate failed')
            count += 1
    return count


def test_stirling():
    s = [[0]*13 for _ in range(13)]
    s[0][0]=1
    for r in range(1,13):
        for k in range(1,r+1):
            s[r][k] = s[r-1][k-1]+k*s[r-1][k]
    count=0
    for x in range(81):
        for r in range(1,13):
            falling=1
            total=0
            for k in range(1,r+1):
                falling *= x-k+1
                total += s[r][k]*falling
            require(total == x**r,'Stirling moment identity failed')
            count += 1
    return count


def actual_bgs(n: int, tau: float):
    require(n >= 3 and n % 2 == 1,'Odd dimension is required')
    x=np.arange(n)
    q=x/n
    profile=lambda u: (1-np.cos(14*np.pi*u))*(1+np.cos(2*np.pi*u))
    rr=profile(q)
    diag=np.cos(14*np.pi*q)+rr/10+rr*np.sin(2*np.pi*q)/100-0.1
    h=(n+1)//2
    beta=complex(-3,-4)/1000 * profile(((x+h)%n)/n)
    a=np.diag(diag.astype(complex))
    a[x,(x+1)%n]+=beta
    a[(x+1)%n,x]+=beta.conjugate()
    xx=x[:,None]; yy=x[None,:]
    exponent=(-pow(8,-1,n)*(3*xx*xx-2*xx*yy+3*yy*yy))%n
    m=np.exp(2j*np.pi*exponent/n)/np.sqrt(n)
    vals,vecs=np.linalg.eigh(a)
    kick=(vecs*np.exp(1j*tau*n*vals))@vecs.conj().T
    u=kick@m
    require(np.linalg.norm(a-a.conj().T)<1e-12,'Generator not Hermitian')
    require(np.linalg.norm(u.conj().T@u-np.eye(n))<1e-10,'Unitarity failed')
    return u


def test_fourier_and_toeplitz():
    rng=np.random.default_rng(640215)
    qhat={0:0.21,1:0.055,-1:0.055,2:0.035,-2:0.035,3:0.012,-3:0.012}
    deg=max(abs(m) for m in qhat)
    records=[]
    max_fourier=max_pair=max_certificate=0.0
    cases=[]
    for n in (3,5,7,9,11,19):
        cases.append((f'frozen_form_proxy_N{n}', actual_bgs(n,0.03)))
    for n in (4,7,9):
        cases.append((f'clock_N{n}',np.diag(np.exp(2j*np.pi*np.arange(n)/n))))
        cases.append((f'cluster_N{n}',np.eye(n,dtype=complex)))
        cases.append((f'arbitrary_N{n}',np.diag(np.exp(2j*np.pi*rng.random(n)))))
    for name,u in cases:
        n=len(u)
        phases=np.angle(np.linalg.eigvals(u))/(2*np.pi)
        maxk=4
        traces={0:complex(n)}
        power=np.eye(n,dtype=complex)
        for m in range(1,maxk*deg+1):
            power=power@u
            traces[m]=np.trace(power)
            traces[-m]=np.conjugate(traces[m])
        grid=np.arange(2*n*deg+3)/(2*n*deg+3)
        emean=np.zeros(n+1)
        zmean=0.0
        for origin in grid:
            hvals=sum(c*np.exp(2j*np.pi*m*(phases-origin)) for m,c in qhat.items()).real
            require(np.min(hvals)>=-1e-12 and np.max(hvals)<=1+1e-12,'Invalid positive test')
            emean += np.array(elementary(list(hvals)),float)/len(grid)
            zmean += float(np.prod(1-hvals))/len(grid)
        errors=[]
        for k in range(1,min(maxk,n)+1):
            total=0j
            parts=partitions(k)
            for free in itertools.product(qhat,repeat=k-1):
                last=-sum(free)
                if last not in qhat: continue
                modes=free+(last,)
                weight=math.prod(qhat[m] for m in modes)
                total += weight*mobius_trace(modes,traces,parts)
            moment=total/math.factorial(k)
            error=abs(moment-emean[k])
            errors.append(float(error))
            max_fourier=max(max_fourier,float(error))
            require(error<2e-8,'Fourier-Mobius identity failed')
        toeplitz=np.array([[qhat.get(i-j,0.0) for j in range(n)] for i in range(n)])
        eigs=np.linalg.eigvalsh(toeplitz)
        require(np.min(eigs)>-1e-12 and np.max(eigs)<1+1e-12,'Reference positivity failed')
        ecue=np.array(elementary(list(eigs)),float)
        cue_product=float(np.linalg.det(np.eye(n)-toeplitz))
        pair_formula=0.5*(qhat[0]**2*n*(n-1)+sum(abs(c)**2*(min(abs(m),n)-n) for m,c in qhat.items() if m))
        pair_error=abs(pair_formula-ecue[2])
        max_pair=max(max_pair,pair_error)
        require(pair_error<1e-10,'CUE Toeplitz pair benchmark failed')
        for order in (1,3,5,7):
            observed=abs(zmean-cue_product)
            rhs=sum(abs(coefficient(emean,k)-coefficient(ecue,k)) for k in range(1,order+1))+coefficient(ecue,order)
            violation=max(0.0,observed-rhs)
            max_certificate=max(max_certificate,violation)
            require(violation<2e-10,'Integrated finite-N comparison bound failed')
            h=n*qhat[0]
            require(coefficient(ecue,order)<=h**order/math.factorial(order)+1e-10,'Reference tail failed')
        records.append({'case':name,'fourier_errors_k1_to_k4':errors,'cue_pair_error':pair_error,'laplace_defect':abs(zmean-cue_product)})
    return {'cases':records,'max_fourier_error':max_fourier,'max_cue_pair_error':max_pair,'max_certificate_violation':max_certificate}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='verification.json')
    args=parser.parse_args()
    exact_count=test_exact_bonferroni()
    stirling_count=test_stirling()
    numeric=test_fourier_and_toeplitz()
    tails={}
    for h in (1,2,4):
        order=1
        while h**order/math.factorial(order)>1e-6:
            order += 2
        tails[str(h)]={'odd_order':order,'tail_upper_bound':h**order/math.factorial(order)}
    payload={
      'status':'PASS',
      'scope':'Finite algebra and inequality checks; NOT a proof of the BGS hierarchy.',
      'model_computations':'Exact BGS matrix formula at proxy tau=0.03 for finite identity checks only.',
      'bonferroni_and_comparison_checks_exact':exact_count,
      'stirling_checks_exact':stirling_count,
      'numeric':numeric,
      'illustrative_reference_tails':tails,
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }
    Path(args.output).write_text(json.dumps(payload,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in payload.items() if k!='numeric'},indent=2))
    print(json.dumps({k:v for k,v in numeric.items() if k!='cases'},indent=2))

if __name__=='__main__':
    main()
