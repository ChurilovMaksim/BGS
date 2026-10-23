#!/usr/bin/env python3
"""Finite checks of contractive radial secular observables.

No BGS asymptotic is inferred. Proxy couplings are labelled explicitly.
Dependencies: numpy, scipy. Checks remain active under python -O.
"""
from __future__ import annotations
import argparse
import json
import math
import time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.linalg import eigh, schur, toeplitz
from scipy.integrate import quad


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def determinant_fraction(a: list[list[F]]) -> F:
    a = [row[:] for row in a]
    out = F(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            out = -out
        p = a[j][j]
        out *= p
        for i in range(j + 1, len(a)):
            f = a[i][j] / p
            for k in range(j + 1, len(a)):
                a[i][k] -= f * a[j][k]
    return out


def kernel_q(x, s: float, t: float):
    x = np.asarray(x)
    return .5 * np.log1p((t*t - s*s)/(s*s + (2*np.pi*x)**2))


def periodic_q(x, n: int, s: float, t: float):
    x = np.asarray(x)
    ss = np.sinh(s/(2*n))**2
    dd = np.sinh(t/(2*n))**2 - ss
    return .5 * np.log1p(dd/(ss + np.sin(np.pi*x/n)**2))


def radial_values(phases, origins, s: float, t: float):
    """F=e^{-(t-s)} |p(e^{-s/N-i2pi alpha})/p(e^{-t/N-i2pi alpha})|^2."""
    phases = np.asarray(phases, dtype=float)
    origins = np.asarray(origins, dtype=float)
    n = len(phases)
    ss = math.sinh(s/(2*n))**2
    dd = math.sinh(t/(2*n))**2 - ss
    vals = []
    for start in range(0, len(origins), 512):
        sin2 = np.sin(np.pi*(phases[None, :] - origins[start:start+512, None]))**2
        vals.extend(np.exp(-np.log1p(dd/(ss + sin2)).sum(axis=1)))
    return np.asarray(vals)


def strip_eta(n: int, s: float, t: float) -> float:
    # cosh(eta)=(cosh(s/N)+cosh(t/N))/2, using a stable acosh identity.
    u = math.sinh(s/(2*n))**2 + math.sinh(t/(2*n))**2
    return 2 * math.asinh(math.sqrt(u/2))


def angular_mean(phases, s=1., t=2., multiplier=24):
    n = len(phases)
    count = int(multiplier*n)
    value = float(radial_values(phases, np.arange(count)/count, s, t).mean())
    eta = .9 * strip_eta(n, s, t)  # strictly inside the contractive strip
    error = 2 / math.expm1(eta*count)
    return value, error


def cue_reference(n: int, s: float, t: float) -> float:
    a = math.exp(-s/n)
    b = math.exp(-t/n)
    delta = b * math.expm1((t-s)/n)
    return math.exp(-(t-s)) * (1 + delta**2 / (-math.expm1(-2*t/n))
             * (-math.expm1(-2*s)) / (-math.expm1(-2*s/n)))


def product_mean(phases, tests, multiplier=24):
    n=len(phases)
    count=multiplier*n
    origins=np.arange(count)/count
    vals=np.ones(count)
    eta=min(.9*strip_eta(n,s,t) for s,t,shift,power in tests)
    for s,t,shift,power in tests:
        require(isinstance(power,int) and power>=1,'Integer positive powers')
        vals *= radial_values(phases,origins+shift/n,s,t)**power
    return float(vals.mean()), 2/math.expm1(eta*count)


def cue_product_reference(n, tests, multiplier=64):
    requested_count=multiplier*n
    require(requested_count == int(requested_count), 'Integer angular grid required')
    count=int(requested_count)
    require(count >= n,
            'Discrete Toeplitz compression requires an integer grid M>=N')
    angles=np.arange(count)/count
    vals=np.ones(count)
    eta=min(.9*strip_eta(n,s,t) for s,t,shift,power in tests)
    for s,t,shift,power in tests:
        ss=math.sinh(s/(2*n))**2
        dd=math.sinh(t/(2*n))**2-ss
        den=ss+dd+np.sin(np.pi*(angles-shift/n))**2
        vals *= (1-dd/den)**power
    ft=np.fft.fft(vals)/count
    mat=toeplitz(ft[:n],np.conj(ft[:n]))
    sign,logdet=np.linalg.slogdet(mat)
    require(abs(sign-1)<1e-9,'Reference determinant positivity')
    # Analytic alias bound for |k|<N, then a trace-norm determinant bound.
    coefficient_error=2*math.exp(-eta*(count-n))/(1-math.exp(-eta*count))
    det_error=n*n*coefficient_error
    return float(math.exp(logdet)),det_error


def cue_limit(s: float, t: float) -> float:
    return math.exp(-(t-s))*(1+(t-s)**2/(4*s*t)*(-math.expm1(-2*s)))


def clock_reference(s: float, t: float) -> float:
    return math.exp(-(t-s))*(1+(math.exp(-s)-math.exp(-t))**2/(1-math.exp(-2*t)))


def build_bgs(n: int):
    require(n >= 3 and n % 2 == 1, 'Odd dimension >=3 required')
    x = np.arange(n, dtype=np.int64)
    q = x/n
    r = lambda q: (1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))
    diag = np.cos(14*np.pi*q)+r(q)/10+r(q)*np.sin(2*np.pi*q)/100-.1
    a = np.diag(diag).astype(complex)
    edge = ((-3-4j)/5) * r(((x+pow(2,-1,n)) % n)/n)/200
    a[x,(x+1)%n] += edge
    a[(x+1)%n,x] += edge.conj()
    xx=x[:,None]; yy=x[None,:]
    phase = (-pow(8,-1,n)*(3*xx*xx-2*xx*yy+3*yy*yy)) % n
    m = np.exp(2j*np.pi*phase/n)/np.sqrt(n)
    return a,m


