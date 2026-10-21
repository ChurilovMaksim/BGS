#!/usr/bin/env python3
"""Exact Fourier check for the original kick; no floating point arithmetic.

This checks only the stated finite algebra, not a spectral asymptotic.
All complex coefficients are pairs of fractions (real, imaginary).
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ZERO = (F(0), F(0))

def add(z, w):
    return (z[0] + w[0], z[1] + w[1])

def scale(c, z):
    return (F(c) * z[0], F(c) * z[1])

def conj(z):
    return (z[0], -z[1])

def total(values):
    answer = ZERO
    for value in values:
        answer = add(answer, value)
    return answer

def encode(z):
    return [str(z[0]), str(z[1])]

r = {0: F(1), -1: F(1, 2), 1: F(1, 2),
     -7: F(-1, 2), 7: F(-1, 2),
     -6: F(-1, 4), 6: F(-1, 4),
     -8: F(-1, 4), 8: F(-1, 4)}
c = {}
for k in range(-9, 10):
    rk = r.get(k, F(0))
    z = (F(int(abs(k) == 7), 2) + rk / 10 - F(int(k == 0), 10),
         -(r.get(k - 1, F(0)) - r.get(k + 1, F(0))) / 200)
    if z != ZERO:
        c[(k, 0)] = z
    for ell, imaginary in ((1, -4), (-1, 4)):
        z = (F(-3, 1000) * rk, F(imaginary, 1000) * rk)
        if z != ZERO:
            c[(k, ell)] = z

assert len(c) == 32
assert c.get((0, 0), ZERO) == ZERO
assert all(c[(-k, -ell)] == conj(z) for (k, ell), z in c.items())
d = {(k, ell): scale(-1 if k * ell % 2 else 1, z)
     for (k, ell), z in c.items()}
assert all(d[(-k, -ell)] == conj(z) for (k, ell), z in d.items())

moments = {}
for degree in range(3):
    for ell in (-1, 0, 1):
        moments[(degree, ell)] = total(
            scale(k ** degree, z) for (k, l), z in d.items() if l == ell)

expected = {
    (0, -1): ZERO, (0, 0): (F(9, 10), F(0)), (0, 1): ZERO,
    (1, -1): ZERO, (1, 0): ZERO, (1, 1): ZERO,
    (2, -1): (F(3, 500), F(-4, 500)),
    (2, 0): (F(196, 5), F(0)),
    (2, 1): (F(3, 500), F(4, 500)),
}
assert moments == expected
aqq_over_pi_squared = {
    ell: scale(-4, moments[(2, ell)]) for ell in (-1, 0, 1)}
assert aqq_over_pi_squared == {
    -1: (F(-3, 125), F(4, 125)),
    0: (F(-784, 5), F(0)),
    1: (F(-3, 125), F(-4, 125)),
}

output = {
    "arithmetic": "exact fractions only; complex numbers encoded as [real, imaginary]",
    "original_nonzero_fourier_coefficients": len(c),
    "original_coefficients": {f"{k},{ell}": encode(z) for (k, ell), z in sorted(c.items())},
    "ordinary_coefficients": {f"{k},{ell}": encode(z) for (k, ell), z in sorted(d.items())},
    "q_zero_fourier_moments": {f"degree={degree},ell={ell}": encode(z)
                               for (degree, ell), z in sorted(moments.items())},
    "aqq_over_pi_squared_at_q_zero": {str(ell): encode(z)
                                      for ell, z in sorted(aqq_over_pi_squared.items())},
    "conclusion": "a(0,p)=9/10, da(0,p)=0, a_pp=a_qp=0; "
                  "a_qq(0,p)=-(2*pi^2/25)*(1960-cos(2*pi*p-alpha_0)) < 0.",
    "asymptotic_verification": False,
}
destination = Path(__file__).with_name("r12_countersequence_exact_check.json")
destination.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({
    "assertions_passed": True,
    "coefficient_count": len(c),
    "output": str(destination),
    "output_sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}, ensure_ascii=False))
