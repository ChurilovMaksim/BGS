"""Exact rational check of the explicit four-sheet return coefficient.

This checks a finite coefficient identity used in the analytic proof; it
does not simulate U_N and is not evidence for spectral universality.
"""

from fractions import Fraction as F
import json


def multiply(a, b):
    out = {}
    for j, aj in a.items():
        for k, bk in b.items():
            out[j + k] = out.get(j + k, F(0)) + aj * bk
    return {j: aj for j, aj in out.items() if aj}


r = {0: F(1), -1: -F(1, 2), 1: -F(1, 2),
     -7: F(1, 2), 7: F(1, 2),
     -8: -F(1, 4), -6: -F(1, 4), 6: -F(1, 4), 8: -F(1, 4)}
r2 = multiply(r, r)
r4 = multiply(r2, r2)
coefficient = r4[2]
assert coefficient == F(245, 32)

# (-3-4i)^4 = -527-336i, with denominator 1000^4.
real_g4_over_kappa6 = -F(527, 1000**4) * coefficient / 96
imag_g4_over_kappa6 = -F(336, 1000**4) * coefficient / 96
assert real_g4_over_kappa6 == -F(25823, 614400000000000)
assert imag_g4_over_kappa6 == -F(343, 12800000000000)

# The diagonal return integral contributes 8*kappa^2*Re(g4),
# and t^4=(tau/kappa)^4 with kappa=2*pi.
return_coefficient_over_pi4_tau4 = 8 * 16 * real_g4_over_kappa6
assert return_coefficient_over_pi4_tau4 == -F(25823, 4800000000000)

print(json.dumps({
    "R_fourier": {str(k): str(v) for k, v in sorted(r.items())},
    "R2_fourier": {str(k): str(v) for k, v in sorted(r2.items())},
    "coefficient_R4_z2": str(coefficient),
    "g4_z2_over_kappa6_real": str(real_g4_over_kappa6),
    "g4_z2_over_kappa6_imag": str(imag_g4_over_kappa6),
    "return_coefficient_over_pi4_tau4": str(return_coefficient_over_pi4_tau4),
    "arithmetic": "exact fractions; no floating-point arithmetic",
}, indent=2))
