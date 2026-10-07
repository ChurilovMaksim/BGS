#!/usr/bin/env python3
"""Independent exact finite checks for the literal kick-phase proof.

This verifies algebra, signs and finite exceptions. It does not verify an
asymptotic theorem numerically, evaluate tiny-tau exponentials, or inspect
p-adic surrogates. All generated files remain in this review directory.
"""
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
x, y = sp.symbols("x y", nonzero=True)
I = sp.I
R = sp.Rational


def coefficients(expr):
    result = {}
    for term in sp.Add.make_args(sp.expand(expr)):
        powers = term.as_powers_dict()
        k, ell = int(powers.get(x, 0)), int(powers.get(y, 0))
        result[k, ell] = sp.simplify(result.get((k, ell), 0)
                                         + term / x**k / y**ell)
    return {v: c for v, c in result.items() if c != 0}


manifest = json.loads((ROOT / "manifest.json").read_text())
hashes = {}
for name, expected in manifest["files"].items():
    actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    assert actual == expected, (name, expected, actual)
    hashes[name] = actual

c7 = (x**7 + x**-7) / 2
r = (1 - c7) * (1 + (x + x**-1) / 2)
sin_q = (x - x**-1) / (2 * I)
cos_pa = ((-3 - 4*I) * y + (-3 + 4*I) / y) / 10
raw = c7 + r/10 + r*sin_q/100 + r*cos_pa/100 - R(1, 10)
ordinary = c7 + r/10 + r*sin_q/100 + r.subs(x, -x)*cos_pa/100 - R(1, 10)
raw_c, ordinary_c = coefficients(raw), coefficients(ordinary)
assert ordinary_c == {v: c * (-1 if v[0]*v[1] % 2 else 1)
                      for v, c in raw_c.items()}
assert all(sp.simplify(ordinary_c.get((-k, -ell), 0) - sp.conjugate(c)) == 0
           for (k, ell), c in ordinary_c.items())


def euler(expr, z):
    return sp.expand(z * sp.diff(expr, z))


gradient_over_2pi_i = [euler(ordinary, z) for z in (x, y)]
hessian_over_pi2 = sp.Matrix([
    [-4*euler(euler(ordinary, z1), z2) for z2 in (x, y)]
    for z1 in (x, y)
])
hessians = []
expected_bs = [-R(19606, 125), -R(19594, 125),
               R(24306, 125), R(24894, 125)]
for (x0, y0), expected in zip(itertools.product((1, -1), repeat=2), expected_bs):
    subst = {x: x0, y: y0}
    assert all(sp.simplify(t.subs(subst)) == 0 for t in gradient_over_2pi_i)
    H = hessian_over_pi2.subs(subst).applyfunc(sp.simplify)
    assert H == sp.diag(expected, 0)
    hessians.append(str(H))

b, s = sp.symbols("b s", real=True, nonzero=True)
B = sp.Matrix([[0, 0], [-b, 0]])
assert B != sp.zeros(2) and B**2 == sp.zeros(2)
assert sp.exp(s * B) == sp.eye(2) + s*B

# Integer modular exponent checks, including labels beyond a centered cell.
# In units pi*i/N, W(a,b) has phase b*(2*j+a), shift j -> j+a.
phase_checks = 0
for N in (1, 3, 5, 7, 9, 21, 35):
    inv2 = (N + 1)//2
    labels = [(-N-1, 3), (N+2, -2), (0, 0), (1, 0), (0, 1),
              (-3, -2), (-1, 2), (2, -1), (3, 3)]
    for a, bb in labels:
        for j in range(N):
            raw_phase = N*a*bb + 2*bb*(j + inv2*a)
            midpoint_phase = bb*(2*j+a)
            assert (raw_phase - midpoint_phase) % (2*N) == 0
    for (a, bb), (c, d) in itertools.product(labels, repeat=2):
        omega = a*d - bb*c
        for j in range(N):
            lhs = bb*(2*j+a) + d*(2*((j+a) % N)+c)
            rhs = omega + (bb+d)*(2*j+a+c)
            assert (lhs-rhs) % (2*N) == 0
            phase_checks += 1

# An exact exceptional-N=7 matrix over Q(i)[zeta_7].
z = sp.symbols("z")
N = 7
inv2 = pow(2, -1, N)
phi7 = sp.Poly(sp.cyclotomic_poly(N, z), z, domain=sp.QQ_I)
rows = [[sp.Integer(0) for _ in range(N)] for _ in range(N)]
for (k, ell), coef in raw_c.items():
    for j in range(N):
        rows[j][(j+ell) % N] += coef * z**((k*(j+inv2*ell)) % N)
for j in range(N):
    for k in range(N):
        reduced = sp.Poly(sp.expand(rows[j][k]), z, domain=sp.QQ_I).rem(phi7).as_expr()
        assert reduced == (R(9, 10) if j == k else 0)
for N in (3, 5, 7, 9, 21, 35, 49, 77):
    inv2 = pow(2, -1, N)
    cuts = [j for j in range(N) if (7*(j+inv2)) % N == 0]
    assert len(cuts) == math.gcd(N, 7)

# The commutator sign: i*N*(2*i*sin(pi*omega/N)) -> -2*pi*omega.
# X_g(e_nu)/(2*pi) has exactly this same coefficient.
omega, h = sp.symbols("omega h", real=True)
assert sp.limit(-2*sp.sin(sp.pi*omega*h)/h, h, 0) == -2*sp.pi*omega

u, rho = sp.symbols("u rho", real=True)
trimmed = sp.integrate(4*sp.sin(sp.pi*u/2)**2, (u, 0, 1-rho))
assert sp.simplify(trimmed - (2*(1-rho)-2*sp.sin(sp.pi*rho)/sp.pi)) == 0
assert sp.simplify(2*sp.sin(sp.pi*(1-rho)/2)-2*sp.cos(sp.pi*rho/2)) == 0

report = {
    "result": "PASS: exact finite algebra only; no numerical asymptotic inference",
    "candidate_sha256": hashlib.sha256((ROOT / "literal_kick_phase_law.md").read_bytes()).hexdigest(),
    "input_sha256": hashes,
    "fourier_terms": len(ordinary_c),
    "hessians_over_pi_squared": hessians,
    "integer_weyl_phase_checks": phase_checks,
    "exceptional_dimension_7": "A_7 = (9/10) I exactly",
    "uniform_rank_hs_formula": str(sp.simplify(trimmed)),
    "caveat": "Finite algebra checks support the separate analytic proof audit; they do not prove K1-K5 by extrapolation."
}
print(json.dumps(report, indent=2))
