#!/usr/bin/env python3
"""Exact witnesses and cohomology tests for temporal_resonance.tex.

Quad arithmetic uses integers only. Fourier coefficients are Gaussian integers;
bracket() returns {f,h}/(4*pi**2), so stored Gram matrices equal G/pi**2.
No files are written unless --output or --replay is supplied.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from dataclasses import dataclass
from functools import total_ordering, lru_cache
import hashlib
import json
from pathlib import Path
import random

Vec = tuple[int, int]
Mat = tuple[int, int, int, int]
GI = tuple[int, int]
Fourier = dict[Vec, GI]

@total_ordering
@dataclass(frozen=True, eq=False)
class Quad:
    a: int
    b: int
    d: int
    def lift(self, other):
        if isinstance(other, int): return Quad(other, 0, self.d)
        if not isinstance(other, Quad) or self.d != other.d:
            raise TypeError('Incompatible quadratic fields')
        return other
    def __add__(self, other):
        o = self.lift(other); return Quad(self.a+o.a, self.b+o.b, self.d)
    __radd__ = __add__
    def __neg__(self): return Quad(-self.a, -self.b, self.d)
    def __sub__(self, other): return self + (-self.lift(other))
    def __rsub__(self, other): return self.lift(other) - self
    def __mul__(self, other):
        o = self.lift(other)
        return Quad(self.a*o.a+self.d*self.b*o.b, self.a*o.b+self.b*o.a, self.d)
    __rmul__ = __mul__
    def __pow__(self, n):
        if not isinstance(n, int) or n < 0: raise ValueError('Nonnegative exponent required')
        x, y = self, Quad(1, 0, self.d)
        while n:
            if n & 1: y = y*x
            x = x*x; n //= 2
        return y
    def sign(self):
        sg = lambda x: (x > 0)-(x < 0)
        if self.b == 0: return sg(self.a)
        if self.a == 0: return sg(self.b)
        if sg(self.a) == sg(self.b): return sg(self.a)
        return sg(self.a)*sg(self.a*self.a-self.d*self.b*self.b)
    def __abs__(self): return self if self.sign() >= 0 else -self
    def __eq__(self, other):
        try: return (self-self.lift(other)).sign() == 0
        except TypeError: return False
    def __lt__(self, other): return (self-self.lift(other)).sign() < 0

def mv(a: Mat, v: Vec) -> Vec: return (a[0]*v[0]+a[1]*v[1], a[2]*v[0]+a[3]*v[1])
def mm(a: Mat, b: Mat) -> Mat:
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])
def inv(a: Mat) -> Mat: return (a[3], -a[1], -a[2], a[0])
def power(a: Mat, n: int) -> Mat:
    if n < 0: return power(inv(a), -n)
    b = (1, 0, 0, 1)
    while n:
        if n & 1: b = mm(b, a)
        a = mm(a, a); n //= 2
    return b

def add(u: Vec, v: Vec) -> Vec: return (u[0]+v[0], u[1]+v[1])
def neg(v: Vec) -> Vec: return (-v[0], -v[1])
def det(u: Vec, v: Vec) -> int: return u[0]*v[1]-u[1]*v[0]

def geometry(a: Mat):
    if a[0]*a[3]-a[1]*a[2] != 1 or abs(a[0]+a[3]) < 3:
        raise ValueError('A must be hyperbolic in SL(2,Z)')
    t = abs(a[0]+a[3]); s = 1 if a[0]+a[3] > 0 else -1
    b = tuple(s*x for x in a); d = t*t-4
    xi = lambda v: Quad(2*b[2]*v[0]+(t-2*b[0])*v[1], v[1], d)
    eta = lambda v: Quad(2*b[2]*v[0]+(t-2*b[0])*v[1], -v[1], d)
    return s, b, Quad(t, 1, d), xi, eta

def witness(a: Mat, support: list[Vec], r: int) -> tuple[Vec, Vec]:
    vset = set(support)
    if r < 1 or not vset or (0, 0) in vset or any(neg(v) not in vset for v in vset):
        raise ValueError('Positive lag and nonempty centrally symmetric nonzero support required')
    s, b, lam2, xi, eta = geometry(a)
    vx = max(vset, key=xi); uy = max(vset, key=eta)
    x, y = xi(vx), eta(uy)
    sig = 1 if (y*xi(uy)+x*eta(vx)).sign() >= 0 else -1
    l = lambda z: (2**r)*y*xi(z)+sig*(lam2**r)*x*eta(z)
    key = lambda z: (l(z), xi(z))
    u = max(vset, key=key)
    br = power(b, r); w = max(vset, key=lambda z: key(mv(br, z)))
    return u, (s**r*w[0], s**r*w[1])

def check_witness(a: Mat, support: list[Vec], r: int, u: Vec, v: Vec) -> int:
    """Independent checker: no exposing functional and no finite orbit cutoff."""
    vset = set(support)
    if len(vset) != len(support) or not vset or (0, 0) in vset:
        raise ValueError('Bad support')
    if any(neg(w) not in vset for w in vset) or u not in vset or v not in vset:
        raise ValueError('Bad symmetry or witness membership')
    _, _, lam2, xi, eta = geometry(a)
    if r < 1: raise ValueError('Bad lag')
    ar = power(a, r); av = mv(ar, v); k = add(u, av); d = det(u, av)
    if d == 0: raise ValueError('Zero determinant')
    for j in range(1, r+1):
        aj = power(a, j)
        count = sum(add(p, mv(aj, q)) == k for p in support for q in support)
        if count != (1 if j == r else 0): raise ValueError('Decomposition or lower-lag collision')
    x, y = max(abs(xi(w)) for w in support), max(abs(eta(w)) for w in support)
    if not lam2*(2**r)*abs(xi(k)) > 2*(2**r+lam2**r)*x:
        raise ValueError('Forward all-time escape failed')
    if not lam2**2*abs(eta(k)) > (2*lam2+4)*y:
        raise ValueError('Backward all-time escape failed')
    return d

def ga(z: GI, w: GI) -> GI: return (z[0]+w[0], z[1]+w[1])
def gm(z: GI, w: GI) -> GI: return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def gc(z: GI) -> GI: return (z[0], -z[1])
def norm(z: GI) -> int: return z[0]*z[0]+z[1]*z[1]
def accumulate(out: Fourier, key: Vec, value: GI) -> None:
    z = ga(out.get(key, (0, 0)), value)
    if z == (0, 0): out.pop(key, None)
    else: out[key] = z

def combine(items) -> Fourier:
    out: Fourier = {}
    for c, f in items:
        for k, z in f.items(): accumulate(out, k, (c*z[0], c*z[1]))
    return out

def transport(a: Mat, f: Fourier, j: int) -> Fourier:
    aj = power(a, j); return {mv(aj, k): z for k, z in f.items()}
def bracket(f: Fourier, h: Fourier) -> Fourier:
    out: Fourier = {}
    for u, z in f.items():
        for v, w in h.items():
            d = -det(u, v); c = gm(z, w)
            accumulate(out, add(u, v), (d*c[0], d*c[1]))
    return out

@lru_cache(maxsize=200000)
def orbit_key(a: Mat, k: Vec) -> Vec:
    if k == (0, 0): raise ValueError('Zero orbit')
    _, _, lam2, xi, _ = geometry(a)
    while abs(xi(k)) < 1: k = mv(a, k)
    while 2*abs(xi(k)) >= lam2: k = mv(inv(a), k)
    return k

def orbit_sums(a: Mat, f: Fourier) -> Fourier:
    out: Fourier = {}
    for k, z in f.items(): accumulate(out, orbit_key(a, k), z)
    return out

def filter_apply(a: Mat, g: Fourier, p: list[int]) -> Fourier:
    return combine((c, transport(a, g, j)) for j, c in enumerate(p))
def filter_residue(p: list[int], q: list[int]) -> list[int]:
    n = max(len(p), len(q)); p = p+[0]*(n-len(p)); q = q+[0]*(n-len(q))
    return [sum(p[i]*q[i+r]-q[i]*p[i+r] for i in range(n-r)) for r in range(1, n)]
def autocorrelation(p: list[int]) -> list[int]:
    return [sum(p[i]*p[i+r] for i in range(len(p)-r)) for r in range(len(p))]

def determinant(m: list[list[int]]) -> int:
    """Fraction-free elimination; the tested matrices are positive definite."""
    b = [row[:] for row in m]; previous = 1
    if not b: return 1
    for k in range(len(b)-1):
        pivot = b[k][k]
        if pivot == 0: raise ValueError('Zero Bareiss pivot')
        for i in range(k+1, len(b)):
            for j in range(k+1, len(b)):
                numerator = pivot*b[i][j]-b[i][k]*b[k][j]
                if numerator % previous: raise ArithmeticError('Nonintegral Bareiss quotient')
                b[i][j] = numerator//previous
        previous = pivot
    return b[-1][-1]

def algebra_checks(a: Mat, support: list[Vec], rng: random.Random) -> dict:
    g: Fourier = {}
    for v in sorted(set(support)):
        if v in g: continue
        z = (rng.randint(1, 5), rng.randint(-4, 4)); g[v] = z; g[neg(v)] = gc(z)
    m = 4; h = [bracket(g, transport(a, g, r)) for r in range(1, m+1)]
    rows = [orbit_sums(a, f) for f in h]
    gram = [[sum(gm(z, gc(rows[j].get(k, (0, 0))))[0] for k, z in rows[i].items())
             for j in range(m)] for i in range(m)]
    for j in range(1, m+1): assert determinant([r[:j] for r in gram[:j]]) > 0
    lower = 1
    for r in range(1, m+1):
        u, v = witness(a, support, r); d = check_witness(a, support, r, u, v)
        lower *= 2*d*d*norm(g[u])*norm(g[v])
    gd = determinant(gram); assert gd >= lower
    c = {(i, j): rng.randint(-3, 3) for i in range(m+1) for j in range(i+1, m+1)}
    H = combine((v, bracket(transport(a, g, i), transport(a, g, j))) for (i, j), v in c.items())
    ar = [sum(c[i, i+r] for i in range(m-r+1)) for r in range(1, m+1)]
    reduced = combine(zip(ar, h))
    F = combine((c[i, i+r], transport(a, h[r-1], l))
                for r in range(1, m+1) for i in range(m-r+1) for l in range(i))
    assert H == combine([(1, reduced), (1, transport(a, F, 1)), (-1, F)])
    assert orbit_sums(a, H) == orbit_sums(a, reduced)
    for _ in range(4):
        p = [rng.randint(-3, 3) for _ in range(5)]
        q = [rng.randint(-3, 3) for _ in range(5)]
        lhs = orbit_sums(a, bracket(filter_apply(a, g, p), filter_apply(a, g, q)))
        residue = filter_residue(p, q)
        assert lhs == orbit_sums(a, combine(zip(residue, h)))
        assert bool(lhs) == any(residue)
    special = bracket(transport(a, g, 1), combine([(1, g), (1, transport(a, g, 2))]))
    assert special and not orbit_sums(a, special)
    p, q = [1, 5, 6], [2, 7, 3]
    assert autocorrelation(p) == autocorrelation(q) == [62, 35, 6]
    hp = bracket(filter_apply(a, g, p), transport(a, filter_apply(a, g, p), 1))
    hq = bracket(filter_apply(a, g, q), transport(a, filter_apply(a, g, q), 1))
    assert orbit_sums(a, hp) == orbit_sums(a, hq)
    assert orbit_sums(a, hp) == orbit_sums(a, combine(zip([56, 35, 6], h)))
    return {'A': a, 'support': support, 'gram_over_pi_squared': gram,
            'determinant_over_pi_power': gd, 'isolated_minor_lower_bound': lower}

def matrices() -> list[Mat]:
    out = []
    for t in [3, 4, 6, 11, 25]:
        for n in [-5, -1, 0, 2, 7]:
            p = (1, n, 0, 1); a = mm(mm(p, (t, -1, 1, 0)), inv(p))
            out.extend([a, tuple(-x for x in a)])
    return out+[(3, 2, 4, 3), (2, 1, 1, 1), (-2, -1, -1, -1)]

def main() -> None:
    if not __debug__: raise RuntimeError('Do not run verification with python -O')
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cases', type=int, default=30)
    ap.add_argument('--max-lag', type=int, default=5)
    ap.add_argument('--algebra-cases', type=int, default=8)
    ap.add_argument('--seed', type=int, default=20260906)
    ap.add_argument('--output', type=Path)
    ap.add_argument('--replay', type=Path)
    args = ap.parse_args()
    if min(args.cases, args.max_lag, args.algebra_cases) < 1: ap.error('Positive counts required')
    rng = random.Random(args.seed); mats = matrices(); records = []; algebra = []
    for case in range(args.cases):
        a = mats[case % len(mats)]
        if case % 10 == 0: support = [(6, 1), (-6, -1)]
        elif case % 10 == 1:
            support = [(x, y) for x in range(-2, 3) for y in range(-2, 3) if (x, y) != (0, 0)]
        else:
            vset = set()
            for _ in range(rng.randint(2, 11)):
                v = (rng.randint(-20, 20), rng.randint(-20, 20))
                if v != (0, 0): vset.update([v, neg(v)])
            support = sorted(vset) or [(1, 0), (-1, 0)]
        support = sorted(support)
        for r in range(1, args.max_lag+1):
            u, v = witness(a, support, r); check_witness(a, support, r, u, v)
            records.append((a, r, support, u, v))
        if case < args.algebra_cases: algebra.append(algebra_checks(a, support, rng))
    for a in [(1, 0, 0, 1), (1, 1, 0, 1), (2, 0, 0, 1)]:
        try: geometry(a)
        except ValueError: pass
        else: raise AssertionError('Bad matrix accepted')
    a, r, support, u, v = records[0]
    try: check_witness(a, support, r, (0, 0), v)
    except ValueError: pass
    else: raise AssertionError('Tampered witness accepted')
    lines = [str(len(records))]
    for a, r, support, u, v in records:
        lines.append(' '.join(map(str, (*a, r, len(support), *u, *v))))
        lines.extend(f'{x} {y}' for x, y in support)
    replay = ('\n'.join(lines)+'\n').encode()
    if args.replay:
        args.replay.parent.mkdir(parents=True, exist_ok=True); args.replay.write_bytes(replay)
    result = {'status': 'PASS', 'scope': 'finite exact regression, not a proof by enumeration',
              'seed': args.seed, 'matrices_available': len(mats), 'supports': args.cases,
              'witnesses': len(records), 'maximum_lag': args.max_lag,
              'exact_gram_cases': len(algebra), 'random_filter_comparisons': 4*len(algebra),
              'nonzero_coboundary_examples': len(algebra), 'homometric_filter_examples': len(algebra),
              'negative_controls': 4, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'replay_sha256': hashlib.sha256(replay).hexdigest(), 'anchors': algebra[:2]}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'anchors'}, indent=2))

if __name__ == '__main__': main()
