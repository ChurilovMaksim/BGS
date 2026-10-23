#!/usr/bin/env python3
"""Finite controls for parameter-bandwidth de-averaging.

No BGS or physical parameter-moment limit is asserted.
Uses the exact matrix prescription at small sizes and explicitly labelled
control parameters. All checks stay active under python -O.
Dependencies: Python 3.10+, NumPy, SciPy. No network or repository writes.
"""
from __future__ import annotations
import itertools
import json
import math
import time
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
from typing import Iterable
import numpy as np
from scipy import integrate, linalg


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def profile(q: np.ndarray) -> np.ndarray:
    return (1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))


def model(n: int) -> tuple[np.ndarray, np.ndarray]:
    require(n >= 3 and n % 2 == 1, 'odd N >= 3 required')
    x = np.arange(n, dtype=np.int64)
    q = x/n
    r = profile(q)
    a = np.diag((np.cos(14*np.pi*q)+r/10+r*np.sin(2*np.pi*q)/100-0.1).astype(complex))
    upper = ((-3-4j)/5)*profile(((x+pow(2,-1,n)) % n)/n)/200
    a[x,(x+1)%n] += upper
    a[(x+1)%n,x] += upper.conjugate()
    xx = x[:,None]
    phase = (-pow(8,-1,n)*(3*xx*xx-2*xx*xx.T+3*xx.T*xx.T)) % n
    m = np.exp(2j*np.pi*phase/n)/np.sqrt(n)
    require(linalg.norm(a-a.conj().T) < 1e-12, 'A not Hermitian')
    require(linalg.norm(m@m.conj().T-np.eye(n)) < 1e-12, 'M not unitary')
    return a,m


def trace_polynomial(v: np.ndarray, m: int) -> dict[tuple[int,...],complex]:
    """Tr[(diag(z_j) V)^m], indexed by occupation vectors."""
    n = len(v)
    out: dict[tuple[int,...],complex] = defaultdict(complex)
    for path in itertools.product(range(n), repeat=m):
        count = tuple(path.count(j) for j in range(n))
        coeff = 1.0+0j
        for j in range(m):
            coeff *= v[path[j],path[(j+1)%m]]
        out[count] += coeff
    return dict(out)


def add_index(a: tuple[int,...], b: tuple[int,...]) -> tuple[int,...]:
    return tuple(x+y for x,y in zip(a,b))


def multiply(a: dict, b: dict) -> dict:
    c: dict[tuple[int,...],complex] = defaultdict(complex)
    for x,ax in a.items():
        for y,by in b.items():
            c[add_index(x,y)] += ax*by
    return dict(c)


def pair_polynomial(n: int, v: np.ndarray, max_m: int) -> dict:
    out: dict[tuple[int,...],complex] = defaultdict(complex)
    zero = (0,)*n
    for m in range(1,max_m+1):
        weight = 1.0/(m+1)  # finite algebra test, not a smooth BGS band
        p = trace_polynomial(v,m)
        for a,ca in p.items():
            for b,cb in p.items():
                index = tuple(x-y for x,y in zip(a,b))
                out[index] += weight*ca*cb.conjugate()/n**2
        out[zero] -= weight*min(m,n)/n**2
    return dict(out)


def frequencies(poly: dict, n: int, eigenvalues: np.ndarray) -> tuple[np.ndarray,np.ndarray]:
    indices = np.array(list(poly),dtype=int)
    return n*indices@eigenvalues, np.array(list(poly.values()),dtype=complex)


def evaluate(freq: np.ndarray, coeff: np.ndarray, t: float) -> complex:
    return complex(np.dot(coeff,np.exp(1j*t*freq)))


def direct_pair(a: np.ndarray, mcat: np.ndarray, t: float, max_m: int) -> float:
    n=len(a)
    u=linalg.expm(1j*t*n*a)@mcat
    power=np.eye(n,dtype=complex)
    value=0.0
    for m in range(1,max_m+1):
        power=power@u
        value += (abs(np.trace(power))**2-min(m,n))/(n*n*(m+1))
    return float(value)


