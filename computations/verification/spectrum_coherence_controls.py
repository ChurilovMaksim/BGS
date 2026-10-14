#!/usr/bin/env python3
"""Exact finite controls for TRACE-081/082, not their asymptotic proof.

Integers and SymPy rational/Gaussian-rational matrices. No floating-point
eigensolver, statistical sampling, or generic-discriminant certification.
The output is printed unless --output explicitly names a result artifact.
"""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import platform
import sympy as s

ROOT = Path(__file__).resolve().parents[2]


def zero(a):
    return all(s.expand(x) == 0 for x in a)


def gauss_controls():
    cases = []
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        assert s.isprime(p)
        for d in range(p):
            pairs = {((b-c) % p, (b+c+d) % p)
                     for b in range(p) for c in range(p)}
            assert len(pairs) == p*p
            counts = Counter((b*b-c*c+d*(b-c)) % p
                             for b in range(p) for c in range(p))
            assert counts[0] == 2*p-1
            assert all(counts[a] == p-1 for a in range(1, p))
        for q in range(1, p):
            counts = Counter(q*(b*b-c*c) % p
                             for b in range(p) for c in range(p))
            assert counts[0] == 2*p-1
            assert all(counts[a] == p-1 for a in range(1, p))
        cases.append({'prime': p, 'all_linear_offsets': p,
                      'nonzero_quadratic_coefficients': p-1})
    return cases


def tensor_controls():
    multiplicities = Counter({0: 1})
    cases = []
    c1, c2 = (2, 1, -1, -2, -1, 1), (2, -1, -1, 2, -1, -1)
    for k in range(1, 17):
        new = Counter()
        for r, count in multiplicities.items():
            for q in (0, 2, 3, 4):
                new[(r+q) % 6] += count
        multiplicities = new
        numerators = [4**k+(-1)**k*c1[r]+c2[r]+2**k*(-1)**r
                      for r in range(6)]
        assert all(x % 6 == 0 for x in numerators)
        assert [multiplicities[r] for r in range(6)] == [x//6 for x in numerators]
        assert sum(multiplicities.values()) == 4**k
        cases.append({'k': k, 'dimension': 4**k,
                      'multiplicities': [multiplicities[r] for r in range(6)]})
    return cases


def discriminant_controls():
    lam = s.Symbol('lambda')
    cases = []
    matrices = [s.eye(1), s.Matrix([[1, 1], [0, 1]]),
                s.Matrix([[0, 1], [1, 0]]),
                s.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])]
    for a in matrices:
        n = a.rows
        z = s.symbols('z:'+str(n))
        polynomial = (lam*s.eye(n)-a*s.diag(*z)).det()
        discriminant = s.factor(s.discriminant(polynomial, lam))
        assert a.det() != 0 and discriminant != 0
        cases.append({'matrix': str(a.tolist()), 'discriminant': str(discriminant)})
    assert s.discriminant(lam**2, lam) == 0
    return cases


def memory_controls(u):
    n = u.rows
    assert zero(u.H*u-s.eye(n))
    t = s.Matrix(n*n, n*n,
                 lambda a, b: s.expand(u[a//n, b//n]*s.conjugate(u[a % n, b % n])))
    assert zero(t.H*t-s.eye(n*n))
    diagonal = [j*n+j for j in range(n)]
    off = [j for j in range(n*n) if j not in diagonal]
    p, e = t.extract(diagonal, diagonal), t.extract(off, off)
    ell, c = t.extract(diagonal, off), t.extract(off, diagonal)
    assert p == s.ones(n)/n
    z = s.Rational(1, 5)
    direct = (s.eye(n*n)-z*t).inv().extract(diagonal, diagonal)
    schur = (s.eye(n)-z*p-z*z*ell*(s.eye(len(off))-z*e).inv()*c).inv()
    assert zero(direct-schur)
    returns = [(t**j).extract(diagonal, diagonal) for j in range(9)]
    for j in range(8):
        rhs = p*returns[j]
        for a in range(j):
            rhs += ell*e**(j-1-a)*c*returns[a]
        assert zero(returns[j+1]-rhs)
    budgets = []
    for r in range(n):
        gram_defect = s.eye(len(off))-(e**r).H*e**r
        assert gram_defect.rank() < len(off)
        observations = [((t**j).extract(diagonal, off)) for j in range(1, r+1)]
        obs = s.Matrix.vstack(*observations) if observations else s.zeros(0, len(off))
        nullity = len(off)-obs.rank()
        budget = (n-1)*(n-r)
        assert nullity >= budget > 0
        budgets.append({'r': r, 'observability_nullity': nullity, 'lower_bound': budget})
    return {'dimension': n, 'resolvent_parameter': str(z),
            'exact_return_recurrences': 8, 'plateau_and_dimension': budgets}, (e, ell, c, returns)


def run():
    w = s.Matrix([[1, 1, 1, 1], [1, -1, -1, 1],
                  [1, 1, -1, -1], [1, -1, 1, -1]])
    h = w/2
    assert w*w.T == 4*s.eye(4) and h**6 == s.eye(4)
    reversal = s.Matrix(4, 4, lambda i, j: h[i, j]*h[j, i])
    assert reversal*reversal.T == s.eye(4)/4
    core, (_, _, _, ret) = memory_controls(h)
    assert ret[6] == s.eye(4)
    # A rational SU(2) rotation gives a sharp endpoint witness at r=N=2.
    qubit = s.Matrix([[1-s.I, -1-s.I], [1-s.I, 1+s.I]])/2
    boundary, (e, ell, c, ret) = memory_controls(qubit)
    assert e != s.zeros(2) and e**2 == s.zeros(2)
    assert zero(ell*c) and ell*e*c == s.eye(2)-s.ones(2)/2
    assert ret[3] == s.eye(2)
    hashes = {}
    for name in ('flat_spectrum_obstruction_20261014.md', 'coherence_memory_plateau_20261014.md'):
        path = ROOT/'mathematics'/name
        hashes[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return {'status': 'pass', 'python': platform.python_version(), 'sympy': s.__version__,
            'arithmetic': 'integers, rational and Gaussian-rational exact algebra',
            'scope': 'finite core, finite Gauss/discriminant controls, exact memory identities and endpoint witness; not generic/asymptotic/BGS proof',
            'source_sha256': hashes, 'gauss': gauss_controls(), 'tensor': tensor_controls(),
            'discriminants': discriminant_controls(), 'memory': [core, boundary],
            'endpoint_witness': 'N=2: E nonzero, E^2=0, LC=0, LEC=I-J, return at time 3'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    payload = json.dumps(run(), indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(payload)
    print(payload, end='')


if __name__ == '__main__':
    main()
