"""Compare the phase intervals with an independent dense Schur calculation."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from pathlib import Path
import sys

import numpy as np
from scipy.linalg import solve

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from critical_oscillation.check_matrix import chart
from effective_gaps.check_intervals import DIGITS, gap_coefficient
from spectrum.bgs_packet_check import rho_at


def verify():
    k = 2
    n = 7**k
    basis, terms = chart(k)
    x = np.arange(n)
    rho = rho_at(k)
    M = np.eye(n)[(pow(3+2*rho,-1,n)*x)%n]
    A = np.zeros((n,n),complex)
    for target,mult in terms:
        A[x,target] += mult
    I = np.eye(n)
    smallest_margin = float("inf")
    for ell in (4,6):
        for h in range(3):
            V = basis(ell,h)
            P = V@V.conj().T
            lam = np.trace(V.conj().T@M@V)/2
            H = V.conj().T@A@(lam*I+M)@solve(lam*I-M+P,(I-P)@A@V)/(2j)
            assert np.linalg.norm(H-H.conj().T)<2e-13
            eigenvalues = np.linalg.eigvalsh(H)
            gap = eigenvalues[1]-eigenvalues[0]
            lo,hi = gap_coefficient(ell,h)
            smallest_margin = min(smallest_margin,gap-lo/DIGITS,hi/DIGITS-gap)
    assert smallest_margin > 1e-11
    print(f"All six dense-matrix coefficients lie inside the exact intervals, margin {smallest_margin:.3g}.")


if __name__=="__main__":
    verify()
