"""Independent position-matrix checks of the square and the Schur coefficient."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from pathlib import Path
import sys

import numpy as np
from scipy.linalg import expm, solve

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from critical_oscillation.check_matrix import chart
from exact_splitting.bgs_packet_check import ODD_MODES, direct_reductions, TAME_EXP
from spectrum.bgs_packet_check import SQUARES, p_log, rho_at, split


def verify_square_by_two_steps():
    k = 2
    n = 7**k
    s = n//7
    half = pow(2,-1,n)
    rho = rho_at(k)
    logs = {x:p_log(x,k) for x in range(1,n) if x%7}
    modes = [split(v,rho,n) for v in ODD_MODES]
    cyclotomic = [1,2,4,3,6,7,5]
    predicted = direct_reductions(k,True)
    for ell in (4,6):
        for h in range(3):
            out = [0]*(3*s)
            for x in logs:
                if x%7 not in SQUARES:
                    continue
                for a,b in modes:
                    y = (x+a)%n
                    for c,d in modes:
                        z = (y+c)%n
                        if z%7==0 or z%7 in SQUARES:
                            continue
                        phase = b*(x+a*half)+d*(y+c*half)+ell*(logs[z]-logs[x])
                        q,r = divmod(phase%n,s)
                        w = (1,2,3)[(h*(TAME_EXP[z%7]-TAME_EXP[x%7]))%3]
                        for i in range(3):
                            if cyclotomic[q]>>i&1:
                                out[r+i*s] ^= w
            assert next((i,v) for i,v in enumerate(out) if v)==predicted[ell,h]
    print("N=49: finite-field square agrees with explicit two-step position sums.")


def verify_schur(k):
    n = 7**k
    rho = rho_at(k)
    gamma = (3+2*rho)%n
    x = np.arange(n)
    M = np.eye(n)[(pow(gamma,-1,n)*x)%n]
    get_basis, terms = chart(k)
    A = np.zeros((n,n),complex)
    for target, values in terms:
        A[x,target] += values
    assert np.max(abs(A-A.conj().T))<1e-13
    I = np.eye(n)
    ell_values = (4,6) if k==2 else (4,18,25,32,39,46)
    dense_samples = 0
    for ell in ell_values:
        V = get_basis(ell,1)
        lam = np.trace(V.conj().T@M@V)/2
        assert np.linalg.norm(M@V-lam*V)<2e-13
        H1 = V.conj().T@A@V
        if np.linalg.norm(H1-np.trace(H1)*np.eye(2)/2)>1e-12:
            continue
        P = V@V.conj().T
        Q = I-P
        AQ = Q@A@V
        F = solve(lam*I-M+P, AQ)
        H2 = 0.5*(V.conj().T@A@(lam*I+M)@F)
        assert np.linalg.norm(H2+H2.conj().T)<1e-11
        gap = abs(np.linalg.eigvalsh(H2/1j)[1]-np.linalg.eigvalsh(H2/1j)[0])
        assert gap>1e-7
        # Compare the analytic Schur coefficient of the complete exponential
        # with the predicted first two coefficients at two nonzero parameters.
        errors = []
        for s in (4e-4,2e-4):
            U = expm(1j*s*A)@M
            schur = V.conj().T@U@V - (V.conj().T@U@Q)@solve(Q@(U-lam*I)@Q+P,Q@U@V)
            predicted = (schur/lam-np.eye(2)-1j*s*H1)/(-s*s)
            expected = H1@H1/2 + H2
            errors.append(np.linalg.norm(predicted-expected))
        assert errors[1] < 0.55*errors[0]+1e-8 and errors[1]<0.002
        dense_samples += 1
    assert dense_samples
    print(f"N={n}: exact propagator checked against the quadratic Schur matrix on {dense_samples} doublets.")


if __name__=="__main__":
    verify_square_by_two_steps()
    verify_schur(2)
    verify_schur(3)