def sinc_gram_integral(freq: np.ndarray, coeff: np.ndarray, left: float, right: float) -> float:
    """Integral |sum c exp(i gamma t)|^2 using the exact sinc Gram kernel."""
    length=right-left
    center=(left+right)/2
    rotated=coeff*np.exp(1j*freq*center)
    total=0j
    for lo in range(0,len(freq),128):
        hi=min(len(freq),lo+128)
        difference=freq[lo:hi,None]-freq[None,:]
        kernel=np.sinc(length*difference/(2*np.pi))
        total += np.sum(rotated[lo:hi,None]*rotated.conjugate()[None,:]*kernel)
    total *= length
    require(abs(total.imag)<2e-9,'sinc Gram integral has spurious imaginary part')
    require(total.real>-2e-9,'sinc Gram integral significantly negative')
    return float(total.real)


def physical_bandwidth_controls() -> dict:
    records=[]
    max_error=0.0
    moment_checks=[]
    for n,max_m in [(3,5),(5,3),(7,2)]:
        a,m=model(n)
        eigenvalues,basis=linalg.eigh(a)
        v=basis.conj().T@m@basis
        poly=pair_polynomial(n,v,max_m)
        freq,coeff=frequencies(poly,n,eigenvalues)
        bound=2*n*max_m*linalg.norm(a,2)
        require(float(np.max(np.abs(freq))) <= bound+1e-10,'frequency exceeds proved support')
        require(all(sum(index)==0 for index in poly),'nonneutral occupation difference')
        hermitian_error=max(abs(c-poly.get(tuple(-i for i in index),0).conjugate()) for index,c in poly.items())
        require(hermitian_error<1e-12,'nonreal formal pair function')
        for t in [0.0,0.0001,0.003,0.03,0.17,1.0]:
            value=evaluate(freq,coeff,t)
            direct=direct_pair(a,m,t,max_m)
            error=abs(value-direct)
            max_error=max(max_error,error)
            require(error<2e-11,'formal/direct pair mismatch')
        records.append({'N':n,'max_m':max_m,'number_formal_frequencies':len(poly),
                        'largest_frequency':float(np.max(np.abs(freq))),
                        'proved_frequency_upper_bound':float(bound),
                        'hermitian_coefficient_error':hermitian_error})
        if n==3:
            cube=multiply(multiply(poly,poly),poly)
            fc,cc=frequencies(cube,n,eigenvalues)
            for left,right in [(0.01,0.04),(0.1,0.35)]:
                gram=sinc_gram_integral(fc,cc,left,right)
                quadrature,err=integrate.quad(lambda t: abs(evaluate(freq,coeff,t))**6,left,right,
                                             epsabs=1e-13,epsrel=1e-11,limit=200)
                require(abs(gram-quadrature)<2e-10,'sixth parameter moment mismatch')
                moment_checks.append({'interval':[left,right], 'cube_frequency_count':len(cube),
                                      'sinc_Gram_integral':gram,'positive_quadrature':quadrature,
                                      'quadrature_error_estimate':err,'difference':abs(gram-quadrature)})
    return {'records':records,'max_direct_evaluation_error':max_error,
            'sixth_moment_checks':moment_checks,
            'boundary':'Small-size identities only; no asymptotic physical moment bound.'}


def kernel(x: float, r: int) -> float:
    if abs(x)<1e-13:
        return 2/np.pi
    return float(np.sin(2*x)/(np.pi*x)*np.sinc(x/(2*r*np.pi))**(2*r))


