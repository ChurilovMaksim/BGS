#!/usr/bin/env python3
"""Independent double-precision quadrature of the critical likelihood exponent.

This is a numerical diagnostic of a proved compensated integral, not a
finite-copy simulation or a certified infinite-integral enclosure. Compare
multiple quadrature orders and windows before interpreting numeric values.
"""
from __future__ import annotations
import argparse,hashlib,json,math
from pathlib import Path
import numpy as np


def psi(v,*,n=None,order=96,angles=1024,window=25.0):
    nodes,weights=np.polynomial.legendre.leggauss(order)
    phi=2*np.pi*(np.arange(angles)+.5)/angles
    cosine=np.cos(phi)
    pieces=[-window,-8,-2,-.3,0,.3,2,8,window]
    if n:
        u=1/n;x=math.exp((math.lgamma(n+1)+math.log((1-u)/u))/n)
        lower=max(-window,-x)
        pieces=[lower]+[p for p in pieces if lower<p<window]+[window]
        pieces=sorted(set(pieces))
    total=0j
    for left,right in zip(pieces,pieces[1:]):
        if right<=left:continue
        y=(left+right)/2+(right-left)*nodes/2
        logt=np.e*y if n is None else n*np.log1p(y/x)
        amplitude=1+np.exp(logt)
        contrast=2*np.exp(logt/2)/(1+np.exp(logt))
        tt=contrast[:,None]*cosine[None,:]
        tt=np.clip(tt,-1+1e-15,1-1e-15)
        lr=np.log1p(tt)-np.log1p(-tt)
        avg=np.mean(-2*np.sin(v*lr/2)**2-1j*tt*np.sin(v*lr),axis=1)
        total+=np.sum(weights*(right-left)/2*np.exp(-y)*amplitude*avg)
    return total


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--order',type=int,default=96);p.add_argument('--angles',type=int,default=1024)
    p.add_argument('--output',type=Path);a=p.parse_args()
    if a.order<24 or a.angles<128:p.error('insufficient quadrature order')
    out=[]
    for v in [.25,.5,1.0]:
        limit=psi(v,order=a.order,angles=a.angles)
        assert limit.real<0
        assert abs(psi(-v,order=a.order,angles=a.angles)-limit.conjugate())<1e-10
        finite=[]
        for n in [32,128,512,2048]:
            z=psi(v,n=n,order=a.order,angles=a.angles)
            finite.append({'n':n,'real':z.real,'imaginary':z.imag,'distance_to_limit':abs(z-limit)})
        out.append({'v':v,'limit_real':limit.real,'limit_imaginary':limit.imag,'finite':finite})
    midpoint=psi(-.5j,order=a.order,angles=a.angles)
    assert abs(midpoint.imag)<1e-10
    assert abs(-2*midpoint.real-2.908610238318175)<2e-4
    assert psi(0,order=a.order,angles=a.angles)==0
    r={'status':'PASS','scope':'numerical quadrature, not a rigorous interval certificate',
       'radial_order':a.order,'angles':a.angles,'window':25,
       'chernoff_C_crosscheck':-2*midpoint.real,'characteristic_exponents':out,
       'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))
if __name__=='__main__':main()
