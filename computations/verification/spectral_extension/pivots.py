"""Independent finite verifier: decimal outward boxes, different pi identity,
Horner trig, LDL inertia, reversed eigenvector recurrence, Fourier chirp kernel.
Does not import author code. Source certificates provide candidate root intervals,
which are independently validated; their stored pivots are not trusted or reused.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import json, time, hashlib, platform, argparse
DIGITS = 260
S = 10 ** DIGITS

def down(x):
    return x.numerator * S // x.denominator

def up(x):
    return -(-x.numerator * S // x.denominator)

class R:
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi):
        if not lo <= hi:
            raise RuntimeError('Exact check failed at original line 20')
        self.lo, self.hi = (lo, hi)

    @staticmethod
    def rational(x):
        x = F(x)
        return R(down(x), up(x))

    @staticmethod
    def endpoints(a, b):
        return R(down(F(a)), up(F(b)))

    def __add__(x, y):
        if not isinstance(y, R):
            y = R.rational(y)
        return R(x.lo + y.lo, x.hi + y.hi)
    __radd__ = __add__

    def __neg__(x):
        return R(-x.hi, -x.lo)

    def __sub__(x, y):
        return x + -y

    def __rsub__(x, y):
        return -x + y

    def __mul__(x, y):
        if not isinstance(y, R):
            y = R.rational(y)
        corners = [x.lo * y.lo, x.lo * y.hi, x.hi * y.lo, x.hi * y.hi]
        return R(min(corners) // S, -(-max(corners) // S))
    __rmul__ = __mul__

    def reciprocal(x):
        if not (x.lo > 0 or x.hi < 0):
            raise RuntimeError('zero in divisor')
        a, b = (F(S, x.hi), F(S, x.lo))
        return R.endpoints(a, b)

    def __truediv__(x, y):
        if not isinstance(y, R):
            y = R.rational(y)
        return x * y.reciprocal()

    def square(x):
        lower = 0 if x.lo <= 0 <= x.hi else min(x.lo * x.lo, x.hi * x.hi)
        return R(lower // S, -(-max(x.lo * x.lo, x.hi * x.hi) // S))

    def sign(x):
        if not (x.lo > 0 or x.hi < 0):
            raise RuntimeError('uncertain sign')
        return 1 if x.lo > 0 else -1

    def contains_zero(x):
        return x.lo <= 0 <= x.hi

    def serial(x):
        return [str(x.lo), str(x.hi)]

class Z:
    __slots__ = ('re', 'im')

    def __init__(x, re=0, im=0):
        x.re = re if isinstance(re, R) else R.rational(re)
        x.im = im if isinstance(im, R) else R.rational(im)

    def __add__(x, y):
        return Z(x.re + y.re, x.im + y.im)

    def __neg__(x):
        return Z(-x.re, -x.im)

    def __sub__(x, y):
        return x + -y

    def __mul__(x, y):
        return Z(x.re * y.re - x.im * y.im, x.re * y.im + x.im * y.re)

    def conjugate(x):
        return Z(x.re, -x.im)

    def __truediv__(x, y):
        denom = y.re.square() + y.im.square()
        if not denom.lo > 0:
            raise RuntimeError('Exact check failed at original line 66')
        num = x * y.conjugate()
        return Z(num.re / denom, num.im / denom)

    def nonzero(x):
        return not (x.re.contains_zero() and x.im.contains_zero())

    def serial(x):
        return {'real': x.re.serial(), 'imag': x.im.serial()}

def rational_atan(inv):
    s = F(0)
    k = 0
    while True:
        term = F((-1) ** k, (2 * k + 1) * inv ** (2 * k + 1))
        s += term
        k += 1
        nextterm = F((-1) ** k, (2 * k + 1) * inv ** (2 * k + 1))
        if abs(nextterm) < F(1, 100 * S):
            return (min(s, s + nextterm), max(s, s + nextterm), k)

def make_grid(n):
    a, b, ka = rational_atan(2)
    c, d, kb = rational_atan(3)
    pi = R.endpoints(4 * (a + c), 4 * (b + d))
    if not 3 * S < pi.lo < pi.hi < 4 * S:
        raise RuntimeError('Exact check failed at original line 84')
    degree = 2
    while F(4 ** (degree + 1), factorial(degree + 1)) > F(1, 100 * S):
        degree += 2

    def horner(coeff, x2):
        val = R.rational(coeff[-1])
        for c in reversed(coeff[:-1]):
            val = val * x2 + R.rational(c)
        return val
    coscoeff = [F((-1) ** k, factorial(2 * k)) for k in range(degree // 2 + 1)]
    sincoeff = [F((-1) ** k, factorial(2 * k + 1)) for k in range(degree // 2 + 1)]
    tail = F(4 ** (degree + 1), factorial(degree + 1))
    if not F(4 ** (degree + 2), factorial(degree + 2)) <= tail:
        raise RuntimeError('Exact check failed at original line 94')
    err = R.endpoints(-tail, tail)
    grid = []
    for j in range(n):
        j = j if j <= n // 2 else j - n
        if not j:
            grid.append(Z(1))
            continue
        x = pi * F(2 * j, n)
        xx = x.square()
        grid.append(Z(horner(coscoeff, xx) + err, x * horner(sincoeff, xx) + err))
    return (grid, pi, {'pi_atan_terms': [ka, kb], 'cos_degree': degree, 'scale_decimal_digits': DIGITS})

def model_chains(n, grid):
    h = (n + 1) // 2
    rr = [(1 - grid[7 * x % n].re) * (1 + grid[x].re) for x in range(n)]
    diagonal = [grid[7 * x % n].re + rr[x] * F(1, 10) + rr[x] * grid[x].im * F(1, 100) - F(1, 10) for x in range(n)]
    starts = [x for x in range(n) if 7 * ((x - 1 + h) % n) % n == 0]
    chains = []
    for x in starts:
        inds = [(x + j) % n for j in range(n // 7)]
        ds = [diagonal[j] for j in inds]
        bs = [rr[(j + h) % n] * F(1, 200) for j in inds[:-1]]
        if not all((b.lo > 0 for b in bs)):
            raise RuntimeError('Exact check failed at original line 113')
        chains.append((inds, ds, bs))
    if not sorted((j for inds, _, _ in chains for j in inds)) == list(range(n)):
        raise RuntimeError('Exact check failed at original line 115')
    return chains

def inertia(ds, bs, q):
    pivot = ds[0] - q
    count = int(pivot.sign() < 0)
    for j, b in enumerate(bs, 1):
        pivot = ds[j] - q - b.square() / pivot
        count += int(pivot.sign() < 0)
    return count

def reverse_vector(ds, bs, lam):
    vs = [R.rational(1)]
    if len(ds) > 1:
        vs.append((lam - ds[-1]) / bs[-1])
    for j in range(len(ds) - 2, 0, -1):
        vs.append(((lam - ds[j]) * vs[-1] - bs[j] * vs[-2]) / bs[j - 1])
    vs.reverse()
    return vs

def check_one(path):
    started = time.time()
    data = json.loads(path.read_text())
    n = data['N']
    binary = 1 << data['precision_bits']
    if not n in [21, 35, 49, 63]:
        raise RuntimeError('Exact check failed at original line 136')
    grid, pi, params = make_grid(n)
    chs = model_chains(n, grid)
    byinds = {tuple(inds): (ds, bs) for inds, ds, bs in chs}
    if not set(byinds) == {tuple(x) for x in data['chain_indices']}:
        raise RuntimeError('Exact check failed at original line 140')
    ordered = []
    seen = set()
    vectors = []
    lohi = []
    eta = (F(-3, 5), F(4, 5))
    phase = [(F(1), F(0))]
    for j in range(1, n // 7):
        a, b = phase[-1]
        c, d = eta
        phase.append((a * c - b * d, a * d + b * c))
    for root in data['ordered_roots']:
        lo, hi = [F(int(z), binary) for z in root['interval']]
        if not (lo < hi and hi - lo <= F(1, 1 << data['root_target_bits'])):
            raise RuntimeError('Exact check failed at original line 147')
        ci, k = (root['chain'], root['chain_root_ascending'])
        if not (ci, k) not in seen:
            raise RuntimeError('Exact check failed at original line 148')
        seen.add((ci, k))
        inds = tuple(data['chain_indices'][ci])
        ds, bs = byinds[inds]
        if not inertia(ds, bs, R.rational(lo)) == k:
            raise RuntimeError('Exact check failed at original line 150')
        if not inertia(ds, bs, R.rational(hi)) == k + 1:
            raise RuntimeError('Exact check failed at original line 151')
        ordered.append((ci, k))
        lohi.append((lo, hi))
        vv = reverse_vector(ds, bs, R.endpoints(lo, hi))
        if not ((ds[0] - R.endpoints(lo, hi)) * vv[0] + bs[0] * vv[1]).contains_zero():
            raise RuntimeError('Exact check failed at original line 154')
        vectors.append([(x, Z(v * R.rational(phase[j][0]), v * R.rational(phase[j][1]))) for j, (x, v) in enumerate(zip(inds, vv))])
    if not (len(seen) == n and seen == {(i, k) for i in range(7) for k in range(n // 7)}):
        raise RuntimeError('Exact check failed at original line 156')
    if not all((lohi[j][0] > lohi[j + 1][1] for j in range(n - 1))):
        raise RuntimeError('Exact check failed at original line 157')
    chirp = [grid[-3 * pow(8, -1, n) * x * x % n] for x in range(n)]
    G = [[chirp[x] * grid[pow(4, -1, n) * x * y % n] * chirp[y] for y in range(n)] for x in range(n)]
    H = []
    for left in vectors:
        row = []
        for right in vectors:
            z = Z()
            for x, v in left:
                for y, w in right:
                    z = z + v.conjugate() * G[x][y] * w
            row.append(z)
        H.append(row)
    pivots = []
    for k in range(n):
        p = H[k][k]
        if not p.nonzero():
            raise RuntimeError(f'Uncertain independent pivot {n}:{k + 1}')
        pivots.append(p.serial())
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                H[i][j] = H[i][j] - H[i][k] * H[k][j] / p
    return {'N': n, 'status': 'independently passed', 'validated_root_intervals': len(seen), 'strictly_decreasing': True, 'all_leading_pivots_nonzero': True, 'pivots_reverse_normalized': pivots, 'root_source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'parameters': params, 'pi': pi.serial(), 'runtime_seconds': time.time() - started}

def run(inputs):
    return [check_one(inputs / f'N{n}.json') for n in [21, 35, 49, 63]]
