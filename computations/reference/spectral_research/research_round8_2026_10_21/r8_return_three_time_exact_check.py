"""Bounded exact audit from the original Laurent polynomial, no external libraries."""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product


@dataclass(frozen=True)
class G:
    r: F = F(0)
    i: F = F(0)

    def __add__(self, other):
        other = other if isinstance(other, G) else G(F(other))
        return G(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __mul__(self, other):
        other = other if isinstance(other, G) else G(F(other))
        return G(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def __bool__(self):
        return bool(self.r or self.i)

    def __str__(self):
        return f"({self.r})+({self.i})i"


def padd(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}


def scale(p, c):
    return {k: c * v for k, v in p.items() if c * v}


def pmul(a, b):
    out = {}
    for (k, l), u in a.items():
        for (j, m), v in b.items():
            key = (k + j, l + m)
            out[key] = out.get(key, 0) + u * v
    return {k: v for k, v in out.items() if v}


one = {(0, 0): G(F(1))}
C7 = {(-7, 0): G(F(1, 2)), (7, 0): G(F(1, 2))}
C1 = {(-1, 0): G(F(1, 2)), (1, 0): G(F(1, 2))}
S1 = {(-1, 0): G(F(0), F(1, 2)), (1, 0): G(F(0), F(-1, 2))}
r = pmul(padd(one, scale(C7, -1)), padd(one, C1))
Cphase = {(0, 1): G(F(-3, 10), F(-4, 10)),
          (0, -1): G(F(-3, 10), F(4, 10))}
coeff = padd(C7, scale(r, F(1, 10)),
             scale(pmul(r, S1), F(1, 100)),
             scale(pmul(r, Cphase), F(1, 100)), scale(one, F(-1, 10)))


def sm(v):
    return 3 * v[0] + 2 * v[1], 4 * v[0] + 3 * v[1]


def omega(a, b):
    return a[1] * b[0] - a[0] * b[1]


closed = []
areas = {}
for x, y, z in product(coeff, repeat=3):
    a, b, c = x, sm(y), sm(sm(z))
    if all(a[j] + b[j] + c[j] == 0 for j in range(2)):
        area = omega(a, b) + omega(a, c) + omega(b, c)
        value = coeff[x] * coeff[y] * coeff[z]
        closed.append((x, y, z, area, str(value)))
        areas[area] = areas.get(area, 0) + value

assert len(coeff) == 32
assert len(closed) == 4
assert areas == {24: G(F(-97, 800000)), 2: G()}
print("support", len(coeff), "integer triples checked", len(coeff) ** 3)
for row in closed:
    print(row)
print("area sums", {a: str(v) for a, v in areas.items()})

# Independently compare all coefficients of the formal quadratic CH identity.
def ls(a, c):
    return tuple(c * v for v in a)


def la(*a):
    return tuple(sum(v) for v in zip(*a))


def vs(v, c):
    return ls(v[0], c), ls(v[1], c)


def va(*a):
    return la(*(v[0] for v in a)), la(*(v[1] for v in a))


def S(v):
    return la(ls(v[0], 3), ls(v[1], 2)), la(ls(v[0], 4), ls(v[1], 3))


def Sinv(v):
    return la(ls(v[0], 3), ls(v[1], -2)), la(ls(v[0], -4), ls(v[1], 3))


def lp(a, b):
    out = {}
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            k = tuple(sorted((i, j)))
            out[k] = out.get(k, 0) + u * v
    return {k: v for k, v in out.items() if v}


def om(a, b):
    return padd(lp(a[1], b[0]), scale(lp(a[0], b[1]), -1))


def area(a, b, c):
    return padd(om(a, b), om(a, c), om(b, c))


units = [tuple(int(i == j) for i in range(8)) for j in range(8)]
e0, e1, e2, h = [tuple(units[j:j + 2]) for j in (0, 2, 4, 6)]
x, y, z = e0, S(e1), S(S(e2))
a, b, c = h, vs(S(h), -6), S(S(h))
actual = padd(area(va(x, a), va(y, b), va(z, c)), scale(area(x, y, z), -1))
claimed = padd(om(h, va(e0, S(e1), vs(Sinv(e1), -1), vs(e2, -1))),
               scale(om(h, S(h)), -6))
assert actual == claimed
print("formal quadratic CH coefficient difference: zero")
print("all exact assertions passed")
