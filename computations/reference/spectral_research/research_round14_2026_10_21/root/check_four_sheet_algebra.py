"""Exact finite algebra audit; no spectral simulation or asymptotic claim.

Command, inputs and exclusions are specified in four_sheet_contract.json.
All coefficients belong to Q[i]; no floating-point calculation is used.
The momentum frequency scale kappa is set to 1 only after recording the
homogeneity g_n ~ kappa**(2*n-2) in the accompanying proof.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


@dataclass(frozen=True)
class Qi:
    re: F = F(0)
    im: F = F(0)

    def __add__(self, other):
        return Qi(self.re + other.re, self.im + other.im)

    def __neg__(self):
        return Qi(-self.re, -self.im)

    def __mul__(self, other):
        return Qi(self.re * other.re - self.im * other.im,
                  self.re * other.im + self.im * other.re)

    def __bool__(self):
        return bool(self.re or self.im)

    def record(self):
        return {"real": str(self.re), "imaginary": str(self.im)}


ZERO = Qi()
II = Qi(im=F(1))


def add(*polynomials):
    out = {}
    for a in polynomials:
        for k, v in a.items():
            out[k] = out.get(k, ZERO) + v
    return {k: v for k, v in out.items() if v}


def scale(a, c):
    return {k: v * c for k, v in a.items() if v * c}


def multiply(a, b):
    out = {}
    for j, aj in a.items():
        for k, bk in b.items():
            out[j + k] = out.get(j + k, ZERO) + aj * bk
    return {k: v for k, v in out.items() if v}


def power(a, n):
    out = {0: Qi(F(1))}
    for _ in range(n):
        out = multiply(out, a)
    return out


def D(a, n):
    # d/dq - 3*i*n/4, with z=exp(i*q) and kappa=1.
    return {k: v * Qi(im=F(k) - F(3 * n, 4))
            for k, v in a.items() if k != F(3 * n, 4)}


rr = {0: F(1), 1: -F(1, 2), -1: -F(1, 2),
      7: F(1, 2), -7: F(1, 2),
      6: -F(1, 4), -6: -F(1, 4),
      8: -F(1, 4), -8: -F(1, 4)}
R = {k: Qi(v) for k, v in rr.items()}
u = scale(R, Qi(-F(3, 1000), -F(4, 1000)))
g1 = u
g2 = scale(multiply(u, D(g1, 1)), Qi(im=F(1, 2)))
g3 = scale(add(scale(multiply(u, D(g2, 2)), II),
               scale(multiply(u, power(D(g1, 1), 2)), Qi(-F(1, 2)))),
           Qi(F(1, 3)))
g4 = scale(add(scale(multiply(u, D(g3, 3)), II),
               scale(multiply(multiply(u, D(g1, 1)), D(g2, 2)), Qi(-F(1))),
               scale(multiply(u, power(D(g1, 1), 3)), Qi(im=-F(1, 6)))),
           Qi(F(1, 4)))
closed_g4 = scale(D(D(D(power(u, 4), 4), 4), 4), Qi(im=-F(1, 96)))
assert g4 == closed_g4

# Separate literal four-index sum: every tuple is visited without pruning.
coefficient_direct = F(0)
tuples_visited = 0
tuples_contributing = 0
for labels in product(tuple(rr), repeat=4):
    tuples_visited += 1
    if sum(labels) == 2:
        tuples_contributing += 1
        term = F(1)
        for label in labels:
            term *= rr[label]
        coefficient_direct += term
assert tuples_visited == 9**4
R2 = multiply(R, R)
R4 = multiply(R2, R2)
assert R4[2] == Qi(coefficient_direct)
assert coefficient_direct == F(245, 32)
expected_g4 = Qi(-F(25823, 614400000000000), -F(343, 12800000000000))
assert g4[2] == expected_g4
return_coefficient = F(128) * g4[2].re
assert return_coefficient == -F(25823, 4800000000000)

# Exact Gauss identity in Z[zeta_8], represented modulo z^4+1.
def zeta8(exponent, coefficient=1):
    exponent %= 8
    v = [0, 0, 0, 0]
    v[exponent % 4] = coefficient * (-1 if exponent >= 4 else 1)
    return v


gauss_cases = []
for N_residue, d_residue in product((1, 3, 5, 7), range(8)):
    terms = [zeta8(2 * d_residue * m - 3 * N_residue * m * m)
             for m in range(4)]
    lhs = [sum(t[j] for t in terms) for j in range(4)]
    rhs = zeta8(-3 * N_residue + 3 * N_residue * d_residue**2, 2)
    assert lhs == rhs
    gauss_cases.append({"N_mod_8": N_residue, "d_mod_8": d_residue})

result = {
    "assertion_tested": "Complete Laurent g4 recurrence equals its closed differential expression; exact Fourier coefficient and four-sheet Gauss residue identity",
    "domain": "Q[i] Laurent coefficients; Z[zeta_8] residues",
    "R2_coefficients": {str(k): v.record() for k, v in sorted(R2.items())},
    "g4_nonzero_coefficients": len(g4),
    "g4_recurrence_equals_closed_polynomial": True,
    "four_tuples_visited": tuples_visited,
    "four_tuples_contributing_to_mode_2": tuples_contributing,
    "R4_mode_2": str(coefficient_direct),
    "g4_mode_2_over_kappa6": g4[2].record(),
    "diagonal_return_coefficient_over_pi4_tau4": str(return_coefficient),
    "gauss_cases_checked": gauss_cases,
    "randomness": False,
    "non_claims": ["No finite-N spectral data were computed.",
                   "This computation does not prove H_diag, Sine_2 convergence, or their failure.",
                   "Analytic remainders and the discrete-to-limit passage require the written proof."]
}
output = Path("research_round14_2026_10_21/root/four_sheet_run/result.json")
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"result": str(output), "polynomial_identity": True,
                  "R4_mode_2": str(coefficient_direct),
                  "gauss_cases": len(gauss_cases)}))