def finite_checks():
    rng=np.random.default_rng(240615)
    results={}
    exact=0
    for a,b in [(F(3,4),F(1,2)),(F(9,10),F(4,5)),(F(2,3),F(1,3))]:
        d=(a-b)*(1-a*b)/(a*(1-b*b))
        for n in range(1,10):
            mat=[[(F(i==j)-d*b**abs(i-j)) for j in range(n)] for i in range(n)]
            expected=(b/a)**n*(1+(a-b)**2/(1-b*b)*sum(a**(2*j) for j in range(n)))
            require(determinant_fraction(mat)==expected,'Exact CUE Toeplitz identity')
            exact+=1
    results['exact_rational_toeplitz_cases']=exact
    # For M<N the N Fourier columns on M grid points are not an isometry:
    # the sampled constant symbol at M=1 gives an all-ones matrix of norm N.
    # Keep this domain check separate from the analytic alias error estimate.
    try:
        cue_product_reference(3, [(1.,2.,0.,1)], multiplier=F(1,3))
    except (AssertionError, ArithmeticError, ValueError):
        results['undersampled_grid_rejected']=True
    else:
        raise ArithmeticError('Undersampled Toeplitz grid was accepted')
    toeplitz_errors=[]
    for n in [1,3,7,19,61]:
        got,bound=cue_product_reference(n,[(1.,2.,0.,1)])
        error=abs(got-cue_reference(n,1,2))
        require(error<bound+3e-12,'Toeplitz FFT / exact scalar CUE')
        toeplitz_errors.append(error)
    results['toeplitz_fft_exact_comparison_max_error']=max(toeplitz_errors)
    errors=[]; bounds=[]; period_errors=[]; strip_cases=0; circle_integral_errors=[]
    configs=[]
    for n in [1,2,3,7,19]:
        configs.extend([np.arange(n)/n, np.zeros(n), rng.uniform(0,1,n)])
    for ph in configs:
        n=len(ph)
        for s,t in [(.4,1.3),(1.,2.),(2.,3.)]:
            origins=rng.uniform(0,1,7)
            vals=radial_values(ph,origins,s,t)
            require(np.all(vals>=0) and np.all(vals<=1+1e-13),'Contractivity')
            # Independent direct characteristic polynomial product.
            direct=[]
            for alpha in origins:
                z=np.exp(2j*np.pi*(ph-alpha))
                direct.append(math.exp(-(t-s))*abs(np.prod(1-math.exp(-s/n)*z)
                                      /np.prod(1-math.exp(-t/n)*z))**2)
            errors.extend(abs(vals-np.array(direct)))
            for alpha in origins[:3]:
                mean=s+(t-s)/2
                eta=.9*strip_eta(n,s,t)
                for sign in [-1,1]:
                    angles=2*np.pi*(ph-alpha)+1j*sign*eta
                    num=math.cosh(s/n)-np.cos(angles)
                    den=math.cosh(t/n)-np.cos(angles)
                    require(np.max(abs(num/den))<=1+1e-10,'Complex strip bound')
                    strip_cases+=1
            v,err=angular_mean(ph,s,t,48)
            v2,_=angular_mean(ph,s,t,96)
            circle_integral_errors.append(abs(v-v2))
            require(abs(v-v2)<=err+2e-12,'Trapezoid error comparison')
            if np.max(abs(ph-np.arange(n)/n))<1e-14:
                require(abs(v-clock_reference(s,t))<err+3e-12,'Exact clock mean')
            # Periodized kernel sum with certified analytic remainder.
            for x in [-.37*n,.1,.23*n]:
                L=2000
                direct_sum=float(kernel_q(x+n*np.arange(-L,L+1),s,t).sum())
                target=float(periodic_q(x,n,s,t))
                rem=2*(t*t-s*s)/(8*np.pi**2*n*n*(L-.5))
                period_errors.append(target-direct_sum)
                require(target-direct_sum>=-1e-12 and target-direct_sum<=rem+1e-12,
                        'Periodization with tail')
    for s,t in [(.4,1.3),(1.,2.),(2.,3.)]:
        val,e=quad(lambda x: float(kernel_q(x,s,t)),-np.inf,np.inf,epsabs=2e-12)
        require(abs(val-(t-s)/2)<5e-11,'Kernel mass')
    # Full pair-energy identity from the second radial derivative.
    radial_derivative_errors=[]
    tail_checks=0
    for ph in configs:
        n=len(ph)
        orig=np.arange(128*n)/(128*n)
        for s0 in [1.,2.]:
            diff=ph[:,None]-ph[None,:]
            poisson=math.sinh(2*s0/n)/(2*(math.sinh(s0/n)**2+np.sin(np.pi*diff)**2))
            expected=float(poisson.mean())
            def d2(h):
                plus=float(radial_values(ph,orig,s0,s0+h).mean())
                minus=float(radial_values(ph,orig,s0,s0-h).mean())
                return (plus+minus-2)/(h*h)
            got=(4*d2(.0005)-d2(.001))/3
            error=abs(got-expected)
            require(error<2e-6,'Second radial derivative equals 1+2 Abel energy')
            radial_derivative_errors.append(error)
        alpha=.173
        ss=math.sinh(1/(2*n))**2
        dd=math.sinh(2/(2*n))**2-ss
        eig=dd/(ss+dd+np.sin(np.pi*(ph-alpha))**2)
        q=dd/(ss+dd)
        exactlog=float(-np.log1p(-eig).sum())
        for L in [2,5,9]:
            partial=sum(float((eig**k).sum())/k for k in range(1,L+1))
            bound=q**L*float(eig.sum())/((L+1)*(1-q))
            require(-2e-12<=exactlog-partial<=bound+2e-12,'Log determinant tail')
            tail_checks+=1
    results['second_radial_derivative_cases']=len(radial_derivative_errors)
    results['second_radial_derivative_max_error']=max(radial_derivative_errors)
    results['log_determinant_tail_checks']=tail_checks
    results['spectra_checked']=len(configs)
    results['direct_ratio_max_error']=float(max(errors))
    results['complex_strip_cases']=strip_cases
    results['max_trapezoid_refinement_difference']=float(max(circle_integral_errors))
    results['periodization_cases']=len(period_errors)
    results['reference_s1_t2']={
        'cue_limit':cue_limit(1,2), 'clock_exact':clock_reference(1,2),
        'poisson_limit':math.exp(-.75), 'collapsed_weak_limit':1.0}
    # Positive determinant operator identity tested in an arbitrary basis.
    matrix_errors=[]
    for n in [3,5,9]:
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        u,r=np.linalg.qr(z)
        ph=np.mod(np.angle(np.linalg.eigvals(u))/(2*np.pi),1)
        for alpha in [.07,.31]:
            ss=math.cosh(1/n); tt=math.cosh(2/n)
            v=np.exp(-2j*np.pi*alpha)*u
            h=tt*np.eye(n)-(v+v.conj().T)/2
            k=(tt-ss)*np.linalg.inv(h)
            direct=np.linalg.det(np.eye(n)-k)
            expected=radial_values(ph,[alpha],1,2)[0]
            matrix_errors.append(abs(direct-expected))
            require(abs(direct-expected)<2e-11,'Positive determinant identity')
    results['positive_determinant_max_error']=float(max(matrix_errors))
    return results


