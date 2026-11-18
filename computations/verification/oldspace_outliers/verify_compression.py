#!/usr/bin/env python3
"""Numerical convention and local propagation checks at test couplings.

No floating-point calculation here probes the fixed-coupling limit.
"""
import numpy as np
from scipy.linalg import eigh, norm


def require(condition, label):
    if not condition:
        raise ArithmeticError(label)


def r(q):
    return (1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))


def potential(q):
    return np.cos(14*np.pi*q)-0.1+r(q)*(0.1+0.01*np.sin(2*np.pi*q))


def raw_symbol_generator(n):
    mesh = np.arange(32)/32
    alpha = np.angle((-3+4j)/5)
    f = potential(mesh[:, None]) + .01*r(mesh[:, None])*np.cos(2*np.pi*mesh-alpha)
    coeff = np.fft.fft2(f)/32**2
    x = np.arange(n)
    a = np.zeros((n,n), complex)
    for shift in (-1,0,1):
        for mode in range(-9,10):
            midpoint = (x+pow(2,-1,n)*shift) % n
            a[x,(x+shift)%n] += coeff[mode%32,shift%32]*np.exp(2j*np.pi*mode*midpoint/n)
    return a


def cat(n):
    x = np.arange(n)[:, None]
    y = x.T
    phase = (-pow(8,-1,n)*(3*x*x-2*x*y+3*y*y)) % n
    return np.exp(2j*np.pi*phase/n)/np.sqrt(n)


def matrix_case(m, coupling):
    n = 49*m
    x = np.arange(n)
    hop = (-3-4j)*r(.5+(x+.5)/n)/1000
    literal = np.diag(potential(x/n).astype(complex))
    literal[x,(x+1)%n] = hop
    literal[(x+1)%n,x] = hop.conj()
    a = raw_symbol_generator(n)
    require(norm(a-literal,2) < 2e-13, "midpoint versus modular Weyl")
    values, vectors = eigh(a)
    kick = (vectors*np.exp(1j*coupling*n*values))@vectors.conj().T
    comb = np.zeros((n,m))
    for j in range(7):
        comb[7*np.arange(m)+j*n//7,np.arange(m)] = 1/np.sqrt(7)
    mn, mm = cat(n), cat(m)
    require(norm(mn@comb-comb@mm,2) < 2e-13, "metaplectic intertwining")
    w = comb.T@kick@mn@comb
    require(norm(w@mm.conj().T-comb.T@kick@comb,2) < 2e-13, "compression")
    column = comb[:, [(7*m+1)//2 % m]]
    supp = np.where(column[:,0] != 0)[0]
    phases = np.exp(1j*coupling*n*potential(x/n))
    error = norm(kick@column-phases[:,None]*column)
    bound = coupling*n*(np.max(abs(hop[supp]))+np.max(abs(hop[(supp-1)%n])))
    require(error <= bound+1e-12, "diagonal Duhamel bound")
    print(f"PASS n={n}, coupling={coupling}, error={error:.6g}, bound={bound:.6g}")


def plane_case(force):
    radius = 23
    positions = np.arange(-radius-1,radius+2)
    c, z, p = .14-.23j, .73, .3
    time = .79

    def mode(t):
        integral = t if force == 0 else np.expm1(1j*force*t)/(1j*force)
        phase = 2*z*np.real(c*np.exp(1j*p)*integral)
        v = np.exp(1j*((p+force*t)*positions+phase))/np.sqrt(2*radius+1)
        v[[0,-1]] = 0
        return v

    v = mode(time)
    step = 1e-6
    derivative = (mode(time+step)-mode(time-step))/(2*step)
    operator = np.diag(force*positions).astype(complex)
    operator += np.diag(np.full(len(positions)-1,z*c),1)
    operator += np.diag(np.full(len(positions)-1,z*c.conjugate()),-1)
    residual = derivative-1j*operator@v
    bound = 2*z*abs(c)/np.sqrt(2*radius+1)
    require(norm(residual[2:-2]) < 1e-8, "plane phase sign")
    require(abs(norm(residual)-bound) < 1e-8, "cutoff boundary residual")
    print(f"PASS force={force}, boundary residual={norm(residual):.7f}")


if __name__ == "__main__":
    for m, coupling in ((3,.025),(5,.1),(7,.075)):
        matrix_case(m,coupling)
    for force in (0,.074):
        plane_case(force)
