"""Direct finite-matrix checks of adjacent compressions and orbit transfer."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from itertools import product
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import eigh

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from critical_block.bgs_packet_check import alpha_at
from critical_oscillation.bgs_packet_check import (STABLE_A, STABLE_B, depth,
                                        critical_phase, eta_exponent)
from spectrum.bgs_packet_check import COEFFICIENTS, SQUARES, p_log, rho_at, split
from split_law.check_matrix import TAME_EXP


def phase_factor(phase, hessian, tame, k, conductor):
    gauss = 1
    if conductor % 2:
        gauss = np.mean(np.exp(2j*np.pi*(hessian*np.arange(7)**2%7)/7))*np.sqrt(7)
    return gauss * np.exp(2j*np.pi*(phase/7**k + tame/3))


def predict_cross(ell, h, k):
    V, V2, W = [
        phase_factor(phase, c, (h+1)*TAME_EXP[y%7]-h*TAME_EXP[x%7], k, k)
        for v, root in [(STABLE_A,1), (STABLE_A,2), (STABLE_B,1)]
        for phase, c, x, y in [critical_phase(v, ell, k, root)]
    ]
    eta = np.exp(2j*np.pi*eta_exponent(k)/7**k)
    Z = -2*V + (1+eta)*W
    off = V*V2*np.conj(Z)
    return (7/1200)*np.diag([(3+4j)/5, (3-4j)/5]) @ np.array([[Z,off],[off,Z]])


def predict_diagonal(ell, h, k):
    n = 7**k
    rho = rho_at(k)
    output = np.zeros((2,2),complex)
    for label, raw_coeff in COEFFICIENTS.items():
        a,b = split(label,rho,n)
        d = depth(label)
        a0,b0 = split(tuple(z//7**d for z in label),rho,n)

        def polynomial(x):
            return b0*x*(x+a)-ell*a0

        for root in range(1,7):
            if (root+a)%7 == 0 or polynomial(root)%7:
                continue
            if (2*root+a)%7 == 0:
                assert not any(polynomial(root+7*j)%49 == 0 for j in range(7))
                assert k>=4
                continue
            for i in range(1,k):
                step = 7**i
                root, = [root+step*j for j in range(7)
                         if polynomial(root+step*j)%(step*7)==0]
            y = (root+a)%n
            c = b0*(2*root+a)*pow(2*root*y,-1,7)%7
            phase = (b*(root+a*pow(2,-1,n))+ell*(p_log(y,k)-p_log(root,k)))%n
            tame = h*(TAME_EXP[y%7]-TAME_EXP[root%7])
            entry = int(root%7 not in SQUARES), int(y%7 not in SQUARES)
            output[entry] += (
                (7/3)*7**(d/2)*complex(*raw_coeff)/4000
                * phase_factor(phase,c,tame,k,k-d)
            )
    return output


def chart(k):
    n = 7**k
    rho = rho_at(k)
    x = np.arange(n)
    units = x%7!=0
    plus = np.isin(x%7,list(SQUARES))
    logs = np.array([p_log(int(j), k) if units[j] else 0 for j in x])
    tame = np.array([TAME_EXP.get(j%7, 0) for j in x])
    terms = []
    for label, raw_coeff in COEFFICIENTS.items():
        a,b = split(label,rho,n)
        oscillator = np.exp(2j*np.pi*((b*(x+a*pow(2,-1,n)))%n)/n)
        terms.append(((x+a)%n, complex(*raw_coeff)*oscillator/4000))

    def basis(ell, h):
        chi = np.exp(2j*np.pi*((ell*logs)%n/n+(h%3)*tame/3))/np.sqrt(3*n/7)
        return np.stack((chi*plus,chi*(units&~plus)),axis=1)

    return basis, terms


def check_compressions(k, dense):
    n = 7**k
    basis,terms = chart(k)
    kappa = 0.6
    rho = rho_at(k)
    inv_gamma = pow(3+2*rho,-1,n)
    if dense:
        A = np.zeros((n,n),complex)
        x = np.arange(n)
        for target,mult in terms:
            A[x,target] += mult
        assert np.max(abs(A-A.conj().T))<1e-12
        values,vecs = eigh(A)
        t = kappa/np.sqrt(n)
        K = 2*n*(vecs*np.tan(t*values/2))@vecs.conj().T
        U = ((vecs*np.exp(1j*t*values))@vecs.conj().T)[:,(3+2*rho)*x%n]
        assert np.allclose(U@U.conj().T,np.eye(n),atol=2e-11)
    cross_error = 0.0
    diag_error = 0.0
    for ell,h in product((5,12,19,26,54),range(3)):
        next_ell = ell+alpha_at(k)
        V = np.column_stack((basis(ell,h),basis(next_ell,h+1)))
        assert np.max(abs(V.conj().T@V-np.eye(4)))<1e-11
        AV = sum((mult[:,None]*V[target] for target,mult in terms),np.zeros_like(V))
        block = np.sqrt(n)*(V.conj().T @ AV)
        cross_error = max(cross_error,np.max(abs(block[:2,2:]-predict_cross(ell,h,k))))
        if ell%49==5 and k>=4:
            err = max(np.max(abs(block[:2,:2]-predict_diagonal(ell,h,k))),
                      np.max(abs(block[2:,2:]-predict_diagonal(next_ell,h+1,k))))
            diag_error = max(diag_error,err)
        if dense:
            m = 3*n//7
            lam = np.exp(2j*np.pi*(ell*p_log(inv_gamma,k)%n/n+h*TAME_EXP[inv_gamma%7]/3))
            phase_step = np.exp(2j*np.pi/m)
            J = V.conj().T@U@V
            R = n/(1j*lam)*J[:2,2:]
            S = AV.conj().T@AV
            taylor = phase_step*(kappa*block[:2,2:]+1j*kappa**2/2*S[:2,2:])
            norm_A = np.max(abs(values))
            assert np.linalg.norm(R-taylor,2) <= n*(t*norm_A)**3/6+1e-10
            diag_tangent = np.diag([0,0,2*n*np.tan(np.pi/m),2*n*np.tan(np.pi/m)])
            cayley = V.conj().T@K@V+diag_tangent
            error = np.linalg.norm(cayley-kappa*block-diag_tangent,2)
            assert error <= 2*n*(np.tan(t*norm_A/2)-t*norm_A/2)+1e-10
    assert cross_error<2e-10 and diag_error<2e-10
    print(f"N={n}: largest cross-entry error {cross_error:.3g}"
          + (f", diagonal-entry error {diag_error:.3g}." if k>=4 else "."))


def check_transfer(k):
    """Compute full-layer transfer via dilation traces, without stationary phase."""
    n = 7**k
    m = 3*n//7
    _,terms = chart(k)
    rho = rho_at(k)
    gamma = (3+2*rho)%n
    x = np.arange(n)
    A = np.zeros((n,n),complex)
    for target,mult in terms:
        A[x,target] += mult
    overlaps = []
    mult = 1
    for _ in range(m):
        inv = pow(mult,-1,n)
        val = sum(np.vdot(v,A[inv*x%n,inv*tar%n]) for tar,v in terms)
        overlaps.append(val)
        mult = mult*gamma%n
    g_ratio = (1+7*rho)*pow(1-7*rho,-1,n)%n
    gamma_exp = {pow(gamma,r,n):r for r in range(m)}
    def angle(d):
        ratio = (1+d*rho)*pow(-1+d*rho,-1,n)%n
        return 2*np.pi*gamma_exp[ratio]/m

    for h in range(8):
        actual = np.sum(np.exp(2j*np.pi*h*np.arange(m)/m)*overlaps)/n
        expected = (1233/160000+(567/200 if h%7==0 else 0)
                    +(400*np.cos(2*np.pi*h*gamma_exp[g_ratio]/m)
                      -28*np.cos(h*angle(6))-28*np.cos(h*angle(8))
                      -112*np.cos(2*np.pi*h/m))/16000000)
        assert abs(actual-expected)<2e-10
    print(f"N={n}: eight full-layer transfer weights agree with dilation traces.")


if __name__ == "__main__":
    check_compressions(3,True)
    check_compressions(4,False)
    check_transfer(3)
