#!/usr/bin/env python3
"""Exact finite controls for the Haar-feedback/Cayley factorization."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")

import argparse
import json
from pathlib import Path
import sympy as sp


def reduced(matrix):
    return matrix.applyfunc(sp.cancel)


def same(left, right):
    assert reduced(left - right) == sp.zeros(*left.shape)


def hermitian_fixture(dimension, offset):
    result = sp.zeros(dimension)
    for j in range(dimension):
        result[j, j] = sp.Rational((-1)**j * (j + 1), offset + j + 3)
        for k in range(j + 1, dimension):
            result[j, k] = sp.Rational(j + 1, offset + k + 5) + sp.I * sp.Rational(k + 1, offset + j + 7)
            result[k, j] = sp.conjugate(result[j, k])
    return result


def exact_colligation_controls():
    results = []
    for u, q in [(1, 1), (2, 1), (1, 2), (2, 2), (3, 1)]:
        a = hermitian_fixture(u, 2)
        x = sp.Matrix(q, u, lambda j, k: sp.Rational(j + 1, k + 5) + sp.I * sp.Rational(k + 1, j + 7))
        z = hermitian_fixture(q, 8)
        b = reduced(x * (a + sp.I * sp.eye(u)))
        d = reduced(x * a * x.H + z)
        c = a.row_join(b.H).col_join(b.row_join(d))
        n = u + q
        v = reduced((c - sp.I * sp.eye(n)) * (c + sp.I * sp.eye(n)).inv())
        same(v.H * v, sp.eye(n))
        rr, re, er, ee = v[:u, :u], v[:u, u:], v[u:, :u], v[u:, u:]
        resolvent = reduced((sp.eye(q) - ee).inv())
        x_direct = reduced(resolvent * er)
        s_direct = reduced(rr + re * x_direct)
        same(x_direct, x)
        same(s_direct, reduced((a - sp.I * sp.eye(u)) * (a + sp.I * sp.eye(u)).inv()))
        same(s_direct.H * s_direct, sp.eye(u))
        # Different representation: differentiate the full rational resolvent,
        # rather than computing the clock from its predicted graph identity.
        derivative = reduced(rr + 2 * re * resolvent * er + re * resolvent * ee * resolvent * er)
        clock_from_derivative = reduced(s_direct.H * derivative)
        same(clock_from_derivative, reduced(sp.eye(u) + x.H * x))
        g = reduced(sp.eye(q) + x * x.H)
        schur_left = sp.cancel((sp.eye(n) + sp.I * c).det())
        schur_right = sp.cancel((sp.eye(u) + sp.I * a).det() * (g + sp.I * z).det())
        assert sp.cancel(schur_left - schur_right) == 0
        # Absorb a nontrivial eliminated-port phase vector and compare two
        # expressions from the original colligation, including its derivative.
        phases = sp.diag(*[(sp.Rational(3, 5) + 4 * sp.I / 5)**(j + 1) for j in range(q)])
        original = sp.diag(sp.eye(u), phases.H) * v
        orr, ore, oer, oee = original[:u, :u], original[:u, u:], original[u:, :u], original[u:, u:]
        phase_resolvent = reduced((sp.eye(q) - phases * oee).inv())
        phase_s = reduced(orr + ore * phase_resolvent * phases * oer)
        phase_derivative = reduced(orr + 2 * ore * phase_resolvent * phases * oer
                                   + ore * phase_resolvent * phases * oee * phase_resolvent * phases * oer)
        same(phase_s, s_direct)
        same(phase_derivative, derivative)
        results.append({"u": u, "q": q, "N": n, "exact_unitary_delay_schur_and_phase_checks": True})
    return results


def jacobian_controls():
    a, xr, xi, y = sp.symbols("a xr xi y", real=True)
    variables = sp.Matrix([a, xr, xi, y])
    # Real coordinates of B=X(A+i), D=A|X|^2+(1+|X|^2)Y.
    transformed = sp.Matrix([a, a * xr - xi, xr + a * xi,
                             a * (xr**2 + xi**2) + (1 + xr**2 + xi**2) * y])
    jacobian = sp.factor(transformed.jacobian(variables).det())
    assert jacobian == (1 + a**2) * (1 + xr**2 + xi**2)
    b = (xr + sp.I * xi) * (a + sp.I)
    d = transformed[3]
    c = sp.Matrix([[a, sp.conjugate(b)], [b, d]])
    density_factor = sp.factor((sp.eye(2) + c**2).det())
    assert sp.expand(density_factor - (1 + a**2) * (1 + xr**2 + xi**2)**2 * (1 + y**2)) == 0

    h1, h2, hr, hi = sp.symbols("h1 h2 hr hi", real=True)
    h = sp.Matrix([[h1, hr + sp.I * hi], [hr - sp.I * hi, h2]])
    r = sp.Matrix([[2, sp.I], [1 - sp.I, 3]])
    image = sp.expand(r * h * r.H)
    coords = sp.Matrix([sp.expand(sp.re(image[0, 0])), sp.expand(sp.re(image[1, 1])),
                        sp.expand(sp.re(image[0, 1])), sp.expand(sp.im(image[0, 1]))])
    hermitian_jacobian = sp.factor(coords.jacobian([h1, h2, hr, hi]).det())
    assert sp.cancel(hermitian_jacobian - (r.det() * sp.conjugate(r.det()))**2) == 0

    a2 = hermitian_fixture(2, 2)
    m = a2 + sp.I * sp.eye(2)
    row = sp.Matrix([[h1 + sp.I * h2, hr + sp.I * hi]])
    out = sp.expand(row * m)
    complex_coords = sp.Matrix([sp.re(out[0, 0]).expand(), sp.im(out[0, 0]).expand(),
                                sp.re(out[0, 1]).expand(), sp.im(out[0, 1]).expand()])
    rectangular_jacobian = sp.cancel(complex_coords.jacobian([h1, h2, hr, hi]).det())
    assert rectangular_jacobian == sp.cancel((sp.eye(2) + a2**2).det())
    return {"scalar_block_jacobian": str(jacobian), "scalar_density_factorization": True,
            "non_diagonal_complex_hermitian_congruence_jacobian": str(hermitian_jacobian),
            "non_diagonal_rectangular_right_product_jacobian": str(rectangular_jacobian)}


def independent_one_port_moments():
    r, w, s = sp.symbols("r w s", real=True)
    results = []
    for k in range(1, 5):
        # Direct phase averaging of the deleted Haar diagonal, independently
        # of the rectangular Cauchy density: residue at w=r, pole order k.
        pole_free = (1 - r**2)**k * w**(k - 1) / (1 - r * w)**k
        phase_mean = sp.factor(sp.diff(pole_free, w, k - 1).subs(w, r) / sp.factorial(k - 1))
        radial = sp.cancel(phase_mean).subs(r**2, s)
        assert not radial.has(r)
        for u in range(k, k + 3):
            integrand = sp.cancel(u * (1 - s)**(u - 1) * radial)
            observed = sp.integrate(integrand, (s, 0, 1))
            predicted = sp.factorial(u + k - 1) * sp.factorial(u - k) / (sp.factorial(u - 1) * sp.factorial(u))
            assert sp.cancel(observed - predicted) == 0
            results.append({"u": u, "q": 1, "power": k, "direct_Haar_diagonal_moment": str(observed)})
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = {"status": "PASS", "arithmetic": "SymPy exact Gaussian rationals and symbolic real polynomials",
              "colligations": exact_colligation_controls(), "jacobians": jacobian_controls(),
              "independent_one_port_moments": independent_one_port_moments(),
              "non_claims": ["No computation establishes a Haar distribution, probabilistic limit or entropy transfer theorem",
                            "No deterministic-map flatness, prescribed-origin microscopic universality, BGS or priority claim",
                            "No analytic Lean formalization"]}
    serialized = json.dumps(result, indent=2) + "\n"
    if arguments.output:
        with arguments.output.open("x", encoding="utf-8") as stream:
            stream.write(serialized)
    print(serialized, end="")


if __name__ == "__main__":
    main()