def probe(sizes):
    rows=[]
    tests2=[(1.,2.,0.,2)]
    testsshift=[(1.,2.,-.5,1),(1.,2.,.5,1)]
    for n in sizes:
        ref2,ref2err=cue_product_reference(n,tests2)
        refshift,refshifterr=cue_product_reference(n,testsshift)
        a,m=build_bgs(n)
        ev,vec=eigh(a)
        for tau in [0.0,0.03,0.30]:
            q=(vec*np.exp(1j*tau*n*ev))@vec.conj().T
            u=q@m
            t,z=schur(u,output='complex')
            diag=np.diag(t)
            phases=np.mod(np.angle(diag)/(2*np.pi),1)
            val,err=angular_mean(phases,multiplier=24)
            doubled,_=angular_mean(phases,multiplier=48)
            require(abs(val-doubled)<=err+3e-12,'Probe quadrature convergence')
            val2,err2=product_mean(phases,tests2)
            valshift,errshift=product_mean(phases,testsshift)
            residual=float(np.linalg.norm(u@z-z@np.diag(diag),'fro')/np.sqrt(n))
            rows.append({'N':n,'tau':tau,'coupling_role':('unperturbed cat control' if tau==0.0 else 'nonphysical proxy'),
                'ratio_mean':val,'cue_finite':cue_reference(n,1,2),
                'defect':val-cue_reference(n,1,2),
                'ratio_squared_mean':val2, 'cue_ratio_squared':ref2,
                'shifted_product_mean':valshift, 'cue_shifted_product':refshift,
                'cue_product_alias_bound':max(ref2err,refshifterr),
                'angular_quadrature_bound_given_exact_phases':err,
                'refined_grid_difference':abs(val-doubled),
                'schur_normalized_frobenius_residual':residual,
                'eigenvalue_unit_circle_error':float(np.max(abs(abs(diag)-1)))})
    return rows


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--sizes',default='31,61,127,251,509')
    parser.add_argument('--out',default=str(Path(__file__).with_name('verification.json')))
    args=parser.parse_args()
    start=time.perf_counter()
    report={'scope':'Finite algebra, exact reference formulas, bounded observable probes. Not a proof of BGS.',
            'floating_point_warning':'Quadrature theorem is rigorous for the exact supplied phases; eigenphase residuals are not interval enclosures.',
            'checks':finite_checks(),
            'probes':probe([int(x) for x in args.sizes.split(',') if x]),
            'runtime_seconds':time.perf_counter()-start}
    Path(args.out).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    main()
