"""Exercise determinant-preserving balanced rounding and trace inequalities."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np
from scipy.optimize import linprog


def finite_round(angles, q, order):
    """Numerical basic point and deterministic conditional-expectation rounding."""
    n = len(angles)
    h = 2*np.pi/q
    lower = h*np.floor(angles/h)
    fractions = (angles-lower)/h
    m = np.arange(1,order+1)
    trace_columns = np.exp(1j*m[:,None]*lower)
    steps = trace_columns*np.expm1(1j*m[:,None]*h)
    last = h*np.linalg.norm(m)
    columns = np.vstack([steps.real,steps.imag,np.full(n,last)])
    eq = linprog(np.arange(1,n+1,dtype=float), A_eq=columns,
                 b_eq=columns@fractions, bounds=(0,1), method="highs-ds")
    assert eq.success and np.max(abs(columns@(eq.x-fractions)))<1e-7
    p = np.clip(eq.x,0,1)
    p[np.isclose(p,0,atol=1e-10,rtol=0)] = 0
    p[np.isclose(p,1,atol=1e-10,rtol=0)] = 1
    fractional = np.flatnonzero((p>0)&(p<1))
    assert len(fractional)<=2*order+1
    current_trace = trace_columns.sum(axis=1)+steps@p
    source_trace = np.exp(1j*m[:,None]*angles).sum(axis=1)
    offset = np.sum(lower+h*p-angles)
    residual = np.r_[(current_trace-source_trace).real,
                     (current_trace-source_trace).imag,
                     np.linalg.norm(m)*offset]
    bits = p.copy()
    for j in fractional:
        candidates = [residual+(bit-p[j])*columns[:,j] for bit in (0,1)]
        bit = int(np.linalg.norm(candidates[1])<np.linalg.norm(candidates[0]))
        bits[j] = bit
        residual = candidates[bit]

    rounded = lower+h*bits
    common = np.mean(angles-rounded)
    result = rounded+common
    assert abs(np.sum(result-angles))<1e-11
    assert np.max(abs(result-angles))<=h*(1+(2*order+1)/n)+1e-11
    trace_error = np.linalg.norm(np.exp(1j*m[:,None]*result).sum(axis=1)-source_trace)**2
    bound = 4*(2*order+1)*h*h*np.sum(m*m)+0.5*n*n*h**4*np.sum(m**4)
    assert trace_error<=bound+1e-10
    assert abs(abs(np.mean(np.exp(1j*q*result)))-1)<1e-12
    return result, len(fractional), trace_error


def verify():
    rng = np.random.default_rng(241122)
    n = 97
    angles = rng.uniform(-np.pi,np.pi,n)
    rounded, fractions, err = finite_round(angles,29,7)
    sample = rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    Q,_ = np.linalg.qr(sample)
    U = (Q*np.exp(1j*angles))@Q.conj().T
    V = (Q*np.exp(1j*rounded))@Q.conj().T
    E = np.linalg.norm(V-U,2)
    P = np.linalg.norm(abs(V)**2-abs(U)**2,2)
    assert P<=2*E+1e-13
    assert abs(np.linalg.det(U)/np.linalg.det(V)-1)<1e-11
    print(f"N={n}: {fractions} fractional coordinates, squared trace error {err:.5g}.")
    print("Determinant, common eigenbasis, revival and position-chain bound verified.")


if __name__=="__main__":
    verify()
