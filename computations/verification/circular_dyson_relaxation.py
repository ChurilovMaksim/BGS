#!/usr/bin/env python3
"""Finite independent normalization/residue controls for FLOW-014.

Fourier Vandermonde interpolation is compared with sine products and a
periodic rectangle quadrature, including the crossing residue on both
sides of the horizontal contours. These computations neither establish
the asymptotic contour estimates nor sample Brownian endpoints.
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
import numpy as np
import scipy
from scipy.special import roots_hermite


def sine_product(z, alpha):
    return np.prod(2*np.sin((np.asarray(z)[..., None]-alpha)/2), axis=-1)


def heat_fourier(z, modes, coefficients):
    return np.exp(1j*np.asarray(z)[..., None]*modes)@coefficients


def finite_controls():
    time, height, phi, nodes = .4, .2, .93, 4096
    tolerance = 5e-11
    result, backward_result = [], []
    max_interpolation, max_residue, max_backward, max_heat = 0., 0., 0., 0.
    hermite_x, hermite_weights = roots_hermite(96)
    # Independent symbolic exponent check of the balanced general-start rule:
    # t=N^-beta, epsilon=N^-9 / sqrt(t), n=2*t^3*N^36.
    balanced = []
    for beta in (Fraction(0), Fraction(2, 3), Fraction(1)):
        epsilon_exponent = -9+beta/2
        errors = [-beta/2, Fraction(-1), 4+epsilon_exponent,
                  9+2*epsilon_exponent, 9+epsilon_exponent-beta,
                  10+2*epsilon_exponent-beta]
        assert all(exponent <= -beta/2 for exponent in errors)
        assert 36-3*beta == -beta-4*epsilon_exponent
        balanced.append({"beta": str(beta), "epsilon_exponent": str(epsilon_exponent),
            "step_exponent": str(36-3*beta), "error_exponents": [str(x) for x in errors]})
    for n in (3, 5, 7, 9):
        ell = np.arange(-(n//2), n//2+1)
        tau = time/(2*n)
        # |exp(-tau*m^2+i*m*z)| <= exp(-tau*m^2+0.6*|m|).
        # The cutoff is beyond the Gaussian's maximum plus sqrt(80/tau).
        cutoff = int(np.ceil(.6/(2*tau)+np.sqrt(80/tau)))+n
        modes = np.arange(-cutoff, cutoff+1)
        coefficient = np.exp(-tau*modes**2-1j*modes*phi)
        grid = phi-np.pi+2*np.pi*np.arange(nodes)/nodes
        lower, upper = grid-1j*height, grid+1j*height
        qlower = heat_fourier(lower, modes, coefficient)
        qupper = heat_fourier(upper, modes, coefficient)
        # Separate winding-Gaussian calibration, not the same Fourier code.
        for z in (.31, .31+.2j, .31+.6j):
            wrapped = np.sqrt(2*np.pi*n/time)*sum(
                np.exp(-n*(z-phi+2*np.pi*k)**2/(2*time))
                for k in range(-8, 9))
            error = float(abs(heat_fourier(z, modes, coefficient)-wrapped))
            assert error < tolerance
            max_heat = max(max_heat, error)
        for warped in (False, True):
            alpha = 2*np.pi*np.arange(n)/n
            if warped:
                alpha = alpha+.17*np.sin(alpha)
            inverse = np.linalg.inv(np.exp(1j*ell[:, None]*alpha))
            qalpha = heat_fourier(alpha, modes, coefficient)
            plower, pupper = sine_product(lower, alpha), sine_product(upper, alpha)
            for real_u in (.31, 1.11):
                for imag_u in (0., .05, .15, .3, .6, -.05, -.15, -.3, -.6):
                    u = real_u+1j*imag_u
                    # Independently invert the finite Fourier Vandermonde.
                    interpolation = inverse@np.exp(1j*ell*u)
                    sine_interpolation = np.array([
                        np.prod(np.sin((u-np.delete(alpha, j))/2)/
                                np.sin((alpha[j]-np.delete(alpha, j))/2))
                        for j in range(n)])
                    interpolation_error = float(np.max(abs(
                        interpolation-sine_interpolation)))
                    assert interpolation_error < tolerance
                    direct = interpolation@qalpha
                    pu = sine_product(u, alpha)
                    bottom = qlower*pu/(2*np.sin((u-lower)/2)*plower)
                    top = qupper*pu/(2*np.sin((u-upper)/2)*pupper)
                    # CCW rectangle: bottom left-to-right, top right-to-left;
                    # (1/(2*pi*i)) times dx=2*pi/nodes.
                    rectangle = (np.sum(bottom)-np.sum(top))/(1j*nodes)
                    crossing = heat_fourier(u, modes, coefficient) if abs(imag_u)<height else 0.
                    residue_error = float(abs(direct-rectangle-crossing))
                    assert residue_error < tolerance
                    max_interpolation = max(max_interpolation, interpolation_error)
                    max_residue = max(max_residue, residue_error)
                    result.append({"N": n, "spectrum": "warped" if warped else "clock",
                        "real_u": real_u, "imag_u": imag_u,
                        "crossing_present": abs(imag_u)<height,
                        "interpolation_error": interpolation_error,
                        "rectangle_plus_residue_error": residue_error})
            for theta in (.31, 1.11):
                expected = inverse@np.exp(tau*ell**2+1j*ell*theta)
                for real_shift in (0., .17):
                    y = np.sqrt(2*time/n)*hermite_x
                    u = theta+real_shift+1j*y
                    values = inverse@np.exp(1j*ell[:, None]*u)
                    weights = hermite_weights*np.exp(
                        n*real_shift**2/(2*time)+1j*n*real_shift*y/time)/np.sqrt(np.pi)
                    integrated = values@weights
                    error = float(np.max(abs(expected-integrated)))
                    assert error < tolerance
                    max_backward = max(max_backward, error)
                    backward_result.append({"N": n, "warped": warped, "theta": theta,
                        "vertical_real_shift": real_shift, "error": error})
        length = n//2
        assert (length+1)**2-length**2 == n
        assert Fraction(1, 2*n)*n == Fraction(1, 2)
    return {"time": time, "source_heat_coefficient": "t/(2*N)",
        "horizontal_height": height, "rectangle_nodes": nodes,
        "hermite_nodes": len(hermite_x), "tolerance": tolerance,
        "residue_cases": result, "backward_heat_cases": backward_result,
        "max_interpolation_error": max_interpolation,
        "max_rectangle_plus_residue_error": max_residue,
        "max_backward_heat_error": max_backward,
        "max_wrapped_heat_vs_fourier_error": max_heat,
        "measure": "dtheta/(2*pi)",
        "crossing_sign": "rectangle=nodal sum-crossing heat",
        "balanced_comparison_exponents": balanced,
        "windings": "Fourier series independently calibrated against k=-8,...,8 Gaussians",
        "arithmetic": "complex128 diagnostics and exact Fraction Casimir"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = {"claim_id": "BGS-FLOW-014", "status": "PASS",
        "versions": {"Python": platform.python_version(), "NumPy": np.__version__,
                     "SciPy": scipy.__version__},
        "finite_controls": finite_controls(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Executed finite identity calibration, not a limiting proof",
        "exclusions": ["No asymptotic or all-N certificate from quadrature",
            "No two-dimensional saddle quadrature or Fredholm numerical certificate",
            "No Brownian endpoint simulation", "No deterministic BGS or priority claim"]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2)+"\n")
    print("PASS circular Dyson sine interpolation, shifted heat and crossing residue controls")


if __name__ == "__main__":
    main()
