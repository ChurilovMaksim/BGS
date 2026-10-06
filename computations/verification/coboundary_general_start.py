#!/usr/bin/env python3
"""Finite controls for FLOW-012/013 and the FM-017 Poisson corollary.

Exact rational normalization/exponents, high-precision balanced-cluster
traces, and independent complex128 spectral-matching/window geometry.
The matrix perturbations below are NOT Brownian endpoint samples.
No numerical assertion certifies an asymptotic limit or nonvanishing
of all infinitely many traces.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import mpmath as mp
import numpy as np
import scipy
from scipy.linalg import expm
from scipy.optimize import linear_sum_assignment


def exact_controls():
    a, beta = Fraction(26, 3), Fraction(2, 3)
    exponents = {
        "sqrt_time": -beta/2, "initial_centering": Fraction(-1),
        "exit": 4-a, "boundary_layer": 9-2*a,
        "linear_step": 9-a-beta, "quadratic_step": 10-2*a-beta,
        "steps": 4*a-beta,
    }
    assert exponents == dict(sqrt_time=Fraction(-1, 3),
        initial_centering=Fraction(-1), exit=Fraction(-14, 3),
        boundary_layer=Fraction(-25, 3), linear_step=Fraction(-1, 3),
        quadratic_step=Fraction(-8), steps=Fraction(34))
    dimensions = list(range(3, 30, 2))
    for n in dimensions:
        # Sum diagonal squares directly in the real HS-orthonormal basis.
        for k in range(n):
            diagonal = sum((Fraction(1, j*(j+1)) for j in range(k+1, n)),
                           Fraction(0))
            if k:
                diagonal += Fraction(k, k+1)
            assert diagonal == 1-Fraction(1, n)
            # Real/imaginary off-diagonal pair adds one for each partner.
            traceless = (n-1+diagonal)/n
            assert traceless == 1-Fraction(1, n*n)
            assert traceless+Fraction(1, n*n) == 1
        t, eps = Fraction(1, n), Fraction(1, n**10)
        h = eps**4/2
        steps = t//h
        assert 0 <= t-steps*h < h
    # Stationary forcing and summed initial transient bookkeeping.
    assert 2+6-4 == 4 and 2+24-4 == 22
    assert 4+6-1 == 9
    return {"exponents": {k: str(v) for k, v in exponents.items()},
            "brownian_basis_dimensions": dimensions,
            "generic_epsilon_N_minus_10_errors":
                ["sqrt(t)", "N^-1", "N^-6", "N^-11", "t/N", "t*N^-10"]}


def cluster_controls():
    mp.mp.dps = 120
    count, max_trace_ratio, max_first_two, bounds = 0, mp.mpf(0), mp.mpf(0), []
    for q in (3, 5, 7, 9, 11, 13):
        qbounds = []
        for remainder in range(q):
            n = q**10+remainder
            if n % 2 == 0:
                n += q
            assert n % 2 == 1 and n % q == remainder and n >= q**10
            assert n < (q+2)**10  # q is the largest admissible odd integer.
            multiplicities = [n//q]*q
            for ell in range(remainder):
                multiplicities[ell*q//remainder] += 1
            assert sum(multiplicities) == n
            traces = []
            for j in range(1, min(q-1, 8)+1):
                step = 2j*mp.pi*j/n**5
                p = sum(mp.exp(2j*mp.pi*j*k/q)*mp.expm1(step*m)/mp.expm1(step)
                        for k, m in enumerate(multiplicities))
                p += mp.expm1(1j*mp.mpf(j)/n**4)
                bound = 2*mp.pi*j+2*mp.pi*j/n**3+mp.mpf(j)/n**4
                assert abs(p) <= bound+mp.mpf("1e-90")
                assert abs(p) > mp.mpf("1e-90")  # sampled j only
                max_trace_ratio = max(max_trace_ratio, abs(p)/bound)
                traces.append(abs(p))
                count += 1
            first_two = sum(traces[:2])
            assert first_two < 20
            max_first_two = max(max_first_two, first_two)
            delta, b, t = (2*mp.pi+1)/n**4, mp.mpf(1)/q**2, mp.mpf(1)/q**6
            # R3 for I=[-1/2,1/2], using 2*pi*R/N rather than q/N.
            probability_bound = q/mp.pi*(b+mp.pi/n)+(2*delta**2+mp.pi**2*t/2)/b**2
            qbounds.append(float(probability_bound))
        bounds.append({"Q": q, "all_remainders": q,
                       "max_finite_empty_window_bound": max(qbounds)})
    return {"precision_decimal_digits": mp.mp.dps, "trace_cases": count,
            "max_trace_to_analytic_bound_ratio": float(max_trace_ratio),
            "max_first_two_sum": float(max_first_two), "finite_bounds": bounds,
            "nonvanishing_scope": "sampled powers only; the universal result is analytic"}


def circular_interval_union_probability(angles, n):
    """Exact geometric origin measure for I=[-1/2,1/2], to rounding."""
    twopi, radius = 2*np.pi, np.pi/n
    pieces = []
    for theta in np.mod(angles, twopi):
        lo, hi = theta-radius, theta+radius
        if lo < 0:
            pieces.extend([(0., hi), (lo+twopi, twopi)])
        elif hi > twopi:
            pieces.extend([(lo, twopi), (0., hi-twopi)])
        else:
            pieces.append((lo, hi))
    pieces.sort()
    total, lo, hi = 0., *pieces[0]
    for left, right in pieces[1:]:
        if left <= hi:
            hi = max(hi, right)
        else:
            total += hi-lo
            lo, hi = left, right
    return (total+hi-lo)/twopi


def geometry_controls():
    rng = np.random.default_rng(20261004)
    cases, max_match_excess, max_angle_excess, nontrivial = [], 0., 0., 0
    for n, q in ((9, 3), (15, 3), (21, 5), (31, 7), (61, 7)):
        multiplicities = [n//q]*q
        for ell in range(n % q):
            multiplicities[ell*q//(n % q)] += 1
        angles = np.array([2*np.pi*k/q+2*np.pi*s/n**5
                          for k, m in enumerate(multiplicities) for s in range(m)])
        angles[0] += n**-4
        eig_a, delta = np.exp(1j*angles), (2*np.pi+1)*n**-4
        a = np.diag(eig_a)
        z = rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        h = (z+z.conj().T)/(2*np.sqrt(n))
        centers = 2*np.pi*np.arange(q)/q
        for scale in (0., 1e-6, 1e-4, .01):
            v = expm(1j*scale*h)@a
            eig_v = np.linalg.eigvals(v)
            hs_mean = float(np.sum(abs(v-a)**2)/n)
            cost = abs(eig_v[:, None]-eig_a[None, :])**2
            rows, columns = linear_sum_assignment(cost)
            match_mean = float(np.sum(cost[rows, columns])/n)
            excess = match_mean-hs_mean
            assert excess < 2e-12
            max_match_excess = max(max_match_excess, excess)
            theta = np.angle(eig_v)
            distances = abs(np.angle(np.exp(1j*(theta[:, None]-centers))))
            nearest_mean = float(np.mean(np.min(distances, axis=1)**2))
            angular_bound = 2*delta**2+np.pi**2*hs_mean/2
            assert nearest_mean-angular_bound < 2e-12
            max_angle_excess = max(max_angle_excess, nearest_mean-angular_bound)
            probability = circular_interval_union_probability(theta, n)
            b = .005
            bound = q/np.pi*(b+np.pi/n)+angular_bound/b**2
            assert probability <= bound+2e-11
            nontrivial += bound < 1
            cases.append({"N": n, "Q": q, "scale": scale,
                          "origin_nonempty_probability": probability,
                          "deterministic_window_bound": bound})
    assert nontrivial > 0
    return {"seed": 20261004, "cases": cases,
            "max_matching_excess": max_match_excess,
            "max_angular_excess": max_angle_excess,
            "bounds_below_one": nontrivial,
            "sampling": "deterministic exponential of seeded GUE; not Brownian endpoints"}


def poisson_controls():
    # Independent direct spectral rational transform vs Fourier tail budget.
    cases = []
    for n in (9, 15, 31):
        angles = 2*np.pi*np.arange(n)/n+.01*np.sin(2*np.pi*np.arange(n)/n)
        spectrum = np.exp(1j*angles)
        jmax = n//2
        d = max(abs(np.mean(spectrum**j)) for j in range(1, jmax+1))
        for g in (.2, .5, 1.):
            z = np.exp(-g+2j*np.pi*np.arange(257)/257)
            transform = np.mean((spectrum[:, None]+z)/(spectrum[:, None]-z), axis=0)
            bound = 2*(d+np.exp(-(jmax+1)*g))/(1-np.exp(-g))
            error = float(np.max(abs(transform-1)))
            assert error <= bound+2e-13
            w = (.2+.1j)/n
            moved = (spectrum-w)/(1-w.conjugate()*spectrum)
            moved_transform = np.mean((moved[:, None]+z)/(moved[:, None]-z), axis=0)
            centering_error = float(np.max(abs(moved_transform-transform)))
            centering_bound = 8*abs(w)*np.exp(-g)/(1-np.exp(-g))**2
            assert centering_error <= centering_bound+2e-13
            cases.append({"N": n, "J": jmax, "g": g, "error": error,
                          "M1_bound": float(bound),
                          "Mobius_stability_error": centering_error,
                          "Mobius_stability_bound": float(centering_bound)})
    return cases


def kernel_controls():
    """Prior arbitrary-start biorthogonal formula, finite calibration only."""
    results = []
    for n in (3, 5, 7, 9):
        modes = np.arange(-(n//2), n//2+1)
        grid = 2*np.pi*np.arange(1024)/1024
        for warped in (False, True):
            alpha = 2*np.pi*np.arange(n)/n
            if warped:
                alpha = alpha+.15*np.sin(alpha)
            vandermonde = np.exp(1j*modes[:, None]*alpha)
            coefficients = np.linalg.inv(vandermonde)
            for t in (.05, .2, 1.):
                tau = t/(2*n)
                cutoff = int(np.ceil(np.sqrt(40/tau)))+n
                heat_modes = np.arange(-cutoff, cutoff+1)
                backward = coefficients@(np.exp(tau*modes**2)[:, None]*
                                         np.exp(1j*modes[:, None]*grid))
                forward = (np.exp(-1j*alpha[:, None]*heat_modes)*
                           np.exp(-tau*heat_modes**2))@np.exp(1j*heat_modes[:, None]*grid)
                # Bilinear pairing; a conjugate transpose would be wrong.
                gram = backward@forward.T/len(grid)
                gram_error = float(np.max(abs(gram-np.eye(n))))
                trace_error = float(abs(np.mean(np.sum(backward*forward, axis=0))-n))
                assert gram_error < 2e-12 and trace_error < 2e-12
                alias_error = None
                if not warped:
                    x, y = .37, 1.13
                    rx = coefficients@(np.exp(tau*modes**2+1j*modes*x))
                    qy = np.sum(np.exp(-tau*heat_modes**2+
                                      1j*(y-alpha[:, None])*heat_modes), axis=1)
                    direct = np.sum(rx*qy)
                    alias = sum(np.exp(-tau*((ell+r*n)**2-ell**2)+
                                       1j*ell*x-1j*(ell+r*n)*y)
                                for ell in modes for r in range(-cutoff//n-2, cutoff//n+3))
                    alias_error = float(abs(direct-alias))
                    assert alias_error < 2e-12
                results.append({"N": n, "spectrum": "warped" if warped else "clock",
                    "time": t, "heat_coefficient": tau,
                    "biorthogonal_error": gram_error, "trace_error": trace_error,
                    "clock_alias_error": alias_error})
    return {"cases": results, "measure": "dtheta/(2*pi)",
            "prior_formula": "Kieburg-Li-Zhang-Forrester, arXiv:2012.11993v2 Prop.21",
            "scope": "finite algebraic calibration; no saddle/Fredholm asymptotic certificate"}


def phase_controls():
    """Direct sine-product potential; finite M9/M10 calibration on a clock."""
    n, jmax, g, t = 1001, 500, .02, .2
    # Low Fourier coefficients are exactly zero by character orthogonality.
    v = np.exp(-(jmax+1)*g)/((jmax+1)*(1-np.exp(-g)))
    assert g <= t/8 and v <= t/512
    alpha = 2*np.pi*np.arange(n)/n
    cases = []
    def potential(theta, y):
        with np.errstate(divide="ignore"):
            return float(np.mean(np.log(abs(2*np.sin((theta+1j*y-alpha)/2)))))
    for theta in (0., .031, 2*np.pi/7):
        reference = -t/8+potential(theta, t/2)
        for y in (0., .005, .01, .0199, .02, .025, .049, .05,
                  .07, .074, .126, .15, .2, .5, 2.):
            for sign in (-1, 1):
                q = potential(theta, sign*y)
                action = -y*y/(2*t)+q
                if y >= g:
                    assert abs(q-y/2) <= v+3e-13
                else:
                    assert q <= g/2+v+3e-13
                if y <= t/4:
                    bound = -t/64
                elif abs(y-t/2) >= t/8:
                    bound = -(y-t/2)**2/(4*t)
                else:
                    continue
                assert action-reference <= bound+3e-13
                cases.append({"theta": theta, "y": sign*y,
                    "action_minus_reference": None if not np.isfinite(action) else action-reference,
                    "M10_bound": bound})
    return {"N": n, "J": jmax, "g": g, "time": t, "v_bound": float(v),
            "cases": cases, "negative_infinity_convention": "null at a real root",
            "scope": "direct complex128 clock potential only; no general asymptotic certificate"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = {"claim_ids": ["BGS-FLOW-012", "BGS-FLOW-013", "BGS-FM-017"],
            "status": "PASS", "arithmetic": ["exact Fraction", "mpmath 120 digits", "complex128"],
            "versions": {"Python": platform.python_version(), "NumPy": np.__version__,
                         "SciPy": scipy.__version__, "mpmath": mp.__version__},
            "exact": exact_controls(), "clusters": cluster_controls(),
            "geometry": geometry_controls(), "poisson": poisson_controls(),
            "prior_kernel_calibration": kernel_controls(),
            "vertical_phase_calibration": phase_controls(),
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "exclusions": ["No Brownian sampling or enormous-step simulation",
                "No asymptotic proof from finite tests", "No all-power numerical certificate",
                "Finite checks do not establish actual-map Dyson relaxation or deterministic noise removal",
                "No novelty or analytic Lean claim"]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2)+"\n")
    print("PASS general-start comparison, cluster geometry and Poisson finite controls")


if __name__ == "__main__":
    main()
