#!/usr/bin/env python3
"""Fixed-strength, disjoint-symbol coboundary: reproducible finite checks.

The analytic theorem is in mathematics/fixed_strength_locality.md. Exact
integer/rational checks, Fourier discretization controls, and finite numerical
operator tests are separate. No experiment is a proof of an asymptotic claim.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh, eigvals, svdvals

ROOT = Path(__file__).resolve().parents[2]
RADIUS = 1 / 16
ASYMMETRY = 1 / 3


def bump(t: np.ndarray | float) -> np.ndarray:
    t = np.asarray(t, dtype=float)
    value = np.zeros_like(t)
    inside = np.abs(t) < 1
    value[inside] = np.exp(1 - 1 / (1 - t[inside] ** 2))
    return value


def wrapped(t: np.ndarray | float) -> np.ndarray:
    return (np.asarray(t) + 0.5) % 1 - 0.5


def position_factor(x: np.ndarray | float) -> np.ndarray:
    u = wrapped(np.asarray(x) - 0.25) / RADIUS
    v = wrapped(np.asarray(x) + 0.25) / RADIUS
    return bump(u) * (1 + ASYMMETRY * u) + bump(v) * (1 - ASYMMETRY * v)


def momentum_factor(x: np.ndarray | float) -> np.ndarray:
    return bump(wrapped(x) / RADIUS)


def symbol(q: np.ndarray | float, p: np.ndarray | float) -> np.ndarray:
    return position_factor(q) * momentum_factor(p)


def exact_geometry() -> dict:
    r = Fraction(1, 16)
    image_distance = Fraction(1, 2) - 5 * r
    assert image_distance == Fraction(3, 16)
    assert image_distance - r == Fraction(1, 8)
    # Cauchy-disk constants used in the bump derivative estimate.
    relative_error = Fraction(17, 64)
    real_inverse_bound = (1-relative_error)/(1+relative_error)**2
    assert real_inverse_bound > Fraction(1, 3)
    # Universal scaled-coordinate support exclusion, finite exact controls.
    cases = 0
    for denom in (8, 16, 32):
        for u in range(-denom, denom+1):
            for v in range(-denom, denom+1):
                y = 8*denom + 2*u + 3*v
                assert 3*denom <= y <= 13*denom
                assert min(y, 16*denom-y) >= 3*denom
                cases += 1
    return {'radius':str(r), 'image_distance_lower_bound':str(image_distance),
            'separation_margin':str(image_distance-r),
            'cauchy_real_inverse_bound':str(real_inverse_bound),
            'integer_grid_checks':cases}


def wedge(v: tuple[int, int], w: tuple[int, int]) -> int:
    return v[0]*w[1]-v[1]*w[0]


def convolution(f: dict, g: dict, power: int = 0) -> dict:
    out = defaultdict(int)
    for v, a in f.items():
        for w, b in g.items():
            out[(v[0]+w[0],v[1]+w[1])] += a*b*wedge(v,w)**power
    return {v:a for v,a in out.items() if a}


def poisson_negative_control() -> dict:
    g = {(1,0):1,(-1,0):1,(0,1):1,(0,-1):1}
    d = convolution(g,g)
    first = convolution(g,d,1)
    third = convolution(g,d,3)
    assert not first and third
    rows = []
    for n in (31, 63, 127):
        gm, dm = quantize_polynomial(n,g), quantize_polynomial(n,d)
        c = gm@dm-dm@gm
        norm = float(svdvals(c)[0])
        assert norm > 1e-8
        rows.append({'N':n,'commutator_operator_norm':norm,'N_cubed_norm':n**3*norm})
    return {'first_moyal_coefficient_zero':True,
            'third_moyal_coefficient':{str(v):a for v,a in sorted(third.items())},
            'matrix_checks':rows,
            'meaning':'Poisson commutation alone does not imply all-orders quantum commutation.'}


def qweyl(n: int, a: int, b: int) -> np.ndarray:
    x = np.arange(n,dtype=np.int64)
    mat = np.zeros((n,n),complex)
    # Physical integer Fourier lift, not modular division by two.
    mat[x,(x-b)%n] = np.exp(1j*np.pi*((2*a*x-a*b)%(2*n))/n)
    return mat


def quantize_polynomial(n: int, coeff: dict) -> np.ndarray:
    out = np.zeros((n,n),complex)
    for (a,b),c in coeff.items():
        out += c*qweyl(n,a,b)
    return out


def cat_kernel(n: int) -> np.ndarray:
    if n < 3 or n % 2 == 0:
        raise ValueError('N must be odd and at least three')
    x = np.arange(n,dtype=np.int64)
    power = ((3*x[:,None]**2-2*x[:,None]*x[None,:]+3*x[None,:]**2)*pow(8,-1,n))%n
    return np.exp(2j*np.pi*power/n)/np.sqrt(n)


def odd_compress(a: np.ndarray) -> np.ndarray:
    n = len(a)
    j = np.arange(1,(n+1)//2)
    return (a[np.ix_(j,j)]-a[np.ix_(j,n-j)]-a[np.ix_(n-j,j)]+a[np.ix_(n-j,n-j)])/2


def exponential(a: np.ndarray, scale: float) -> np.ndarray:
    if np.max(np.abs(a-a.conj().T)) > 1e-11:
        raise ValueError('expected Hermitian input')
    values, vectors = eigh(a)
    return (vectors*np.exp(1j*scale*values))@vectors.conj().T


def fourier_coefficients(size: int) -> np.ndarray:
    if size < 4096 or size & (size-1):
        raise ValueError('Fourier grid must be a power of two >=4096')
    return np.fft.fft(momentum_factor(np.arange(size)/size))/size


def quantize_bump(n: int, cutoff: int = 512, grid: int = 32768) -> np.ndarray:
    if 2*cutoff >= grid:
        raise ValueError('Fourier cutoff must be below Nyquist')
    bhat = fourier_coefficients(grid)
    x = np.arange(n)
    result = np.zeros((n,n),complex)
    # Sum all integer aliases b, including their half-grid midpoint shifts.
    # Summation over the q frequency is exact via position_factor.
    for b in range(-cutoff,cutoff+1):
        result[x,(x-b)%n] += bhat[b%grid]*position_factor((x-b/2)/n)
    return result


def quantize_bump_weyl_reference(n: int, cutoff: int = 80, grid: int = 32768) -> np.ndarray:
    """Independent 2D finite Fourier polynomial and physical Weyl assembly."""
    x = np.arange(grid)/grid
    ahat = np.fft.fft(position_factor(x))/grid
    bhat = fourier_coefficients(grid)
    out = np.zeros((n,n),complex)
    rows = np.arange(n)
    for b in range(-cutoff,cutoff+1):
        phases = np.zeros(n,complex)
        for a in range(-cutoff,cutoff+1):
            phases += ahat[a%grid]*np.exp(1j*np.pi*((2*a*rows-a*b)%(2*n))/n)
        out[rows,(rows-b)%n] += bhat[b%grid]*phases
    return out


def finite_conventions() -> dict:
    errors=[]
    for n in (7, 9, 41):
        u=cat_kernel(n)
        unitary=float(np.max(np.abs(u@u.conj().T-np.eye(n))))
        assert unitary<1e-12
        for v in ((1,0),(0,1),(1,1),(-2,3),(n+1,-n+2)):
            tv=(3*v[0]+2*v[1],4*v[0]+3*v[1])
            err=float(np.max(np.abs(u@qweyl(n,*v)@u.conj().T-qweyl(n,*tv))))
            assert err<2e-12
            errors.append(err)
        for v,w in (((1,1),(2,3)),((-2,5),(3,-4))):
            target=np.exp(1j*np.pi*wedge(v,w)/n)*qweyl(n,v[0]+w[0],v[1]+w[1])
            assert np.max(abs(qweyl(n,*v)@qweyl(n,*w)-target))<2e-12
        j=(-np.arange(n))%n
        assert np.max(abs(u[np.ix_(j,j)]-u))<2e-12
    return {'covariance_tests':len(errors),'largest_covariance_entry_error':max(errors),
            'includes_composite_modulus':9,'physical_odd_product_mode':True}


def coefficient_controls() -> dict:
    c1,c2=fourier_coefficients(16384),fourier_coefficients(32768)
    ks=np.arange(-1024,1025)
    difference=float(np.sum(abs(c1[ks%len(c1)]-c2[ks%len(c2)])))
    assert difference<1e-12
    quadrature=[]
    for b in (0,1,7,31,100,250):
        value,error=quad(lambda x:float(bump(x/RADIUS))*math.cos(2*math.pi*b*x),
                         -RADIUS,RADIUS,epsabs=1e-13,epsrel=1e-13,limit=300)
        diff=abs(value-c2[b])
        assert diff<2e-12
        quadrature.append({'frequency':b,'fft_coefficient_real':float(c2[b].real),
                           'quadrature_absolute_difference':float(diff),
                           'quadrature_internal_error_estimate':error})
    reference=quantize_bump_weyl_reference(41,640)
    summed=quantize_bump(41,640)
    error=float(svdvals(reference-summed)[0])
    # Difference is q-frequency truncation, not a convention mismatch.
    assert error<1e-8
    return {'two_grid_coefficient_l1_difference':difference,
            'quadrature':quadrature,'two_dimensional_reference_cutoff':640,
            'two_dimensional_reference_operator_difference':error,
            'scope':'Numerical refinement checks, not certified Fourier-tail or rounding intervals.'}


def matrix_case(n: int, kappa: float = .125) -> dict:
    start=time.monotonic()
    g=quantize_bump(n,2048,65536)
    refined=quantize_bump(n,4096,131072)
    truncdiff=float(svdvals(refined-g)[0])
    herm=float(np.max(abs(g-g.conj().T)))
    assert herm<2e-12 and truncdiff<1e-10
    u=cat_kernel(n)
    d=u@g@u.conj().T
    product=float(svdvals(g@d)[0])
    comm=float(svdvals(g@d-d@g)[0])
    gg,dd,uu=map(odd_compress,(g,d,u))
    scale=kappa*n
    kick=exponential(gg-dd,scale)@uu
    gauge=exponential(gg,scale)
    model=gauge@uu@gauge.conj().T
    error=float(svdvals(kick-model)[0])
    bound=scale*scale*comm/2
    assert error<=bound+2e-11
    trace_error=abs(np.trace(kick)-np.trace(uu))/len(uu)
    assert trace_error<=error+1e-11
    row={'N':n,'dimension':len(uu),'kappa':kappa,
         'full_product_operator_norm':product,'full_commutator_operator_norm':comm,
         'odd_kick_conjugacy_operator_error':error,'trotter_upper_bound':bound,
         'hermiticity_entry_error':herm,'Fourier_refinement_operator_difference':truncdiff,
         'rounding_scope':'Double precision; no interval certification.',
         'seconds':time.monotonic()-start}
    # Actual spectra, never substituted by the conjugated reference spectra.
    angles=np.sort((np.angle(eigvals(kick))/(2*np.pi))%1)
    gaps=len(angles)*np.diff(np.r_[angles,angles[0]+1])
    row['spacing_min']=float(min(gaps));row['spacing_mean']=float(np.mean(gaps))
    row['spacing_fraction_below_0_01']=float(np.mean(gaps<.01))
    for k,nn in ((3,7),(5,41),(7,239)):
        if n==nn:
            uk=np.linalg.matrix_power(uu,k)
            phase=np.trace(uk)/len(uu)
            assert abs(abs(phase)-1)<1e-11
            assert svdvals(uk-phase*np.eye(len(uu)))[0]<1e-10
            residue=np.trace(np.linalg.matrix_power(kick,k))/len(uu)
            row.update(Pell_period=k,unperturbed_return_phase_real=float(phase.real),
                       unperturbed_return_phase_imag=float(phase.imag),
                       actual_normalized_return_modulus=float(abs(residue)),
                       phase_corrected_return_error=float(abs(residue-phase)))
            assert abs(residue-phase)<=k*error+2e-10
    return row


def report(extended: bool=False) -> dict:
    data={'producer':'computations/verification/fixed_strength_locality.py',
          'schema_version':1,'status':'PASS',
          'scope':'Exact finite algebra plus numerical finite operator falsifiers; not an asymptotic proof or a priority certificate.',
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'geometry':exact_geometry(),'conventions':finite_conventions(),
          'poisson_only_negative_control':poisson_negative_control(),
          'coefficient_controls':coefficient_controls(),
          'matrix_checks':[]}
    sizes=(7,41,127,239,511) if extended else (7,41,127,239)
    for n in sizes:
        data['matrix_checks'].append(matrix_case(n))
    return data


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    p.add_argument('--extended',action='store_true')
    args=p.parse_args()
    data=report(args.extended)
    text=json.dumps(data,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    else:
        print(text,end='')

if __name__=='__main__':
    main()