def reproducer_controls() -> dict:
    r=3
    cutoff=250.0
    tail=(2*r)**(2*r)/(np.pi*r)*cutoff**(-2*r)
    records=[]
    for freq in [-3.5,-1.0,-0.8,-0.25,0.0,0.45,0.95,1.0,3.5]:
        result,err=integrate.quad(lambda t:2*kernel(t,r)*np.cos(freq*t),0,cutoff,
                                  epsabs=2e-11,epsrel=2e-11,limit=1000)
        expected=1.0 if abs(freq)<=1 else 0.0
        require(abs(result-expected)<=tail+err+1e-9,'flat-top reproducer mismatch')
        records.append({'frequency':freq,'integral':result,'expected':expected,
                        'quadrature_error_estimate':err,'analytic_tail_upper_bound':tail})
    return {'kernel':'sin(2x)/(pi*x)*sinc(x/(2r))^(2r), unnormalized sinc','r':r,'records':records}


def central_exp_moment(k: int) -> int:
    return sum(math.comb(k,j)*(-1)**(k-j)*math.factorial(j) for j in range(k+1))


def exact_sixth_moment(coeff: list[F]) -> tuple[F,F]:
    moments=[F(1)]+[F(0)]*6
    for c in coeff:
        single=[F(central_exp_moment(j))*c**j for j in range(7)]
        moments=[sum(F(math.comb(j,l))*moments[l]*single[j-l] for l in range(j+1)) for j in range(7)]
    cumulant={j:F(math.factorial(j-1))*sum(c**j for c in coeff) for j in range(2,7)}
    via_cumulants=(cumulant[6]+15*cumulant[4]*cumulant[2]+10*cumulant[3]**2+15*cumulant[2]**3)
    return moments[6],via_cumulants


