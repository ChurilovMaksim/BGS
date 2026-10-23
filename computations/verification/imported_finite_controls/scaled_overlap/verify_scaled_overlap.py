#!/usr/bin/env python3
"""Finite controls for a scale-normalized Weyl-overlap deduction.

Dependencies: numpy. No network and no repository mutations.
The calculations below do NOT prove the analytic estimate or BGS.
Q is evaluated at an explicitly labelled proxy coupling, not at 1e-80.
Checks use explicit exceptions so they remain active under python -O.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def centered(x: int, p: int) -> int:
    return (int(x) + p // 2) % p - p // 2


def rho(v: tuple[int, int], p: int) -> int:
    return max(abs(centered(v[0], p)), abs(centered(v[1], p)))


def quadratic(v: tuple[int, int], p: int) -> int:
    a, b = v
    return (a*a - 2*b*b) % p


def step(v: tuple[int, int], p: int) -> tuple[int, int]:
    a, b = v
    return ((3*a + 4*b) % p, (2*a + 3*b) % p)


def all_orbits(p: int) -> list[list[tuple[int, int]]]:
    seen = np.zeros((p, p), dtype=bool)
    seen[0, 0] = True
    result = []
    for a in range(p):
        for b in range(p):
            if seen[a, b]:
                continue
            v0 = (a, b)
            orb = []
            v = v0
            while not seen[v]:
                seen[v] = True
                orb.append(v)
                v = step(v, p)
            require(v == v0, 'An orbit did not close at its initial point')
            result.append(orb)
    require(sum(map(len, result)) == p*p-1, 'Orbit partition incomplete')
    lengths = {len(o) for o in result}
    require(len(lengths) == 1, 'Nonzero orbit lengths differ at a prime')
    return result


def raw_weyl(n: int, v: tuple[int, int]) -> np.ndarray:
    a, b = v
    x = np.arange(n, dtype=np.int64)
    phase = (b * (x + pow(2, -1, n)*a)) % n
    out = np.zeros((n,n), dtype=np.complex128)
    out[x, (x+a)%n] = np.exp(2j*np.pi*phase/n)
    return out


def metaplectic(n: int) -> np.ndarray:
    x = np.arange(n, dtype=np.int64)[:,None]
    y = x.T
    z = (pow(8,-1,n)*(3*x*x-2*x*y+3*y*y)) % n
    return np.exp(-2j*np.pi*z/n)/np.sqrt(n)


def profile(q: np.ndarray) -> np.ndarray:
    return (1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))


def physical_generator(n: int) -> np.ndarray:
    x = np.arange(n, dtype=np.int64)
    q = x/n
    r = profile(q)
    diagonal = np.cos(14*np.pi*q)+r/10+r*np.sin(2*np.pi*q)/100-0.1
    A = np.diag(diagonal.astype(np.complex128))
    # This modular-midpoint expression equals the shifted physical symbol.
    shifted_q = ((x+pow(2,-1,n)) % n)/n
    upper = ((-3-4j)/5)*profile(shifted_q)/200
    A[x,(x+1)%n] += upper
    A[(x+1)%n,x] += upper.conjugate()
    return A


def coefficients(Q: np.ndarray) -> np.ndarray:
    n = Q.shape[0]
    x = np.arange(n, dtype=np.int64)
    out = np.empty((n,n), dtype=np.complex128)
    h = pow(2,-1,n)
    for a in range(n):
        diagonal = Q[x,(x+a)%n]
        out[a] = np.fft.fft(diagonal)/n * np.exp(-2j*np.pi*((x*h*a)%n)/n)
    return out


def F_from_coefficients(c: np.ndarray) -> np.ndarray:
    n = c.shape[0]
    P = np.abs(c)**2
    ft = np.fft.fft2(P)
    a = np.arange(n)[:,None]
    b = np.arange(n)[None,:]
    return ft[b,(-a)%n]


def exact_exponents() -> dict:
    beta = Fraction(1,65)
    cut = Fraction(16,65)
    require(cut/Fraction(16) == beta, 'Sublevel exponent mismatch')
    require(1-4*cut == beta, 'Normalized cutoff balance mismatch')
    require(2*65+1 == 131, 'Compression dimension budget mismatch')
    return {'beta': str(beta), 'cutoff_exponent': str(cut),
            'grid_compression_power': 131}


def check_geometry(orbits: list[list[tuple[int,int]]], p: int) -> dict:
    beta = 1/65
    d = len(orbits[0])
    box_checks = 0
    worst_weight_ratio = 0.
    for orb in orbits:
        require(all(quadratic(v,p)==quadratic(orb[0],p) for v in orb),
                'Quadratic invariant changed')
        hist = np.bincount([rho(v,p) for v in orb], minlength=p//2+1)
        require(hist[0] == 0, 'Zero entered a nonzero orbit')
        counts = np.cumsum(hist)
        for R in range(1,p//2+1):
            require(int(counts[R]) <= 4*R+2, 'Conic small-box count failed')
            box_checks += 1
        radii = np.sort(np.array([rho(v,p) for v in orb], dtype=float))
        require(np.all(radii >= np.arange(1,d+1)/6), 'Ordered-radius bound failed')
        lhs = float(np.mean(radii**(-beta)))
        upper = 6**beta/(1-beta)*d**(-beta)
        require(lhs <= upper*(1+1e-13), 'Weighted orbit bound failed')
        worst_weight_ratio = max(worst_weight_ratio,lhs/upper)
    return {'p':p,'period':d,'orbit_count':len(orbits),
            'exact_integer_small_box_checks':box_checks,
            'max_weight_bound_ratio':worst_weight_ratio}



def physical_weyl(n: int, a: int, b: int) -> np.ndarray:
    return ((-1) ** (a*b)) * raw_weyl(n,(a,b))


def positive_quantizer_checks() -> dict:
    """Exact finite definitions checked numerically; not a proof of asymptotic constants."""
    reports=[]
    for n in (3,5,7,11,31):
        xc=np.array([centered(x,n) for x in range(n)],dtype=float)
        psi=np.exp(-np.pi*xc**2/n)
        psi=psi/np.linalg.norm(psi)
        state=np.outer(psi,psi.conj())
        # a(q,p)=|1+0.3 exp(2pi i q)+0.2i exp(2pi i p)|^2
        f={(0,0):1.+0j,(1,0):.3+0j,(0,1):.2j}
        ahat={}
        for (k,l),z in f.items():
            for (u,v),w in f.items():
                idx=(k-u,l-v)
                ahat[idx]=ahat.get(idx,0j)+z*np.conjugate(w)
        frame=np.zeros((n,n),dtype=complex)
        Aw=np.zeros_like(frame)
        for q in range(n):
            for pp in range(n):
                T=raw_weyl(n,(-q,pp))
                rho=T@state@T.conj().T
                a=abs(sum(z*np.exp(2j*np.pi*(k*q+l*pp)/n) for (k,l),z in f.items()))**2
                frame+=rho/n
                Aw+=a*rho/n
        rhs=np.zeros_like(frame)
        for (k,l),z in ahat.items():
            W=physical_weyl(n,l,k)
            multiplier=np.vdot(psi,W.conj().T@psi)
            rhs+=z*multiplier*W
        frame_err=float(np.linalg.norm(frame-np.eye(n)))
        multiplier_err=float(np.linalg.norm(Aw-rhs))
        require(frame_err<3e-12,'Positive quantization is not unital')
        require(multiplier_err<5e-12,'Positive-quantizer Fourier multiplier failed')
        require(np.linalg.eigvalsh(Aw).min()>-2e-12,'Positive-quantizer positivity failed')
        ratios=[]; imag=[]
        K=int(np.sqrt(n))+2
        labels=[(a,b) for a in range(-K,K+1) for b in range(-K,K+1) if a or b]
        labels += [(n,0),(n,1),(1,n),(n+1,n-1)]
        for a,b in labels:
            W=physical_weyl(n,a,b)
            mv=np.vdot(psi,W@psi)
            ratios.append(float(abs(1-mv)*n/(a*a+b*b)))
            imag.append(float(abs(mv.imag)))
        require(max(imag)<2e-12,'Parity reality of coherent-state coefficient failed')
        # Conservative finite sanity bound only; analytic proof is separate.
        require(max(ratios)<100.,'Coherent multiplier finite sanity bound failed')
        shift=np.roll(psi,-1)
        reports.append({'N':n,'frame_error':frame_err,'multiplier_error':multiplier_err,
                        'min_positive_eigenvalue':float(np.linalg.eigvalsh(Aw).min()),
                        'max_multiplier_scaled_ratio':max(ratios),
                        'variance_over_N':float(np.sum(xc**2*abs(psi)**2)/n),
                        'gradient_energy_times_N':float(n*np.sum(abs(shift-psi)**2))})
    return {'status':'finite checks of positive quantizer, aliases and multipliers', 'reports':reports}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path('verification.json'))
    parser.add_argument('--tau-proxy', type=float, default=0.03)
    args = parser.parse_args()
    records = []
    max_parseval = 0.
    max_char = 0.
    max_cov = 0.
    rng = np.random.default_rng(15102026)
    for p in (31,61,127,199,239,509):
        A = physical_generator(p)
        require(np.max(np.abs(A-A.conj().T))<2e-14,'Generator not Hermitian')
        norm2 = float(np.trace(A@A).real/p)
        require(abs(norm2-66033/160000)<2e-12,'Physical Fourier norm incorrect')
        ev, vec = np.linalg.eigh(A)
        Q = (vec*np.exp(1j*args.tau_proxy*p*ev))@vec.conj().T
        c = coefficients(Q)
        P = np.abs(c)**2
        errp = abs(float(P.sum())-1)
        max_parseval = max(max_parseval,errp)
        require(errp<2e-12,'Parseval failed')
        F = F_from_coefficients(c)
        require(abs(F[0,0]-1)<2e-12,'Zero-probe trace failed')
        M = metaplectic(p)
        for v in ((1,0),(0,1),(p//3,p//4)):
            T=raw_weyl(p,v)
            direct = np.trace(Q.conj().T@T@Q@T.conj().T)/p
            err = abs(direct-F[v])
            max_char=max(max_char,err)
            require(err<5e-12,'Characteristic-function orientation failed')
            errc=float(np.linalg.norm(M@T@M.conj().T-raw_weyl(p,step(v,p)))/np.sqrt(p))
            max_cov=max(max_cov,errc)
            require(errc<2e-11,'Metaplectic covariance failed')
        orbits=all_orbits(p)
        geo=check_geometry(orbits,p)
        mean_abs=[]; mean_signed=[]
        for orb in orbits:
            vals=np.array([F[v] for v in orb])
            mean_abs.append(float(np.mean(np.abs(vals))))
            mean_signed.append(float(abs(np.mean(vals))))
        d=len(orbits[0])
        # This diagnostic is the original FULL spectral pair source, not an OTOC.
        U=Q@M
        z=np.linalg.eigvals(U)
        powers=np.arange(1,(p-1)//4+1)
        trace=np.sum(z[:,None]**powers[None,:],axis=0)
        weights=(1-4*powers/p)**2
        delta2=float(np.sum(weights*(np.abs(trace)**2-powers))/p**2)
        # Different observable: exact finite diagnostic, no asymptotic claim.
        geo.update({'tau_proxy':args.tau_proxy,
                    'max_orbit_average_absolute_otoc':max(mean_abs),
                    'max_absolute_orbit_average_otoc':max(mean_signed),
                    'full_pair_diagnostic_triangle_weight':delta2,
                    'norm2_generator':norm2})
        records.append(geo)
        print(json.dumps(geo,sort_keys=True),flush=True)
    # All entries small is not a power bound: Fourier matrix F^4=I.
    n=17
    x=np.arange(n)[:,None]
    D=np.exp(2j*np.pi*x*x.T/n)/np.sqrt(n)
    err_fourier=float(np.linalg.norm(np.linalg.matrix_power(D,4)-np.eye(n)))
    require(err_fourier<2e-12,'Fourier recurrence control failed')
    result={'status':'finite algebra and arithmetic controls only; no analytic/BGS certification',
            'physical_tau': '1e-80 (NOT simulated)', 'proxy_tau':args.tau_proxy,
            'exponent_checks':exact_exponents(), 'positive_quantizer':positive_quantizer_checks(), 'records':records,
            'max_parseval_error':max_parseval,'max_otoc_characteristic_error':max_char,
            'max_metaplectic_covariance_error':max_cov,'fourier_fourth_power_error':err_fourier,
            'python':sys.version,'numpy':np.__version__,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('All finite checks passed. Analytic constants and the Heisenberg spectral limit are NOT verified by this program.')

if __name__=='__main__':
    main()
