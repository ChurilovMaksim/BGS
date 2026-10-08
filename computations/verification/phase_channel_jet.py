#!/usr/bin/env python3
"""Finite orientation and falsifier controls for TRACE-053/054/056.

Continuous-phase integrals of degree n are replaced by (n+1)-root quadrature:
the Laurent exponents lie in [-n,n], so this replacement is exact algebraically.
Evaluation still uses float64/complex128. Matrix identities, circle quadrature
and random samples do not certify the general analytic theorems.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
from pathlib import Path
import numpy as np

SEED = 20261008
ATOL = 2e-9
RTOL = 3e-9


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def adj(a: np.ndarray) -> np.ndarray:
    return a.conj().swapaxes(-1, -2)


def tr(a: np.ndarray) -> np.ndarray:
    return np.trace(a, axis1=-2, axis2=-1).real


def close(a: np.ndarray, b: np.ndarray, message: str) -> None:
    require(bool(np.allclose(a, b, atol=ATOL, rtol=RTOL)), message)


def unitary(m: int, rng: np.random.Generator) -> np.ndarray:
    q, r = np.linalg.qr(rng.normal(size=(m, m)) + 1j*rng.normal(size=(m, m)))
    d = np.diag(r)
    return q * (d/np.abs(d)).conj()


def phase_channel(s: np.ndarray, n: int) -> np.ndarray:
    m = len(s)
    total = np.zeros((m*m, m*m), dtype=np.complex128)
    roots = np.exp(2j*np.pi*np.arange(n+1)/(n+1))
    for phases in itertools.product(roots, repeat=m):
        v = np.linalg.matrix_power(np.asarray(phases)[:, None]*s, n)
        total += np.kron(v, v.conj())
    return total/(n+1)**m


def channel_controls(rng: np.random.Generator) -> dict:
    count, max_error = 0, 0.0
    for m in (3, 4):
        dft = np.exp(2j*np.pi*np.outer(np.arange(m), np.arange(m))/m)/np.sqrt(m)
        for s in (dft, unitary(m, rng), np.eye(m)):
            ad = np.kron(s, s.conj())  # row-major vectorization
            pinch = np.diag([int(i == j) for i in range(m) for j in range(m)])
            a = pinch @ ad
            close(phase_channel(s, 1), a, 'degree-one channel')
            r2 = phase_channel(s, 2) - a @ a
            exact = np.zeros_like(r2)
            for i in range(m):
                for j in range(m):
                    if i != j:
                        exact[i*m+j] = s[i,j]*s[j,i].conjugate()*ad[j*m+i]
            close(r2, exact, 'degree-two transpose orientation')
            norm = np.linalg.norm(r2, 2)
            expected = max(abs(s[i,j]*s[j,i]) for i in range(m) for j in range(m) if i != j)
            close(np.asarray(norm), np.asarray(expected), 'exact degree-two norm')
            delta = np.max(np.abs(s)**2)
            for n in (2, 3, 4):
                diff = phase_channel(s, n) - np.linalg.matrix_power(a, n)
                bound = (math.factorial(n)-1)*np.sqrt(delta)+math.factorial(n)*n*(n-1)*delta
                require(np.linalg.norm(diff, 2) <= bound+ATOL, 'channel upper bound')
                count += 1
            max_error = max(max_error, float(np.max(np.abs(r2-exact))))
        for n, expected in ((2, 2-1/m), (3, 6-9/m+4/m**2)):
            moment = np.trace(phase_channel(dft, n)).real
            close(np.asarray(moment), np.asarray(expected), 'Fourier trace moment')
    return {'channel_order_cases': count, 'dimensions': [3,4], 'orders': [1,2,3,4],
            'max_degree_two_identity_error': max_error,
            'quadrature': 'n+1 roots per coordinate; exact characters, complex128 evaluation'}


def cascade_controls(rng: np.random.Generator) -> dict:
    max_error, min_gap, count = 0.0, math.inf, 0
    for m in range(1, 7):
        for _ in range(300):
            g = rng.normal(size=(m,m)) + 1j*rng.normal(size=(m,m))
            a = np.eye(m) + adj(g) @ g
            c0 = rng.normal(size=(m,m)) + 1j*rng.normal(size=(m,m))
            c = (c0+adj(c0))/2
            q = unitary(m, rng)
            rank = int(rng.integers(1,m+1))
            pmat = q[:,:rank] @ adj(q[:,:rank])
            p, pd = math.exp(float(rng.uniform(-2,2))), float(rng.normal())
            t = a+p*pmat
            td = c+1j*p*(a@pmat-pmat@a)+pd*pmat
            x, y = c+1j*p*a@pmat, pd*pmat-1j*p*pmat@a
            close(td, x+y, 'commutator split')
            close(pmat@y, y, 'left support PY=Y')
            lhs = float(tr(td @ np.linalg.solve(t,td)))
            rhs = float(tr(c @ np.linalg.solve(a,c))+p*p*tr(pmat@a)+p*tr(pmat@a@a)+pd*pd/p*rank)
            gap = rhs-lhs
            require(gap >= -ATOL-RTOL*abs(rhs), 'weighted matrix Cauchy')
            cube = tr(t@t@t)-tr(a@a@a)
            increment = 3*p*tr(pmat@a@a)+3*p*p*tr(pmat@a)+p**3*rank
            close(np.asarray(cube),np.asarray(increment),'noncommutative cubic increment')
            err = float(abs(cube-increment)/(1+abs(increment)))
            max_error, min_gap, count = max(max_error,err), min(min_gap,gap), count+1
    return {'cases':count,'dimensions':[1,6],'projection_ranks':'1..m',
            'max_relative_cubic_identity_error':max_error,'minimum_Cauchy_gap':min_gap}


def inner_jets(m: int, poles: list[complex], rng: np.random.Generator,
               theta: np.ndarray) -> tuple[np.ndarray,np.ndarray,np.ndarray]:
    z = np.exp(1j*theta)[:,None,None]
    eye = np.eye(m)[None,:,:]
    f, fp, fpp = z*eye, np.broadcast_to(eye,(len(theta),m,m)).copy(), np.zeros((len(theta),m,m),complex)
    for pole in poles:
        q = unitary(m,rng)
        rank = int(rng.integers(1,m+1))
        p = (q[:,:rank] @ adj(q[:,:rank]))[None,:,:]
        den = 1-pole.conjugate()*z
        b = (z-pole)/den
        bp = (1-abs(pole)**2)/den**2
        bpp = 2*pole.conjugate()*(1-abs(pole)**2)/den**3
        factor, factorp, factorpp = eye+(b-1)*p, bp*p, bpp*p
        f, fp, fpp = f@factor, fp@factor+f@factorp, fpp@factor+2*fp@factorp+f@factorpp
    return f,fp,fpp


def jet_controls(rng: np.random.Generator) -> dict:
    theta = 2*np.pi*np.arange(8192)/8192
    z = np.exp(1j*theta)[:,None,None]
    omega = 1+.4*np.cos(theta)+.2*np.cos(2*theta)
    omegapp = -.4*np.cos(theta)-.8*np.cos(2*theta)
    count, max_ratio, max_identity_error = 0, 0.0, 0.0
    for m in (1,2,3):
        for degree in (0,1,3,6):
            for _ in range(4):
                poles = [float(rng.choice([0,.3,.7,.95,.98]))*np.exp(2j*np.pi*rng.random()) for _ in range(degree)]
                f, fp, fpp = inner_jets(m,poles,rng,theta)
                t = adj(f) @ (z*fp)
                td = -1j*(adj(fp)@fp)+1j*t+1j*(adj(f)@(z*z*fpp))
                close(t,adj(t),'Hermitian delay')
                require(np.linalg.eigvalsh(t).min() >= 1-ATOL, 'T>=I')
                close(adj(f)@(z*z*fpp),t@t-t-1j*td,'exact right-jet identity')
                invt = np.linalg.inv(t)
                lhs = tr(adj(fpp)@fpp@invt)
                energy = tr(td@invt@td)
                cubic, square, linear = tr(t@t@t), tr(t@t), tr(t)
                close(lhs,cubic-2*square+linear+energy,'right weight norm expansion')
                rhs = (4*cubic-6*square+2*linear)/3
                require(lhs.mean() <= rhs.mean()+ATOL+RTOL*abs(rhs.mean()),'sharp integrated jet')
                localized_rhs = omega*rhs+(2/3)*omegapp*linear
                require((omega*lhs).mean() <= localized_rhs.mean()+ATOL+RTOL*abs(localized_rhs.mean()),'localized jet with penalty')
                max_ratio = max(max_ratio,float(lhs.mean()/cubic.mean()))
                err = np.max(np.abs(lhs-(cubic-2*square+linear+energy))/(1+np.abs(lhs)))
                max_identity_error = max(max_identity_error,float(err))
                count += 1
    scalar = []
    for r in (.5,.9,.99,.999):
        # Analytic moments give a rigorous sandwich, not a near-pole quadrature.
        m2, m3 = (1+r*r)/(1-r*r), (1+4*r*r+r**4)/(1-r*r)**2
        denom = m3+3*m2+4
        scalar.append({'r':r,'lower_ratio':(4*m3/3+2/3)/denom,
                       'upper_ratio':(4*m3/3+m2-1/3)/denom})
    return {'cases':count,'dimensions':[1,2,3],'factor_counts':[0,1,3,6],
            'circle_points':len(theta),'largest_computed_ratio':max_ratio,
            'max_relative_norm_identity_error':max_identity_error,'scalar_sharpness_sandwich':scalar,
            'scope':'finite quadrature and orientation checks; no theorem or optimality certificate'}


def scalar_flow_controls(rng: np.random.Generator) -> dict:
    """Test common-phase smoothing independently of the pinching-rate proof."""
    from scipy.linalg import expm
    from scipy.optimize import linear_sum_assignment
    phase = 2*np.pi*np.arange(16384)/16384
    rotations = np.exp(1j*phase)
    cases, max_derivative_error, min_margin = 0, 0.0, math.inf
    for m in (3,4):
        s = np.exp(2j*np.pi*np.outer(np.arange(m),np.arange(m))/m)/np.sqrt(m)
        h0 = rng.normal(size=(m,m))+1j*rng.normal(size=(m,m))
        h0 = (h0+adj(h0))/2
        h0 -= np.trace(h0)/m*np.eye(m)
        h = np.eye(m)+.3*h0/np.linalg.norm(h0,2)
        for _ in range(4):
            d = np.diag(np.exp(2j*np.pi*rng.random(m)))
            base = d@s
            for x in (-.3,.3):
                w = base@expm(1j*x*h/m)
                v = np.exp(1j*x/m)*base
                ew, ev = np.linalg.eigvals(w),np.linalg.eigvals(v)
                distances = np.abs(np.angle(ew[:,None]/ev[None,:]))
                rows, cols = linear_sum_assignment(distances)
                cost = distances[rows,cols].sum()
                for absorption in (.4,2.0):
                    radius = math.exp(-absorption/m)
                    derivative = np.mean(radius/np.abs(1-radius*rotations)**2)
                    exact = 1/(2*math.sinh(absorption/m))
                    close(np.asarray(derivative),np.asarray(exact),'common-phase L1 derivative')
                    zw = np.mean(1/(1-radius*rotations[:,None]*ew[None,:])-1,axis=1)
                    zv = np.mean(1/(1-radius*rotations[:,None]*ev[None,:])-1,axis=1)
                    lhs, rhs = float(np.abs(zw-zv).mean()),float(cost*exact/m)
                    require(lhs <= rhs+1e-7,'common-phase scalar-source transport')
                    max_derivative_error=max(max_derivative_error,abs(derivative-exact))
                    min_margin=min(min_margin,rhs-lhs)
                    cases += 1
    return {'cases':cases,'dimensions':[3,4],'common_phase_points':len(phase),
            'max_derivative_integral_error':max_derivative_error,
            'minimum_transport_margin':min_margin,
            'scope':'finite common-phase kernel control; no averaged-pinching rate or stochastic-flow limit certified'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    rng = np.random.default_rng(SEED)
    result = {'status':'PASS','seed':SEED,'numpy':np.__version__,
              'arithmetic':'float64/complex128','atol':ATOL,'rtol':RTOL,
              'channel':channel_controls(rng),'cascade':cascade_controls(rng),
              'jets':jet_controls(rng),'scalar_flow':scalar_flow_controls(rng)}
    text = json.dumps(result,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    print(text,end='')


if __name__ == '__main__':
    main()