def cue_controls() -> dict:
    records=[]
    count=0
    for n in [14,28,56,112,224,448]:
        modes=list(range((n+13)//14,n//7+1))
        require(6*max(modes)<=n,'stable sixth moment premise fails')
        for form in [0,1,2]:
            weights=[F(1) if form==0 else F(n+m,n) if form==1 else F((-1)**m*(m+1),n) for m in modes]
            coeff=[w*F(m,n*n) for m,w in zip(modes,weights)]
            first,second=exact_sixth_moment(coeff)
            require(first==second,'sixth central moment/cumulant identity failed')
            require(first>=0,'negative sixth moment')
            count += 1
            if form==0:
                records.append({'N':n,'modes':[min(modes),max(modes)],'sixth_moment_exact':str(first),
                                'N_cubed_times_sixth':float(n**3*first)})
    return {'exact_checks':count,'records':records,
            'scope':'Exact CUE moment calibration uses Theorem 2.1 only when 6*max(mode)<=N.'}


def set_partitions(items: tuple[int,...]) -> Iterable[list[list[int]]]:
    if not items:
        yield []
        return
    first,*rest=items
    for partition in set_partitions(tuple(rest)):
        yield [[first]]+[block[:] for block in partition]
        for j in range(len(partition)):
            copy=[block[:] for block in partition]
            copy[j]=[first]+copy[j]
            yield copy


def determinant(a: list[list[F]]) -> F:
    n=len(a)
    a=[row[:] for row in a]
    result=F(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None:
            return F(0)
        if pivot!=j:
            a[j],a[pivot]=a[pivot],a[j]
            result=-result
        x=a[j][j]
        result*=x
        for k in range(j,n):
            a[j][k]/=x
        for i in range(j+1,n):
            f=a[i][j]
            for k in range(j,n):
                a[i][k]-=f*a[j][k]
    return result


def perm_sign(p: tuple[int,...]) -> int:
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))


def connected_on_pairs(p: tuple[int,...]) -> bool:
    r=len(p)//2
    graph=[set() for _ in range(r)]
    for i,j in enumerate(p):
        graph[i//2].add(j//2)
        graph[j//2].add(i//2)
    reached={0}
    stack=[0]
    while stack:
        i=stack.pop()
        for j in graph[i]-reached:
            reached.add(j)
            stack.append(j)
    return len(reached)==r


def connected_determinant_controls() -> dict:
    count=0
    records=[]
    for r in [1,2,3]:
        size=2*r
        for shift in [0,2,5]:
            a=[[F(1,shift+i+j+2) for j in range(size)] for i in range(size)]
            by_partitions=F(0)
            for pi in set_partitions(tuple(range(r))):
                term=F((-1)**(len(pi)-1)*math.factorial(len(pi)-1))
                for block in pi:
                    labels=[x for b in block for x in (2*b,2*b+1)]
                    term*=determinant([[a[i][j] for j in labels] for i in labels])
                by_partitions+=term
            by_connected=F(0)
            terms=0
            for perm in itertools.permutations(range(size)):
                if connected_on_pairs(perm):
                    term=F(perm_sign(perm))
                    for i,j in enumerate(perm):
                        term*=a[i][j]
                    by_connected+=term
                    terms+=1
            require(by_partitions==by_connected,'connected determinantal cumulant identity failed')
            records.append({'pair_groups':r,'shift':shift,'connected_permutations':terms,'exact_value':str(by_connected)})
            count+=1
    return {'exact_checks':count,'records':records,
            'scope':'Checks disjoint-position cumulant combinatorics; no test alone proves asymptotic cluster bounds.'}


def spike_controls() -> dict:
    m=6
    rational=F(sum((-1)**k*math.comb(2*m,k)*(m-k)**(2*m-1) for k in range(m+1)),math.factorial(2*m-1))
    integral_sinc=float(rational)*np.pi
    numeric,err=integrate.quad(lambda x:np.sinc(x/np.pi)**12,-150,150,epsabs=1e-12,limit=1000)
    require(abs(numeric-integral_sinc)<2e-10,'sinc spike integral mismatch')
    finite_spikes=[]
    for n in [2,3,5,8,16]:
        length=n*n
        coeffs=[1]
        for _ in range(6):
            nxt=[0]*(len(coeffs)+length-1)
            for i,a in enumerate(coeffs):
                for j in range(length):
                    nxt[i+j]+=a
            coeffs=nxt
        mean=F(sum(c*c for c in coeffs),length**12)
        grid=12*length+1
        t=2*np.pi*np.arange(grid)/grid
        val=np.ones(grid)
        val[1:]=(np.sin(length*t[1:]/2)/(length*np.sin(t[1:]/2)))**12
        measured=float(np.mean(val))
        require(abs(measured-float(mean))<2e-13,'finite Fejer spike moment mismatch')
        finite_spikes.append({'N':n,'bandwidth':length-1,'peak':1,
                             'sixth_period_mean_exact':str(mean),
                             'N_squared_times_mean':float(length*mean),
                             'trapezoid_error':abs(measured-float(mean))})
    return {'finite_exponential_polynomial_spikes':finite_spikes,
            'sinc12_integral_over_pi_exact':str(rational),'sinc12_integral':integral_sinc,
            'quadrature':numeric,'quadrature_error_estimate':err,
            'Omega_times_integral_F_to_sixth':2*integral_sinc,
            'definition':'F(t)=sinc(Omega*(t-t0)/2)^2; sup F=F(t0)=1; Fourier support [-Omega,Omega]',
            'meaning':'An O(Omega^-1) local qth moment need not force pointwise decay.'}


def main() -> None:
    started=time.perf_counter()
    out={'status':'Finite controls; NO physical sixth parameter-moment estimate or BGS proof.',
         'physical_bandwidth':physical_bandwidth_controls(),
         'flat_top_reproducer':reproducer_controls(),
         'stable_CUE_sixth_moments':cue_controls(),
         'connected_determinant_identity':connected_determinant_controls(),
         'sharpness_spike':spike_controls(),
         'python_O_safe_checks':True,'runtime_seconds':time.perf_counter()-started}
    path=Path(__file__).with_name('verification.json')
    path.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({'output':str(path),'runtime_seconds':out['runtime_seconds'],
                      'max_pair_polynomial_error':out['physical_bandwidth']['max_direct_evaluation_error'],
                      'exact_CUE_checks':out['stable_CUE_sixth_moments']['exact_checks'],
                      'connected_diagram_checks':out['connected_determinant_identity']['exact_checks']},indent=2))


if __name__=='__main__':
    main()
