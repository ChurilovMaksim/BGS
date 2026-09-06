#!/usr/bin/env python3
"""Finite checks for a compact-test microscopic pair-correlation obstruction.

The proof uses an exact positive Fourier identity, not these floating-point
checks. Direct pair sums and an independently integrated moving-window count
are compared. No infinite Fourier truncation is used to assert equality.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from pell_floquet_regression import design, weyl, hermitian_exponential

ROOT=Path(__file__).resolve().parents[2]


def checked_phases(phases) -> np.ndarray:
    x=np.asarray(phases,dtype=float)
    if x.ndim!=1 or len(x)<2 or not np.all(np.isfinite(x)):
        raise ValueError('at least two finite phases in turns are required')
    return x%1


def pair_and_window(phases, L: float, modes: tuple[int,...]) -> dict:
    x=checked_phases(phases); d=len(x)
    if not 0<L<d:
        raise ValueError('require 0 < L < dimension')
    if len(set(modes))!=len(modes) or any(m<=0 for m in modes):
        raise ValueError('selected Fourier modes must be distinct positive integers')
    difference=x[:,None]-x[None,:]
    kernel=sum(np.maximum(1-np.abs(d*(difference+j))/L,0)/L for j in (-1,0,1))
    # Remove indices i=j, not merely pairs with distinct eigenvalues.
    pair=(float(kernel.sum())-float(np.trace(kernel)))/d
    assert abs(float(np.trace(kernel))/d-1/L)<1e-12
    width=L/d
    boundaries=np.unique(np.concatenate(([0.,1.],x,(x-width)%1)))
    first=second=0.
    for a,b in zip(boundaries[:-1],boundaries[1:]):
        midpoint=(a+b)/2
        count=int(np.count_nonzero((x-midpoint)%1 < width))
        first+=(b-a)*count
        second+=(b-a)*count*count
    variance=second-first*first
    assert abs(first-L)<1e-10
    assert abs(variance-(L*L*(pair-1)+L))<1e-9
    partial=0.
    normalized_traces=[]
    for m in modes:
        trace=np.mean(np.exp(2j*np.pi*m*x))
        partial+=2*float(np.sinc(L*m/d)**2)*abs(trace)**2
        normalized_traces.append([m,float(trace.real),float(trace.imag)])
    lower=1+partial-1/L
    assert pair+1e-10>=lower,(d,L,pair,lower)
    assert variance+1e-9>=L*L*partial
    return {'dimension':d,'L':L,'pair_statistic':pair,
            'independent_window_variance':variance,
            'finite_pair_lower_bound':lower,'finite_variance_lower_bound':L*L*partial,
            'selected_traces':normalized_traces}


def odd_eigenphases(k: int,tau: float) -> np.ndarray:
    n,f,h=design(k)
    if n>300:raise ValueError('dense reference limited to N <= 300')
    d=(n-1)//2
    p=np.zeros((n,d));j=np.arange(1,d+1)
    p[j,j-1]=1/math.sqrt(2);p[n-j,j-1]=-1/math.sqrt(2)
    w=weyl(n,-f%n,1); b=p.T@(w+w.conj().T)@p
    u0=p.T@np.eye(n)[h*np.arange(n)%n]@p
    u=hermitian_exponential(b,tau/math.sqrt(2*k))@u0
    eigenvalues=np.linalg.eigvals(u)
    assert np.max(abs(abs(eigenvalues)-1))<1e-10
    return (np.angle(eigenvalues)/(2*np.pi))%1


def report() -> dict:
    rows=[]
    for k in (3,5,7):
        for tau in (0.,.5,1.,2.):
            phases=odd_eigenphases(k,tau)
            for L in (1.,2.,3.,5.):
                if L>=len(phases):continue
                row=pair_and_window(phases,L,(k,2*k))
                row.update({'K':k,'tau':tau,
                            'asymptotic_single_resonance_pair_bound':1+2*math.exp(-tau*tau)-1/L})
                rows.append(row)
    clock=pair_and_window(np.arange(64)/64,3.,(1,8))
    assert abs(clock['independent_window_variance'])<1e-10
    assert abs(clock['pair_statistic']-2/3)<1e-10
    repeated=pair_and_window(np.repeat(np.arange(8)/8,8),2.,(8,16))
    assert repeated['pair_statistic']>1
    # The zero first harmonic is insufficient to detect the eighth-harmonic resonance.
    assert abs(np.mean(np.exp(2j*np.pi*np.repeat(np.arange(8)/8,8))))<1e-12
    for bad in (0.,64.,-1.):
        try:pair_and_window(np.arange(64)/64,bad,(1,))
        except ValueError:pass
        else:raise AssertionError('invalid interval length accepted')
    return {'producer':'computations/verification/pell_pair_obstruction.py',
            'scope':'Floating-point finite identity and inequality checks. Direct compactly supported pair sums versus exact-in-x piecewise-constant window integration. The analytic theorem is proved independently; no claim of universal finite-size asymptotics.',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'checks':rows,'clock_control':clock,'repeated_clock_control':repeated,'status':'PASS'}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args(); data=report();text=json.dumps(data,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    else:print(text,end='')

if __name__=='__main__':main()
