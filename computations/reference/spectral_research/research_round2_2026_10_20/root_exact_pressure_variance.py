"""Exact rational certificate; all-time support classification is in the note."""
from fractions import Fraction as F

ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def addz(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mulz(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def conj(a):
    return (a[0], -a[1])


def scale(poly, x):
    return {n: (x * z[0], x * z[1]) for n, z in poly.items()
            if x * z[0] or x * z[1]}


def plus(*polys):
    result = {}
    for p in polys:
        for n, z in p.items():
            result[n] = addz(result.get(n, ZERO), z)
    return {n: z for n, z in result.items() if z != ZERO}


def times(a, b):
    result = {}
    for n, z in a.items():
        for m, w in b.items():
            index = (n[0] + m[0], n[1] + m[1])
            result[index] = addz(result.get(index, ZERO), mulz(z, w))
    return {n: z for n, z in result.items() if z != ZERO}


def cosq(k):
    return {(k, 0): (F(1, 2), F(0)), (-k, 0): (F(1, 2), F(0))}


constant = {(0, 0): ONE}
sin1 = {(1, 0): (F(0), -F(1, 2)), (-1, 0): (F(0), F(1, 2))}
r = times(plus(constant, scale(cosq(7), F(-1))), plus(constant, cosq(1)))
r_shift = {n: ((-1 if n[0] % 2 else 1) * z[0],
               (-1 if n[0] % 2 else 1) * z[1]) for n, z in r.items()}
cos_phase = {(0, 1): (-F(3, 10), -F(2, 5)),
             (0, -1): (-F(3, 10), F(2, 5))}
a = plus(cosq(7), scale(r, F(1, 10)), scale(times(r, sin1), F(1, 100)),
         scale(constant, -F(1, 10)), scale(times(r_shift, cos_phase), F(1, 100)))
assert len(a) == 32 and a.get((0, 0), ZERO) == ZERO
assert all(a[(-k, -l)] == conj(z) for (k, l), z in a.items())

l0 = {1: (F(1, 20), -F(1, 200)), 2: (F(0), -F(1, 400)),
      5: (F(0), -F(1, 800)), 6: (-F(1, 40), -F(1, 400)),
      7: (F(9, 20), F(0)), 8: (-F(1, 40), F(1, 400)),
      9: (F(0), F(1, 800))}
l1 = {0: (-F(3, 1000), -F(1, 250)),
      1: (F(3, 2000), F(1, 500)), 6: (F(3, 4000), F(1, 1000)),
      7: (-F(3, 2000), -F(1, 500)), 8: (F(3, 4000), F(1, 1000))}
expected = {(k, 0): z for k, z in l0.items()}
expected.update({(-k, 0): conj(z) for k, z in l0.items()})
for k, z in l1.items():
    for signed_k in {k, -k}:
        expected[(signed_k, 1)] = z
        expected[(signed_k, -1)] = conj(z)
assert a == expected


def q(n):
    k, l = n
    return 2 * k * k - l * l


def st(n):
    k, l = n
    return (3 * k + 2 * l, 4 * k + 3 * l)


rxi = {n: (q(n) * z[0], q(n) * z[1]) for n, z in a.items()}
assert all(q(st(n)) == q(n) for n in a)
c0 = sum((mulz(z, conj(z))[0] for z in rxi.values()), F(0)) / 2
c1z = ZERO
intersections = []
for n, z in rxi.items():
    if st(n) in rxi:
        intersections.append((n, st(n)))
        c1z = addz(c1z, mulz(z, conj(rxi[st(n)])))
assert set(intersections) == {((1, -1), (1, 1)), ((-1, 1), (-1, -1))}
assert c1z[1] == 0
c1 = c1z[0] / 2
sigma = c0 + 2 * c1
assert c0 == F(313386243, 160000)
assert c1 == -F(7, 4000000)
assert sigma == F(7834656061, 4000000)
assert sigma / 8 == F(7834656061, 32000000)
print('Exact rational certificate: PASS')
print('C_0 / pi^2 =', c0)
print('C_1 / pi^2 =', c1)
print('sigma^2 / pi^2 =', sigma)
print('(sigma^2 / 8) / pi^2 =', sigma / 8)
