#!/usr/bin/env python3
"""Independent checks for fixed-strength flat kicks and analytic non-flatness.

Nodal bump matrix is exact as a mathematical formula (no Fourier cutoff).
Evaluation, eigenvalues, matrix exponentials and ODEs use floating point.
No asymptotic theorem is inferred from a finite small residual.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time
import numpy as np
from scipy.linalg import eigh, expm, svdvals
from scipy.integrate import solve_ivp

T = np.array([[3, 2], [4, 3]], dtype=np.int64)
S = T.T
RADIUS = 1.0 / 16


def eta(t):
    t = np.asarray(t, dtype=float)
    out = np.zeros_like(t)
    mask = np.abs(t) < 1
    u = t[mask]
    out[mask] = np.exp(1.0 - 1.0 / (1.0-u*u))
    return out


def eta_prime(t):
    t = np.asarray(t, dtype=float)
    out = np.zeros_like(t)
    mask = np.abs(t) < 1
    u = t[mask]
    out[mask] = eta(u) * (-2*u) / (1-u*u)**2
    return out


def periodic_bump(x):
    return eta(((np.asarray(x)+.5) % 1-.5) / RADIUS)


def periodic_derivative(x):
    return eta_prime(((np.asarray(x)+.5) % 1-.5)/RADIUS)/RADIUS


def ell(x):
    return periodic_bump(x-.25)+periodic_bump(x+.25)


def ell_prime(x):
    return periodic_derivative(x-.25)+periodic_derivative(x+.25)


def g0(point):
    q, p = np.asarray(point)
    return ell(q)*periodic_bump(p)


def grad_g(point):
    q, p = np.asarray(point)
    return np.array([ell_prime(q)*periodic_bump(p), ell(q)*periodic_derivative(p)])


def field_g(point):
    v = grad_g(point)
    return np.array([v[1], -v[0]])


def field_f(point):
    v = grad_g(point)-T@grad_g(S@np.asarray(point))
    return np.array([v[1], -v[0]])


def circle_difference(a, b):
    return (np.asarray(a)-np.asarray(b)+.5) % 1-.5


def cat(n: int):
    if n < 3 or n % 2 == 0:
        raise ValueError('odd N >= 3 required')
    x = np.arange(n, dtype=np.int64)
    y = x[None, :]
    x = x[:, None]
    phase = ((3*x*x-2*x*y+3*y*y)*pow(8, -1, n)) % n
    return np.exp(2j*np.pi*phase/n)/math.sqrt(n)


def qweyl(n: int, a: int, b: int):
    x = np.arange(n)
    # Physical integer convention; modular half would require (-1)^(ab).
    exponent = (a*(2*x-b)) % (2*n)
    z = np.zeros((n, n), dtype=complex)
    z[x, (x-b) % n] = np.exp(1j*np.pi*exponent/n)
    return z


def bump_matrix(n: int):
    x = np.arange(n)
    coef = np.fft.fft(periodic_bump(x/n))/n
    return ell((x[:, None]+x[None, :])/(2*n))*coef[(x[:, None]-x[None, :]) % n]


def sym_exp(eigen, multiplier: float):
    val, vec = eigen
    return (vec*np.exp(1j*multiplier*val))@vec.conj().T


def opnorm(a):
    return float(svdvals(a, check_finite=False)[0])


def exact_support():
    r = Fraction(1,16)
    corners = [Fraction(1,2)+2*u+3*v for u in (-r,r) for v in (-r,r)]
    lo, hi = min(corners), max(corners)
    assert lo == Fraction(3,16) and hi == Fraction(13,16)
    assert min(lo,1-hi)-r == Fraction(1,8)
    return {'halfwidth':str(r), 'second_coordinate_range':[str(lo),str(hi)],
            'separation_gap':str(min(lo,1-hi)-r),'arithmetic':'exact rational'}


def nodal_and_covariance_controls():
    worst_product = worst_covariance = worst_nodal = 0.0
    negative = []
    for n in (7,9,15,31):
        u=cat(n)
        assert np.linalg.norm(u@u.conj().T-np.eye(n), 'fro') < 2e-12
        for v in ((1,0),(0,1),(1,1),(8,-9),(-5,3)):
            tv=T@np.array(v)
            err=opnorm(u@qweyl(n,*v)@u.conj().T-qweyl(n,int(tv[0]),int(tv[1])))
            worst_covariance=max(worst_covariance,err)
            for w in ((0,1),(1,-1),(9,8)):
                vw=(v[0]+w[0],v[1]+w[1])
                phase=np.exp(1j*np.pi*((v[0]*w[1]-v[1]*w[0]) % (2*n))/n)
                err=opnorm(qweyl(n,*v)@qweyl(n,*w)-phase*qweyl(n,*vw))
                worst_product=max(worst_product,err)
        # A separable symbol with even q frequencies, including aliasing modes.
        lc={2:.5,-2:.5,4:.15,-4:.15}
        bc={1:.5,-1:.5,9:.1,-9:.1}
        x=np.arange(n)
        l=lambda q: sum(c*np.exp(2j*np.pi*a*q) for a,c in lc.items())
        b=sum(c*np.exp(2j*np.pi*v*x/n) for v,c in bc.items())
        nodal=l((x[:,None]+x[None,:])/(2*n))*(np.fft.fft(b)/n)[(x[:,None]-x[None,:]) % n]
        direct=sum(c*d*qweyl(n,a,b) for a,c in lc.items() for b,d in bc.items())
        worst_nodal=max(worst_nodal,opnorm(direct-nodal))
        # Wrongly using the half-period formula for a non-half-periodic symbol.
        bad=np.exp(2j*np.pi*(x[:,None]+x[None,:])/(2*n))*(np.fft.fft(np.exp(2j*np.pi*x/n))/n)[(x[:,None]-x[None,:]) % n]
        error=opnorm(bad-qweyl(n,1,1))
        assert error > 1.9
        negative.append({'N':n,'omitted_half_period_error':error})
    assert max(worst_product,worst_covariance,worst_nodal) < 3e-12
    return {'weyl_product_max_error':worst_product,'cat_covariance_max_error':worst_covariance,
            'nodal_control_max_error':worst_nodal,'negative_controls':negative}


def classical_controls():
    starts=[np.array(x) for x in ((.26,.02),(.235,-.012),(.74,.01),(.1,.3),(.52,.01))]
    inverse_s=np.array([[3,-4],[-2,3]],dtype=float)
    starts.extend(inverse_s@x for x in starts[:3])
    rows=[]
    max_displacement=max_wrong_sign=0.0
    def flow(field,point,t):
        sol=solve_ivp(lambda _,x:field(x),(0,t),np.asarray(point,dtype=float),
                      rtol=2e-11,atol=2e-13,method='DOP853',max_step=max(abs(t)/16,1e-5))
        if not sol.success: raise RuntimeError(sol.message)
        return sol.y[:,-1]
    for kappa in (-.013,.007,.021):
        for x in starts:
            direct=S@flow(field_f,x,-kappa)
            conjugated=flow(field_g,S@flow(field_g,x,-kappa),kappa)
            err=float(np.linalg.norm(circle_difference(direct,conjugated),np.inf))
            assert err < 2e-8
            displacement=float(np.linalg.norm(circle_difference(direct,S@x),np.inf))
            wrong=flow(field_g,S@flow(field_g,x,kappa),-kappa)
            wrong_error=float(np.linalg.norm(circle_difference(direct,wrong),np.inf))
            max_displacement=max(max_displacement,displacement)
            max_wrong_sign=max(max_wrong_sign,wrong_error)
            rows.append({'kappa':kappa,'point':x.tolist(),'error':err,
                         'nonlinear_displacement':displacement,'wrong_sign_error':wrong_error})
    assert max_displacement>1e-3 and max_wrong_sign>1e-3
    return {'method':'DOP853, not interval integration; both separated supports tested',
            'maximum_displacement':max_displacement,
            'wrong_sign_negative_control':max_wrong_sign,'checks':rows}


def dense_checks(n: int, kappas: tuple[float,...]):
    started=time.monotonic()
    u=cat(n); a=bump_matrix(n)
    herm=float(np.linalg.norm(a-a.conj().T,'fro'))
    assert herm < 2e-11
    rev=(-np.arange(n)) % n
    parity=float(np.linalg.norm(a-a[rev][:,rev],'fro'))
    assert parity < 2e-11
    # Work on full space so no parity trace convention enters this test.
    a=(a+a.conj().T)/2
    d=u@a@u.conj().T
    d=(d+d.conj().T)/2
    h=a-d
    ev_a=eigh(a,check_finite=False)
    ev_h=eigh(h,check_finite=False)
    comm=a@d-d@a
    comm_norm=opnorm(comm)
    rows=[]
    for kappa in kappas:
        e=2*math.pi*n*kappa
        j=sym_exp(ev_a,e)
        v=sym_exp(ev_h,e)@u
        defect=j.conj().T@v@j-u
        err=opnorm(defect)
        bound=.5*e*e*comm_norm
        assert err <= bound+2e-9
        alt_error=None
        if n<=63:
            alt=expm(-1j*e*a)@expm(1j*e*h)@expm(1j*e*d)
            alt_error=opnorm(alt-j.conj().T@v@j@u.conj().T)
            assert alt_error < 3e-10
        rows.append({'kappa':kappa,'quantum_exponent':e,'gauge_operator_error':err,
                     'measured_commutator_product_bound':bound,'independent_expm_error':alt_error})
    return {'N':n,'commutator_operator_norm':comm_norm,'hermiticity_frobenius_error':herm,
            'parity_frobenius_error':parity,'checks':rows,'seconds':time.monotonic()-started,
            'precision_warning':'Floating-point value; small residual is not an exact zero or a proof of asymptotic rate.'}


def analytic_control():
    # g=b_(1,0). Its bracket h={g,Cg}=16*pi^2*(b_(2,4)-b_(4,4)).
    # The two cosines are orthogonal: ||h||_2=32*pi^2.
    target=32*math.pi**2
    rows=[]
    for n in (31,63,127,255):
        u=cat(n); w=qweyl(n,1,0); a=w+w.conj().T
        d=u@a@u.conj().T; comm=a@d-d@a
        scaled=float(np.linalg.norm(comm,'fro')/math.sqrt(n)*(2*math.pi*n))
        exact=8*math.pi*n*abs(math.sin(4*math.pi/n))
        assert abs(scaled-exact) < 2e-10
        rows.append({'N':n,'HS_commutator_over_hbar':scaled,'exact_value':exact,'limiting_value':target})
    assert abs(rows[-1]['HS_commutator_over_hbar']/target-1) < .001
    return rows



def pell_spectral_controls():
    rows=[]
    for period,n in ((3,7),(5,41),(7,239)):
        full=cat(n)
        phase=np.exp(-1j*np.angle(np.trace(np.linalg.matrix_power(full,period))/n)/period)
        full=phase*full
        dim=(n-1)//2
        x=np.arange(1,dim+1)
        u=full[np.ix_(x,x)]-full[np.ix_(x,n-x)]
        whole=bump_matrix(n)
        a=whole[np.ix_(x,x)]-whole[np.ix_(x,n-x)]
        a=(a+a.conj().T)/2
        assert opnorm(np.linalg.matrix_power(u,period)-np.eye(dim))<2e-11
        eigen_a=eigh(a,check_finite=False)
        h=a-u@a@u.conj().T
        eigen_h=eigh((h+h.conj().T)/2,check_finite=False)
        for kappa in (.002,.02):
            exponent=2*math.pi*n*kappa
            j=sym_exp(eigen_a,exponent)
            v=sym_exp(eigen_h,exponent)@u
            defect=opnorm(j.conj().T@v@j-u)
            vals=np.linalg.eigvals(v)
            labels=np.rint(period*np.angle(vals)/(2*math.pi)).astype(int)%period
            counts=np.bincount(labels,minlength=period)
            if defect<math.sin(math.pi/period):
                assert all(counts==dim//period)
            maximum=0.
            checks=[]
            for t in sorted({-dim,-period,1,period,dim,period*(dim//period)}):
                actual=np.mean(vals**t)
                ref=1. if t%period==0 else 0.
                error=abs(actual-ref)
                assert error<=abs(t)*defect+2e-10
                maximum=max(maximum,error)
                checks.append({'time':t,'trace_error':float(error),'unitary_telescope_bound':abs(t)*defect})
            rows.append({'N':n,'K':period,'odd_dimension':dim,'kappa':kappa,
                         'gauge_operator_error':defect,'cluster_counts':counts.tolist(),
                         'trace_controls':checks})
    return rows

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--sizes',default='31,63,127,255,511')
    args=parser.parse_args()
    sizes=[int(x) for x in args.sizes.split(',')]
    report={'producer':'computations/verification/pell_flat_quantum_check.py','scope':'Finite exact rational geometry and floating-point operator/flow controls; not full theorem formalization.',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'python':platform.python_version(),'numpy':np.__version__,
            'support':exact_support(),'algebra':nodal_and_covariance_controls(),
            'classical':classical_controls(),'analytic':analytic_control(),'pell_spectra':pell_spectral_controls(),'flat':[]}
    for n in sizes:
        row=dense_checks(n,(-.02,.02,.1))
        report['flat'].append(row)
        print('N',n,'comm',row['commutator_operator_norm'],'loop',[r['gauge_operator_error'] for r in row['checks']],flush=True,file=sys.stderr)
    report['status']='PASS'
    text=json.dumps(report,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    else:
        print(text,end='')

if __name__=='__main__': main()
