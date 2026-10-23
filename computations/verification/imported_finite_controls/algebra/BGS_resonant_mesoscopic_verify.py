"""Portable exact-Fourier and finite spectral tests for the BGS resonant variance note.
Requires Python standard library only. The packet matrices are ABSTRACT test unitaries,
not the prescribed quantum map. No claim of proof by numerics is made.
"""
from fractions import Fraction as F
from math import ceil, floor, sqrt, pi, isqrt
from cmath import exp
Z = (F(0), F(0))

def plus(a, b):
    return (a[0] + b[0], a[1] + b[1])

def prod(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

def sc(a, q):
    return (a[0] * q, a[1] * q)

def add(A, B):
    C = dict(A)
    for k, v in B.items():
        C[k] = plus(C.get(k, Z), v)
    return C

def mul(A, B):
    C = {}
    for k, a in A.items():
        for j, b in B.items():
            C[k + j] = plus(C.get(k + j, Z), prod(a, b))
    return C

def scale(A, q):
    return {k: sc(a, q) for k, a in A.items()}

def cos_mode(k):
    return {k: (F(1, 2), F(0)), -k: (F(1, 2), F(0))}

def sin_mode(k):
    return {k: (F(0), F(-1, 2)), -k: (F(0), F(1, 2))}

def n2(A):
    return sum((x * x + y * y for x, y in A.values()))
one = {0: (F(1), F(0))}
r = mul(add(one, scale(cos_mode(7), F(-1))), add(one, cos_mode(1)))
g0 = add(cos_mode(7), add(scale(r, F(1, 10)), add(scale(mul(r, sin_mode(1)), F(1, 100)), scale(one, F(-1, 10)))))
r_shift = {k: sc(v, F(-1) if k % 2 else F(1)) for k, v in r.items()}
sigma2 = n2(g0) + F(1, 2) * n2(scale(r_shift, F(1, 100)))
if not sigma2 == F(66033, 160000):
    raise AssertionError('verification failed')
print('Physical kick exact normalized HS norm squared =', sigma2, float(sigma2))
print('Rigorous E_p([1,2]) lower bound up to p=10**39:', (1 - 2 * float(sigma2) * 0.0001) ** 2)

def count_variance(phases, length):
    p = len(phases)
    count = sum((0 < z <= length for z in phases))
    events = []
    for z in phases:
        enter = (z - length) % 1
        leave = z % 1
        if enter > 0:
            events.append((enter, +1))
        if leave > 0:
            events.append((leave, -1))
    events.sort()
    mean = 0.0
    var = 0.0
    last = 0.0
    for at, change in events:
        span = at - last
        mean += span * count
        var += span * (count - p * length) ** 2
        count += change
        last = at
    span = 1 - last
    mean += span * count
    var += span * (count - p * length) ** 2
    if not abs(mean - p * length) < 1e-08:
        raise AssertionError('verification failed')
    return var
for p, d in ((199, 9), (4663, 21), (13729, 48)):
    R = p // d
    n = isqrt(p * d)
    P = p - n
    phases = [j / P for j in range(P)] + [k / ((n + 1) * p * p) for k in range(1, n + 1)]
    lo = ceil(p / (2 * d))
    hi = floor(p / d)
    if not hi < P:
        raise AssertionError('verification failed')
    energy = 0.0
    maximum = 0.0
    for power in range(lo, hi + 1):
        tr = sum((exp(2j * pi * power * phi) for phi in phases[-n:]))
        energy += abs(tr) ** 2 / p ** 2
        maximum = max(maximum, abs(tr) / p)
    ell = d / (8 * p)
    v = count_variance(phases, ell)
    cue = sum((min(power * d, p) / p ** 2 for power in range(lo, hi + 1)))
    upper = 2 * pi * pi * 2 ** 2 * v / d ** 2
    if not energy <= upper + 1e-08:
        raise AssertionError('verification failed')
    print(f'p={p:5d} d={d:3d} packet={n:4d} E={energy:.8f} max_trace_over_p={maximum:.8f} V_over_d2={v / d ** 2:.8f} CUE_E_expected={cue:.8f}')
