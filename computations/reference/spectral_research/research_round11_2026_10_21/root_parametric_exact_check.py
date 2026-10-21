#!/usr/bin/env python3
"""Exact rational checks for Round 11; no asymptotic simulation is performed."""
from dataclasses import dataclass
from fractions import Fraction as F
import json
from pathlib import Path


@dataclass(frozen=True)
class C:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))

    @staticmethod
    def coerce(x):
        return x if isinstance(x, C) else C(x)

    def __add__(self, other):
        b = C.coerce(other)
        return C(self.re + b.re, self.im + b.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, other):
        return self + -C.coerce(other)

    def __rsub__(self, other):
        return C.coerce(other) + -self

    def __mul__(self, other):
        b = C.coerce(other)
        return C(self.re*b.re - self.im*b.im,
                 self.re*b.im + self.im*b.re)

    __rmul__ = __mul__

    def conj(self):
        return C(self.re, -self.im)

    def abs2(self):
        return self.re*self.re + self.im*self.im

    def __truediv__(self, other):
        b = C.coerce(other)
        n = b.abs2()
        if not n:
            raise ZeroDivisionError
        c = self*b.conj()
        return C(c.re/n, c.im/n)

    def text(self):
        return {"real": str(self.re), "imag": str(self.im)}


ZERO, ONE, I = C(), C(1), C(0, 1)


def clean(p):
    return {v: z for v, z in p.items() if z != ZERO}


def add(p, q):
    out = dict(p)
    for v, z in q.items():
        out[v] = out.get(v, ZERO) + z
    return clean(out)


def scale(p, x):
    return clean({v: z*x for v, z in p.items()})


def mul(p, q):
    out = {}
    for (k, l), a in p.items():
        for (m, n), b in q.items():
            v = (k+m, l+n)
            out[v] = out.get(v, ZERO) + a*b
    return clean(out)


def fourier():
    one = {(0, 0): ONE}
    c7 = {(7, 0): C(F(1, 2)), (-7, 0): C(F(1, 2))}
    c1 = {(1, 0): C(F(1, 2)), (-1, 0): C(F(1, 2))}
    s1 = {(1, 0): -I/2, (-1, 0): I/2}
    r = mul(add(one, scale(c7, -1)), add(one, c1))
    omega = C(F(-3, 5), F(4, 5))
    cp = {(0, 1): omega.conj()/2, (0, -1): omega/2}
    p = add(c7, scale(r, F(1, 10)))
    p = add(p, scale(mul(r, s1), F(1, 100)))
    p = add(p, scale(mul(r, cp), F(1, 100)))
    return add(p, {(0, 0): C(F(-1, 10))})


def mm(a, b):
    n = len(a)
    return [[sum((a[j][r]*b[r][k] for r in range(n)), ZERO)
             for k in range(n)] for j in range(n)]


def msub(a, b):
    return [[x-y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def phase_check():
    # These matrices check a finite identity, not the family in the problem.
    lam = [ONE, C(F(3, 5), F(4, 5)), C(F(-5, 13), F(12, 13))]
    a = [[C(1), C(2, 1), C(0)],
         [C(2, -1), C(-1), C(3)],
         [C(0), C(3), C(0)]]
    n = len(a)
    h = [[ZERO if l == j else I*lam[j]*a[l][j]/(lam[j]-lam[l])
          for j in range(n)] for l in range(n)]
    for j in range(n):
        for k in range(n):
            assert h[j][k] == -h[k][j].conj()
    ap = msub(mm(a, h), mm(h, a))
    values = []
    for j in range(n):
        target = sum((a[j][k].abs2()*I*(lam[j]+lam[k])/(lam[j]-lam[k])
                      for k in range(n) if k != j), ZERO)
        assert ap[j][j] == target
        assert target.im == 0
        values.append(target.text())
    return values


def main():
    coeff = fourier()
    assert len(coeff) == 32
    assert coeff.get((0, 0), ZERO) == ZERO
    for (k, l), z in coeff.items():
        assert coeff[(-k, -l)] == z.conj()
    q0 = sum((z.abs2() for z in coeff.values()), F(0))
    overlap = sum((z*coeff.get((-3*k-2*l, -4*k-3*l), ZERO)
                   for (k, l), z in coeff.items()), ZERO)
    assert q0 == F(66033, 160000)
    assert overlap == C(F(-7, 2000000))
    charge = 2*(q0-overlap.re)
    assert charge == F(1650839, 2000000)
    diagonal_energy = sum((z.abs2() for (k, l), z in coeff.items()
                           if l == 0), F(0))
    assert diagonal_energy == F(66015, 160000)
    # 39 is a sufficient odd-dimension gate: |v+S w|_infty <=37.
    radius = max(max(abs(k+3*m+2*n), abs(l+4*m+3*n))
                 for k, l in coeff for m, n in coeff)
    assert radius == 37
    result = {
        "status": "exact_finite_algebra_only",
        "sympy_used": False,
        "support_size": len(coeff),
        "trace_A2_div_N_for_odd_N_ge_39": str(q0),
        "trace_A_Mstar_A_M_div_N_for_odd_N_ge_39": str(overlap.re),
        "trace_D2_div_N_for_odd_N_ge_39": str(charge),
        "l_zero_energy": str(diagonal_energy),
        "alias_exclusion_radius": radius,
        "phase_equation_exact_3_by_3_check": phase_check(),
        "coefficients": [
            {"k": k, "l": l, **coeff[(k, l)].text()}
            for k, l in sorted(coeff)
        ],
    }
    path = Path(__file__).with_name("root_parametric_exact_results.json")
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k != "coefficients"},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
