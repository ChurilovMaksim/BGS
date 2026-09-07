#!/usr/bin/env python3
"""One-mode high-precision reference for known Gaussian-channel input inversion.

This is numerical quadrature of the theorem's finite Weyl integral using a
characteristic-function oracle. It is not a finite-copy experimental claim.
The theorem also specifies an unbiased random-homodyne estimator. All gains
must be positive; the vacuum characteristic function is exp(-|z|^2/2).
"""
from __future__ import annotations
from math import factorial, comb
import mpmath as mp


def physical_parameters(gain, noise):
    gain, noise = mp.mpf(gain), mp.mpf(noise)
    if not (mp.isfinite(gain) and mp.isfinite(noise) and gain > 0 and noise >= abs(1-gain)):
        raise ValueError('Require finite gain>0 and noise>=abs(1-gain)')
    return gain, noise


def displacement_element(j: int, k: int, z):
    if not isinstance(j,int) or not isinstance(k,int) or min(j,k)<0:
        raise ValueError('Nonnegative occupation indices required')
    z=mp.mpc(z)
    return mp.exp(-abs(z)**2/2)*mp.sqrt(factorial(j)*factorial(k))*mp.fsum(
        z**(j-ell)*(-mp.conj(z))**(k-ell)/
        (factorial(j-ell)*factorial(k-ell)*factorial(ell))
        for ell in range(min(j,k)+1))


def finite_characteristic(rho: mp.matrix, z):
    if rho.rows != rho.cols:
        raise ValueError('Square matrix required')
    return mp.fsum(rho[j,k]*displacement_element(k,j,z)
                   for j in range(rho.rows) for k in range(rho.cols))


def pure_loss(rho: mp.matrix, eta):
    eta=mp.mpf(eta)
    if not 0 <= eta <= 1 or rho.rows!=rho.cols:
        raise ValueError('Invalid state shape or transmissivity')
    dim=rho.rows; out=mp.zeros(dim)
    for m in range(dim):
        for n in range(dim):
            for ell in range(min(m,n)+1):
                out[m-ell,n-ell]+=rho[m,n]*mp.sqrt(comb(m,ell)*comb(n,ell))*\
                    (1-eta)**ell*eta**(mp.mpf(m+n)/2-ell)
    return out


def pair_loss_fidelity(n: int, u, eta):
    u,eta=mp.mpf(u),mp.mpf(eta)
    if not isinstance(n,int) or n<1 or not 0<u<1 or not 0<eta<1:
        raise ValueError('Require n>=1, 0<u<1, 0<eta<1')
    a=1-u+u*(1-eta)**n;b=u*eta**n;c2=u*(1-u)*eta**n;s=a+b
    gap=4*c2/(s+mp.sqrt(s*s-4*c2))
    return {'root_fidelity_gap':gap,'root_fidelity':1-gap,
            'trace_distance':2*mp.sqrt(c2),'active_trace':s}


def quadrature_inverse(output_characteristic, cutoff: int, gain, noise,
                       radius_squared, radial_order: int=48, angular_order: int=64):
    """Recover a low input block from its output characteristic function.

    Returns the Hermitian raw block; no state cutoff is assumed by the oracle.
    Increase quadrature and precision independently before trusting numerics.
    For the analytic tail guarantee use radius_squared>=32*cutoff.
    """
    gain,noise=physical_parameters(gain,noise)
    if not isinstance(cutoff,int) or cutoff<0 or radial_order<2 or angular_order<2:
        raise ValueError('Invalid cutoff or quadrature order')
    L=mp.mpf(radius_squared)
    if not mp.isfinite(L) or L<=0: raise ValueError('Positive finite radius required')
    nodes,weights=mp.gauss_quadrature(radial_order,'legendre')
    out=mp.zeros(cutoff+1)
    for t,w in zip(nodes,weights):
        x=L*(t+1)/2; radial_weight=L*w/2; r=mp.sqrt(x)
        for q in range(angular_order):
            theta=2*mp.pi*q/angular_order;z=r*mp.exp(1j*theta)
            recovered=mp.exp(noise*x/(2*gain))*output_characteristic(z/mp.sqrt(gain))
            for j in range(cutoff+1):
                for k in range(cutoff+1):
                    out[j,k]+=radial_weight*recovered*displacement_element(j,k,-z)/angular_order
    return (out+out.H)/2
