"""Literal construction of M_N, A_N, U_N following formalization/Bgs/TraceStatement.lean
and mathematics/fixed-map/kick_blind_arithmetic_spike.md (BGS-TRACE-117)."""
import numpy as np
from fractions import Fraction

def eN(N, t):
    return np.exp(2j*np.pi*(np.asarray(t) % N)/N)

def MN(N):
    x = np.arange(N)[:, None]; y = np.arange(N)[None, :]
    inv8 = pow(8, -1, N)
    ph = (-inv8*(3*x*x - 2*x*y + 3*y*y)) % N
    return eN(N, ph)/np.sqrt(N)

def weylT(N, a, b):
    """(T(a,b)psi)(x)=e_N(b(x+a/2)) psi(x+a): entry (x, x+a) = e_N(b(x+2^{-1}a))."""
    inv2 = pow(2, -1, N)
    T = np.zeros((N, N), complex)
    x = np.arange(N)
    T[x, (x+a) % N] = eN(N, b*(x + inv2*a))
    return T

def rCoeff(k):
    return {0: 1.0, 1: .5, -1: .5, 7: -.5, -7: -.5, 6: -.25, -6: -.25, 8: -.25, -8: -.25}.get(k, 0.0)

def fCoeff(k, l):
    if l == 0:
        v = (0.5 if k in (7, -7) else 0) + rCoeff(k)/10 + (rCoeff(k-1)-rCoeff(k+1))/(200j)
        v -= (0.1 if k == 0 else 0)
        return complex(v)
    if l == 1:
        return rCoeff(k)*((-3-4j)/1000)
    if l == -1:
        return rCoeff(k)*((-3+4j)/1000)
    return 0j

def modes():
    return [(k, l, fCoeff(k, l)) for k in range(-9, 10) for l in (-1, 0, 1) if abs(fCoeff(k, l)) > 0]

def AN(N):
    A = np.zeros((N, N), complex)
    for k, l, c in modes():
        A += c*weylT(N, l % N, k % N)
    return A

def UN(N, tau=1e-80):
    from scipy.linalg import expm
    return expm(1j*tau*N*AN(N)) @ MN(N)
